import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from importlib import import_module
import warnings



from app import app
# El llamado de estos modulos tiene que estar DESPUES de que se crea el app.Dash
from apps import Home, mapa


server = app.server


prop_LOGO = "/assets/logos/isologo-properati-claim-1024x284.png"

warnings.filterwarnings("ignore")

navbar_children = dbc.NavbarSimple(
    [
        html.Div(
            [
                html.Div(
                    [
                        dbc.NavItem(
                            [
                        dbc.NavLink(
                            "Mapa",
                            href="/mapa",
                            className='text-uppercase btn-link font-weight-bold font-bold px-2'
                        ),
                            ]
                        ),
                    ],
                    className='row ml-5 pt-3'
                ),
            ],
        #className='row'
        ),
    ],
    className='mx-auto'
)


navbar = dbc.Navbar(
    [
    html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=prop_LOGO, height="30px")),
                ],
                className='mr-5',
            ),
            href="/",
        ),
    navbar_children,
    ],
    id='navbar',
    sticky="top"
)


footer = html.Footer(
    [
        html.Div(
            [
                html.Div(
                    [
                        'Sebastián Carmona Ángel - DS40'
                    ],
                    className='SCA'
                )
            ],
            className = 'container py-4'
        )
    ],
    style = {'background-color': '#343a40', 'color': '#aaaaaa'}
)




# define page layout
app.layout = html.Div(
    [
        html.Div(id='blank-output'), # only for the name in the tab
        dcc.Location(id="url", refresh=False),
        navbar,
        # Column for user controls (SIDE BAR)
        dcc.Loading(
            id="loading-1",
            type="circle",
            fullscreen=True,
            children=[
                html.Div(
                    id="content"
                ),
            ],
        ),
        footer
    ]
)



# create callback for modifying page layout
@app.callback(
    Output("content", "children"),
    [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return Home.layout
    if pathname == "/mapa":
        return mapa.layout
    # if not recognised, return home page
    return Home.layout



# create callback for modifying navbar
@app.callback(Output("navbar", "className"), [Input("url", "pathname")])
def display_navbar(pathname):
    # Navbar white if home
    if pathname == "/":
        return 'div-for-nav-white'
    # Else navbar white
    return 'div-for-nav-white'

# Changing name of
app.clientside_callback(
    """
    function(pathname) {
        if (pathname === '/') {
            document.title = 'Demo2 - Home'
        } else if (pathname === '/mapa') {
            document.title = 'Demo2 - Mapa'
        } else if (pathname === '/h/') {
            document.title = 'Demo2 - Home'
        }
    }
    """,
    Output('blank-output', 'children'),
    [Input("url", "pathname")]
)




if __name__ == "__main__":
    app.run_server(debug=True)