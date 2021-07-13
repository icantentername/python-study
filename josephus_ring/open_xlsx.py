#open xlsx file

import openpyxl

class Person():
    # 初始化中给对象属性赋值
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Read_xlsx():
    def read(self, path):
        excel_file = openpyxl.load_workbook(path)
        sheet = excel_file.get_sheet_by_name('Sheet1')
        player = []
        sheet_list = list(sheet.rows)
        for row in sheet_list:
            cow_list = []
            for cell in row:
                cow_list.append(cell.value)
            player.append(cow_list)
        return player

read_excel = Read_xlsx()
pe_list = read_excel.read('E:/code/joseph_ring/read_class/test.xlsx')

def josephus_ring(pe_list, start_pos, step):
    assert start_pos >= 0
    assert step > 0

    new_pe_list = pe_list[start_pos:] + pe_list[:start_pos]             
    lenths = len(new_pe_list)
    result = [0 for i in range(lenths)]                                
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
    player = result_list[i]   
    player_list = Person(player[0],player[1])
    print('第%d次被淘汰的为'%(i+1) + player_list.name + '  id:' + str(player_list.id))