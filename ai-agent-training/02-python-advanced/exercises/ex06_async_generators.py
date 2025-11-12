"""
练习 06: 异步生成器
难度: 🔴 挑战
预计时间: 25分钟

目标：创建异步生成器
"""

import asyncio


async def async_number_generator(n: int):
    """
    异步数字生成器
    
    参数:
        n: 生成0到n-1的数字
    
    返回:
        异步生成器
    """
    # TODO: 使用async for和yield
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i


async def consume_async_generator():
    """
    消费异步生成器
    
    返回:
        结果列表
    """
    # TODO: 使用async for
    results = []
    async for value in async_number_generator(5):
        results.append(value)
    return results


if __name__ == "__main__":
    results = asyncio.run(consume_async_generator())
    print(results)

