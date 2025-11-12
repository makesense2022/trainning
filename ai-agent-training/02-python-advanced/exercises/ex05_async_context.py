"""
练习 05: 异步上下文管理器
难度: 🔴 挑战
预计时间: 25分钟

目标：创建异步上下文管理器
"""

import asyncio


class AsyncResource:
    """异步资源类"""
    
    async def __aenter__(self):
        """进入上下文"""
        print("获取资源...")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        print("释放资源...")
        await asyncio.sleep(0.1)
        return False


async def use_async_context():
    """
    使用异步上下文管理器
    
    返回:
        结果
    """
    # TODO: 使用async with
    async with AsyncResource() as resource:
        await asyncio.sleep(0.1)
        return "完成"


if __name__ == "__main__":
    result = asyncio.run(use_async_context())
    print(result)

