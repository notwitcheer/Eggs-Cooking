# improving code with collections

import time
import beepy

CHOICE_COOKING = (
       ("classic eggs", 3*60),
       ("mollet eggs", 6*60),
       ("strong eggs", 9*60),
       ("raw steak", 4*60 + 30),
)


def time_sec_str(t):
    min = t//60
    sec = t-min*60
    min_unit = "minutes"
    sec_unit = "secondes"
    if min == 1:
           min_unit = "minute"
    if sec == 1:
           sec_unit = "seconde"
    r = ""
    if min > 0:
        r += f"{min} {min_unit}"
    if sec > 0:
        if len(r) > 0:
            r += " "
        r += f"{sec} {sec_unit}"
    return r


def ask_numerical_value(value_min, value_max):
    v = input(f"please give a value between {value_min} and {value_max} :")
    try:
        v_int = int(v)
    except:
        print("ERROR: please enter a numerical value.")
        return ask_numerical_value(value_min, value_max)
    if not value_min <= v_int <= value_max:
        print(f"ERROR: your value needs to be between {value_min} and {value_max}.")
        return ask_numerical_value(value_min, value_max)
    
    return v_int


# displaying menu
print("please chose cooking.")
index_choice = 1
for choice_cooking in CHOICE_COOKING:
       print(f"{index_choice} - {choice_cooking[0]} : {time_sec_str(choice_cooking[1])}")
       index_choice += 1


# user choice
choice = ask_numerical_value(1, len(CHOICE_COOKING))
choice_cooking = CHOICE_COOKING[choice - 1]
timing = choice_cooking[1]

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