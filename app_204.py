# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:13:50 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

#import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Geología Estructural")
page_names = ['Adair Guzmán López', 'Alejandra Aguilar Hernandez', 'Alejandro Salvador Ruiz Osorio', 'Andrei Francisco Sáenz Torres', 'Antonio Fernández Gutiérrez', 'Ariel Ramírez Espinoza', 'David Corral Arzola', 'David Ernesto Aguirre De la Torre', 'Ernesto Miranda Madrigal','Héctor Gilberto López Céspedes', 'Héctor Melo Amaro', 'Heraclio Israel Gutiérrez Moreno', 'Irasema Saray Olvera Barroso', 'Irving Rafael Arvizu Gutiérrez', 'Jorge Alberto Briseño Sotelo', 'José Alejandro Ávila Luna', 'José Carlos Ruiz Gutiérrez', 'Juan Carlos Fajardo Rivera', 'Juan Jose Urbano González', 'Juvenal Vega Noeggerath', 'Luís Enrique Salomón Mora', 'Luis Juárez Aguilar', 'Marco Antonio Escutia Aduna', 'María Isabel Zúñiga Barrios', 'Maribel Osorio Veloz', 'Miguel Hernández Padilla', 'Norma Araceli Olaez Ahedo', 'Oscar Manuel López Reyes', 'Ricardo Martínez Rodríguez', 'Rodrigo Portillo Pineda', 'Rolando Heberto Peterson Rodríguez', 'Rolando Ramos Landeros', 'Salvador Cruz López', 'Sergio Pacheco Sandoval', 'Ulises de Jesús Rodríguez Del Ángel', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

#df = pd.read_excel("NDR.xlsx")
#st.title("Datos")
#st.write(df)
#1 vertical menu

#selected = option_menu
#    menu_title = "Geología Estructural", #required
#    options = ["Ariel Ramírez Díaz", "Arnulfo Zarate Santiago", "Daniel Gómez Ochoa", "Gustavo Gutiérrez Rodríguez", "Jesica Aguirre Olguin", "Jesús Alejandro García Cantú", "José Luis Landa Mondragon", "María Elena Arenas Martínez", "Marybeth Garrido Hernández", "Mónica Rodríguez Otero", "Nestor Daniel Ortíz Najera", "Oscar Emmanuel Guadalupe Vences Estudillo", "Raúl Arturo Palacios Zamora", "Rosalía Molina Mandujano", "Uriel Román Manjarrez Juárez", "Uzziel Saldaña Hernández", "Verónica Iveth Ramírez Soria", "Yessica Guerrero Amador"], #required
#    #icons = ["house", "envelope", "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope",], #optional
#    #icons = ["house"],
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
    
#    ) 

#1                    
if page == 'Adair Guzmán López':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,2,1,1,2,2,2,1,2,1,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Adair Guzmán López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#2   
if page == 'Alejandra Aguilar Hernandez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[1,2,2,2,2,2,2,2,3,1,1,1,1,1,2,3,3,2,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandra Aguilar Hernandez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show() 
else: 
    st.subheader("")
    st.write("")

#3
if page == 'Alejandro Salvador Ruiz Osorio':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,4,2,2,2,4,3,2,1,2,1,1,3,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandro Salvador Ruiz Osorio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show() 
else:   
    st.subheader("")
    st.write("")

#4
if page == 'Andrei Francisco Sáenz Torres':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,2,3,2,1,1,2,1,1,1,2,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Andrei Francisco Sáenz Torres', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#5
if page == 'Antonio Fernández Gutiérrez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,3,2,3,2,2,3,2,3,1,1,1,1,2,1,1,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Antonio Fernández Gutiérrez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#6
if page == 'Ariel Ramírez Espinoza':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,5,4,4,5,4,4,5,4,3,3,4,2,5,2,2,3,2,4])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ariel Ramírez Espinoza', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:      
    st.subheader("")
    st.write("")  

