import time

def call_self(n):
    time.sleep(2)
    print(n)
    if type(n) != int:
        print("{} must be an integer".format(n))
        return
        
    elif n <= 0:
        print("{} must be greater than 0 ".format(n))
        return
            
    if n >= 1:
        call_self(n - 1)


call_self(3)