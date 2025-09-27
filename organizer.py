import shutil

from pathlib import Path
import itertools

# Path to organize
SOURCE_FOLDER = Path('c:/Users/jr29b/Downloads')

# create destination folders if they dont exist
# for folder in [IMAGES_FOLDER, DOCUMENTS_FOLDER, VIDEOS_FOLDER, OTHERS_FOLDERS]:
#     os.makedirs(folder, exist_ok=True)

 # Define categories and their corresponding extensions
categories = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg", ".app"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}


# creating a function allows me to change the folder and make it a more general tool for any folder
def sort_files_in_a_folder(source):
    '''
        A function to sort the files in a download folder into different categories/directories
    '''

    try:
        for item in source.iterdir():
            if item.is_file(): # Process ony files
                file_extension = item.suffix.lower() # get the file  ex .pdf or .txt

                moved = False
                for category, extensions in categories.items():

                    if file_extension in extensions: # compares current item extension with extensions in category dictionary
                        destination_folder = source / category # use
                        destination_folder.mkdir(exist_ok=True) # Create category if it doesnt exist
                        shutil.move(str(item), str(destination_folder / item.name))
                        print(f"Moved '{item.name}' to '{category}'")
                        moved = True
                        break

                if not moved:
                    other_folder = source / "Others"
                    other_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(other_folder / item.name))
                    print(f"Moved '{item.name}' to 'Others'")

    except FileNotFoundError:
        print(f"Error: the directory '{source}' was not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


sort_files_in_a_folder(SOURCE_FOLDER)