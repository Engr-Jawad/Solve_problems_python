import time 
wait_times=1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print("attempt",attempts + 1,"waiting for ",wait_times,"sec")
    time.sleep(wait_times)
    wait_times *=2
    attempts += 1
    print("retrying....")