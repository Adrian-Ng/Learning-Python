#https://www.hackerrank.com/challenges/python-tuples/problem
#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

#Sample Input

#2
#1 2

#Sample Output

#3713081631934410656


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))