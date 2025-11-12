"""
练习 03: 并发HTTP请求
难度: 🟡 进阶
预计时间: 20分钟

目标：使用异步编程并发处理HTTP请求
"""

import asyncio
import aiohttp


async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    """
    异步获取URL
    
    参数:
        session: aiohttp会话
        url: URL
    
    返回:
        响应信息字典
    """
    # TODO: 使用session.get()异步获取
    try:
        async with session.get(url) as response:
            return {
                "url": url,
                "status": response.status,
                "content": await response.text()
            }
    except Exception as e:
        return {"url": url, "error": str(e)}


async def fetch_multiple_urls(urls: list) -> list:
    """
    并发获取多个URL
    
    参数:
        urls: URL列表
    
    返回:
        响应列表
    """
    # TODO: 使用aiohttp和asyncio.gather
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


if __name__ == "__main__":
    urls = ["https://httpbin.org/delay/1"] * 3
    results = asyncio.run(fetch_multiple_urls(urls))
    print(f"获取了 {len(results)} 个URL")

