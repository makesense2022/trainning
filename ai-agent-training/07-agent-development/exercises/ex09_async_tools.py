"""
练习 09: 异步工具
难度: 🔴 挑战
预计时间: 30分钟

目标：创建异步工具（提高性能）
"""

from langchain.tools import tool
import asyncio


@tool
async def async_fetch_data(url: str) -> str:
    """
    异步获取数据
    
    参数:
        url: URL
    
    返回:
        数据字符串
    """
    # TODO: 实现异步获取
    await asyncio.sleep(0.1)  # 模拟网络请求
    return f"Data from {url}"


async def run_async_tool(tool_func, *args):
    """
    运行异步工具
    
    参数:
        tool_func: 异步工具函数
        *args: 参数
    
    返回:
        结果
    """
    # TODO: 调用异步工具
    return await tool_func(*args)


if __name__ == "__main__":
    result = asyncio.run(run_async_tool(async_fetch_data, "https://example.com"))
    print(result)

