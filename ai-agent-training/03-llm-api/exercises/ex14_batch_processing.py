"""
练习 14: 批量处理
难度: 🔴 挑战
预计时间: 30分钟

目标：批量处理多个请求，提高效率
"""

from openai import OpenAI
import asyncio
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()


def batch_chat_sync(client: OpenAI, messages: List[str]) -> List[str]:
    """
    同步批量处理
    
    参数:
        client: OpenAI客户端
        messages: 消息列表
    
    返回:
        回复列表
    """
    # TODO: 顺序处理所有消息
    results = []
    for msg in messages:
        if not os.getenv("OPENAI_API_KEY"):
            results.append("请设置API Key")
            continue
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        results.append(response.choices[0].message.content)
    return results


async def batch_chat_async(client: OpenAI, messages: List[str]) -> List[str]:
    """
    异步批量处理（更快）
    
    参数:
        client: OpenAI客户端
        messages: 消息列表
    
    返回:
        回复列表
    """
    # TODO: 使用asyncio并发处理
    async def process_one(msg):
        # 注意：OpenAI SDK可能需要异步版本
        # 这里用同步版本模拟
        await asyncio.sleep(0.1)  # 模拟异步
        if not os.getenv("OPENAI_API_KEY"):
            return "请设置API Key"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        return response.choices[0].message.content
    
    tasks = [process_one(msg) for msg in messages]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        messages = ["什么是Python？", "什么是JavaScript？", "什么是AI？"]
        
        # 同步处理
        results_sync = batch_chat_sync(client, messages)
        print("同步结果:", len(results_sync))
        
        # 异步处理
        results_async = asyncio.run(batch_chat_async(client, messages))
        print("异步结果:", len(results_async))

