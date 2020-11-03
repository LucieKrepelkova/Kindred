import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt

import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output, State

# importing the data
skills_in_detail = pd.read_csv("data/skills_in_detail.csv")

def render_detailed_skills():
    """Renders detailed skills tab"""
    DETAILED_SKILLS_PAGE = dcc.Tab(label="Data Knowledge in Detail", children=[
        html.Div([
            html.Div([
                html.H2("Skills in Detail"),
                dt.DataTable(
                    id='table-exp',
                    sort_action='native',
                    style_data={'whiteSpace': 'pre-line'},
                    style_cell={
                        'padding': '15px',
                        'width': 'auto',
                        'textAlign': 'left'
                    },
                    columns=[{"name": i.title(), "id": i} for i in skills_in_detail.columns],
                    data=skills_in_detail.to_dict("records")
                ),
            ], className="item3", id="tableSkills"),
        ],  className="flexContainer3 item2")
    ])
    return DETAILED_SKILLS_PAGE
