import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table


# Section layout --------------------

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'BIENVENIDOS A MI DEMO!',
                            className='mb-5 display-4 font-weight-bold text-home-title text-light font-medium title-visor',
                        ),
                        html.Div(
                            [
                                html.P(
                                    """
                                    ¡ACÁ PODREMOS VER LA EXPLORACIÓN DE LOS DATOS (DESCRIBE) Y SU DISTRIBUCIÓN EN EL MAPA DE BUENOS AIRES!
                                    """,
                                    className='lead font-weight-normal text-light font-home-m'
                                ),
                            ],
                            className='mb-5',
                        ),
                    ],
                    className='col-md-5 p-lg-5 mx-auto my-5',
                ),
            ],
            className = 'position-relative overflow-hidden text-center back-home',
        ),
            html.Div(
                [
                    dbc.Row(
                        [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Img(src='/../assets/yo/sebastian.jpg', className='div-for-image-team'),
                                    html.Div('Sebastián Carmona Ángel',className='font-weight-bold text-names-team font-medium'),
                                    html.Div('Ingeniero de Petróleos, Especialista en Negocios Internacionales y Data Scientist',
                                        className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(className="fab fa-linkedin", style={'color': 'grey'}),
                                            href='https://www.linkedin.com/in/sebascarmona/', role="button",
                                        ),
                                        className='social',
                                    ),
                                ],
                                className='div-for-member mx-4'
                            ), xs=10, sm=12, md=12, lg=12, xl=12
                        ),
                    ]
                ),
            ],
        className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
        ),
    ],
)