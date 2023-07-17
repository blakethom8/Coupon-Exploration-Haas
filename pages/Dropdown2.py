import dash
from dash import dcc, html, Output, Input, callback
import plotly.express as px
import plotly.graph_objects as go
import plotly
import dash_bootstrap_components as dbc
import pandas as pd


dash.register_page(__name__, name='Coupon Charts')

df = pd.read_csv("coupons.csv")
# df.info()

# List of columns that we would like to explore
unique_weather = df['weather'].unique()
unique_income = df['income'].unique()
unique_education = df['education'].unique()
unique_destination = df['destination'].unique()
unique_passanger = df['passanger'].unique()
unique_time = df['time'].unique()
unique_expiration = df['expiration'].unique()
unique_age = df['age'].unique()
unique_gender = df['gender'].unique()

#-------------------------------------------------------------------------------------
# Function that creates a multi-select dropdown for each of the column in the dictionary
def generate_dropdowns():
    dictionary = [
        {"label": "Weather", "id": "weather_dropdown", "values": unique_weather},
        {"label": "Income", "id": "income_dropdown", "values": unique_income},
        {"label": "Education", "id": "education_dropdown", "values": unique_education},
        {"label": "Destination", "id": "destination_dropdown", "values": unique_destination},
        {"label": "Passanger", "id": "passanger_dropdown", "values": unique_passanger},
        {"label": "Time", "id": "time_dropdown", "values": unique_time},
        {"label": "Expiration", "id": "expiration_dropdown", "values": unique_expiration},
        {"label": "Age", "id": "age_dropdown", "values": unique_age},
        {"label": "Gender", "id": "gender_dropdown", "values": unique_gender},
    ]


    dropdowns = []
    rows = [dictionary[i:i + 5] for i in
            range(0, len(dictionary), 5)]  # divide dictionary into rows with up to 5 items each

    for row in rows:
        width = 100 / len(row)  # calculate width based on the number of items in the row
        for item in row:
            dropdown = html.Div([
                html.Label(item["label"]),
                dcc.Dropdown(
                    id=item['id'],
                    options=[{'label': i, 'value': i} for i in item['values']],
                    multi=True),
            ], style={'width': f'{width}%', 'display': 'inline-block'})
            dropdowns.append(dropdown)
        dropdowns.append(html.Br())  # add a line break after each row
    return dropdowns


