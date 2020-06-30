# Gardner

> Note: This is still an alpha product

Gardner is a cli tool meant to organize your digital garden.

## Workflow

- Fork [Foam template](https://github.com/foambubble/foam-template), this will be our base setup.
- Write notes in markdown, use wiki-links (`[[file-name]]`) for linking notes together.
    vs code has an excellent extension called [Markdown notes](https://marketplace.visualstudio.com/items?itemName=kortina.vscode-markdown-notes) which provides autocomplete, back-links in editor etc..
- Run `gardner link` in your notes folder. For every note file, it will attach a couple of lines of markdown links with a header and footer.
    These turn into actual links later on if you want to make your website public using github pages (tutorial coming soon!)
- Push the updated files and switch on github pages if you please.

### Limitations
- Although gardner handles nested files, it cannot handle file conflicts.
    So, if the same file name is in two different folders. There will be conflicts.

### What is done?

- `gardner link`: Generates links using wiki-links in the notes.

### What is planned?

- `gardner link`: Should also generate back links to the note. And there will be a config option
    which can dictate if back links section should be included in the file as well. (default: on)
- `gardner tend`: Looks for words in notes which could be wiki-links. This will enhance the quality of
    wiki-links and back links!
- `gardner init`: Will init a folder with template ready for github, a file recommending what extensions
    could be used with vs code and some markdown files to showcase what can be done.(heavily inspired by foam-template)
- `gardner push`: (still in discussion) will be a meta command which will run `tend` -> `link` -> `git push`.
- `gardner clean`: (still in discussion) will clean the references block and back links block. If those look like clutter
    in your note taking experience, this should help.
    
Please do let me know if you have any other interesting ideas over at github issues!