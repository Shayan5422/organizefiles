import os
import shutil
from tkinter import Tk, filedialog

def get_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    root.destroy()
    return file_path


file_path = get_file_path()



def sort_files_by_extension(source_dir, destination_dir):

    categories = {
        'png': os.path.join(destination_dir, 'image'),
        'jpg': os.path.join(destination_dir, 'image'),
        'jpeg': os.path.join(destination_dir, 'image'),
        'psd': os.path.join(destination_dir, 'image'),
        'mp4': os.path.join(destination_dir, 'video'),
        'mov': os.path.join(destination_dir, 'video'),
        'mkv': os.path.join(destination_dir, 'video'),
        'avi': os.path.join(destination_dir, 'video'),
        'flv': os.path.join(destination_dir, 'video'),
        'doc': os.path.join(destination_dir, 'documents'),
        'docx': os.path.join(destination_dir, 'documents'),
        'pdf': os.path.join(destination_dir, 'documents'),
        'xlsx': os.path.join(destination_dir, 'documents'),
        'xls': os.path.join(destination_dir, 'documents'),
        'zip': os.path.join(destination_dir, 'zip'),
        'rar': os.path.join(destination_dir, 'zip'),
        '7z': os.path.join(destination_dir, 'zip'),
        'mp3': os.path.join(destination_dir, 'audio'),
        'wav': os.path.join(destination_dir, 'audio'),
        'flac': os.path.join(destination_dir, 'audio'),
        'ogg': os.path.join(destination_dir, 'audio'),
        'py': os.path.join(destination_dir, 'python'),
        'other': os.path.join(destination_dir, 'other')
    }

    for category in categories.values():
        if not os.path.exists(category):
            os.makedirs(category)


    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)


        if os.path.isfile(source_file):

            file_extension = os.path.splitext(filename)[1][1:]


            if file_extension in categories:
                destination_folder = categories[file_extension]
            else:
                destination_folder = categories['other']

            shutil.move(source_file, destination_folder)


sort_files_by_extension(file_path, file_path)
