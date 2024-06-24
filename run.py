import os

directory = '/Users/sumanthpagadala/Desktop/House_Satt_Dataset/Train'

image_files = []
json_files = []

for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_files.append(os.path.splitext(filename)[0])
    elif filename.endswith('.json'):
        json_files.append(os.path.splitext(filename)[0])

image_set = set(image_files)
json_set = set(json_files)

extra_json_files = json_set - image_set

print("Extra JSON files:", extra_json_files)




