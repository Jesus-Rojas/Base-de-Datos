# Validar correo fue de internet.
import re
body_regex = re.compile('''
    ^(?!\.)                            # name may not begin with a dot
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
      |
      (?<!\.)\.                        # single dots only
    )+
    (?<!\.)$                            # name may not end with a dot
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
            # [sub]domain begins with alphanumeric
        (
          [-\w]*                         # alphanumeric, underscore, dot, hyphen
          [a-z0-9]                       # ending alphanumeric
        )?
      \.                               # ending dot
      )+
      [a-z]{2,}                        # TLD alpha-only
   )$
''', re.VERBOSE | re.IGNORECASE)

def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)

# cedula,nombre,apellido,correo,genero
def crearArchivo(a,b,c,d,e):
	f=open("archivo.txt","a")
	f.write(f"{a},{b},{c},{d},{e}\n")
	f.close()

def leerArchivo():
	f=open("archivo.txt","r")
	a=f.readlines()
	f.close()
	return a

def crearMatriz():
	x=leerArchivo()
	if (x!=[]):
		for e in range(len(x)):
			aux=x[e]
			x[e]=aux[:-1].split(sep=",")
	return x

def busquedaGenero(x,c):
	j=[]
	for i in x:
		if (i[4]==c):
			j.append(i)

	for h in j:
		print(h)

def busquedaCedula(x,c):
	j=str(c)
	for i in x:
		if (i[0]==j):
			return print(i)
def busquedaGeneral(x):
	for i in x:
		print(i)

def comprobar(x,a,b):
	l=str(a)
	for i in x:
		if (i[b]==l):
			return True

def datoNumerico(a):
	while(True):
		opcion=""
		try:
			opcion=int(input(f"Ingrese {a}: "))
		except:
			print()	

		if (type(opcion) == int):
			return opcion

def correo():
	while (True):
		d=input("Ingrese Correo: ")
		if(is_valid_email(d)):
			return d

def genero():
	while(True):
		e=input("Ingrese Genero (M/F): ")
		if(e=="M" or e=="F"):
			return e

crear=False
p=open("archivo.txt","a")
p.close()

while (True):
	print("\n# 1. Agregar Contacto\n# 2. Consultar Contacto Por Cedula\n# 3. Listar Por Genero\n# 4. Listarlos Todos\n")
	opcion=datoNumerico("Opcion")
	if (opcion==1):
		a=datoNumerico("Cedula")
		b=input("Ingrese Nombre: ")
		c=input("Ingrese Apellido: ")
		d=correo()
		e=genero()

		matriz=crearMatriz()
		if (matriz==[]):
			crear=True
		elif(comprobar(matriz,a,0)!=True):
			if(comprobar(matriz,d,4)!=True):
				crear=True
			else:
				print("Ingrese un correo distinto")
		else:
			print("Ingrese un numero de cedula distinto")
		if(crear):
			crearArchivo(a,b,c,d,e)
			print("Usuario se guardo en la base de datos")
		break
	elif (opcion==2):
		c=int(input("Ingrese Cedula: "))
		matriz=crearMatriz()
		busquedaCedula(matriz,c)
		break
	elif (opcion==3):
		e=input("Ingrese Genero (M / F): ")
		matriz=crearMatriz()
		busquedaGenero(matriz,e)
		break
	elif (opcion==4):
		matriz=crearMatriz()
		busquedaGeneral(matriz)
		break
