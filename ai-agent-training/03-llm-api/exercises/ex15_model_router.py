"""
练习 15: 多模型切换
难度: 🔴 挑战
预计时间: 30分钟

目标：根据任务自动选择最合适的模型
"""

from openai import OpenAI
from typing import Literal
import os
from dotenv import load_dotenv

load_dotenv()


class ModelRouter:
    """模型路由器"""
    
    def __init__(self, client: OpenAI):
        self.client = client
        self.models = {
            "simple": "gpt-3.5-turbo",      # 简单任务
            "complex": "gpt-4",              # 复杂任务
            "fast": "gpt-3.5-turbo",         # 快速响应
        }
    
    def select_model(self, task_type: str, complexity: str = "simple") -> str:
        """
        选择模型
        
        参数:
            task_type: 任务类型
            complexity: 复杂度
        
        返回:
            模型名称
        """
        # TODO: 根据任务类型和复杂度选择模型
        if complexity == "complex":
            return self.models["complex"]
        return self.models["simple"]
    
    def chat(self, message: str, task_type: str = "general", complexity: str = "simple") -> str:
        """
        智能路由聊天
        
        参数:
            message: 消息
            task_type: 任务类型
            complexity: 复杂度
        
        返回:
            AI回复
        """
        # TODO: 选择模型并调用
        model = self.select_model(task_type, complexity)
        
        if not os.getenv("OPENAI_API_KEY"):
            return f"请设置API Key（将使用模型: {model}）"
        
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        router = ModelRouter(client)
        
        # 简单任务
        result1 = router.chat("什么是Python？", complexity="simple")
        print(f"简单任务: {result1[:50]}...")
        
        # 复杂任务
        result2 = router.chat("详细解释Transformer架构", complexity="complex")
        print(f"复杂任务: {result2[:50]}...")

