init python:
    # 强制全屏启动
    _preferences.fullscreen = True

# 添加字体定义
init python:
    # 定义默认字体
    style.default.font = "fonts/CrimsonText-Regular.ttf"
    
    # 定义文本样式 - 增大字体大小
    style.text.font = "fonts/CrimsonText-Regular.ttf"
    style.text.size = 32  # 从22增加到32
    
    # 定义按钮文本样式
    style.button_text.font = "fonts/CrimsonText-Regular.ttf"
    style.button_text.selected_font = "fonts/CrimsonText-Bold.ttf"
    style.button_text.size = 32  # 从22增加到32
    
    # 定义日文字体支持
    style.default.language = "japanese"
    style.default.size = 32  # 从22增加到32
    
    # 设置选项菜单样式
    style.choice_button_text.font = "fonts/CrimsonText-Regular.ttf"
    style.choice_button_text.hover_font = "fonts/CrimsonText-Bold.ttf"
    style.choice_button_text.size = 38  # 从28增加到38

# 定义对话框样式
style say_dialogue:
    font "fonts/NotoSansJP-Regular.ttf"  # 使用Noto Sans支持中日文
    size 32  # 从22增加到32
    line_spacing 10
    outlines [(1, "#000000", 0, 0)]

# 定义角色名称样式
style say_label:
    font "fonts/NotoSansJP-Bold.ttf"  # 使用Noto Sans支持中日文
    size 38  # 从28增加到38
    outlines [(2, "#000000", 0, 0)]

# 定义日文样式
style japanese:
    font "fonts/NotoSansJP-Regular.ttf"
    size 32  # 从22增加到32
    line_spacing 10

# 定义菜单样式
init python:
    style.choice_vbox = Style(style.vbox)
    style.choice_button = Style(style.button)
    style.choice_button_text = Style(style.button_text)
    
    # 设置菜单整体样式
    style.choice_vbox.xalign = 0.5
    style.choice_vbox.yalign = 0.5
    style.choice_vbox.spacing = 30
    
    # 设置按钮样式
    style.choice_button.xminimum = 600
    style.choice_button.xmaximum = 600
    style.choice_button.yminimum = 60
    style.choice_button.background = "#2b2b2bcc"
    style.choice_button.hover_background = "#4a4a4acc"
    style.choice_button.padding = (40, 20, 40, 20)
    style.choice_button.margin = (0, 5)
    
    # 设置选项文字样式
    style.choice_button_text.color = "#ffffff"
    style.choice_button_text.hover_color = "#ffcccc"
    style.choice_button_text.outlines = [(2, "#000000", 0, 0)]
    style.choice_button_text.hover_outlines = [(2, "#2b2b2b", 0, 0)]
    style.choice_button_text.text_align = 0.5
    style.choice_button_text.yalign = 0.5

# 游戏选项界面
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action

# 重新定义角色，使用正确的样式名称
define t = Character('Troy Martini (トロイ・マティーニ)', color="#c8c8ff", what_style="say_dialogue", who_style="say_label")
define d = Character('Leonardo da Vinci (ダ・ヴィンチ)', color="#ff9999", what_style="say_dialogue", who_style="say_label")
define k = Character('Kou (こう)', color="#ff8533", what_style="say_dialogue", who_style="say_label")
define h = Character('Hattori Hanzo (服部半蔵)', color="#666666", what_style="say_dialogue", who_style="say_label")
define e = Character('Eito (惠図)', color="#99ffac", what_style="say_dialogue", who_style="say_label")
define f = Character('Fred', color="#ffcc99", what_style="say_dialogue", who_style="say_label")
define eu = Character('Eugene Darius', color="#f6ab0a", what_style="say_dialogue", who_style="say_label")
define a = Character('Anakin', color="#ff3333", what_style="say_dialogue", who_style="say_label")
define v = Character('Darth Vader', color="#660000", what_style="say_dialogue", who_style="say_label")
define ar = Character('Arjun', color="#9966ff", what_style="say_dialogue", who_style="say_label")
define ka = Character('Karna (迦爾納)', color="#ff99cc", what_style="say_dialogue", who_style="say_label")
define ta = Character('Tang Zining (唐梓宁)', color="#ff66cc", what_style="say_dialogue", who_style="say_label")
define ko = Character('Xiang Yu (項羽)', color="#cc3300", what_style="say_dialogue", who_style="say_label")
define kc = Character('Huang Zhong (黄忠)', color="#f96552", what_style="say_dialogue", who_style="say_label")
define s = Character('Saladin', color="#996633", what_style="say_dialogue", who_style="say_label")
define narrator = Character(None, what_style="say_dialogue")

