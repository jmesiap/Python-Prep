class FuncionesM09:
    
    def __init__(self, Lista_Valores):
        self.Lista = Lista_Valores 


    def Calc_Primo(self):
        for i in self.Lista:
            print(self.F_primo(i))
            
    def F_primo(self, num):
        if num == 1: return num, "No es número primo"    

        for i in range(2,num):
            if  num % i == 0: 
                return num, "No es número primo"
                break           
        return  num, "Es número primo"    
    
   
    def F_Repite(self):
        self.Lista.sort()
        contador = 1
        mayor_Veces=0
        mayor_Num=0
        i = 1
        Lista_Nueva=[]
        while i < (len(self.Lista)):
           
            if self.Lista[i-1] == self.Lista[i]:
               contador = contador+1
               if i == len(self.Lista)-1:
                  Lista_Nueva.append([self.Lista[i-1], contador])  
                    
                  if contador > mayor_Veces:
                    mayor_Veces = contador 
                    mayor_Num = self.Lista[i-1] 

            else:
                Lista_Nueva.append((self.Lista[i-1], contador))    
                
                if contador > mayor_Veces:
                    mayor_Veces = contador 
                    mayor_Num = self.Lista[i-1]
                contador=1
            i += 1
        
        return Lista_Nueva, mayor_Veces, mayor_Num
    
    def Calc_Convertir(self, origen, destino ):

        esperados =  ["Celsius", "Farenheit", "Kelvin"]
        #Valor_Result = []
        print("Hola Pepe")
        print(esperados)

        if str(origen) not in esperados:
           print(" 1  Ingrese los parametros esperados,", esperados) 
           return 
        if str(destino) not in esperados:
           print(" 2  Ingrese los parametros esperados,", esperados) 
           return 
        
        for i in self.Lista:    
            Valor_Result = self.F_convertir(i, origen, destino)    
            print(i,"Celcius convertido a Farenheit es igual a:",  round(Valor_Result,2))
        
        
        #if origen or destino == "Celsius" or origen or destino == "Kelvin" or destino == "Farenheit":
          
        #else:   
            #return "Ingrese un valor correcto: Celsius, Kelvin ó Farenheit"       

    def F_convertir(self, valor, origen, destino):
            resultado=0
            if origen=="Celsius":
                if destino == "Farenheit":
                    resultado = (valor*1.8) + 32    
                elif destino == "Kelvin":
                    resultado = valor + 273.15    
                elif destino == "Celsius":
                    resultado = valor        
                else: print("1 --- Inghrese valor correcto Farenheit, Kelvin ó Celsius")
            elif origen=="Farenheit":
                if destino == "Celsius":
                    resultado = (valor-32) + 1.8    
                elif destino == "Kelvin":
                    resultado = ((5*valor) + 2298.35)/9
                elif destino == "Farenheit":
                    resultado = valor        
                else: print("2 -- Inghrese valor correcto Farenheit, Kelvin ó Celsius")
            elif origen=="Kelvin":
                if destino == "Celsius":
                    resultado = valor-273.15
                if destino == "Farenheit":
                    resultado = (9*valor-2458.35)/5 + 32
                if destino == "Kelvin":
                    resultado = valor        
                else: print("3 -- Inghrese valor correcto Farenheit, Kelvin ó Celsius")
            else: print("4 -- Inghrese valor correcto Farenheit, Kelvin ó Celsius")    
   
            return resultado
    
    def Calc_facto(self):
        for i in self.Lista:
            print("Factorial de", i, ": ", self.F_facto(i))

    def F_facto(self, num):
        
        if num == 1:
            return 1
        if type(num) != int:
            return 'Debe ingresar un número entero'
        if num < 0:
            return 'El número debe ser positivo'
            
        num = num  * self.F_facto(num - 1)
        return num     
