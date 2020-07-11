import os
from typing import Dict, Optional, List

from constants import GITHUB_PAGES, HEADER, FOOTER, SUPPORTED_FILE_EXT, ALL_NOTES_PAGE_ENABLED
from utils import find_wiki_links, get_file_contents_without_reference_block, get_all_notes_page_contents, \
    write_all_notes_file, NoteMetadata


class NoteRepo:
    def __init__(self, notes_dir: str):
        self.notes_dir = notes_dir
        self.note_to_metadata_map = NoteRepo.generate_notes_to_metadata_map(notes_dir)
        if not self.note_to_metadata_map:
            raise Exception("No notes found in this directory!")

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
                        note_contents = note.read()
                        note_contents_without_ref_block = get_file_contents_without_reference_block(note_contents)
                        wiki_links = find_wiki_links(note_contents_without_ref_block)
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
    def _get_back_link_md_line(metadata: NoteMetadata) -> Optional[str]:
        if metadata:

            is_github_readme = metadata.note_name.lower() == 'readme' and GITHUB_PAGES
            if is_github_readme:
                metadata.relative_path_without_ext = metadata.relative_path_without_ext.replace("readme", "")

            return f"- [[{metadata.note_name}]]({metadata.relative_path_without_ext})"

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

    def get_note_contents(self, note_name: str) -> str:
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(note_name)
        with open(note_metadata.complete_path, "r") as readable_file:
            return readable_file.read()

    def put_note_contents(self, note_name: str, note_contents: str):
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(note_name)
        with open(note_metadata.complete_path, "w") as writeable_file:
            writeable_file.write(note_contents)

    def refresh_reference_block_for_note(self, note_name: str):
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(note_name)
        if not note_metadata:
            raise Exception(f"Note named {note_name} not found!")

        file_contents = self.get_note_contents(note_name)
        cleared_file_contents = get_file_contents_without_reference_block(file_contents)
        ref_text = self.generate_reference_block(note_name)
        self.put_note_contents(note_name, cleared_file_contents.strip() + (os.linesep * 3) + ref_text)

    def rename_note(self, src_name, dst_name):
        note_metadata: NoteMetadata = self.note_to_metadata_map.get(src_name)
        if not note_metadata:
            raise Exception(f"Note named {src_name} not found!")

        note_complete_path = note_metadata.complete_path

        for note, metadata in self.note_to_metadata_map.items():
            if src_name in metadata.wiki_links:
                note_contents = self.get_note_contents(note_name=note)
                modified_note_contents = note_contents.replace(f"[[{src_name}]]", f"[[{dst_name}]]")
                self.put_note_contents(metadata.note_name, modified_note_contents)

        renamed_complete_path = note_metadata.complete_path.replace(src_name, dst_name)
        os.rename(note_complete_path, renamed_complete_path)
        print(f"Rename from {src_name} -> {dst_name} is complete.")

    def process_notes(self):
        for note, metadata in self.note_to_metadata_map.items():
            self.refresh_reference_block_for_note(note)
        if ALL_NOTES_PAGE_ENABLED:
            write_all_notes_file(
                path=os.path.join(self.notes_dir, "all-notes.md"),
                all_notes_lines=get_all_notes_page_contents(self.note_to_metadata_map),
            )
