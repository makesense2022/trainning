"""
练习 08: 异步错误处理
难度: 🟡 进阶
预计时间: 20分钟

目标：处理异步函数中的错误
"""

import asyncio


async def flaky_async_task(n: int) -> int:
    """
    可能失败的异步任务
    
    参数:
        n: 数字（如果<0会失败）
    
    返回:
        结果
    """
    await asyncio.sleep(0.1)
    if n < 0:
        raise ValueError("数字不能为负")
    return n * 2


async def handle_async_errors(tasks: list) -> list:
    """
    处理异步任务中的错误
    
    参数:
        tasks: 异步任务列表
    
    返回:
        结果列表（包含错误信息）
    """
    # TODO: 使用asyncio.gather处理错误
    results = []
    for task in tasks:
        try:
            result = await task
            results.append({"success": True, "result": result})
        except Exception as e:
            results.append({"success": False, "error": str(e)})
    return results


if __name__ == "__main__":
    tasks = [flaky_async_task(5), flaky_async_task(-1), flaky_async_task(3)]
    results = asyncio.run(handle_async_errors(tasks))
    print(results)

