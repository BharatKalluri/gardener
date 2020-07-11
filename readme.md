<div>
  <h1 align="center">Gardener</h1>
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

## Workflow

- Write notes in markdown, use wiki-links (`[[file-name]]`) for linking notes together.
    vs code has an excellent extension called [Markdown notes](https://marketplace.visualstudio.com/items?itemName=kortina.vscode-markdown-notes) which provides autocomplete, back-links in editor etc..
> Note: We will require readme.md which will act as the index page of your website
- Run `gardener link` in your notes folder. For every note file, it will attach a couple of lines of markdown links with a header and footer.
    These turn into actual links later on if you want to make your website public using github pages.
    > Pro tip: Setup a pre-commit hook so that all your will have up to date backlinks/wikilinks. I use [lefthook](https://github.com/Arkweid/lefthook/)
     personally, The config is [very simple!](https://github.com/BharatKalluri/notes/blob/master/lefthook.yml)
- Push the updated files and switch on github pages if you please. You will have a great looking website ready for you! ([example](https://notes.bharatkalluri.in))

### Limitations
- Although gardener handles nested files, it cannot handle file name conflicts.
    So, if the same file name is in two different folders. There will be conflicts.

### What else can I do?

- `gardener rename old_name new_name`: Will rename the note and corresponding wiki-links

### What is planned?

- `gardener tend`: Looks for words in notes which could be wiki-links. This will enhance the quality of
    wiki-links and back links!
    
Please do let me know if you have any other interesting ideas over at github issues!