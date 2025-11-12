"""
练习 04: 异步推导式
难度: 🟡 进阶
预计时间: 15分钟

目标：使用异步列表推导式
"""

import asyncio


async def async_task(n: int) -> int:
    """异步任务"""
    await asyncio.sleep(0.1)
    return n * 2


async def async_list_comprehension(numbers: list) -> list:
    """
    异步列表推导式
    
    参数:
        numbers: 数字列表
    
    返回:
        处理后的列表
    """
    # TODO: 使用异步推导式（注意语法）
    # Python 3.6+: [await async_task(n) async for n in numbers]
    # 但更常用的是：
    tasks = [async_task(n) for n in numbers]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    results = asyncio.run(async_list_comprehension(numbers))
    print(results)