#-------------------------------------------------------------------------------------
layout = html.Div([

    # -------------------------------------------------------------------------------------
    # Main content
    html.Div([

        html.Div(generate_dropdowns()),

        # -------------------------------------------------------------------------------------
        # Clear filter Button
        html.Div([
        html.Button('Clear Filters', id='clear-button', n_clicks=0),
        ]),
        #-------------------------------------------------------------------------------------
        # Master Dropdown that impacts table categories
        html.Div([

            html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

            dcc.Dropdown(id='my_dropdown',
                         options=[
                             {'label': 'Coupon', 'value': 'coupon'},
                             {'label': 'Marital Status', 'value': 'maritalStatus'},
                             {'label': 'Education', 'value': 'Education'},
                             {'label': '# Children', 'value': 'has_children'},
                             {'label': 'Age', 'value': 'age'},
                             {'label': 'Destination', 'value': 'destination'},
                             {'label': 'Gender', 'value': 'gender'},
                             {'label': 'Expiration', 'value': 'expiration'},
                             {'label': 'Time', 'value': 'time'},
                             {'label': 'Weather', 'value': 'weather'},

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
        ], style={'display': 'inline-block', 'width': '90%', 'height': '100px'}),  # changed from 4 to 3 columns

        #-------------------------------------------------------------------------------------
        # Add Grouped Bar Graphs

        html.Div(
             dcc.Graph(id = 'bar_graph'), style={'display': 'inline-block', 'width': '90%'}
        ),

                # -------------------------------------------------------------------------------------
        # Add Drop Downs for Filtering
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

        # -------------------------------------------------------------------------------------
        # Add side by side graphs

        html.Div([
            html.Div(dcc.Graph(id='our_graph'), style={'display': 'inline-block', 'width': '49%', 'height': '500px'}),
            html.Div(dcc.Graph(id='our_graph2'), style={'display': 'inline-block', 'width': '49%', 'height': '500px'})
        ]),



    ],
        # style=CONTENT_STYLE
    ),

])



#---------------------------------------------------------------
# Connecting the Dropdown values to the graph to use as data filters
    # function immediately below is used to show the unique values of the columns that we use for dropdown filters
def filter_dataframe(df, column, values):
    if values:
        return df[df[column].isin(values)]
    else:
        return df

    # callback below is used to update the graph based on the filters applied from the dropdowns
@callback(
    [Output(component_id='our_graph', component_property='figure'),
     Output(component_id='our_graph2', component_property='figure'),
     # Output(component_id='our_graph3', component_property='figure')
     ],
    [
     Input(component_id='my_dropdown', component_property='value'),
     Input(component_id='coupon_status', component_property='value'),
     Input(component_id='weather_dropdown', component_property='value'),
     Input(component_id='income_dropdown', component_property='value'),
     Input(component_id='education_dropdown', component_property='value'),
     Input(component_id='destination_dropdown', component_property='value'),
     Input(component_id='passanger_dropdown', component_property='value'),
     Input(component_id='time_dropdown', component_property='value'),
     Input(component_id='expiration_dropdown', component_property='value'),
     Input(component_id='age_dropdown', component_property='value'),
     Input(component_id='gender_dropdown', component_property='value'),
     ]
)

def build_graph(column_chosen, coupon_status, selected_weather, selected_income, selected_education,
                selected_destination, selected_passanger, selected_time, selected_expiration, selected_age, selected_gender):
    if coupon_status == 'all':
        dff = df

    elif coupon_status == 'accepted':
        dff = df[(df['Y'] == 1)]
    elif coupon_status == 'rejected':
        dff = df[(df['Y'] == 0)]
    else:
        dff = df  # Default case, no filter applied

    dff = filter_dataframe(dff, 'weather', selected_weather)
    dff = filter_dataframe(dff, 'income', selected_income)
    dff = filter_dataframe(dff, 'education', selected_education)
    dff = filter_dataframe(dff, 'destination', selected_destination)
    dff = filter_dataframe(dff, 'passanger', selected_passanger)
    dff = filter_dataframe(dff, 'time', selected_time)
    dff = filter_dataframe(dff, 'expiration', selected_expiration)
    dff = filter_dataframe(dff, 'age', selected_age)
    dff = filter_dataframe(dff, 'gender', selected_gender)

    fig = px.histogram(dff, x=column_chosen, color='coupon')
    fig2 = px.histogram(dff, color=column_chosen, x='coupon')


    return fig, fig2

#---------------------------------------------------------------
# create grouped bar graph

@callback(
         Output(component_id='bar_graph', component_property='figure'),
    [
        Input(component_id='weather_dropdown', component_property='value'),
        Input(component_id='income_dropdown', component_property='value'),
        Input(component_id='education_dropdown', component_property='value'),
        Input(component_id='destination_dropdown', component_property='value'),
        Input(component_id='passanger_dropdown', component_property='value'),
        Input(component_id='time_dropdown', component_property='value'),
        Input(component_id='expiration_dropdown', component_property='value'),
        Input(component_id='age_dropdown', component_property='value'),
        Input(component_id='gender_dropdown', component_property='value'),
        Input(component_id='my_dropdown', component_property='value'),
    ]
)

def create_grouped_bar(selected_weather, selected_income, selected_education,
                selected_destination, selected_passanger, selected_time, selected_expiration, selected_age,
                selected_gender, column_chosen2):
    dffBar = df
    dffBar = filter_dataframe(dffBar, 'weather', selected_weather)
    dffBar = filter_dataframe(dffBar, 'income', selected_income)
    dffBar = filter_dataframe(dffBar, 'education', selected_education)
    dffBar = filter_dataframe(dffBar, 'destination', selected_destination)
    dffBar = filter_dataframe(dffBar, 'passanger', selected_passanger)
    dffBar = filter_dataframe(dffBar, 'time', selected_time)
    dffBar = filter_dataframe(dffBar, 'expiration', selected_expiration)
    dffBar = filter_dataframe(dffBar, 'age', selected_age)
    dffBar = filter_dataframe(dffBar, 'gender', selected_gender)
    accepted = dffBar[dffBar['Y'] == 1]
    acceptedDf = accepted.groupby(column_chosen2).size().reset_index().set_index(column_chosen2)
    acceptedDf.columns = ['Accepted']

    denied = dffBar[dffBar['Y'] == 0]
    deniedDf = denied.groupby(column_chosen2).size().reset_index().set_index(column_chosen2)
    deniedDf.columns = ['Denied']

    groupedDf = acceptedDf.merge(deniedDf, on=column_chosen2).reset_index()



    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=groupedDf[column_chosen2], y=groupedDf['Accepted'], name='Accepted'))
    fig_bar.add_trace(go.Bar(x=groupedDf[column_chosen2], y=groupedDf['Denied'], name='Denied'))
    fig_bar.update_layout(barmode='group', xaxis_title=column_chosen2, yaxis_title='Count', title='Grouped bar')


    return fig_bar


#---------------------------------------------------------------
# callback below is used to clear all dropdown filters

@callback(
    [Output('weather_dropdown', 'value'),
     Output('income_dropdown', 'value'),
     Output('education_dropdown', 'value'),
        Output('destination_dropdown', 'value'),
        Output('passanger_dropdown', 'value'),
        Output('time_dropdown', 'value'),
        Output('expiration_dropdown', 'value'),
        Output('age_dropdown', 'value'),
        Output('gender_dropdown', 'value')
     # add more outputs here for any additional dropdowns
    ],
    [Input('clear-button', 'n_clicks')]
)
def clear_filters(n_clicks):
    if n_clicks > 0:
        return [None]*9  # return a list of None values, one for each dropdown
    raise dash.exceptions.PreventUpdate