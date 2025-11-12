"""
练习 11: 错误处理
难度: 🟡 进阶
预计时间: 20分钟

目标：处理LLM API调用中的各种错误
"""

from openai import OpenAI, APIError, RateLimitError, APIConnectionError
import os
from dotenv import load_dotenv
import time

load_dotenv()


def safe_chat_completion(client: OpenAI, messages: list) -> dict:
    """
    安全的聊天完成调用（带错误处理）
    
    参数:
        client: OpenAI客户端
        messages: 消息列表
    
    返回:
        {
            "success": bool,
            "result": str or None,
            "error": str or None
        }
    """
    # TODO: 实现错误处理
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return {
            "success": True,
            "result": response.choices[0].message.content,
            "error": None
        }
    except RateLimitError as e:
        return {
            "success": False,
            "result": None,
            "error": f"速率限制: {e}"
        }
    except APIConnectionError as e:
        return {
            "success": False,
            "result": None,
            "error": f"连接错误: {e}"
        }
    except APIError as e:
        return {
            "success": False,
            "result": None,
            "error": f"API错误: {e}"
        }
    except Exception as e:
        return {
            "success": False,
            "result": None,
            "error": f"未知错误: {e}"
        }


def retry_on_error(client: OpenAI, messages: list, max_retries: int = 3) -> str:
    """
    错误时重试
    
    参数:
        client: OpenAI客户端
        messages: 消息列表
        max_retries: 最大重试次数
    
    返回:
        AI回复
    """
    # TODO: 实现重试逻辑
    for attempt in range(max_retries):
        result = safe_chat_completion(client, messages)
        if result["success"]:
            return result["result"]
        
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt  # 指数退避
            print(f"重试 {attempt + 1}/{max_retries}，等待{wait_time}秒...")
            time.sleep(wait_time)
        else:
            raise Exception(f"重试失败: {result['error']}")


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        messages = [{"role": "user", "content": "Hello"}]
        result = safe_chat_completion(client, messages)
        print(result)

