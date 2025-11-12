"""
练习 27: 装饰器 (Decorators)
难度: 🔴 挑战
预计时间: 20分钟

对比学习：
JS:  HOC (Higher-Order Component) 或 函数包装
Python: @decorator 语法糖

装饰器是Python的核心特性，在AI开发中到处都是！
例如：@tool, @chain, @retry, @cache
"""

import time
from functools import wraps


def timing_decorator(func):
    """
    计时装饰器：测量函数执行时间
    
    这是最常见的装饰器模式！
    在AI开发中经常用来监控LLM调用耗时
    
    JS类比：
    function withTiming(fn) {
        return function(...args) {
            const start = Date.now();
            const result = fn(...args);
            const end = Date.now();
            console.log(`${fn.name} took ${end - start}ms`);
            return result;
        }
    }
    
    Python实现：
    def timing_decorator(func):
        @wraps(func)  # 保留原函数的元信息
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f}s")
            return result
        return wrapper
    
    TODO: 实现这个装饰器
    """
    # TODO: 在这里实现
    pass


def retry_decorator(max_attempts=3):
    """
    重试装饰器：失败时自动重试
    
    这是带参数的装饰器！在调用LLM API时非常有用
    
    JS类比：
    function withRetry(maxAttempts) {
        return function(fn) {
            return async function(...args) {
                for (let i = 0; i < maxAttempts; i++) {
                    try {
                        return await fn(...args);
                    } catch (e) {
                        if (i === maxAttempts - 1) throw e;
                    }
                }
            }
        }
    }
    
    使用方式：
    @retry_decorator(max_attempts=3)
    def unreliable_function():
        # 可能失败的函数
        pass
    
    TODO: 实现这个带参数的装饰器
    
    提示：
    1. retry_decorator 接收参数，返回真正的装饰器
    2. 真正的装饰器接收函数，返回包装函数
    3. 包装函数里实现重试逻辑
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: 实现重试逻辑
            # 提示：使用for循环尝试max_attempts次
            # 捕获异常，最后一次失败时抛出
            pass
        return wrapper
    return decorator


def cache_decorator(func):
    """
    缓存装饰器：缓存函数结果（简单版）
    
    在AI开发中用于缓存LLM响应，节省成本
    
    JS类比：
    function withCache(fn) {
        const cache = new Map();
        return function(...args) {
            const key = JSON.stringify(args);
            if (cache.has(key)) {
                return cache.get(key);
            }
            const result = fn(...args);
            cache.set(key, result);
            return result;
        }
    }
    
    TODO: 实现这个装饰器
    
    提示：
    1. 在wrapper外面创建一个dict作为cache
    2. 使用args作为key（需要转换成可哈希的类型）
    3. 先查缓存，没有则调用函数并缓存结果
    """
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: 实现缓存逻辑
        # 提示：用 args 作为 key（tuple是可哈希的）
        pass
    
    return wrapper


def log_decorator(prefix="LOG"):
    """
    日志装饰器：记录函数调用
    
    在AI Agent开发中用于追踪工具调用
    
    使用方式：
    @log_decorator(prefix="TOOL")
    def search_tool(query):
        return f"Results for {query}"
    
    输出：
    [TOOL] Calling search_tool with args: ('Python',), kwargs: {}
    [TOOL] search_tool returned: Results for Python
    
    TODO: 实现这个带参数的装饰器
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: 实现日志逻辑
            # 1. 打印调用信息（函数名、参数）
            # 2. 调用原函数
            # 3. 打印返回值
            # 4. 返回结果
            pass
        return wrapper
    return decorator


# ============ 测试函数 ============

@timing_decorator
def slow_function():
    """测试timing_decorator"""
    time.sleep(0.1)
    return "Done"


@retry_decorator(max_attempts=3)
def flaky_function(succeed_on_attempt=2):
    """测试retry_decorator - 会在第N次调用时成功"""
    if not hasattr(flaky_function, 'attempt'):
        flaky_function.attempt = 0
    flaky_function.attempt += 1
    
    if flaky_function.attempt < succeed_on_attempt:
        raise ValueError(f"Failed on attempt {flaky_function.attempt}")
    
    return f"Success on attempt {flaky_function.attempt}"


@cache_decorator
def expensive_computation(n):
    """测试cache_decorator - 斐波那契数列"""
    print(f"Computing fib({n})...")
    if n <= 1:
        return n
    time.sleep(0.01)  # 模拟耗时计算
    return expensive_computation(n-1) + expensive_computation(n-2)


@log_decorator(prefix="TOOL")
def search_tool(query, limit=10):
    """测试log_decorator"""
    return f"Found {limit} results for '{query}'"


# 测试代码
if __name__ == "__main__":
    print("=" * 50)
    print("测试 timing_decorator:")
    print("=" * 50)
    result = slow_function()
    print(f"结果: {result}\n")
    
    print("=" * 50)
    print("测试 retry_decorator:")
    print("=" * 50)
    flaky_function.attempt = 0  # 重置
    result = flaky_function(succeed_on_attempt=2)
    print(f"结果: {result}\n")
    
    print("=" * 50)
    print("测试 cache_decorator:")
    print("=" * 50)
    print("第一次调用 fib(5):")
    result1 = expensive_computation(5)
    print(f"结果: {result1}")
    print("\n第二次调用 fib(5) (应该使用缓存):")
    result2 = expensive_computation(5)
    print(f"结果: {result2}\n")
    
    print("=" * 50)
    print("测试 log_decorator:")
    print("=" * 50)
    result = search_tool("Python", limit=20)
    print()


# ============ 进阶知识：装饰器叠加 ============

def demo_stacked_decorators():
    """
    演示多个装饰器的使用
    
    装饰器从下往上应用：
    @decorator1
    @decorator2
    def func():
        pass
    
    等价于：
    func = decorator1(decorator2(func))
    """
    
    @timing_decorator
    @retry_decorator(max_attempts=2)
    @log_decorator(prefix="API")
    def api_call():
        return "API response"
    
    print("=" * 50)
    print("测试装饰器叠加:")
    print("=" * 50)
    result = api_call()
    print(f"最终结果: {result}")


if __name__ == "__main__":
    demo_stacked_decorators()

