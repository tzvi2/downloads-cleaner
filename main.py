import os
import shutil

# Prompt user for directory path
source_dir = input("Please enter the path to your downloads folder: ")

# Create a copy of the source directory in the destination directory
dest_dir = source_dir + "_copy"

shutil.copytree(source_dir, dest_dir)

#set file classifications and file types
images = {"jpeg", "jpg", "png", "svg", "gif", "webp"}
audio = {"mp3", "midi", "mid", "wav", "wma"}
video = {"mp4", "wmv", "mov"}
code = {"html", "js", "c", "cpp", "py", "php"}
applications = {"exe", "msi"}
pdf = {"pdf"}
excel = {"xls", "xlsx"}
text = {"doc", "docx", "txt", "rtf"}

# keep track of which file types are present
typesMap = {
    "images": False,
    "audio": False,
    "video": False,
    "code": False,
    "applications": False,
    "pdf": False,
    "excel": False,
    "text": False
}

# detect and mark present file types in source folder
for root, dirs, files in os.walk(str(dest_dir)):
    for file in files:
        file_type = file.split('.')[-1].lower()
        if file_type in images:
            typesMap["images"] = True
        elif file_type in audio:
            typesMap["audio"] = True
        elif file_type in audio:
            typesMap["video"] = True
        elif file_type in code:
            typesMap["code"] = True
        elif file_type in applications:
            typesMap["applications"] = True
        elif file_type in pdf:
            typesMap["pdf"] = True
        elif file_type in excel:
            typesMap["excel"] = True
        elif file_type in text:
            typesMap["text"] = True

# Create a folder for each file type
for k, v in typesMap.items():
    if v:
        os.makedirs(os.path.join(dest_dir, k))

for file in os.listdir(dest_dir):
    file_path = os.path.join(dest_dir, file)
    file_type = file.split(".")[-1]
    if os.path.isfile(file_path):  

        if file_type in applications:
            shutil.move(file_path, dest_dir + "/applications")

        elif file_type in images:
            shutil.move(file_path, dest_dir + "/images")

        elif file_type in audio:
            shutil.move(file_path, dest_dir + "/audio")

        elif file_type in video:
            shutil.move(file_path, dest_dir + "/video")

        elif file_type in code:
            shutil.move(file_path, dest_dir + "/code")

        elif file_type in pdf:
            shutil.move(file_path, dest_dir + "/pdf")

        elif file_type in excel:
            shutil.move(file_path, dest_dir + "/excel")

        elif file_type in text:
            shutil.move(file_path, dest_dir + "/text")

# go through each type-directory in original directory, sort by date then into folders of 10
for dirpath, dirnames, filenames in os.walk(dest_dir):
    # check if there are more than 10 files in inner directory
    if len(filenames) > 10:
        # sort the files by creation time, oldest first
        filenames.sort(key=lambda x: os.path.getctime(os.path.join(dirpath, x)))
        i = 0
        folder_num = 1
        while i < len(filenames):
            subdir_path = os.path.join(dirpath, "Folder " + str(folder_num))
            os.makedirs(subdir_path, exist_ok=True)
            # move 10 files at a time
            for j in range(i, min(i + 10, len(filenames))):
                shutil.move(os.path.join(dirpath, filenames[j]), subdir_path)
            i += 10
            folder_num += 1

print("Your downloads have been successfully organized.")
