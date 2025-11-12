"""
练习 01 参考答案: 变量赋值和类型推断
"""


def create_user_info():
    """创建用户信息字典"""
    name = "张三"
    age = 28
    is_active = True
    salary = 15000.5
    
    return {
        "name": name,
        "age": age,
        "is_active": is_active,
        "salary": salary
    }


def swap_values(a, b):
    """
    交换两个值
    
    Python的多重赋值特性：
    - 右边的值会先被打包成一个元组
    - 然后同时赋值给左边的多个变量
    - 这样就不需要临时变量了
    """
    a, b = b, a
    return a, b


def variable_reassignment():
    """
    演示Python的动态类型
    
    Python是动态类型语言：
    - 变量只是对象的引用（类似JS）
    - 可以在运行时改变变量指向的对象类型
    - 这在TypeScript中会报错，但Python允许
    """
    x = 10          # x现在是int类型
    x = "hello"     # x现在是str类型
    x = [1, 2, 3]   # x现在是list类型
    return x


# 额外知识点：类型注解（可选但推荐）
def create_user_info_typed() -> dict:
    """带类型注解的版本（类似TypeScript）"""
    name: str = "张三"
    age: int = 28
    is_active: bool = True
    salary: float = 15000.5
    
    return {
        "name": name,
        "age": age,
        "is_active": is_active,
        "salary": salary
    }


if __name__ == "__main__":
    print(create_user_info())
    print(swap_values(5, 10))
    print(variable_reassignment())

