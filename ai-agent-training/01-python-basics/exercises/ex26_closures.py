"""
练习 26: 闭包（Closure）
难度: 🟡 进阶
预计时间: 15分钟

闭包：内部函数可以访问外部函数的变量
"""


def create_counter():
    """
    创建计数器（使用闭包）
    
    返回:
        一个函数，每次调用返回递增的计数
    
    示例:
        counter = create_counter()
        counter() -> 1
        counter() -> 2
        counter() -> 3
    """
    # TODO: 使用闭包实现计数器
    count = 0
    
    def counter():
        nonlocal count  # 声明使用外部变量
        count += 1
        return count
    
    return counter


def create_accumulator(initial: int = 0):
    """
    创建累加器
    
    参数:
        initial: 初始值
    
    返回:
        累加函数，每次调用加上传入的值
    
    示例:
        acc = create_accumulator(10)
        acc(5) -> 15
        acc(3) -> 18
    """
    # TODO: 使用闭包实现累加器
    pass


def create_cache():
    """
    创建缓存函数（使用闭包）
    
    返回:
        一个缓存函数，可以缓存计算结果
    
    示例:
        cache_func = create_cache()
        cache_func("key1", lambda: expensive_computation())  # 计算
        cache_func("key1", lambda: expensive_computation())  # 从缓存返回
    """
    # TODO: 使用闭包实现缓存
    cache = {}
    
    def cached(key, func):
        if key not in cache:
            cache[key] = func()
        return cache[key]
    
    return cached


if __name__ == "__main__":
    counter = create_counter()
    print(counter())  # 1
    print(counter())  # 2
    
    acc = create_accumulator(10)
    print(acc(5))  # 15
    print(acc(3))  # 18
    
    cache_func = create_cache()
    result1 = cache_func("key1", lambda: "expensive result")
    result2 = cache_func("key1", lambda: "expensive result")
    print(result1 == result2)  # True

