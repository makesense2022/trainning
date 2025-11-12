"""
练习 01: async/await基础
难度: 🟢 基础
预计时间: 15分钟

对比学习：
JS:  async function fetchData() { const data = await fetch(url); }
Python: async def fetch_data(): data = await fetch(url)

语法几乎完全一样！
"""

import asyncio


async def simple_async_function() -> str:
    """
    简单的异步函数
    
    返回:
        "Hello from async!"
    """
    # TODO: 实现异步函数
    await asyncio.sleep(0.1)  # 模拟异步操作
    return "Hello from async!"


async def fetch_multiple_data(urls: list) -> list:
    """
    并发获取多个URL的数据
    
    JS: Promise.all(urls.map(url => fetch(url)))
    Python: await asyncio.gather(*[fetch(url) for url in urls])
    
    参数:
        urls: URL列表
    
    返回:
        数据列表
    """
    # TODO: 使用asyncio.gather并发执行
    async def fetch_one(url):
        await asyncio.sleep(0.1)  # 模拟网络请求
        return f"Data from {url}"
    
    # TODO: 使用gather并发执行
    pass


async def async_with_timeout(coro, timeout: float):
    """
    带超时的异步操作
    
    参数:
        coro: 协程对象
        timeout: 超时时间（秒）
    
    返回:
        结果或None（如果超时）
    """
    # TODO: 使用asyncio.wait_for实现超时
    pass


if __name__ == "__main__":
    # 运行异步函数
    result = asyncio.run(simple_async_function())
    print(result)
    
    # 测试并发
    urls = ["url1", "url2", "url3"]
    results = asyncio.run(fetch_multiple_data(urls))
    print(results)