# 修改transform定义，统一角色立绘的显示效果
transform center_sprite:
    xalign 0.5  # 水平居中
    yalign 1.0  # 垂直对齐底部
    zoom 1.0    # 统一缩放比例
    yoffset -50 # 向上偏移以避免太靠底部

transform left_sprite:
    xalign 0.2  # 靠左
    yalign 1.0  # 垂直对齐底部
    zoom 1.0    # 统一缩放比例
    yoffset -50 # 向上偏移

transform right_sprite:
    xalign 0.8  # 靠右
    yalign 1.0  # 垂直对齐底部
    zoom 1.0    # 统一缩放比例
    yoffset -50 # 向上偏移

# 添加背景图片的transform
transform bg_transform:
    xalign 0.5
    yalign 0.5
    zoom 1.1  # 稍微放大以确保覆盖全屏

# 修改图片定义，应用新的transform
image bg troy_room = im.Scale("images/troy_room.jpg", 1920, 1080)
image bg model_shop = im.Scale("images/model_shop.jpg", 1920, 1080)
image bg west_15 = im.Scale("images/west_15.jpg", 1920, 1080)
image bg risd_beach = im.Scale("images/risd_beach.jpg", 1920, 1080)
image bg risd_place = im.Scale("images/risd_place.jpg", 1920, 1080)
image bg brown_bg = im.Scale("images/brown_bg.jpg", 1920, 1080)
image bg fengmian = im.Scale("images/fengman.png", 2300, 1080)
image bg bad_end = im.Scale("images/bad_end.jpg", 1920, 1080)

# 统一角色立绘大小
image kou = im.Scale("images/kou.png", 585, 950)
image davinci = im.Scale("images/davinci.png", 725, 900)
image hattori = im.Scale("images/hattori.png", 665, 1000)
image troy = im.Scale("images/troy.png", 615, 1000)
image eito = im.Scale("images/eito.png", 600, 975)
image eugene = im.Scale("images/eugene.png", 740, 1000)
image fred = im.Scale("images/fred.png", 600, 1000)
image anakin = im.Scale("images/anakin.png", 700, 1000)
image vader = im.Scale("images/vader.png", 925, 1400)
image arjun = im.Scale("images/arjun.png", 465, 1000)
image karna = im.Scale("images/karna.png", 580, 960)
image tangzining = im.Scale("images/tangzining.png", 585, 950)
image xiangyu = im.Scale("images/xiangyu.png", 685, 1000)
image huangzhong = im.Scale("images/huangzhong.png", 700, 1000)

# 在文件开头的定义部分添加
define audio.room_theme = "audio/The illusion.mp3"
define audio.shop_theme = "audio/yueshu.mp3"  # 添加新的音乐定义
define audio.end_theme = "audio/gudu.mp3"  # 添加结局音乐
define audio.battle_theme = "audio/zhandou.mp3"  # 添加战斗音乐
define audio.west_theme = "audio/yee.mp3"  # 添加15 West场景音乐

# 游戏主体代码
label start:
    play music room_theme fadeout 1.0 fadein 1.0
    scene bg troy_room with fade
    
    show troy at left_sprite with dissolve
    t "(I am Troy Martini, an Industrial Design student at RISD.)"
    t "(Until a few days ago, I was living a normal life. But that day, when I opened my eyes, everything changed...)"
    t "W-Who are you?!"
    
    show davinci at right_sprite with dissolve
    d "Good morning, Master! (おはようございます、御主様!)"
    
    d "I am Leonardo da Vinci, a Caster-class Servant, and I have been summoned to serve you."
    d "You have been chosen to participate in the Holy Grail War (聖杯戦争)."
    
    t "Holy Grail War? What is that?!"
    
    d "The Holy Grail War is a special battle between seven Masters and their Servants (サーヴァント)."
    d "Servants are heroic spirits from history and mythology. You must defeat all other participants."
    d "The last one standing will receive the omnipotent Holy Grail, capable of granting any wish."
    d "For your safety, we should head to the Model Shop immediately."
    hide troy
    hide davinci

    menu:
        "What will you do?"
        
        "Ask more about the Holy Grail War":
            jump ask_more
            
        "Go to the Model Shop with da Vinci":
            jump go_to_shop

