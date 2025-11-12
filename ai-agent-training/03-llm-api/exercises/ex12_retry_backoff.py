"""
练习 12: 指数退避重试
难度: 🔴 挑战
预计时间: 25分钟

目标：实现指数退避重试策略
"""

from openai import OpenAI, APIError, RateLimitError
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()


def exponential_backoff_retry(func, max_retries: int = 3, base_delay: float = 1.0):
    """
    指数退避重试装饰器
    
    参数:
        func: 要重试的函数
        max_retries: 最大重试次数
        base_delay: 基础延迟（秒）
    
    返回:
        包装后的函数
    """
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except (APIError, RateLimitError) as e:
                if attempt == max_retries - 1:
                    raise e
                
                # 指数退避：1s, 2s, 4s...
                delay = base_delay * (2 ** attempt)
                # 添加随机抖动
                jitter = random.uniform(0, 0.1 * delay)
                wait_time = delay + jitter
                
                print(f"重试 {attempt + 1}/{max_retries}，等待 {wait_time:.2f}秒...")
                time.sleep(wait_time)
        
        return None
    return wrapper


@exponential_backoff_retry(max_retries=3)
def chat_with_retry(client: OpenAI, message: str) -> str:
    """
    带重试的聊天调用
    
    参数:
        client: OpenAI客户端
        message: 消息
    
    返回:
        AI回复
    """
    # TODO: 实现聊天调用（会自动重试）
    if not os.getenv("OPENAI_API_KEY"):
        return "请设置API Key"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        result = chat_with_retry(client, "Hello")
        print(result)

