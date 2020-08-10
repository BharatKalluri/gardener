<div>
  <h1 align="center">Gardener 🌱</h1>
  <h3 align="center">A simple command line tool to maintain your digital garden.</h3>
</div>

<br/>

<p align="center">
   <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-GPL--3.0-blue.svg">
   </a>
</p>

<p align="center">
    <a href="https://github.com/bharatkalluri/gardener/issues/new"> Report a problem! </a>
</p>

> Note: This is still an alpha product

Gardener is a command line tool meant to organize your digital garden.

The aim of this tool is to **get out of the way and make managing a digital garden editor/service independent.**

## Installation

You will need to install python and pip on your system.

```shell script
pip install --user https://github.com/BharatKalluri/gardener/releases/download/0.1/gardener-0.1.0.tar.gz
```

[Will publish to pypi soon](https://github.com/BharatKalluri/gardener/issues/14)

## What can it do?

Create a `readme.md`. This will serve as an entry point for your notes. Write notes in markdown, use wiki-links (`[[file-name]]`) to link between notes.

- `gardener link` : Converts all wiki links to markdown links (so that github pages can pick these up as normal web links)
- `gardener rename <name> <new name>`: Will rename a note and also the corresponding wiki links
- `gardener tend`: Will scan all your notes and find out which notes are not linked and will automatically create wiki links for you (coming soon in release 0.2!)

Push the updated files and switch on github pages if you please. You will have a great looking website ready for you! ([example](https://notes.bharatkalluri.in))

> Pro tip: Setup a pre-commit hook so that all your will have up to date backlinks/wikilinks. I use [lefthook](https://github.com/Arkweid/lefthook/)
     personally, The config is [very simple!](https://github.com/BharatKalluri/notes/blob/master/lefthook.yml)

### What is planned?

- A graph view between all your wiki links.
    
### Limitations
- Although gardener handles nested files, it cannot handle same file name conflicts.
    
Please do let me know if you have any other interesting ideas over at github issues!
