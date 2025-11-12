# Module 02: Python进阶

> 目标：掌握Python高级特性，为AI开发打下坚实基础

## 🎯 学习目标

- [ ] 掌握异步编程（async/await）
- [ ] 理解面向对象编程
- [ ] 熟悉模块和包管理
- [ ] 掌握常用标准库

## 📊 练习列表（40题）

### Part 1: 异步编程 (10题)
- ex01_async_basics.py - async/await基础
- ex02_asyncio.py - asyncio事件循环
- ex03_concurrent_requests.py - 并发HTTP请求
- ex04_async_comprehension.py - 异步推导式
- ex05_async_context.py - 异步上下文管理器
- ex06_async_generators.py - 异步生成器
- ex07_gather_vs_wait.py - gather和wait
- ex08_async_errors.py - 异步错误处理
- ex09_async_queue.py - 异步队列
- ex10_sync_vs_async.py - 同步异步性能对比

### Part 2: 面向对象 (10题)
- ex11_class_basics.py - 类定义
- ex12_init_self.py - __init__和self
- ex13_properties.py - @property装饰器
- ex14_magic_methods.py - 魔术方法
- ex15_inheritance.py - 继承
- ex16_multiple_inheritance.py - 多继承和MRO
- ex17_abstract_classes.py - 抽象类
- ex18_dataclasses.py - @dataclass
- ex19_class_vs_static.py - 类方法vs静态方法
- ex20_dunder_methods.py - 完整的魔术方法

### Part 3: 模块和包 (10题)
- ex21_imports.py - import机制
- ex22_from_import.py - from...import
- ex23_relative_imports.py - 相对导入
- ex24_init_py.py - __init__.py
- ex25_packages.py - 包结构
- ex26_namespace.py - 命名空间
- ex27_sys_path.py - sys.path操作
- ex28_importlib.py - 动态导入
- ex29_circular_imports.py - 循环导入
- ex30_module_reload.py - 模块重载

### Part 4: 常用库 (10题)
- ex31_pathlib.py - 路径操作
- ex32_json.py - JSON处理
- ex33_datetime.py - 日期时间
- ex34_re.py - 正则表达式
- ex35_collections.py - collections模块
- ex36_itertools.py - itertools技巧
- ex37_requests.py - HTTP请求
- ex38_pydantic.py - 数据验证
- ex39_logging.py - 日志系统
- ex40_dotenv.py - 环境变量管理

## 🔥 核心概念

### 异步编程（对前端很重要！）

```python
# Python的async/await和JS几乎一样！
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

### 面向对象

```python
# Python的类和JS的类很相似
class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"
```

## ⏭️ 下一步

完成本模块后，您将掌握Python的高级特性，可以开始AI开发了！

