label SGFD2_OKA01A:



    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT001")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade

    $ date="8/10"
    $ day="WED"






    $ loadBG(0,"BG23A0")

    play bgm "BGM05"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA02"),"True","lh/FEI_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0000"
    $ current_voice = "voice/OKA01A_FEI0000.ogg"
    "Faris NyanNyan" "「Oh, good morning-nya!」"
    window hide


    hide screen phonebtn
    $ loadBG(2,"IBG020A")



    play se "SGSE346"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET"])
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0000"
    $ current_voice = "voice/OKA01A_MAY0000.ogg"
    "Shiina Mayuri" "Wow，that's an amazing bus! It's covered in {color=#f00}RAINET{/color}!」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    "A bus was parked in front of {color=#f00}ＵＰＸ{/color}."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB3D"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB3D"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET_AB3D"])
    "It was advertising the release date of the popular game 「{color=#f00}RAINET AB3D{/color}」. It was the promotion bus that drove around Akihabara."
    "The sides of the bus were covered in RAINET characters and TV screens looping promotional videos."
    window hide



    $ loadBG(2,"BG23A0")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA02"),"True","lh/FEI_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("voc")
    play voc "OKA01A_Y030000"
    $ current_voice = "voice/OKA01A_Y030000.ogg"
    "工作人员" "「冠军，今天虽然会很辛苦，但还是拜托您了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSB01"),"True","lh/FEI_BSB01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0001"
    $ current_voice = "voice/OKA01A_FEI0001.ogg"
    "菲利斯" "「是，还请各位多多指教喵！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET_AB"])
    "菲利斯是{color=#f00}雷ＮｅｔＡＢ{/color}的四联冠军。"
    "被部分人很早就称呼的「绝对王者」这个名字也很响亮。"
    "而且又有型，是做宣传的上佳人才。"
    "因此在雷ＮｅｔＡＢ３Ｄ发售前夕，被借来当活动嘉宾。"
    hide screen phoneSD1
    window hide

    stop bgm 
    stop se
    stop se


    hide screen phonebtn
    $ loadBG(2,"BG_BLACK",trans=fade)





    "然而，这就是一切悲剧的开头——"

    window hide



    $ loadBG(0,"IBG020A")

    play bgm "BGM18"
    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0002"
    $ current_voice = "voice/OKA01A_FEI0002.ogg"
    pause 0.00001
    "菲利斯" "「那个，我能拍几张照片用在博客上吗喵？？」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0001"
    $ current_voice = "voice/OKA01A_MAY0001.ogg"
    "真由理" "「啊，真由喜也想拍」"
    $ stopvoc("Y03")
    play voc "OKA01A_Y030001"
    $ current_voice = "voice/OKA01A_Y030001.ogg"
    "工作人员" "「当然可以啊！对了，从角度来看，还是在那边拍比较——」"
    window hide


    $ loadBG(2,"BG23A0")



    show screen phonebtn
    "在宣传人员的引导下，两人来到了巴士的阴影处。"
    "就是现在。"
    "以不被宣传人员发现的动作，我趴着身子从菲利斯她们的视觉盲点冲进了巴士。"
    hide screen phonebtn
    window hide



    show screen phonebtn
    $ loadBG(2,"BG_BLACK",trans=fade)
    $ loadBG(0,"BG66A")

    "车内的中部，宣传用品杂乱地被扔在纸箱里。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn

    stop bgm 
    "没关系，谁都没有发现我。"
    "车内的东西到处乱放，所以只要顺利溜进来了，就不会简单地暴露。"
    "我用身后的斗篷盖着身体，静静地等待时机的到来。"
    window hide


    play se "SGSE110"

    pause 0.5
    "终于，真由理和菲利斯再度进入车内，拉上了驾驶席后的窗帘。"
    play se "SGSE056"

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0003"
    $ current_voice = "voice/OKA01A_FEI0003.ogg"
    "菲利斯" "「啊……呼」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSTUME"])
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0004"
    $ current_voice = "voice/OKA01A_FEI0004.ogg"
    "菲利斯" "「第一次{color=#f00}Cos{/color}凯拉玲，会不会有问题呀喵？」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0002"
    $ current_voice = "voice/OKA01A_MAY0002.ogg"
    "真由理" "「菲利斯绝对适合！」"
    play se "SGSE072"
    "听着真由理的鼓劲，菲利斯开始换衣服。"
    "脱下平时穿的衣服后就露出了细细的手。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_LAYER"])
    "顺带一提，真由理也来帮忙装扮成{color=#f00}Ｌａｙｅｒ{/color}"
    play se "SGSE390"
    "她也一件件地脱下衣服。"
    "…………"
    "绝对不能有什么歪想法。"
    "为了不让冲出去的机会溜掉，我死死地监视着她们两人换衣服。"
    stop se
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0005"
    $ current_voice = "voice/OKA01A_FEI0005.ogg"
    "菲利斯" "「啊……抱歉喵！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0006"
    $ current_voice = "voice/OKA01A_FEI0006.ogg"
    "菲利斯" "「我可以继续戴着这个耳朵吗喵？」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0003"
    $ current_voice = "voice/OKA01A_MAY0003.ogg"
    "真由理" "「是呢，这对耳朵是菲利斯的标物呢」"
    "就是标志性物品。"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0007"
    $ current_voice = "voice/OKA01A_FEI0007.ogg"
    "菲利斯" "「不好意思，有听到我说话吗喵？」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0008"
    $ current_voice = "voice/OKA01A_FEI0008.ogg"
    "菲利斯" "「……去什么地方了吗喵？」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0009"
    $ current_voice = "voice/OKA01A_FEI0009.ogg"
    "菲利斯" "「那个，不好意思——」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040000"
    $ current_voice = "voice/OKA01A_Y040000.ogg"
    "巴士劫持犯" "「嘿嘿嘿嘿嘿嘿……」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0010"
    $ current_voice = "voice/OKA01A_FEI0010.ogg"
    "菲利斯" "「喵！？」"
    window hide
    play bgm "BGM08"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") at right as lh6 zorder (10-6) :
        ypos 1.15
    $ loadBG(0,"BG66A",trans=ImageDissolve(im.Scale("mask/mask11.png",1024,576),2),hide=False)

















    play se "SGSE352"














    "拉开窗帘，正好与正在换衣服的两个人目光交汇。"
    "眼前的是，一个两眼放光身材消瘦的男子。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC04"),"True","lh/FEI_BSC04a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0011"
    $ current_voice = "voice/OKA01A_FEI0011.ogg"
    "菲利斯" "「喵啊啊啊啊啊！！」"
    "菲利斯急忙用衣服挡住身体发出尖叫。"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0012"
    $ current_voice = "voice/OKA01A_FEI0012.ogg"
    "菲利斯" "「讨厌！喂，你这变态不要过来呀喵！」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0004"
    $ current_voice = "voice/OKA01A_MAY0004.ogg"
    "真由理" "「真由喜觉得变态是不对的！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040001"
    $ current_voice = "voice/OKA01A_Y040001.ogg"
    "巴士劫持犯" "「你、你们不要误会！我不是为了偷窥而来的！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040002"
    $ current_voice = "voice/OKA01A_Y040002.ogg"
    "巴士劫持犯" "「我、我是来劫巴士的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0013"
    $ current_voice = "voice/OKA01A_FEI0013.ogg"
    "菲利斯" "「喵──？」"
    "菲利斯现在才第一次发现。"
    "男人手中那把刃长超过３０厘米的长刀反射着光芒。"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040003"
    $ current_voice = "voice/OKA01A_Y040003.ogg"
    "巴士劫持犯" "「我、我要把你们劫为人质」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh6 zorder (10-6) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0005"
    $ current_voice = "voice/OKA01A_MAY0005.ogg"
    "真由理" "「人质？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0014"
    $ current_voice = "voice/OKA01A_FEI0014.ogg"
    "菲利斯" "「别开玩笑了喵！为什么要——」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040004"
    $ current_voice = "voice/OKA01A_Y040004.ogg"
    "巴士劫持犯" "「别吵！你没看见这个吗！」"
    "巴士劫持犯拿着刀一步步地靠近。"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040005"
    $ current_voice = "voice/OKA01A_Y040005.ogg"
    "巴士劫持犯" "「这、这是天罚！『雷ＮｅｔＡＢ(Ａｃｃｅｓｓ　Ｂａｔｔｌｅｒｓ)』是最好的游戏！靠预测力、欺骗力和勇气来定胜败，是成人竞技！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040006"
    $ current_voice = "voice/OKA01A_Y040006.ogg"
    "巴士劫持犯" "「但是有必要故意做成儿童向的吗？就连点阵图都乱画，让这么可爱的角色凯拉玲酱都废掉了！！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLYING_GET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLYING_GET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_FLYING_GET"])
    $ stopvoc("Y04")
    play voc "OKA01A_Y040007"
    $ current_voice = "voice/OKA01A_Y040007.ogg"
    "巴士劫持犯" "「而且还传说有{color=#f00}Ｆｌｙｇｅ{/color}！在未来篇中，凯拉玲酱成了母亲！？别开玩笑了！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040008"
    $ current_voice = "voice/OKA01A_Y040008.ogg"
    "巴士劫持犯" "「凯拉玲酱怎么会和男人恋爱！这种展开，绝、绝、绝、绝对不能容忍啊———————！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0006"
    $ current_voice = "voice/OKA01A_MAY0006.ogg"
    "真由理" "「嗯，但是真由喜认为凯拉玲酱也会有一天想要恋爱吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0015"
    $ current_voice = "voice/OKA01A_FEI0015.ogg"
    "菲利斯" "「况且你把我们当成人质要去干什么喵？」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040009"
    $ current_voice = "voice/OKA01A_Y040009.ogg"
    "巴士劫持犯" "「我、我们要让游戏停止发售！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0007"
    $ current_voice = "voice/OKA01A_MAY0007.ogg"
    "真由理" "「这怎么可以…大家好不容易才等到的」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUSOGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUSOGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KUSOGE"])
    $ stopvoc("Y04")
    play voc "OKA01A_Y040010"
    $ current_voice = "voice/OKA01A_Y040010.ogg"
    "巴士劫持犯" "「{color=#f00}粪作{/color}就不应该出现在世上！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0016"
    $ current_voice = "voice/OKA01A_FEI0016.ogg"
    "菲利斯" "「别开玩笑了喵！」"
    "菲利斯大声地反驳道。"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0017"
    $ current_voice = "voice/OKA01A_FEI0017.ogg"
    "菲利斯" "「你们不配做粉丝喵！无论怎样的游戏，都倾注了创作者的心血喵。这个世上没有不该出现的游戏喵！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0018"
    $ current_voice = "voice/OKA01A_FEI0018.ogg"
    "菲利斯" "「我知道你们讨厌游戏的原因了喵。但是，这种思想不能强加给所有人喵！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040011"
    $ current_voice = "voice/OKA01A_Y040011.ogg"
    "巴士劫持犯" "「闭嘴！！」"
    window hide
    play se "SGSE148"



    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") as lh6 zorder (10-6) :
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0019"
    $ current_voice = "voice/OKA01A_FEI0019.ogg"
    "菲利斯" "「呀！」"
    "长刀一闪。"
    "边上的显示器电缆被切断了。"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040012"
    $ current_voice = "voice/OKA01A_Y040012.ogg"
    "巴士劫持犯" "「真、真真是不听话的人质。就让我亲自来教训你——嘿嘿嘿嘿嘿………」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0008"
    $ current_voice = "voice/OKA01A_MAY0008.ogg"
    "真由理" "「你别激动！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0020"
    $ current_voice = "voice/OKA01A_FEI0020.ogg"
    "菲利斯" "「不……不要喵！别过来！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040013"
    $ current_voice = "voice/OKA01A_Y040013.ogg"
    "巴士劫持犯" "「怎、怎么了？刚刚的气势去哪了？」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040014"
    $ current_voice = "voice/OKA01A_Y040014.ogg"
    "巴士劫持犯" "「现在就算你喊破喉咙也没有人——」"
    stop bgm 
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0000"
    $ current_voice = "voice/OKA01A_OKA0000.ogg"
    "伦太郎" "「嗬———！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh6 zorder (10-6) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("Y04")
    play voc "OKA01A_Y040015"
    $ current_voice = "voice/OKA01A_Y040015.ogg"
    "巴士劫持犯" "「嗯……？」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0021"
    $ current_voice = "voice/OKA01A_FEI0021.ogg"
    "菲利斯" "「这个声音是——！？」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0001"
    $ current_voice = "voice/OKA01A_OKA0001.ogg"
    "伦太郎" "「嘿！！」"
    window hide
    play se "SGSE347"
    $ loadBG(1,"BG_BLACK",trans=Dissolve(0.1))
    $ loadBG(0,"BG66A",trans=Dissolve(0.1))




    "我帅气地从藏身的箱子中冲了出来。"
    "就是为了这一刻，才事先偷偷潜入巴士中的！"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040016"
    $ current_voice = "voice/OKA01A_Y040016.ogg"
    "巴士劫持犯" "「你、你是什么人！！」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0002"
    $ current_voice = "voice/OKA01A_OKA0002.ogg"
    "伦太郎" "「我？我的名字是——」"
    hide screen phoneSD1
    window hide
    play bgm "FD2BGM03"
    $ current_voice = "voice/FD2BGM03.ogg"

