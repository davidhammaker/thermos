# _Thermos_ | Flask Practice Project
This project follows the [PluralSight](https://www.pluralsight.com/) course, [_Introduction to the Flask Microframework_](https://app.pluralsight.com/library/courses/flask-micro-framework-introduction/table-of-contents). The project will use [Flask](http://flask.pocoo.org/) to create a "bookmark sharing" web-app.

**As of 11/26/2018, this entire code is non-functional. I am following the instructor examples in hopes that I will eventually be able to make the code work in Python 3. One problem is that** `manage.py` **does not behave for me the way it behaves for the instructor, so I am unable to use it to update the database (which is now outdated and unusable). I intend to try correcting the problems in the future when I am more skilled in working with packages in Python 3. In the meantime, I have tagged the last known working version of the code as "Semi-working" in the repository. Subsequent commits, particularly those which include** `models.py` **will only result in an error.**

## Overview
This project is currently a work-in-progress. I will be updating files (and the README) continually as I make my way through the course.

Per the course instructor, I obtained a _Responsive_ template from [Initializr](http://www.initializr.com/). (To replicate this template, go to the  _Initializer_ website and select "_Responsive_". Under "_H5BP Optional_", select only "_404 Page_".) All HTML files from _Initializer_ are located in the `templates` directory. Other files, including CSS and JavaScript files, are located in the `static` directory.

The `thermos` directory contains `__init__.py`, also per the instructor. Up to this point, the file has remained empty.

The `thermos` directory also contains `thermos.py`, which contains the _Flask_ project.

## Dependencies
For this project, I am using [Python 3](https://www.python.org/) and [Flask](http://flask.pocoo.org/). I have also created a virtual environment in which to run this project, using the `venv` module for Python 3.

To replicate these things, first install Python 3 (you can find instructions on Python's [website](https://www.python.org/about/gettingstarted/)). I am using Python 3.7. You should also ensure that you can [install packages](https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages) with _pip_.

I am using the `venv` module to create a virtual environment (see the `venv` [documentation](https://docs.python.org/3/library/venv.html)). Open a shell prompt (I am using [Git Bash](https://git-scm.com/downloads) for Windows) and run `$ python -m venv thermos_venv`, where '`thermos_venv`' is the name of my virtual environment. If Python 2 is the default version of Python on your machine, you may need to run `$ python3 -m venv thermos_venv` instead. (You may substitute '`thermos_venv`' for the path to your new virtual environment.) Activate the environment by running the appropriate command (found in the [documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)). In Git Bash on Windows, I ran `source thermos_venv/Scripts/activate`.

Inside your active virtual environment, install _Flask_ by running `$ pip install flask`.

Additionally, install _Flask WTF_ by running `$ pip install flask-wtf`.

## Usage
The project has not been deployed to an online server. To experimentally test the web-app, I recommend that you first _clone_ the repository, then `cd` into the cloned repository. From there, run `$ python thermos/thermos.py` (or `$ python3 thermos/thermos.py` if Python 3 is not the default version of Python on your machine). This deploys the web-app to the local host on port 7700. To access the app, go to `http://localhost:7700/` in your web browser.

## My Code VS Instructor Code

In `forms.py`, line 3, the instructor wanted me to use `from flask.ext.wtf.html5 import URLField`. My code editor gave me an error, saying `flask.ext` does not exist, and there is certainly no `URLField` inside it. After some internet searching, I think I have found the solution. I am using `from wtforms.fields.html5 import URLField` instead. (This module will be used to validate URLs.)

Additionally, `flask_wtf.Form` is deprecated. I am using `flask_wtf.FlaskForm` instead, which is the replacement for `flask_wtf.Form`. For simplicity in this example, I still import the module as `Form`: `from flask_wtf import FlaskForm as Form`.

## Notes:

* My code editor gives me errors in `thermos.py` in the line that includes, `from forms import BookmarkForm`. The errors state, "Unresolved reference 'forms'..." and "Unresolved reference 'BookmarkForm'..." Regardless of this error, the code runs fine. (I am using _PyCharm_ as my code editor. I don't know whether this error appears on other code editors.)

* Following the instructor's code, I used `form.url.errors` to show form errors when a user enters an invalid URL. In the instructor video, when he enters an invalid URL in the URL field, the text next to and inside of the field turns red, and a red error message appears as an item in an unordered list beneath the field. To the best of my knowledge, I have copied his code precisely, but I only achieve the same results if I enter a "localhost" URL (I.e. `http://localhost:7700`). Other invalid URLs result in a small notification just below the field, which says either "Please fill out this field." or "Please enter a URL." I am not certain how where these notifications come from, but I think they may be associated with the validators (`DataRequired()` and `url()` respectively). These notifications may have been a part of an update that came after the instructor videos were published.
