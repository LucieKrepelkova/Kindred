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

app = dash.Dash(__name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

certifications = pd.read_csv(
    os.path.join(APP_PATH, os.path.join("data", "certifications.csv"))
)
hobbies = pd.read_csv(
    os.path.join(APP_PATH, os.path.join("data", "hobbies.csv"))
)
jobs = pd.read_csv(
    os.path.join(APP_PATH, os.path.join("data", "jobs.csv"))
)
skills = pd.read_csv(
    os.path.join(APP_PATH, os.path.join("data", "skills.csv"))
)

available_types = skills['type'].unique()


colors_array = ['#e30613', '#000000', '#808B96', '#FFFFFF']

layout_custom = go.layout.Template(
    layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                    legend=dict(orientation='h',y=1.1),
                    autosize=True))

hobbies_fig = px.scatter(
    hobbies, x='hobby', y='frequency', size='importance',
    color='type', color_discrete_sequence=colors_array)

hobbies_fig.update_layout(transition_duration=500, template=layout_custom)

hobbies_fig.update_xaxes(title_text = "")
hobbies_fig.update_yaxes(title_text = "Frequency (times per week)")

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                [
                    html.Img(src=app.get_asset_url("profile.jpg"), className='profile-image'),
                    html.Div(
                    [
                        dcc.Markdown
                        (
                            """
                            **Name:** Pikatchu\n
                            **Surname:** Not Identified\n
                            **Phone #:** +42045845124575\n
                            **E-mail:** pikatchu@pikatchuemail.com\n
                            LinkedIn\n
                            GitHub\n
                            \n
                            \n
                            **Use cases**:\n
                            Use case number 1\n
                            Use case number 2\n
                            Use case number 3\n
                            Use case number 4
                            """
                        )
                    ], className="markdown-text"),
                ], className='sidebar'),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                [
                                    html.H3("Work Experience"),
                                    dt.DataTable(
                                        id='table-work-job',
                                        style_cell={
                                            'padding': '15px',
                                            'width': 'auto',
                                            'textAlign': 'center'
                                        },
                                        columns=[{"name": i.title(), "id": i} for i in jobs.columns],
                                        data=jobs.to_dict("rows")
                                    )
                                ], className="four-columns",
                                ),
                                html.Div(
                                [
                                    html.H3("Skills"),
                                    dcc.Dropdown(
                                        id='skills-dropdown',
                                        options=[{'label': i, 'value': i} for i in available_types],
                                        value=available_types[0]
                                    ),
                                    dcc.Graph(id="skills-graph")
                                ], className="four-columns"),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [dcc.Graph(id="count_graph")],
                            id="countGraphContainer",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="main_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="individual_graph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="pie_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="aggregate_graph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

@app.callback(
    Output('skills-graph', 'figure'),
    [Input('skills-dropdown', 'value')])
def update_figure(selected_type):
    filtered_df = skills[skills['type'] == selected_type]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df["skills"], y=filtered_df["rating"],
        marker=dict(color=colors_array[0], opacity=0.6)
        )
    )

    fig.update_layout(transition_duration=500, template=layout_custom)

    fig.update_xaxes(title_text = "Skill")

    fig.update_yaxes(title_text = "Rating", range=[0, 10])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
