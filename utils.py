import os
import re


def generate_notes_to_path_map(notes_dir: str) -> dict:
    """
    Generates a map which contains note names and relative ext stripped note path's
    Used in generating reference text for notes
    :param notes_dir: str , it is the root file path for notes
    :return: dict of note name and relative github friendly path
    """
    _notes_to_path_map = {}
    for root, dirs, files in os.walk(notes_dir):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext == ".md":
                complete_path = os.path.join(root, file)
                relative_path = complete_path.replace(notes_dir + os.sep, "")
                relative_path_without_ext = relative_path.replace(".md", "")
                _notes_to_path_map[file_name] = relative_path_without_ext

    return _notes_to_path_map


def find_wiki_links(content: str):
    regex = r"\[\[(.*)\]\]"
    matches = re.findall(regex, content, re.MULTILINE | re.IGNORECASE)
    return matches
