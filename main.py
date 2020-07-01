import os

import click

from utils import generate_notes_to_metadata_map


@click.group()
def cli():
    pass


@click.command()
def link():
    notes_dir_path = os.getcwd()
    notes_to_metadata_map = generate_notes_to_metadata_map(notes_dir_path)

    if not notes_to_metadata_map:
        click.echo("No notes found in this directory, are you sure this folder is your digital garden?")
        return

    for note, metadata in notes_to_metadata_map.items():
        metadata.refresh_reference_block_for_note(notes_to_metadata_map)


if __name__ == "__main__":
    cli.add_command(link)
    cli()
