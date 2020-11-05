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

# importing codes for pages
import summary_page as sm
import skills_detailed_page as sdp

app = dash.Dash(__name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

server = app.server

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

skills = sm.import_data("skills.csv")

# creating a colors array to be used in the graphs
colors_array = ['#e30613', '#000000', '#808B96', '#FFFFFF']

# custom layout for the graphs
layout_custom = go.layout.Template(
    layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                    legend=dict(orientation='h',y=1.1),
                    autosize=True, font=dict(family='Montserrat')))

SUMMARY_PAGE = sm.render_summary_page()
DETAILED_SKILLS_PAGE = sdp.render_detailed_skills()

# app structure
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url("profile.jpg"), className='profileImage'),
            html.Div([
                dcc.Markdown(
                    # CHANGE YOUR INFO HERE-------------------------------------
                    """
                    **Name:** Pikatchu\n
                    **Surname:** Not Identified\n
                    **Phone #:** +42045845124575\n
                    **E-mail:** pikatchu@pikatchuemail.com\n
                    **Highest Education:** BC in Statistics\n
                    """
                ),
                html.A(
                    [html.Img(src=app.get_asset_url("LinkedIn-logo.png"), className='socialLogos')],
                    title="LinkedIn",
                    # CHANGE YOUR INFO HERE-------------------------------------
                    href="https://www.linkedin.com/in/morta-vilkaite/",
                    target="_blank"
                ),
                html.A(
                    [html.Img(src=app.get_asset_url("github.png"), className='socialLogos')],
                    title="Github",
                    # CHANGE YOUR INFO HERE-------------------------------------
                    href="https://github.com/MortaV",
                    target="_blank"
                ),
                html.A(
                    [html.Img(src=app.get_asset_url("kaggle.webp"), className='socialLogos')],
                    title="Kaggle",
                    # CHANGE YOUR INFO HERE-------------------------------------
                    href="https://www.kaggle.com/forgetmenot",
                    target="_blank"
                ),
                dcc.Markdown(
                    """
                    **Use cases**:
                    """
                ),
                # CHANGE YOUR INFO HERE-----------------------------------------
                html.A(
                    ["1. Image Classifier"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity-Image-Classifier",
                    target="_blank"
                ),
                html.P("\n"),
                # CHANGE YOUR INFO HERE-----------------------------------------
                html.A(
                    ["2. Finding Donors - PCA and Classification"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity-Finding-Donors",
                    target="_blank"
                ),
                html.P("\n"),
                # CHANGE YOUR INFO HERE-----------------------------------------
                html.A(
                    ["3. Text Analysis for Disaster Response"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity_Disaster_Response",
                    target="_blank"
                ),
                html.P("\n"),
                # CHANGE YOUR INFO HERE-----------------------------------------
                html.A(
                    ["4. Customer Segmentation"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity-Customer-Segmentation",
                    target="_blank"
                )
            ], className="markdownText"),
        ], className='item1', id="blackSidebar"),
        html.Div([
            html.Div([
                # CHANGE YOUR INFO HERE-----------------------------------------
                html.H1("Data Analyst"),
                dcc.Markdown(
                    # CHANGE YOUR INFO HERE-------------------------------------
                    """
                    Some text here were the girls can higlight **the main things**
                    about their career or what they are looking for.
                    """
                )
            ], className="headerContainer item2"),
            dcc.Tabs([
                SUMMARY_PAGE,
                DETAILED_SKILLS_PAGE
            ]),
        ], className="flexContainer2 item1"),
    ], className="flexContainer1")
])

# adding the callback for dropdown (skills graph)
@app.callback(
    Output('skills-graph', 'figure'),
    [Input('skills-dropdown', 'value')])
def update_skills(selected_type):
    filtered_df = skills[skills['type'] == selected_type]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=filtered_df["skills"], y=filtered_df["rating"],
            text=filtered_df["rating"],
            textposition="inside",
            textfont=dict(
                family="Montserrat",
                size=20,
                color="#FFFFFF"
            ),
        marker=dict(color=colors_array[1], opacity=0.6)
        )
    )

    fig.update_layout(transition_duration=500, template=layout_custom)

    fig.update_xaxes(title_text = "")

    fig.update_yaxes(title_text = "Rating", range=[0, 10])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
