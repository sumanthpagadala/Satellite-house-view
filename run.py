import os

# Directory containing the images and JSON files
directory = '/Users/sumanthpagadala/Desktop/House_Satt_Dataset/Train'

# Lists to store the filenames without extensions
image_files = []
json_files = []

# Loop through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_files.append(os.path.splitext(filename)[0])
    elif filename.endswith('.json'):
        json_files.append(os.path.splitext(filename)[0])

# Convert lists to sets for easy comparison
image_set = set(image_files)
json_set = set(json_files)

# Find extra JSON files
extra_json_files = json_set - image_set

# Output the extra JSON files
print("Extra JSON files:", extra_json_files)
