from datetime import datetime

fmt = '%d/%m/%Y'

data = datetime.strptime('2024-01-19 19:35:25', '%Y-%m-%d %H:%M:%S')
print(data)
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%m'), data.month)
print(data.strftime('%d'), data.day)