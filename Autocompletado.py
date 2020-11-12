texto = "pan panadero sepan godzilla p pa panpanpan par pam pantano pingüino"
palabras = texto.split()        # Se convierte en lista separado por espacios

prefijo = input("Ingrese el prefijo: ")                 # Se define el prefijo

# Filtra las palabras por prefijo
palabras_prefijo = filter(lambda x: x.startswith(prefijo), palabras)

# Imprime las palabras que tienen ese prefijo
for p in palabras_prefijo:                                  
    print(p)
