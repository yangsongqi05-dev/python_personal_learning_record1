"""
Python 个人学习记录 - 入口文件
用于运行各章节的练习代码
"""

def show_progress():
    """显示当前学习进度"""
    chapters = {
        "chap2": "输入输出、注释、代码缩进、ASCII 与 Unicode",
        "chap3": "数据类型、变量与常量、运算符、字符串操作",
        "chap4": "流程控制（条件判断与循环）",
    }

    print("=" * 50)
    print("  Python 学习进度")
    print("=" * 50)
    for chap, desc in chapters.items():
        print(f"  {chap}: {desc}")
    print("=" * 50)
    print(f"  已完成 {len(chapters)} 个章节，持续更新中...")


if __name__ == "__main__":
    show_progress()
