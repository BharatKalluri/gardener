import base64
import os
import re
from dataclasses import dataclass
from typing import List, Dict, Set

from gardener.constants import HEADER, FOOTER


@dataclass
class NoteMetadata:
    back_links: Set[str]
    note_name: str
    relative_path_without_ext: str
    wiki_links: Set[str]
    complete_path: str


def find_wiki_links(content: str) -> List[str]:
    regex = r"\[\[(.*?)\]\]"
    matches = re.findall(regex, content, re.MULTILINE | re.IGNORECASE)
    return matches


def get_file_contents_without_reference_block(file_contents: str):
    header_line_no = None
    footer_line_no = None
    lines_in_file = file_contents.split(os.linesep)
    total_line_count = len(lines_in_file)
    for i in range(len(lines_in_file)):
        line_contents = lines_in_file[i]
        if HEADER in line_contents:
            header_line_no = i
        if FOOTER in line_contents:
            footer_line_no = i

    contents_till_header = lines_in_file[:header_line_no] if header_line_no else lines_in_file[:total_line_count]
    contents_after_footer = lines_in_file[(footer_line_no + 1) :] if footer_line_no else lines_in_file[total_line_count:]
    final_file_contents = os.linesep.join(contents_till_header + contents_after_footer)
    return final_file_contents


def get_all_notes_page_contents(note_to_metadata_map: Dict[str, NoteMetadata]) -> List[str]:
    page_header = ["# All notes in the garden", os.linesep]
    note_list = [
        f"- [{metadata.note_name}]({metadata.relative_path_without_ext})" for name, metadata in note_to_metadata_map.items()
    ]
    return page_header + note_list


def write_all_notes_file(path: str, all_notes_lines: List[str]):
    with open(path, "w") as all_notes_page:
        all_notes_page.write(os.linesep.join(all_notes_lines))
