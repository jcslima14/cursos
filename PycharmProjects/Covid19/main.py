import pandas as pd
import numpy as np

# salva o total por município
df = pd.read_csv('/home/juliolima/git/curso_ciencia_de_dados/datasets/brazil_covid19_cities.csv', dtype={'code': str})
tm = df.query('date == "2020-11-30"')
tm['code'] = tm.code.str[:6]
tm[['state', 'code', 'name', 'cases', 'deaths']].to_csv('/home/juliolima/git/curso_ciencia_de_dados/datasets/brazil_covid_total_per_city.csv', index=False)

g = df[['date', 'cases', 'deaths']].groupby(by=['date'])
ult_data = None
ult_df = None

g.sum().to_csv('/home/juliolima/git/curso_ciencia_de_dados/datasets/brazil_covid_total_per_day.csv')

print('Fim do processamento')
