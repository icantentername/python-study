'''
#0001题:做为 Apple Store App 独立开发者,
你要搞限时促销，为你的应用生成激活码（或者优惠券）,
使用 Python 如何生成 200 个激活码（或者优惠券）?
'''
#可自定义激活码长度   思路：生成一个激活码，再循环200次

import random
words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijilmnopqrstuvwxyz0123456789"

def getActCodes(Lenth): 
    i = 0
    while i <200:
        actCode = ''
        actCodes = set()
        for j in range(Lenth):
            actCode += random.choice(words)
        if actCode not in actCodes:
            actCodes.add(actCode)
            i += 1
        else:
            i = i
        print(actCodes)

getActCodes(16)
'''
#0001题:做为 Apple Store App 独立开发者,
你要搞限时促销，为你的应用生成激活码（或者优惠券）,
使用 Python 如何生成 200 个激活码（或者优惠券）?
'''
#可自定义激活码长度及个数   思路：生成一个激活码，再循环200次

import random
words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijilmnopqrstuvwxyz0123456789"
actCodes = set()

def getActCodes(lenth,count): 
    i = 0
    while i <count:
        actCode = ''
        for j in range(lenth):
            actCode += random.choice(words)
        if actCode not in actCodes:
            actCodes.add(actCode)
            i += 1
        else:
            i = i
    return(actCodes)

activationCodes = getActCodes(16,200)
print(activationCodes)
