"""
练习 25: 包结构
难度: 🟡 进阶
预计时间: 20分钟

目标：理解Python包的结构
"""

# 包结构示例：
# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#     __init__.py
#     module3.py


def explain_package_structure() -> dict:
    """
    解释包结构
    
    返回:
        包结构说明
    """
    return {
        "structure": """
mypackage/
  __init__.py          # 包初始化
  module1.py           # 模块1
  module2.py           # 模块2
  subpackage/          # 子包
    __init__.py
    module3.py
        """,
        "import_examples": {
            "import_package": "import mypackage",
            "import_module": "from mypackage import module1",
            "import_from_subpackage": "from mypackage.subpackage import module3"
        }
    }


if __name__ == "__main__":
    print(explain_package_structure())

