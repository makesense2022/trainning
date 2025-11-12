"""
练习 16: 多继承和MRO
难度: 🔴 挑战
预计时间: 25分钟

目标：理解Python的多继承和方法解析顺序（MRO）
"""


class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return "B"


class C(A):
    def method(self):
        return "C"


class D(B, C):
    """多继承：D继承B和C"""
    pass


def get_mro(cls) -> list:
    """
    获取类的MRO（方法解析顺序）
    
    参数:
        cls: 类
    
    返回:
        MRO列表
    """
    # TODO: 使用__mro__或mro()方法
    return list(cls.__mro__)


if __name__ == "__main__":
    d = D()
    print(d.method())  # 应该调用哪个？
    print("MRO:", get_mro(D))

