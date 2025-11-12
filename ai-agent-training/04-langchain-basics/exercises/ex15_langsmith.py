"""
练习 15: LangSmith追踪
难度: 🟡 进阶
预计时间: 20分钟

目标：使用LangSmith追踪和调试LangChain应用
"""

import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def setup_langsmith():
    """
    设置LangSmith追踪
    
    返回:
        是否成功设置
    """
    # TODO: 设置环境变量启用LangSmith
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "ai-agent-training"
    
    if os.getenv("LANGCHAIN_API_KEY"):
        return True
    return False


def create_traced_chain():
    """
    创建会被LangSmith追踪的Chain
    
    返回:
        LLMChain实例
    """
    # TODO: 创建Chain（会自动被追踪）
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = PromptTemplate(
        input_variables=["query"],
        template="回答：{query}"
    )
    return LLMChain(llm=llm, prompt=prompt)


if __name__ == "__main__":
    if setup_langsmith():
        chain = create_traced_chain()
        if chain:
            result = chain.run("测试追踪")
            print(result)
            print("查看LangSmith平台查看追踪信息")

