# pseudo codigo
# main()
     #datos =get_data(filename)
     #reporte = generar_repor(datos)
     #save_data(reporte)
     

import encodings
from logging import root
import os 
import pathlib import path
import pandas as pd
def main():
    filename="llamadas123_julio_2022.csv"
    root_dir = path(".").reolve().parent
    data_dir = "raw"
    fil_path =os.path.join,(root_dir,"data",data_dir,filename)
    datos=pd.read_csv(fel)
    datos=pd.read_csv
    datos = get_data(filename)
    if __name__== "__main__":
        main()