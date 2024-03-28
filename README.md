# Phase 3 CLI Artist and Album Project

## Introduction
    This is a project showcasing a one to many relationship by using python and SQLite3.

    Here the user will use their terminal to navigate through a series of menus so they can access information about an artist and their albums. To make it a bit more interactive I used the rich package to add animations and styling.

## Getting started

    -Fork repo
    -Enter the following comands on the files terminal
    ```bash
        pipenv install
        pipenv shell
    ```
    -Once you're in the files enviroment
    ```bash
        pip install rich
    ```
    -This will install the rich package so the colors and animations can run properly.
    -Make sure that the rich package is in the Pipfile before proceeding, otherwise it will not work!
    -Once you've made sure that all the packages have been installed run the following line to seed the database and to start the program.
    ```bash
        python lib/seed.py
        python lib/cli.py
    ```
## Using the program
    -To use the program follow the prompts that will be presented to you.
    -It will start with numerical inputs to move through the different menus.
    -Read the prompts and selections to figure out what needs to be typed to keep the program working.
    -This program will allow you to do the following:
        -Search artist by ID, name or all
        -Create a new artist
        -Update an existing artist
        -See all the albums that correspond to that artist
        -Delete an artist
        -Search an album by ID, year or all
        -Create a new album
        -Update an existing album
        -See all the albums that correspond to an artist
        -Delete an album

## Technologies and Packages used:

-Python
-SQLite3
-rich

## Conclusion

I tried to give some flare to an otherwise bland project, hope that you enjoy!

***

## Resources and disclaimer:

For the load bars and fetching data animations I used code from the resources below, these functions have no effect on the functionality of the program. They just add a 'Flare' to an otherwise bland project.

For using rich
-https://rich.readthedocs.io/en/stable/index.html 
-https://youtu.be/NIyljVEcJKw?si=9k0qOjC5-ljjW0WJ

For the load_bar(This code was used for the animation only, there is no functionality that affects how the program works)
-https://youtu.be/x1eaT88vJUA?si=pGW2McU0UN7-gjJ8 

