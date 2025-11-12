"""
练习 20: 完整的魔术方法
难度: 🔴 挑战
预计时间: 30分钟

目标：实现常用的魔术方法
"""


class Book:
    """图书类（演示多种魔术方法）"""
    
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"{self.title} by {self.author}"
    
    def __repr__(self) -> str:
        """对象表示"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self) -> int:
        """长度（页数）"""
        return self.pages
    
    def __eq__(self, other: 'Book') -> bool:
        """相等比较"""
        # TODO: 实现相等比较
        return (self.title == other.title and 
                self.author == other.author and 
                self.pages == other.pages)
    
    def __lt__(self, other: 'Book') -> bool:
        """小于比较（按页数）"""
        # TODO: 实现小于比较
        return self.pages < other.pages
    
    def __hash__(self) -> int:
        """哈希值（用于set和dict的key）"""
        # TODO: 实现哈希
        return hash((self.title, self.author))
    
    def __call__(self) -> str:
        """可调用对象"""
        return f"正在阅读《{self.title}》..."


if __name__ == "__main__":
    book1 = Book("Python编程", "作者A", 300)
    book2 = Book("Python编程", "作者A", 300)
    book3 = Book("JavaScript指南", "作者B", 200)
    
    print(book1)  # 使用__str__
    print(book1 == book2)  # True
    print(book1 < book3)  # False (300 > 200)
    print(book1())  # 调用对象

