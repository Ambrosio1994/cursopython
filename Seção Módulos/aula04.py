from datetime import datetime
from dateutil.relativedelta import relativedelta

data_inicio = datetime.strptime('2020-12-20', '%Y-%m-%d') # data do empréstimo
data_fim = data_inicio + relativedelta(years=5) # data fim do empréstimo
valor_parcela = 1000 / 60

datas_parcelas = []

while data_inicio < data_fim:
    datas_parcelas.append(data_inicio)
    data_inicio += relativedelta(months=1)


for data in datas_parcelas:
    print(f'Data da parcela: {data.strftime('%d/%m/%Y')} Valor: R${valor_parcela:.2f}')