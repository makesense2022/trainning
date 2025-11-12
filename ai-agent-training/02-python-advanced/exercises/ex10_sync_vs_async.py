"""
练习 10: 同步异步性能对比
难度: 🟡 进阶
预计时间: 20分钟

目标：对比同步和异步的性能差异
"""

import asyncio
import time
import requests
import aiohttp


def sync_fetch_urls(urls: list) -> list:
    """
    同步获取URL（顺序执行）
    
    参数:
        urls: URL列表
    
    返回:
        响应列表
    """
    # TODO: 使用requests顺序获取
    results = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            results.append({"url": url, "status": response.status_code})
        except:
            results.append({"url": url, "error": "请求失败"})
    return results


async def async_fetch_urls(urls: list) -> list:
    """
    异步获取URL（并发执行）
    
    参数:
        urls: URL列表
    
    返回:
        响应列表
    """
    # TODO: 使用aiohttp并发获取
    async def fetch_one(session, url):
        try:
            async with session.get(url, timeout=5) as response:
                return {"url": url, "status": response.status}
        except:
            return {"url": url, "error": "请求失败"}
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)


def compare_performance(urls: list) -> dict:
    """
    对比同步和异步性能
    
    参数:
        urls: URL列表
    
    返回:
        性能对比结果
    """
    # TODO: 测量两种方式的耗时
    # 同步
    start = time.time()
    sync_results = sync_fetch_urls(urls)
    sync_time = time.time() - start
    
    # 异步
    start = time.time()
    async_results = asyncio.run(async_fetch_urls(urls))
    async_time = time.time() - start
    
    return {
        "sync_time": sync_time,
        "async_time": async_time,
        "speedup": sync_time / async_time if async_time > 0 else 0
    }


if __name__ == "__main__":
    urls = ["https://httpbin.org/delay/1"] * 3
    comparison = compare_performance(urls)
    print(f"同步耗时: {comparison['sync_time']:.2f}秒")
    print(f"异步耗时: {comparison['async_time']:.2f}秒")
    print(f"加速比: {comparison['speedup']:.2f}x")

