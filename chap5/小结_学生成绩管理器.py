# -*- coding: utf-8 -*-
"""
chap5 综合练习：学生成绩管理器

综合运用列表、字典、函数，实现一个简单的成绩管理工具。
这是本章的实践小结，用到的知识点：
    - 列表的增删改查、遍历
    - 字典的创建、取值、遍历
    - 函数的定义、参数、返回值
    - 列表推导式、sorted 排序
    - lambda 表达式

运行方式：python 小结_学生成绩管理器.py
"""


# ============ 数据 ============
students = []


# ============ 功能函数 ============
def add_student(name, score):
    """添加一个学生记录"""
    students.append({"name": name, "score": score})


def find_student(name):
    """按姓名查找学生，找不到返回 None"""
    for s in students:
        if s["name"] == name:
            return s
    return None


def remove_student(name):
    """按姓名删除学生，返回是否删除成功"""
    s = find_student(name)
    if s is None:
        return False
    students.remove(s)
    return True


def get_average():
    """计算平均分，没有数据时返回 0"""
    if not students:
        return 0
    return sum(s["score"] for s in students) / len(students)


def get_max():
    """返回分数最高的学生"""
    if not students:
        return None
    return max(students, key=lambda s: s["score"])


def get_min():
    """返回分数最低的学生"""
    if not students:
        return None
    return min(students, key=lambda s: s["score"])


def sort_by_score(reverse=True):
    """按分数排序，默认从高到低"""
    return sorted(students, key=lambda s: s["score"], reverse=reverse)


def get_level(score):
    """根据分数返回等级"""
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def print_report():
    """打印成绩报告"""
    if not students:
        print("暂无学生数据")
        return

    print("=" * 40)
    print("成绩报告")
    print("=" * 40)

    for i, s in enumerate(sort_by_score(), 1):
        level = get_level(s["score"])
        print(f"{i}. {s['name']:<6} {s['score']:>5} 分    {level}")

    print("-" * 40)
    print(f"人数   : {len(students)}")
    print(f"平均分 : {get_average():.1f}")
    print(f"最高分 : {get_max()['name']} ({get_max()['score']})")
    print(f"最低分 : {get_min()['name']} ({get_min()['score']})")

    # 用列表推导式统计不及格人数
    failed = [s for s in students if s["score"] < 60]
    print(f"不及格 : {len(failed)} 人")
    print("=" * 40)


def save_to_file(filename="report.txt"):
    """把报告写入文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for s in sort_by_score():
                f.write(f"{s['name']},{s['score']},{get_level(s['score'])}\n")
        print(f"报告已保存到 {filename}")
    except IOError as e:
        print(f"保存失败：{e}")


# ============ 主程序 ============
def main():
    # 添加测试数据
    data = [
        ("张三", 88),
        ("李四", 92),
        ("王五", 75),
        ("赵六", 58),
        ("钱七", 95),
    ]
    for name, score in data:
        add_student(name, score)

    # 打印报告
    print_report()

    # 查找测试
    print("\n查找「张三」：", find_student("张三"))
    print("查找「孙悟空」：", find_student("孙悟空"))

    # 删除测试
    print("\n删除「赵六」：", "成功" if remove_student("赵六") else "失败")
    print("删除后人数：", len(students))

    # 保存文件
    print()
    save_to_file()


if __name__ == "__main__":
    main()