label L_OKB:
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001A"]]["Check"]=True

    show EVOKA001A_BG1 
    show EVOKA001A_FACE_R 

    hide screen phonebtn
    with Fade(0.1,0.1,0.1,color="fff")
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0003"
    $ current_voice = "voice/OKA01A_OKA0003.ogg"
    "伦太郎" "「天在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001B"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG1 
    hide EVOKA001A_FACE_R 
    show EVOKA001A_BG2 
    show EVOKA001A_FACE_L 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA01A_OKA0004"
    $ current_voice = "voice/OKA01A_OKA0004.ogg"
    "伦太郎" "「地在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001C"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG2 
    hide EVOKA001A_FACE_L 
    show EVOKA001A_BG3 
    show EVOKA001A_FACE_C 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA01A_OKA0005"
    $ current_voice = "voice/OKA01A_OKA0005.ogg"
    "伦太郎" "「安第斯在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001D"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG3 
    hide EVOKA001A_FACE_C 
    show EVOKA001A_BG4 
    show EVOKA001A_FACE_H 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA01A_OKA0006"
    $ current_voice = "voice/OKA01A_OKA0006.ogg"
    "伦太郎" "「秋叶原中诞生的神秘英雄！」"
    window hide







    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001E"]]["Check"]=True






    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPACA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPACA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ALPACA"])
    hide EVOKA001A_FACE_H 
    show EVOKA001A_HAND 
    show EVOKA001A_FACE 
    with Fade(0.1,0.1,0.1,color="fff")
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0007"
    $ current_voice = "voice/OKA01A_OKA0007.ogg"
    "伦太郎" "「{color=#f00}羊驼{/color}人，登场！」"


    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0009"
    $ current_voice = "voice/OKA01A_MAY0009.ogg"
    "真由理" "「哇！是羊驼人本尊！！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0022"
    $ current_voice = "voice/OKA01A_FEI0022.ogg"
    "菲利斯" "「这个，怎么听这声音都是凶真———啊！！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SECRET_ORG"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SECRET_ORG"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SECRET_ORG"])
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0023"
    $ current_voice = "voice/OKA01A_FEI0023.ogg"
    "菲利斯" "「难、难道凶真接受了{color=#f00}恶之秘密组织{/color}的改造喵！？」"
    window hide
    hide EVOKA001A_HAND 
    hide EVOKA001A_BG4 
    hide EVOKA001A_FACE 




    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001B"]]["Check"]=True
    $ loadBG(0,"EV_OKA001B0",trans=fade)












    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0008"
    $ current_voice = "voice/OKA01A_OKA0008.ogg"
    "伦太郎" "「我的名字不是什么凤凰院凶真！！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001E"]]["Check"]=True







    show EVOKA001E 
    with dissolve
    play se "SGSE347"










    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0009"
    $ current_voice = "voice/OKA01A_OKA0009.ogg"
    "伦太郎" "「是秋叶原中诞生的神秘英雄——羊驼人！！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0024"
    $ current_voice = "voice/OKA01A_FEI0024.ogg"
    "菲利斯" "「但是……羊驼人，是怎么知道凶真的姓是凤凰院的？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPA_POWER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPA_POWER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ALPA_POWER"])
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0010"
    $ current_voice = "voice/OKA01A_OKA0010.ogg"
    "伦太郎" "「唔！　那，那当然是因为{color=#f00}羊驼之力{/color}的关系！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TITICACA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TITICACA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TITICACA"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VIRACOCHA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VIRACOCHA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_VIRACOCHA"])

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0025"
    $ current_voice = "voice/OKA01A_FEI0025.ogg"
    "菲利斯" "「羊驼之力！？与{color=#f00}维拉科嘉神{/color}共同沉入{color=#f00}琪琪咔咔湖{/color}的湖底中的那个特殊能力，凶真已经搞到手了喵！？」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001B"]]["Check"]=True
    hide EVOKA001E 


    $ loadBG(2,"EV_OKA001B0")



    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0011"
    $ current_voice = "voice/OKA01A_OKA0011.ogg"
    "伦太郎" "「都说了不是凶真而是羊驼人啦！」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0010"
    $ current_voice = "voice/OKA01A_MAY0010.ogg"
    "真由理" "「羊驼人，加油！」"
    window hide



    $ loadBG(2,"BG66A",hold=True)


    $ loadBG(3,"IBG019A",png=True)




    show screen phonebtn
    show screen phoneSD1
    "真由理的一句话让我回过神来。"
    "没错，我是守护秋叶原的正义的伙伴，羊驼人！"
    "有着将真由理从人质的困境中救出来的使命！"
    hide background-png 
    with dissolve

    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0012"
    $ current_voice = "voice/OKA01A_OKA0012.ogg"
    "伦太郎" "「所以，恶人们都等着吧——」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040017"
    $ current_voice = "voice/OKA01A_Y040017.ogg"
    "巴士劫持犯" "「哇啊啊啊啊啊啊啊啊！！」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0026"
    $ current_voice = "voice/OKA01A_FEI0026.ogg"
    "菲利斯" "「凶真！！」"
    window hide
    play se "SGSE155"


    stop bgm
    with Fade(0.1,0.1,0.1,color="f00")

    "回过头的瞬间，刀，刺了进来。"
    "四处飞散的红色液体。"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0013"
    $ current_voice = "voice/OKA01A_OKA0013.ogg"
    "伦太郎" "「唔——唔唔唔！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040018"
    $ current_voice = "voice/OKA01A_Y040018.ogg"
    "巴士劫持犯" "「别把我们当傻子！无、无视我——诶？啊，唔、啊、唔唔」"





    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0014"
    $ current_voice = "voice/OKA01A_OKA0014.ogg"
    "伦太郎" "「唔——唔——唔呼呼呼！看来胜负已定」"


    play se "SGSE391"

    "拔出插在胸前的长刀，我大声笑道。"
    "巴士劫持犯看见红色的液体，完全失了神。"
    "一边扶着脸，跌坐在地上。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA03"),"True","lh/FEI_BMA03a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0027"
    $ current_voice = "voice/OKA01A_FEI0027.ogg"
    "菲利斯" "「凶真，受伤了吗——！？」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0015"
    $ current_voice = "voice/OKA01A_OKA0015.ogg"
    "伦太郎" "「不用担心！羊驼服下面穿着防刺背心！而且！！」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001E"]]["Check"]=True













    hide lh5 
    show EVOKA001E2 
    hide screen phonebtn
    "我将羊驼服厚厚的毛扒开，让她们看里面。"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0028"
    $ current_voice = "voice/OKA01A_FEI0028.ogg"
    "菲利斯" "「咦？好像有个袋喵……？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPACA_TOOLS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ALPACA_TOOLS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ALPACA_TOOLS"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_COUNTER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_COUNTER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SALSA_COUNTER"])

    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0016"
    $ current_voice = "voice/OKA01A_OKA0016.ogg"
    "伦太郎" "「没错。这是{color=#f00}羊驼七道具( seven gear ){/color}中的一个！{color=#f00} Ｓａｌｓａ　Ｃｏｕｎｔｅｒ{/color}！」"
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0011"
    $ current_voice = "voice/OKA01A_MAY0011.ogg"
    "真由理" "「猴子什么来着？」"
    hide EVOKA001E2 
    show EVOKA001E3 






    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0017"
    $ current_voice = "voice/OKA01A_OKA0017.ogg"
    "伦太郎" "「不是猴子！Ｓａｌｓａ　Ｃｏｕｎｔｅｒ是根据受到攻击的地方，来正确喷出莎莎酱的必杀技！！」"


    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HABANERO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HABANERO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HABANERO"])
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0018"
    $ current_voice = "voice/OKA01A_OKA0018.ogg"
    "伦太郎" "「被在南美的太阳下生长的{color=#f00}Ｊａｌａｐｅｎｏ{/color}淋到，不可能忍受的了！」"
    window hide


    hide EVOKA001E3 
    $ loadBG(2,"BG66A")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("Y04")
    play voc "OKA01A_Y040019"
    $ current_voice = "voice/OKA01A_Y040019.ogg"
    "巴士劫持犯" "「呜哇！啊、唔、唔……！！」"
    "巴士劫持犯的呻吟声从地上传来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA03"),"True","lh/FEI_BMA03a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0029"
    $ current_voice = "voice/OKA01A_FEI0029.ogg"
    "菲利斯" "「喵喵！犯人逃跑了喵！」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0019"
    $ current_voice = "voice/OKA01A_OKA0019.ogg"
    "伦太郎" "「没事」"
    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0030"
    $ current_voice = "voice/OKA01A_FEI0030.ogg"
    "菲利斯" "「但、但是——」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040020"
    $ current_voice = "voice/OKA01A_Y040020.ogg"
    "巴士劫持犯" "「这个混账怪人！给我记住了——？嗯，这个声音是——」"
    window hide

    play se "SGSE126L" loop


    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC02"),"True","lh/FEI_BMC02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("Y04")
    play voc "OKA01A_Y040021"
    $ current_voice = "voice/OKA01A_Y040021.ogg"
    "巴士劫持犯" "「警察！？」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0020"
    $ current_voice = "voice/OKA01A_OKA0020.ogg"
    "伦太郎" "「哈哈哈哈！我早就提前报警了！来吧，随你们逃到天涯海角！！」"
    $ stopvoc("Y04")
    play voc "OKA01A_Y040022"
    $ current_voice = "voice/OKA01A_Y040022.ogg"
    "巴士劫持犯" "「给、给我记住了！！」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0021"
    $ current_voice = "voice/OKA01A_OKA0021.ogg"
    "伦太郎" "「反正３０分钟后就会被抓住」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC04"),"True","lh/FEI_BMC04a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0031"
    $ current_voice = "voice/OKA01A_FEI0031.ogg"
    "菲利斯" "「凶真……？」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0022"
    $ current_voice = "voice/OKA01A_OKA0022.ogg"
    "伦太郎" "「我不是凶真！是羊驼人！」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0023"
    $ current_voice = "voice/OKA01A_OKA0023.ogg"
    "伦太郎" "「你们两个没受伤吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMB01"),"True","lh/FEI_BMB01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA01A_FEI0032"
    $ current_voice = "voice/OKA01A_FEI0032.ogg"
    "菲利斯" "「没受伤喵」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0012"
    $ current_voice = "voice/OKA01A_MAY0012.ogg"
    "真由理" "「工作人员晕倒在驾驶席上，但是没受伤」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0024"
    $ current_voice = "voice/OKA01A_OKA0024.ogg"
    "伦太郎" "「嗯。那么——」"
    "我看着真由理，在面具下露出一个只有她能看到的笑容。"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0025"
    $ current_voice = "voice/OKA01A_OKA0025.ogg"
    "伦太郎" "「下次不要被劫为人质了哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0013"
    $ current_voice = "voice/OKA01A_MAY0013.ogg"
    "真由理" "「嗯，谢谢」"
    window hide
    play se "SGSE347"


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0026"
    $ current_voice = "voice/OKA01A_OKA0026.ogg"
    "伦太郎" "「秋叶原中诞生的正义伙伴羊驼人，就此撤退！哈哈哈哈哈哈！」"
    hide screen phoneSD1
    window hide

    stop bgm 

    stop se

    stop se



    $ loadBG(0,"BG_BLACK",trans=Dissolve(3))
    pause 5
    $ loadBG(0,"BG02A2")


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0027"
    $ current_voice = "voice/OKA01A_OKA0027.ogg"
    "伦太郎" "「就这样在羊驼人的活跃下，秋叶原的和平再一次被维护了！」"
    window hide


    $ loadBG(2,"IBGX007")



    hide screen phonebtn
    play bgm "FD2BGM10"
    $ current_voice = "voice/FD2BGM10.ogg"

    $ stopvoc("Y05")
    play voc "OKA01A_Y050000"
    $ current_voice = "voice/OKA01A_Y050000.ogg"
    "羊驼司令" "「……真无聊」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0028"
    $ current_voice = "voice/OKA01A_OKA0028.ogg"
    "伦太郎" "「你、你说什么！」"
    $ stopvoc("Y05")
    play voc "OKA01A_Y050001"
    $ current_voice = "voice/OKA01A_Y050001.ogg"
    "羊驼司令" "「老实说，我没兴趣」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0029"
    $ current_voice = "voice/OKA01A_OKA0029.ogg"
    "伦太郎" "「你小子这么说是什么意思！今天让我这么干的是你吧！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SCANNING_LINE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SCANNING_LINE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SCANNING_LINE"])
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0030"
    $ current_voice = "voice/OKA01A_OKA0030.ogg"
    "伦太郎" "「不就是个游戏！是个程序！不就是个{color=#f00}扫描线{/color}上反映的信号！」"
