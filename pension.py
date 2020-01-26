from datetime import date
from datetime import timedelta
import math

def pension(fechaInicio, fechaNacimiento, insalubre, sexo):

	#Calculamos fecha actual
	fecha=date.today()
	#Se calcula las semanas que ha trabajado
	semanasTrabajo=math.floor((fecha-fechaInicio).days/7)

	#Primero calculamos la cantidad de dias tope con base en
	#sus condiciones de trabajo(insalubre o no) y el sexo

	
	#Calculamos la edad
	edad=math.floor((fecha-fechaNacimiento).days/365)

	edadRequerida=60

	#Es mujer
	if(sexo):
		edadRequerida=55

	if(insalubre):
		anosTrabajo=math.floor(semanasTrabajo/52)
		if(anosTrabajo>=20):
			edadRequerida-=5
		elif(anosTrabajo>=16):
			edadRequerida-=4
		elif(anosTrabajo>=12):
			edadRequerida-=3
		elif(anosTrabajo>=8):
			edadRequerida=-2
		elif(anosTrabajo>=4):
			edadRequerida-=1

	return (semanasTrabajo>=750 and edad>=edadRequerida)





	

if __name__ == '__main__':






	#Se solicita al usuario la fecha de inicio de trabajo
	anoInicio= int(input("\nIntroduzca el ano de inicio de trabajo en formato AAAA\n"))
	mesInicio= int(input("\nIntroduzca el mes de inicio de trabajo en formato MM\n"))
	diaInicio= int(input("\nIntroduzca el dia de inicio de trabajo en formato DD\n"))
	
	#Creamos el objeto date correspondiente a la fecha de inicio de trabajo
	
	fechaInicio=date(anoInicio,mesInicio,diaInicio)
	
	
	#Se solicita al usuario la fecha de nacimiento
	
	anoNacimiento= int(input("\nIntroduzca su ano de nacimiento\n"))
	mesNacimiento= int(input("\nIntroduzca su mes de nacimiento\n"))
	diaNacimiento= int(input("\nIntroduzca su dia de nacimiento\n"))
	
	#Creamos el objeto date correspondiente a la fecha de nacimiento
	fechaNacimiento=date(anoNacimiento,mesNacimiento,diaNacimiento)
	
	
	#Se solicita al usuario su sexo
	
	cualSexo=""
	
	while(cualSexo!="M" and cualSexo!="F"):
		cualSexo= input("\nIntroduzca M para masculino o F para femenino\n")
		
		if(cualSexo=="M"):
			sexo=False
		
		elif(cualSexo=="F"):
			sexo=True
		else:
			print("\nPor favor introduzca un valor valido\n")
	
	
	fueInsalubre=-1
	#Si trabajo en condicion insalubre
	while(fueInsalubre != 0 and fueInsalubre!= 1):
		fueInsalubre= int(input("\nIntroduzca 1 si trabajo en condiciones insalubre, 0 en caso contrario\n"))
		
		if(fueInsalubre==0):
			instalubre=False
		
		elif(fueInsalubre==1):
			insalubre=True
	
		else:
			print("\nPor favor introduzca un valor valido\n")
	
	
	#Finalmente, llamamos a la funcion pension
	
	
	
	pension(fechaInicio,fechaNacimiento,insalubre,sexo)	