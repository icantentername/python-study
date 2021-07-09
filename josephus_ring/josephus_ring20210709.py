class Person():
    # 初始化中给对象属性赋值
    def __init__(self, name, id):
        self.name = name
        self.id = id

player_1 = Person('Adam', 202101)
player_2 = Person('Ben', 202102)
player_3 = Person('Cary', 202103)
player_4 = Person('David', 202104)
player_5 = Person('Eamonn', 202105)

pe_list = [player_1, player_2, player_3, player_4, player_5,]

def josephus_ring(pe_list, start_pos, step):

    new_pe_list = pe_list[start_pos:] + pe_list[:start_pos]             
    #start_pos为容器中的开始位置
    lenths = len(new_pe_list)
    result = [0 for i in range(lenths)]                                
    #result用于依次存放被淘汰的对象，初始化为全0
    rank = 0

    for i in range(lenths):
        rank = (rank + step) % len(new_pe_list)
        rank -= 1
        result[i] = new_pe_list[rank]
        del new_pe_list[rank]
        if rank == -1:
            rank = 0
    return result

result_list = josephus_ring(pe_list, 1, 2)
for i in range(len(result_list)):
    print('第%d次被淘汰的为'%(i+1) + result_list[i].name)