label L_RM_OKA1_FEI01_01_RECEIVE_STA:
    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_FEI01_01"]

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0031"
    $ current_voice = "voice/OKA01A_OKA0031.ogg"
    "伦太郎" "「来反抗玩家的意志，真是有胆——」"
    call CHECK_RM_RECEIVE
    $ stopvoc("Y05")
    play voc "OKA01A_Y050002"
    $ current_voice = "voice/OKA01A_Y050002.ogg"
    "羊驼司令" "「真嚣张」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0032"
    $ current_voice = "voice/OKA01A_OKA0032.ogg"
    "伦太郎" "「呜哇啊啊啊啊啊！！」"
    window hide
    play se "SGSE024"

    stop bgm 
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0014"
    $ current_voice = "voice/OKA01A_MAY0014.ogg"
    "真由理" "「嘟嘟噜♪」"
    window hide



    $ loadBG(2,"BG01A",hold=True)




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    $ loadBG(3,"IBG019A",png=True,hide=False)
    hide background-png 
    with dissolve





    play bgm "BGM18"

    show screen phonebtn
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0033"
    $ current_voice = "voice/OKA01A_OKA0033.ogg"
    "伦太郎" "「哦，是真由理啊。打工结束了吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0015"
    $ current_voice = "voice/OKA01A_MAY0015.ogg"
    "真由理" "「嗯。菲利斯扮演的凯拉玲，超有人气哦」"
    call CHECK_RM_RECEIVE
    "嘛，这是当然的。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0034"
    $ current_voice = "voice/OKA01A_OKA0034.ogg"
    "伦太郎" "「话说菲利斯没有发现羊驼人的本尊吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

