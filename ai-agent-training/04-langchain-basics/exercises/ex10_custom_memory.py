"""
练习 10: 自定义Memory
难度: 🔴 挑战
预计时间: 30分钟

目标：创建自定义的Memory类
"""

from langchain.memory import BaseMemory
from typing import Dict, Any, List
from langchain.schema import BaseMessage


class SimpleMemory(BaseMemory):
    """简单的自定义Memory"""
    
    def __init__(self):
        super().__init__()
        self.messages: List[BaseMessage] = []
    
    @property
    def memory_variables(self) -> List[str]:
        """返回内存变量名"""
        return ["chat_history"]
    
    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """加载内存变量"""
        # TODO: 返回内存内容
        return {"chat_history": self.messages}
    
    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]):
        """保存上下文"""
        # TODO: 保存输入和输出到内存
        from langchain.schema import HumanMessage, AIMessage
        
        if "input" in inputs:
            self.messages.append(HumanMessage(content=inputs["input"]))
        if "output" in outputs:
            self.messages.append(AIMessage(content=outputs["output"]))
    
    def clear(self):
        """清空内存"""
        self.messages = []


if __name__ == "__main__":
    memory = SimpleMemory()
    memory.save_context({"input": "Hello"}, {"output": "Hi there"})
    variables = memory.load_memory_variables({})
    print(variables)

