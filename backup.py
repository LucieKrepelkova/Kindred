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
    style={"display": "flex", "flex-direction": "column"},
    children=[
    html.Div(
        className='sidebar',
        children=[
        html.Img(src=app.get_asset_url("profile.jpg"), className='profile-image'),
        dcc.Markdown("""
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
            """)
    ]),
    html.Div(
        className="row flex-display",
        children=[
        html.Div(
            className="row container-display",
            children=[
            html.Div(
                [
                html.H2("Work Experience"),
                dt.DataTable(
                    id='table-work',
                    style_cell={
                        'padding': '15px',
                        'width': 'auto',
                        'textAlign': 'center'
                    },
                    columns=[{"name": i.title(), "id": i} for i in jobs.columns],
                    data=jobs.to_dict("rows")
                )
            ], style={
                'padding': '10px 5px'
            }),
            html.Div(
                className="row container-display",
                children=[
                html.H2("Skills (from 1 to 10)"),
                dcc.Dropdown(
                    id='skills-dropdown',
                    options=[{'label': i, 'value': i} for i in available_types],
                    value=available_types[0]
                ),
                dcc.Graph(id='skills-graph')
            ]),

        ], style={'columnCount': 2}),
        html.Div(
            className="row flex-display",
            children=[
            html.Div(
                className="row container-display",
                children=[
                html.Div(
                    className="mini_container",
                    children=[html.H2("Certifications"),
                    dt.DataTable(
                        id='table-certifications',
                        style_cell={
                            'padding': '15px',
                            'width': 'auto',
                            'textAlign': 'center'
                        },
                        columns=[{"name": i.title(), "id": i} for i in certifications.columns],
                        data=certifications.to_dict("rows")
                    )
                ]),
                html.Div(
                    className="mini_container",
                    children=[
                    html.H2("Hobbies"),
                    dcc.Graph(
                        id='hobbies-graph',
                        figure=hobbies_fig
                    )
                ]),
            ]),
        ], style={'columnCount': 2}),
    ]),
])

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
