import pandas as pd
import requests
import time
import json
import os

from dotenv import load_dotenv
load_dotenv()

from ratelimit import limits, sleep_and_retry


books_df_path = 'main_dataset/temp_desc_books.csv'
books_df = pd.read_csv(books_df_path)
print(len(books_df))


API_KEY = os.getenv("GBOOKS_API_KEY_BnB")
ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 100
MAX_CALLS_PER_DAY = 1000
BOOKS_DATA_PATH = 'gbooks/books_data_byisbn1.json'
PROGRESS_PATH = 'gbooks/progress_byisbn1.json'


def  get_books_data():
    if os.path.exists(BOOKS_DATA_PATH):
        with open(BOOKS_DATA_PATH, 'r') as f:
            return json.load(f)
    else:
        os.makedirs(os.path.dirname(BOOKS_DATA_PATH), exist_ok=True)
        return []


def get_progress():
    if os.path.exists(PROGRESS_PATH):
        with open(PROGRESS_PATH, 'r') as f:
            return json.load(f)
    else:
        os.makedirs(os.path.dirname(PROGRESS_PATH), exist_ok=True)
        return {}


@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
@limits(calls=MAX_CALLS_PER_DAY, period=24*ONE_MINUTE)
def fetch_book_by_isbn(isbn):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': f'isbn:{isbn}',
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_all_books_by_isbn(existing_data, progress):
    all_books_data = existing_data
    total_requests = 0

    for index, row in books_df.iterrows():
        isbn = row['isbn']
        if isbn in progress:
            continue
        
        try:
            response = fetch_book_by_isbn(isbn)
            total_requests += 1
            if 'items' in response:
                all_books_data.extend(response['items'])
                progress[isbn] = True
            else:
                progress[isbn] = False  # No items found
        except Exception as e:
            print(f"An error occurred for ISBN {isbn}: {e}")
            progress[isbn] = False  # Mark as not found due to error

        print(f"Total requests: {total_requests}")
        if total_requests >= MAX_CALLS_PER_DAY:
            break
        
        time.sleep(ONE_MINUTE / MAX_CALLS_PER_MINUTE)

    return all_books_data, progress


def save_books_data(books_data, filename=BOOKS_DATA_PATH):
    with open(filename, 'w') as f:
        json.dump(books_data, f)


def save_progress(progress, filename=PROGRESS_PATH):
    with open(filename, 'w') as f:
        json.dump(progress, f)


if __name__ == '__main__':
    existing_data = get_books_data()
    progress = get_progress()
    books_data_byisbn, progress_byisbn = fetch_all_books_by_isbn(existing_data, progress)
    save_books_data(books_data_byisbn)
    save_progress(progress_byisbn)

    print(f"Data fetching complete. Total books fetched: {len(books_data_byisbn)}")