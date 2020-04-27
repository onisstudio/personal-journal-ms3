# Personal Journal

Data Centric Development Milestone Project | Personal Journal

## Demo

A live demo can be found [here](https://personaljournal.herokuapp.com/).

## Project Purpose

The purpose of the project is to allow users to create an online journal where thay can express their memories and the feeling they had at the moment of writing the story.

## UX

### User Stories

As a new user you can login and can add new entries in the journal, edit entries, archive/unarchive entries and also delete entries.

### Strategy

My goal was to create an user-friendly web application where users can easily add journal entries.

### Scope

The scope of the application is for users to easily add new entries, edit entries or delete them.

### Structure

The application is a one page app which has a login page for first time users, after login the users have a top navbar, a collapsible sidebar and the main content. To a add a new entry you need to go on the "Add entry" page or you can click on the floating button on the bottom right corner. When addding a new entry, the user can add a story and a feeling.

### Skeleton

[Landing wireframe](https://github.com/onisstudio/personal-journal-ms3/blob/master/wireframes/landing.png)

[Landing mobile wireframe](https://github.com/onisstudio/personal-journal-ms3/blob/master/wireframes/landing-mobile.png)

[Login wireframe](https://github.com/onisstudio/personal-journal-ms3/blob/master/wireframes/login-page.png)

[New entry wireframe](https://github.com/onisstudio/personal-journal-ms3/blob/master/wireframes/new-entry.png)

### Surface

The color scheme offers a white background a dark navbar and footer. The entries are using the card component with a white background.

## Technologies

1. HTML
2. CSS
3. Materialize (v1.0.0)
4. Javascript and jQuery (v3.5.0)
5. MongoDB Atlas
6. Python+Flask

## Features

The app allows users to add journal entries. When adding a new entry the user can add a story and a feeling, the feeling list is auto populated from the database. Entries can be edited, archived or deleted. Archived entris will go on a separate page and can be accesed at a later time, they also can be unarchived. When deleting an entry a confirmation modal will be shown to the user. Logging out will send the user back to the login page, keeping all the entries in the database from where they can be accesed at a later time.

### Future plans

Some of the features that can be implemented:

- add images/videos to the entries
- instead of delete confirmation add "Undo" option, add "Bin" page
- add a WYSIWYG editor
- add pagination

## Testing

The app was tested on all major browsers with no known issues.

When testing on the official validator services I had some errors with duplicate ids for some elements, errors that were corrected.

After fixing the ids issues, tested HTML, CSS and JS on the official validator services. No other major issues found.

## Deployment

The site is hosted on GitHub, deployed from the master branch. The deployed site will update automatically upon new commits to the master branch.

The project is also hosted on Heroku [here](https://personaljournal.herokuapp.com/). To deploy the app to Heroku, you typically use the git push command to push the code from your local repository's master branch to your heroku remote, like so: \$ git push heroku master.

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone <https://github.com/onisstudio/personal-journal-ms3.git> into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

## Credits

### Media

The photo used on the login page was obtained from [Pexels](https://www.pexels.com/).
