## 初始化设置
init -2 python:
    # 设置窗口属性
    config.screen_width = 1920
    config.screen_height = 1080
    
    # 禁用窗口调整大小
    config.gl_resize = False
    
    # 添加show_name定义
    gui.show_name = True
    
    # 设置背景和窗口样式
    style.window.background = Frame("gui/textbox.png", 0, 0)
    style.window.xsize = 1920
    style.window.ysize = 1080
    style.window.xalign = 0.5
    style.window.yalign = 0.5
    
    # 移除所有边距确保全屏显示
    style.window.padding = (0, 0, 0, 0)
    style.window.margin = (0, 0, 0, 0)
    
    # 设置图像显示方式
    config.preserve_zorder = True

    # 设置默认语言为英文
    config.language = "english"
    
    # 强制使用英文界面
    config.translations = {"japanese": False}
    
    # 设置字体回退
    style.default.language = "unicode"

    # 设置游戏名称和版本显示
    gui.main_menu_title = "FATE/RISD"
    gui.main_menu_version = "1.0"
    
    # 设置窗口标题
    config.window_title = "FATE/RISD"

# 添加关于界面的设置
define gui.about = _p("""
FATE/RISD - A Holy Grail War Story

Version 1.0

Created by: Your Name
Art: Your Artist
Music: Your Musician

Special Thanks:
- Type-Moon for Fate Series inspiration
- RISD for the setting
- All testers and supporters

This is a fan game created for educational purposes.
All rights belong to their respective owners.
""")

# 设置关于界面的样式
define gui.about_spacing = 15
define gui.about_text_size = 33
define gui.about_text_color = "#ffffff"

# 添加历史记录相关的GUI设置
define gui.history_height = 280  # 增加高度，给文字更多空间
define gui.history_spacing = 20  # 增加间距，防止文字重叠

# 调整文本位置和宽度
define gui.history_name_xpos = 150  # 名字左对齐
define gui.history_name_ypos = 0
define gui.history_name_width = 300  # 增加名字宽度
define gui.history_name_xalign = 0.0  # 名字左对齐

define gui.history_text_xpos = 500  # 对话文本右移
define gui.history_text_ypos = -3  # 稍微上移文本
define gui.history_text_width = 1000  # 增加文本宽度
define gui.history_text_xalign = 0.0  # 文本左对齐

# 调整字体大小
define gui.history_name_size = 36
define gui.history_text_size = 33

# 设置历史记录的颜色
define gui.history_name_color = "#c8c8ff"
define gui.history_text_color = "#ffffff"

# 添加历史记录的边距和背景
define gui.history_margins = (50, 10, 50, 10)
define gui.history_background = "#0008"

# 设置历史记录每页显示的条目数
define config.history_length = 250

# 设置历史记录的滚动条
define gui.history_scrollbar_size = 12
define gui.history_scrollbar_color = "#ffffff4d"
define gui.history_scrollbar_hover_color = "#ffffff80"

# 修改帮助界面文本为英文
define gui.help = _p("""
\u2022 Use Left Click or Space to advance dialogue
\u2022 Right Click or ESC brings up the game menu
\u2022 Mouse wheel to scroll back through dialogue
\u2022 Middle Click or H hides the text window
\u2022 Press S to take a screenshot
""")