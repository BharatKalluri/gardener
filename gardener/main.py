import os

import click

from gardener.note_repo import NoteRepo


@click.group()
def cli():
    pass


@click.command()
def link():
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo(notes_dir_path)
    notes_repo.process_notes()
    click.echo("Linking complete!")


@click.command()
def tend():
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo(notes_dir_path)
    notes_repo.tend_garden()
    click.echo("Your garden has been tended!")


@click.command()
@click.argument('src')
@click.argument('dst')
def rename(src, dst):
    notes_dir_path = os.getcwd()
    notes_repo = NoteRepo(notes_dir_path)
    notes_repo.rename_note(src, dst)
    click.echo(f"Rename from {src} -> {dst} is complete.")


def app():
    cli.add_command(link)
    cli.add_command(rename)
    cli.add_command(tend)
    cli()
