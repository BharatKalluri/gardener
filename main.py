import os

import click

from note_repo import NoteRepo


@click.group()
def cli():
    pass


@click.command()
def link():
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo.get_new_note_repo(notes_dir_path)
    notes_repo.process_notes()


if __name__ == "__main__":
    cli.add_command(link)
    cli()
