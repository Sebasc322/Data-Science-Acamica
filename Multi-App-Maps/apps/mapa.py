import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import plotly.express as px
from plotly import graph_objs as go
from urllib.request import urlopen

from data import data, precio_barrio2

px.set_mapbox_access_token("pk.eyJ1Ijoic2ViYXNjMzIyIiwiYSI6ImNraGR4Zm93eDA3YnoyeG94cnBvMW9zcDUifQ.4QOtyd2kj4SIZmC2rKRl4Q")

fig1 = px.scatter_mapbox(
    data,
    lat="lat", lon="lon",
    color="l2",
    hover_name="property_type",
    size="price",
    hover_data=["price", "l3"],
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10, height=1000,
    center={"lat":-34.60652, "lon":-58.43557}
    )

fig2 = px.scatter_mapbox(
    precio_barrio2,
    lat="lat", lon="lon",
    color="l2",
    hover_name="l3",
    size="price",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10, height=1000,
    center={"lat":-34.60652, "lon":-58.43557}
    )


layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                         html.Div(
                                            'MAPA DE BUENOS AIRES',
                                            className='mb-5 display-4 font-weight-bold text-home-title text-light font-medium title-visor'
                                         ),
                                    ],
                                    className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                                ),
                            ],
                            className='text-left p-5'
                        ),
                    ],
                    className='px-5 mx-5 back-home',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    'Distribución de propiedades en Buenos Aires',
                                    className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                                ),
                                html.Div(
                                    [
                                        html.P(
                                            """
                                            Los mapas fueron generados con la librería Plotly.
                                            """
                                        ),
                                    ],
                                    className='text-left pl-5 pr-5 text-center'
                                ),
                                dcc.Tabs(
                                    value = 'mapas',
                                    colors={
                                        "border": "white",
                                        "primary": "#59a0f1 ",
                                        "background": "#daecf5"
                                    },
                                    parent_className='div-for-tab',
                                    children=[
                                        dcc.Tab(
                                            label = 'Propiedades Vs. Precio',
                                            #value = 'num_contratos',
                                            children=[
                                                dcc.Graph(figure=fig1, className='div-for-graph-border')
                                            ],
                                            className='div-for-tab',
                                            selected_className='font-weight-bold',
                                        ),
                                        dcc.Tab(
                                            label = 'Barrios Vs. Precio ',
                                            #value = 'cuantia_contratos',
                                            children=[
                                                dcc.Graph(figure=fig2, className='div-for-graph-border')
                                            ],
                                            className='div-for-tab',
                                            selected_className='font-weight-bold',
                                        )
                                    ]
                                )
                            ],
                            className='col div-for-graph-card'
                        ),
                    ],
                    className='row',
                ),
            ],
            className='mb-5',
        ),
    ]
)
