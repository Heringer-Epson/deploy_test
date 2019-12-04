import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dash_app.config.suppress_callback_exceptions = True
app = dash_app.server

dash_app.layout = html.Div(children=[

    html.Div(children='Example of Dash app'),

    html.H6('Currency:', style={'marginLeft': '3.0em', }),
    dcc.Dropdown(
        id='tab-test',
        options=[{'label': i, 'value': i} for i in ['USD', 'CAD']],
        value='USD',
        style={'width': '100px', 'marginLeft': '.5em'},
    ),

    html.Div(
        id='printer',
        style={'textAlign': 'center'},),

    dcc.Graph(id='figure-test'),

])

@dash_app.callback(Output('printer', 'figure'),
              [Input('tab-test', 'value')])
def tab_func(curr):
    return 'Currency is "{}'.format(curr)

@dash_app.callback(Output('figure-test', 'figure'),
              [Input('tab-test', 'value')])
def figure_func(aux):
    traces = []
    traces.append(go.Scattergl(
        x=[1,2,3],
        y=[1,2,3],
        mode='lines',
        opacity=1.,
        line=dict(color='#fdae61', width=3.),
        name='Linear',
    ))
    traces.append(go.Scattergl(
        x=[1,2,3],
        y=[1,4,9],
        mode='lines',
        opacity=1.,
        line=dict(color='#3288bd', width=3.),
        name='Quad',
    ))
    aux =aux
    return {
        'data': traces,
        'layout': dict(
        xaxis={'title': 'x label',},
        yaxis={'title': 'y label',},
        hovermode='closest',
        )          
    }

if __name__ == '__main__':
    dash_app.run_server(debug=True)
