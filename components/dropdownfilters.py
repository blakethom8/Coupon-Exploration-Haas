#-------------------------------------------------------------------------------------
# Function that creates a multi-select dropdown for each of the column in the dictionary


import dash
from dash import dcc, html, Output, Input, callback
from components import column_dictionary



def generate_dropdowns():
    dictionary = column_dictionary.column_dict

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