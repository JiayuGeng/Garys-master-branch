# 贪心算法
# 给出项目开始时间和结束时间，尽可能多的安排会议室
def Best_Arrange(program_list, start):
    # 结束最早的项目排在前面
    program_list.sort(key=lambda x: x[1])
    result = 0
    for i in range(len(program_list)):
        # 大于开始时间，项目才能开始
        if program_list[i][0] > start:
            result += 1
            # 下一个项目开始时间=上一个项目结束时间
            start = program_list[i][1]

    return result


if __name__ == '__main__':
    print(Best_Arrange([[1,3],[4,5],[2,4],[6,8]], 1))
