"""
练习 02: 文档切分策略
难度: 🟡 进阶
预计时间: 25分钟

关键概念：
- chunk_size: 每块大小
- chunk_overlap: 重叠大小
- separators: 分隔符优先级
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text_basic(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list:
    """
    基础文本切分
    
    参数:
        text: 长文本
        chunk_size: 每块大小（字符数）
        chunk_overlap: 重叠大小
    
    返回:
        文本块列表
    """
    # TODO: 使用RecursiveCharacterTextSplitter
    pass


def split_with_custom_separators(text: str) -> list:
    """
    使用自定义分隔符切分
    
    参数:
        text: 文本
    
    返回:
        切分后的块列表
    """
    # TODO: 自定义separators参数
    pass


def analyze_chunk_quality(chunks: list) -> dict:
    """
    分析切分质量
    
    返回:
        {
            "num_chunks": 块数量,
            "avg_length": 平均长度,
            "min_length": 最小长度,
            "max_length": 最大长度
        }
    """
    # TODO: 分析切分结果
    pass


if __name__ == "__main__":
    long_text = "这是一个很长的文档..." * 100
    chunks = split_text_basic(long_text)
    print(analyze_chunk_quality(chunks))