label ask_more:
    t "If I lose... will I die?"
    
    show davinci at center_sprite with dissolve
    d "Yes, that's correct."
    d "However, if you die, I will disappear as well."
    d "That's why I will protect you with all my power."
    hide davinci with dissolve
    
    jump go_to_shop

label go_to_shop:
    play music shop_theme fadeout 1.0 fadein 1.0
    scene bg model_shop with fade
    
    "As soon as we entered the Model Shop, we encountered a student with an ominous aura. He was staring at us with cold eyes."
    
    show davinci at right_sprite with dissolve
    d "Be careful, Troy. This person seems dangerous."
    
    show troy at left_sprite with dissolve
    t "Is he an enemy?"
    hide troy
    hide davinci
    
    show kou at center_sprite with dissolve
    k "Hmph, I am Kou from Japan."
    k "In the Holy Grail War, there are only winners and losers. You'll soon become the latter!"
    hide kou

    show hattori at center_sprite with dissolve
    k "By my Command Seal (令呪), I order you, Servant Hattori Hanzo! Use your Noble Phantasm (宝具)!"
    
    h "Shadow Clone Technique: Thousand Shadow Phantoms (隠身の術：影遁千影)!"
    hide hattori

    "Hattori Hanzo creates multiple shadow clones and launches an attack towards Troy."
    
    show davinci at right_sprite with dissolve
    d "Troy, watch out! I'll protect you!"
    d "Imaginary Workshop: Virtual Craftsman (虚数工房：仮想の工匠)!"
    
    "Da Vinci's Noble Phantasm activates, creating a defensive barrier that blocks the enemy's attack."
    
    show troy at left_sprite with dissolve
    d "That's ninja techniques... Troy, I'm at my limit."
    hide davinci
    hide troy

    menu:
        "What will you do?"
        
        "Run away":
            jump run_away
            
        "Keep fighting":
            jump keep_fighting

label run_away:
    play music shop_theme fadeout 1.0 fadein 1.0
    scene bg brown_bg with fade
    "While fleeing from the battle with Kou, Troy bumps into Eito."
    
    show eito at center_sprite with dissolve
    e "Huang Zhong, take care of the pursuing Servant!"
    
    show huangzhong at right_sprite with dissolve
    kc "Understood!"
    
    "Huang Zhong releases an arrow, and Hattori Hanzo, unable to dodge in the open space, is defeated."
    hide huangzhong
    hide eito
    
    show kou at center_sprite with dissolve
    k "Damn... I didn't expect you to be involved in this too..."
    hide kou
    
    show troy at left_sprite with dissolve
    t "Eito, you're...?"
    
    show eito at right_sprite with dissolve
    e "Looks like we've got the same 'problem' here."
    
    t "You really saved me there, thank you!"
    hide troy
    hide eito

label keep_fighting:
    show davinci at right_sprite with dissolve
    d "Troy, quickly strengthen me with your Command Seal (令呪)!"
    
    show troy at left_sprite with dissolve
    t "By my Command Seal, I order you, Da Vinci! Use your Noble Phantasm (宝具)!"
    
    d "Imaginary Workshop: Virtual Craftsman (虚数工房：仮想の工匠)!!!"
    
    "Da Vinci's shockwave hits Hattori Hanzo, defeating him."
    hide davinci
    hide troy

    show kou at center_sprite with dissolve
    k "Wait! Please don't kill me! I'll do anything!"
    hide kou

    show troy at center_sprite with dissolve
    t "Did we... win? Is this the Holy Grail War (聖杯戦争)...?"
    hide troy
    hide davinci

    show kou at center_sprite with dissolve
    menu:
        "What will you do?"
        
        "Spare Kou":
            hide kou
            jump rooftop_meeting
            
        "Defeat Kou":
            hide kou
            jump defeat_kou

label spare_kou:
    "Troy chose to spare Kou."
    jump rooftop_meeting

label defeat_kou:
    "Troy chose to defeat Kou."
    jump rooftop_message

label rooftop_message:
    "Checking his phone, Troy notices a message."
    
    show troy at center_sprite with dissolve
    t "Eito... he's been messaging me since the Holy Grail War began. I should reply now."
    t "I just finished a battle at the Model Shop. Where can we meet?"
    hide troy with dissolve
    
    show eito at center_sprite with dissolve
    e "Troy, you don't have to fight alone. Tell me where you are, let's fight together."
    hide eito with dissolve
    "A few minutes later, Eito replies, and they agree to meet on the rooftop of 15 Westminster."
    
    # 15 West场景
