import time;
second=int(input("Enter the time in seconds: "))

def counter(seconds):
    while seconds>0:
        min=int(seconds/60);
        sec=int(seconds%60);
        timer=f'counter:{min}:{sec}'
        print(timer)
        time.sleep(1)
        seconds-=1
    
counter(second)