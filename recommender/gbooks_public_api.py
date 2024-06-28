import pandas as pd
import requests
import time
import json
import os
import sys

from dotenv import load_dotenv
load_dotenv()

from ratelimit import limits, sleep_and_retry


books_df_path = 'main_dataset/temp_desc_books.csv'
books_df = pd.read_csv(books_df_path)
print(len(books_df))


ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 100
MAX_CALLS_PER_DAY = 1000
JSON_COUNTER_PATH = 'gbooks/json_counter.json'
books_data_path = 'gbooks/books_data_byisbn'
PROGRESS_PATH = 'gbooks/progress_byisbn.json'


def  get_json_counter_file():
    if os.path.exists(JSON_COUNTER_PATH):
        with open(JSON_COUNTER_PATH, 'r') as f:
            return json.load(f)
    else:
        os.makedirs(os.path.dirname(JSON_COUNTER_PATH), exist_ok=True)
        return {"counter": 1}
    

def increment_counter():
    json_counter = get_json_counter_file()
    json_counter["counter"] += 1
    with open(JSON_COUNTER_PATH, 'w') as f:
        json.dump(json_counter, f)

def counter_setup():
    global books_data_path
    counter = get_json_counter_file().get("counter", 0)
    books_data_path = books_data_path + "_" + str(counter) + ".json"


def  get_books_data():
    if os.path.exists(books_data_path):
        with open(books_data_path, 'r') as f:
            return json.load(f)
    else:
        os.makedirs(os.path.dirname(books_data_path), exist_ok=True)
        increment_counter()
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
    err_counter = 0

    for index, row in books_df.iterrows():
        isbn = row['isbn']
        if isbn in progress and progress[isbn] != "Error":
            print(f"Skipping ISBN {isbn} because it was found in progress.")
            continue
        
        try:
            response = fetch_book_by_isbn(isbn)
            total_requests += 1
            if 'items' in response:
                all_books_data.extend(response['items'])
                progress[isbn] = True
            else:
                progress[isbn] = False  # No items found
            err_counter = 0
        except Exception as e:
            print(f"An error occurred for ISBN {isbn}: {e}")
            progress[isbn] = "Error"  # Mark as not found due to error
            err_counter += 1
            if err_counter >= 5:
                break

        print(f"Total requests: {total_requests}")
        if total_requests >= MAX_CALLS_PER_DAY:
            break
        
        time.sleep(ONE_MINUTE / MAX_CALLS_PER_MINUTE)

    return all_books_data, progress


def save_books_data(books_data, filename):
    with open(filename, 'w') as f:
        json.dump(books_data, f)


def save_progress(progress, filename):
    with open(filename, 'w') as f:
        json.dump(progress, f)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python gbooks_public_api.py <which GBOOKS_API_KEY?>")
        exit(1)

    API_KEY = os.getenv(str(sys.argv[1]))
    if API_KEY is None:
        print("Usage: python gbooks_public_api.py <valid GBOOKS_API_KEY>")
        exit(1)
    
    counter_setup()
    existing_data = get_books_data()
    progress = get_progress()
    books_data_byisbn, progress_byisbn = fetch_all_books_by_isbn(existing_data, progress)
    save_books_data(books_data_byisbn, books_data_path)
    save_progress(progress_byisbn, PROGRESS_PATH)

    print(f"Data fetching complete. Total books fetched: {len(books_data_byisbn)}")