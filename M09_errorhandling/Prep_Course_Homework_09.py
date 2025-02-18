#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 8, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:

import sys
sys.path.append(r'C:\JIMPSOFT\HENRY\DATA SCIENCE\Python-Prep\M08_clasesyOOP')

# In[2]
from TareaM08 import FuncionesM08

# Func_Import = FuncionesM08([1,2,"Hola"]) # Al ingresar datos incorrectos, aroja un error, en este caso espera numeros y se ingreso el texto "Hola"

Func_Import = FuncionesM08([1,2])
Func_Import.Calc_Primo()




# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:

from TareaM08 import FuncionesM08


Func_Import = FuncionesM08([1,2,3,4,5,6,7,8,9,10])
Func_Import.Calc_Convertir("1","2")
Func_Import.Calc_Convertir("Celsius","Farenheit")


# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:




# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:




# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:




# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:




