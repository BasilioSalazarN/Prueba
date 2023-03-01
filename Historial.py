import numpy as np
import streamlit as st
import pandas as pd
#import psycopg2
from urllib.parse import urlparse

uri=st.secrets.db_credentials.URI
result = urlparse(uri)
hostname = result.hostname
database = result.path[1:]
username = result.username
pwd = result.password
port_id = result.port
con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro", con)
data_2_r = data_1_r.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)
  
data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,horas,reporte from capacitaciones", con)
data_2_C = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros", con)
data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

nombre_r=data_2_r.iloc[:,0]
nombre_c=data_2_c.iloc[:,0]
nombre_o=data_2_o.iloc[:,0]

fecha_r=data_2_r.iloc[:,0]
fecha_c=data_2_c.iloc[:,0]
fecha_o=data_2_o.iloc[:,0]


nombre=str.cat(nombre_r,nombre_c,nombre_o)

d = {'col1':nombre}
df = pd.DataFrame(data=d)

st.dataframe(d=df)
