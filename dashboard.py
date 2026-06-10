import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html

data = pd.read_csv(r'C:\Users\gyanr\OneDrive\Desktop\Dash\gapminder.csv')
print(data.head())

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        children=[
            html.H1("My First Dashboard",style={'color':'red','text-align':'center'})
        ],
        style={
            'border': '1px black solid',
            'float': 'left',
            'width': '100%',
            'height': '50px'
        }
    ),
    html.Div(
        children=[
            dcc.Graph(id='scatter-plot',
                      figure={'data':[go.Scatter(x=data['pop'],
                                                 y=data['gdpPercap'],
                                                 mode='markers')],
                              'layout':go.Layout(title='Scatter Plot')})
        ],
        style={
            'border': '1px black solid',
            'float': 'left',
            'width': '49%'
        }
    ),
    html.Div(
        children=[
            dcc.Graph(id='box-ploat',
                      figure={'data':[go.Box(x=data['gdpPercap'])],
                              'layout':go.Layout(title='Boxplot')})
        ],
        style={
            'border': '1px black solid',
            'float': 'left',
            'width': '49%'
        }
    )
])



if __name__ == "__main__":
    app.run(debug=True)
