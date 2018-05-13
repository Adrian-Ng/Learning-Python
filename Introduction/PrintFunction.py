import math

if __name__ == '__main__':
    n = int(input())
    output = int(0)
    for i in range(1,n+1):
        output *= 10 * (10 ** math.floor(math.log(i, 10)))
        output += i
    print(output)