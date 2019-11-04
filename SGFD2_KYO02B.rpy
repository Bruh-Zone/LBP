label SGFD2_KYO02B:
    play bgm "BGM09"
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG02N1")
    play se "SGSE316"
    show fire zorder 4 




    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "我和红莉栖一起跑进了Ｌａｂ。"
    "感到一阵热浪迎面袭来，我下意识地后退了几步。"
    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0000"
    $ current_voice = "voice/KYO02B_CRS0000.ogg"
    "红莉栖" "「为，为什么会变成这幅样子哦！」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0000"
    $ current_voice = "voice/KYO02B_OKA0000.ogg"
    "伦太郎" "「天知道！」"
    "从室内冒出滚滚浓烟。"
    "视野很差，无法掌握几米之外的情况。"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0001"
    $ current_voice = "voice/KYO02B_OKA0001.ogg"
    "伦太郎" "「真由理！　桶子！　你们在哪儿！」"
    "我大声地呼喊着。"
    "立刻得到了回复。"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0000"
    $ current_voice = "voice/KYO02B_MAY0000.ogg"
    "真由理" "「冈伦！　这里！」"
    "我俯下身子，从烟的下方向里面看去。"
    "在房间的中央的烈火之墙——"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") at center as lh5 zorder 3 :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play se "SGSE317"

    "在熊熊燃烧的业火的另一侧，是真由理的身影。"
    "真由理像小动物一般不住地颤抖着。"
    "好像是因为被火焰之墙挡住了道路，无法到这里来的样子。"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0002"
    $ current_voice = "voice/KYO02B_OKA0002.ogg"
    "伦太郎" "「在那里等着！　我马上来救你！」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0001"
    $ current_voice = "voice/KYO02B_MAY0001.ogg"
    "真由理" "「恩……！」"
    window hide
    play se "SGSE317"




    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0001"
    $ current_voice = "voice/KYO02B_CRS0001.ogg"
    "红莉栖" "「桥田在哪里！？」"
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0000"
    $ current_voice = "voice/KYO02B_DAR0000.ogg"
    "至" "「在、在这里呢！」"
    window hide



    $ loadBG(2,"BG01N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "回头一看，桶子就在我的边上站着。"
    "感觉是被吓得不知如何是好吧，一副惊慌失措的样子。"
    "现在就不先问发生了什么了。先把真由理救出来再说。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0003"
    $ current_voice = "voice/KYO02B_OKA0003.ogg"
    "伦太郎" "「红莉栖，快打１１９！　快点！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0002"
    $ current_voice = "voice/KYO02B_CRS0002.ogg"
    "红莉栖" "「明白了！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0004"
    $ current_voice = "voice/KYO02B_OKA0004.ogg"
    "伦太郎" "「桶子赶紧下楼，让店长先去避难！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0001"
    $ current_voice = "voice/KYO02B_DAR0001.ogg"
    "至" "「Ｏ、ＯＫ！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "听到了他们的回答时，我已经脱掉了我穿着的白大褂。"
    "将它用一只手抓住，朝着厨房的水槽——"
    "快速地拧开了水龙头，将白大褂浸湿了。"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0002"
    $ current_voice = "voice/KYO02B_MAY0002.ogg"
    "真由理" "「冈伦……」"
    "从火焰的另一侧传来了微弱的声音……"
    "我听见了真由理的哀鸣。"
    "但是没有回答她的时间了。"
    "我用打湿的白大褂抱住头，毫不犹豫地冲进了火焰中——！"
    hide screen phoneSD1
    window hide
    hide fire 



    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO001A"]]["Check"]=True
    $ loadBG(0,"EV_KYO001A")









    hide screen phonebtn
    "穿过了火之墙后，在眼前就是真由理的身影。"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0005"
    $ current_voice = "voice/KYO02B_OKA0005.ogg"
    "伦太郎" "「真由理，没事吧！？」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0003"
    $ current_voice = "voice/KYO02B_MAY0003.ogg"
    "真由理" "「恩……！　那冈伦没事吗……？」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0006"
    $ current_voice = "voice/KYO02B_OKA0006.ogg"
    "伦太郎" "「不必在意我。我是凤凰院凶真啊。这样的火焰还不足以伤到我的真身」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0004"
    $ current_voice = "voice/KYO02B_MAY0004.ogg"
    "真由理" "「但是，脸颊附近，被烧伤了呢……」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0007"
    $ current_voice = "voice/KYO02B_OKA0007.ogg"
    "伦太郎" "「这个只是……被晒伤了」"
    "一边说着，我一边从头上取下白大褂，将它包在真由理的身上。"
    "感觉差不多能把她全身给包住的程度。"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0005"
    $ current_voice = "voice/KYO02B_MAY0005.ogg"
    "真由理" "「怎么感觉有点像万圣节的时候的妖怪啊……」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0008"
    $ current_voice = "voice/KYO02B_OKA0008.ogg"
    "伦太郎" "「不如说是被警察带走的犯罪者的样子呢」"
    "什么呀，现在才不是说这种无聊的话的时候！"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0009"
    $ current_voice = "voice/KYO02B_OKA0009.ogg"
    "伦太郎" "「好了，走吧，真由理！」"
    "我几乎是以把真由理抱在怀里的姿势，又一次冲过了火焰之壁。"
    window hide

    stop bgm 


    $ loadBG(0,"BG79N6",at=[Transform(yalign=1.0)])





    show screen phonebtn
    show screen phoneSD1
    "跑下楼梯，来到了显像管工房前……"
    "在那里已经有一些躁动的人了。"
    "在最前方怒号着的是店长。"
    "店长好像是要抡起那结实的臂膀朝我这边打过来的样子。"
    "桶子在后面拼命地试图阻止他这么做。"
    "桶子抱住店长的腰，然后两只脚用力地固定在原地。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "KYO02B_TEN0000"
    $ current_voice = "voice/KYO02B_TEN0000.ogg"
    "天王寺" "「喂，冈部！这到底是怎么回事！你这家伙，到底都干了什么啊！」"
    "为什么……会变成我的责任啊。"
    "嘛因为Ｌａｂ的最高负责人是我的关系，说是我的责任就是我的吗。"
    "这么想着，真由理似乎看透了我的想法，开口说道。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA05"),"True","lh/MAY_CMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM05"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0006"
    $ current_voice = "voice/KYO02B_MAY0006.ogg"
    "真由理" "「全部是……真由喜的……责任……」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0007"
    $ current_voice = "voice/KYO02B_MAY0007.ogg"
    "真由理" "「是因为真由喜在着了火的天妇罗锅里，加了水的关系……」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0008"
    $ current_voice = "voice/KYO02B_MAY0008.ogg"
    "真由理" "「然后火焰就突然冲的老高，锅子就翻掉了……」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0009"
    $ current_voice = "voice/KYO02B_MAY0009.ogg"
    "真由理" "「所以……所以……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC04"),"True","lh/MAY_CMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0010"
    $ current_voice = "voice/KYO02B_MAY0010.ogg"
    "真由理" "「抱歉呢、冈伦、红莉栖酱……。真的……非常抱歉……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0003"
    $ current_voice = "voice/KYO02B_CRS0003.ogg"
    "红莉栖" "「等一下，要道歉还太早了。在那之前，能先说一下为什么天妇罗的锅子会着火吗？」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0010"
    $ current_voice = "voice/KYO02B_OKA0010.ogg"
    "伦太郎" "「难道是没有看仔细？」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0011"
    $ current_voice = "voice/KYO02B_MAY0011.ogg"
    "真由理" "「桶子君那时候……在看录好的米稻酱的动画……」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0012"
    $ current_voice = "voice/KYO02B_MAY0012.ogg"
    "真由理" "「真由喜那时候接到了……新一的电话……」"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0011"
    $ current_voice = "voice/KYO02B_OKA0011.ogg"
    "伦太郎" "「新一……？」"
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0013"
    $ current_voice = "voice/KYO02B_MAY0013.ogg"
    "真由理" "「中濑新一是……吹雪酱的哥哥哦……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_LAYER"])
    $ stopvoc("MAY")
    play MAY "KYO02B_MAY0014"
    $ current_voice = "voice/KYO02B_MAY0014.ogg"
    "真由理" "「吹雪酱的哥哥他在……当铺工作……是{color=#f00}Ｌａｙｅｒ{/color}……」"
    "问了这个问题的我真是个傻瓜。这些都是无关紧要的情报。"
    "但是谜题解开了，也就是说是这么回事。"
    hide screen phoneSD1
    window hide
    hide lh5 
    hide lh6 
    with dissolve


    hide screen phonebtn
    "首先桶子把天妇罗锅放在火上，然后去看米稻酱的动画了。"
    "另一方面真由理在那个时候也在和吹雪酱的哥哥打电话，所以并没有看着锅子。"
    "这样一来，放置Ｐｌａｙ状态的锅子里的油因为超高温而大量蒸发——"
    "然后就被炉火点燃，变成了巨大的火柱。"
    "慌忙之中，真由理为了灭火，就将水给倒了进去。"
    "但是，那是在油锅起火时万万不能做的禁断之法——"
    "水一瞬间就会蒸发，与此同时大量暴沸的油会向四面八方溅开。"
    window hide
























    show expression "bg/BG79N6~ipad.jpg" as background :
        yalign 1.0
        linear 0.5yalign 0.5
    hide screen phonebtn
    show screen phoneSD1
    "听到了似乎还很遥远的救火车的声音。"
    "我呆然地伫立着，抬头朝Ｌａｂ方向看去。"
    "火势并没有减小的迹象。"
    "不如说势头反而增加了。"
    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0004"
    $ current_voice = "voice/KYO02B_CRS0004.ogg"
    "红莉栖" "「道具什么的，难得进行了魔改造结果都泡汤了呢……」"
    "红莉栖轻声说道。"
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0002"
    $ current_voice = "voice/KYO02B_DAR0002.ogg"
    "至" "「不对，现在这个时候那种事怎样都好了……比起那个我辛辛苦苦收集起来的宝贝就……」"
    window hide



    hide background 
    $ loadBG(2,"BG79N6",at=[Transform(yalign=1.0)])






    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    "不知何时，我才注意到桶子已经回到了我们的边上。"
    "店长带着从店里拿出来的重要文件之类的东西不知去向。"
    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0005"
    $ current_voice = "voice/KYO02B_CRS0005.ogg"
    "红莉栖" "「什么宝贝……？」"
    "红莉栖问道。"
    window hide


    $ loadBG(2,"BG79N6")




    hide screen phonebtn
    "桶子将目光投向２楼的窗户，茫然地答道。"
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0003"
    $ current_voice = "voice/KYO02B_DAR0003.ogg"
    "至" "「在说Ｓｋｅｂｏ啦……」"
    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0006"
    $ current_voice = "voice/KYO02B_CRS0006.ogg"
    "红莉栖" "「Ｓｋｅｂｏ……？」"
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0004"
    $ current_voice = "voice/KYO02B_DAR0004.ogg"
    "至" "「就是素描簿……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"IBG023A")

    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0005"
    $ current_voice = "voice/KYO02B_DAR0005.ogg"
    "至" "「在那里面可是有青梅酱，伊户野意酱，伊野陆奥酱，海千佳酱，关寻酱，七奈留酱，日野伊田酱，服智酱，堀雪酱，福家酱的画哦」"
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0006"
    $ current_voice = "voice/KYO02B_DAR0006.ogg"
    "至" "「不止那些哦……还有很多其他有名的画师的画……」"
    window hide


    $ loadBG(0,"BG79N6")






    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DAMEPO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DAMEPO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DAMEPO"])
    $ stopvoc("DAR")
    play DAR "KYO02B_DAR0007"
    $ current_voice = "voice/KYO02B_DAR0007.ogg"
    "至" "「但在这样的火里的话，已经{color=#f00}不行咯{/color}……。肯定已经被烧完了，啊啊……」"
    "『变成那样的原因难道不是你吗！』……我把这句都到喉咙边上的话又咽了下去。"
    "就算责怪桶子也没有意义。本来那些就是已经无法挽回的事了……"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "无法挽回……所以才……"
    "无法……"

    stop bgm 
    "…………"
    "无法挽回……？"
    window hide


    $ loadBG(0,"BG79N6")




















    hide screen phonebtn
    show screen phoneSD1
    play bgm "BGM08"
    "是哦，是呢！我现在在干什么呢！"
    "这样的话电话微波炉（暂）也好，好不容易完成的时间机器也好，不都要烧成灰了么！"
    "在真由理被诱拐的威胁尚未消去的现在，如果Ｄｍａｉｌ或者时间机器都不能用了就非常麻烦了！"
    "就是那样，就是那样！这个Ｌａｂ里面满是我们的回忆啊！"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SANCTUARY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SANCTUARY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SANCTUARY"])
    "这样重要的场所，{color=#f00}圣域{/color}，我们崇高的未来道具研究所，难道就只能这样被天妇罗的油给燃烧殆尽吗！"
    window hide



    $ loadBG(0,"BG79N6")






    show screen phonebtn
    show screen phoneSD1
    "在想完这些之前脚已经迈出去了。"
    "飞快地跑过台阶，冲上楼梯。"
    $ stopvoc("CRS")
    play CRS "KYO02B_CRS0007"
    $ current_voice = "voice/KYO02B_CRS0007.ogg"
    "红莉栖" "「等等冈部！　你想干啥！？」"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "问我要干啥？真是愚蠢的问题……"
    "这个状况下，只有一件事要去做。"
    "把火给——灭了！"
    show fire 
    window hide


    $ loadBG(0,"BG02N1")


    show screen phonebtn
    "我再一次打开门，朝着Ｌａｂ里……"
    "从附近找到了白大褂套在头上，又冲进了熊熊大火。"

    window hide
    hide fire 



    $ loadBG(0,"BG03A4")









    "越过了火焰之墙，我来到了开发室里。"
    "幸运的是，火焰还没有吞噬掉这里。"
    "电话微波炉（暂）安然无恙。"
    "来吧，把火给灭了！去灭掉！灭给你看看！"
    "有两种方法可以完成。"
    "时间跳跃，或者发送Ｄｍａｉｌ。"
    "但是前者有一定的奉献。"
    "『时间机器是残次品』……之前世界线的红莉栖如此说过。"
    "现在想起来，时间跳跃的误差说不定是因为魔改造计划的关系。"
    "可能是电话微波炉（暂）改良的结果，记忆的拷贝好像变得不好了。"
    "总之不允许失败，选择必定会成功的方法吧。"
    "Ｄｍａｉｌ吧！发送Ｄｍａｉｌ！"
    "收件人是我自己的手机。"
    "要发送到的时间是『１５点２２分』──"
    "『阻止真由理外出的邮件』是『１５時２０分』收到的，所以就发送到那个时刻之后。"
    "这是因为发到那封邮件之前的话可能会导致阻止真由理外出的邮件消失。"
    "虽然没有验证过不知道到底会不会消失，但是我还是不打算冒这个险。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "邮件内容就是这样吧。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_KYO02B_EDIT_FG801_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_KYO02B_SEND_FG801"]
    call send_mail (id=[20,21,22,23])


    "输入完邮件后，我将微波炉的定时器设定为２４０秒——启动！"
    show houden 
    window hide

    play se "SGSE035L" loop

    "因为现在是『１９点２２分』，要发送到『１５点２２分』的话，２４０分钟就等于定时器的２４０秒。"
    "这么想着的时候，放电现象已经开始了。"
    "收件人也设定完毕。"
    window hide


    "只需要按下发送按钮——"
    "我将我的右手高高举起，大声地说道。"
    $ stopvoc("OKA")
    play OKA "KYO02B_OKA0012"
    $ current_voice = "voice/KYO02B_OKA0012.ogg"
    "伦太郎" "「颤动吧，我的右腕！以契约之名命令你！镇压这狂野的红莲之炎吧！」"
    "然后我——按下了发送按钮。"
    window hide

    stop bgm 



    stop bgm 
    stop se
    stop se


    hide screen phoneSD1



    $ loadBG(1,"BG21N2")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_02A.avi")
    hide screen invisible





    return
