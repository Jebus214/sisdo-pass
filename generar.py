import unicodedata

f = open('nombres.txt', 'r',encoding="utf8")
x = f.readlines()

f = open('puestos.txt', 'r',encoding="utf8")
p = f.readlines()

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


def generar_usu_sisdo(l):
	for name  in l:
		n=name.lower()
		n=n.split()
		if (len(n)>3):
			res=elimina_tildes(n[0])+'.'+elimina_tildes(n[1])+'.'+elimina_tildes(n[2])
		else:
			res=elimina_tildes(n[0])+'.'+elimina_tildes(n[1])
		print(res+","+res+'.2017')

def generar_query_sisdo(l,puestos):
	i=0
	for name  in l:
		n=name.lower()
		n=n.split()
		if (len(n)>3):
			res=elimina_tildes(n[0])+'.'+elimina_tildes(n[1])+'.'+elimina_tildes(n[2])
		else:
			res=elimina_tildes(n[0])+'.'+elimina_tildes(n[1])
		username=res
		password=res+'.2017'
		print("INSERT INTO `sisdo_af3f4fsa`.`members` (`memberID`, `username`, `password`, `email`, `active`, `resetToken`, `resetComplete`, `token`, `nombre`, `puesto`, `nivel`, `porcentaje`) VALUES (NULL, '"+username+"', '"+password+"', '', '', NULL, 'No', '', '', '"+puestos[i]+"', '', '');")
		i=i+1

generar_usu_sisdo(x)
#generar_query_sisdo(x,p)
