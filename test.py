import time

start_time = time.time()
time.sleep(2)
end_time = time.time()
res_time = end_time - start_time
print(round(res_time, 3))