label L_RM_OKA1_FEI01_01_RECEIVE_END:

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0016"
    $ current_voice = "voice/OKA01A_MAY0016.ogg"
    "真由理" "「当然！羊驼服之力可是很强大的」"
label L_RM_OKA1_FEI01_01_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_FEI01_01"]]["late"]=True

    "我已经决定要作为羊驼人来保卫秋叶原的和平了，为我做羊驼服的就是真由理。"
    "因为我原本就不擅长裁缝这种细致的工作。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0017"
    $ current_voice = "voice/OKA01A_MAY0017.ogg"
    "真由理" "「冈伦还在跟司令对话吗？」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0035"
    $ current_voice = "voice/OKA01A_OKA0035.ogg"
    "伦太郎" "「嗯嗯。桶子刚刚还在时说不了话」"
    window hide


    $ loadBG(2,"IBGX007")



    hide screen phonebtn
    "司令是我眼前这台晶像管显示器中的奇妙生物“羊驼人”的特定名称。"
    "是以前被随便称为“羊驼”“槽泥马”“泥马人”“草人”“尼玛”的羊驼人。"
    "他被亲切地称为“羊驼司令”还是在我成为保卫秋叶原的正义伙伴羊驼人之后。"
    "羊驼司令从未来传递过来的短信和电话，让正义的伙伴羊驼人能够事先知道未来的事情，防范罪恶于未然！"
    "——就是这种设定。"
