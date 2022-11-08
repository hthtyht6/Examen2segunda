'''
# Tema:  Examen 2 segunda Oportunidad
# Fecha: 07/11/2022
# Autor: Juan Antonio Jaramillo Moreno
'''
import json

def codigospostales(municipio):
    codigosP = {}
    archivo = open('CPdescarga.txt', 'r')

    cadena = archivo.read()
    cadena = cadena.replace('||','| |')
    listaCP = cadena.split("\n")

    archivo.close()

    i = 1

    for mnp in listaCP:
        codigos = mnp.split("|")
        cp = {}
        if len(codigos)>1 :
            if codigos[3] == municipio:
                cp["d_codigo"] = codigos[0]
                cp["d_tipo_asenta"] = codigos[2]
                cp["d_zona"] = codigos[13]
                codigosP[f"{i}"] = cp
                i=i+1
    retornoList = json.dumps(codigosP)
    return (retornoList)

print(codigospostales('Jiquilpan'))

def codigospostales2(estado):
    codigosP = {}
    archivo = open('CPdescarga.txt', 'r')

    cadena = archivo.read()
    cadena = cadena.replace('||','| |')
    listaCP = cadena.split("\n")
    archivo.close()
    retornoList = []

    for mnp in listaCP:
        codigos = mnp.split("|")
        # print(codigos)
        cp = {}
        if len(codigos)>1 :
            if codigos[4] == estado:
                cp["d_codigo"] = codigos[0]
                cp["D_mnpio"] = codigos[3]
                retornoList.append(cp)
    codigosP[estado] = retornoList
    retornoList = json.dumps(codigosP)
    return(retornoList)

print(codigospostales2('Michoacán de Ocampo'))