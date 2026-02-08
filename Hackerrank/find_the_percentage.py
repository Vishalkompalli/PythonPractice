if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores #Dictionary Updation done

    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average))
    

#inputs
#Testcase1

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika