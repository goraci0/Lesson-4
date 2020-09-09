import random

def func (spis,N):
    rand_list = []
    for i in range(0,N):
        k = random.randint(0, len(spis)-1)
        rand_list.append(spis[k])
    return rand_list

def func_max_slov(name_list,rn_list):
    dict_slov = {}
    for nm in name_list:
        dict_slov[nm] = rn_list.count(nm)
    list_txt = list(dict_slov.items())
    list_txt.sort(key=lambda i: i[1])
    list_txt.reverse()
    return list_txt[:1]

def func_min_symb(rn_list):
    dict_symb = {}
    for i in range(len(rn_list)):
        dict_symb[rn_list[i][0]] = 0
    for i in range(len(rn_list)):
        dict_symb[rn_list[i][0]] += 1

    list_symb = list(dict_symb.items())
    list_symb.sort(key=lambda i: i[1])

    return list_symb[:1]

list_name = ['Iren','Andrew','Kate','Jim']
rn_list = func(list_name,10)
print(rn_list)

print(func_max_slov(list_name,rn_list))

print(func_min_symb(rn_list))

