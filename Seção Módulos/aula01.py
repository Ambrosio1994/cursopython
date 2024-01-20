from pytz import timezone
from datetime import datetime


data = datetime.now(timezone('Asia/Tokyo'))
print(data)
