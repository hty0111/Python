#可索引，可切片，不可修改
tuple = (1, 2, 3)
tuple = (0,) + tuple[:]
print(tuple)