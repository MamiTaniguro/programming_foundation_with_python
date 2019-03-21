import webbrowser
import time


total_breaks = 3 # number of breaks thoughouut the day
break_count = 0  # initialize count

print("This program started on" + time.ctime())

while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=cI4ryatVkKw")
    break_count = break_count + 1