label rooftop_meeting:
    play music west_theme fadeout 1.0 fadein 1.0
    scene bg west_15 with fade
    
    show eito at center_sprite with dissolve
    e "Troy, you're okay. Let's fight together."

    show troy at left_sprite with dissolve
    t "Thanks, Eito."
    
    "They smile at each other, forming an alliance, and prepare for the next battle."
    
    t "Look over there... there's something moving over there. Are other Masters fighting there?"
    
    show eito at right_sprite with dissolve
    e "Yes, that's RISD Beach. My Servant, Huang Zhong, has the power to judge, and they're fighting there with the American Master Fred and the Saber Archer Anakin, and the Turkish Master Eugene Darius and the Rider Saber Saladin."
    hide troy
    hide eito

# RISD Beach场景
label beach_battle:
    play music battle_theme fadeout 1.0 fadein 1.0
    scene bg risd_beach with fade
    "RISD Beach was where the two Masters faced each other."
    
    show eugene at right_sprite with dissolve
    eu "Fred, I didn't like your face before. I knew it was Anakin Skywalker's light saber. I could tell from the moment it started attacking."
    
    show fred at left_sprite with dissolve
    f "Damn, you saw through it. I have to do it."
    hide eugene
    hide fred
    
    "Anakin activated his Noble Phantasm, 'The Force and I Are One' (願原力与我同在), and began attacking with his light saber."
    "The clash between the light saber and the knight's spear was intense, and sparks flew everywhere. The battle intensified."
    
    show troy at left_sprite
    show eito at right_sprite with dissolve
    e "Troy, you have two choices. You can either take out the Anakin Master or the Saladin Master."
    hide troy
    hide eito

    menu:
        "Which one do you target?"
        
        "Target the Anakin Master":
            jump target_anakin_exact
            
        "Target the Saladin Master":
            jump target_saladin_exact

label target_anakin_exact:
    show troy at left_sprite with dissolve
    t "Eito, target Anakin!"
    
    "Eito shot at Fred, but in an instant, Anakin let out a roar of anger, and his body was enveloped in darkness, becoming Darth Vader."
    
    hide troy
    show vader at center_sprite with dissolve
    v "Your fate is already decided. Feel the power of the dark side."
    hide vader
    
    "Darth Vader defeated everyone in succession."
    
    jump bad_end_exact

