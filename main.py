from utils import *
import cv2

path = f"{os.getcwd()}/images/annotation_files"
downloaded_files_folder_path = f"{os.getcwd()}/images/downloaded_files"
treated_images_folder_path = f"{os.getcwd()}/images/treated_images"

annotation_data = get_annotation_data(path)

naming_root = "SUB-IMG-"
i = 0
for _annotation_file in annotation_data:
    annotation_file = _annotation_file[0]
    file_name = annotation_file["image"]
    downloaded_file_path = f"{downloaded_files_folder_path}/{file_name}"
    print(downloaded_file_path)
    downloaded_image = cv2.imread(downloaded_file_path)
    if downloaded_image is None:
        continue
    for sub_image_data in annotation_file["annotations"]:
        coordinates = sub_image_data["coordinates"]
        width = int(coordinates["width"])
        height = int(coordinates["height"])
        x = int(coordinates["x"] - width/2)
        y = int(coordinates["y"] - height/2)

        sub_downloaded_image = downloaded_image[x:x+width,y:y+height]
        sub_image_name = f"{naming_root}{i}"
        path = f"{treated_images_folder_path}/{sub_image_name}.jpg"
        # print("test")
        # print(coordinates)
        # print(downloaded_file_path)
        # print(sub_downloaded_image)
        # print(path)
        if len(sub_downloaded_image) == 0:
            continue
        cv2.imwrite(path , sub_downloaded_image)
        i += 1

