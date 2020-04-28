"""
 功能：配置文件
 作者：指尖魔法师
 QQ：14555110
"""
import os

# 屏幕大小
SCREENSIZE = (650, 370)

# 背景颜色
BG_COLOR = '#92877d'

# 背景音乐路径
BGMPATH = 'resources/shaonian.mp3'

# 字体路径
FONTPATH = os.path.join(os.getcwd(), 'resources/gabriola.ttf')

# 4 * 4 大小
GAME_MATRIX_SIZE = (4, 4)

# 方块大小
MATRIX_SIZE = 80

# 方块间间距
MARGIN_SIZE = 10

# 保存最高分文件路径
MAX_SCORE_FILEPATH = 'score'