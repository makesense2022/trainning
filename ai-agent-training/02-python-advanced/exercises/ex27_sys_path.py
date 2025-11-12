"""
练习 27: sys.path操作
难度: 🟡 进阶
预计时间: 15分钟

目标：理解sys.path和模块搜索路径
"""

import sys
from pathlib import Path


def show_sys_path() -> list:
    """
    显示sys.path（模块搜索路径）
    
    返回:
        路径列表
    """
    # TODO: 返回sys.path
    return list(sys.path)


def add_to_path(directory: str):
    """
    添加目录到sys.path
    
    参数:
        directory: 目录路径
    """
    # TODO: 添加到sys.path
    if directory not in sys.path:
        sys.path.insert(0, directory)


if __name__ == "__main__":
    print("当前sys.path:")
    for path in show_sys_path():
        print(f"  {path}")

