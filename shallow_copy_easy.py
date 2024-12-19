import copy

b = [1, 2, 3, [4, 5]]
b_copy = copy.copy(b)

def func1(params):
    params[0] = 100
    return params
    
print(f'원본: {b}')  # [1, 2, 3, [4, 5]]
func1(b_copy)
print(b_copy)       # [100, 2, 3, [4, 5]]
print(b, end="\n\n")            # [1, 2, 3, [4, 5]] -> 원본 불변

def func2(params):
    params[3][0] = 500
    return params

print(f'원본: {b}')  # [1, 2, 3, [4, 5]]
func2(b_copy)
print(b_copy)       # [1, 2, 3, [500, 5]]
print(b)            # [1, 2, 3, [500, 5]] -> 원본 변경