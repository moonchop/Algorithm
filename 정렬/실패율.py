def solution(N, stages):

    answer = []
    member=[0]*(N+1)
    stages.sort()
    count=len(stages)
    fail_arr=[]
    for i in stages:
        if i <=N:
            member[i]+=1

    
    for i in range(1,N+1):
        
        if count==0:
            fail_arr.append((0,i))
            continue
        fail_arr.append((member[i]/count,i))
        count-=member[i]
        
    fail_arr.sort(key=lambda x:x[0],reverse=True)
    for i in fail_arr:
        answer.append(i[1])

    return answer