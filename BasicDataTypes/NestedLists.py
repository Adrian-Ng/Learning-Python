#Given the names and grades for each student in a Physics class of N students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Sample Input

#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#Sample Output

#Berry
#Harry

if __name__ == '__main__':
    N = int(input())
    #use list comprehension to create nested list
    studentsList = [[input(),float(input())] for _ in range(N)]
    #sort nested list
    studentsList = sorted(studentsList, key=lambda e: e[1], reverse=False)
    #get lowest Student Score
    lowestStudentScore = studentsList[0][1]
    #filter lowest Student
    studentsList = [i for i in studentsList if i[1] != lowestStudentScore]
    #get second lowest score
    secondLowestScore = studentsList[0][1]
    #get second lowest students names
    secondLowestNames = [i[0] for i in studentsList if i[1] == secondLowestScore]
    secondLowestNames.sort()
    print(*secondLowestNames, sep='\n')

