
#!/usr/bin/python
#!encoding: UTF-8
import modulo


tupla = (10, 20, 30, 40)

lista = [] #para indicar que es una variable de tipo lista
for i in tupla:
   valor_pi = modulo.calcular_pi (i)
   lista.append (valor_pi) #para anadir valores a la lista
print lista

pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT)
  
  
dif35 = []
for i in range (len (tupla)):
  dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
for i in range (len (tupla)):
   print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])
   

   
  
#EJERCICIOS PROPUESTOS
#1. HEMOS CREADO EL ARCHIVO MODULO QUE REALIZA LO QUE SE PIDE (QUE ES LA PRACTICA 6 ANTERIOR) Y DESDE EL ARCHIVO PRCT07 "LLAMAMOS" A MODULO Y UTILIZAMOS EL CODIGO.
#2. EL NUMERO MAXIMO DE ELEMENTOS DE LA T-UPLA DEPENDE DE LA MEMORIA DE CADA MÁQUINA. SE PRODUCEN ERRORES PARA LOS ELEMENTOS DEMASIADO GRNADES, EN CUYO CASO HABRÁ QUE ESCRIBIRLOS EN NOTACION CIENTIFICA. LA EXTENSIÓN PYC PODRÁ SER RECONOCIDA DEPENDIENDO DE LA UTILIZACION DEL "IF (__NAME__=="__MAIN__")" QUE EMPLEAMOS EN EL MÓDULO CREADO.
#3. HABRÍA QUE AÑADIR LA FUNCION "TIME" EN EL FOR PARA QUE MIDA CUANTO TARDA EN CADA ITERACION.       






#PARA SABER MAS:

print "pasando la salida a una matriz..."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #
matriz = []
for i in range (len (tupla)):
    matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len (tupla)):
  print
  print matriz[i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #