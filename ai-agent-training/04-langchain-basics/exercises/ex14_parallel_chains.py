"""
练习 14: 并行Chain
难度: 🔴 挑战
预计时间: 30分钟

目标：并行执行多个Chain
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


def create_parallel_chains() -> list:
    """
    创建多个Chain
    
    返回:
        Chain列表
    """
    # TODO: 创建多个Chain
    if not os.getenv("OPENAI_API_KEY"):
        return []
    
    llm = ChatOpenAI()
    
    chain1 = LLMChain(
        llm=llm,
        prompt=PromptTemplate(input_variables=["topic"], template="解释：{topic}")
    )
    
    chain2 = LLMChain(
        llm=llm,
        prompt=PromptTemplate(input_variables=["topic"], template="总结：{topic}")
    )
    
    return [chain1, chain2]


async def run_parallel_chains(chains: list, topic: str) -> list:
    """
    并行运行多个Chain
    
    参数:
        chains: Chain列表
        topic: 主题
    
    返回:
        结果列表
    """
    # TODO: 使用asyncio.gather并行执行
    async def run_chain(chain):
        # 注意：需要异步版本的chain
        return chain.run(topic)
    
    tasks = [run_chain(chain) for chain in chains]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chains = create_parallel_chains()
        if chains:
            results = asyncio.run(run_parallel_chains(chains, "Python"))
            print(results)