#7      
if page == 'David Corral Arzola':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,1,3,2,2,2,3,2,2,2,3,2,1,2,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='David Corral Arzola', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
   st.subheader("")
   st.write("")

#8
if page == 'David Ernesto Aguirre De la Torre':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,3,3,2,2,1,2,3,2,2,1,2,1,1,3,2,3,1,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='David Ernesto Aguirre De la Torre', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
    st.subheader("")
    st.write("")

#9
if page == 'Ernesto Miranda Madrigal':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,2,5,5,3,2,3,3,2,2,5,2,2,2,2,1,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ernesto Miranda Madrigal', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:
    st.subheader("")
    st.write("")

#10    
if page == 'Héctor Gilberto López Céspedes':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,3,3,4,2,3,3,3,4,2,2,2,2,2,3,2,1,1,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Héctor Gilberto López Céspedes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
    st.subheader("")
    st.write("")

#11
if page == 'Héctor Melo Amaro':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales", "Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,5,3,5,3,3,4,4,4,4,3,4,2,3,3,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Héctor Melo Amaro', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show()  
else:
    st.subheader("")
    st.write("")

#12
if page == 'Heraclio Israel Gutiérrez Moreno':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,2,5,3,2,3,3,5,2,3,3,2,2,2,2,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Heraclio Israel Gutiérrez Moreno', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
     st.subheader("")
     st.write("")

#13    
if page == 'Irasema Saray Olvera Barroso':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,4,2,5,3,2,3,3,3,2,1,2,2,2,2,2,1,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Irasema Saray Olvera Barroso', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")


#14
if page == 'Irving Rafael Arvizu Gutiérrez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,3,3,2,2,2,3,4,2,2,3,1,2,3,2,1,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Irving Rafael Arvizu Gutiérrez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")

#15
if page == 'Jorge Alberto Briseño Sotelo':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,2,2,2,1,2,2,2,1,3,2,1,2,1,2,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jorge Alberto Briseño Sotelo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")

#16
if page == 'José Alejandro Ávila Luna':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,1,3,2,2,3,3,2,2,3,3,3,2,2,2,2,1,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Alejandro Ávila Luna', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#17
if page == 'José Carlos Ruiz Gutiérrez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,2,3,2,2,2,2,2,2,2,3,4,2,3,2,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Carlos Ruiz Gutiérrez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()         
else:
     st.subheader("")
     st.write("")

#18    
if page == 'Juan Carlos Fajardo Rivera':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,3,3,3,2,1,4,2,3,4,2,2,2,4,2,1,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Carlos Fajardo Rivera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show()     
else:
    st.subheader("")
    st.write("")
    
#19                    
if page == 'Juan Jose Urbano González':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,4,3,3,2,2,3,3,2,2,2,3,2,2,2,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Jose Urbano González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#20   
if page == 'Juvenal Vega Noeggerath':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,2,1,2,2,2,3,2,1,1,1,1,1,1,2,2,2,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juvenal Vega Noeggerath', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show() 
else: 
    st.subheader("")
    st.write("")

#21
if page == 'Luís Enrique Salomón Mora':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,5,2,5,4,3,5,4,5,2,3,4,2,2,3,3,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luís Enrique Salomón Mora', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show() 
else:   
    st.subheader("")
    st.write("")

#22
if page == 'Luis Juárez Aguilar':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,3,2,3,3,2,3,3,2,2,2,2,2,2,3,2,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luis Juárez Aguilar', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#23
if page == 'Marco Antonio Escutia Aduna':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,3,2,2,1,1,1,1,1,1,2,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marco Antonio Escutia Aduna', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#24
if page == 'María Isabel Zúñiga Barrios':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,2,3,3,3,3,3,3,2,2,2,2,2,2,3,2,2,2,4])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Isabel Zúñiga Barrios', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:      
    st.subheader("")
    st.write("")  

#25     
if page == 'Maribel Osorio Veloz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,4,2,4,3,2,3,3,2,2,2,3,2,2,2,2,4,4,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maribel Osorio Veloz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
   st.subheader("")
   st.write("")

