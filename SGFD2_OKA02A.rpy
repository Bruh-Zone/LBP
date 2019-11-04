label SGFD2_OKA02A:


    window hide



    $ loadBG(0,"BG05A1",trans=Fade(0.1,0.1,0.1,color="fff"))







    play se "SGSE024"






    play bgm "BGM05"





    $ date="8/11"
    $ day = "THU"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0000"
    $ current_voice = "voice/OKA02A_OKA0000.ogg"
    "伦太郎" "「呼哇哇……啊……嗯……嗯……」"
    "盛夏的太阳早就已经温暖了空气。"
    "或者说是炎热。湿气也很重。让人很不舒服。"
    "就在揉着睡眼走下楼梯时，我感觉有急促的脚步声正在接近。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0000"
    $ current_voice = "voice/OKA02A_NAE0000.ogg"
    "绹" "「早上好，冈伦叔叔！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0001"
    $ current_voice = "voice/OKA02A_OKA0001.ogg"
    "伦太郎" "「嗯……早、早上好小动物」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0000"
    $ current_voice = "voice/OKA02A_TEN0000.ogg"
    "天王寺" "「喂，冈部！来太晚了！」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    play se "SGSE348"
    with Fade(0.1,0.1,0.1,color="fff")




    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0002"
    $ current_voice = "voice/OKA02A_OKA0002.ogg"
    "伦太郎" "「好痛啊啊啊啊啊！！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0003"
    $ current_voice = "voice/OKA02A_OKA0003.ogg"
    "伦太郎" "「你、你在干什么啊Ｍｒ．布朗！」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0001"
    $ current_voice = "voice/OKA02A_TEN0001.ogg"
    "天王寺" "「你嚣张什么！马上就到该出门的时间了」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0004"
    $ current_voice = "voice/OKA02A_OKA0004.ogg"
    "伦太郎" "「我也是有事情的！我为了不迟到，特意还住在这里了！」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0002"
    $ current_voice = "voice/OKA02A_TEN0002.ogg"
    "天王寺" "「啊？这种牢骚等交了房租后再说」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0005"
    $ current_voice = "voice/OKA02A_OKA0005.ogg"
    "伦太郎" "「唔唔唔唔唔……！」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0003"
    $ current_voice = "voice/OKA02A_TEN0003.ogg"
    "天王寺" "「嗯？怎么？还敢发牢骚——！」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0001"
    $ current_voice = "voice/OKA02A_NAE0001.ogg"
    "绹" "「爸、爸爸……时间就快……」"
label L_RM_OKA1_SUZ01_01_RECEIVE_STA:
    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]

    $ LR_RM_CHANCE=1

    call CHECK_RM_RECEIVE
label L_RM_OKA1_SUZ01_01_RECEIVE_END:


    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0004"
    $ current_voice = "voice/OKA02A_TEN0004.ogg"
    "天王寺" "「嗯，抱歉绹！这样啊！都没时间了，抱歉啊」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0005"
    $ current_voice = "voice/OKA02A_TEN0005.ogg"
    "天王寺" "「可恶！要不是我有一件一定要去做的事情，我就能一直跟着你了……」"
    window hide
    hide lh6  with dissolve
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0006"
    $ current_voice = "voice/OKA02A_TEN0006.ogg"
    "天王寺" "「冈部，听好了！如果你敢让绹哭的话，我可不会轻饶你哦！从头到尾，都要照顾好哦！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0006"
    $ current_voice = "voice/OKA02A_OKA0006.ogg"
    "伦太郎" "「作为补偿，如果能顺利地买到的话，就按照之前说好的给这个月的房租打折啊！」"
    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0007"
    $ current_voice = "voice/OKA02A_TEN0007.ogg"
    "天王寺" "「知道了！好了，快点去吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA02A_TEN0008"
    $ current_voice = "voice/OKA02A_TEN0008.ogg"
    "天王寺" "「绹也要乖乖地跟着去哦」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0002"
    $ current_voice = "voice/OKA02A_NAE0002.ogg"
    "绹" "「好！」"
    "就这样，为了降低Ｌａｂ的房租，我一早就要陪着绹去买东西。"
label L_RM_OKA1_SUZ01_01_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"])

    hide screen phoneSD1
    window hide
    stop bgm 



    $ loadBG(0,"BG22B0")
label L_RM_OKA1_SUZ01_02_RECEIVE_STA:
    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ01","")

    $ LR_RM_CHANCE=1

    call CHECK_RM_RECEIVE
