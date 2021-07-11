# 唯一性，不可用下标访问
List = list((1, 2, 3, 4, 4, 2, 0))
Set = set(List)
print(Set)                #自动排序
Set.add(6)
print(Set)
Set.remove(4)
print(Set)

Set = frozenset([1, 2, 3])  #不可变集合