label target_saladin_exact:
    show troy at center_sprite with dissolve
    t "Eito, target Saladin!"
    hide troy with dissolve
    
    "Huang Zhong's Noble Phantasm, 'My Arrow Is Still Sharp Even If I Am Old' (吾虽年迈箭矢尤锋), hit Eugene Darius exactly."
    
    show troy at center_sprite with dissolve
    t "That's right, this is your chance. Huang Zhong, prepare again!"
    hide troy with dissolve
    
    show huangzhong at center_sprite with dissolve
    kc "Please wait a moment. I can feel the presence of other Servants. I'll check their information with 'Insight Eyes' (洞察之眼)."
    
    t "What kind of information can you see?"
    
    kc "The Lancer Karna, from the Hindu myth, is a hero from the Indian legend. His Master is Arjun, an Indian student."
    kc "And the Berserker is Xiang Yu, a general from the Qin Dynasty in China, and his Master is Tang Zining."
    hide huangzhong
    
    "At that time, Fred also noticed them."
    
    show fred at center_sprite with dissolve
    f "New face... If you're going to fight with Archer and Caster together, let's cooperate and take them out, right?"
    hide fred
    
    "Arjun and Tang Zining looked at each other and nodded in agreement."
    
    show arjun at left_sprite
    show tangzining at right_sprite with dissolve
    ar "If you're right, then the cooperation here has meaning."
    ta "That's right, the temporary cooperation has value, right?"
    hide arjun
    hide tangzining
    
    show fred at center_sprite with dissolve
    f "Okay, then... let's start!"
    hide fred
    
    show troy at center_sprite with dissolve
    t "Having such powerful Servants working together... this is quite disadvantageous."
    
    hide troy
    show huangzhong at center_sprite with dissolve
    kc "But there's still a chance."
    
    "Huang Zhong drew his bow and shot at Anakin's shoulder, causing Anakin to be surprised and mumble."
    hide huangzhong
    
    show anakin at center_sprite with dissolve
    a "Damn... you hurt me!"
    hide anakin
    
    show troy at left_sprite
    show davinci at right_sprite with dissolve
    t "Da Vinci, now!"
    
    d "Understood, Master."
    
    "Da Vinci's light cannon hit Anakin directly, erasing him."
    hide davinci
    hide troy
    
    show eito at center_sprite with dissolve
    "Eito restrained Tang Zining from behind and aimed the weapon at her neck."
    
    e "The Berserker Master is mine! Don't move!"
    hide eito
    show xiangyu at center_sprite with dissolve
    ko "Let her go!"
    hide xiangyu
    hide eito
    
    "Arjun commanded calmly."
    
    show arjun at center_sprite with dissolve
    ar "Karna, do it."
    hide arjun
    
    show karna at center_sprite with dissolve
    "Karna stabbed Eito and Tang Zining with his spear. Eito fell and Tang Zining suffered heavy injuries."
    hide karna
    
    show eito at center_sprite with dissolve
    e "Troy... I'm sorry..."
    hide eito
    
    show xiangyu at left_sprite
    show arjun at right_sprite with dissolve
    ko "Why didn't you help, Arjun?"
    ar "Cooperation is only temporary. The one who can grant the Holy Grail is only one person."
    hide xiangyu
    hide arjun
    
    show tangzining at center_sprite with dissolve
    ta "Xiang Yu, use your Noble Phantasm... on him."
    hide tangzining
    show xiangyu at center_sprite with dissolve
    ko "But that will kill you!"
    hide xiangyu
    show tangzining at center_sprite with dissolve
    ta "Anyone who betrays me should all die!"
    hide tangzining

    "Xiang Yu activated his Noble Phantasm, 'The King and His Concubine' (霸王别姬), causing a massive explosion to engulf the battlefield."
    
    "When the smoke cleared, Da Vinci was uninjured, but Karna was already defeated."
    
    show davinci at center_sprite with dissolve
    d "Troy, we've won."
    hide davinci
    
    "Troy took the Holy Grail, but the surrounding area was silent, and Eito's body was cold."

    menu:
        "What do you wish for the Holy Grail?"
        
        "Wish to forget everything":
            jump forget_ending
            
        "Wish to become the god of the world":
            jump god_ending

label bad_end_exact:
    play music end_theme fadeout 1.0 fadein 1.0
    scene bg bad_end with fade
    "No one survived..."
    "Darth Vader's dark power ended everything."
    "～Bad End～"
    return

label forget_ending:
    play music end_theme fadeout 1.0 fadein 1.0
    scene bg risd_place with fade
    show troy at center_sprite with dissolve
    t "Is this all there is... is it really worth it to get the Holy Grail by sacrificing the most important friend?"
    t "Please, Holy Grail (聖杯), please let me forget everything..."
    hide troy with dissolve
    
    "Troy used the power of the Holy Grail to turn back time and eliminate the existence of the Holy Grail War (聖杯戦争)."
    
    t "Eito... let's study and play together again like before."
    
    scene bg risd_place with fade
    "Everything returned to normal."
    "The daily life of the two began again."
    "～Reset End～"
    return

label god_ending:
    show troy at center_sprite with dissolve
    t "Ha ha ha ha ha! I won! I'm going to become the god of this world!"
    
    menu:
        "Final Choice"
        
        "Revive Eito":
            jump revive_friend_exact
            
        "Wish to become the god of the world":
            jump dream_end_exact

label revive_friend_exact:
    play music end_theme fadeout 1.0 fadein 1.0
    scene bg risd_place with fade
    show troy at center_sprite with dissolve
    t "Without friends, nothing has meaning."
    t "Please let me forget everything... Holy Grail (聖杯)..."
    hide troy with dissolve
    "Troy used the power of the Holy Grail to turn back time and eliminate the existence of the Holy Grail War (聖杯戦争)."
    
    scene bg risd_place with fade
    t "Eito... let's study and play together again like before."
    "～Friendship End～"
    return

label dream_end_exact:
    play music end_theme fadeout 1.0 fadein 1.0
    scene black with fade
    "Nothing happened. It was all a dream that Troy was seeing."
    
    scene bg troy_room with fade
    "Troy woke up."
    "It was all a dream. But the clear sense of bonds (絆) remained."
    "～Dream End～"
    return

# 在游戏开始前添加封面显示
label splashscreen:
    scene bg fengmian with fade
    "FATE/RISD - A Holy Grail War (聖杯戦争) Story"
    pause 2.0
    scene black with fade
    return