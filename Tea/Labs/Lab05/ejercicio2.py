cadena = "X-DSPAMConfidence:0.8475"

post1 = cadena.find(":")
print("Inicia en el Indice en: "+str(post1))

pos2 = cadena.find("5")
print("Terminaen:"+ str(pos2))

final = len(cadena )
substring = cadena [post1+1:final]
numerico = float(substring)

print(numerico)
print(type(numerico))
