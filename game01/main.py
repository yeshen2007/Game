"""
 功能：2048小游戏
 作者：指尖魔法师
 QQ：14555110
"""

import pygame
from sys import exit
from modules.game2048 import *
from modules.utils import *
import cfg
from modules.endInterface import *


def main(cfg):
    # 初始化pygame
    pygame.init()

    pygame.mixer.music.load(cfg.BGMPATH)
    pygame.mixer.music.play(-1)

    # 创建一个窗口
    screen = pygame.display.set_mode(cfg.SCREENSIZE, 0, 32)

    # 设置窗口标题
    pygame.display.set_caption("2048小游戏--作者：指尖魔法师 QQ:14555110")

    # 实例化Game2048
    game_2048 = Game2048(matrix_size=cfg.GAME_MATRIX_SIZE, max_score_filepath=cfg.MAX_SCORE_FILEPATH)

    # 游戏主循环
    is_running = True
    while is_running:
        # 填充背景颜色
        screen.fill(pygame.Color(cfg.BG_COLOR))

        # 按键检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接受到退出事件后退出
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    game_2048.setDirection({pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN', pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'}[event.key])

        # 更新游戏状态
        game_2048.update()
        if game_2048.isGameOver:
            print('游戏结束')
            is_running = False
            game_2048.saveMaxScore()

        # 将元素画到屏幕上
        drawGameMatrix(screen, game_2048.game_matrix, cfg)
        (start_x, start_y) = drawScore(screen, game_2048.score, game_2048.max_score, cfg)
        drawGameIntro(screen, start_x, start_y, cfg)

        # 刷新画面
        pygame.display.update()

    # 游戏结束界面
    return endInterface(screen, cfg)

if __name__ =='__main__':
    while True:
        if not main(cfg):
            break