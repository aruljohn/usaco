"""
ID: arulsjo1
LANG: PYTHON3
TASK: gift1
"""
# input
lines = []
with open('gift1.in', 'r') as fin:
    lines = fin.readlines()
lines = [x.strip() for x in lines]

names = []
money = {}

num_of_friends = int(lines[0])
for i in range(1, num_of_friends+1):
    name = lines[i]
    names.append(name)
    money[name] = 0

i = num_of_friends+2
while i < len(lines):
    line = lines[i].strip()
    if ' ' in line:
        donation, num = [int(x) for x in line.split(' ')]
        donor = lines[i - 1]
        if num > 0:
            money[donor] -= donation
            money[donor] += donation % num
        if num > 0:
            donation_per_person = int(donation / num)
            for j in range(1, num+1):
                donated_name = lines[i + j]
                money[donated_name] += donation_per_person
        else:
            num += 1
        i += num
    else:
        i += 1
    
with open('gift1.out', 'w') as fout:
    for name in names:
        fout.write(name + ' ' + str(money[name]) + '\n')
