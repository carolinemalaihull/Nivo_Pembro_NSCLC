import pandas as pd

file_path = "data/GSE126044_series_matrix.txt"

gsm_ids = []
responses = []

with open(file_path, "r") as f:
    for line in f:

        # GSM IDs
        if line.startswith("!Series_sample_id"):
            gsm_ids = line.strip().split("\t")[1].replace('"', '').split()

        # patient response row
        if line.startswith("!Sample_characteristics_ch1"):
            if "patient response" in line:
                responses = line.strip().split("\t")[1:]
                responses = [r.replace('"', '').strip() for r in responses]

# clean response text
clean_responses = []
for r in responses:
    if "non-responder" in r:
        clean_responses.append("non-responder")
    elif "responder" in r:
        clean_responses.append("responder")
    else:
        clean_responses.append("unknown")

# align safely
n = min(len(gsm_ids), len(clean_responses))

meta = pd.DataFrame({
    "GSM": gsm_ids[:n],
    "response": clean_responses[:n]
})

print(meta)

meta.to_csv("results/sample_metadata.csv", index=False)

print("Clean metadata saved → results/sample_metadata.csv")