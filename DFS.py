list1=[]
smallList=[]
def dfs(adj,src,goal):
    smallList.append(chr(src+ord('A')))
    if(src==goal):
        return
    lenofAdj=len(adj[src])
   
    for neigh in adj[src]:
        dfs(adj,neigh,goal)
        print(smallList)
        smallList.pop()
        
    

if __name__ =="__main__":
    
    adj=[[]for i in range(7)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(3)
    adj[1].append(4)
    adj[4].append(5)
    adj[2].append(6)

    goal="G"
    goal_node=ord(goal)-ord('A')
    dfs(adj,0,goal)
    print(list1)
