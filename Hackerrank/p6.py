if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for x in range(n):
        name, *marks_list = input().split()
        scores = list(map(float, marks_list))
        student_marks[name] = scores
    query_name = input('')

    print(query_name)
    print(student_marks.key)
    print(len(student_marks[name]))
    
    '''for x in range(len(marks_list)):
        if query_name in marks_list:    
            total = sum(marks_list)
            average = total / len(marks_list)
            print(f'{average:.2f}')
            '''