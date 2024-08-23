# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def Validacion(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_15= st.sidebar.empty()
  titulo= placeholder1_15.title("Menú")

  placeholder2_15 = st.sidebar.empty()
  procesos_15 = placeholder2_15.button("Procesos",key="procesos_15")

  placeholder3_15 = st.sidebar.empty()
  historial_15 = placeholder3_15.button("Historial",key="historial_15")

  placeholder4_15 = st.sidebar.empty()
  capacitacion_15 = placeholder4_15.button("Capacitaciones",key="capacitacion_15")

  placeholder5_15 = st.sidebar.empty()
  otros_registros_15 = placeholder5_15.button("Otros Registros",key="otros_registros_15")

  placeholder6_15 = st.sidebar.empty()
  bonos_15 = placeholder6_15.button("Bonos",key="bonos_15")

  placeholder7_15 = st.sidebar.empty()
  salir_15 = placeholder7_15.button("Salir",key="salir_15")

  placeholder8_15 = st.empty()
  validacion_15 = placeholder8_15.title("Validación")

  default_date_15 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_15= st.empty()
  fecha_15= placeholder9_15.date_input("Fecha",value=default_date_15,key="fecha_15")

  placeholder10_15= st.empty()
  bloque_15= placeholder10_15.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_15")
    
  placeholder11_15= st.empty()
  estado_15= placeholder11_15.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_15")
       
  placeholder12_15= st.empty()
  tipo_15= placeholder12_15.selectbox("Tipo", options=("Ordinario","Fincas No Ubicadas","Afectados"), key="tipo_15")

  placeholder13_15= st.empty()
  predios_15= placeholder13_15.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_15")

  placeholder14_15= st.empty()
  horas_15= placeholder14_15.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_15")

  placeholder15_15 = st.empty()
  reporte_15 = placeholder15_15.button("Generar Reporte",key="reporte_15")

  # ----- Procesos ---- #
    
  if procesos_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder4_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Procesos=False
    st.session_state.Validacion=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder14_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Validacion=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder4_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Validacion=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder4_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Validacion=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder4_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Validacion=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

    # ----- Salir ---- #
    
  elif salir_15:
    placeholder1_15.empty()
    placeholder2_15.empty()
    placeholder3_15.empty()
    placeholder4_15.empty()
    placeholder5_15.empty()
    placeholder6_15.empty()
    placeholder7_15.empty()
    placeholder8_15.empty()
    placeholder9_15.empty()
    placeholder10_15.empty()
    placeholder11_15.empty()
    placeholder12_15.empty()
    placeholder13_15.empty()
    placeholder14_15.empty()
    placeholder15_15.empty()
    st.session_state.Ingreso = False
    st.session_state.Validacion=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_15:

    cursor01=con.cursor()

    marca_15= datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_15= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_15 = nombre_15.loc[0,'nombre']
      
    horario_15= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_15 = horario_15.loc[0,'horario']

    supervisor_15= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_15 = supervisor_15.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_15}','{usuario}','{nombre_15}','{horario_15}','{puesto}','{supervisor_15}','Validación','{fecha_15}','{bloque_15}','{estado_15}','{tipo_15}','{predios_15}','{horas_15}')")
    con.commit()                                                                                                                                 
    st.success('Reporte enviado correctamente')
