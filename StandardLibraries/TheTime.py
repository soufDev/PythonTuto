# -*-coding:Latin-1 -*

import time

start = time.time()
end = time.time()

print(start, end)
print(end-start)
print(end>start)

print("Local Time {0}".format(time.localtime(start).tm_mday))

t = time.localtime(start)
print(t)
print(time.strftime("%A %B %d %Y %H:%M:%S"))
ts_start = time.mktime(t)
#time.sleep(3)
print(ts_start)

