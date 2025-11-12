"""
练习 12: 流式Chain
难度: 🔴 挑战
预计时间: 30分钟

目标：实现流式输出的Chain
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_streaming_chain():
    """
    创建流式Chain
    
    返回:
        LLMChain实例（配置为流式）
    """
    # TODO: 创建Chain，设置streaming=True
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI(streaming=True)
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="详细解释：{topic}"
    )
    return LLMChain(llm=llm, prompt=prompt)


def stream_chain_output(chain, topic: str):
    """
    流式输出Chain结果
    
    参数:
        chain: LLMChain
        topic: 主题
    """
    # TODO: 使用stream()方法
    if chain is None:
        print("请设置API Key")
        return
    
    for chunk in chain.stream({"topic": topic}):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_streaming_chain()
        if chain:
            stream_chain_output(chain, "Python装饰器")

