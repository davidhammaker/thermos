# _Thermos_ | Flask Practice Project
This project follows the [PluralSight](https://www.pluralsight.com/) course, [_Introduction to the Flask Microframework_](https://app.pluralsight.com/library/courses/flask-micro-framework-introduction/table-of-contents). The project will use [Flask](http://flask.pocoo.org/) to create a "bookmark sharing" web-app.

## Overview
This project is currently a work-in-progress. I will be updating files (and the README) continually as I make my way through the course.

Per the course instructor, I obtained a _Responsive_ template from [Initializr](http://www.initializr.com/). (To replicate this template, go to the  _Initializer_ website and select "_Responsive_". Under "_H5BP Optional_", select only "_404 Page_".) All HTML files from _Initializer_ are located in the `templates` directory. Other files, including CSS and JavaScript files, are located in the `static` directory.

The `thermos` directory contains `__init__.py`, also per the instructor. Up to this point, the file has remained empty.

The `thermos` directory also contains `thermos.py`, which contains the _Flask_ project.

## Dependencies
For this project, I am using [Python 3](https://www.python.org/) and [Flask](http://flask.pocoo.org/). I have also created a virtual environment in which to run this project, using the `venv` module for Python 3.

To replicate these things, first install Python 3 (you can find instructions on Python's [website](https://www.python.org/about/gettingstarted/)). I am using Python 3.7. You should also ensure that you can [install packages](https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages) with _pip_.

I am using the `venv` module to create a virtual environment (see the `venv` [documentation](https://docs.python.org/3/library/venv.html)). Open a shell prompt (I am using [Git Bash](https://git-scm.com/downloads) for Windows) and run `$ python -m venv thermos_venv`, where '`thermos_venv`' is the name of my virtual environment. (You may substitute '`thermos_venv`' for the path to your new virtual environment.) Activate the environment by running the appropriate command (found in the [documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)). In Git Bash on Windows, I ran `source thermos_venv/Scripts/activate`.

Inside your active virtual environment, install _Flask_ by running `$ pip install flask`.
