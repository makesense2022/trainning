"""
练习 13: 降级Chain
难度: 🔴 挑战
预计时间: 30分钟

目标：实现Chain的降级策略
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_fallback_chain():
    """
    创建带降级的Chain
    
    返回:
        Chain实例（主链失败时使用备用链）
    """
    # TODO: 创建主链和备用链
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    # 主链（使用GPT-4）
    primary_llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    # 备用链（使用GPT-3.5）
    fallback_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    prompt = PromptTemplate(
        input_variables=["query"],
        template="回答：{query}"
    )
    
    # 尝试主链，失败时使用备用链
    try:
        return LLMChain(llm=primary_llm, prompt=prompt)
    except:
        return LLMChain(llm=fallback_llm, prompt=prompt)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_fallback_chain()
        if chain:
            result = chain.run("什么是Python？")
            print(result)

