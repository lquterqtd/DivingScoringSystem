__author__ = 'Administrator'
#coding:utf-8
def calculate_score(calculation_params):
    """
    计算选手在一跳中的得分，共7名裁判，去掉两个最高分和两个最低分，余下3名裁判员的分数之和乘以运动员所跳动作的难度系数，便得出该动作的实得分
    传入参数为字典
    calculation_params["score_list"] = []
    calculation_params["difficulty"] = float
    """
    score_list = calculation_params["score_list"]
    difficulty = calculation_params["difficulty"]
    score_list.sort()
    temp_sum = 0.0
    res = {}
    res['expression'] = '('
    for i in score_list[2:5]:
        temp_sum += i
        res['expression'] += "%.1f + " % i
    res['final_score'] = temp_sum * difficulty
    res['expression'] = res['expression'][:-3]
    res['expression'] += ') * %.1f = %.1f' % (difficulty, res['final_score'])
    return res


if __name__ == "__main__":
    calculation_params = {
        "score_list" : [1.0, 5.0, 3.0, 2.0, 9.0, 10.0, 2.0],
        "difficulty" : 3.6,
    }

    print calculate_score(calculation_params)