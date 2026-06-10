import numpy as np
import pandas as pd
import plotly.graph_objects as go

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# External CSS stylesheet (Bootstrap)
external_stylesheets = [
    {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        "crossorigin": "anonymous"
    }
]

# Load and process data
patients = pd.read_csv('C:\\Users\\gyanr\\OneDrive\\Desktop\\Dash\\Covid_19\\IndividualDetails.csv')
totalpatients = patients.shape[0]
active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deaths = patients[patients['current_status'] == 'Deceased'].shape[0]

# Dropdown options
options = [{'label':'All','value':'All'},
           {'label':'Hospitalized','value':'Hospitalized'},
           {'label':'Recovered','value':'Recovered'},
           {'label':'Deceased','value':'Deceased'}]


# Create Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("COVID-19 Virus Pandemic",style={'color':'#fff','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases',className='text-light'),
                    html.H4(totalpatients,className='text-light')
                ],className='card-body')
            ],className='card bg-danger') # Changed to bg-danger for red color
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases',className='text-light'),
                    html.H4(active,className='text-light')
                ],className='card-body')
            ],className='card bg-info') # Changed to bg-info for blue color
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered',className='text-light'),
                    html.H4(recovered,className='text-light')
                ],className='card-body')
            ],className='card bg-warning') # Changed to bg-warning for yellow color
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Death Cases',className='text-light'),
                    html.H4(deaths,className='text-light')
                ],className='card-body')
            ],className='card bg-success') # Changed to bg-success for green color
        ],className='col-md-3')
    ],className='row'),
    html.Div([],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar',figure={})
                ],className='card-body')
            ],className='card')
        ],className='col-md-12'),
    ],className='row'),
],className='container')

'''Faces some error''' 
# # Based user selected dropdown value then show the graph
# @app.callback(Output('bar', 'figure'),Input('picker', 'value'))
# def update_graph(type):
#     if type == 'All':
#         pbar = patients['detected_state'].value_counts().reset_index()
#         return {'data':[go.Bar(x=pbar['index'],y=pbar['detected_state'])],
#                 'layout':go.Layout(title='State-wise Cases')}# plotly graph object based on the selected type
#     else:
#         npat = patients[patients['current_status'] == type]
#         pbar = npat['detected_state'].value_counts().reset_index()
#         return {'data':[go.Bar(x=pbar['index'],y=pbar['detected_state'])],
#                 'layout':go.Layout(title='State-wise Cases')}# plotly graph object based on the selected type
    

@app.callback(
    Output('bar', 'figure'),
    Input('picker', 'value')
)
def update_graph(status):

    if status is None or status == 'All':
        df = (
            patients['detected_state']
            .value_counts()
            .reset_index(name='count')
        )
    else:
        df = (
            patients[patients['current_status'] == status]
            ['detected_state']
            .value_counts()
            .reset_index(name='count')
        )

    return {
        'data': [
            go.Bar(
                x=df['detected_state'],
                y=df['count']  
            )
        ],
        'layout': go.Layout(
            title='State-wise COVID-19 Cases',
            xaxis_title='State',
            yaxis_title='Number of Cases'
        )
    }


if __name__ == "__main__":
    app.run(debug=True)

