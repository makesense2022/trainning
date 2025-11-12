"""
练习 26: 命名空间
难度: 🟡 进阶
预计时间: 15分钟

目标：理解Python的命名空间
"""


def demonstrate_namespace():
    """
    演示命名空间
    
    返回:
        命名空间信息
    """
    # TODO: 演示局部、全局、内置命名空间
    global_var = "全局变量"
    
    def inner_function():
        local_var = "局部变量"
        return {
            "local": local_var,
            "global": global_var,
            "builtin": len([1, 2, 3])  # 使用内置函数
        }
    
    return inner_function()


if __name__ == "__main__":
    result = demonstrate_namespace()
    print(result)

