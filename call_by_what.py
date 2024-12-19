"""_summary_
    이 코드는 파이썬의 immutable 객체(예: int, str, tuple)와 mutable 객체(예: list, dict)를 함수에 전달할 때의 동작 차이를 보여준다.
    파이썬은 immutable 객체에 대해서는 사실상 call by value와 유사한 동작을 한다.
"""
# 전역 스코프에 immutable, mutable 객체 정의
immutable_int = 42
immutable_tuple = (1, 2, 3)
mutable_list = [10, 20, 30]

# 함수 호출 전 전역 변수 상태 출력
print(f"전역 변수의 값: \n{immutable_int}\n{immutable_tuple}\n{mutable_list}\n")

def modify_immutable(val):
    # 여기서 val는 immutable_int나 immutable_tuple 같은 immutable 객체를 참조한다.
    # 새로운 객체를 할당하더라도 외부 값(전역변수)에는 영향이 없다.
    val = 999
    return val

def modify_immutable_tuple(tpl):
    # tuple은 immutable 객체이다.
    # 값을 직접 변경할 수 없으므로 새로운 tuple을 할당하면 기존 값(전역변수)에는 아무런 영향이 없다.
    tpl = (9, 9, 9)
    return tpl

def modify_mutable(lst):
    # list는 mutable 객체이다.
    # 내부 값을 변경하면 함수 밖의 변수(전역변수)에도 영향을 준다.
    lst[0] = 999
    return lst

new_int = modify_immutable(immutable_int)
new_tuple = modify_immutable_tuple(immutable_tuple)
new_list = modify_mutable(mutable_list)

print("After modify_immutable:", immutable_int, "->", new_int)
print("After modify_immutable_tuple:", immutable_tuple, "->", new_tuple)
print("After modify_mutable:", mutable_list, "->", new_list, end="\n\n")

# 중첩 함수와 lambda를 활용한 예시
# 내부 함수에서 immutable, mutable 객체를 바꿔보는 경우
def complex_operation(x, y):
    # x: immutable, y: mutable
    def inner_change_immutable(val):
        val = val * 100
        return val
    
    def inner_change_mutable(m):
        m.append("new_item")
        return m

    x_modified = inner_change_immutable(x)  # immutable 객체는 함수 밖으로 영향을 주지 않음
    y_modified = inner_change_mutable(y)    # mutable 객체는 함수 밖으로 영향을 줌
    
    # lambda를 이용한 또 다른 변경 시도
    modifier = lambda z: z + 1 if isinstance(z, int) else None
    x_modified_2 = modifier(x)  # lambda를 통해 x를 바꾸려 하지만 외부에는 영향을 주지 없음
    
    return x_modified, y_modified, x_modified_2

ret = complex_operation(immutable_int, mutable_list)
print("After complex_operation with immutable_int and mutable_list:", ret, end="\n\n")

print(f"전역 변수의 값: \n{immutable_int}\n{immutable_tuple}\n{mutable_list}\n")