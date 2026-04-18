def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
lst = [1,2]
print(add_item(2,lst))
print(add_item(3))