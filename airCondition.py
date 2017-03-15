
with open("stats.csv","r") as f:
    x = f.readlines()
with open("stats10.csv","r") as f10:
    x10 = f10.readlines()

pm = [[],[],[],[]]

for item in x[1:]:
    y = item.split(';')
    if "Aglomeracja Krakowska" in y:
        pm[0].append([int(y[0]),float(y[8].replace(',','.'))])
    elif "Katow" in y[5]:
        pm[1].append([int(y[0]),float(y[8].replace(',','.'))])
for item in x10[1:]:
    y = item.split(';')
    if "Aglomeracja Krakowska" in y:
        pm[2].append([int(y[0]),float(y[8].replace(',','.'))])
    elif "Katow" in y[5]:
        pm[3].append([int(y[0]),float(y[8].replace(',','.'))])


list = [['Kraków','PM 2,5'],['Katowice','PM 2,5'],['Kraków','PM 10'],['Katowice','PM 10']]

lastyear=0
i = 0
y = 0

for l in range(0,4):
    for item in pm[l]:
        if item[0] == lastyear:
            i += 1
            y += item[1]
        else:
            if i!=0:
                list[l].append([lastyear,y/i])
            i = 1
            y = item[1]
            lastyear = item[0]
    list[l].append([lastyear, y / i])
    i = 0
    y = 0
    lastyear = 0

for u in range(0,4):
    for item in list[u]:
        print(item)