label L_RM_OKA1_FEI01_02_RECEIVE_STA:
    $ targetmailid = cml.setdefault("RM_OKA_SEND_FEI01","")

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0018"
    $ current_voice = "voice/OKA01A_MAY0018.ogg"
    "真由理" "「嘿嘿。司令，谢谢您今天也在保佑冈伦，嗯嗯」"
    call CHECK_RM_RECEIVE
    $ stopvoc("Y05")
    play voc "OKA01A_Y050003"
    $ current_voice = "voice/OKA01A_Y050003.ogg"
    "羊驼司令" "「哼，哼。你这么感激我也不会有好处的！」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TSUNDERE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TSUNDERE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TSUNDERE"])
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0036"
    $ current_voice = "voice/OKA01A_OKA0036.ogg"
    "伦太郎" "「唔！真由理啊！为什么你总能引出这个{color=#f00}傲娇{/color}的情绪！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0019"
    $ current_voice = "voice/OKA01A_MAY0019.ogg"
    "真由理" "「嗯，可能是因为与司令心意相通吧？」"
label L_RM_OKA1_FEI01_02_RECEIVE_END:

    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0037"
    $ current_voice = "voice/OKA01A_OKA0037.ogg"
    "伦太郎" "「司令也会有心吗！」"
label L_RM_OKA1_FEI01_02_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_FEI02_01"]]["late"]=True

