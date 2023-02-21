# Wiki

Wiki is a web application that allows users to create, edit, and view encyclopedia entries. It is built using Python and the Django web framework.

## Features

The features of this project include:

### Entry Page

Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, will render a page that displays the contents of that encyclopedia entry. The view gets the content of the encyclopedia entry by calling the appropriate util function.

If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found. If the entry does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.

### Index Page

The `index.html` page has been updated such that, instead of merely listing the names of all pages in the encyclopedia, the user can click on any entry name to be taken directly to that entry page.

### Search

The user can type a query into the search box in the sidebar to search for an encyclopedia entry. If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page. If the query does not match the name of an encyclopedia entry, the user is taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. Clicking on any of the entry names on the search results page takes the user to that entry’s page.

### New Page

Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry. Users can enter a title for the page and, in a textarea, can enter the Markdown content for the page. Users can click a button to save their new page.

When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message. Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.

### Edit Page

On each entry page, the user can click a link to be taken to a page where they can edit that entry’s Markdown content in a textarea. The textarea is pre-populated with the existing Markdown content of the page. (i.e., the existing content is the initial value of the textarea). The user can click a button to save the changes made to the entry. Once the entry is saved, the user is redirected back to that entry’s page.

### Random Page

Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. This is done using the `markdown2` package, which can be installed via `pip3 install markdown2`.

## Credits

This project is part of the CS50 Web Programming with Python and JavaScript course, offered by Harvard University. The project specifications can be found [here](https://cs50.harvard.edu/web/2020/projects/1/wiki/).
