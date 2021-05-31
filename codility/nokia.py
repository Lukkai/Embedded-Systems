s = 'abracadabra'
d = {}
for i in s:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1

print(d)
print(max(d.values()))


LTE_list = ['MME', 'S-GW', 'eNodeB', 'HSS', '1234567']

salvation  = [LTE_list[each] for each in range(len(LTE_list)) if len(LTE_list[each])%2!=0]
# salvation = []
# for i in range(len(LTE_list)):
#     if len(LTE_list[i])%2 != 0:
#         salvation.append(LTE_list[i])
print(salvation)