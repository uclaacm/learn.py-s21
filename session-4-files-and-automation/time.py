import time

t = time.time() #time since 12AM Jan 1st, 1970
readable_t = time.ctime(t) #readable time
print(t) 
print(readable_t)


    # print("started")
    # start_time = time.time()
    # time.sleep(5)
    # end_time = time.time()

    # print("start - end = " + str(end_time - start_time)) 


count = 60
while (count >= 0):
    print(count)
    time.sleep(1)
    count -= 1

