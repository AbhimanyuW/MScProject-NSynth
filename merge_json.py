import json

# Function to recursively merge two dictionaries
def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            merge_dicts(dict1[key], dict2[key])
        else:
            dict1[key] = value

# Read the three JSON files
with open('/Users/abhimanyuwadhwa/Desktop/QMUL/MScProject/DataSet/examples-test-original.json', 'r') as file:
    data1 = json.load(file)

with open('/Users/abhimanyuwadhwa/Desktop/QMUL/MScProject/DataSet/examples-train-original.json', 'r') as file:
    data2 = json.load(file)

with open('/Users/abhimanyuwadhwa/Desktop/QMUL/MScProject/DataSet/examples-valid-original.json', 'r') as file:
    data3 = json.load(file)

# Merge the JSON objects
merged_data = {}

# Merge the dictionaries recursively
print("Merging JSON files...")
merge_dicts(merged_data, data1)
print("1/3 JSON files merged.")
merge_dicts(merged_data, data2)
print("2/3 JSON files merged.")
merge_dicts(merged_data, data3)
print("3/3 JSON files merged.")

# Write the merged JSON data to a new file
with open('merged.json', 'w') as file:
    json.dump(merged_data, file, indent=4)