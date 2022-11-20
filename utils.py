import os 
import json

def get_files_paths(directory_path):
    _directory = directory_path
    entries = os.walk(_directory) 
    file_list = []
    for entry in entries:
        file_list += [os.path.join(f"{entry[0]}/", file) for file in entry[2]]
    return file_list

def load_json_data(file_path):
    with open(file_path) as f:
        return json.load(f)

def get_annotation_data(directory_path):
    annotation_files = []
    files_paths = get_files_paths(directory_path)
    for file_path in files_paths:
        if os.path.split(file_path)[1].endswith(".json") :
            file_content = load_json_data(file_path)
            annotation_files.append(file_content)
    return annotation_files

# def crop_image(image_name, coordinates):
#     image_path = os.path.join(os.getcwd(), downloaded_files_directory, image_name)
#     img = cv2.imread(image_path)
#     if img is None:
#         return None
#     width = int(coordinates["width"])
#     height = int(coordinates["height"])
#     left = int(coordinates["x"] - width / 2)
#     top = int(coordinates["y"] - height / 2)
    
#     img = img[top:top+height, left:left+width]

#     return img