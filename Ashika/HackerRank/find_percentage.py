if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
   
 
    ans=student_marks.get(query_name)
    sums=0
    for i in ans:
        sums+=i
   
    final=round(sums/len(ans),2)
    print(f'{final:.2f}')