def fun():
    n = int(input("enter the limit:"))
    prime = []
    for i in range(2, n + 1):
        if n % i == 0:
            continue
        else:
            prime.append(i)
    print(prime)

fun()



