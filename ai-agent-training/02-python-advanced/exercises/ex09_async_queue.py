"""
练习 09: 异步队列
难度: 🔴 挑战
预计时间: 30分钟

目标：使用异步队列处理任务
"""

import asyncio


async def producer(queue: asyncio.Queue, items: list):
    """
    生产者（向队列添加任务）
    
    参数:
        queue: 异步队列
        items: 任务列表
    """
    # TODO: 向队列添加任务
    for item in items:
        await queue.put(item)
        await asyncio.sleep(0.1)
    await queue.put(None)  # 结束信号


async def consumer(queue: asyncio.Queue):
    """
    消费者（从队列获取任务并处理）
    
    参数:
        queue: 异步队列
    
    返回:
        处理结果列表
    """
    # TODO: 从队列获取并处理
    results = []
    while True:
        item = await queue.get()
        if item is None:
            break
        # 处理任务
        result = f"处理了: {item}"
        results.append(result)
        queue.task_done()
    return results


async def producer_consumer_demo():
    """
    生产者-消费者演示
    
    返回:
        处理结果
    """
    # TODO: 创建队列并运行生产者和消费者
    queue = asyncio.Queue()
    items = [1, 2, 3, 4, 5]
    
    # 并发运行
    results = await asyncio.gather(
        producer(queue, items),
        consumer(queue)
    )
    return results[1]  # 返回消费者结果


if __name__ == "__main__":
    results = asyncio.run(producer_consumer_demo())
    print(results)

