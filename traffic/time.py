import time
from datetime import datetime

s=datetime.now()
time.sleep(10)

e=datetime.now()

print((s - e).total_seconds()*10**3)
