import textwrap

def wrap(string, max_width):
    res=' '
    i=0
    while(i<len(string)):
        for j in range(max_width):
            if(i<len(string)):
                res+=string[i]
                i+=1
            
        res+='\n'
    
    
    return res.strip()

        
     

if __name__ == '__main__':