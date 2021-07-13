import csv
import openpyxl

class Person():

    def __init__(self, name, id):
        self.name = name
        self.id = id

class Read_txt():
    def read(self, path):
        txt_data = []
        with open(path, 'r') as txt_file:
            while True:
                line = txt_file.readline()
                if not line:
                    break
                line = line.strip('\n')
                txt_data.append(line)
        txt_file.close()
        return txt_data

class Read_csv():
    def read(self, path):  
        with open(path, 'r') as csv_file:
            csv_read_lines = csv.reader(csv_file)
            csv_data = []
            for line in csv_read_lines:
                csv_data.append(' '.join(line))
        return csv_data

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

#read_txt = Read_txt()
#pe_list = read_txt.read('E:/code/joseph_ring/read_class/test.txt')
read_csv = Read_csv()
pe_list = read_csv.read('E:/code/joseph_ring/read_class/test.csv')
#read_excel = Read_xlsx()
#pe_list = read_excel.read('E:/code/joseph_ring/read_class/test.xlsx')

def josephus_ring(pe_list, start_pos, step):
    assert start_pos >= 0
    assert step > 0

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
    player = result_list[i].split('\t')     #player = result_list[i].split('\t')
    player_list = Person(player[0],player[1])
    print('第%d次被淘汰的为'%(i+1) + player_list.name + '  id:' + player_list.id)