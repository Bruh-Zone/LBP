label SGFD2_KYO02A:
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade


    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1
    python:
        rml = []
        sml = []
        lml = []
        cml = {}
        RcvMail(19)
        ReadMail(19)
        RcvMail(18)
        ReadMail(18)
        RcvMail(17)
        ReadMail(17)

    $ loadBG(0,"BG23E")
    "褪了色的世界错乱地扭曲着。"
    "感觉耳朵深处被刺伤了一般，我咬了咬牙齿。"
    "感觉自己失去了平衡，我用手扶住了路边的树。"
    "从眼角的余光勉强捕捉到了行人的惊讶神色。"
    show screen phonebtn
    show screen phoneSD1
    "好不容易平息了眩晕感，世界又恢复了颜色。"
    "我放开路边的树，摇了摇头，环顾了一下四周。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0000"
    $ current_voice = "voice/KYO02A_OKA0000.ogg"
    "伦太郎" "「这里是……{color=#f00}ＵＰＸ{/color}的前面吗……」"
    "在这时候从我的身后……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO02A_FEI0000"
    $ current_voice = "voice/KYO02A_FEI0000.ogg"
    "菲利斯" "「凶真、怎么了喵？」"
    "站着一位猫娘。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0001"
    $ current_voice = "voice/KYO02A_OKA0001.ogg"
    "伦太郎" "「菲利斯……你，为什么会在这里啊？」"
    $ stopvoc("FEI")
    play FEI "KYO02A_FEI0001"
    $ current_voice = "voice/KYO02A_FEI0001.ogg"
    "菲利斯" "「什么为什么，从刚才开始就一直在这里啊」"
    "无法掌握情况。"
    "而且也不明白为什么自己会在这里。"
    "但是肯定发生了什么，这一点倒是很清楚。"
    "“Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ”的发动意味着——世界线变化了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0002"
    $ current_voice = "voice/KYO02A_OKA0002.ogg"
    "伦太郎" "「对了，真由理……。真由理怎样了……？」"
    "这么说着，我向左手看去。"
    "刚刚还握在手里的真由理的电话，已经消失了。"
    "口袋里只有我的手机，和之前的传单。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我立刻掏出自己的手机，给真由理打了电话。"
    window hide








    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0000"
    $ current_voice = "voice/KYO02A_MAY0000.ogg"
    "真由理" "「嘟嘟噜♪　真由喜的说」"

    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0003"
    $ current_voice = "voice/KYO02A_OKA0003.ogg"
    "伦太郎" "「真由理！　真由理！」"


    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0001"
    $ current_voice = "voice/KYO02A_MAY0001.ogg"
    "真由理" "「哇哇，小冈伦，好大声哦。难道说生气了？」"

    "不是生气。怎么可能生气呢。"
    "我安心地呼了口气，然后又扶住了附近路边的树。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0004"
    $ current_voice = "voice/KYO02A_OKA0004.ogg"
    "伦太郎" "「真由理、你现在在哪里？」"



    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0002"
    $ current_voice = "voice/KYO02A_MAY0002.ogg"
    "真由理" "「那个，恩，在Ｌａｂ哦。刚刚回来的说。手机电池没有电了，没能和你联络。抱歉啦」"

    "不太明白她在说什么。"



    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0003"
    $ current_voice = "voice/KYO02A_MAY0003.ogg"
    "真由理" "「顺便一说红莉栖酱也在Ｌａｂ哦。但她刚刚才到就是了」"

    "越来越难懂了。"
    "但……算了。"
    "真由理现在正在和我打电话。"
    "也知道她在哪里。在Ｌａｂ。真由理现在在Ｌａｂ，这就足够了。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0005"
    $ current_voice = "voice/KYO02A_OKA0005.ogg"
    "伦太郎" "「真由理，留在Ｌａｂ，千万不要去别的地方，好吗？」"

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0004"
    $ current_voice = "voice/KYO02A_MAY0004.ogg"
    "真由理" "「啊、嗯、明白了」"

    window hide


    call hide_phone

    "我挂了电话，抬起头和菲利斯简单地告别了，急匆匆地向Ｌａｂ赶去。"
    window hide



    $ loadBG(0,"BG05E1")

    "来到了显像管工房门前——"
    "飞冲上楼梯，打开了玄关的门。"
    window hide


    $ loadBG(2,"BG_BLACK")
    play se "SGSE316"




    hide screen phonebtn
    "扑进了Ｌａｂ，在那里……"
    window hide


    $ loadBG(0,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    "是两手沾满面包粉的真由理。"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0005"
    $ current_voice = "voice/KYO02A_MAY0005.ogg"
    "真由理" "「啊，欢迎回伦，小冈伦」"
    play bgm "BGM13"
    "真由理这么说着，一边用门牙啃着指尖上的面粉块。"
    "胸口中的冰冷的结块终于化开了。"
    "我重重地舒了一口气，用手擦去额头上沁出的汗水。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RHETORIC"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RHETORIC"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RHETORIC"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TAUTOLOGY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TAUTOLOGY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TAUTOLOGY"])

    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0006"
    $ current_voice = "voice/KYO02A_OKA0006.ogg"
    "伦太郎" "「{color=#f00}修辞法（ｒｈｅｔｏｒｉｃ）{/color}错了哦，真由理。那变成{color=#f00}同意反复(ｔａｕｔｏｌｏｇｙ){/color}了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0006"
    $ current_voice = "voice/KYO02A_MAY0006.ogg"
    "真由理" "「呃？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0007"
    $ current_voice = "voice/KYO02A_OKA0007.ogg"
    "伦太郎" "「『欢迎回伦＝欢迎回来＋小冈伦』应该是那样的。但是你说『欢迎回伦，小冈伦』就成了『欢迎回来＋小冈伦×２』了，那样的话语法就不自然了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0007"
    $ current_voice = "voice/KYO02A_MAY0007.ogg"
    "真由理" "「啊哈哈，确实说不定是那样的。但是那个说法，有种『ＭａｙＱｕｅｅｎ＋Ｎｙａ²』的感觉，挺可爱的不是吗」"
    "朝我露出了无忧无虑的微笑的真由理……"
    "虽然不太明白我在说什么，但是这样就好。"
    "这种完全无法预测走向的展开，才是这个Ｌａｂ的真正面貌和精髓的同时，也是开发出未来道具所不可欠缺的要素啊……"
    "嘛这样就好。总之我现在已经回到了日常，能放心了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HADMAND"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HADMAND"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HADMAND"])
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0008"
    $ current_voice = "voice/KYO02A_OKA0008.ogg"
    "伦太郎" "「那，你的手是怎么会变成那样和{color=#f00}哈德蒙德{/color}一样的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0008"
    $ current_voice = "voice/KYO02A_MAY0008.ogg"
    "真由理" "「啊，这个吗？　这是，面粉哟ー」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0009"
    $ current_voice = "voice/KYO02A_OKA0009.ogg"
    "伦太郎" "「看了就知道了，我是在问为什么会变成这样」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0009"
    $ current_voice = "voice/KYO02A_MAY0009.ogg"
    "真由理" "「啊，那个呢，因为正在帮桶子君的忙的说」"
    "她那沾满了面粉的手指指向了厨房的方向。"
    "朝那里看去，在灶台前站着一个像水桶一般的男子。"
    window hide


    $ loadBG(2,"BG01E")

    stop bgm 



    "是桶子。"
    "因为缩着身子，所以感觉就像水桶一样了。"
    play bgm "BGM22"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0010"
    $ current_voice = "voice/KYO02A_OKA0010.ogg"
    "伦太郎" "「你，你在干什么呀，桶子……？」"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0000"
    $ current_voice = "voice/KYO02A_DAR0000.ogg"
    "至" "「被米稻酱触到了萌点」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0011"
    $ current_voice = "voice/KYO02A_OKA0011.ogg"
    "伦太郎" "「米稻酱……？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAIMAI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAIMAI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAIMAI"])
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0001"
    $ current_voice = "voice/KYO02A_DAR0001.ogg"
    "至" "「说起米稻酱的话就是{color=#f00}Ｃｏｏｋｉｎｇ爱ＤＯＬＬ（ＬｏｖｅＤｏｌｌ）米米米稻(まいまいまいね){/color}酱吧常考」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0012"
    $ current_voice = "voice/KYO02A_OKA0012.ogg"
    "伦太郎" "「也就是说……？」"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0002"
    $ current_voice = "voice/KYO02A_DAR0002.ogg"
    "至" "「也就是说正在做料理。为了开发评议会做的料理。虽然出去买了零食，但是光靠那些是不够的吧？」"
    "到现在为止这样的对话躲避球游戏已经进行了三次了，但是我依然没能掌握情况。"
    "我再次试图搞清楚现状。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0013"
    $ current_voice = "voice/KYO02A_OKA0013.ogg"
    "伦太郎" "「为什么必须要你来做？」"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0003"
    $ current_voice = "voice/KYO02A_DAR0003.ogg"
    "至" "「交给我来做有什么不好的吗？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0014"
    $ current_voice = "voice/KYO02A_OKA0014.ogg"
    "伦太郎" "「虽然没什么不好的……你觉得披萨怎么样？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PIZZARAT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PIZZARAT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PIZZARAT"])
    "确实在别的世界线上，桶子点了３个{color=#f00}逼胜客{/color}的披萨。"
    "有那些披萨的话，足够评议会的时候吃的了。"
    window hide



    $ loadBG(2,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "但是回答我的是真由理。"
    "真由理就像要做手术前的外科医生一样，举着两只手说道。"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0010"
    $ current_voice = "voice/KYO02A_MAY0010.ogg"
    "真由理" "「逼胜客它，今天不开门」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0015"
    $ current_voice = "voice/KYO02A_OKA0015.ogg"
    "伦太郎" "「关门？　今天是那家店关门休业的日子吗？」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0011"
    $ current_voice = "voice/KYO02A_MAY0011.ogg"
    "真由理" "「不是预定好的休业，而是临时的。桶子君在打了电话之后，那么说的」"
    "桶子背对着我点了点头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0012"
    $ current_voice = "voice/KYO02A_MAY0012.ogg"
    "真由理" "「是不是发生什么了啊？　比如做披萨的酱用完了什么的……」"
    "不可能吧……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0013"
    $ current_voice = "voice/KYO02A_MAY0013.ogg"
    "真由理" "「所以说就是那样，逼胜客今天关门了」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0014"
    $ current_voice = "voice/KYO02A_MAY0014.ogg"
    "真由理" "「『那么作为替代好像吃Ｋｉｔｃｈｅｎ・次郎的炸肉饼啊』这么说了，真由喜就说『那我们来自己做吧』于是桶子君就……」"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0004"
    $ current_voice = "voice/KYO02A_DAR0004.ogg"
    "至" "「刚好昨天的节目里，米稻酱就做了炸肉饼。因为在硬盘里还有录像，所以就一边看着那个一边试着做了……」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0015"
    $ current_voice = "voice/KYO02A_MAY0015.ogg"
    "真由理" "「所以真由喜就在帮桶子君的忙」"
    window hide


    $ loadBG(2,"BG01E")



    "朝着电视看去，大概是米稻酱的美少女举着她的食指站在画面上。"
    "好像是暂停在某个画面了。"
    "桶子和之前一样站在灶台前面，观察着天麸罗锅里的油温。"
    "真由理也回到了之前干活的位置。"
    "站在桶子边上，给浸泡过小麦粉和鸡蛋的肉团子抹上面粉。"
    "就这么让他们做下去没问题吧……？"
    "一丝不安划过脑海。"

    stop bgm 
    "说起来，红莉栖在哪里？"
    "这么想着，于是去开发室里瞄了一眼……"
    window hide


    $ loadBG(2,"BG03A4")



    "有了。"
    "红莉栖坐在ＰＣ的显示器前，噼噼啪啪地敲打着键盘。"
    "我悄悄地走到她背后，轻声说道。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_2GET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_2GET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_2GET"])
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0016"
    $ current_voice = "voice/KYO02A_OKA0016.ogg"
    "伦太郎" "「还会用{color=#f00}２ＧＥＴ{/color}么？　栗悟饭与龟波波哟」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA09"),"True","lh/CRS_BSA09a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0000"
    $ current_voice = "voice/KYO02A_CRS0000.ogg"
    "红莉栖" "「为，为啥你会知道啊！」"
    "红莉栖慌张地关闭了显示器的电源，转过身来张开双手试图挡住背后的画面。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0017"
    $ current_voice = "voice/KYO02A_OKA0017.ogg"
    "伦太郎" "「有我的魔眼的话，那种程度的事简直就是小菜一碟！唔哈哈哈哈！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0001"
    $ current_voice = "voice/KYO02A_CRS0001.ogg"
    "红莉栖" "「才不是在上{color=#f00}＠Ｃｈａｎｎｅｌ{/color}呢。只是在稍微调查一个东西」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0018"
    $ current_voice = "voice/KYO02A_OKA0018.ogg"
    "伦太郎" "「调查东西？　时间机器已经完成了，还有什么要调查的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB05"),"True","lh/CRS_BSB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0002"
    $ current_voice = "voice/KYO02A_CRS0002.ogg"
    "红莉栖" "「唔咕……」"
    "红莉栖悔恨地咬着嘴唇。"
    "是想改变话题吗，她悄悄地移开了视线说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM26"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0003"
    $ current_voice = "voice/KYO02A_CRS0003.ogg"
    "红莉栖" "「比起那个，真是太好了呢」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0019"
    $ current_voice = "voice/KYO02A_OKA0019.ogg"
    "伦太郎" "「什么……？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0004"
    $ current_voice = "voice/KYO02A_CRS0004.ogg"
    "红莉栖" "「真由理的事」"
    "不明白她在说什么。"
    "红莉栖应该不知道在前一条世界线上，我们收到了恐吓信，而且真由理也去向不明这件事啊……"
    "当然不仅限于她。"
    "桶子和真由理也不知道这件事吧。"
    window hide


    $ loadBG(2,"BG01E")



    "我朝厨房方向瞄了一眼。"
    "两个人一边哼着愉快的歌，一边做着肉丸子。"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0005"
    $ current_voice = "voice/KYO02A_DAR0005.ogg"
    "至" "「♪炸一下的话～就是肉丸子哦～」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0016"
    $ current_voice = "voice/KYO02A_MAY0016.ogg"
    "真由理" "「♪卷心菜～波动炮～」"
    $ stopvoc("DAR")
    play DAR "KYO02A_DAR0006"
    $ current_voice = "voice/KYO02A_DAR0006.ogg"
    "至" "「啊哈哈，真由氏，卷心菜波动是什么呀？」"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0017"
    $ current_voice = "voice/KYO02A_MAY0017.ogg"
    "真由理" "「诶，桶子不知道嘛？　卷心菜波动炮是……」"
    "回到身边的日常……平稳的光景……"
    "但是这样的日常，就算世界线稍有偏离，就会分崩离析。"
    "我对此十分清楚。"
    "如果在这个未来，有什么事情发生的话该怎么办？"
    "并不能保证以后什么也不会发生。"
    "或许为了那个时候，稍微和红莉栖说明一下情况也是不错的选择。"
    "这么想着，我又一次将目光移回了开发室，开口说道。"
    window hide



    $ loadBG(2,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0020"
    $ current_voice = "voice/KYO02A_OKA0020.ogg"
    "伦太郎" "「呐，克里斯提娜，稍微有点事想说……可以吧？」"
    window hide



    $ loadBG(0,"BG05E1")

    "和红莉栖一起走下了楼梯，在显像管工房门口……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0005"
    $ current_voice = "voice/KYO02A_CRS0005.ogg"
    "红莉栖" "「怎么了，把我带到这种地方……」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0021"
    $ current_voice = "voice/KYO02A_OKA0021.ogg"
    "伦太郎" "「啊啊，事实上呢……」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我向红莉栖说明了之前的世界线的经历。"
    "虽然因此也不得不说明了进行过时间跳跃这件事，但是她好像很快就接受了这个事实。"
    window hide


    $ loadBG(0,"BG05E1")

    show screen phonebtn
    show screen phoneSD1
    "今天如果是在别的世界线的话，工房应该会提早打烊，不过好像这条世界线上还没有。"
    "店里的灯光还十分明亮，里面的４２型显像管电视机还通着电。"
    "店长的身影还在店里。他正站在店的中央像仁王像一样伫立着，看着晚间新闻。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0006"
    $ current_voice = "voice/KYO02A_CRS0006.ogg"
    "红莉栖" "「原来如此，明白你的意思了」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0007"
    $ current_voice = "voice/KYO02A_CRS0007.ogg"
    "红莉栖" "「虽然让你说了那么多很不好意思，但实际上，这是我第二次听说这些了」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0022"
    $ current_voice = "voice/KYO02A_OKA0022.ogg"
    "伦太郎" "「第二次……？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0008"
    $ current_voice = "voice/KYO02A_CRS0008.ogg"
    "红莉栖" "「是的，第二次……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0009"
    $ current_voice = "voice/KYO02A_CRS0009.ogg"
    "红莉栖" "「总之听了刚才的话之后，大概的情况我已经了解了，你身上发生过什么我也知道了」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0010"
    $ current_voice = "voice/KYO02A_CRS0010.ogg"
    "红莉栖" "「但只有一点还想确认一下」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0011"
    $ current_voice = "voice/KYO02A_CRS0011.ogg"
    "红莉栖" "「现在有收到过Ｄｍａｉｌ吗？ｉｃｈｓ发送过来的，恐吓信什么的……」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "大概已经消失了……"
    "这条世界线上，真由理并没有被掳走。"
    "这么想着的我打开了手机……"
    window hide


    "和想象的一员，果然ｉｃｈｓ发送的恐吓信消失得无影无踪。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC01"),"True","lh/CRS_ALC01a~ipad.png") at right0 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0012"
    $ current_voice = "voice/KYO02A_CRS0012.ogg"
    "红莉栖" "「看起来没有呢」"
    "注意到的时候，不知何时我已和红莉栖并肩而立。"
    "看着我手中的手机画面，红莉栖继续说道。"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0013"
    $ current_voice = "voice/KYO02A_CRS0013.ogg"
    "红莉栖" "「呐，这三封ｍａｉｌ是什么？　看起来好像也是Ｄｍａｉｌ的样子……」"
    "恐怕是来自之前的世界线，从真由理的手机发送的Ｄｍａｉｌ吧。"
    "为了确认而打开了它们。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY01"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY02"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY03"]




    "果然和我想的一样。"
    "『真由理的外出』『必须阻止下来』『会被诱拐的！』"
    "收到了这样的邮件，过去的我肯定就采取了行动，世界线才会变成现在这样吧。"
    "正因如此，真由理现在才会在Ｌａｂ里吧。"
    "在Ｌａｂ里面，厨房边上站着，欢快地唱着炸肉饼之歌也是因为那些事。"
    "没有问题。什么问题也没有。"
    "但……还是有一件令我在意的事情。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0023"
    $ current_voice = "voice/KYO02A_OKA0023.ogg"
    "伦太郎" "「好奇怪啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC06"),"True","lh/CRS_ALC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0014"
    $ current_voice = "voice/KYO02A_CRS0014.ogg"
    "红莉栖" "「什么……？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0024"
    $ current_voice = "voice/KYO02A_OKA0024.ogg"
    "伦太郎" "「这三封Ｄｍａｉｌ，全部都是今天下午１５点２０分收到的」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0025"
    $ current_voice = "voice/KYO02A_OKA0025.ogg"
    "伦太郎" "「但是我之前的世界线上发送的时间是１８点２０分前后。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0026"
    $ current_voice = "voice/KYO02A_OKA0026.ogg"
    "伦太郎" "「发送到的时间是交给桶子去处理的」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0027"
    $ current_voice = "voice/KYO02A_OKA0027.ogg"
    "伦太郎" "「最后确认真由理在Ｌａｂ的时间是１５点１６分，所以就拜托桶子把Ｄｍａｉｌ发送到那个时候了」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0015"
    $ current_voice = "voice/KYO02A_CRS0015.ogg"
    "红莉栖" "「所以那就设定为１５点２０分？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0028"
    $ current_voice = "voice/KYO02A_OKA0028.ogg"
    "伦太郎" "「啊啊」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0016"
    $ current_voice = "voice/KYO02A_CRS0016.ogg"
    "红莉栖" "「那，有什么奇怪的地方吗？」"
    hide screen phoneSD1
    window hide

    call hide_phone

    $ loadBG(0,"IBGX043")

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0029"
    $ current_voice = "voice/KYO02A_OKA0029.ogg"
    "伦太郎" "「电话微波炉（暂）是只能以１小时为单位来发送的。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0030"
    $ current_voice = "voice/KYO02A_OKA0030.ogg"
    "伦太郎" "「也就是定时器的１秒钟是现实的一小时，按照这样的比例向过去发送」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0031"
    $ current_voice = "voice/KYO02A_OKA0031.ogg"
    "伦太郎" "「那么助手哦。『１５点２０分』是『１８点２０分』的几个小时之前？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0017"
    $ current_voice = "voice/KYO02A_CRS0017.ogg"
    "红莉栖" "「『３小时前』」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0032"
    $ current_voice = "voice/KYO02A_OKA0032.ogg"
    "伦太郎" "「正是如此，但是三小时前的话——也就是要将电话微波炉（暂）设定为３秒」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0033"
    $ current_voice = "voice/KYO02A_OKA0033.ogg"
    "伦太郎" "「但是另一方面，根据到目前为止的实验结果来看，将Ｄｍａｉｌ发送到一小时之前是不可能的事情。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0034"
    $ current_voice = "voice/KYO02A_OKA0034.ogg"
    "伦太郎" "「原因的话，就是电话微波炉（暂）的定时器如果设置为１秒的话，因为时间太短就不会产生放电现象。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0035"
    $ current_voice = "voice/KYO02A_OKA0035.ogg"
    "伦太郎" "「那么『３秒』会怎样呢？『３秒』的话放电现象会发生吗？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0036"
    $ current_voice = "voice/KYO02A_OKA0036.ogg"
    "伦太郎" "「而且在如此短的时间里，我还要按下真由理手机的放松按钮……」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0037"
    $ current_voice = "voice/KYO02A_OKA0037.ogg"
    "伦太郎" "「那会怎样呢？我能在桶子启动电话微波炉（暂）之后的３秒内，按下发送按钮吗？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0038"
    $ current_voice = "voice/KYO02A_OKA0038.ogg"
    "伦太郎" "「答案是否定的。肯定经过了３秒以上吧，那样的话就──」"
    window hide


    $ loadBG(0,"BG05E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0018"
    $ current_voice = "voice/KYO02A_CRS0018.ogg"
    "红莉栖" "「好好好好，明白了明白了。说到这里就行了，不用说下去也没关系。」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0019"
    $ current_voice = "voice/KYO02A_CRS0019.ogg"
    "红莉栖" "「让我来……告诉你答案吧？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0039"
    $ current_voice = "voice/KYO02A_OKA0039.ogg"
    "伦太郎" "「答案……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0020"
    $ current_voice = "voice/KYO02A_CRS0020.ogg"
    "红莉栖" "「很简单哦。电话微波炉被改良过了。定时器的一秒相当于现实的一分钟了。」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0021"
    $ current_voice = "voice/KYO02A_CRS0021.ogg"
    "红莉栖" "「所以向３小时之前发送Ｄｍａｉｌ也是可以做到的了。」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0022"
    $ current_voice = "voice/KYO02A_CRS0022.ogg"
    "红莉栖" "「『３小时』是『１８０分钟』──桥田只是简单地将微波炉设定为『１８０秒』而已」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0040"
    $ current_voice = "voice/KYO02A_OKA0040.ogg"
    "伦太郎" "「『１８０秒』的话，放电现象显然是有足够的时间发生的……是这样啊」"
    "红莉栖点了点头。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0041"
    $ current_voice = "voice/KYO02A_OKA0041.ogg"
    "伦太郎" "「进行改良的是谁？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0023"
    $ current_voice = "voice/KYO02A_CRS0023.ogg"
    "红莉栖" "「当然是我」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0042"
    $ current_voice = "voice/KYO02A_OKA0042.ogg"
    "伦太郎" "「那么想问一下。为什么你在别的世界线并没有进行这样的改良？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0024"
    $ current_voice = "voice/KYO02A_CRS0024.ogg"
    "红莉栖" "「那样的问题就算问我也很难回答啊……大概，是没钱吧？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0025"
    $ current_voice = "voice/KYO02A_CRS0025.ogg"
    "红莉栖" "「在改良的过程中，用了非常昂贵的零件。」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0026"
    $ current_voice = "voice/KYO02A_CRS0026.ogg"
    "红莉栖" "「如果无法入手那些零件的话，估计就会放弃改良了吧。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0043"
    $ current_voice = "voice/KYO02A_OKA0043.ogg"
    "伦太郎" "「这样的话在这条世界线里，那些资金是哪里来的呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0027"
    $ current_voice = "voice/KYO02A_CRS0027.ogg"
    "红莉栖" "「是魔改造计划剩下来的资金」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0044"
    $ current_voice = "voice/KYO02A_OKA0044.ogg"
    "伦太郎" "「魔改造……计划？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0028"
    $ current_voice = "voice/KYO02A_CRS0028.ogg"
    "红莉栖" "「等一下，那个也不知道吗？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0029"
    $ current_voice = "voice/KYO02A_CRS0029.ogg"
    "红莉栖" "「『未来道具魔改造计划』──不是你提出来的计划吗？」"
    "啊啊，说起来，拜托Ｄｍａｉｌ的发送设定的时候，桶子也说过……"
    "『魔改造过了真好啊』什么的……。"
    "但是并不知道具体的情况。"
    "我眯起眼睛向红莉栖继续问了下去。"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0045"
    $ current_voice = "voice/KYO02A_OKA0045.ogg"
    "伦太郎" "「那是啥啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0030"
    $ current_voice = "voice/KYO02A_CRS0030.ogg"
    "红莉栖" "「哈……果然不记得了呢。肯定是Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ的缘故」"
    "好像是那样的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0031"
    $ current_voice = "voice/KYO02A_CRS0031.ogg"
    "红莉栖" "「那关于『秋叶原发明大赛』的事呢？」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0046"
    $ current_voice = "voice/KYO02A_OKA0046.ogg"
    "伦太郎" "「啊啊，那个的话我是知道的」"
    "我从口袋里取出传单，朝着红莉栖的方向打开。"
    window hide


    $ loadBG(2,"IBG024A")



    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0032"
    $ current_voice = "voice/KYO02A_CRS0032.ogg"
    "红莉栖" "「那样的话说起来就很简单了。也就，这么回事」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0047"
    $ current_voice = "voice/KYO02A_OKA0047.ogg"
    "伦太郎" "「但是除了这个传单就什么也不知道了。好好地给我说明一下吧」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0033"
    $ current_voice = "voice/KYO02A_CRS0033.ogg"
    "红莉栖" "「所以说，你不知道在哪里看到了这个传单以后，突然说出『来参加这个竞赛！』这样的话，肯定是因为奖金的关系吧」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0048"
    $ current_voice = "voice/KYO02A_OKA0048.ogg"
    "伦太郎" "「好失礼啊！毕竟是我这样的人，比起为了钱更像是为了名声吧」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0034"
    $ current_voice = "voice/KYO02A_CRS0034.ogg"
    "红莉栖" "「嘛总而言之就是这样，就把实验室里各种各样的玩意送去参展了。」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0049"
    $ current_voice = "voice/KYO02A_OKA0049.ogg"
    "伦太郎" "「不准把道具叫做玩意！」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0035"
    $ current_voice = "voice/KYO02A_CRS0035.ogg"
    "红莉栖" "「但是，你自己也是这么考虑的吧？」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0036"
    $ current_voice = "voice/KYO02A_CRS0036.ogg"
    "红莉栖" "「『这个样子参赛是不幸的。我们要赢取大奖，所以有进行改良的必要』说了那样的话，然后──」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0050"
    $ current_voice = "voice/KYO02A_OKA0050.ogg"
    "伦太郎" "「于是就开始了『未来道具魔改造计划』吗……」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0037"
    $ current_voice = "voice/KYO02A_CRS0037.ogg"
    "红莉栖" "「正是如此」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0038"
    $ current_voice = "voice/KYO02A_CRS0038.ogg"
    "红莉栖" "「虽然说，其实我并没有听到那个发言就是了」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0039"
    $ current_voice = "voice/KYO02A_CRS0039.ogg"
    "红莉栖" "「魔改造计划开始的时间是在一个月之前的样子。那个时候我还不在Ｌａｂ……」"
    window hide


    $ loadBG(2,"BG_BLACK")



    "根据红莉栖所说的，通过我提案的魔改造计划，未来道具被改良为如下的样子。"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "首先是未来道具１号机『比特粒子炮』。这个装置到目前为止只能通过扣动扳机来切换电视机的频道。"
    "但是现在在枪身上加了一个按钮，所以可以通过按下那个按钮来切断电视机的电源了。"
    "然后是未来道具２号机『竹蜻蜓照相机』——"
    "虽然该装置的竹筒上面装有摄像头，但上面的摄像头会隨著竹蜻蜓而高速旋转，导致看拍出來的视频的時候会让人看到头晕。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GYRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GYRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GYRO"])
    "现在那个道具上加了{color=#f00}陀螺仪{/color}，因此摄像头拍出来的图像可以拍出固定的图像了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PH"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PH"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PH"])
    "未来道具３号机『难道是JOJO系的吗！？』新加入了测定试验者的唾液{color=#f00}ｐＨ{/color}值的功能。"
    "也就是所说的测谎仪，通过试验者的拇指是否流汗来判断他有没有撒谎。"
    "但是通过追加新的机能，装置的可信度变高了。不如说离伪装成真正的测谎仪又近了一步。"
    "未来道具４号机『蒸汽蛇』没有受到特别的改良。"
    "好像是因为看起来过于危险，没有在竞赛中获奖的可能性，于是没有成为魔改造计划的一部分。"
    "然后还有……未来道具５号机『又把无聊的东西接一起了Ｂｙ五右卫门』是吹风机和吸尘器的结合体。"
    "改造后新加入了空气净化机。这样一来这台机器排出的气体也会变得绿色，对环境保护有一定的好处。"
    "未来道具６号机『荧光棒·Ｓａｂｅｒ』在发光后，里面的血浆会凝固这一点是非常的不合理的。"
    "魔改造计划消除了这一缺陷。现在血浆不会凝固了，而且质感上来书也更加接近真正的血液。"
    "最后，脱胎换骨的是，未来道具７号机『攻壳机动迷彩球』。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OELD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OELD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OELD"])
    "至今为止作为显示部分的６寸的显像管电视换成了超高分辨率的{color=#f00}液晶屏幕{/color}"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_20MEN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_20MEN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_20MEN"])
    "这些屏幕有１２个五边形和２０个六边形贴在一个和普通足球一样形状的{color=#f00}截角二十面体{/color}上面。"
    "各个显示屏的对角线上，设置了高性能的广角摄像头，可以将拍摄到的画面传送到对面的显示屏上。"
    "但唯一美中不足的一点就是启动时间太长了。"
    window hide







    $ loadBG(0,"BG05E1")
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0051"
    $ current_voice = "voice/KYO02A_OKA0051.ogg"
    "伦太郎" "「就算如此，资金预算还是很充足的……。也就是剩下的一部分，用来改良了电话微波炉（暂）」"
    $ stopvoc("OKA")
    play OKA "KYO02A_OKA0052"
    $ current_voice = "voice/KYO02A_OKA0052.ogg"
    "伦太郎" "「到底是谁给了那么多钱……」"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0040"
    $ current_voice = "voice/KYO02A_CRS0040.ogg"
    "红莉栖" "「那是……」"

    stop bgm 
    "在那个时候——"
    $ stopvoc("MAY")
    play MAY "KYO02A_MAY0018"
    $ current_voice = "voice/KYO02A_MAY0018.ogg"
    "真由理" "「呜啊啊啊啊────！！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM09"
    "突然，传来了一阵撕心裂肺的悲鸣。"
    "是真由理的声音。声音从我的天灵盖直贯而入。"
    "抬起头来，窗户的另一侧正在跳动着的……"
    "发散着红色的光芒的正体是——"
    $ stopvoc("CRS")
    play CRS "KYO02A_CRS0041"
    $ current_voice = "voice/KYO02A_CRS0041.ogg"
    "红莉栖" "「着火了哟，冈部！快点！」"
    "红莉栖一个箭步冲了出去，向着楼道内侧飞奔进去。"
    "我也没有犹豫，紧接着她追了进去。"

    hide screen phoneSD1
    window hide



    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
