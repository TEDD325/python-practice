class MyClass:
    class_variable = "I am class variable"

    def __init__(self, value):
        # self는 인스턴스 자기 자신을 나타내는 파라미터
        self.value = value

    def instance_method(self):
        # instance method는 반드시 첫 번째 파라미터로 self를 받아야만 한다.
            # self를 통해 인스턴스 상태에 접근 가능
        return f"Instance method: value={self.value}, class_variable={self.class_variable}"

    @classmethod
    def class_method(cls):
        # class method는 첫 번째 파라미터로 cls를 받는다.
            # cls를 통해 클래스 상태에 접근 가능
            # 인스턴스 없이도 호출 가능
        return f"Class method: class_variable={cls.class_variable}"

    @staticmethod
    def static_method(x, y):
        # static method는 클래스나 인스턴스 상태에 의존하지 않는 메서드
        # 첫 번째 파라미터로 self나 cls 등을 받을 필요 없음
        return f"Static method: x+y={x+y}"


# 사용 예시
instance = MyClass(10)
print(instance.instance_method())  # 인스턴스로 instance_method 접근
print(MyClass.class_method())      # 클래스로 class_method 접근
print(MyClass.static_method(3, 5)) # 클래스로 static_method 접근