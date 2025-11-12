"""
练习 01: 变量赋值和类型推断
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  const name = "Alice"; let age = 30;
Python: name = "Alice"; age = 30

关键区别：
1. Python没有const/let/var，直接赋值
2. Python是动态类型，但有类型推断
3. Python变量可以重新赋值为不同类型（JS的let也可以）
"""


def create_user_info():
    """
    创建一个用户信息的变量集合
    
    要求：
    1. 创建变量 name，值为 "张三"
    2. 创建变量 age，值为 28
    3. 创建变量 is_active，值为 True
    4. 创建变量 salary，值为 15000.5
    5. 返回一个包含所有变量的字典
    
    返回示例：
    {
        "name": "张三",
        "age": 28,
        "is_active": True,
        "salary": 15000.5
    }
    """
    obj = {
        "name": "张三",
        "age": 28,
        "is_active": True,
        "salary": 15000.5
    }
    return obj


def swap_values(a, b):
    """
    交换两个变量的值（使用Python的多重赋值特性）
    
    JS方式（需要临时变量）:
    let temp = a;
    a = b;
    b = temp;
    
    Python方式（一行搞定）:
    a, b = b, a
    
    参数:
        a: 第一个值
        b: 第二个值
    
    返回:
        tuple: (新的a, 新的b)
    """
    a, b = b, a
    return a, b


def variable_reassignment():
    """
    演示Python的动态类型特性
    
    要求：
    1. 创建变量 x，初始值为整数 10
    2. 将 x 重新赋值为字符串 "hello"
    3. 将 x 重新赋值为列表 [1, 2, 3]
    4. 返回最终的 x
    
    注意：这在TypeScript中会报错，但Python允许！
    """
    x = 10
    x = "hello"
    x = [1, 2, 3]
    return x


# 测试代码（可选）
if __name__ == "__main__":
    # 测试 create_user_info
    print("测试 create_user_info:")
    user = create_user_info()
    print(user)
    print()
    
    # 测试 swap_values
    print("测试 swap_values:")
    a, b = 5, 10
    print(f"交换前: a={a}, b={b}")
    a, b = swap_values(a, b)
    print(f"交换后: a={a}, b={b}")
    print()
    
    # 测试 variable_reassignment
    print("测试 variable_reassignment:")
    result = variable_reassignment()
    print(f"最终结果: {result}, 类型: {type(result)}")

