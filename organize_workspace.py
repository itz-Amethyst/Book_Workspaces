import os
import shutil
import argparse

SUPPORTED_LANGUAGES = ['js', 'py', 'rs', 'java', 'cpp', 'c', 'h', 'html', 'css', 'php', 'swift', 'go', 'rb', 'sh', 'pl', 'lua', 'ts', 'dart']

def create_directory_structure_for_file(file_path, book_directory):
    file_name = os.path.basename(file_path)
    file_name_no_ext, file_ext = os.path.splitext(file_name)
    file_ext = file_ext.lstrip('.')

    
    new_directory = os.path.join(book_directory, file_name_no_ext, file_ext)
    os.makedirs(new_directory, exist_ok=True)
    
    new_file_path = os.path.join(new_directory, file_name)
    shutil.move(file_path, new_file_path)
    print(f"Moved '{file_path}' to '{new_file_path}'")

def process_files_in_directory(book_directory):
    current_script = os.path.realpath(__file__)

    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path) and file_path != current_script:
            _, file_ext = os.path.splitext(file_path)
            file_ext = file_ext.lstrip('.')
            if file_ext in SUPPORTED_LANGUAGES:
                create_directory_structure_for_file(file_path, book_directory)
            else:
                print(f"Ignored '{file_path}' because it's not in the list of supported languages.")

def main():
    """
    Process the files in the current directory and organize them into the specified book directory
    """

    parser = argparse.ArgumentParser(description="Organize files into directories based on their names and extensions.")
    parser.add_argument('--dr', type=str, required=True, help="The book directory to organize the files into")
    
    args = parser.parse_args()
    
    process_files_in_directory(args.dr)

if __name__ == "__main__":
    main()
