if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for x in range(n):
        name, *marks_list = input().split()
        scores = list(map(float, marks_list))
        student_marks[name] = scores
    query_name = input('')

    # print(query_name)
    #print(student_marks.keys())
    #print(student_marks[name])

    total = 0
    for x in range(len(scores)):
        if query_name == student_marks.keys():
            total += scores[x]
            result = total / len(scores)
    
    print(result)