label L_RM_OKA1_RUK01_01_RECEIVE_STA:
    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_RUK01_01"]

    $ LR_RM_CHANCE=9
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0038"
    $ current_voice = "voice/OKA01A_OKA0038.ogg"
    "伦太郎" "「况且，潜入巴士中，装备Ｓａｌｓａ　ｃｏｕｎｔｅｒ在身上，全都是未来的我的记忆——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0020"
    $ current_voice = "voice/OKA01A_MAY0020.ogg"
    "真由理" "「啊，冈伦？羊驼服在什么地方？因为被划开了，要缝补好才行」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0039"
    $ current_voice = "voice/OKA01A_OKA0039.ogg"
    "伦太郎" "「喂，听人说话啊——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0021"
    $ current_voice = "voice/OKA01A_MAY0021.ogg"
    "真由理" "「真由喜我很高兴」"
    window hide
    $ loadBG(0,"IBG018A",png=True,hold=True,hide=False)
    with moveinbottom



    hide screen phonebtn
    call CHECK_RM_RECEIVE
    "真由理自顾自地从我的背包中取出羊驼服，将脸埋在其中。"
    window hide

    show screen phonebtn
    hide background-png 
    with dissolve
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0022"
    $ current_voice = "voice/OKA01A_MAY0022.ogg"
    "真由理" "「因为冈伦都不太穿ｃｏｓ服，看着你穿羊驼服，让我觉得做出来很值得」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA01A_MAY0023"
    $ current_voice = "voice/OKA01A_MAY0023.ogg"
    "真由理" "「我早就在期待羊驼人什么时候能够救出被当成人质的真由喜了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0040"
    $ current_voice = "voice/OKA01A_OKA0040.ogg"
    "伦太郎" "「……这、这样啊」"

    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0041"
    $ current_voice = "voice/OKA01A_OKA0041.ogg"
    "伦太郎" "「呼，怎么会有让你被别人抓住这种事！」"
