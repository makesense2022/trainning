"""
练习 32: JSON处理
难度: 🟢 基础
预计时间: 15分钟

目标：使用json模块处理JSON数据
"""

import json
from typing import Any, Dict, List


def load_json_string(json_str: str) -> Dict[str, Any]:
    """
    解析JSON字符串
    
    参数:
        json_str: JSON字符串
    
    返回:
        字典对象
    """
    # TODO: 使用json.loads()
    return json.loads(json_str)


def dump_to_json_string(data: Dict) -> str:
    """
    将字典转换为JSON字符串
    
    参数:
        data: 字典
    
    返回:
        JSON字符串
    """
    # TODO: 使用json.dumps()
    return json.dumps(data, ensure_ascii=False, indent=2)


def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    从文件加载JSON
    
    参数:
        file_path: 文件路径
    
    返回:
        字典对象
    """
    # TODO: 使用json.load()
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json_file(data: Dict, file_path: str):
    """
    保存JSON到文件
    
    参数:
        data: 字典
        file_path: 文件路径
    """
    # TODO: 使用json.dump()
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # 测试JSON字符串
    json_str = '{"name": "Alice", "age": 25}'
    data = load_json_string(json_str)
    print(data)
    
    # 测试转换回JSON
    new_json = dump_to_json_string(data)
    print(new_json)

