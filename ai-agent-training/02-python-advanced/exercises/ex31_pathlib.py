"""
练习 31: pathlib路径操作
难度: 🟢 基础
预计时间: 15分钟

目标：使用pathlib进行路径操作（比os.path更现代）
"""

from pathlib import Path


def get_current_dir() -> Path:
    """
    获取当前目录
    
    返回:
        Path对象
    """
    # TODO: 使用Path.cwd()
    return Path.cwd()


def join_paths(base: str, *parts: str) -> Path:
    """
    拼接路径
    
    参数:
        base: 基础路径
        *parts: 路径部分
    
    返回:
        Path对象
    
    示例:
        join_paths("/home", "user", "documents") -> Path("/home/user/documents")
    """
    # TODO: 使用Path和/操作符
    return Path(base) / Path(*parts)


def check_file_exists(file_path: str) -> dict:
    """
    检查文件是否存在及信息
    
    参数:
        file_path: 文件路径
    
    返回:
        {
            "exists": bool,
            "is_file": bool,
            "is_dir": bool,
            "size": int (如果存在)
        }
    """
    # TODO: 使用Path的方法
    path = Path(file_path)
    result = {
        "exists": path.exists(),
        "is_file": path.is_file(),
        "is_dir": path.is_dir(),
    }
    if path.exists() and path.is_file():
        result["size"] = path.stat().st_size
    return result


def list_files(directory: str, pattern: str = "*") -> list:
    """
    列出目录中的文件
    
    参数:
        directory: 目录路径
        pattern: 文件模式（如"*.py"）
    
    返回:
        文件路径列表
    """
    # TODO: 使用Path.glob()
    path = Path(directory)
    return list(path.glob(pattern))


if __name__ == "__main__":
    print(get_current_dir())
    print(join_paths("/home", "user", "documents"))
    print(check_file_exists(__file__))
    print(list_files(".", "*.py")[:5])  # 前5个

