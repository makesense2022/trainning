"""
练习 23: 相对导入
难度: 🟡 进阶
预计时间: 15分钟

目标：理解相对导入的用法
"""

# 相对导入示例
# from .module import function  # 同目录
# from ..parent import function  # 父目录
# from ...grandparent import function  # 祖父目录


def explain_relative_imports() -> dict:
    """
    解释相对导入
    
    返回:
        说明字典
    """
    return {
        "same_dir": "from .module import func  # 同目录",
        "parent_dir": "from ..parent import func  # 父目录",
        "sibling_dir": "from ..sibling import func  # 兄弟目录",
        "note": "只能在包内使用，不能在脚本中直接使用"
    }


if __name__ == "__main__":
    print(explain_relative_imports())

