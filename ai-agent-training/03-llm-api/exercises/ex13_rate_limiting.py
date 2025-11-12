"""
练习 13: 速率限制处理
难度: 🔴 挑战
预计时间: 25分钟

目标：处理API速率限制
"""

import time
from collections import deque
from openai import OpenAI, RateLimitError
import os
from dotenv import load_dotenv

load_dotenv()


class RateLimiter:
    """速率限制器"""
    
    def __init__(self, max_calls: int, time_window: float):
        """
        初始化速率限制器
        
        参数:
            max_calls: 时间窗口内最大调用次数
            time_window: 时间窗口（秒）
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
    
    def wait_if_needed(self):
        """如果需要，等待直到可以调用"""
        # TODO: 实现速率限制逻辑
        now = time.time()
        
        # 移除过期的调用记录
        while self.calls and self.calls[0] < now - self.time_window:
            self.calls.popleft()
        
        # 如果达到限制，等待
        if len(self.calls) >= self.max_calls:
            wait_time = self.calls[0] + self.time_window - now
            if wait_time > 0:
                print(f"速率限制：等待 {wait_time:.2f}秒...")
                time.sleep(wait_time)
                # 清理过期记录
                while self.calls and self.calls[0] < time.time() - self.time_window:
                    self.calls.popleft()
        
        # 记录本次调用
        self.calls.append(time.time())


def rate_limited_chat(client: OpenAI, limiter: RateLimiter, message: str) -> str:
    """
    带速率限制的聊天调用
    
    参数:
        client: OpenAI客户端
        limiter: 速率限制器
        message: 消息
    
    返回:
        AI回复
    """
    # TODO: 使用速率限制器
    limiter.wait_if_needed()
    
    if not os.getenv("OPENAI_API_KEY"):
        return "请设置API Key"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except RateLimitError:
        print("遇到速率限制，等待后重试...")
        time.sleep(60)  # 等待1分钟
        return rate_limited_chat(client, limiter, message)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        limiter = RateLimiter(max_calls=3, time_window=60.0)  # 每分钟最多3次
        
        for i in range(5):
            result = rate_limited_chat(client, limiter, f"消息 {i+1}")
            print(f"结果 {i+1}: {result[:50]}...")

