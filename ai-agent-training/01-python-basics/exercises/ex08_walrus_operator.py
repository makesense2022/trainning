"""
练习 08: 海象运算符 (Walrus Operator) :=
难度: 🟡 进阶
预计时间: 10分钟

Python 3.8+ 新特性
允许在表达式中赋值，减少重复代码
"""


def use_walrus_in_while():
    """
    在while循环中使用海象运算符
    
    关键区别：
    ❌ 传统方式（需要重复写input()）：
        line = input()              # 第一次调用
        while line != "quit":
            process(line)
            line = input()          # 每次循环都要重复调用！
    
    ✅ 海象运算符（只需写一次）：
        while (line := input()) != "quit":  # 在条件中同时赋值和判断
            process(line)
    
    为什么不能用 line = input()？
    - 如果只用 line = input()，条件判断 line != "quit" 需要分开
    - 这样就必须在循环外先调用一次，循环内再调用一次
    - 海象运算符让赋值和判断在同一个表达式中完成，避免重复代码
    
    返回:
        处理的行数（模拟）
    """
    # TODO: 演示海象运算符（用模拟数据）
    count = 0
    lines = ["hello", "world", "quit"]
    index = 0
    
    # 模拟海象运算符：在条件中同时"读取"和判断
    def mock_input():
        nonlocal index
        if index < len(lines):
            result = lines[index]
            index += 1
            return result
        return "quit"
    
    # 使用海象运算符的方式
    while (line := mock_input()) != "quit":
        count += 1
        # process(line)  # 处理这一行
    
    return count


def use_walrus_in_list_comp():
    """
    在列表推导式中使用海象运算符
    
    关键区别：
    ❌ 传统方式（需要先计算，再判断）：
        results = []
        for item in items:
            value = expensive_function(item)  # 先计算
            if value > 10:                   # 再判断
                results.append(value)        # 还要用value
    
    ✅ 海象运算符（一次完成）：
        results = [value for item in items if (value := expensive_function(item)) > 10]
        # 在if条件中同时计算和判断，并且value可以在列表中使用
    
    为什么不能用 value = expensive_function(item)？
    - 列表推导式中不能直接写赋值语句
    - 海象运算符允许在表达式中赋值，同时返回值用于判断和使用
    
    返回:
        符合条件的值列表
    """
    # TODO: 使用海象运算符优化列表推导式
    items = [5, 8, 12, 15, 3, 20]
    
    def expensive_function(x):
        """模拟耗时计算"""
        return x * 2
    
    # 使用海象运算符：在条件中计算，在结果中使用
    results = [value for item in items if (value := expensive_function(item)) > 10]
    return results


if __name__ == "__main__":
    # 演示while循环中的海象运算符
    print("while循环示例:")
    print(f"处理了 {use_walrus_in_while()} 行")
    
    # 演示列表推导式中的海象运算符
    print("\n列表推导式示例:")
    print(use_walrus_in_list_comp())
    
    # 实际对比示例
    print("\n--- 实际对比 ---")
    print("传统方式需要写两次input():")
    print("  line = input()")
    print("  while line != 'quit':")
    print("      process(line)")
    print("      line = input()  # 重复！")
    print("\n海象运算符只需写一次:")
    print("  while (line := input()) != 'quit':")
    print("      process(line)")

