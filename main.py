import os

from reference_generator import refresh_references_text_for_file
from utils import generate_notes_to_path_map

if __name__ == "__main__":
    # TODO: This should come from config or env
    # TODO: This should be a command line program
    notes_dir_path = "/home/bharatkalluri/projects/notes"
    notes_to_path_map = generate_notes_to_path_map(notes_dir_path)
    for root, dirs, files in os.walk(notes_dir_path):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext == ".md":
                complete_path = os.path.join(root, file)
                print(f"Processing {complete_path}")
                refresh_references_text_for_file(complete_path, notes_to_path_map)
