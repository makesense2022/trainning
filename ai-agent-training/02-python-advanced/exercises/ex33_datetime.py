"""
练习 33: 日期时间
难度: 🟡 进阶
预计时间: 15分钟

目标：使用datetime模块处理日期和时间
"""

from datetime import datetime, timedelta, date


def get_current_datetime() -> datetime:
    """
    获取当前日期时间
    
    返回:
        datetime对象
    """
    # TODO: 使用datetime.now()
    return datetime.now()


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    格式化日期时间
    
    参数:
        dt: datetime对象
        format_str: 格式字符串
    
    返回:
        格式化后的字符串
    """
    # TODO: 使用strftime()
    return dt.strftime(format_str)


def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d") -> datetime:
    """
    解析日期字符串
    
    参数:
        date_str: 日期字符串
        format_str: 格式字符串
    
    返回:
        datetime对象
    """
    # TODO: 使用strptime()
    return datetime.strptime(date_str, format_str)


def add_days(dt: datetime, days: int) -> datetime:
    """
    日期加减
    
    参数:
        dt: datetime对象
        days: 天数（可以是负数）
    
    返回:
        新的datetime对象
    """
    # TODO: 使用timedelta()
    return dt + timedelta(days=days)


def calculate_age(birth_date: date) -> int:
    """
    计算年龄
    
    参数:
        birth_date: 出生日期
    
    返回:
        年龄
    """
    # TODO: 计算年龄
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


if __name__ == "__main__":
    now = get_current_datetime()
    print(format_datetime(now))
    
    future = add_days(now, 7)
    print(f"7天后: {format_datetime(future)}")
    
    birth = date(1990, 1, 1)
    print(f"年龄: {calculate_age(birth)}")

