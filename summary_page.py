import pathlib
import os
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt

import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output, State

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

# function for importing data
def import_data(file_name):
    return pd.read_csv(os.path.join(APP_PATH, os.path.join("data", file_name)))

# importing the data
certifications = import_data("certifications.csv")
hobbies = import_data("hobbies.csv")
jobs = import_data("jobs.csv")
skills = import_data("skills.csv")

# sorting the skills table to have it nicely sorted in the graphs
skills=skills.sort_values(by='rating', ascending = False)

# getting all possible skill types for the filter
available_types = skills['type'].unique()

# creating a colors array to be used in the graphs
colors_array = ['#e30613', '#000000', '#808B96', '#FFFFFF']

# custom layout for the graphs
layout_custom = go.layout.Template(
    layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                    legend=dict(orientation='h',y=1.1),
                    autosize=True, font=dict(family='Montserrat')))

def plot_hobbies(hobbies_data):
    """Make the plot for hobbies"""
    hobbies_fig = px.scatter(
        hobbies_data, x='hobby', y='frequency', size='importance',
        color='type', color_discrete_sequence=colors_array
    )

    hobbies_fig.update_layout(transition_duration=500, template=layout_custom)

    hobbies_fig.update_xaxes(title_text = "")
    hobbies_fig.update_yaxes(title_text = "Frequency (times per week)")
    return hobbies_fig

def render_summary_page():
    """Renders summary tab"""
    SUMMARY_PAGE = dcc.Tab(label="Summary", children=[
        html.Div([
            html.Div([
                html.H2("Work Experience"),
                dt.DataTable(
                    id='table-work-job',
                    sort_action='native',
                    style_cell={
                        'padding': '15px',
                        'width': 'auto',
                        'textAlign': 'left'
                    },
                    columns=[{"name": i.title(), "id": i} for i in jobs.columns],
                    data=jobs.to_dict("rows")
                ),
            ], className="item3", id="tableExperience"),
            html.Div([
                html.H2("Skills"),
                html.Div([
                    dcc.Dropdown(
                        id='skills-dropdown',
                        options=[{'label': i, 'value': i} for i in available_types],
                        value=available_types[0]
                    ),
                    dcc.Graph(id="skills-graph")
                ], id="skills-graph-container"),
            ], className="item4"),
            html.Div([
                html.H2("Certificates"),
                dt.DataTable(
                    id='table-cert',
                    sort_action='native',
                    style_cell={
                        'padding': '15px',
                        'width': 'auto',
                        'textAlign': 'left'
                    },
                    columns=[{"name": i.title(), "id": i} for i in certifications.columns],
                    data=certifications.to_dict("rows")
                ),
                html.P("Full list of certificates can be found on my Linkedin page."),
            ], className="item3", id="tableCertificates"),
            html.Div([
                html.H2("Hobbies"),
                html.Div([
                    dcc.Graph(id="hobby-graph", figure=plot_hobbies(hobbies))
                ], id="hobby-graph-container"),
            ], className="item4", id="tableHobbies"),
        ], className="flexContainer3 item2"),
    ])
    return SUMMARY_PAGE
