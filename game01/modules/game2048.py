"""
 功能：Game2048类
 作者：指尖魔法师
 QQ：14555110
"""

import pygame
import random
import copy
class Game2048(object):
    def __init__(self, matrix_size=(4, 4), max_score_filepath=None):
        self.matrix_size = matrix_size
        # 游戏最高分保存路径
        self.max_score_filepath = max_score_filepath

        self.initialize()

    def initialize(self):
        """初始化"""
        self.game_matrix = [['null' for _ in range(self.matrix_size[1])] for _ in range(self.matrix_size[0])]

        # 读取最高分
        self.score = 0
        self.max_score = self.readMaxScore()

        # 初始化时随机2位数值
        self.randomGenerateNumber()
        self.randomGenerateNumber()
        # 当前所有位置的数值
        print(self.game_matrix)

        self.move_direction = None

    def update(self):
        """更新游戏状态"""
        self.game_matrix_before = copy.deepcopy(self.game_matrix)
        self.move()
        if self.game_matrix != self.game_matrix_before:
            # 方块变化后，随机一个新的数字
            self.randomGenerateNumber()

        # 游戏分数大于最高分，更新最高分
        if self.score > self.max_score:
            self.max_score = self.score

    def randomGenerateNumber(self):
        """在空白位置产生随机数 2 或者 4"""
        empty_pos = []
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j] == 'null':
                    empty_pos.append([i, j])
        # 空白位置列表
        # print(empty_pos)

        # 随机位置生成
        i, j = random.choice(empty_pos)

        # 随机数生成
        self.game_matrix[i][j] = 2 if random.random() > 0.1 else 4

        print('随机数位置为[{0}][{1}] = 数值{2}'.format(i, j, self.game_matrix[i][j]))

    def readMaxScore(self):
        """读取文件中的最高分"""
        try:
            f = open(self.max_score_filepath, 'r', encoding='utf-8')
            score = int(f.read().strip())
            f.close()
            return score
        except:
            return 0

    def setDirection(self, direction):
        assert direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.move_direction = direction
        print(self.move_direction)

    def move(self):

        # 提取非空数值
        def extract(array):
            new_array = []
            for arr in array:
                if arr != 'null':
                    new_array.append(arr)
            return new_array

        # 合并非空数字
        def merge(array):
            score = 0
            if len(array) < 2:
                return array, score
            for i in range(len(array)-1):
                if array[i] == 'null':
                    break
                if array[i] == array[i+1]:
                    array[i] += array[i+1]
                    score += array[i]
                    array.pop(i+1)
                    array.append('null')
            return extract(array), score

        # 不需要移动的话直接返回
        if self.move_direction is None:
            return

        if self.move_direction == 'UP':
            # print("向上移动一次")
            for j in range(self.matrix_size[1]):
                # 获取该列数据
                col = []
                for i in range(self.matrix_size[0]):
                    col.append(self.game_matrix[i][j])

                # 提取非空数值
                new_col = extract(col)

                # 合并非空数字
                new_col, score = merge(new_col)
                self.score += score

                # 补全列表null
                new_col.extend('null' for _ in range(self.matrix_size[0] - len(new_col)))

                # 从上往下更新该列数据
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = new_col[i]
                # print(self.game_matrix)

        elif self.move_direction == 'DOWN':
            # print("向下移动一次")
            for j in range(self.matrix_size[1]):
                # 获取该列数据
                col = []
                for i in range(self.matrix_size[0]):
                    col.append(self.game_matrix[i][j])

                # 翻转列表
                col.reverse()

                # 提取非空数值
                new_col = extract(col)

                # 合并非空数字
                new_col, score = merge(new_col)
                self.score += score

                # 补全列表null
                new_col.extend('null' for _ in range(self.matrix_size[0] - len(new_col)))

                # 翻转列
                new_col.reverse()

                # 从上往下更新该列数据
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = new_col[i]
                # print(self.game_matrix)

        elif self.move_direction == 'LEFT':
            # print("向左移动一次")
            for i in range(self.matrix_size[0]):
                # 获取该和行数据
                row = []
                for j in range(self.matrix_size[1]):
                    row.append(self.game_matrix[i][j])

                # 提取非空数值
                new_row = extract(row)

                # 合并非空数字
                new_row, score = merge(new_row)
                self.score += score

                # 补全列表null
                new_row.extend('null' for _ in range(self.matrix_size[1] - len(new_row)))

                # 从左往右更新该该行数据
                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = new_row[j]
                # print(self.game_matrix)

        elif self.move_direction == 'RIGHT':
            # print("向右移动一次")
            for i in range(self.matrix_size[0]):
                # 获取该和行数据
                row = []
                for j in range(self.matrix_size[1]):
                    row.append(self.game_matrix[i][j])

                # 翻转行列表
                row.reverse()
                # 提取非空数值
                new_row = extract(row)

                # 合并非空数字
                new_row, score = merge(new_row)
                self.score += score

                # 补全列表null
                new_row.extend('null' for _ in range(self.matrix_size[1] - len(new_row)))

                # 翻转行列表
                new_row.reverse()

                # 从左往右更新该该行数据
                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = new_row[j]

                # print(self.game_matrix)

        # 状态置空
        self.move_direction = None

    def saveMaxScore(self):
        """保存最高分"""
        f = open(self.max_score_filepath, 'w', encoding='utf-8')
        f.write(str(self.max_score))
        f.close()

    @property
    def isGameOver(self):
        """判断游戏是否结束"""
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j] == 'null':
                    return False
                elif (j + 1 <= self.matrix_size[1] - 1) and (self.game_matrix[i][j] == self.game_matrix[i][j+1]):
                    return False
                elif (i + 1 <= self.matrix_size[0] - 1) and (self.game_matrix[i][j] == self.game_matrix[i+1][j]):
                    return False
        return True


if __name__ == "__main__":
    game_2048 = Game2048(matrix_size=(4, 4), max_score_filepath='../score')