label L_RM_OKA1_RUK01_01_RECEIVE_END:

    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0042"
    $ current_voice = "voice/OKA01A_OKA0042.ogg"
    "伦太郎" "「因为啊，真由理可是我的人质啊！哈哈哈！」"
label L_RM_OKA1_RUK01_01_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK01_01"]]["late"]=True

    window hide
    stop bgm 
    play se "SGSE024"

    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0000"
    $ current_voice = "voice/OKA01A_DAR0000.ogg"
    "至" "「冈伦怎么了？干嘛戴个面具？」"
    hide screen phoneSD1
    window hide



    $ loadBG(2,"BG01A",hold = True)


    $ loadBG(3,"IBG019A",png=True,hold=True)


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0043"
    $ current_voice = "voice/OKA01A_OKA0043.ogg"
    "伦太郎" "「呜哇！桶、桶子！」"
    window hide
    play se "SGSE056"
    hide background-png 
    with moveouttop
    $ loadBG(0,"IBG017A",png=True,hide=False)

    show screen phoneSD1



    hide screen phonebtn
    "我急急忙忙脱下羊驼面具。 "
    "戴着这个被看见，还真是有点不好意思。"
    window hide
    hide background-png 
    with dissolve

    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0044"
    $ current_voice = "voice/OKA01A_OKA0044.ogg"
    "伦太郎" "「！看见了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0001"
    $ current_voice = "voice/OKA01A_DAR0001.ogg"
    "至" "「看什么？冈伦的大声笑早就看习惯了」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0045"
    $ current_voice = "voice/OKA01A_OKA0045.ogg"
    "伦太郎" "「也、也是呢」"
    play bgm "BGM22"


    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

