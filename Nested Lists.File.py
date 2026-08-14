if __name__ == '__main__':
    students = []  

   
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

   
    unique_scores = sorted(list(set([score for name, score in students])))

    
    second_lowest_score = unique_scores[1]

    
    target_students = [
        name for name, score in students if score == second_lowest_score
    ]

    
    target_students.sort()
    for name in target_students:
        print(name)