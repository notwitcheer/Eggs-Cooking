# learning how to make a egg cookooor.

import time
import beepy

"""
# MY SUBMISSION:
d = 100
min = d//60
sec = d-min*60

def selection():
    print("please chose between (a) classic eggs - (b) mollets eggs - (c) strong eggs.")
    choice_str = input("your choice: ")
    try:
        choice_int = int(choice_str)
    except ValueError:
        print("ERROR, please chose between 1, 2 or 3.")
        return selection()
    nb_sec = 0
    if choice_int == 1:
        nb_sec = 3*60
    elif choice_int == 2:
        nb_sec = 6*60
    elif choice_int == 3:
        nb_sec = 9*60
    else:
        return selection()
    time = nb_sec
    print(f"time is {time} secondes.")
    return time

selection() 
for i in range(0, -1):
    time.sleep(1)
    print(".", end="", flush=True)

time_left = i
min_left = time_left // 60
sec_left = time_left % 60



# print("")
# print("end of cooking.")
# print("DRIIIIIIIING.")



# print(f"{min:02d}")
# print(f"{sec:02d}")
"""

# CORRECTION:

print("please chose between (a) classic eggs - (b) mollets eggs - (c) strong eggs.")
while True:
    choice = input("your choice: ")
    if choice == "1" or choice == "2" or choice == "3":
           break
    print("ERROR: please chose 1 or 2 or 3\n")

timing = 0
if choice == "1":
        timing = 3*60
elif choice == "2":
        timing = 6*60
elif choice == "3":
        timing = 9*60

while True:
        for i in range(10):
            time.sleep(1)
            timing -= 1
            if timing <= 0:
                   break
            print(".", end="", flush=True)
          
        if timing <= 0:
                   break
            
        min = timing//60
        sec = timing-min*60
        print(f"\ntime left: {min:02d}:{sec:02d}", end="", flush=True)
print("")
print("COOKED")