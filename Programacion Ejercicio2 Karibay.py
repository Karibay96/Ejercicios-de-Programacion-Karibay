print("Definir un entero")
entero_1 = 20
type (entero_1 )
print("")
print("Definir numeros reales")
float_1,float_2,float_3=0.348,10.5,1.5e2
print(float_1)
print(float_2)
print(float_3)
type(float_1)
print("")
print("Definir numeros complejos")
complejo_1=2.1+7.8j
type(complejo_1)
print(complejo_1.imag)
print(complejo_1.real)
abs(complejo_1)
print("")
print("Definir un Boleano")
print("false")
False
False == False
0 == False
"" == False
None == False
[] == False
() == False
{} == False
['',''] == False
print("")
print("none")
int(False)
int(True)
print("")
print("Definir Numero cero en todos los tipos")
type(True)
str(True)
type(str(True))
type(False)
str(False)
type(str(False))
print("")
print("Datos tipo List")
factura=['pan','huevos',100,1234]
factura
print("")
factura[0]
factura[3]
print("")
len(factura)
len(factura)-1
factura[-1]
factura[-len(factura)]
factura[1]="carne"
factura
print("")
versiones_plone=[2.5,3.6,4,5]
print(versiones_plone)
versiones_plone.append(6)
print(versiones_plone)
print("")
versiones_plone=[2.1,2.5,3.6,4,5,5,6]
print(versiones_plone.count(6))
print(versiones_plone.count(5))
print("")
versiones_plone=[2.1,2.5,3.6,4,5,5,6]
print(versiones_plone.count(6))
print(versiones_plone.count(5))
print("")
versiones_plone=[2.1,2.5,3.6]
print(versiones_plone)
print("")
versiones_plone.extend([4])
print(versiones_plone)
print("")
versiones_plone=[2.1,2.5,3.6,4,5,6,4]
print(versiones_plone.index(4))
print("")
versiones_plone=[2.1,2.5,3.6,4,5,6]
versiones_plone.insert(2,3.7)
print(versiones_plone)
print("")
versiones_plone=[4,2.5,5,3.6,2.1,6]
print(versiones_plone)
versiones_plone.sort()
print(versiones_plone)
print("")
print("Definir Cadena de Caracteres")
print("")
'Hola_Mundo'
#hla_mnd='Hola_Mundo'
print("")
a,b="uno","dos"
a+b
print("")
c="tres"
c*3
print("")
tipo_calculo = "raiz_cuadrada_de_dos"
valor=2**0.5
print("el resultado de {} es {}".format(tipo_calculo, valor))