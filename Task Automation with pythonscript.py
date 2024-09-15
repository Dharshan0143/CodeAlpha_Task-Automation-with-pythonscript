import os
import shutil

def organize_files_by_extension(folder_path):
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
    
        if os.path.isdir(file_path):
            continue
        
        file_extension = filename.split('.')[-1]
        extension_folder = os.path.join(folder_path, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
    
        shutil.move(file_path, extension_folder)

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    organize_files_by_extension(folder_to_organize)
    print("Files have been organized by extension.")
