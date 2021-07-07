def joseph_Ring(num_people, skip_num):
    if num_people == 1:
        return(0)   
    else:
        return((joseph_Ring(num_people - 1, skip_num) + skip_num) % num_people)

num_people = int(input('请输入总人数： '))
skip_num = int(input('请输入要跳过的数字： '))
result = joseph_Ring(num_people, skip_num)

print('最后留下的人编号是: ', result)