import sys
"""
worst_code_ever.exe
"""
i = sys.stdin.read().split("\n")
def colser(i):
    cols = []
    for pos in range(len(i[0])):
        col = [x[pos] for x in i]
        cols.append(0 if col.count('1') < col.count('0') else 1)

    return cols

o2=i.copy()
for pos in range(len(i[0])):
    cols = colser(o2)
    temp_o2 = []
    for row in o2:
        if cols[pos]==1 and row[pos]=='1' or cols[pos]==0 and row[pos]=='0':
            temp_o2.append(row)
    o2 = temp_o2
    if len(o2)==1: break

co2=i.copy()
for pos in range(len(i[0])):
    cols = colser(co2)
    temp_co2 = []
    for row in co2:
        if cols[pos]==1 and row[pos]=='0' or cols[pos]==0 and row[pos]=='1':
            temp_co2.append(row)
    co2 = temp_co2

    if len(co2)==1: break
print(int(o2[0],2)*int(co2[0],2))