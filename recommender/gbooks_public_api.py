import pandas as pd

# Load your existing Kaggle dataset
books_df_path = 'main_dataset/updated_books.csv'
books_df = pd.read_csv(books_df_path)

# Ensure your dataset has the required columns
required_columns = {'isbn', 'avg_rating', 'n_ratings', 'title'}
assert required_columns.issubset(books_df.columns), "Missing required columns in Kaggle dataset"