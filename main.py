import os

import click

from note_repo import NoteRepo


@click.group()
def cli():
    pass


@click.command()
def link():
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo(notes_dir_path)
    notes_repo.process_notes()


@click.command()
@click.argument('src')
@click.argument('dst')
def rename(src, dst):
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo(notes_dir_path)
    notes_repo.rename_note(src, dst)


if __name__ == "__main__":
    cli.add_command(link)
    cli.add_command(rename)
    cli()
