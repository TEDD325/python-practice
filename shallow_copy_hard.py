# 이 코드는 shallow copy의 동작을 복잡한 구조에서 살펴보는 예시이다.
# deepcopy와 shallow copy의 차이를 명확히 보여주기 위해 다양한 자료구조(리스트, 딕셔너리)와 함수를 사용한다.
# 또한 클래스 인스턴스를 포함하여 참조 관계를 확인한다.

import copy

class CustomObj:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def mutate(self):
        # 객체 내부의 리스트를 변경하는 메소드
        if self.data and isinstance(self.data, list):
            self.data[0] = "MUTATED"

    def __repr__(self):
        return f"CustomObj(name={self.name}, data={self.data})"

# 복잡한 데이터 구조
original = [
    1,
    2,
    [3, 4, [5, 6, [7, 8]]],
    {"a": [10, 20], "b": {"nested_key": [100, 200]}},
    CustomObj("obj1", [999, 1000])
]

# shallow copy를 수행
shallow_copied = copy.copy(original)

def mutate_outer_structure(params):
    # 가장 바깥 리스트의 첫 번째 값 변경
    params[0] = 9999
    # 딕셔너리 내부 리스트 값 변경
    params[3]["a"][0] = "CHANGED"
    return params

def mutate_deep_structure(params):
    # deeply nested 구조 변경
    # params[2][2][2][0] = 700 -> 인덱스가 너무 깊으니 변수에 담아 해보자.
    nested_ref = params[2][2][2]  # [7, 8]
    nested_ref[0] = "DEEPLY_CHANGED"
    # 딕셔너리 내부 더 깊은 구조 변경
    params[3]["b"]["nested_key"][1] = "DEEPLY_MUTATED"
    return params

def mutate_custom_obj(params):
    # CustomObj 내부 데이터 변경
    if isinstance(params[4], CustomObj):
        params[4].mutate()
    return params

print("원본:", original)
print("shallow copy:", shallow_copied, "\n")

print("외부 구조 변경")
print("원본:", original)
mutate_outer_structure(shallow_copied) # 최상위 수준에서만 복사를 수행
print("shallow copy:", shallow_copied)
print("원본:", original, "\n") # 최상단의 요소들의 원본은 변경되지 않으나, shallow copy로 인해 중첩된 요소들의 원본은 변경된다.

print("중첩 구조 변경")
print("원본:", original)
mutate_deep_structure(shallow_copied)
print("shallow copy:", shallow_copied)
print("원본:", original, "\n")

print("커스텀 객체 변경")
print("원본:", original)
mutate_custom_obj(shallow_copied)
print("shallow copy:", shallow_copied)
print("원본:", original, "\n")

# 이 결과를 통해 shallow copy는 1차원적인 참조 복사만 수행하여,
# 중첩된 mutable 객체나 사용자 정의 객체 내부의 변화가 원본에도 영향을 미친다는 점을 확인할 수 있다.