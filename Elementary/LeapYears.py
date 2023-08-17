from datetime import datetime

now = datetime.now()
leap = now.year + 4

for i in range(0,20):
    print(leap, end=" ")
    leap += 4