# gets the total size of all files directly within the given directory

from pathlib import Path

def get_sub_directories(path: str) -> list[str]:
    try:
        directory = Path(path)
        if not directory.exists():
            raise FileNotFoundError(f"Path '{path}' does not exist")

        if not directory.is_dir():
            raise NotADirectoryError(f"Path '{path}' is not a directory")
        
        # To exclude system folder paths
        subdirectories = [
            str(subdir) for subdir in directory.iterdir()
            if subdir.is_dir() and not subdir.name.startswith('.')
            and not subdir.name.startswith('$')
            and subdir.name != "System Volume Information"
        ]
        
        return subdirectories
    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print("An Error occured: ", e)

# def calculate_path_size(path: str) -> int:
#     """
#     Calculates the total size of all files directly within the given directory,
#     skipping directories where access is denied.
#     """
#     try:
#         total_size = 0
#         for filename in os.listdir(path):
#             filepath = os.path.join(path, filename)
#             try:
#                 if os.path.isfile(filepath):
#                     total_size += os.path.getsize(filepath)
#             except OSError as e:
#                 if e.winerror == 13:  # Check if the error is Access Denied
#                     print(f"Access denied: {filepath}")
#                 else:
#                     print(f"Error processing {filepath}: {e}")
#         # print(total)
#         return total_size
#     except Exception as e:
#         print(f"An error occurred: {e}")
        
def calculate_path_size(path: str) -> int:
    """
    Calculates the total size of all files directly within the given directory,
    skipping directories where access is denied.
    """
    try:
        total_size = sum(f.stat().st_size for f in Path(path).glob("**/*") if f.is_file())
        return total_size
    
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def format_size(size_bytes: int) -> str:
    """
    Converts bytes to a human-readable format (KB, MB, GB).
    """
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"


while True:
    
    path = input("Enter your path: ")
    try:

        # print(get_sub_directories(path))
        res = {
            subdir:format_size(calculate_path_size(subdir)) for subdir in get_sub_directories(path)
        }
        if res:
            for key, value in res.items():
                print("{} -> {}".format(key, value))
    except Exception:
        print("Invalid path try again")