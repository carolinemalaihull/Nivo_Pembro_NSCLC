import gzip
import shutil

input_file = "data/GSE126044_series_matrix.txt.gz"
output_file = "data/GSE126044_series_matrix.txt"

with gzip.open(input_file, "rb") as f_in:
    with open(output_file, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Unzipping complete.")