"""
练习 07: gather和wait
难度: 🟡 进阶
预计时间: 20分钟

目标：理解asyncio.gather和asyncio.wait的区别
"""

import asyncio


async def task(name: str, delay: float) -> str:
    """异步任务"""
    await asyncio.sleep(delay)
    return f"{name}完成"


async def use_gather() -> list:
    """
    使用asyncio.gather（等待所有任务完成）
    
    返回:
        所有任务结果
    """
    # TODO: 使用gather
    tasks = [task("任务1", 0.1), task("任务2", 0.2), task("任务3", 0.1)]
    return await asyncio.gather(*tasks)


async def use_wait() -> dict:
    """
    使用asyncio.wait（可以设置条件）
    
    返回:
        {
            "done": 已完成的任务,
            "pending": 待完成的任务
        }
    """
    # TODO: 使用wait
    tasks = [task("任务1", 0.1), task("任务2", 0.5), task("任务3", 0.2)]
    done, pending = await asyncio.wait(tasks, timeout=0.3)
    return {
        "done": [t.result() for t in done],
        "pending": len(pending)
    }


if __name__ == "__main__":
    results1 = asyncio.run(use_gather())
    print("gather结果:", results1)
    
    results2 = asyncio.run(use_wait())
    print("wait结果:", results2)

