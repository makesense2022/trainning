#!/usr/bin/env python3
"""
进度追踪工具
查看学习进度和完成情况
"""

import os
import sys
from pathlib import Path
from typing import Dict, List
import subprocess


# 添加项目根目录到路径
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


class ProgressTracker:
    """进度追踪器"""
    
    MODULES = {
        "01-python-basics": {
            "name": "Python基础",
            "total": 40,
            "time": "16h"
        },
        "02-python-advanced": {
            "name": "Python进阶",
            "total": 40,
            "time": "16h"
        },
        "03-llm-api": {
            "name": "LLM API",
            "total": 15,
            "time": "5-6h"
        },
        "04-langchain-basics": {
            "name": "LangChain基础",
            "total": 15,
            "time": "5-6h"
        },
        "05-embedding-vectordb": {
            "name": "Embedding和向量库",
            "total": 12,
            "time": "4-5h"
        },
        "06-rag-implementation": {
            "name": "RAG实现",
            "total": 13,
            "time": "5-6h"
        },
        "07-agent-development": {
            "name": "Agent开发",
            "total": 20,
            "time": "8-10h"
        },
        "08-final-projects": {
            "name": "综合项目",
            "total": 3,
            "time": "18-26h"
        }
    }
    
    def __init__(self):
        self.project_root = PROJECT_ROOT
    
    def count_completed_exercises(self, module: str) -> int:
        """统计已完成的练习题数量"""
        exercises_dir = self.project_root / module / "exercises"
        if not exercises_dir.exists():
            return 0
        
        # 统计非空的练习文件
        completed = 0
        for file in exercises_dir.glob("ex*.py"):
            try:
                content = file.read_text()
                # 如果文件有实现（不只是pass），算完成
                if "TODO" not in content or len(content) > 500:
                    completed += 1
            except Exception:
                pass
        
        return completed
    
    def count_passed_tests(self, module: str) -> Dict[str, int]:
        """统计通过的测试数量"""
        tests_dir = self.project_root / module / "tests"
        if not tests_dir.exists():
            return {"passed": 0, "failed": 0, "total": 0}
        
        # 运行pytest
        try:
            result = subprocess.run(
                ["pytest", str(tests_dir), "-v", "--tb=no"],
                capture_output=True,
                text=True,
                cwd=self.project_root
            )
            
            output = result.stdout
            # 解析pytest输出
            if "passed" in output:
                passed = int(output.split("passed")[0].split()[-1])
            else:
                passed = 0
            
            if "failed" in output:
                failed = int(output.split("failed")[0].split()[-1])
            else:
                failed = 0
            
            return {
                "passed": passed,
                "failed": failed,
                "total": passed + failed
            }
        except Exception as e:
            return {"passed": 0, "failed": 0, "total": 0, "error": str(e)}
    
    def print_progress_bar(self, completed: int, total: int, width: int = 30):
        """打印进度条"""
        if total == 0:
            percent = 0
        else:
            percent = completed / total
        
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        percent_str = f"{percent*100:.1f}%"
        
        return f"{bar} {percent_str} ({completed}/{total})"
    
    def show_module_progress(self, module: str):
        """显示单个模块的进度"""
        info = self.MODULES.get(module)
        if not info:
            print(f"❌ 未知模块: {module}")
            return
        
        print(f"\n{'='*70}")
        print(f"📚 {info['name']} ({module})")
        print(f"{'='*70}")
        
        # 练习完成情况
        completed = self.count_completed_exercises(module)
        total = info["total"]
        print(f"\n练习完成: {self.print_progress_bar(completed, total)}")
        
        # 测试通过情况
        test_results = self.count_passed_tests(module)
        if test_results["total"] > 0:
            print(f"测试通过: {self.print_progress_bar(test_results['passed'], test_results['total'])}")
            print(f"  ✅ 通过: {test_results['passed']}")
            print(f"  ❌ 失败: {test_results['failed']}")
        else:
            print(f"测试通过: 尚未运行测试")
        
        # 预计时间
        print(f"\n⏱️  预计时间: {info['time']}")
        
        # 下一步建议
        if completed < total:
            print(f"\n💡 下一步: 完成剩余 {total - completed} 道练习题")
        else:
            print(f"\n🎉 本模块练习已全部完成！")
            if test_results["failed"] > 0:
                print(f"⚠️  但还有 {test_results['failed']} 个测试未通过，继续加油！")
    
    def show_overall_progress(self):
        """显示总体进度"""
        print("\n" + "="*70)
        print(" "*20 + "🚀 AI Agent 训练营进度")
        print("="*70)
        
        total_completed = 0
        total_exercises = 0
        total_passed = 0
        total_tests = 0
        
        for module, info in self.MODULES.items():
            completed = self.count_completed_exercises(module)
            total = info["total"]
            total_completed += completed
            total_exercises += total
            
            # 测试情况
            test_results = self.count_passed_tests(module)
            total_passed += test_results["passed"]
            total_tests += test_results["total"]
            
            # 打印模块进度
            status = "✅" if completed == total else "⏳"
            print(f"\n{status} {info['name']}")
            print(f"   {self.print_progress_bar(completed, total, width=40)}")
            if test_results["total"] > 0:
                print(f"   测试: {test_results['passed']}/{test_results['total']} 通过")
        
        # 总体统计
        print(f"\n{'='*70}")
        print(f"📊 总体进度:")
        print(f"   练习: {self.print_progress_bar(total_completed, total_exercises, width=40)}")
        if total_tests > 0:
            print(f"   测试: {self.print_progress_bar(total_passed, total_tests, width=40)}")
        
        # 里程碑
        print(f"\n🏆 里程碑:")
        milestones = [
            ("Python精通", 80, total_completed >= 80),
            ("LLM调用", 110, total_completed >= 110),
            ("RAG掌握", 135, total_completed >= 135),
            ("Agent开发", 155, total_completed >= 155),
        ]
        
        for name, threshold, achieved in milestones:
            icon = "✅" if achieved else "⏳"
            print(f"   {icon} {name} (需完成{threshold}题)")
        
        # 预估完成时间
        if total_completed < total_exercises:
            remaining = total_exercises - total_completed
            # 假设平均每题30分钟
            hours = remaining * 0.5
            days = hours / 10  # 每天10小时
            print(f"\n⏱️  预估完成时间: {days:.1f}天 (按每天10小时计算)")
        else:
            print(f"\n🎉 恭喜！所有练习已完成！")
            print(f"💼 下一步：完成综合项目，准备面试！")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Agent训练营进度追踪")
    parser.add_argument(
        "--module",
        "-m",
        help="指定模块名（如：01-python-basics）"
    )
    
    args = parser.parse_args()
    
    tracker = ProgressTracker()
    
    if args.module:
        # 显示单个模块进度
        tracker.show_module_progress(args.module)
    else:
        # 显示总体进度
        tracker.show_overall_progress()
    
    print()


if __name__ == "__main__":
    main()

