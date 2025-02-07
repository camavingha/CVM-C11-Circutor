import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random

import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#7FDBFF'}, children=[
    html.H1(
        children='Power Management Dashboard',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }
    ),
    html.Div(children='A high-tech electrical theme dashboard.', style={
        'textAlign': 'center',
        'color': '#7FDBFF'
    }),
    dcc.Graph(
        id='power-graph',
        config={'displayModeBar': False}
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output('power-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    # Generate random data for demonstration
    x = list(range(10))
    y = [random.randint(0, 100) for _ in range(10)]

    data = go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        name='Power Consumption',
        line=dict(color='#FF5733')
    )

    return {
        'data': [data],
        'layout': go.Layout(
            title='Live Power Consumption',
            xaxis=dict(range=[min(x), max(x)]),
            yaxis=dict(range=[0, 100]),
            plot_bgcolor='#111111',
            paper_bgcolor='#111111',
            font=dict(color='#7FDBFF')
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)

    # Additional CSS for styling
    app.css.append_css({
        'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    })

    # Adding a logo and footer
    app.layout.children.insert(0, html.Img(src='/assets/logo.png', style={'height': '10%', 'width': '10%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}))
    app.layout.children.append(html.Footer(children='© 2023 Power Management Inc.', style={'textAlign': 'center', 'color': '#7FDBFF', 'padding': '10px', 'position': 'fixed', 'left': '0', 'bottom': '0', 'width': '100%', 'backgroundColor': '#111111'}))