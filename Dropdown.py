import dash
from dash import dcc, html
from dash.dependencies import Output, Input, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import plotly
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("coupons.csv")
df.info()
app.layout = html.Div([

    html.Div([
        html.Br(),
        dcc.RadioItems(options=[
            {'label': 'All Coupons', 'value': 'all'},
            {'label': 'Accepted', 'value': 'accepted'},
            {'label': 'Rejected', 'value': 'rejected'}],
            value='all',
            labelStyle={'display': 'inline-block'},
            id='coupon_status'
        ),
        html.Br()]),

    html.Div([
        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
                     options=[
                         {'label': 'Coupon', 'value': 'coupon'},
                         {'label': 'Marital Status', 'value': 'maritalStatus'},
                         {'label': 'Education', 'value': 'Education'},
                         {'label': '# Children', 'value': 'has_children'},
                         {'label': 'Age', 'value': 'age'}
                     ],
                     optionHeight=35,  # height/space between dropdown options
                     value='coupon',  # dropdown value selected automatically when page loads
                     disabled=False,  # disable dropdown value selection
                     multi=False,  # allow multiple dropdown values to be selected
                     searchable=True,  # allow user-searching of dropdown values
                     search_value='',  # remembers the value searched in dropdown
                     placeholder='Please select...',  # gray, default text shown when no option is selected
                     clearable=True,  # allow user to removes the selected value
                     style={'width': "100%"},  # use dictionary to define CSS styles of your dropdown
                     # className='select_box',           #activate separate CSS document in assets folder
                     persistence=True,  # remembers dropdown value. Used with persistence_type
                     persistence_type='memory'  # remembers dropdown value selected until...
                     )
    ], className='three columns'),  # changed from 4 to 3 columns

    html.Br(),
    html.Div([
        dcc.Graph(id='our_graph')
    ], className='nine columns')

])

#---------------------------------------------------------------
# Select Dataframe

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
     Input(component_id='coupon_status', component_property='value')]
)

def build_graph(column_chosen, coupon_status):
    if coupon_status == 'all':
        dff = df
    elif coupon_status == 'accepted':
        dff = df[(df['Y'] == 1)]
    elif coupon_status == 'rejected':
        dff = df[(df['Y'] == 0)]
    else:
        dff = df  # Default case, no filter applied

    fig = px.histogram(dff, x=column_chosen, color='coupon')
    return fig

#---------------------------------------------------------------
# For tutorial purposes to show the user the search_value
#---------------------------------------------------------------


if __name__ == '__main__':
    app.run_server(debug=True, port=9000)


