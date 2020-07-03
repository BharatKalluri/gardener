# Gardener

> Note: This is still an alpha product

Gardener is a command line tool meant to organize your digital garden.

Features:
- Back link's and wiki links support
- Run `link` and host your notes on github pages.

## Workflow

- Write notes in markdown, use wiki-links (`[[file-name]]`) for linking notes together.
    vs code has an excellent extension called [Markdown notes](https://marketplace.visualstudio.com/items?itemName=kortina.vscode-markdown-notes) which provides autocomplete, back-links in editor etc..
> Note: We will require readme.md which will act as the index page of your website
- Run `gardener link` in your notes folder. For every note file, it will attach a couple of lines of markdown links with a header and footer.
    These turn into actual links later on if you want to make your website public using github pages (tutorial coming soon!)
- Push the updated files and switch on github pages if you please.

### Limitations
- Although gardener handles nested files, it cannot handle file name conflicts.
    So, if the same file name is in two different folders. There will be conflicts.

### What is done?

- `gardener link`: Generates links using wiki-links in the notes.

### What is planned?

- `gardener tend`: Looks for words in notes which could be wiki-links. This will enhance the quality of
    wiki-links and back links!
- `gardener push`: (still in discussion) will be a meta command which will run `tend` -> `link` -> `git push`.
- `gardener clean`: (still in discussion) will clean the references block and back links block. If those look like clutter
    in your note taking experience, this should help.
    
Please do let me know if you have any other interesting ideas over at github issues!