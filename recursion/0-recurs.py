import time

def call_self(n):
    time.sleep(2)
    print(n)
    if n <= 0:
        return
    if n > 0:
        call_self(n - 1)


call_self(5)