label L_RM_OKA1_SUZ01_02_RECEIVE_END:


    play bgm "BGM26"

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0007"
    $ current_voice = "voice/OKA02A_OKA0007.ogg"
    "伦太郎" "「啊……？」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0003"
    $ current_voice = "voice/OKA02A_NAE0003.ogg"
    "绹" "「啊……」"
    "友都八喜（译注：日本大型连锁购物中心）前面已经排起了长长的队伍。"
    "雷ＮＥＴＡＢ３Ｄ已经热门到足以成为社会现象了。"
    "无论再怎么有人气，开店前一小时排队也应该能买到的，但是……"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0004"
    $ current_voice = "voice/OKA02A_NAE0004.ogg"
    "绹" "「呐，队尾在那里！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0008"
    $ current_voice = "voice/OKA02A_OKA0008.ogg"
    "伦太郎" "「嗯、嗯」"
    window hide



    $ loadBG(0,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0005"
    $ current_voice = "voice/OKA02A_NAE0005.ogg"
    "绹" "「真的，能买到吗？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0009"
    $ current_voice = "voice/OKA02A_OKA0009.ogg"
    "伦太郎" "「啊哈哈哈！小动物你在怀疑什么啊。没什么好担心的」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0006"
    $ current_voice = "voice/OKA02A_NAE0006.ogg"
    "绹" "「但是，排队的人很多哦」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0010"
    $ current_voice = "voice/OKA02A_OKA0010.ogg"
    "绹" "「哼！这么长的队伍，到底是怎么回事！」"
label L_RM_OKA1_SUZ01_02_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"])

    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0011"
    $ current_voice = "voice/OKA02A_OKA0011.ogg"
    "伦太郎" "「无论会遇到什么样的困难，我都一定会买到游戏的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0007"
    $ current_voice = "voice/OKA02A_NAE0007.ogg"
    "绹" "「……好担心」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0012"
    $ current_voice = "voice/OKA02A_OKA0012.ogg"
    "伦太郎" "「别小看我。我是会遵守约定的男人」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0013"
    $ current_voice = "voice/OKA02A_OKA0013.ogg"
    "伦太郎" "「我绝对不会让你哭的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0008"
    $ current_voice = "voice/OKA02A_NAE0008.ogg"
    "绹" "「…………」"
    "小动物用惊讶的眼神看着我。"
    "真是疑心重的家伙……"
label L_RM_OKA1_SUZ01_03_RECEIVE_STA:
    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ02","")

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE
label L_RM_OKA1_SUZ01_03_RECEIVE_END:

label L_RM_OKA1_SUZ01_03_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"])

    "我既有Ｄｍａｉｌ又有时间机器。"
    "就算这条世界线上不能买到游戏，只要再来过就好了。"
    hide screen phoneSD1
    window hide
    hide screen phonebtn

    stop bgm 



    $ loadBG(0,"IBGX048",trans=Fade(1,0,0.5))


    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0009"
    $ current_voice = "voice/OKA02A_NAE0009.ogg"
    "绹" "「啊，刚刚！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0014"
    $ current_voice = "voice/OKA02A_OKA0014.ogg"
    "伦太郎" "「嗯？」"
    window hide


    $ loadBG(2,"BG14A")



    show screen phonebtn
    "绹的一句话让我回过神来。"
    "在我们的前方，有一个男人插了进来。"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0015"
    $ current_voice = "voice/OKA02A_OKA0015.ogg"
    "伦太郎" "「等、等等！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM02"

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0000"
    $ current_voice = "voice/OKA02A_SDO0000.ogg"
    "插队的男人" "「啊？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0016"
    $ current_voice = "voice/OKA02A_OKA0016.ogg"
    "伦太郎" "「混蛋！不准插队！」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0001"
    $ current_voice = "voice/OKA02A_SDO0001.ogg"
    "插队的男人" "「我是被召唤到这里的」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0017"
    $ current_voice = "voice/OKA02A_OKA0017.ogg"
    "伦太郎" "「被召唤的？」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0002"
    $ current_voice = "voice/OKA02A_SDO0002.ogg"
    "被召唤之男" "「你这小子难道没听到吗？那个细声」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0018"
    $ current_voice = "voice/OKA02A_OKA0018.ogg"
    "伦太郎" "「啊？」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0003"
    $ current_voice = "voice/OKA02A_SDO0003.ogg"
    "被低语之男" "「盖亚在说话，命中注定我要排在这里……」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0019"
    $ current_voice = "voice/OKA02A_OKA0019.ogg"
    "伦太郎" "「那是幻听吧。你坑什么人啊？」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0004"
    $ current_voice = "voice/OKA02A_SDO0004.ogg"
    "命中注定在此之男" "「能在这充满坑的街道和时代中生存下来就是Ｔｏｕｇｈ　ｂｏｙ。Ｄｏ　ｙｏｕ　ｔｏｕｇｈ　ｂｏｙ？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0020"
    $ current_voice = "voice/OKA02A_OKA0020.ogg"
    "伦太郎" "「难道不是用『Ａｒｅ　ｙｏｕ』吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0005"
    $ current_voice = "voice/OKA02A_SDO0005.ogg"
    "命中注定在此之男" "「啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0006"
    $ current_voice = "voice/OKA02A_SDO0006.ogg"
    "命中注定在此之男" "「呵……呵呵，语言就是生活。我这种外国人用的ｂｒｅａｋｉｎｇ英语你怎么听得懂？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0021"
    $ current_voice = "voice/OKA02A_OKA0021.ogg"
    "伦太郎" "「『ｂｒｏｋｅｎ』」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0007"
    $ current_voice = "voice/OKA02A_SDO0007.ogg"
    "Braking男" "「我叫４℃！４摄氏度的『４℃』。这是水的密度最高的温度——」"
    "说自己叫４℃的小混混，似乎想要将自己刚刚犯的错误蒙混过去。"
    "但是，我一点兴趣都没有。"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0010"
    $ current_voice = "voice/OKA02A_NAE0010.ogg"
    "绹" "「冈伦叔叔……这个，很奇怪吧？」"
    "小动物藏在我背后，紧紧抓住我的白大褂。"
    "当然我不会就这样无言地忍下去。"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0022"
    $ current_voice = "voice/OKA02A_OKA0022.ogg"
    "伦太郎" "「好了，你还是好好地排到后面去吧」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0008"
    $ current_voice = "voice/OKA02A_SDO0008.ogg"
    "４℃" "「真是顾不自身的井中的青蛙男。就让我来告诉你小子——世界的残酷」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0023"
    $ current_voice = "voice/OKA02A_OKA0023.ogg"
    "伦太郎" "「世界？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0009"
    $ current_voice = "voice/OKA02A_SDO0009.ogg"
    "４℃" "「没错，大伙儿！」"
    $ stopvoc("Y06")
    play voc "OKA02A_Y060000"
    $ current_voice = "voice/OKA02A_Y060000.ogg"
    "４℃的伙伴Ａ" "「哦」"
    $ stopvoc("Y07")
    play voc "OKA02A_Y070000"
    $ current_voice = "voice/OKA02A_Y070000.ogg"
    "４℃的伙伴Ｂ" "「怎么了４℃。有麻烦吗？」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0010"
    $ current_voice = "voice/OKA02A_SDO0010.ogg"
    "４℃" "「嗯嗯，今天是超级霉运日……」"
    "４℃的身后出现了与他同一套派头的男人们。"
    "肯定是同伙不会错。"
    "说起来，这么多这样的家伙同时存在真是让人无法忍受。"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0011"
    $ current_voice = "voice/OKA02A_SDO0011.ogg"
    "４℃" "「这个白大褂男人，说我似乎插了队」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0012"
    $ current_voice = "voice/OKA02A_SDO0012.ogg"
    "４℃" "「我只不过是去趟厕所吧，大伙说对吧？」"
    $ stopvoc("Y06")
    play voc "OKA02A_Y060001"
    $ current_voice = "voice/OKA02A_Y060001.ogg"
    "４℃的伙伴Ａ" "「嗯，没错」"
    $ stopvoc("Y07")
    play voc "OKA02A_Y070001"
    $ current_voice = "voice/OKA02A_Y070001.ogg"
    "４℃的伙伴Ｂ" "「还拜托你去买东西了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0013"
    $ current_voice = "voice/OKA02A_SDO0013.ogg"
    "４℃" "「就是这样」"
    play se "SGSE337"
    "４℃一边看着这里，一边将便利店袋子递给他们俩。"
    window hide
    stop se
    $ loadBG(0,"IBG015A",png=True,hide=False,trans=moveinbottom)


    hide screen phonebtn
    "满脸得意地从中拿出来的是油炸油炸君。"
    $ stopvoc("Y06")
    play voc "OKA02A_Y060002"
    $ current_voice = "voice/OKA02A_Y060002.ogg"
    "４℃的伙伴Ａ" "「这、这个爆好吃……」"
    $ stopvoc("Y07")
    play voc "OKA02A_Y070002"
    $ current_voice = "voice/OKA02A_Y070002.ogg"
    "４℃的伙伴Ｂ" "「光是看着就不停地流口水……」"
    window hide
    hide background-png 
    with moveoutbottom

    show screen phonebtn
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0014"
    $ current_voice = "voice/OKA02A_SDO0014.ogg"
    "４℃" "「所以，我有站在这里的权利。知道了吗，青蛙男？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0024"
    $ current_voice = "voice/OKA02A_OKA0024.ogg"
    "伦太郎" "「我有异议！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0025"
    $ current_voice = "voice/OKA02A_OKA0025.ogg"
    "伦太郎" "「如果是去上厕所，没有必要特意去便利店。」"
    "４℃买回来的是油炸油炸君。"
    "虽然真由理时不时也会买来吃，但是秋叶原中很少有便利店。"
    "必须要走到车站附近的地方才会有。"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0026"
    $ current_voice = "voice/OKA02A_OKA0026.ogg"
    "伦太郎" "「你只不过是从家到这里的路上，顺路去了便利店而已。根本没有在这里排队！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0015"
    $ current_voice = "voice/OKA02A_SDO0015.ogg"
    "４℃" "「你说什么？」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0016"
    $ current_voice = "voice/OKA02A_SDO0016.ogg"
    "４℃" "「不知天高地厚的青蛙男。你说我这个Ｌｉｅｒ在Ｌｉｅ吗？啊？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0027"
    $ current_voice = "voice/OKA02A_OKA0027.ogg"
    "伦太郎" "「当然，我不会容忍这种不正当的行为」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0017"
    $ current_voice = "voice/OKA02A_SDO0017.ogg"
    "４℃" "「……看来」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DMA01"),"True","lh/SDO_DMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "４℃按着指关节向前踏出一步。"
    "就好像谁叫了一声似的，周围的人全都拉开了距离。"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0018"
    $ current_voice = "voice/OKA02A_SDO0018.ogg"
    "４℃" "「看来语言已经无法沟通了」"
    $ stopvoc("Y06")
    play voc "OKA02A_Y060003"
    $ current_voice = "voice/OKA02A_Y060003.ogg"
    "４℃的伙伴Ａ" "「４℃，上吗？」"
    $ stopvoc("Y07")
    play voc "OKA02A_Y070003"
    $ current_voice = "voice/OKA02A_Y070003.ogg"
    "４℃的伙伴Ｂ" "「但是，在大街上——」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0019"
    $ current_voice = "voice/OKA02A_SDO0019.ogg"
    "４℃" "「没关系。只要我一跳舞，什么地方都是最好的舞台」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DMA02"),"True","lh/SDO_DMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0020"
    $ current_voice = "voice/OKA02A_SDO0020.ogg"
    "４℃" "「——喂，上啊。如果想成为Ｓｐｏｔｌｉｇｈｔ下的主角的话！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0028"
    $ current_voice = "voice/OKA02A_OKA0028.ogg"
    "伦太郎" "「正合我意」"
    "面对４℃的挑衅，我向前迈出一步。"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0011"
    $ current_voice = "voice/OKA02A_NAE0011.ogg"
    "绹" "「冈伦叔叔，不行！」 "
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0029"
    $ current_voice = "voice/OKA02A_OKA0029.ogg"
    "伦太郎" "「没事，绝对不会输的」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0030"
    $ current_voice = "voice/OKA02A_OKA0030.ogg"
    "伦太郎" "「因为——我是正义的伙伴」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0012"
    $ current_voice = "voice/OKA02A_NAE0012.ogg"
    "绹" "「正义的伙伴……？」"
    "绹歪着头一幅难以置信的样子。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DMA02"),"True","lh/SDO_DMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    "我把她拉到身后，保护着她。"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0031"
    $ current_voice = "voice/OKA02A_OKA0031.ogg"
    "伦太郎" "「啊哈哈哈！我就接受３℃你发出来的挑战」"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0021"
    $ current_voice = "voice/OKA02A_SDO0021.ogg"
    "４℃" "「不是３℃……是４℃啊啊啊啊啊啊————！！」"
    hide screen phoneSD1
    window hide
    stop bgm



    play se "SGSE349"

    python:
        loadBG(0,"IBGX048",trans=
            Fade(0.5,3,0.5))
    hide screen phonebtn
    show screen phoneSD1
    stop se
    "——１０分钟后。"
    window hide



    $ loadBG(2,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM22"

    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0013"
    $ current_voice = "voice/OKA02A_NAE0013.ogg"
    "绹" "「冈伦叔叔，没事吧？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0032"
    $ current_voice = "voice/OKA02A_OKA0032.ogg"
    "伦太郎" "「啊、嗯嗯，完全没事……好痛啊啊啊！！」"
    "我将身体靠在墙壁上，才能勉强站立起来。"
label L_RM_OKA1_FEI02_01_RECEIVE_STA:
    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    "总觉得４℃已经习惯了打架。"
    call CHECK_RM_RECEIVE
    "相反我却不能靠变身来与他们对抗。"
    call CHECK_RM_RECEIVE
    "说到底羊驼人还是人啊。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    "羊驼服只是真由理亲手做的{color=#f00}Ｃｏｓｐｌａｙ{/color}服，并没有办法来提升身体能力。"
    call CHECK_RM_RECEIVE
    "羊驼人唯一的弱点，那就是——如果不知道未来的话，什么也做不到。"
    call CHECK_RM_RECEIVE
    "依靠着穿越时空获得未来的知识，用知识和勇气掩盖身体的弱点，羊驼人才得以作为正义的伙伴来行动着。"
label L_RM_OKA1_FEI02_01_RECEIVE_END:

    "也就是说，在不知道未来会怎样的现在，变身成羊驼人也没用。"
label L_RM_OKA1_FEI02_01_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"])

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0014"
    $ current_voice = "voice/OKA02A_NAE0014.ogg"
    "绹" "「明明很弱还要逞强」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0033"
    $ current_voice = "voice/OKA02A_OKA0033.ogg"
    "伦太郎" "「小动物啊，你完全不知道『真正的强大』是什么」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0034"
    $ current_voice = "voice/OKA02A_OKA0034.ogg"
    "伦太郎" "「所谓真正的强大就是——百折不挠的心！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0015"
    $ current_voice = "voice/OKA02A_NAE0015.ogg"
    "绹" "「百折不挠……？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0035"
    $ current_voice = "voice/OKA02A_OKA0035.ogg"
    "伦太郎" "「不是说腕力。而是靠内心中的强大信念，开辟未来！呼哈哈哈，好痛，好痛啊啊啊……！！」"
    "唔，笑起来都很痛……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

label L_RM_OKA1_FEI02_02_RECEIVE_STA:
    $ targetmailid = cml.setdefault("RM_OKA_SEND_FEI03","")

    $ LR_RM_CHANCE=20
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0016"
    $ current_voice = "voice/OKA02A_NAE0016.ogg"
    "绹" "「那，冈伦叔叔，如果不屈不挠地去排队的话，还能买到吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0036"
    $ current_voice = "voice/OKA02A_OKA0036.ogg"
    "伦太郎" "「啊，嗯嗯。是呢……」"

    stop bgm 
    call CHECK_RM_RECEIVE
    "我们因为打架，而暂时离开了队伍。"
    call CHECK_RM_RECEIVE
    "最后重新排在队末，能不能买到游戏还是未知数……"
    call CHECK_RM_RECEIVE
    "４℃那边也在担心这个问题。"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0037"
    $ current_voice = "voice/OKA02A_OKA0037.ogg"
    "伦太郎" "「嗯……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play bgm "BGM07"

    call CHECK_RM_RECEIVE
    "再次看向队伍，我突然感觉到一种违和感。"
    call CHECK_RM_RECEIVE
    "虽然雷Ｎｅｔ翔受到很多年龄层的支持，但是主要客户群还是年轻人。"
    call CHECK_RM_RECEIVE
    "特别对这种在便携式游戏机上的雷ＮｅｔＡＢ３Ｄ更为显著。"
    call CHECK_RM_RECEIVE
    "现在排在我们身边的基本都是小孩子。"
    call CHECK_RM_RECEIVE
    "可是队伍的一大半，特别是前面的大半都是大人。"
    call CHECK_RM_RECEIVE
    "而且看起来几乎都是平时不怎么玩游戏的人。"
    call CHECK_RM_RECEIVE
    "也许像４℃这样的人，竟然还是一流的雷ＮｅｔＡＢ玩家也说不定。"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0038"
    $ current_voice = "voice/OKA02A_OKA0038.ogg"
    "伦太郎" "「……哎呀，不对」"
    call CHECK_RM_RECEIVE
    "如果有便携式游戏机的话，排队的时候应该会拿出来打发时间。"
    call CHECK_RM_RECEIVE
    "但是，大人们基本没有在玩游戏机。"
    call CHECK_RM_RECEIVE
    "这条队伍，总觉得很奇怪……"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0039"
    $ current_voice = "voice/OKA02A_OKA0039.ogg"
    "伦太郎" "「咦？」"
    call CHECK_RM_RECEIVE
    "一个男人按顺序向排着队的大人们发钱。"
    call CHECK_RM_RECEIVE
    "这究竟是……？"
label L_RM_OKA1_FEI02_02_RECEIVE_END:

label L_RM_OKA1_FEI02_02_REPLY_END:

    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0017"
    $ current_voice = "voice/OKA02A_NAE0017.ogg"
    "绹" "「冈伦叔叔！队伍前移了！快走！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0040"
    $ current_voice = "voice/OKA02A_OKA0040.ogg"
    "伦太郎" "「哦，嗯……」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG22A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0022"
    $ current_voice = "voice/OKA02A_SDO0022.ogg"
    "４℃" "「最后的一个，到手了！！」"

    play se "SGSE007L" loop
    "不顾队伍后方的怨念的视线，４℃高举最后着一个游戏，放声大笑着。"
    $ stopvoc("SDO")
    play SDO "OKA02A_SDO0023"
    $ current_voice = "voice/OKA02A_SDO0023.ogg"
    "４℃" "「你们有像我这样就算有可能买不到也还是要排队的觉悟吗？呵呵呵呵！！哈哈哈哈！！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0041"
    $ current_voice = "voice/OKA02A_OKA0041.ogg"
    "伦太郎" "「什么『继续排』啊。明明是中途插队」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0018"
    $ current_voice = "voice/OKA02A_NAE0018.ogg"
    "绹" "「呜……呜……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0042"
    $ current_voice = "voice/OKA02A_OKA0042.ogg"
    "伦太郎" "「嗯？怎么了？」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0019"
    $ current_voice = "voice/OKA02A_NAE0019.ogg"
    "绹" "「果、果然……买不到了吗？」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0020"
    $ current_voice = "voice/OKA02A_NAE0020.ogg"
    "绹" "「哇，呜呜呜呜…………」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0043"
    $ current_voice = "voice/OKA02A_OKA0043.ogg"
    "伦太郎" "「啊啊，别哭别哭。没事的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0021"
    $ current_voice = "voice/OKA02A_NAE0021.ogg"
    "绹" "「才不是没事！因为，我们从早上开始，就、就一直排着的！」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0022"
    $ current_voice = "voice/OKA02A_NAE0022.ogg"
    "绹" "「然后没有放弃，还继续排下去了……冈伦叔叔，你是大骗子！」"
    "的确就像绹说的一样，这样下去我真的是骗子了。"
    "原本最早就是由于我睡过了头导致的，好不容易感觉补救到了……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0023"
    $ current_voice = "voice/OKA02A_NAE0023.ogg"
    "绹" "「呜呜，呜……呜呜呜……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "绹的眼泪渐渐地传染给了周围的少年少女。"
    "虽然陪在一旁的大人们都在拼命地安慰，但是完全没办法让他们停下来。"
    window hide

    stop se
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我无意识中拿出了手机。"
    "如果使用Ｄｍａｉｌ或者穿越时空回到过去干涉的话，又会走向一个不同的未来吧。"
    "但是——"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0044"
    $ current_voice = "voice/OKA02A_OKA0044.ogg"
    "伦太郎" "「…………」"
    "只是为了这种事就改变过去好吗？"
    "时间机器不是应该用在更重要的事上吗？"
    "况且以前也做了无法回头的事情……"
    "咦……？"
    "无法回头的事情……？"
    "那究竟是……"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0024"
    $ current_voice = "voice/OKA02A_NAE0024.ogg"
    "绹" "「冈伦叔叔……？」"
    "我回过神来，看到了小动物正泪汪汪地仰视着我。"
    "可恶，忍不了了！"
    "这样的话——"
    window hide
    play bgm "FD2BGM01"




    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0045"
    $ current_voice = "voice/OKA02A_OKA0045.ogg"
    "伦太郎" "「是我。「东西」到手了吗？好，现在立刻去拿。啊？你在说什么啊？你也想回到故乡，看看儿子的脸吧？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0046"
    $ current_voice = "voice/OKA02A_OKA0046.ogg"
    "伦太郎" "「３０分钟。只要能坚持这么久的话，后面就交给我了。你只要考虑保护好「东西」就行了。知道吗！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0047"
    $ current_voice = "voice/OKA02A_OKA0047.ogg"
    "伦太郎" "「为了命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)无法引导的东西。Ｅｌ　Ｐｓｙ　Ｃｏｎｇｒｏｏ」"
    window hide
    hide screen phonemenu
    call hide_phone


    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0025"
    $ current_voice = "voice/OKA02A_NAE0025.ogg"
    "绹" "「冈伦叔叔？」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0048"
    $ current_voice = "voice/OKA02A_OKA0048.ogg"
    "伦太郎" "「好消息！我从某个渠道得到了能到手游戏的情报」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0026"
    $ current_voice = "voice/OKA02A_NAE0026.ogg"
    "绹" "「诶……真的吗！？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0049"
    $ current_voice = "voice/OKA02A_OKA0049.ogg"
    "伦太郎" "「你先回{color=#f00}显像管工房{/color}等着就行！」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0027"
    $ current_voice = "voice/OKA02A_NAE0027.ogg"
    "绹" "「那，我也想一起——」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0050"
    $ current_voice = "voice/OKA02A_OKA0050.ogg"
    "伦太郎" "「再见小动物！要小心车！呼哈哈哈哈！！」"
    $ stopvoc("NAE")
    play NAE "OKA02A_NAE0028"
    $ current_voice = "voice/OKA02A_NAE0028.ogg"
    "绹" "「冈、冈伦叔叔……！！」"
    window hide


    $ loadBG(2,"BG14A")



    "如果带上她的话，所有的东西就都暴露了。"
    "我就像从绹身边逃开一样，在秋叶原的街道上奔跑着。"
    "这是世界第一的「电器街」秋叶原。"
    "如果淀桥不行的话，在街上应该能找到——"
    hide screen phoneSD1
    hide screen phonebtn
    window hide

    stop bgm 




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"BG03A4",trans=Fade(0.5,3,0.5),hide=False)


    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0000"
    $ current_voice = "voice/OKA02A_DAR0000.ogg"
    "至" "「我也有过会这么想的时候」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0051"
    $ current_voice = "voice/OKA02A_OKA0051.ogg"
    "伦太郎" "「桶子！别开玩笑！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0001"
    $ current_voice = "voice/OKA02A_DAR0001.ogg"
    "至" "「声音太大的话楼下会听见的」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0052"
    $ current_voice = "voice/OKA02A_OKA0052.ogg"
    "伦太郎" "「咕噜噜」"
    play bgm "BGM19"
    "在秋叶原中跑来跑去，结果还是没找到「雷ＮＥＴＡＢ３Ｄ」。"
    "都说了那种话了，现在实在是没脸去见楼下的绹。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAKAR"])
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0053"
    $ current_voice = "voice/OKA02A_OKA0053.ogg"
    "伦太郎" "「拜托了，{color=#f00}超级嗨客{/color}！除了你之外我已经没有任何能求助的人了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0002"
    $ current_voice = "voice/OKA02A_DAR0002.ogg"
    "至" "「超级黑客」"
    window hide


    $ loadBG(2,"IBG014A")



    hide screen phonebtn
    "虽然一边在不耐烦地订正，但是桶子没有停下手里的活。"
    "同时操作着鼠标和键盘，以令人惊讶的速度浏览着大量打开的网页。"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0003"
    $ current_voice = "voice/OKA02A_DAR0003.ogg"
    "至" "「但是，嗯……真不愧是高人气，已经不能用商品来形容了」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0054"
    $ current_voice = "voice/OKA02A_OKA0054.ogg"
    "伦太郎" "「网上也找不到吗？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0004"
    $ current_voice = "voice/OKA02A_DAR0004.ogg"
    "至" "「量贩店都卖完了。小商店似乎也全灭了。{color=#f00}＠ｃｈａｎｎｅｌ{/color}上都是哀声载道」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"])
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0055"
    $ current_voice = "voice/OKA02A_OKA0055.ogg"
    "伦太郎" "「{color=#f00}Ｔａｂｏｏ！Ａｕｃｔｉｏｎ{/color}呢！？」"
    window hide


    $ loadBG(2,"IBG014B")



    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0005"
    $ current_voice = "voice/OKA02A_DAR0005.ogg"
    "至" "「哦，这个还有十分钟成交」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0056"
    $ current_voice = "voice/OKA02A_OKA0056.ogg"
    "伦太郎" "「哦哦，而且还是定价的一半，真是太棒了！那赶紧出价——」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0006"
    $ current_voice = "voice/OKA02A_DAR0006.ogg"
    "至" "「冈伦，真的好吗？还是看仔细比较好」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0057"
    $ current_voice = "voice/OKA02A_OKA0057.ogg"
    "伦太郎" "「看仔细……？」"
    "我靠近屏幕，死死地盯着网拍的画面。"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0058"
    $ current_voice = "voice/OKA02A_OKA0058.ogg"
    "伦太郎" "「…………价格，多了一位？」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0007"
    $ current_voice = "voice/OKA02A_DAR0007.ogg"
    "至" "「正确」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0059"
    $ current_voice = "voice/OKA02A_OKA0059.ogg"
    "伦太郎" "「怎么可能！！这是有组织的阴谋吗！？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TENBUYER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TENBUYER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TENBUYER"])
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0008"
    $ current_voice = "voice/OKA02A_DAR0008.ogg"
    "至" "「虽不中亦不远矣。也就是所谓的{color=#f00}转卖屋{/color}」"
    window hide



    $ loadBG(2,"BG03A4",hold=True)
    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0060"
    $ current_voice = "voice/OKA02A_OKA0060.ogg"
    "伦太郎" "「转卖屋？」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0009"
    $ current_voice = "voice/OKA02A_DAR0009.ogg"
    "至" "「没错。买入可能会断货的东西，以高价在网拍上出售。为此，特意雇人排队」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DQN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DQN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DQN"])
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0010"
    $ current_voice = "voice/OKA02A_DAR0010.ogg"
    "至" "「冈伦你也看见了吧？网络攻击之类的，那个{color=#f00}ＤＱＮ{/color}军团也在用这个」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0061"
    $ current_voice = "voice/OKA02A_OKA0061.ogg"
    "伦太郎" "「不、不会吧！」"
    hide screen phoneSD1
    window hide



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"BG14A",hide=False,hold=True)
    with Fade(0.2,0.5,0.2,color="fff")


    hide screen phonebtn
    "我的脑海中浮现了４℃今天早上插队的样子。"
    "那家伙果然不是因为想玩游戏才在那里排队的……"
    "不对，不单是那家伙。"
    window hide


    $ loadBG(0,"BG22B0",trans=Fade(0.2,0.5,0.2,color="fff"))

    "排在队伍前面的人，基本都是看起来平时不玩游戏的人。"
    "而且他们在买商品时，还从头目样子的人那里拿到了钱。"
    "这么说来，那些人果然是转卖屋雇来排队的临时工……？"
    window hide


    $ loadBG(0,"BG03A4",hold=True)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Fade(0.2,0.5,0.2,color="fff")


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0062"
    $ current_voice = "voice/OKA02A_OKA0062.ogg"
    "伦太郎" "「不、不可原谅。因为那些人，我们买不到东西这种事……」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0063"
    $ current_voice = "voice/OKA02A_OKA0063.ogg"
    "伦太郎" "「说起来面向对象是孩子吧？就算出网拍也卖不出东西」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOJAKU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOJAKU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOJAKU"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])

    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0011"
    $ current_voice = "voice/OKA02A_DAR0011.ogg"
    "至" "「{color=#f00}情弱{/color}{color=#f00}乙{/color}买雷ＮｅｔＡＢ３Ｄ的又不是他们自己。如果向爷爷奶奶恳求的话怎么办？」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0012"
    $ current_voice = "voice/OKA02A_DAR0012.ogg"
    "至" "「因为是可爱孙子的恳求，就算稍微贵一点也没有关系」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0064"
    $ current_voice = "voice/OKA02A_OKA0064.ogg"
    "伦太郎" "「但是，这种交易怎么能信」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0013"
    $ current_voice = "voice/OKA02A_DAR0013.ogg"
    "至" "「嗯，也不能一概而论。你看这个交易记录」"
    window hide


    $ loadBG(2,"IBG014C")



    hide screen phonebtn
    "桶子打开卖家的档案。"
    "我扫了一眼交易历史——"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0065"
    $ current_voice = "voice/OKA02A_OKA0065.ogg"
    "伦太郎" "「想不到评价还挺好……」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0014"
    $ current_voice = "voice/OKA02A_DAR0014.ogg"
    "至" "「被交易对象缠上才是最麻烦的吧？所以转卖屋主们为了不让对方受骗也在尽全力让交易更顺利」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0015"
    $ current_voice = "voice/OKA02A_DAR0015.ogg"
    "至" "「原本买家如果能接受这个价格才会让交易成立。通过需求与供给的平衡来决定价格是资本主义的基本原则」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0016"
    $ current_voice = "voice/OKA02A_DAR0016.ogg"
    "至" "「无法去特定的地方才导致这种区域差别。也不能过早地判断这种事情就是坏事」"
    window hide



    $ loadBG(2,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0066"
    $ current_voice = "voice/OKA02A_OKA0066.ogg"
    "伦太郎" "「唔、唔。不过……」 "
    "的确，我也不是不明白桶子说的话。"
    "但是，不过。"
    "总觉心里有些不舒服——"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0067"
    $ current_voice = "voice/OKA02A_OKA0067.ogg"
    "伦太郎" "「唔，我果然还是不能接受！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0068"
    $ current_voice = "voice/OKA02A_OKA0068.ogg"
    "伦太郎" "「如果买家能更便宜的购入商品，就能将剩下的钱用去买其他游戏！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0069"
    $ current_voice = "voice/OKA02A_OKA0069.ogg"
    "伦太郎" "「另一方卖家如果能以更低的价格出售商品的话，就能卖掉更多的商品！」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0070"
    $ current_voice = "voice/OKA02A_OKA0070.ogg"
    "伦太郎" "「但是中间夹入转卖屋的话，两者的利益都被损害了！」"
    $ stopvoc("DAR")
    play DAR "OKA02A_DAR0017"
    $ current_voice = "voice/OKA02A_DAR0017.ogg"
    "至" "「嘛，这也是一种解释」"
    "我之所以没买到游戏，就是因为转卖屋雇用的４℃为了自己赚钱而插了我的队。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG22A",trans=Fade(0.2,0.5,0.2,color="fff"))

    hide screen phonebtn
    "我的脑海中出现了因没有买到游戏而大声哭叫的孩子们。"
    "一部分的大人为了自己的利益，去抢买孩子们的游戏，实在是太没天理了。"
    window hide


    $ loadBG(0,"BG03A4",trans=Fade(0.2,0.5,0.2,color="fff"))

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0071"
    $ current_voice = "voice/OKA02A_OKA0071.ogg"
    "伦太郎" "「绝不放过转卖屋！！」"
    "正义的火焰在我心中燃烧，于是——"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG02E1",trans=Fade(0.5,1,0.5))

    play bgm "FD2BGM08"

    show screen phoneSD1
    "桶子离开Ｌａｂ后，我在只剩我一个人的Ｌａｂ中与司令对话。"
    window hide


    $ loadBG(2,"IBGX007")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0072"
    $ current_voice = "voice/OKA02A_OKA0072.ogg"
    "伦太郎" "「羊驼司令啊」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0073"
    $ current_voice = "voice/OKA02A_OKA0073.ogg"
    "伦太郎" "「我为了正义要回到过去！」"
    $ stopvoc("Y05")
    play voc "OKA02A_Y050000"
    $ current_voice = "voice/OKA02A_Y050000.ogg"
    "羊驼司令" "「呼啊啊……」"
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0074"
    $ current_voice = "voice/OKA02A_OKA0074.ogg"
    "伦太郎" "「唔！我认真的要维护正义，你却——！给我认真地听我说话啊！」"
