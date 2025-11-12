"""
练习 05: 多轮对话
难度: 🟡 进阶
预计时间: 20分钟

目标：实现多轮对话，保持上下文
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class Conversation:
    """对话管理器"""
    
    def __init__(self, client: OpenAI):
        self.client = client
        self.messages = []
    
    def add_message(self, role: str, content: str):
        """
        添加消息到对话历史
        
        参数:
            role: "user" 或 "assistant"
            content: 消息内容
        """
        # TODO: 添加消息到self.messages
        self.messages.append({"role": role, "content": content})
    
    def chat(self, user_message: str) -> str:
        """
        发送用户消息并获取回复
        
        参数:
            user_message: 用户消息
        
        返回:
            AI回复
        """
        # TODO: 添加用户消息，调用API，添加AI回复
        self.add_message("user", user_message)
        
        if not os.getenv("OPENAI_API_KEY"):
            return "请设置API Key"
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        
        assistant_message = response.choices[0].message.content
        self.add_message("assistant", assistant_message)
        
        return assistant_message
    
    def get_history(self) -> list:
        """获取对话历史"""
        return self.messages.copy()


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        conv = Conversation(client)
        
        print(conv.chat("我的名字是Alice"))
        print(conv.chat("我的名字是什么？"))  # 应该能记住
        print("\n对话历史:")
        for msg in conv.get_history():
            print(f"{msg['role']}: {msg['content']}")

