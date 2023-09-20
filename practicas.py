#import  sys
#import os
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen("https://es.wikipedia.org/wiki/Python")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
links = soup.find_all("a")
print(links)

#print(f"Buenos dias {sys.argv[1]}")
#print(sys.argv)
""" def dividir (num, div):
    return num/div

def mas_10(num):
  return num + 10 """

""" try:
    res = dividir(20, 4)
    print(round(res,1))
except ZeroDivisionError:
    print("Trataste de dividir entre cero :( ") """
""" try:
    resultado = mas_10("10")
    print(resultado)
except TypeError:
   print("El argumento debe ser un numero  :(")  """

""" def suma(num1, num2):
    return num1+num2

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("\n")
        print("ERROR: Parametros incorrectos \n")
        print("Modo de uso:")
        print(f"    {sys.argv[0]} Numero1 Numero2 \n")
        print("Ejemplo:")
        print(f"    {sys.argv[0]} 4 8 \n")
        sys.exit(1)
    else:
        try:
            n1=int(sys.argv[1])
        except ValueError:
            
            print("\n  ERROR: El primer parametro no es un número")        
            sys.exit(1)
        
        try:
            n2=int(sys.argv[2])
        except ValueError:
            print("\n  ERROR: El segundo parametro no es un número")        
            sys.exit(1)      
        
        print(f"\n  la suma de: {n1} + {n2} = {suma(n1,n2)}\n ")
        sys.exit(0) """
       
""" lista = ["Pepe", "Janet", "Mateo", "Delicia"]
archivo=open("Mi_Texto.txt", "r")
#contenido = archivo.read()
for linea in archivo:
    if "Pepe" in linea:
        print(linea, end="") """


