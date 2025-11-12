"""
练习 13: 列表推导式 (List Comprehension)
难度: 🟡 进阶
预计时间: 15分钟

对比学习：
JS:  array.filter(x => x > 0).map(x => x * 2)
Python: [x * 2 for x in array if x > 0]

这是Python最强大的特性之一！一行代码搞定过滤+映射+嵌套循环
"""


def filter_and_double(numbers):
    """
    过滤出偶数并将它们翻倍
    
    JS实现:
    const result = numbers
        .filter(x => x % 2 === 0)
        .map(x => x * 2);
    
    Python实现（使用列表推导式）:
    result = [x * 2 for x in numbers if x % 2 == 0]
    
    参数:
        numbers: 整数列表，如 [1, 2, 3, 4, 5]
    
    返回:
        list: 偶数翻倍后的列表，如 [4, 8]
    """
    # TODO: 使用列表推导式实现（一行代码）
    pass


def nested_list_flatten(matrix):
    """
    将二维列表展平为一维列表
    
    JS实现:
    const result = matrix.flat();
    // 或者 matrix.reduce((acc, row) => acc.concat(row), [])
    
    Python实现（嵌套列表推导式）:
    result = [item for row in matrix for item in row]
    
    参数:
        matrix: 二维列表，如 [[1, 2], [3, 4], [5, 6]]
    
    返回:
        list: 一维列表，如 [1, 2, 3, 4, 5, 6]
    """
    # TODO: 使用列表推导式实现（一行代码）
    pass


def create_coordinate_pairs(x_list, y_list):
    """
    创建坐标对
    
    将两个列表的所有组合生成坐标元组
    
    示例:
        x_list = [1, 2]
        y_list = [3, 4]
        结果: [(1, 3), (1, 4), (2, 3), (2, 4)]
    
    JS实现（嵌套循环）:
    const result = [];
    for (const x of x_list) {
        for (const y of y_list) {
            result.push([x, y]);
        }
    }
    
    Python实现（列表推导式）:
    result = [(x, y) for x in x_list for y in y_list]
    
    参数:
        x_list: x坐标列表
        y_list: y坐标列表
    
    返回:
        list: 坐标元组列表
    """
    # TODO: 使用列表推导式实现（一行代码）
    pass


def conditional_mapping(numbers):
    """
    条件映射：正数变平方，负数变0，0保持不变
    
    示例:
        [1, -2, 0, 3, -4] -> [1, 0, 0, 9, 0]
    
    JS实现:
    const result = numbers.map(x => 
        x > 0 ? x * x : (x < 0 ? 0 : x)
    );
    
    Python实现（带条件表达式的列表推导式）:
    result = [x*x if x > 0 else (0 if x < 0 else x) for x in numbers]
    
    参数:
        numbers: 整数列表
    
    返回:
        list: 处理后的列表
    """
    # TODO: 使用列表推导式实现
    pass


def extract_emails(users):
    """
    从用户字典列表中提取所有邮箱
    
    JS实现:
    const emails = users
        .filter(u => u.email)
        .map(u => u.email.toLowerCase());
    
    Python实现:
    emails = [u['email'].lower() for u in users if 'email' in u]
    
    参数:
        users: 用户字典列表
        示例: [
            {"name": "Alice", "email": "ALICE@example.com"},
            {"name": "Bob"},
            {"name": "Charlie", "email": "charlie@example.com"}
        ]
    
    返回:
        list: 小写的邮箱列表，如 ["alice@example.com", "charlie@example.com"]
    """
    # TODO: 使用列表推导式实现
    pass


def performance_comparison():
    """
    性能对比：列表推导式 vs 传统循环
    
    这个函数演示列表推导式的性能优势
    不需要实现，只需阅读理解
    """
    import time
    
    n = 1000000
    
    # 方式1：传统循环
    start = time.time()
    result1 = []
    for i in range(n):
        if i % 2 == 0:
            result1.append(i * 2)
    time1 = time.time() - start
    
    # 方式2：列表推导式
    start = time.time()
    result2 = [i * 2 for i in range(n) if i % 2 == 0]
    time2 = time.time() - start
    
    print(f"传统循环: {time1:.4f}秒")
    print(f"列表推导式: {time2:.4f}秒")
    print(f"速度提升: {time1/time2:.2f}x")
    
    return time1 > time2  # 列表推导式通常更快


# 测试代码
if __name__ == "__main__":
    print("测试 filter_and_double:")
    print(filter_and_double([1, 2, 3, 4, 5, 6]))
    # 预期: [4, 8, 12]
    
    print("\n测试 nested_list_flatten:")
    print(nested_list_flatten([[1, 2], [3, 4], [5, 6]]))
    # 预期: [1, 2, 3, 4, 5, 6]
    
    print("\n测试 create_coordinate_pairs:")
    print(create_coordinate_pairs([1, 2], [3, 4]))
    # 预期: [(1, 3), (1, 4), (2, 3), (2, 4)]
    
    print("\n测试 conditional_mapping:")
    print(conditional_mapping([1, -2, 0, 3, -4]))
    # 预期: [1, 0, 0, 9, 0]
    
    print("\n测试 extract_emails:")
    users = [
        {"name": "Alice", "email": "ALICE@example.com"},
        {"name": "Bob"},
        {"name": "Charlie", "email": "charlie@example.com"}
    ]
    print(extract_emails(users))
    # 预期: ["alice@example.com", "charlie@example.com"]
    
    print("\n性能对比:")
    performance_comparison()

