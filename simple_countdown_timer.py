import time

def countdown(x):

    while x:
        x=x-1
        if x == 115:
            quit()
        time.sleep(1)
        print(x)

print("Enter seconds : ")

x = int(input())
countdown(x)

print("Time Over")
