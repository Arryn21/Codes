"""
Money Split Program
11 August 2021
Coded by Arryn Rex
"""


v = {"uber": 130, "auto": 50, "train": 1800, "sing": 160}
lv = (26, 10, 360, 120, 362, 112, 57, 20, 8, 37.5, 164, 200, 120, 30)

a = {"train": 1810, "ShabsCafe": 560, "ice-cream": 285}
la = (26, 10, 360, 80, 362, 112, 57, 20, 8, 164, 200, 30)

k = {"auto": 100, "water": 40, "autoB": 150, "bus": 820}
lk = (26, 10, 360, 362, 112, 57, 20, 8, 37.5, 164, 200, 30)

ri = {}
lri = (26, 10, 360, 80, 362, 112, 57, 20, 8, 37.5, 164, 200, 30)

ru = {"bus": 1000, "sing": 200, "tovi": 120, "auto": 150}
lru = (26, 10, 360, 80, 362, 112, 57, 20, 8, 37.5, 164, 200, 30)

v_values = v.values()
a_values = a.values()
k_values = k.values()
ri_values = ri.values()
ru_values = ru.values()
count = sum(v_values) + sum(a_values) + sum(k_values) + sum(ri_values) + sum(ru_values)
# print("Vishal: ", sum(lv))
# print("Aman: ", sum(la))
# print("Kapil: ", sum(lk))
# print("Rinkle: ", sum(lri))
# print("Rutvi: ", sum(lru))
count1 = sum(lv)+sum(la)+sum(lk)+sum(lri)+sum(lru)
print("Total Expense: ", count)
print("Total Expense1: ", count1)
#
# print("Vishal  ", sum(v_values))
# print("Aman   ", sum(a_values))
# print("Kapil  ", sum(k_values))
# print("Rinkle  ", sum(ri_values))
# print("Rutvi  ", sum(ru_values))

print("Vishal = ", sum(v_values) - sum(lv))
print("Aman = ", sum(a_values) - sum(la))
print("Kapil = ", sum(k_values) - sum(lk))
print("Rinkle = ", sum(ri_values) - sum(lri))
print("Rutvi = ", sum(ru_values) - sum(lru))

"""
OutPut:
Total Expense:  7375
Total Expense1:  7375.0
Vishal =  513.5
Aman =  1226
Kapil =  -276.5
Rinkle =  -1466.5
Rutvi =  3.5

"""
