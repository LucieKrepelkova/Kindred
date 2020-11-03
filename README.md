# CzechITas Dash App CV

1. [Summary](#summary)
2. [How to use it](#how-to-use-it)
3. [How to use it](#how-to-change-it)
4. [Main contacts](#main-contacts)
5. [Requirements](#requirements)
6. [Main files](#main-files)
7. [Results](#how-to-deploy-the-app)

## Summary

This is a project for CzechITas Digital Excursion in Kindred.

The code generates the Dash App for your CV.

## How to use it

If you want to run this project yourself, you need to:

1. Fork this directory;
2. Create a new environment in python and install all projects from the requirements.txt file.

You can create a new environment like this:

  `virtualenv -p python3 env_name`

  And activate it:

  `source env_name/bin/activate`

  After both steps are done, you can install packages from requirements.txt:

`pip install -r requirements.txt`

3. Using terminal, run app.py file. You can do it by running `python app.py` in your
terminal. Please make sure that you are in the chechitas_dash_app on your terminal before you run it.

4. Go to http://127.0.0.1:8050/ . If you did everything correctly, you should be able to see the app.

## How to change it

There are several places where you can add your input. Please have in mind that you don't need to run the app again,
the changes should be updated automatically every time when you save app.py file.

1. CSV files under data folder. All tables and graphs in the app are taking the data from there. So
You can just change the CSV files and save them. You are free to change the names of the columns,
the amount of the columns, add different types of skills, etc. The tables will be updated automatically.
2. Chunks in the code in the app.py file. All the code that should be changed (mainly for the left panel)
are marked like this:

`# CHANGE YOUR INFO HERE-------------------------------------`

3. Your profile picture. Go to assets and upload your profile picture as "profile.jpg".
4. Styling (optional). There is a CSS file (in assets folder, "styles.css"), you can change
colours or font family in there. Font family will be called "font-family", colours will be called
"backgroud-color" and "color" for background and text colours accordingly. The colours are in hex format,
you can find the codes for the ones you like in here: https://htmlcolorcodes.com/ .

## Main contacts

| Name | Email  | Role in the project |
| :--- | :---: | :---: |
| Morta Vilkaite | morta.vilkaite@kindredgroup.cz | Data Scientist |
| Alena Dziamidava | alena.dziamidava@kindredgroup.cz | Data Analyst |

## Requirements

Python packages:
- plotly==4.11.0
- dash_core_components==1.12.1
- dash_html_components==1.1.1
- numpy==1.19.1
- dash_table==4.10.1
- dash==1.16.3
- pandas==1.1.3

## Main files

- **.gitignore** - file with the list of directories/files that should be not pushed to git with git push.
- **README.md** - main information about the projects.
- **requirements.txt** - file with required Python projects.
- **app.py** -  python scripts for the main code + left side panel.
- **summary_page.py** - python scripts for "Summary" tab. You don't need to change anything in here.
- **skills_detailed_page.py** - python scripts for the second tab. You don't need to change anything in here.

**data** folder:

- **certifications.csv** - data for certifications table (tab "Summary")
- **hobbies.csv** - data for hobbies graph (tab "Summary")
- **jobs.csv** - data for jobs table (tab "Summary")
- **skills_in_detail.csv** - data for detailed skills table (second tab)
- **skills.csv** - data for skills graph (tab "Summary")

**assets** folder:

- **github.png** - logo for GitHub
- **kaggle.webp** - logo for Kaggle
- **LinkedIn-logo.png** - logo for LinkedIn
- **profile.jpg** - your profile picture
- **styles.css** - CSS stylesheet for styling your app


## How to deploy the app

We are not showing you during the presentation how to deploy your app, but if you decide to,
Plotly has a nice documentation in here: https://dash.plotly.com/deployment .
