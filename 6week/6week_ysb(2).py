import sys
#sys.stdin=open("input.txt", "r")

def DFS(cnt,sum):
    global price
    global mn
    if sum==price:
        if cnt<mn:
            mn=cnt
    elif sum>price:
        return
    elif cnt>mn:
        return
    else:
        for i in coin:
            DFS(cnt+1,sum+i)
            
  
if __name__=="__main__": 
    n = int(input())
    coin = list(map(int,input().split()))
    price = int(input())
    mn = 2147000000
    coin.sort(reverse=True)
    DFS(0,0)
    print(mn)
    
    
    

   


 






        


