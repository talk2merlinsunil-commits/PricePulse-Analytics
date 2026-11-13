
import gzip
import shutil
import os

source = "dataset/cleaned_food_prices.csv"
destination = "dataset/cleaned_food_prices.csv.gz"

with open(source, "rb") as f_in:
    with gzip.open(destination, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

size = os.path.getsize(destination) / (1024 * 1024)

print(f"Compressed file size: {size:.2f} MB")
