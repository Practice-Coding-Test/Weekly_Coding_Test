import sys
#sys.stdin=open("input.txt", "r")

def DFS(v):
    global cnt
    if v>n:
        cnt+=1
        for i in ch[1:]:
            print(i,end=' ')
        print()
    else:
        for i in range(1,m+1):
            ch[v]=i
            DFS(v+1)


    
if __name__=="__main__": 
    m,n = map(int,input().split())
    cnt = 0
    ch = [0]*(n+1)
    DFS(1)
    print(cnt)

    
    

   


 






        


