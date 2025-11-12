"""
练习 40: 生成器和yield
难度: 🔴 挑战
预计时间: 20分钟

生成器：使用yield创建迭代器，内存高效
"""


def number_generator(n: int):
    """
    数字生成器
    
    参数:
        n: 生成0到n-1的数字
    
    返回:
        生成器对象
    
    示例:
        gen = number_generator(5)
        list(gen) -> [0, 1, 2, 3, 4]
    """
    # TODO: 使用yield创建生成器
    for i in range(n):
        yield i


def fibonacci_generator(n: int):
    """
    斐波那契数列生成器
    
    参数:
        n: 生成前n个斐波那契数
    
    返回:
        生成器对象
    """
    # TODO: 使用yield生成斐波那契数
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def infinite_counter(start: int = 0):
    """
    无限计数器生成器
    
    参数:
        start: 起始值
    
    返回:
        无限生成器
    """
    # TODO: 无限生成数字
    count = start
    while True:
        yield count
        count += 1


def generator_expression_example():
    """
    生成器表达式（类似列表推导式，但用()）
    
    返回:
        生成器对象
    """
    # TODO: 使用生成器表达式
    return (x * x for x in range(10))


def chain_generators(*generators):
    """
    链式生成器
    
    参数:
        *generators: 多个生成器
    
    返回:
        链式生成器
    """
    # TODO: 使用yield from链式生成
    for gen in generators:
        yield from gen


if __name__ == "__main__":
    # 测试数字生成器
    gen = number_generator(5)
    print(list(gen))
    
    # 测试斐波那契生成器
    fib = fibonacci_generator(10)
    print(list(fib))
    
    # 测试无限计数器（取前5个）
    counter = infinite_counter(10)
    print([next(counter) for _ in range(5)])
    
    # 测试生成器表达式
    gen_expr = generator_expression_example()
    print(list(gen_expr))
    
    # 测试链式生成器
    gen1 = number_generator(3)
    gen2 = number_generator(3)
    chained = chain_generators(gen1, gen2)
    print(list(chained))

