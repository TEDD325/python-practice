import copy

original = [1, 2, [3, 4]]
deep_copied = copy.deepcopy(original)
deep_copied[2][0] = 100

print(original)      # [1, 2, [3, 4]]
print(deep_copied)   # [1, 2, [100, 4]]
print(original)      # [1, 2, [3, 4]] -> 원본 불변