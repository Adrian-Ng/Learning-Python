
#https://www.hackerrank.com/challenges/python-lists/problem

#Sample input

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print#

#Sample Output

#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        instring = input().split()
        cmd = str(instring[0])
        if cmd == 'print':
            print(l)
        else:
            cmd = cmd + '(' + ', '.join(map(str,instring[1:])) + ')'
            eval('l.' + cmd)
