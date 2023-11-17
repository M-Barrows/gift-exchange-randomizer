import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
import json
import random
import logging

dash.register_page(
    __name__,
    path='/',
    title='Secret Gift Pairing Generator',
    name='Secret Gift Pairing Generator'
    )

form_input = dbc.Textarea(
    'form-input', size='lg',
    placeholder= """ Enter your participants in JSON format like below:
{
    "familyA": [
        "person6",
        "person7"
    ],
    "familyB": [
        "person8",
        "person9",
        "person10",
        "person11"
    ]
}
    """,
    invalid=True,style = {"margin-bottom":"2em"}
)

pairings_results = dbc.Card([
    dbc.CardHeader('Matches'),
    dbc.CardBody('',id='card-body')
])

layout =  dbc.Container([
    html.H1(["Secret Gift Pairing Generator"]),
    form_input,
    pairings_results
])

def validate_json(value:str):
    try:
        json.loads(value) # put JSON-data to a variable
    except json.decoder.JSONDecodeError:
        return True
    else:
        return False
    
def get_giftee_options(family_structure:dict,current_family:str,output:dict)->list:
    """Returns the giftees who are not in the same family that don't have an assigned gifter yet"""

    options = []
    for family, people in family_structure.items():
        if family is not current_family: 
            for person in people: 
                if person not in output.get('Giftees'):
                    options.append(person)
    return options

def assign_pairings(family_structure:dict) -> dict:
    """
    Select a random giftee for each gifter. Ensure the pair are not in the same family. 
    """
    output = {
        'Gifters':[],
        'Giftees':[]
    }
    family_structure = json.loads(family_structure)
    for family,people in family_structure.items():
        for person in people:
            output.get('Gifters').append(person)
            try: 
                output.get('Giftees').append(random.choice(get_giftee_options(family_structure,family,output)))
            except IndexError:
                logging.warning('Could not generate even pairings. Re-running...')
    return output

def print_pairings(output:dict) -> None:
    """ 
    Prints pairings in a human-readable format
    """
    pairings = list()
    for i,x in enumerate(output.get('Gifters')):
        pairings.append((x,output.get('Giftees')[i]))
    content = []
    for pairing in pairings:
        content.append(html.P(f'{" ➡️ ".join(pairing)}'))
    return content

@callback(
        Output('form-input','invalid'),
        Input('form-input','value')
)
def validate_input(form_input):
    return validate_json(form_input)

@callback(
    Output('card-body','children'),
    Input('form-input','value')
)
def show_pairings(form_input):
    output = assign_pairings(form_input)
    while len(output.get('Giftees')) != len(output.get('Gifters')):
        output = assign_pairings(form_input)
    return print_pairings(output)
