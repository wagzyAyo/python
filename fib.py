def fibonacci(n):
    seq = []
    if n < 1:
        return
    elif n == 1:
        seq.append(0)
    else:
        seq.append(0)
        seq.append(1)
        while (n > len(seq)):
            seq.append(seq[-1] + seq[-2])
    print(seq)

fibonacci(10)