
#You are given  numbers. Store them in a list and find the second largest number.

#Sample Input

#5
#2 3 6 6 5

#Sample Output

#5


if __name__ == '__main__':
    n = int(input())
    intMap = map(int, input().split())
    intList = list(intMap)
    maxint = max(intList)
    intList = [x for x in intList if x !=maxint]
    print(max(intList))