label L_RM_OKA1_RUK02_01_RECEIVE_STA:
    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]

    $ LR_RM_CHANCE=19
    call CHECK_RM_RECEIVE
    $ stopvoc("Y05")
    play voc "OKA02A_Y050001"
    $ current_voice = "voice/OKA02A_Y050001.ogg"
    "羊驼司令" "「不用听我也知道」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JYKILL_HYDE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JYKILL_HYDE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JYKILL_HYDE"])
    $ stopvoc("Y05")
    play voc "OKA02A_Y050002"
    $ current_voice = "voice/OKA02A_Y050002.ogg"
    "羊驼司令" "「我跟你是{color=#f00}杰基尔博士与海德先生{/color}那样，是同一枚硬币的正反面」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0075"
    $ current_voice = "voice/OKA02A_OKA0075.ogg"
    "伦太郎" "「正反面……？」"
    call CHECK_RM_RECEIVE
    "司令的想法非常地特殊，时不时会说出不明意义的话。"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA02A_MAY0000"
    $ current_voice = "voice/OKA02A_MAY0000.ogg"
    "真由理" "「冈伦！」"
    call CHECK_RM_RECEIVE
    "正沉浸于思考时，突然身后传来了声音。"
    call CHECK_RM_RECEIVE
    "是真由理。"
    window hide



    $ loadBG(2,"BG01E",hold=True)


    $ loadBG(3,"IBG019A",png=True,hold=True)


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    hide background-png 
    with Dissolve(1)





    show screen phonebtn
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA02A_MAY0001"
    $ current_voice = "voice/OKA02A_MAY0001.ogg"
    "真由理" "「咦？你带上这个面具就是说……要出去吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0076"
    $ current_voice = "voice/OKA02A_OKA0076.ogg"
    "伦太郎" "「是啊，为了正义」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA02A_MAY0002"
    $ current_voice = "voice/OKA02A_MAY0002.ogg"
    "真由理" "「嗯，这样啊。正义的伙伴真是辛苦呢」"
    call CHECK_RM_RECEIVE
    "我以羊驼人的身份不停的穿越时空，作为正义的伙伴守护秋叶原，但是知道这点的只有真由理。"
    call CHECK_RM_RECEIVE
    "她能够理解我——就凭这点，就已经帮了我很大的忙了。"
    call CHECK_RM_RECEIVE
    "能这样将活动继续下去，也许也是多亏了有她在。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA02A_MAY0003"
    $ current_voice = "voice/OKA02A_MAY0003.ogg"
    "真由理" "「那么，冈伦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "OKA02A_MAY0004"
    $ current_voice = "voice/OKA02A_MAY0004.ogg"
    "真由理" "「今天的真由喜，也请多多指教哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA02A_OKA0077"
    $ current_voice = "voice/OKA02A_OKA0077.ogg"
    "伦太郎" "「嗯嗯」"
    call CHECK_RM_RECEIVE
    "微笑着向真由理点头，我静静地取下羊驼面具。"
    window hide


    $ loadBG(3,"IBG019A",png=True,hide=False)
    $ renpy.pause(0.5,hard=True)

    hide lh5 
    with None
    hide background-png 
    with moveouttop
    play se "SGSE056"




    $ loadBG(2,"BG03A4",trans=Fade(0.1,0.5,0.2))



    call CHECK_RM_RECEIVE
    "在Ｘ６８０００中设置日期。"
    window hide
    show houden 

    play se "SGSE035L" loop

    call CHECK_RM_RECEIVE
    "戴上头套。"
label L_RM_OKA1_RUK02_01_RECEIVE_END:

    "我现在就变身为正义的伙伴。"
label L_RM_OKA1_RUK02_01_REPLY_END:
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"])
    hide houden 


    hide screen phonebtn
    hide screen phoneSD1
    window hide
    stop se
    stop se
    stop bgm
    call timeleap (fromtime=[8,11,18,15], totime=[8,11,8,15], fromday=[4])

    return









    return