#26
if page == 'Miguel Hernández Padilla':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,4,3,3,2,2,3,3,4,2,2,3,2,5,3,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Miguel Hernández Padilla', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
    st.subheader("")
    st.write("")

#27
if page == 'Norma Araceli Olaez Ahedo':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,3,2,3,2,2,1,2,2,1,2,1,1,4,2,2,2,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Norma Araceli Olaez Ahedo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:
    st.subheader("")
    st.write("")

#28    
if page == 'Oscar Manuel López Reyes':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,3,2,3,2,2,2,3,2,1,1,1,1,1,2,2,2,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Manuel López Reyes', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
    st.subheader("")
    st.write("")

#29
if page == 'Ricardo Martínez Rodríguez':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,1,2,1,1,1,3,1,1,1,2,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ricardo Martínez Rodríguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show()  
else:
    st.subheader("")
    st.write("")

#30
if page == 'Rodrigo Portillo Pineda':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,2,5,2,2,2,3,5,2,1,3,1,2,2,1,2,3,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rodrigo Portillo Pineda', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
     st.subheader("")
     st.write("")

#31    
if page == 'Rolando Heberto Peterson Rodríguez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,3,5,3,2,2,4,3,2,2,4,2,3,3,2,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rolando Heberto Peterson Rodríguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")


#32
if page == 'Rolando Ramos Landeros':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,3,2,2,3,3,2,1,3,2,1,2,2,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rolando Ramos Landeros', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")

#33
if page == 'Salvador Cruz López':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,1,3,2,2,2,3,3,2,1,2,3,2,2,2,1,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Salvador Cruz López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")

#34
if page == 'Sergio Pacheco Sandoval':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Sergio Pacheco Sandoval', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

#35
if page == 'Ulises de Jesús Rodríguez Del Ángel':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,4,4,3,4,4,3,4,3,4,3,2,3,3,3,3,3,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ulises de Jesús Rodríguez Del Ángel', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()         
else:
     st.subheader("")
     st.write("")
    

######   35    #################################################################################################################################################    


