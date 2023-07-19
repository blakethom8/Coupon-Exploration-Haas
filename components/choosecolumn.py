
from dash import dcc, html, Output, Input, callback




choosecolumn = dcc.Dropdown(id='my_dropdown',
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

def choose_column_dropdown(id):
    return dcc.Dropdown(id=id,
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