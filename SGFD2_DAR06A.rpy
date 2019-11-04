label SGFD2_DAR06A:
    window hide


    $ loadBG(0,"BG13E1")
    play se "SGSE007L" loop



    $ date="8/16"
    show screen phonebtn
    show screen phoneSD1

    "虽然我已经到了车站附近，但是好像没有看见由季碳的人影。"
    "嘛，也是正常的。２０分钟一直呆在这里的人才是不正常的吧。"
    "难道如牧濑氏说的一样，坐电车回去了。"
    "就算那样，至少先看下周围吧。"
    "满眼都是拿着画着萌妹子的袋子的死宅们。"
    "就仿佛夏之秋叶原的风景诗一样。"
    "说起来，人也太多了些。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    "但是那个里面，只有{color=#f00}广播馆{/color}前面好像有一堵看不见的墙壁一样，没有人的影子。"
    window hide


    $ loadBG(2,"BG08E0")



    "广播馆现在在装修中来着。"
    "一楼的卷闸门被拉了下来，根本没法进去。"
    "不过，试着看了下里面的状况，好像可以进到里面去。"
    "从电信那里知道的由季碳手机的位置来看，确定就是这里了。"
    "难道说就在这里面。"
    $ stopvoc("X06")
    play voc "DAR06A_X060000"
    $ current_voice = "voice/DAR06A_X060000.ogg"
    "？？？" "「唔…………」"
    "刚刚，从电话里面发出来的微弱的声音，现在还不断在耳朵里回响。"
    "明明已经接通了电话，却一句话也说不出来。"
    "是不想说出来呢，还是没能说出来呢。"
    "总之首先就是那里好像发生了什么，这一点已经明白了。"
    "如果是这样的话，被抓起来关到这里也是很有可能的。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0000"
    $ current_voice = "voice/DAR06A_DAR0000.ogg"
    "至" "「可恶，冈伦为什么还没有接电话」"
    "从刚刚开始就不断地打电话给冈伦，但是冈伦根本就不接电话。"
    "难道去女仆店里面按摩被吸干了？"
    "冈伦真是太废了。"
    "如果没有冈伦，我只能够单枪匹马的上了。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0001"
    $ current_voice = "voice/DAR06A_DAR0001.ogg"
    "至" "「只是去里面看看情况，只是去里面看看情况……」"
    window hide
    stop se



    $ loadBG(0,"BG07A6",trans=fade)
    "因为是闭馆中，馆内的灯当然也都关掉了。尽管是大白天的但也非常地暗。"
    "这里有着秋叶原中难以想象的安静，只有我自己的足音回响着。"
    "因为电梯和自动扶梯都已经停止运作了，只能走楼梯了。"
    "等到了４楼的时候就已经气喘吁吁地停下来休息。"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010000"
    $ current_voice = "voice/DAR06A_Y010000.ogg"
    "巡行者Ａ" "「那里的那位」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0002"
    $ current_voice = "voice/DAR06A_DAR0002.ogg"
    "至" "「……！？」"
    play bgm "BGM25"
    "这个建筑里面应该是没有人的啊，他突然发出声音真是吓到我了。"
    "从着装上来看是穿着作业服的两名男子，看来是从上面走下来的。"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010001"
    $ current_voice = "voice/DAR06A_Y010001.ogg"
    "巡行者Ａ" "「是谁允许你进来的？」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020000"
    $ current_voice = "voice/DAR06A_Y020000.ogg"
    "巡行者Ｂ" "「这个建筑现在不允许人进入的」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0003"
    $ current_voice = "voice/DAR06A_DAR0003.ogg"
    "至" "「额，那个，我是来找厕所的……」"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010002"
    $ current_voice = "voice/DAR06A_Y010002.ogg"
    "巡行者Ａ" "「真的吗？」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020001"
    $ current_voice = "voice/DAR06A_Y020001.ogg"
    "巡行者Ｂ" "「总之这里非常危险，快点出去」"
    "一边说着其中一位工作人员悄悄地拿出了手机。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0004"
    $ current_voice = "voice/DAR06A_DAR0004.ogg"
    "至" "「啊……」"
    "那个手机，有个呜啪人偶挂在下面。真的不是一般的大啊，太显眼了。"
    "感觉和这个工作人员粗鲁的风格格格不入的反差，我突然笑了出来。"
    "完全不管这边的行动，那个男人已经拿起手机不知道打给谁"
    "另一位的话就什么都没说一直盯着我。"
    "这，这什么情况……"
    "难道……感觉要被埋的感觉！？"

    stop bgm 




    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0005"
    $ current_voice = "voice/DAR06A_DAR0005.ogg"
    "至" "「……！？」"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "这个电话号码……！"
    "是由季碳！？"





    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0006"
    $ current_voice = "voice/DAR06A_DAR0006.ogg"
    "至" "「喂，喂喂！」"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010003"
    $ current_voice = "voice/DAR06A_Y010003.ogg"
    "巡行者Ａ" "「…………」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020002"
    $ current_voice = "voice/DAR06A_Y020002.ogg"
    "巡行者Ｂ" "「…………」"
    "无语中。"
    "眼前的两人一句话都没说。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0007"
    $ current_voice = "voice/DAR06A_DAR0007.ogg"
    "至" "「喂喂！？」"
    "怎么了呢？"
    "电话另一头，好像能够听见自己的声音……的样子……"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010004"
    $ current_voice = "voice/DAR06A_Y010004.ogg"
    "巡行者Ａ" "「…………」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020003"
    $ current_voice = "voice/DAR06A_Y020003.ogg"
    "巡行者Ｂ" "「…………」"
    play bgm "BGM12"
    "好讨厌的……感觉啊……"
    "难道说，这个号码就是那个男的手里那个的手机的……"
    "刚刚打给我电话的那个人是……"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010005"
    $ current_voice = "voice/DAR06A_Y010005.ogg"
    "巡行者Ａ" "「看来没有搞错」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020004"
    $ current_voice = "voice/DAR06A_Y020004.ogg"
    "巡行者Ｂ" "「你这家伙，是什么人？」"
    window hide
    call hide_phone

    "两人逼了上来。"
    "不好了……不好了……怎么办啊……？"
    window hide
    play se "SGSE065"



    with Fade(0.1,0.1,0.1)
    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0008"
    $ current_voice = "voice/DAR06A_DAR0008.ogg"
    "至" "「……！？」"
    "突然被打了！？"
    "眼冒金星。"
    "膝盖那儿已经使不出力气了，感觉这个地方要塌了一样，好不容易才稳住。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0009"
    $ current_voice = "voice/DAR06A_DAR0009.ogg"
    "至" "「等，等，停！　我对这没兴趣！」"
    "慌慌张张地往右边跑着下楼 。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0010"
    $ current_voice = "voice/DAR06A_DAR0010.ogg"
    "至" "「呜哇！？」"
    "突然踩空。"
    hide screen phoneSD1
    window hide
    play se "SGSE304"




    $ loadBG(2,"BG_BLACK",trans=Fade(0.1,0.1,0.1,color="fff"))




    hide screen phonebtn
    "就这样掉到了楼梯的中间。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0011"
    $ current_voice = "voice/DAR06A_DAR0011.ogg"
    "至" "「好疼……」"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010006"
    $ current_voice = "voice/DAR06A_Y010006.ogg"
    "巡行者Ａ" "「…………」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020005"
    $ current_voice = "voice/DAR06A_Y020005.ogg"
    "巡行者Ｂ" "「…………」"
    "两个男人默默地走了下来。"
    "看来是中了圈套了。"
    "打电话给我的人，就是这家伙。"
    "之所以关机肯定是因为为了能够有充足的时间埋伏在这里。"
    "然后我什么都不知道地来到了这里。"
    "看来由季碳被卷进了什么不得了的事。"
    "这个是可以确定的。"
    "恐怕，她已经——"
    "别这样想，现在比起想这个还是关心下自己吧。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0012"
    $ current_voice = "voice/DAR06A_DAR0012.ogg"
    "至" "「救，救命啊……」"
    stop bgm 
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0000"
    $ current_voice = "voice/DAR06A_SUZ0000.ogg"
    "？？？" "「就那么躺着别起来！」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0013"
    $ current_voice = "voice/DAR06A_DAR0013.ogg"
    "至" "「诶！？」"
    play bgm "BGM09"
    "我看见有一道黑影从我头上掠过。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0001"
    $ current_voice = "voice/DAR06A_SUZ0001.ogg"
    "？？？" "「──！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR002A"]]["Check"]=True
    $ loadBG(0,"EV_DAR002A",trans=Fade(0.1,0.1,0.1,color="fff"))


    play se "SGSE014"







    hide screen phonebtn
    $ stopvoc("Y01")
    play voc "DAR06A_Y010007"
    $ current_voice = "voice/DAR06A_Y010007.ogg"
    "巡行者Ａ" "「咕哇！？」"
    window hide
    play se "SGSE015"

    $ stopvoc("Y02")
    play voc "DAR06A_Y020006"
    $ current_voice = "voice/DAR06A_Y020006.ogg"
    "巡行者Ｂ" "「什么！？　是谁！？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0002"
    $ current_voice = "voice/DAR06A_SUZ0002.ogg"
    "？？？" "「太慢了！」"
    window hide
    play se "SGSE064"


    with whiteflash
    $ stopvoc("Y02")
    play voc "DAR06A_Y020007"
    $ current_voice = "voice/DAR06A_Y020007.ogg"
    "巡行者Ｂ" "「！？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0003"
    $ current_voice = "voice/DAR06A_SUZ0003.ogg"
    "？？？" "「哈！」"
    window hide
    play se "SGSE057"

    $ stopvoc("Y02")
    play voc "DAR06A_Y020008"
    $ current_voice = "voice/DAR06A_Y020008.ogg"
    "巡行者Ｂ" "「唔啊……噗……」"
    "只能够在昏暗的环境下看见一个身材娇小的人影，发出了一瞬间打倒两位大男人的气势。"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010008"
    $ current_voice = "voice/DAR06A_Y010008.ogg"
    "巡行者Ａ" "「住手，我开枪了！」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0004"
    $ current_voice = "voice/DAR06A_SUZ0004.ogg"
    "铃羽？" "「……！？」"
    window hide
    play se "SGSE061"


    with whiteflash
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0014"
    $ current_voice = "voice/DAR06A_DAR0014.ogg"
    "至" "「唔哦哦哦哦哦！」"
    $ stopvoc("Y01")
    play voc "DAR06A_Y010009"
    $ current_voice = "voice/DAR06A_Y010009.ogg"
    "巡行者Ａ" "「撤退！」"
    $ stopvoc("Y02")
    play voc "DAR06A_Y020009"
    $ current_voice = "voice/DAR06A_Y020009.ogg"
    "巡行者Ｂ" "「知道了！」"
    window hide
    play se "SGSE306L" loop



    $ loadBG(2,"BG_BLACK",trans=fade)



    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0005"
    $ current_voice = "voice/DAR06A_SUZ0005.ogg"
    "？？？" "「等下！」"
    play se "SGSE061"





    with whiteflash
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0006"
    $ current_voice = "voice/DAR06A_SUZ0006.ogg"
    "？？？" "「！」"
    "那两个男人以迅雷不及掩耳之势下楼跑了。"

    stop se
    "一瞬间内就只能够听见脚步声渐渐远去。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0015"
    $ current_voice = "voice/DAR06A_DAR0015.ogg"
    "至" "「发，发生了什么事……？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0007"
    $ current_voice = "voice/DAR06A_SUZ0007.ogg"
    "？？？" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0008"
    $ current_voice = "voice/DAR06A_SUZ0008.ogg"
    "？？？" "「哈？跑了。不过，确实没有想到手上拿着枪」"
    "刚刚加入战局的娇小的人影，从声音上来判断好像是个女孩子。"
    "放弃了追击那两个男子后，回到了我这里。"
    "伸出了手。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0009"
    $ current_voice = "voice/DAR06A_SUZ0009.ogg"
    "？？？" "「桥田至，没事吗？　有没有被子弹打中？」"
    "直到这时我才清楚地看清楚相貌。"
    window hide


    $ loadBG(0,"BG07A5")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM08"


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0016"
    $ current_voice = "voice/DAR06A_DAR0016.ogg"
    "至" "「等一，阿万音氏！？」"
    "不管怎么看都是铃羽本人，真是谢天谢地啊。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0017"
    $ current_voice = "voice/DAR06A_DAR0017.ogg"
    "至" "「等下，你怎么这么强！？　不对，比起这个问题更加想问的是，你为什么会在这里！？」"
    "窥探到了阿万音氏不为人知的一面，感觉还是有点害怕。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0010"
    $ current_voice = "voice/DAR06A_SUZ0010.ogg"
    "铃羽" "「我现在能说的只有，没事吗。总之先站起来吧」"
    "握住阿万音氏的手借力站了起来。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "她接着就跑到一边拿起了掉落的物品。"
    "那个掉落的东西是刚刚那位男子拿的手机。"
    "可能……是由季碳的吧。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0011"
    $ current_voice = "voice/DAR06A_SUZ0011.ogg"
    "铃羽" "「这个……果然」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0018"
    $ current_voice = "voice/DAR06A_DAR0018.ogg"
    "至" "「这个手机的主人就是，阿万音由季。这就是最后的答复？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0012"
    $ current_voice = "voice/DAR06A_SUZ0012.ogg"
    "铃羽" "「为什么你会知道名字？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0019"
    $ current_voice = "voice/DAR06A_DAR0019.ogg"
    "至" "「……稍微调查了下」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0013"
    $ current_voice = "voice/DAR06A_SUZ0013.ogg"
    "铃羽" "「嘿……」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0020"
    $ current_voice = "voice/DAR06A_DAR0020.ogg"
    "至" "「姐妹吗？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0014"
    $ current_voice = "voice/DAR06A_SUZ0014.ogg"
    "铃羽" "「…………」 "

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0015"
    $ current_voice = "voice/DAR06A_SUZ0015.ogg"
    "铃羽" "「这个，也是世界线收束造成的吧……」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0021"
    $ current_voice = "voice/DAR06A_DAR0021.ogg"
    "至" "「哈？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "接着，我面前的阿万音氏表情紧张。"
    "就像是，下定了决心要准备说些很糟糕的话。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0016"
    $ current_voice = "voice/DAR06A_SUZ0016.ogg"
    "铃羽" "「桥田至，虽然我现在说的话，没有足够说服你的证据──」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0017"
    $ current_voice = "voice/DAR06A_SUZ0017.ogg"
    "铃羽" "「但是非常想帮助，这个手机的主人。希望能够帮我」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0022"
    $ current_voice = "voice/DAR06A_DAR0022.ogg"
    "至" "「……请说明下状况。你和由季碳到底什么关系？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0018"
    $ current_voice = "voice/DAR06A_SUZ0018.ogg"
    "铃羽" "「由季碳？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0023"
    $ current_voice = "voice/DAR06A_DAR0023.ogg"
    "至" "「啊，不对……是由季女士」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0019"
    $ current_voice = "voice/DAR06A_SUZ0019.ogg"
    "铃羽" "「…………她是，我的母亲」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0024"
    $ current_voice = "voice/DAR06A_DAR0024.ogg"
    "至" "「啊，原来如……不对！　不是这样的？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0025"
    $ current_voice = "voice/DAR06A_DAR0025.ogg"
    "至" "「因为她和你一样年轻。岁数基本差不多」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0020"
    $ current_voice = "voice/DAR06A_SUZ0020.ogg"
    "铃羽" "「嗯，这个确实没错。虽然是这么说……」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0021"
    $ current_voice = "voice/DAR06A_SUZ0021.ogg"
    "铃羽" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0022"
    $ current_voice = "voice/DAR06A_SUZ0022.ogg"
    "铃羽" "「稍微过来下」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0026"
    $ current_voice = "voice/DAR06A_DAR0026.ogg"
    "至" "「诶，要我，去哪……」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0023"
    $ current_voice = "voice/DAR06A_SUZ0023.ogg"
    "铃羽" "「楼顶。如果去楼顶的话，我所说的事情，你肯定还是会信一点的」"
    "说不清又道不明只好眼见为实。"
    "只是，有一点必须说出来。"

    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0027"
    $ current_voice = "voice/DAR06A_DAR0027.ogg"
    "至" "「从这上楼顶，这是要我的命啊」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0024"
    $ current_voice = "voice/DAR06A_SUZ0024.ogg"
    "铃羽" "「…………」"
    "阿万音氏完美地无视了我说的话。"
    window hide



    $ loadBG(0,"BG11E3",trans=fade)
    play se "SGSE084"


    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0028"
    $ current_voice = "voice/DAR06A_DAR0028.ogg"
    "至" "「哦，哦，哦哦哦哦～？」"
    play bgm "BGM04"
    "在屋顶上，有一个不寻常的东西。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0029"
    $ current_voice = "voice/DAR06A_DAR0029.ogg"
    "至" "「那是什么啊……，人造卫星……吗，还是人造卫星的复制品？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0025"
    $ current_voice = "voice/DAR06A_SUZ0025.ogg"
    "铃羽" "「是时间机器」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0030"
    $ current_voice = "voice/DAR06A_DAR0030.ogg"
    "至" "「哈哈哈，你这小鬼」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0026"
    $ current_voice = "voice/DAR06A_SUZ0026.ogg"
    "铃羽" "「我乘坐这穿梭机，从２０３６年来到现在」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0031"
    $ current_voice = "voice/DAR06A_DAR0031.ogg"
    "至" "「虽然你很严肃地在开玩笑，但是我每天和冈伦混在一起对这种事的耐性很好的啦」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0027"
    $ current_voice = "voice/DAR06A_SUZ0027.ogg"
    "铃羽" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0032"
    $ current_voice = "voice/DAR06A_DAR0032.ogg"
    "至" "「……不对？　真的吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "听完我的疑问阿万音氏默不作声地走到人工卫星的复制品边上，按了一个按钮。"
    window hide
    play se "SGSE146"

    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0033"
    $ current_voice = "voice/DAR06A_DAR0033.ogg"
    "至" "「唔哦」"
    "只是按了下舱门就打开了。"
    "惊恐地进入到里面后。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR003A"]]["Check"]=True


    $ loadBG(2,"EV_DAR003A")



    hide screen phonebtn
    "眼前出现了很多的仪器表盘。"
    "如果只是人工卫星的话已经是相当厉害了。"
    "只是做出来恐怕就要几百万甚至上千万的资金。"
    "但是放到广播馆的屋顶上意义何在我真的不知道。"
    "这样的话也就是说……？"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0034"
    $ current_voice = "voice/DAR06A_DAR0034.ogg"
    "至" "「真的？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0028"
    $ current_voice = "voice/DAR06A_SUZ0028.ogg"
    "铃羽" "「…………」"
    "阿万音氏笑了笑后盯着我的眼睛点了点头。"
    "嘛，虽然我们也做出了差不多的时间机器所以也不是不能相信。"
    "但是突然这样说，也不知道该怎么反应。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0029"
    $ current_voice = "voice/DAR06A_SUZ0029.ogg"
    "铃羽" "「追其根源的话，这一切都是你造成的」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0030"
    $ current_voice = "voice/DAR06A_SUZ0030.ogg"
    "铃羽" "「也有点任性的成分在里面吧，想在这个时代里见到母亲」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0031"
    $ current_voice = "voice/DAR06A_SUZ0031.ogg"
    "铃羽" "「因为我早就知道联络方式了，就约好了在夏Ｃｏｍｉ上面相见。完全地，装作一个陌生人」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0032"
    $ current_voice = "voice/DAR06A_SUZ0032.ogg"
    "铃羽" "「但是还是未能做到。结果还是因为我的某些问题，才造成这样的事态……」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0033"
    $ current_voice = "voice/DAR06A_SUZ0033.ogg"
    "铃羽" "「在和我约定好的地方，母亲偶然地从“那些人”那里得到了“什么”。」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0034"
    $ current_voice = "voice/DAR06A_SUZ0034.ogg"
    "铃羽" "「就是因为偶然得到的那个东西，才会被“那些人”给抓住的。」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0035"
    $ current_voice = "voice/DAR06A_SUZ0035.ogg"
    "铃羽" "「但是世界线应该收束了，所以，人的命运是一种很复杂细微的东西，有些纰漏没有看见也是正常的……」"
    window hide



    $ loadBG(2,"BG11E3")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0036"
    $ current_voice = "voice/DAR06A_SUZ0036.ogg"
    "铃羽" "「……」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0037"
    $ current_voice = "voice/DAR06A_SUZ0037.ogg"
    "铃羽" "「桥田至，刚刚你说你是知道我母亲的事情了，是不是」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0038"
    $ current_voice = "voice/DAR06A_SUZ0038.ogg"
    "铃羽" "「母亲打电话给你了是不是？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0039"
    $ current_voice = "voice/DAR06A_SUZ0039.ogg"
    "铃羽" "「希望你能够告诉我一点情报。什么都行」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0035"
    $ current_voice = "voice/DAR06A_DAR0035.ogg"
    "至" "「呀，就算是这么说……」"
    "我就这样把我知道的所有事情都告诉了阿万音氏。"
    "只不过见过一次，而且交谈上面也不过是三言两语，虽然个人情报就这样随便地查清了，就这些。"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0040"
    $ current_voice = "voice/DAR06A_SUZ0040.ogg"
    "铃羽" "「是，暗号吗……」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0041"
    $ current_voice = "voice/DAR06A_SUZ0041.ogg"
    "铃羽" "「还不能够解读出来，母亲是这样说的吧？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0036"
    $ current_voice = "voice/DAR06A_DAR0036.ogg"
    "至" "「好像是这样的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0042"
    $ current_voice = "voice/DAR06A_SUZ0042.ogg"
    "铃羽" "「……母亲就这样偶然地得到了，又很巧地解开了，吧」 "
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0043"
    $ current_voice = "voice/DAR06A_SUZ0043.ogg"
    "铃羽" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0037"
    $ current_voice = "voice/DAR06A_DAR0037.ogg"
    "至" "「……顺便问下，你的父亲，也在这个时代吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0044"
    $ current_voice = "voice/DAR06A_SUZ0044.ogg"
    "铃羽" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0045"
    $ current_voice = "voice/DAR06A_SUZ0045.ogg"
    "铃羽" "「父亲的话──」"
    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0038"
    $ current_voice = "voice/DAR06A_DAR0038.ogg"
    "至" "「啊ー啊ー！　果然是不该问的！」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0046"
    $ current_voice = "voice/DAR06A_SUZ0046.ogg"
    "铃羽" "「诶？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0039"
    $ current_voice = "voice/DAR06A_DAR0039.ogg"
    "至" "「不要，我才不想听到关于由季碳老公的事情」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IRAKABE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IRAKABE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IRAKABE"])
    "那种事情，肯定是{color=#f00}浮打墙{/color}状态了吧，常考。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0047"
    $ current_voice = "voice/DAR06A_SUZ0047.ogg"
    "铃羽" "「也是。这样，也不错」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0048"
    $ current_voice = "voice/DAR06A_SUZ0048.ogg"
    "铃羽" "「但是，只有这个是，也想让你看看」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0040"
    $ current_voice = "voice/DAR06A_DAR0040.ogg"
    "至" "「……？」"
    window hide
    $ loadBG(0,"IBG036A",png=True,hide=False,hold=True)
    with moveinbottom


    hide screen phonebtn
    play bgm "FD2BGM05"
    "递过来的是一个古老的徽章。"
    "好像是一个巨大的金属……呜啪。"
    "虽然很熟悉，呜啪的表情已经崩溃了。"
    "这种扁平的样子作为商品确实够失格了。"
    window hide

    hide background-png 
    with moveoutbottom
    show screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0049"
    $ current_voice = "voice/DAR06A_SUZ0049.ogg"
    "铃羽" "「这是父亲给我的纪念品。你是不是，见过这个？」"
    "说着，阿万音氏拿出了刚刚从楼下拿的由季碳的手机。"
    "系在手机下面的是一个呜啪。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0041"
    $ current_voice = "voice/DAR06A_DAR0041.ogg"
    "至" "「……嗯？」"
    "相比了下后。"
    window hide
    $ loadBG(0,"IBG036A",png=True,hide=False,hold=True)
    with moveinbottom


    hide screen phonebtn
    "一边是圆乎乎的。"
    "一边都快烂成渣了。"
    window hide

    hide background-png 
    with moveoutbottom
    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0042"
    $ current_voice = "voice/DAR06A_DAR0042.ogg"
    "至" "「难道说，是同一个东西？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0050"
    $ current_voice = "voice/DAR06A_SUZ0050.ogg"
    "铃羽" "「可能吧，父亲和母亲，都拿着这个东西」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0043"
    $ current_voice = "voice/DAR06A_DAR0043.ogg"
    "至" "「这，这样么……」"
    "为什么要给我看呢？"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0044"
    $ current_voice = "voice/DAR06A_DAR0044.ogg"
    "至" "「有这个纪念品的话也就是说，在２０３６年，你的父亲……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0051"
    $ current_voice = "voice/DAR06A_SUZ0051.ogg"
    "铃羽" "「……没有音讯了」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0045"
    $ current_voice = "voice/DAR06A_DAR0045.ogg"
    "至" "「是吗……」"
    "这也就是说和死了差不多的意思了吧。"
    "也说了这个是纪念品了。"
    "要求说明下的话就太残酷了。"
    "不过，这至少让我明白了。"
    "由季碳有了男朋友。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0046"
    $ current_voice = "voice/DAR06A_DAR0046.ogg"
    "至" "「我想静静，也不要问我静静是谁……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0052"
    $ current_voice = "voice/DAR06A_SUZ0052.ogg"
    "铃羽" "「诶！？」"
    "告白之前就放弃了，而且是第二次放弃。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0053"
    $ current_voice = "voice/DAR06A_SUZ0053.ogg"
    "铃羽" "「呐，拜托了。现在，只有桥田至能够帮助我妈妈了。希望你能够助我一臂之力！」"
    "为什么我得做到这种地步啊。"
    "有着男朋友的三次元妹子，这根本就不是我的攻略对象啊。"
    "如果再对此次事件挖掘下去就不好了。"
    "反正就我这样肯定不可能成为什么白马王子的。"
    "刚刚在楼下，还被两个男子袭击了。"
    "我可不觉得能赢他们。"
    "而且，有比我更强的阿万音氏在，我出手是没有必要的。"
    "所以我的战斗就到此为止吧。第一章节就这么完结吧，第二章节就永远别开启了。"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0047"
    $ current_voice = "voice/DAR06A_DAR0047.ogg"
    "至" "「…………」 "

    stop bgm 
    "嘛，但是——"
    "但是在最后还是想给予阿万音氏一点力量。"
    play bgm "FD2BGM06"

    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0048"
    $ current_voice = "voice/DAR06A_DAR0048.ogg"
    "至" "「如果是发送Ｄｍａｉｌ的话，还是可以的」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0054"
    $ current_voice = "voice/DAR06A_SUZ0054.ogg"
    "铃羽" "「Ｄｍａｉｌ？」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0049"
    $ current_voice = "voice/DAR06A_DAR0049.ogg"
    "至" "「在我们的Ｌａｂ，做出了个时间机器。能够发送短信到过去的那种。如果用那个的话可能……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB03"),"True","lh/SUZ_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0055"
    $ current_voice = "voice/DAR06A_SUZ0055.ogg"
    "铃羽" "「有这样的东西啊……！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0056"
    $ current_voice = "voice/DAR06A_SUZ0056.ogg"
    "铃羽" "「但是，如果能够帮助我母亲的话……！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB04"),"True","lh/SUZ_AMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0057"
    $ current_voice = "voice/DAR06A_SUZ0057.ogg"
    "铃羽" "「走吧，桥田至」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0050"
    $ current_voice = "voice/DAR06A_DAR0050.ogg"
    "至" "「两个人坐在一部自行车上面就“会成为恋人的”，这样真的好吗？」"
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0058"
    $ current_voice = "voice/DAR06A_SUZ0058.ogg"
    "铃羽" "「我的山地自行车，你坐上去的话就太难骑了」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0051"
    $ current_voice = "voice/DAR06A_DAR0051.ogg"
    "至" "「那，我还是走路吧……」 "

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB01"),"True","lh/SUZ_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0059"
    $ current_voice = "voice/DAR06A_SUZ0059.ogg"
    "铃羽" "「给我跑起来！　快点！」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0052"
    $ current_voice = "voice/DAR06A_DAR0052.ogg"
    "至" "「…………」"
    "我没有这样的体力啊。"
    window hide
    play se "SGSE181"


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我一边在心中默念日狗一边狂奔追着阿万音氏，突然注意到手指流血了。"
    "刚刚，被那两个男子殴打后从楼上摔下来时，好像是被什么东西割到了。"
    "搜了搜口袋，拿出了从由季碳那里拿来的创可贴贴在手指上面。"
    window hide

    $ loadBG(0,"BG07A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB01"),"True","lh/SUZ_AMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "DAR06A_SUZ0060"
    $ current_voice = "voice/DAR06A_SUZ0060.ogg"
    "铃羽" "「桥田至！　快点！」"
    $ stopvoc("DAR")
    play DAR "DAR06A_DAR0053"
    $ current_voice = "voice/DAR06A_DAR0053.ogg"
    "至" "「好的好的……」"

    hide screen phoneSD1
    window hide

    stop bgm 






    return