label L_RM_OKA1_RUK01_02_RECEIVE_STA:
    $ targetmailid = cml.setdefault("RM_OKA_SEND_RUK01","")

    $ LR_RM_CHANCE=9
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0002"
    $ current_voice = "voice/OKA01A_DAR0002.ogg"
    "至" "「话说……难、难道冈伦，那个面具——」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KEMONOUR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KEMONOUR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KEMONOUR"])
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0003"
    $ current_voice = "voice/OKA01A_DAR0003.ogg"
    "至" "「{color=#f00}兽耳控{/color}觉醒了！？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0046"
    $ current_voice = "voice/OKA01A_OKA0046.ogg"
    "伦太郎" "「兽耳控？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIGURUMUR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIGURUMUR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIGURUMUR"])
    pause 1
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOKO"])

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0004"
    $ current_voice = "voice/OKA01A_DAR0004.ogg"
    "至" "「最近突然成为新闻话题的羊驼人之类的。而且还拿着缝纫工具？突然进入{color=#f00}人偶人{/color}这种上级课程不太好吧{color=#f00}常考{/color}」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0047"
    $ current_voice = "voice/OKA01A_OKA0047.ogg"
    "伦太郎" "「……你在说什么我完全不明白」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUFFALOES"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUFFALOES"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BUFFALOES"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BELLA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BELLA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BELLA"])

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0005"
    $ current_voice = "voice/OKA01A_DAR0005.ogg"
    "至" "「顺带一提我想推的兽是{color=#f00}Ｒｏｌｌｉｎｇ　Ｂｕｆｆａｌｏｓ{/color}的吉祥物，{color=#f00}水牛贝菈{/color}」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIN_BOOK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIN_BOOK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_THIN_BOOK"])
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0006"
    $ current_voice = "voice/OKA01A_DAR0006.ogg"
    "至" "「就是靠着这种像小学生机器牛一样的细分，{color=#f00}小薄本{/color}也会变厚……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0048"
    $ current_voice = "voice/OKA01A_OKA0048.ogg"
    "伦太郎" "「不知道这种角色」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA12"),"True","lh/DAR_ASA12a~ipad.png") as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0007"
    $ current_voice = "voice/OKA01A_DAR0007.ogg"
    "至" "「哼！」"
label L_RM_OKA1_RUK01_02_RECEIVE_END:

label L_RM_OKA1_RUK01_02_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_RUK02_01"])

    window hide
    play se "SGSE110"



    $ loadBG(2,"BG03A4")



    "桶子的眼镜反着光，以超越人类的行动速度，穿过我的身边刷的一声坐在电脑桌前（桶子曰“驾驶席”）。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SSD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SSD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SSD"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MOUSEPAD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MOUSEPAD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MOUSEPAD"])
    "打开搭载{color=#f00}ＳＳＤ{/color}的超高速电脑，手指立刻就在键盘上敲打起来，鼠标与鼠标垫摩擦似乎会喷出火来，{color=#f00}欧派鼠标垫{/color} "
    "最后那个不是重点。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0008"
    $ current_voice = "voice/OKA01A_DAR0008.ogg"
    "至" "「冈伦！这就是水牛贝菈！！」"
    window hide


    $ loadBG(2,"IBG013A")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0049"
    $ current_voice = "voice/OKA01A_OKA0049.ogg"
    "伦太郎" "「啊，啊啊」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0050"
    $ current_voice = "voice/OKA01A_OKA0050.ogg"
    "伦太郎" "「的确很可爱——」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUNKA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUNKA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KUNKA"])
    pause 1
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PRPR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PRPR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PRPR"])

    $ stopvoc("DAR")
    play DAR "OKA01A_DAR0009"
    $ current_voice = "voice/OKA01A_DAR0009.ogg"
    "至" "「不错不错，这个姿势……里面的人什么的根本不存在！快变成非人类也好哦……美人哦，哈哈{color=#f00}咕哈咕哈{/color}{color=#f00}ｐｒｐｒ{/color}」"
    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0051"
    $ current_voice = "voice/OKA01A_OKA0051.ogg"
    "伦太郎" "「桶子，不要舔屏幕」"
    window hide


    $ loadBG(2,"BG03A4")



    show screen phonebtn
    "这里还是让桶子稍微分散一下注意力比较好吧。"
    "如果继续追问带着羊驼人面具的原因的话，反而会变得更麻烦。"
label L_MAIL_RECEIVE_00:
    stop bgm 
    stop se
    stop se

    hide screen phonebtn
    hide screen phonebtn2

    $ targetmailid = gc["ScriptMacros"]["FM_OKA01A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""


    "手机来了短信。"

label L_MAIL_VIEW_00:
    window hide


    call read_last_mail






    play bgm "BGM11"

    "闪光的指压师(Ｓｈｉｎｉｎｇ　Ｆｉｎｇｅｒ)、桐生萌郁。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HEN_PRO"])
    "在{color=#f00}编Ｐｒｏ{/color}的她在『ark rewrite』打工，现在似乎担任秋叶原自由杂志的编辑。"
    "正值保护秋叶原的本地英雄羊驼人成为杂志的头条之时，她正疯狂地想要揭露羊驼人的本尊。"
    "本来，靠着Ｄｍａｉｌ和时间机器，我就完全不用担心本尊会被暴露。"
    "反正失败的话，再来一次就行了。"
    "知道我秘密的只有真由理…… "
    window hide
    call hide_phone



    $ stopvoc("OKA")
    play OKA "OKA01A_OKA0053"
    $ current_voice = "voice/OKA01A_OKA0053.ogg"
    "伦太郎" "「咦？」"
    "说起来，真由理从刚刚开始就不见了。"
    "我的手上还拿着羊驼服，她究竟是去什么地方了……？"

    hide screen phoneSD1
    window hide

    stop bgm 

    stop se

    stop se
    $ loadBG(0,"BG_BLACK",trans=Fade(2,2,0))






    return
label IMTHD_OKA_01:



    play bgm "FD2BGM03"
    $ current_voice = "voice/FD2BGM03.ogg"

    return
