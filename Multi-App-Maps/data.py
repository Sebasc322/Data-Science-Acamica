import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./datasets").resolve()

#data1
data = pd.read_csv(DATA_PATH.joinpath("DS_Proyecto_01_Datos_Properati_imput.csv"))
data = pd.DataFrame(data)

#data2
precio_barrio2 = pd.read_csv(DATA_PATH.joinpath("precio_barrio2.csv"))
precio_barrio2 = pd.DataFrame(precio_barrio2)