if page == 'Unión de los gráficos':
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,1,3,2,2,1,2,2,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #1
     fig.add_scatter(name = 'Adair Guzmán López', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,2,1,1,2,2,2,1,2,1,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #2
     fig.add_scatter(name = 'Alejandra Aguilar Hernandez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[1,2,2,2,2,2,2,2,3,1,1,1,1,1,2,3,3,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #3
     fig.add_scatter(name = 'Alejandro Salvador Ruiz Osorio', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,4,2,2,2,4,3,2,1,2,1,1,3,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #4
     fig.add_scatter(name = 'Andrei Francisco Sáenz Torres', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,2,3,2,1,1,2,1,1,1,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #5
     fig.add_scatter(name = 'Antonio Fernández Gutiérrez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,3,2,3,2,2,3,2,3,1,1,1,1,2,1,1,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #6
     fig.add_scatter(name = 'Ariel Ramírez Espinoza', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,5,4,4,5,4,4,5,4,3,3,4,2,5,2,2,3,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #7
     fig.add_scatter(name = 'David Corral Arzola', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,1,3,2,2,2,3,2,2,2,3,2,1,2,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #8
     fig.add_scatter(name = 'David Ernesto Aguirre De la Torre', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,3,3,2,2,1,2,3,2,2,1,2,1,1,3,2,3,1,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #9
     fig.add_scatter(name = 'Ernesto Miranda Madrigal', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,2,5,5,3,2,3,3,2,2,5,2,2,2,2,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #10
     fig.add_scatter(name = 'Héctor Gilberto López Céspedes', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,3,3,4,2,3,3,3,4,2,2,2,2,2,3,2,1,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #11
     fig.add_scatter(name = 'Héctor Melo Amaro', x=["Mapeo-correlaciones estratigráficas y estructurales", "Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,5,3,5,3,3,4,4,4,4,3,4,2,3,3,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #12
    
     fig.add_scatter(name = 'Heraclio Israel Gutiérrez Moreno', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,2,5,3,2,3,3,5,2,3,3,2,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #13    
     fig.add_scatter(name = 'Irasema Saray Olvera Barroso', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,4,2,5,3,2,3,3,3,2,1,2,2,2,2,2,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
           
     #14
     fig.add_scatter(name = 'Irving Rafael Arvizu Gutiérrez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,3,3,2,2,2,3,4,2,2,3,1,2,3,2,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
    
     #15
     fig.add_scatter(name = 'Jorge Alberto Briseño Sotelo', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,2,2,2,1,2,2,2,1,3,2,1,2,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #16
     fig.add_scatter(name = 'José Alejandro Ávila Luna', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,1,3,2,2,3,3,2,2,3,3,3,2,2,2,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])

     #17
     fig.add_scatter(name = 'José Carlos Ruiz Gutiérrez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,4,2,3,2,2,2,2,2,2,2,3,4,2,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
           
     #18    
     fig.add_scatter(name = 'Juan Carlos Fajardo Rivera', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,3,3,3,2,1,4,2,3,4,2,2,2,4,2,1,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #19                    
     fig.add_scatter(name = 'Juan Jose Urbano González', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,4,3,3,2,2,3,3,2,2,2,3,2,2,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #20   
     fig.add_scatter(name = 'Juvenal Vega Noeggerath', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,2,1,2,2,2,3,2,1,1,1,1,1,1,2,2,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #21
     fig.add_scatter(name = 'Luís Enrique Salomón Mora', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,2,5,2,5,4,3,5,4,5,2,3,4,2,2,3,3,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #22
     fig.add_scatter(name = 'Luis Juárez Aguilar', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,3,2,3,3,2,3,3,2,2,2,2,2,2,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     
     #23
     fig.add_scatter(name = 'Marco Antonio Escutia Aduna', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,3,2,2,1,1,1,1,1,1,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #24
     fig.add_scatter(name = 'María Isabel Zúñiga Barrios', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,2,3,3,3,3,3,3,2,2,2,2,2,2,3,2,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #25     
     fig.add_scatter(name = 'Maribel Osorio Veloz', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,4,2,4,3,2,3,3,2,2,2,3,2,2,2,2,4,4,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
        
     #26
     fig.add_scatter(name = 'Miguel Hernández Padilla', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,4,3,3,2,2,3,3,4,2,2,3,2,5,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #27
     fig.add_scatter(name = 'Norma Araceli Olaez Ahedo', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,3,2,3,2,2,1,2,2,1,2,1,1,4,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
           
     #28    
     fig.add_scatter(name = 'Oscar Manuel López Reyes', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,2,3,2,3,2,2,2,3,2,1,1,1,1,1,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
       
     #29
     fig.add_scatter(name = 'Ricardo Martínez Rodríguez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,1,2,1,1,1,3,1,1,1,2,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #30
     fig.add_scatter(name = 'Rodrigo Portillo Pineda', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,2,5,2,2,2,3,5,2,1,3,1,2,2,1,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #31    
     fig.add_scatter(name = 'Rolando Heberto Peterson Rodríguez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,5,3,5,3,2,2,4,3,2,2,4,2,3,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #32
     fig.add_scatter(name = 'Rolando Ramos Landeros', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,3,2,2,3,3,2,1,3,2,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
           
     #33
     fig.add_scatter(name = 'Salvador Cruz López', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,1,3,2,2,2,3,3,2,1,2,3,2,2,2,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
           
     #34
     fig.add_scatter(name = 'Sergio Pacheco Sandoval', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
          
     #35
     fig.add_scatter(name = 'Ulises de Jesús Rodríguez Del Ángel', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,4,4,3,4,4,3,4,3,4,3,2,3,3,3,3,3,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
      
     st.plotly_chart(fig)
      
else:
     st.subheader("")
    
