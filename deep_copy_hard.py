import copy

# 복잡한 중첩 데이터 구조
original = {
    "numbers": [1, 2, {"inner_list": [3, 4, 5]}],
    "strings": ("hello", "world"),
    "nested_dict": {
        "key1": [10, 20, {"deep_key": "deep_value"}],
        "key2": (100, 200)
    }
}

# Deep copy
deep_copied = copy.deepcopy(original)

# 원본과 deep copy의 차이를 드러내기 위한 다양한 변경 작업
# 1. 중첩된 리스트의 값 변경
deep_copied["numbers"][2]["inner_list"][0] = 999

# 2. 중첩된 딕셔너리 값 변경
deep_copied["nested_dict"]["key1"][2]["deep_key"] = "modified_value"

# 3. 튜플 변경 시도 (튜플은 immutable 객체이므로 변경 불가, 새로운 값으로 대체)
deep_copied["strings"] = ("modified", "tuple")

# 원본과 deep copy 비교 출력
def compare_structures(original, modified, depth=0):
    indent = "  " * depth
    if isinstance(original, dict):
        for key in original:
            if key in modified:
                print(f"{indent}{key}:")
                compare_structures(original[key], modified[key], depth + 1)
            else:
                print(f"{indent}{key}: [MISSING IN MODIFIED]")
    elif isinstance(original, list):
        for i, item in enumerate(original):
            if i < len(modified):
                print(f"{indent}Index {i}:")
                compare_structures(item, modified[i], depth + 1)
            else:
                print(f"{indent}Index {i}: [MISSING IN MODIFIED]")
    else:
        print(f"{indent}Original: {original}, Modified: {modified}")

print("Original structure:")
print(original)
print("\nDeep copied and modified structure:")
print(deep_copied)
print("\nComparison between original and modified:", end="\n\n")
compare_structures(original, deep_copied)