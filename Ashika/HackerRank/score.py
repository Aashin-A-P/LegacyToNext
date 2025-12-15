if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    scores=[scr[1] for scr in records]
    
    scores.sort()
    uni=[]
    for i in scores:
        if i not in uni:
            uni.append(i)
    
    mini=uni[1]
    output=[]
    for row in records:
            if row[1]==mini:
                output.append(row[0])
                
        
        
output.sort()
for i in output:
    print(i)
            
            