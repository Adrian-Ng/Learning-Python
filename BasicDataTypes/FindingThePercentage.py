if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    numElements = len(student_marks[query_name])
    result = float(sum(student_marks[query_name])/numElements)
    print("%.2f" % result)