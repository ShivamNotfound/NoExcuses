import json

INPUT_FILE = "data.json"
OUTPUT_FILE = "data_final.json"

REMOVE_MODELS = {
    "contenttypes.contenttype",
    "auth.permission",
    "admin.logentry",
}

with open(INPUT_FILE, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

cleaned_data = [
    obj for obj in data
    if obj["model"].lower() not in REMOVE_MODELS
]

removed = len(data) - len(cleaned_data)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=2)

print(f"Original objects: {len(data)}")
print(f"Removed objects:  {removed}")
print(f"Remaining:        {len(cleaned_data)}")
print(f"Created: {OUTPUT_FILE}")