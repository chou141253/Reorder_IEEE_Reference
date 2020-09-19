import json

reference_name = {}
name2name = {}

with open('b.txt', 'r', encoding="utf-8") as ftxt:
    datas = ftxt.read().split('\n')

name_with_index = {}
counter = 1
for d in datas:
    if d.replace(" ", "") == "":
        continue

    #print(d)
    first_c = d.split("}")[1].replace(" ", "")[0].lower()
    #print("b"+str(counter), first_c)
    name_with_index["b"+str(counter)] = ord(first_c)
    reference_name["b"+str(counter)] = d
    counter += 1


for name in name_with_index:
    print(name, name_with_index[name])

sort_orders = sorted(name_with_index.items(), key=lambda x: x[1], reverse=False)

print(len(sort_orders))

for name in sort_orders:
    print(name)


j = 0
for name in name_with_index:
    name2name[name] = sort_orders[j]
    j += 1

print()
print()

print(name2name)
print(reference_name)

with open("ori_reference", "w") as fjson:
    fjson.write(json.dumps(reference_name, indent=2))

print()

name2tmp = {}
b2b = {}


counter = 1
for name in sort_orders:
    name2tmp[name[0]] = "x"*10 + "_tmp_"+name[0]+"_" + "x"*10
    b2b["x"*10 + "_tmp_"+name[0]+"_" + "x"*10] =  "b" + str(counter)
    counter += 1


print(name2tmp)
print(b2b)


with open('a.txt', "r", encoding="utf-8") as ftxt:
    datas = ftxt.read()


for name in name2tmp:
    datas = datas.replace("\\cite{"+name+"}", "\\cite{"+name2tmp[name]+"}")

for name in b2b:
    datas = datas.replace("\\cite{"+name+"}", "\\cite{"+b2b[name]+"}")

for name in name2name:
    change_name = name2name[name][0]
    datas = datas.replace(reference_name[name], reference_name[change_name].replace(change_name, name))

with open('a_change.txt', 'w', encoding="utf-8") as ftxt:
    ftxt.write(datas)
    
