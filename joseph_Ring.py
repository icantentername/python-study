def josephus_ring(n,step):

    link = list(range(1,n+1))       #给成员编号，从1开始
    result = [0 for i in range(n)]  #初始化淘汰结果列表
    rank = 0                        #初始化成员编号的索引值

    for i in range(n):
        rank = (rank + step) % len(link)
        rank -= 1
        result[i] = link[rank]
        del link[rank]
        if rank == -1:
            rank = 0
    
    return result

print(josephus_ring(5,3))
