from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('20/03/1994 09:30:30', fmt)
data_fim = datetime.strptime('20/03/2024 19:30:30', fmt)

delta = data_fim - data_inicio
print(delta.days)

time_delta = timedelta(days=30, hours=12)
print(data_fim + time_delta)


from dateutil.relativedelta import relativedelta

print(data_fim + relativedelta(seconds=60))