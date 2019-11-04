label SGFD2_DAR07A:
    window hide


    $ loadBG(0,"BG05N1")


    $ date="8/16"
    show screen phonebtn
    show screen phoneSD1

    play bgm "FD2BGM01"
    "回到Ｌａｂ的时候，我看到冈伦和牧濑氏关系很好地坐在大楼前的长椅上。爆炸吧现充。"
    window hide



    $ loadBG(2,"BG39N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0000"
    $ current_voice = "voice/DAR07A_OKA0000.ogg"
    "伦太郎" "「哟……桶子……还有打工战士……」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0000"
    $ current_voice = "voice/DAR07A_SUZ0000.ogg"
    "铃羽" "「怎么了！？　突然这么颓废。难道被机关给拷问了？」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0001"
    $ current_voice = "voice/DAR07A_OKA0001.ogg"
    "伦太郎" "「受到了……机关的拷问………总算活着回来了……」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0001"
    $ current_voice = "voice/DAR07A_SUZ0001.ogg"
    "铃羽" "「怎么会这样……。看起来忍受了很多折磨呢……」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0000"
    $ current_voice = "voice/DAR07A_DAR0000.ogg"
    "至" "「啊啊，是说去『ぬくぬくＹＯＵ』做按摩？　如何？」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0002"
    $ current_voice = "voice/DAR07A_SUZ0002.ogg"
    "铃羽" "「ぬくぬく？」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0002"
    $ current_voice = "voice/DAR07A_OKA0002.ogg"
    "伦太郎" "「因为是女仆所以我大意了……。那群人，下那么重的手……。光想想，我就不寒而栗……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0003"
    $ current_voice = "voice/DAR07A_OKA0003.ogg"
    "伦太郎" "「桶子，如果要去的话就小心点。那群女仆，首先会毁坏你的脚心」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0004"
    $ current_voice = "voice/DAR07A_OKA0004.ogg"
    "伦太郎" "「如果变成那样的话……你就是想跑也没法跑了……」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0001"
    $ current_voice = "voice/DAR07A_DAR0001.ogg"
    "至" "「足疗按摩乙」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0003"
    $ current_voice = "voice/DAR07A_SUZ0003.ogg"
    "铃羽" "「……？」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0000"
    $ current_voice = "voice/DAR07A_CRS0000.ogg"
    "红莉栖" "「桥田，找到阿万音由季了吗？」"
    "牧濑氏看着我边上阿万音氏的表情，如是问道。"
    "于是，我就和牧濑氏还有冈伦说了刚才广播馆发生的事情。"
    "但是，隐瞒了阿万音氏是通过时间机器来到这个时代的和由季是她母亲的事实。"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0002"
    $ current_voice = "voice/DAR07A_DAR0002.ogg"
    "至" "「那个，冈伦。Ｄｍａｉｌ的实验，能再搞一次吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0005"
    $ current_voice = "voice/DAR07A_OKA0005.ogg"
    "伦太郎" "「嗯？Ｄｍａｉｌ……。那个的话……」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0001"
    $ current_voice = "voice/DAR07A_CRS0001.ogg"
    "红莉栖" "「不行的」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0002"
    $ current_voice = "voice/DAR07A_CRS0002.ogg"
    "红莉栖" "「我刚刚也做过了，不行」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0003"
    $ current_voice = "voice/DAR07A_DAR0003.ogg"
    "至" "「到底什么意思？」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0006"
    $ current_voice = "voice/DAR07A_OKA0006.ogg"
    "伦太郎" "「今天早上，４２寸显像管好像发生故障了」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0004"
    $ current_voice = "voice/DAR07A_DAR0004.ogg"
    "至" "「等！？」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0007"
    $ current_voice = "voice/DAR07A_OKA0007.ogg"
    "伦太郎" "「修理的话好像要花上两周的时间」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0005"
    $ current_voice = "voice/DAR07A_DAR0005.ogg"
    "至" "「也就是说，没法发Ｄｍａｉｌ咯！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    "为了启动作为时间机器的电话微波炉，就需要{color=#f00}显像管工房{/color}里的镇店之宝４２寸显像管电视机处于开启状态。"
    window hide



    $ loadBG(2,"BG05N3")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB03"),"True","lh/SUZ_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0004"
    $ current_voice = "voice/DAR07A_SUZ0004.ogg"
    "铃羽" "「桥田你不是会修吗？　你不是对这方面很擅长吗？」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0006"
    $ current_voice = "voice/DAR07A_DAR0006.ogg"
    "至" "「我又没说我很擅长，而且说起来，冈伦一直不也是在做道具啥的么」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0007"
    $ current_voice = "voice/DAR07A_DAR0007.ogg"
    "至" "「而且显像管电视机什么的，里面我根本没有看过」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0008"
    $ current_voice = "voice/DAR07A_DAR0008.ogg"
    "至" "「而且，连身为专家的店长都说要修两周了。所以就算是想修估计也不会比那个快咯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0005"
    $ current_voice = "voice/DAR07A_SUZ0005.ogg"
    "铃羽" "「咕……」"
    "当然修肯定能修。"
    "如果过了两周后就能够发送邮件了。"
    "如果能够发送穿越时空的Ｄｍａｉｌ的话，现在发送和两周后发送并没有什么区别。"
    "但是——"
    "Ｄｍａｉｌ并不一定会改变过去。"
    "而且，考虑到由季碳现在可能已经很危险了，已经不能乐观地去想“等着把显像管修好再说”了吧。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0006"
    $ current_voice = "voice/DAR07A_SUZ0006.ogg"
    "铃羽" "「我，我立马去拜托下厂家看能不能立马修好」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0007"
    $ current_voice = "voice/DAR07A_SUZ0007.ogg"
    "铃羽" "「桥田至也，找一下看有没有其他的方法」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE017"

    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0008"
    $ current_voice = "voice/DAR07A_SUZ0008.ogg"
    "铃羽" "「店长！」"
    "阿万音氏立马冲进房子里面。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0003"
    $ current_voice = "voice/DAR07A_CRS0003.ogg"
    "红莉栖" "「Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的事情看来是不能置之不理了」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0004"
    $ current_voice = "voice/DAR07A_CRS0004.ogg"
    "红莉栖" "「虽然我觉得桥田是想得太多了，如果你在广播馆受到袭击是事实的话……我想由季可能现在处在非常危险的境地」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0009"
    $ current_voice = "voice/DAR07A_DAR0009.ogg"
    "至" "「但是啊，我现在能做的事情，已经没有了吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0005"
    $ current_voice = "voice/DAR07A_CRS0005.ogg"
    "红莉栖" "「……果然，是那个暗号啊」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0006"
    $ current_voice = "voice/DAR07A_CRS0006.ogg"
    "红莉栖" "「Ｂ１４　７Ｈ　８Ｈ　Ｙ９１」"
    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0007"
    $ current_voice = "voice/DAR07A_CRS0007.ogg"
    "红莉栖" "「把这个暗号解析出来，是整个事件的关键所在」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC01"),"True","lh/CRS_ASC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR07A_CRS0008"
    $ current_voice = "voice/DAR07A_CRS0008.ogg"
    "红莉栖" "「再一次、重新探讨下解读方法吧。那个、冈部、站起来。桥田你也是」"
    $ stopvoc("OKA")
    play OKA "DAR07A_OKA0008"
    $ current_voice = "voice/DAR07A_OKA0008.ogg"
    "伦太郎" "「哦，别，别拉我起来啊……！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "牧濑氏就这样，把冈伦带到了楼上。"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0010"
    $ current_voice = "voice/DAR07A_DAR0010.ogg"
    "至" "「…………」"
    "就这样呆呆地看着抱着显像管的阿万音氏和店长出门了。"
    "我看着他们将那个显像管电视机装到了店门前面的货车上。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0009"
    $ current_voice = "voice/DAR07A_SUZ0009.ogg"
    "铃羽" "「就这样拿着直接送到厂子里去吧，为了能够更快地修好，现在就去拜托修理厂吧」"
    $ stopvoc("TEN")
    play TEN "DAR07A_TEN0000"
    $ current_voice = "voice/DAR07A_TEN0000.ogg"
    "天王寺" "「即使直接扔进厂子里面，很快地修好这个也是不可能的。别搞错了」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0010"
    $ current_voice = "voice/DAR07A_SUZ0010.ogg"
    "铃羽" "「嗯，我知道。但是，我想可能会有奇迹出现」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "DAR07A_TEN0001"
    $ current_voice = "voice/DAR07A_TEN0001.ogg"
    "天王寺" "「那么就快点坐进副位。速度出发吧」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0011"
    $ current_voice = "voice/DAR07A_SUZ0011.ogg"
    "铃羽" "「桥田至，那么，我们先走了」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0012"
    $ current_voice = "voice/DAR07A_SUZ0012.ogg"
    "铃羽" "「我的，电话号码，告诉过你吗？」"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0013"
    $ current_voice = "voice/DAR07A_SUZ0013.ogg"
    "铃羽" "「如果有什么事情的话，立马联系我」"
    "阿万音氏一边说着一边拿着小纸条写着电话号码。"
    $ stopvoc("SUZ")
    play SUZ "DAR07A_SUZ0014"
    $ current_voice = "voice/DAR07A_SUZ0014.ogg"
    "铃羽" "「这个，还有这个，慎重起见你都拿着吧」"
    "和纸条一起给我的还有由季碳的手机。"
    "上面挂着的呜啪吊坠，感觉有点分量。"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0011"
    $ current_voice = "voice/DAR07A_DAR0011.ogg"
    "至" "「但是，我……」"
    "到了这里已经没有什么可以发掘的了吧。"
    "不管怎样这已经糟透了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE075"

    "在这样想的时候，阿万音氏和店长已经开车走了。"
    window hide
    play se "SGSE103"

    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0012"
    $ current_voice = "voice/DAR07A_DAR0012.ogg"
    "至" "「啊，已经走了……」"
    window hide


    $ loadBG(2,"BG39N")



    "把纸条和手机放到口袋里面后，我慢慢地坐在了椅子上。"
    "到了这地步真的已经离危险很近了。"
    "从受到袭击的我的角度来看大家都太意气用事了。"
    "如果进到不该进的地方后自己被杀掉，什么都晚了。"
    "在这种状况下即使拜托警察，也因为啥证据没有而不会出动的。"
    "可以说是个人行动了——"
    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0013"
    $ current_voice = "voice/DAR07A_DAR0013.ogg"
    "至" "「…………」"
    "哼。"
    "看着眼前这串暗号，有一种即视感。"
    "到底是怎么回事呢。"
    "听说，这数字刻在的地方是——"
    window hide
    $ loadBG(0,"IBG037A",png=True)


    hide screen phonebtn
    play bgm "FD2BGM07"
    "下水道。"
    "到处都有，随处可见的东西啊。"
    "展开这四个暗号。"
    "７７　４Ｈ　８Ｈ　９９"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0014"
    $ current_voice = "voice/DAR07A_DAR0014.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0015"
    $ current_voice = "voice/DAR07A_DAR0015.ogg"
    "至" "「有了！」"
    window hide
    hide background-png 
    $ loadBG(0,"BG05N3")


    play se "SGSE307"








    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0016"
    $ current_voice = "voice/DAR07A_DAR0016.ogg"
    "至" "「诶，这是……」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0017"
    $ current_voice = "voice/DAR07A_DAR0017.ogg"
    "至" "「好像……。从规律上，完全一致！」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"IBG031A")

    hide screen phonebtn
    "由季碳留下来的暗号实际上是『Ｂ１４　７Ｈ　８Ｈ　Ｙ９１』。"
    window hide


    $ loadBG(0,"BG79N3")
    $ loadBG(0,"IBG037A",png=True)










    hide screen phonebtn
    show screen phoneSD1
    "这里面的『７Ｈ　８Ｈ』，和这边这个『４Ｈ　８Ｈ』非常的相似。"
    "没搞错的话，暗号的开头是Ｂ末尾是Ｙ。"
    "这个Ｂ和Ｙ到底代表着什么呢？"
    "看遍了盖子的角角落落，也没有看到那样的字母。"
    "Ｂ和，Ｙ……"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0018"
    $ current_voice = "voice/DAR07A_DAR0018.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0019"
    $ current_voice = "voice/DAR07A_DAR0019.ogg"
    "至" "「颜色……」"
    "这样的话下水道的编号就是，刻着『７７』的是蓝色的板子。刻着『９９』的是黄色的板子"
    "Ｂ是蓝色的意思，Ｙ就是黄色，刚好一致。"
    window hide
    hide background-png 
    with dissolve

    show screen phonebtn
    "看了下四周，试着调查了下其他的下水道。"
    "不远的地方就有一个。"
    "４８　４Ｈ　８Ｈ　９９"
    "４８不是蓝色，是黄色的板子。"
    "好像不是这个。"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0020"
    $ current_voice = "voice/DAR07A_DAR0020.ogg"
    "至" "「有了……就是这样……」"
    window hide





    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0021"
    $ current_voice = "voice/DAR07A_DAR0021.ogg"
    "至" "「冈伦！　牧濑氏！」"
    "朝着２楼窗户大声叫着两人的姓名。"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0022"
    $ current_voice = "voice/DAR07A_DAR0022.ogg"
    "至" "「那个暗号……是下水道的编号！」"
    $ stopvoc("DAR")
    play DAR "DAR07A_DAR0023"
    $ current_voice = "voice/DAR07A_DAR0023.ogg"
    "至" "「我去找了！　你们两位也赶快！」"
    play se "SGSE182"
    window hide


    $ loadBG(2,"BG18N1")



    "就算解开了暗号兴奋不已也无济于事，我立马就开始了搜索之旅。"
    "在秋叶原里面的下水道一个个找，肯定有我想要的那个。"
    "恐怕由季可能已经被抓住了。"
    "找到对应的下水道告诉警察，这就是作为我所能做的一切了。"

    hide screen phoneSD1
    window hide

    stop bgm 






    return
