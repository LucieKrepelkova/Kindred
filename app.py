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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
    external_stylesheets=external_stylesheets,
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


colors_array = ['#00A9A4', '#F8B017', '#80D4D2', '#006562', '#F5911B', '#FCD88B']

layout_custom = go.layout.Template(
    layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                    legend=dict(orientation='h',y=-0.1)))

hobbies_fig = px.scatter(
    hobbies, x='hobby', y='frequency', size='importance',
    color='type', color_discrete_sequence=colors_array)

hobbies_fig.update_layout(
    title='Hobbies',
    transition_duration=500, template=layout_custom
)

hobbies_fig.update_xaxes(title_text = "")
hobbies_fig.update_yaxes(title_text = "Frequency (times per week)")

app.layout = html.Div([
    html.Div(
        className='column',
        children=[html.Img(src=app.get_asset_url("profile.jpg")),
        html.Div([
            dcc.Markdown("""

                **Name:** Pikatchu

                **Surname:** Not Identified

                **Phone #:** +42045845124575

                **E-mail:** pikatchu@pikatchuemail.com

                LinkedIn

                GitHub
                """)
        ], style = {'color': '#FFFFFF'}),
    ], style={
        'backgroundColor': 'rgb(52, 73, 94)',
        'padding': '10px 5px',
        'width': '20%'
    }),
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='skills-dropdown',
                    options=[{'label': i, 'value': i} for i in available_types],
                    value=available_types[0]
                ),
                dcc.Graph(id='skills-graph')
            ]),
            html.Div([
                dcc.Graph(
                    id='hobbies-graph',
                    figure=hobbies_fig
                )
            ])
        ], style={
            'padding': '10px 5px',
            'rowCount': 2
        }),
        html.Div([
            html.Div([
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
            html.Div([
                html.H2("Certifications"),
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
            ], style={
                'padding': '10px 5px'
            }),
        ], style={
            'padding': '10px 5px',
            'rowCount': 2
        })
    ], style={
        'padding': '10px 5px',
        'columnCount': 2
        })
], style={'columnCount': 2})

@app.callback(
    Output('skills-graph', 'figure'),
    [Input('skills-dropdown', 'value')])
def update_figure(selected_type):
    filtered_df = skills[skills['type'] == selected_type]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df["skills"], y=filtered_df["rating"],
        marker=dict(color=colors_array[1], opacity=0.4)
        )
    )

    fig.update_layout(
        title='Skills (out of 10)',
        transition_duration=500, template=layout_custom,

    )
    fig.update_xaxes(title_text = "Skill")

    fig.update_yaxes(title_text = "Rating", range=[0, 10])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
