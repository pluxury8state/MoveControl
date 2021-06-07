from collections import OrderedDict


def norm_func(list_: list):
    count = 0
    for item in list_:
        try:
            value = int(item)
        except Exception as e:
            count += 1
        else:
            return (' '.join(list_[:count]), value,)


dictionry = OrderedDict()

for k in range(int(input())):
    key, value = norm_func(input().split())
    if dictionry.get(key):
        dictionry[key] = dictionry[key] + value
    else:
        dictionry[key] = value
print(dictionry)
