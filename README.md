# CzechITas Dash App CV

1. [Summary](#summary)
2. [How to use it](#how-to-use-it)
2. [Main contacts](#main-contacts)
3. [Where is everything stored](#where-is-everything-stored)
4. [Requirements](#requirements)
5. [Main files](#main-files)
6. [Results](#results)

## Summary

This is a project for CzechITas Digital Excursion in Kindred.

The code generates the Dash App.

## How to use it

You can have any additional folders or files in the directory, but please **don't store csv files and graphs**. Instead, store them on Google Drive or in the Kindred database and include the links. We have limited storage in here, so let's try to keep it clean :)

If you forked this directory or just copied the files to your computer, you will still miss the folder called "folder_to_ignore". You can just create it on your computer in the same directory as this README.md file. In that new folder you can store all project related file or folders which shouldn't be pushed to the GitHub.

If you want to run this project yourself, you can create a new environment in python and install all projects from the requirements.txt file.

You can create a new environment like this:

virtualenv -p python3 env_name`

And activate it:

`source env_name/bin/activate`

After both steps are done, you can install packages from requirements.txt:

`pip install -r /path/to/requirements.txt`

## Main contacts

Client side:

| Client name | Email  | Role in the project |
| :--- | :---: | :---: |
| Name Surname | email@email.com | Ad manager |

Internal:

| Name | Email  | Role in the project |
| :--- | :---: | :---: |
| Name Surname | email@email.com | Project manager |

## Where is everything stored

Graphs: Link to Teams or Google Drive repository <br>
Data: Kindred database (connector is in the code, credentials are needed)

## Requirements

Python packages:
- chart_studio==1.0.0
- pandas==1.0.1
- plotly==4.5.2
- numpy==1.18.1
- scipy==1.3.2
- statsmodels==0.11.1

## Main files

- **.gitignore** - file with the list of directories/files that should be not pushed to git with git push.
- **README.md** - main information about the projects
- **requirements.txt** - file with required Python projects

## Results

Add a short summary of the results of your investigation or project.
