# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def Ubicacion(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_17= st.sidebar.empty()
  titulo= placeholder1_17.title("Menú")

  placeholder2_17 = st.sidebar.empty()
  procesos_17 = placeholder2_17.button("Procesos",key="procesos_17")

  placeholder3_17 = st.sidebar.empty()
  historial_17 = placeholder3_17.button("Historial",key="historial_17")

  placeholder4_17 = st.sidebar.empty()
  capacitacion_17 = placeholder4_17.button("Capacitaciones",key="capacitacion_17")

  placeholder5_17 = st.sidebar.empty()
  otros_registros_17 = placeholder5_17.button("Otros Registros",key="otros_registros_17")

  placeholder6_17 = st.sidebar.empty()
  bonos_17 = placeholder6_17.button("Bonos",key="bonos_17")

  placeholder7_17 = st.sidebar.empty()
  salir_17 = placeholder7_17.button("Salir",key="salir_17")

  placeholder8_17 = st.empty()
  ubicacion_17 = placeholder8_17.title("Ubicación")

  default_date_17 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_17= st.empty()
  fecha_17= placeholder9_17.date_input("Fecha",value=default_date_17,key="fecha_17")

  placeholder10_17= st.empty()
  bloque_17= placeholder10_17.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_17")
    
  placeholder11_17= st.empty()
  estado_17= placeholder11_17.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_17")
       
  placeholder12_17= st.empty()
  tipo_17= placeholder12_17.selectbox("Tipo", options=("Ordinario","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_17")
       
  placeholder13_17= st.empty()
  planos_17= placeholder13_17.number_input("Cantidad de Planos Producidos",min_value=0,step=1,key="predios_17")

  placeholder14_17= st.empty()
  horas_17= placeholder14_17.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_17")

  placeholder15_17 = st.empty()
  reporte_17 = placeholder15_17.button("Generar Reporte",key="reporte_17")

  # ----- Procesos ---- #
    
  if procesos_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Procesos=False
    st.session_state.Ubicacion=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Ubicacion=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Ubicacion=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Ubicacion=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Ubicacion=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

  # ----- Salir ---- #
    
  elif salir_17:
    placeholder1_17.empty()
    placeholder2_17.empty()
    placeholder3_17.empty()
    placeholder4_17.empty()
    placeholder5_17.empty()
    placeholder6_17.empty()
    placeholder7_17.empty()
    placeholder8_17.empty()
    placeholder9_17.empty()
    placeholder10_17.empty()
    placeholder11_17.empty()
    placeholder12_17.empty()
    placeholder13_17.empty()
    placeholder14_17.empty()
    placeholder15_17.empty()
    st.session_state.Ingreso = False
    st.session_state.Ubicacion=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_17:

    cursor01=con.cursor()

    marca_17=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_17= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_17 = nombre_17.loc[0,'nombre']
      
    horario_17= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_17 = horario_17.loc[0,'horario']

    supervisor_17= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_17 = supervisor_17.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_17}','{usuario}','{nombre_17}','{horario_17}','{puesto}','{supervisor_17}','Ubicación','{fecha_17}','{bloque_17}','{estado_17}','{tipo_17}','{planos_17}','{horas_17}')")
    con.commit()
    st.success('Reporte enviado correctamente')
