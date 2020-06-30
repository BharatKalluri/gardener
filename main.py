import os

import click

from reference_generator import refresh_references_text_for_file
from utils import generate_notes_to_path_map


@click.group()
def cli():
    pass


@click.command()
def link():
    notes_dir_path = os.getcwd()
    notes_to_path_map = generate_notes_to_path_map(notes_dir_path)

    if not notes_to_path_map:
        click.echo("No notes found in this directory, are you sure this folder is your digital garden?")
        return

    # TODO: Notes to path map should also give the complete path of the note, along with back links etc.. need to plan this
    for root, dirs, files in os.walk(notes_dir_path):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext == ".md":
                complete_path = os.path.join(root, file)
                refresh_references_text_for_file(complete_path, notes_to_path_map)
                click.echo(f"Processing {complete_path} is complete!")


if __name__ == "__main__":
    cli.add_command(link)
    cli()
