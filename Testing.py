# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def Testing(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_16= st.sidebar.empty()
  titulo= placeholder1_16.title("Menú")

  placeholder2_16 = st.sidebar.empty()
  procesos_16 = placeholder2_16.button("Procesos",key="procesos_16")

  placeholder3_16 = st.sidebar.empty()
  historial_16 = placeholder3_16.button("Historial",key="historial_16")

  placeholder4_16 = st.sidebar.empty()
  capacitacion_16 = placeholder4_16.button("Capacitaciones",key="capacitacion_16")

  placeholder5_16 = st.sidebar.empty()
  otros_registros_16 = placeholder5_16.button("Otros Registros",key="otros_registros_16")

  placeholder6_16 = st.sidebar.empty()
  bonos_16 = placeholder6_16.button("Bonos",key="bonos_16")

  placeholder7_16 = st.sidebar.empty()
  salir_16 = placeholder7_16.button("Salir",key="salir_16")

  placeholder8_16 = st.empty()
  conformacion_16 = placeholder8_16.title("Testing")

  default_date_16 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_16= st.empty()
  fecha_16= placeholder9_16.date_input("Fecha",value=default_date_16,key="fecha_16")

  placeholder10_16= st.empty()
  bloque_16= placeholder10_16.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_16")
    
  placeholder11_16= st.empty()
  estado_16= placeholder11_16.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_16")
       
  placeholder12_16= st.empty()
  tipo_16= placeholder12_16.selectbox("Tipo", options=("Ordinario","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_16")
       
  placeholder13_16= st.empty()
  predios_16= placeholder13_16.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_16")

  placeholder14_16= st.empty()
  horas_16= placeholder14_16.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_16")

  placeholder15_16 = st.empty()
  reporte_16 = placeholder15_16.button("Generar Reporte",key="reporte_16")

  # ----- Procesos ---- #
    
  if procesos_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Procesos=False
    st.session_state.Testing=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Testing=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Testing=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Testing=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Testing=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

  # ----- Salir ---- #
    
  elif salir_16:
    placeholder1_16.empty()
    placeholder2_16.empty()
    placeholder3_16.empty()
    placeholder4_16.empty()
    placeholder5_16.empty()
    placeholder6_16.empty()
    placeholder7_16.empty()
    placeholder8_16.empty()
    placeholder9_16.empty()
    placeholder10_16.empty()
    placeholder11_16.empty()
    placeholder12_16.empty()
    placeholder13_16.empty()
    placeholder14_16.empty()
    placeholder15_16.empty()
    st.session_state.Ingreso = False
    st.session_state.Testing=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_16:

    cursor01=con.cursor()

    marca_16=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_16= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_16 = nombre_16.loc[0,'nombre']
      
    horario_16= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_16 = horario_16.loc[0,'horario']

    supervisor_16= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_16 = supervisor_16.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_16}','{usuario}','{nombre_16}','{horario_16}','{puesto}','{supervisor_16}','Testing','{fecha_16}','{bloque_16}','{estado_16}','{tipo_16}','{predios_16}','{horas_16}')")
    con.commit()
    st.success('Reporte enviado correctamente')