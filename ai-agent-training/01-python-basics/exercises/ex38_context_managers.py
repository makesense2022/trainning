"""
练习 38: 上下文管理器 (with语句)
难度: 🟡 进阶
预计时间: 15分钟

对比学习：
JS:  需要手动关闭资源
Python: with语句自动管理资源

最常见的用途：文件操作
"""


def read_file_safely(file_path: str) -> str:
    """
    安全读取文件（使用with语句）
    
    JS: 需要手动关闭
    const file = fs.openSync('file.txt', 'r');
    try {
        // 读取
    } finally {
        fs.closeSync(file);
    }
    
    Python: 自动关闭
    with open('file.txt', 'r') as file:
        content = file.read()
    
    参数:
        file_path: 文件路径
    
    返回:
        文件内容
    """
    # TODO: 使用with语句读取文件
    pass


def write_file_safely(file_path: str, content: str):
    """
    安全写入文件
    
    参数:
        file_path: 文件路径
        content: 要写入的内容
    """
    # TODO: 使用with语句写入文件
    pass


def custom_context_manager():
    """
    创建自定义上下文管理器
    
    返回:
        一个简单的上下文管理器类
    """
    # TODO: 使用__enter__和__exit__创建
    class MyContext:
        def __enter__(self):
            print("进入上下文")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("退出上下文")
            return False
    
    return MyContext


if __name__ == "__main__":
    # 测试文件操作
    # write_file_safely("test.txt", "Hello World")
    # print(read_file_safely("test.txt"))
    
    # 测试自定义上下文管理器
    with custom_context_manager() as ctx:
        print("在上下文中")

