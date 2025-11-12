"""
练习 02: asyncio事件循环
难度: 🟡 进阶
预计时间: 20分钟

目标：理解asyncio事件循环的工作原理
"""

import asyncio


async def task1():
    """任务1"""
    await asyncio.sleep(1)
    return "任务1完成"


async def task2():
    """任务2"""
    await asyncio.sleep(1)
    return "任务2完成"


async def run_concurrent_tasks() -> list:
    """
    并发运行多个任务
    
    返回:
        任务结果列表
    """
    # TODO: 使用asyncio.gather并发运行
    results = await asyncio.gather(task1(), task2())
    return results


async def run_with_timeout(coro, timeout: float):
    """
    带超时的协程执行
    
    参数:
        coro: 协程对象
        timeout: 超时时间（秒）
    
    返回:
        结果或None（如果超时）
    """
    # TODO: 使用asyncio.wait_for
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return None


def run_async_main():
    """运行异步主函数"""
    # TODO: 使用asyncio.run()
    results = asyncio.run(run_concurrent_tasks())
    return results


if __name__ == "__main__":
    results = run_async_main()
    print(results)

