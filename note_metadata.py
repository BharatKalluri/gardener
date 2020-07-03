import os
from dataclasses import dataclass
from typing import Set, Dict, Optional, List

from utils import find_wiki_links

# TODO: This needs to come from config, this basically trims out readme from relative path's so
#  that github pages does not error
GITHUB_PAGES = True

HEADER: str = '[//begin]: # "Autogenerated link references for markdown compatibility"'
FOOTER: str = '[//end]: # "Autogenerated link references for markdown compatibility"'

SUPPORTED_FILE_EXT = [".md"]


@dataclass
class NoteMetadata:
    back_links: Set[str]
    note_name: str
    relative_path_without_ext: str
    wiki_links: Set[str]
    complete_path: str


@dataclass
class NoteRepo:
    note_to_metadata_map: Dict[str, NoteMetadata]

    @staticmethod
    def get_new_note_repo(folder_path: str) -> 'NoteRepo':
        notes_to_metadata_map = NoteRepo.generate_notes_to_metadata_map(folder_path)
        if not notes_to_metadata_map:
            # TODO: Throw a custom exception
            raise Exception("No notes found in this directory!")
        notes_repo = NoteRepo(note_to_metadata_map=notes_to_metadata_map)
        return notes_repo

    @staticmethod
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

    @staticmethod
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
        contents_after_footer = lines_in_file[(footer_line_no + 1):] if footer_line_no else lines_in_file[
                                                                                            total_line_count:]
        final_file_contents = os.linesep.join(contents_till_header + contents_after_footer)
        return final_file_contents

    @staticmethod
    def _get_back_link_md_line(back_link_metadata: NoteMetadata) -> Optional[str]:
        if back_link_metadata:
            if back_link_metadata.note_name.lower() == 'readme' and GITHUB_PAGES:
                back_link_metadata.relative_path_without_ext = \
                    back_link_metadata.relative_path_without_ext.replace("readme", "")
            return f"- [[{back_link_metadata.note_name}]]({back_link_metadata.relative_path_without_ext})"

    def _get_back_link_lines(self, note_metadata: NoteMetadata) -> List[str]:
        back_links = note_metadata.back_links
        back_link_md_lines = [
            NoteRepo._get_back_link_md_line(self.note_to_metadata_map.get(back_link)) for back_link in back_links
        ]
        return list(filter(None, back_link_md_lines))

    @staticmethod
    def _get_wiki_link_md_line(note_metadata: NoteMetadata) -> Optional[str]:
        return f'[{note_metadata.note_name}]: {note_metadata.relative_path_without_ext} "{note_metadata.note_name}"'

    def generate_reference_block(self, note_name: str) -> str:
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(note_name)
        if not note_metadata:
            raise Exception(f"Note named {note_name} not found!")

        reference_block_lines = [HEADER]

        back_links = note_metadata.back_links
        wiki_links = note_metadata.wiki_links

        if back_links:
            reference_block_lines.extend([
                os.linesep,
                "#### Back links",
                *self._get_back_link_lines(note_metadata),
                os.linesep
            ])

        reference_block_lines.extend([
            self._get_wiki_link_md_line(self.note_to_metadata_map.get(link))
            for link in wiki_links
        ])

        reference_block_lines.append(FOOTER)
        return os.linesep.join(reference_block_lines)

    def refresh_reference_block_for_note(self, note_name: str):
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(note_name)
        if not note_metadata:
            raise Exception(f"Note named {note_name} not found!")

        with open(note_metadata.complete_path, "r") as readable_file:
            file_contents = readable_file.read()
            cleared_file_contents = self.get_file_contents_without_reference_block(file_contents)
            ref_text = self.generate_reference_block(note_name)
            with open(note_metadata.complete_path, "w") as writeable_file:
                writeable_file.write(cleared_file_contents.strip() + (os.linesep * 3) + ref_text)

    def process_notes(self):
        for note, metadata in self.note_to_metadata_map.items():
            self.refresh_reference_block_for_note(note)
