if __name__ == '__main__':
    n = int(input())
    output = ['Not Weird', 'Weird']
    weird = int(0)
    # check
    if n % 2 == 1 or n in range(6, 21): weird = 1

    print(output[weird])