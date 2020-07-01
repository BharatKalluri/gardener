import os
import re
from typing import Dict

from note_metadata import NoteMetadata

SUPPORTED_FILE_EXT = [".md"]


def generate_notes_to_metadata_map(notes_dir: str) -> Dict[str, NoteMetadata]:
    _notes_to_metadata_map: Dict[str, NoteMetadata] = {}
    for root, dirs, files in os.walk(notes_dir):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext in SUPPORTED_FILE_EXT:
                complete_path = os.path.join(root, file)
                relative_path = complete_path.replace(notes_dir, "")
                relative_path_without_ext = relative_path.replace(".md", "")
                with open(complete_path) as note:
                    wiki_links = find_wiki_links(note.read())
                    _notes_to_metadata_map[file_name] = NoteMetadata(
                        back_links=set(),
                        note_name=file_name,
                        relative_path_without_ext=relative_path_without_ext,
                        wiki_links=set(wiki_links),
                        complete_path=complete_path,
                    )

    # Populate back links
    for name, metadata in _notes_to_metadata_map.items():
        wiki_links_for_note = metadata.wiki_links
        for link in wiki_links_for_note:
            note_metadata = _notes_to_metadata_map.get(link)
            if note_metadata:
                _notes_to_metadata_map[link].back_links.add(name)

    return _notes_to_metadata_map


def find_wiki_links(content: str):
    regex = r"\[\[(.*)\]\]"
    matches = re.findall(regex, content, re.MULTILINE | re.IGNORECASE)
    return matches
