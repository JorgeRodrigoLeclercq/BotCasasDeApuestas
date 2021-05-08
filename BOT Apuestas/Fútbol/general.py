from datos_futbol_betfair import datos_futbol_betfair
from datos_futbol_bwin import datos_futbol_bwin
from datos_futbol_winamax import datos_futbol_winamax
import pandas as pd

paginas = {'betfair': datos_futbol_betfair, 'winamax': datos_futbol_winamax,
           'bwin': datos_futbol_bwin}

for [pagina, partidos] in paginas.items():
    try:
        data = pd.DataFrame.from_dict(
            partidos(), orient='index', columns=['1', 'X', '2'])
        data.to_csv(f'{pagina}_futbol.csv', encoding='utf-8')
    except:
        pass


partidos_betfair = pd.read_csv('betfair_futbol.csv', index_col=0)
partidos_bwin = pd.read_csv('bwin_futbol.csv', index_col=0)
partidos_winamax = pd.read_csv('winamax_futbol.csv', index_col=0)

print(partidos_betfair)
# print(partidos_bwin.iloc[1])
# print(partidos_winamax.iloc[0])
