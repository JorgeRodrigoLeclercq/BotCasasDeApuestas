# from datos_tenis_betfair import datos_tenis_betfair
# from datos_tenis_bwin import datos_tenis_bwin
# from datos_tenis_betway import datos_tenis_betway
# from datos_tenis_williamhill import datos_tenis_williamhill
import pandas as pd

# paginas = {'betfair': datos_tenis_betfair,
#            'bwin': datos_tenis_bwin,
#            'betway': datos_tenis_betway,
#            'williamhill': datos_tenis_williamhill}

# for [pagina, partidos] in paginas.items():
#     try:
#         data = pd.DataFrame.from_dict(
#             partidos(), orient='index').reset_index()
#         data.columns = ['Partido', '1', '2']
#         data.to_csv(f'datos_tenis_{pagina}.csv', encoding='utf-8')
#     except Exception as error:
#         print(error)


partidos_betfair = pd.read_csv('datos_tenis_betfair.csv', index_col=0)
partidos_bwin = pd.read_csv('datos_tenis_bwin.csv', index_col=0)
partidos_betway = pd.read_csv('datos_tenis_betway.csv', index_col=0)
partidos_williamhill = pd.read_csv('datos_tenis_williamhill.csv', index_col=0)

nombres_bwin = list(partidos_bwin['Partido'])
nombres_betfair = list(partidos_betfair['Partido'])
nombres_betway = list(partidos_betway['Partido'])
nombres_williamhill = list(partidos_williamhill['Partido'])

lista_nombres = [nombres_betfair, nombres_betway,
                 nombres_bwin, nombres_williamhill]
dict_partidos = {"Betfair": [nombres_betfair, partidos_betfair],
                 "Betway":  [nombres_betway, partidos_betway], "Bwin": [nombres_bwin, partidos_bwin], "William Hill": [nombres_williamhill, partidos_williamhill]}

# Guardamos los partidos repetidos:
nombres_ambos = []
for lista_nombre in lista_nombres:
    for lista_nombrecito in lista_nombres:
        if lista_nombre != lista_nombrecito:
            for nombre in lista_nombre:
                if nombre in lista_nombrecito and (nombre not in nombres_ambos):
                    nombres_ambos.append(nombre)


# Guardamos cada partido en cada casa de apuesta con sus cuotas correspondientes:
partidos_bak = {}
for [pagina, [lista_nombres, lista_partidos]] in dict_partidos.items():
    for nombre in nombres_ambos:
        if nombre in lista_nombres:
            if nombre not in partidos_bak.keys():
                partidos_bak[nombre] = {pagina: list(
                    lista_partidos.loc[lista_partidos['Partido'] == nombre].to_dict('split')['data'][0][1:3])}
            else:
                partidos_bak[nombre] = {**partidos_bak[nombre], pagina: list(
                    lista_partidos.loc[lista_partidos['Partido'] == nombre].to_dict('split')['data'][0][1:3])}


for [key, value] in partidos_bak.items():
    print(key+': '+f'{value}')
    print("\n\n")

# Ahora vamos a comprobar si se cumple la condición matemática:
for [partido, cuotas_casas] in partidos_bak.items():
    cuotas_primero = []
    cuotas_segundo = []
    casas = []
    for [casa, cuotas] in cuotas_casas.items():
        try:
            if type(cuotas[0]) == str:
                cuotas_primero.append(float(cuotas[0].replace(",", ".")))
            else:
                cuotas_primero.append(cuotas[0])

            if type(cuotas[1]) == str:
                cuotas_segundo.append(float(cuotas[1].replace(",", ".")))
            else:
                cuotas_segundo.append(cuotas[1])
        except:
            pass
        casas.append(casa)
    for cuota in cuotas_primero:
        for cuotita in cuotas_segundo:
            try:
                if cuota > (1+1/(cuotita-1)) or cuotita > (1+1/(cuota-1)):
                    print("Bacanerías")
            except:
                pass
