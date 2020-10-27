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
skills_in_detail = pd.read_csv(
    os.path.join(APP_PATH, os.path.join("data", "skills_in_detail.csv"))
)

skills=skills.sort_values(by='rating', ascending = False)

available_types = skills['type'].unique()


colors_array = ['#e30613', '#000000', '#808B96', '#FFFFFF']

layout_custom = go.layout.Template(
    layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                    legend=dict(orientation='h',y=1.1),
                    autosize=True, font=dict(family='Montserrat')))

hobbies_fig = px.scatter(
    hobbies, x='hobby', y='frequency', size='importance',
    color='type', color_discrete_sequence=colors_array)

hobbies_fig.update_layout(transition_duration=500, template=layout_custom)

hobbies_fig.update_xaxes(title_text = "")
hobbies_fig.update_yaxes(title_text = "Frequency (times per week)")

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url("profile.jpg"), className='profileImage'),
            html.Div([
                dcc.Markdown(
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
                    href="https://www.linkedin.com/in/morta-vilkaite/",
                    target="_blank"
                ),
                html.A(
                    [html.Img(src=app.get_asset_url("github.png"), className='socialLogos')],
                    title="Github",
                    href="https://github.com/MortaV",
                    target="_blank"
                ),
                html.A(
                    [html.Img(src=app.get_asset_url("kaggle.webp"), className='socialLogos')],
                    title="Kaggle",
                    href="https://www.kaggle.com/forgetmenot",
                    target="_blank"
                ),
                dcc.Markdown(
                    """
                    **Use cases**:
                    """
                ),
                html.A(
                    ["1. Image Classifier"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity-Image-Classifier",
                    target="_blank"
                ),
                html.P("\n"),
                html.A(
                    ["2. Finding Donors - PCA and Classification"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity-Finding-Donors",
                    target="_blank"
                ),
                html.P("\n"),
                html.A(
                    ["3. Text Analysis for Disaster Response"],
                    title="Use case",
                    href="https://github.com/MortaV/Udacity_Disaster_Response",
                    target="_blank"
                ),
                html.P("\n"),
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
                html.H1("Data Analyst"),
                dcc.Markdown(
                    """
                    Some text here were the girls can higlight **the main things**
                    about their career or what they are looking for.
                    """
                )
            ], className="headerContainer item2"),
            dcc.Tabs([
                dcc.Tab(label="Summary", children=[
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
                                dcc.Graph(id="hobby-graph", figure=hobbies_fig)
                            ], id="hobby-graph-container"),
                        ], className="item4", id="tableHobbies"),
                    ], className="flexContainer3 item2"),
                ]),
                dcc.Tab(label="Data Knowledge in Detail", children=[
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
                ]),
            ]),
        ], className="flexContainer2 item1"),
    ], className="flexContainer1")
])

@app.callback(
    Output('skills-graph', 'figure'),
    [Input('skills-dropdown', 'value')])
def update_figure(selected_type):
    filtered_df = skills[skills['type'] == selected_type]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df["skills"], y=filtered_df["rating"],
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
