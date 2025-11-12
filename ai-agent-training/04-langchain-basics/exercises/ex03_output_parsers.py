"""
练习 03: 输出解析器
难度: 🟡 进阶
预计时间: 20分钟

目标：解析LLM的结构化输出
"""

from langchain.output_parsers import PydanticOutputParser, CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()


class Person(BaseModel):
    """人员信息模型"""
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")
    city: str = Field(description="城市")


def create_pydantic_parser() -> PydanticOutputParser:
    """
    创建Pydantic输出解析器
    
    返回:
        PydanticOutputParser实例
    """
    # TODO: 创建解析器
    return PydanticOutputParser(pydantic_object=Person)


def create_list_parser() -> CommaSeparatedListOutputParser:
    """
    创建列表输出解析器
    
    返回:
        CommaSeparatedListOutputParser实例
    """
    # TODO: 创建列表解析器
    return CommaSeparatedListOutputParser()


def parse_with_pydantic(llm: ChatOpenAI, query: str) -> Person:
    """
    使用Pydantic解析输出
    
    参数:
        llm: Chat Model
        query: 查询（如"提取：Alice, 25, Beijing"）
    
    返回:
        Person对象
    """
    # TODO: 创建Prompt，包含解析器指令，调用LLM，解析结果
    parser = create_pydantic_parser()
    
    prompt = PromptTemplate(
        template="提取以下信息为JSON格式：\n{query}\n{format_instructions}",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    if not os.getenv("OPENAI_API_KEY"):
        # 模拟返回
        return Person(name="Alice", age=25, city="Beijing")
    
    chain = prompt | llm | parser
    result = chain.invoke({"query": query})
    return result


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        llm = ChatOpenAI()
        person = parse_with_pydantic(llm, "提取：Alice, 25, Beijing")
        print(f"姓名: {person.name}, 年龄: {person.age}, 城市: {person.city}")

