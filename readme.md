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

## How to Install?

You will need to install python and pip on your system.

```shell script
pip install --user https://github.com/BharatKalluri/gardener/releases/download/0.1/gardener-0.1.0.tar.gz
```

Currently I am not able to upload to [pypi](pypi.org/) due to [some reasons](https://github.com/BharatKalluri/gardener/issues/14). Will publish sometime soon

## What can it do?

- create a `readme.md`. This will serve as an entry point for your notes.
- Write notes in markdown, use wiki-links (`[[file-name]]`) all you want.
- Run `gardener link` in your notes folder. Now you will have markdown links linking your notes!
- You can also rename notes using `gardener rename <name> <new name>`, gardener will update all your wiki links
- Push the updated files and switch on github pages if you please. You will have a great looking website ready for you! ([example](https://notes.bharatkalluri.in))

Pro tip: Setup a pre-commit hook so that all your will have up to date backlinks/wikilinks. I use [lefthook](https://github.com/Arkweid/lefthook/)
     personally, The config is [very simple!](https://github.com/BharatKalluri/notes/blob/master/lefthook.yml)

### What is planned?

- `gardener tend`: Looks for words in notes which could be wiki-links. This will enhance the quality of
    wiki-links and back links!
- A graph view between all your wiki links.
    
### Limitations
- Although gardener handles nested files, it cannot handle same file name conflicts.
    
Please do let me know if you have any other interesting ideas over at github issues!