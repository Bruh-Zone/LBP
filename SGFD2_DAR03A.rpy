label SGFD2_DAR03A:
    window hide


    $ loadBG(0,"IBG029A")

    play bgm "BGM26"


    $ date="8/15"
    $ day = "SUN"
    hide screen phonebtn
    show screen phoneSD1

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0000"
    $ current_voice = "voice/DAR03A_MAY0000.ogg"
    "真由理" "「嘿，这个角色的服装，真的非常可爱。设计得如此精湛的服装，可是非常稀有的了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0000"
    $ current_voice = "voice/DAR03A_DAR0000.ogg"
    "至" "「是啊。果然角色设计的色野(Ｓｈｉｋｉｎｏ)Ｓｍｉｌｅ简直就是头顶青天灵魂附体啊」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0001"
    $ current_voice = "voice/DAR03A_MAY0001.ogg"
    "真由理" "「最近，经常能见到这个人的画呢」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0001"
    $ current_voice = "voice/DAR03A_DAR0001.ogg"
    "至" "「好像是一波爆发的样子。在今天Ｃｏｓｐｌａｙ广场也是，由Ｓｍｉｌｅ氏进行角色设计的『厂长丛书系列』的Ｃｏｓｐｌａｙ偶尔能看到一两个」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0002"
    $ current_voice = "voice/DAR03A_MAY0002.ogg"
    "真由理" "「嗯。那种的褶边略多一点，大约还有点露出部分，ＣＯＳ的效果会更加好吧」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0002"
    $ current_voice = "voice/DAR03A_DAR0002.ogg"
    "至" "「但是『厂长丛书系列』啊，工口同人本略少啊。要是多出点的话就好了。今天看见的工口同人本也就两个」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0003"
    $ current_voice = "voice/DAR03A_MAY0003.ogg"
    "真由理" "「桶子君，我觉得把工口同人本堂堂正正地摆出来也并不是什么好的做法吧～」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0003"
    $ current_voice = "voice/DAR03A_DAR0003.ogg"
    "至" "「不过，说起来我没有料想到会有那么残酷的争夺战这一点」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0004"
    $ current_voice = "voice/DAR03A_DAR0004.ogg"
    "至" "「嘛，虽然大神的作品已经通过伙伴们Ｇｅｔ了，所以没关系。但是如果说没有他们的话，那就麻烦了啊」"
    window hide
    play se "SGSE803"




    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0004"
    $ current_voice = "voice/DAR03A_MAY0004.ogg"
    "真由理" "「啊，有邮件。可能是萌郁的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0005"
    $ current_voice = "voice/DAR03A_DAR0005.ogg"
    "至" "「难道说，是说她一直迷路，现在终于好不容易抵达了会场？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0005"
    $ current_voice = "voice/DAR03A_MAY0005.ogg"
    "真由理" "「啊哈哈。怎么会呢。会场已经关门了」"

    stop se

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0006"
    $ current_voice = "voice/DAR03A_MAY0006.ogg"
    "真由理" "「那个，说了什么呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0007"
    $ current_voice = "voice/DAR03A_MAY0007.ogg"
    "真由理" "「哇哇，“现在，在Ｌａｂ楼下”的说」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0008"
    $ current_voice = "voice/DAR03A_MAY0008.ogg"
    "真由理" "「那我还是去看下吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE024"

    "真由理慌慌张张地出去后很快就把桐生氏带了回来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0009"
    $ current_voice = "voice/DAR03A_MAY0009.ogg"
    "真由理" "「哈呼，真是担心死我了。电话不接，短信也不回。」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0000"
    $ current_voice = "voice/DAR03A_MOE0000.ogg"
    "萌郁" "「对……不起」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0006"
    $ current_voice = "voice/DAR03A_DAR0006.ogg"
    "至" "「哦，桐生氏乙～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0001"
    $ current_voice = "voice/DAR03A_MOE0001.ogg"
    "萌郁" "「…………」"
    "桐生氏没有和我正视，匆忙地低下头。"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0010"
    $ current_voice = "voice/DAR03A_MAY0010.ogg"
    "真由理" "「难道说，迷路了吗？　因为夏Ｃｏｍｉ人数实在太多了，第一次来的话还是很容易迷路的」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0002"
    $ current_voice = "voice/DAR03A_MOE0002.ogg"
    "萌郁" "「嗯……，在那种地方」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "桐生氏拿着手机快速地打着字。"
    "冈部称她为『闪光的指压师(Ｓｈｉｎｉｎｇ　Ｆｉｎｇｅｒ)』，看来不是夸大其词。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play se "SGSE803"


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0011"
    $ current_voice = "voice/DAR03A_MAY0011.ogg"
    "真由理" "「啊，有邮件？　那个……」"

    stop se

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0012"
    $ current_voice = "voice/DAR03A_MAY0012.ogg"
    "真由理" "「“虽然去了会场，但好不容易来到Ｃｏｓｐｌａｙ广场却一直在闲逛”的说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0013"
    $ current_voice = "voice/DAR03A_MAY0013.ogg"
    "真由理" "「抱歉啊，萌郁。果然，要是早上和你一起去就好了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0007"
    $ current_voice = "voice/DAR03A_DAR0007.ogg"
    "至" "「所以说啊，最后想问问你，黑猫的Ｃｏｓ服到底穿没穿。大概一小时之前就想问了」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0003"
    $ current_voice = "voice/DAR03A_MOE0003.ogg"
    "萌郁" "「没穿……」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0004"
    $ current_voice = "voice/DAR03A_MOE0004.ogg"
    "萌郁" "「连到底去哪里换衣服……我都不知道」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0014"
    $ current_voice = "voice/DAR03A_MAY0014.ogg"
    "真由理" "「但是没关系。还有明后两天时间」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0005"
    $ current_voice = "voice/DAR03A_MOE0005.ogg"
    "萌郁" "「嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0015"
    $ current_voice = "voice/DAR03A_MAY0015.ogg"
    "真由理" "「哈～欠」"
    "真由理突然打了个大哈欠。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0016"
    $ current_voice = "voice/DAR03A_MAY0016.ogg"
    "真由理" "「那么，明天还要赶早，我就差不多该回去了。萌郁和桶子君打算接下来干嘛？」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0006"
    $ current_voice = "voice/DAR03A_MOE0006.ogg"
    "萌郁" "「我……也回去」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0008"
    $ current_voice = "voice/DAR03A_DAR0008.ogg"
    "至" "「我到底该干嘛呢？今天也住在这吧」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0017"
    $ current_voice = "voice/DAR03A_MAY0017.ogg"
    "真由理" "「桶子君，你可要好好地洗个澡啊」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0009"
    $ current_voice = "voice/DAR03A_DAR0009.ogg"
    "至" "「要是还有力气的话」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0018"
    $ current_voice = "voice/DAR03A_MAY0018.ogg"
    "真由理" "「那么萌郁，顺道跟我一起回去吧」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0007"
    $ current_voice = "voice/DAR03A_MOE0007.ogg"
    "萌郁" "「好啊」"
    $ stopvoc("MAY")
    play MAY "DAR03A_MAY0019"
    $ current_voice = "voice/DAR03A_MAY0019.ogg"
    "真由理" "「那么明天见，桶子君」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0010"
    $ current_voice = "voice/DAR03A_DAR0010.ogg"
    "至" "「哦。我也期待明天，能够瞻仰下桐生氏的cos」"
    $ stopvoc("MOE")
    play MOE "DAR03A_MOE0008"
    $ current_voice = "voice/DAR03A_MOE0008.ogg"
    "萌郁" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE024"


    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0011"
    $ current_voice = "voice/DAR03A_DAR0011.ogg"
    "至" "「呼，接下，来」"
    "又变成一个人了。"
    window hide


    $ loadBG(2,"BG02A1")



    "一直呆在一起的冈伦和牧濑氏今天也没有看见啊。"
    "到底是怎么了。"
    "虽然已经检查完战利品了。"
    "因为起得太早了，加上今天走的路也不少，虽然太阳还没有下山但是已经非常困了。如果现在不睡觉的话明天早上就起不来了。"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0012"
    $ current_voice = "voice/DAR03A_DAR0012.ogg"
    "至" "「啊，但是在这之前，不去看下夏Ｃｏｍｉ实况帖的话可不行」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0013"
    $ current_voice = "voice/DAR03A_DAR0013.ogg"
    "至" "「而且连同ｃｏｓｐｌａｙ的帖子也看下吧」"
    "坐到了一直开着机的ＰＣ前面。"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0014"
    $ current_voice = "voice/DAR03A_DAR0014.ogg"
    "至" "「…………」"
    hide screen phoneSD1
    hide screen phonebtn
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR001A"]]["Check"]=True
    $ loadBG(0,"EV_DAR001A",trans=Fade(0.1,0.5,0.1,color="fff"))
    $ renpy.pause(1.5,hard=True)




    $ loadBG(0,"BG02A1",trans=Fade(0.1,0.5,0.1,color="fff"))

    show screen phoneSD1
    play bgm "FD2BGM01"
    "话说回来，从那位Ｃｏｓｅｒ那拿到的创可贴该怎么处理呢。"
    "试着找了下，在裤子的口袋里面找到了。"
    "仔细看了看，发现已经有些褶皱了。"
    "那个女孩，看起来非常的可爱，没准她的写真还在哪个新闻杂志上面刊登过。"
    window hide


    $ loadBG(2,"IBG030A")



    hide screen phonebtn
    "试着在＠ｃｈａｎｎｅｌ上面搜索Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ这个词"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0015"
    $ current_voice = "voice/DAR03A_DAR0015.ogg"
    "至" "「哦，好像有几个不错的记录。粉丝们辛苦了。我看看哦……」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0016"
    $ current_voice = "voice/DAR03A_DAR0016.ogg"
    "至" "「喂，等，等等，这不就是目击情报吗」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0017"
    $ current_voice = "voice/DAR03A_DAR0017.ogg"
    "至" "「嘛，但是除我之外还有人能够一眼看出是筷女的Ｃｏｓ这一点，说真的我确实没有想到」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0018"
    $ current_voice = "voice/DAR03A_DAR0018.ogg"
    "至" "「那么，其他的……事呢？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0019"
    $ current_voice = "voice/DAR03A_DAR0019.ogg"
    "至" "「『在夏Ｃｏｍｉ会场握住了黑衣男子的奇怪的东西』」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0020"
    $ current_voice = "voice/DAR03A_DAR0020.ogg"
    "至" "「为毛会上这种鬼帖子」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0021"
    $ current_voice = "voice/DAR03A_DAR0021.ogg"
    "至" "「也就是说工口的话题咯我懂了。怎么看都感觉是昭和时代的表达方式啊真的非常感谢」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0022"
    $ current_voice = "voice/DAR03A_DAR0022.ogg"
    "至" "「一边说着，Ｃｌｉｃｋ」"
    "显示器上立马刷新出帖子。"
    hide screen phoneSD1
    window hide
    call screen achan("txt/ATCH_001.txt")





    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KOTEHAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KOTEHAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KOTEHAN"])
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0023"
    $ current_voice = "voice/DAR03A_DAR0023.ogg"
    "至" "「啊啊，这个１是Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的{color=#f00}固定名{/color}啊」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OSSAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OSSAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OSSAN"])
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0024"
    $ current_voice = "voice/DAR03A_DAR0024.ogg"
    "至" "「这感觉……，１是女……看起来是女的，其实是{color=#f00}埼玉的大叔{/color}吧！」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0025"
    $ current_voice = "voice/DAR03A_DAR0025.ogg"
    "至" "「握着不得了的东西什么的。呼呼，快去进行工口的联想吧这种感觉很明显吧」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOJAKU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOJAKU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOJAKU"])
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0026"
    $ current_voice = "voice/DAR03A_DAR0026.ogg"
    "至" "「现在这年头，还会有人上这种当吗。啊，{color=#f00}情弱{/color}的话还是有可能会被骗到的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0027"
    $ current_voice = "voice/DAR03A_DAR0027.ogg"
    "至" "「但是感觉还是蛮有趣的。再往下看看吧」"
    window hide
    call screen achan("txt/ATCH_002.txt")









    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0028"
    $ current_voice = "voice/DAR03A_DAR0028.ogg"
    "至" "「超次要的角色ｃｏｓ……啥的？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0029"
    $ current_voice = "voice/DAR03A_DAR0029.ogg"
    "至" "「感觉就像是Ｃｈｏｐ子的ｃｏｓｅｒ做的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0030"
    $ current_voice = "voice/DAR03A_DAR0030.ogg"
    "至" "「…………」"
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR001A"]]["Check"]=True
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR001A"]]["Check"]=True
    $ loadBG(0,"EV_DAR001A",trans=Fade(0.1,0.5,0.1,color="fff"))
    $ renpy.pause(1.5,hard=True)

    $ loadBG(0,"IBG030A",trans=Fade(0.1,0.5,0.1,color="fff"))
    call screen achan("txt/ATCH_003.txt")
    with dissolve












    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0031"
    $ current_voice = "voice/DAR03A_DAR0031.ogg"
    "至" "「难道说，那个女孩？　不是为了吸引眼球？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0032"
    $ current_voice = "voice/DAR03A_DAR0032.ogg"
    "至" "「诶，那么站在那儿的黑衣男子，是我？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0033"
    $ current_voice = "voice/DAR03A_DAR0033.ogg"
    "至" "「手……好像碰到了……又好像没碰到……。不对不对，说起来我本来就没穿着什么黑衣服，也没有给她递纸条」"
    "那么就是别人咯"
    "真是非常在意筷女氏写的暗号"
    window hide


    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0034"
    $ current_voice = "voice/DAR03A_DAR0034.ogg"
    "至" "「Ｂ１４　７Ｈ　８Ｈ　Ｙ９１」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0035"
    $ current_voice = "voice/DAR03A_DAR0035.ogg"
    "至" "「这到底是意味着什么……」"
    play se "SGSE024"

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0000"
    $ current_voice = "voice/DAR03A_CRS0000.ogg"
    "红莉栖" "「ｈｅｌｌｏ」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0036"
    $ current_voice = "voice/DAR03A_DAR0036.ogg"
    "至" "「噢？　牧濑氏，我以为你今天不来嘞」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0001"
    $ current_voice = "voice/DAR03A_CRS0001.ogg"
    "红莉栖" "「什么啊？只有桥田你一个人吗？嗯，那么……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA08"),"True","lh/CRS_ASA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0002"
    $ current_voice = "voice/DAR03A_CRS0002.ogg"
    "红莉栖" "「那个，别把ＨＥＮＴＡＩ书随意丢在床上」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0037"
    $ current_voice = "voice/DAR03A_DAR0037.ogg"
    "至" "「啊啊，抱歉抱歉。刚刚还在跟真由氏一起查看战利品」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0003"
    $ current_voice = "voice/DAR03A_CRS0003.ogg"
    "红莉栖" "「因为那个一般算是性骚扰了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0038"
    $ current_voice = "voice/DAR03A_DAR0038.ogg"
    "至" "「啊，牧濑氏，如果你有兴趣的话，想看的话也是可以的」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0004"
    $ current_voice = "voice/DAR03A_CRS0004.ogg"
    "红莉栖" "「你少来。真是的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0005"
    $ current_voice = "voice/DAR03A_CRS0005.ogg"
    "红莉栖" "「那个，比起这些，桥田。有件事情想问你。」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0039"
    $ current_voice = "voice/DAR03A_DAR0039.ogg"
    "至" "「啊？　什么？」"
    stop bgm 
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0006"
    $ current_voice = "voice/DAR03A_CRS0006.ogg"
    "红莉栖" "「Ｂ１４　７Ｈ　８Ｈ　Ｙ９１。这个暗号，有什么头绪吗？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0040"
    $ current_voice = "voice/DAR03A_DAR0040.ogg"
    "至" "「等等，牧濑氏你也是上＠ｃｈａｎｎｅｌ吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0007"
    $ current_voice = "voice/DAR03A_CRS0007.ogg"
    "红莉栖" "「唔！？」"
    "我把ＰＣ屏幕指给她看。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC02"),"True","lh/CRS_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM22"

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0008"
    $ current_voice = "voice/DAR03A_CRS0008.ogg"
    "红莉栖" "「啊，糟糕了……！　没想到你也会看到这种冷门帖子……！」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0041"
    $ current_voice = "voice/DAR03A_DAR0041.ogg"
    "至" "「牧濑氏啊，如果是想隐藏自己是＠ｃｈａｎｎｅｌ的使用者的话，聊天的对象就更得斟酌了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0009"
    $ current_voice = "voice/DAR03A_CRS0009.ogg"
    "红莉栖" "「但是我拒绝」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC02"),"True","lh/CRS_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0010"
    $ current_voice = "voice/DAR03A_CRS0010.ogg"
    "红莉栖" "「啊，不对，没法拒绝」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0042"
    $ current_voice = "voice/DAR03A_DAR0042.ogg"
    "至" "「那个回复，ＧＪ。从＠ｃｈａｎｎｅｌ的意义上来说」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0011"
    $ current_voice = "voice/DAR03A_CRS0011.ogg"
    "红莉栖" "「……请别和冈部说。拜托了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0043"
    $ current_voice = "voice/DAR03A_DAR0043.ogg"
    "至" "「嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA03"),"True","lh/CRS_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0012"
    $ current_voice = "voice/DAR03A_CRS0012.ogg"
    "红莉栖" "「那个，你难道，是不是打算要我做点什么奇怪的事！」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0013"
    $ current_voice = "voice/DAR03A_CRS0013.ogg"
    "红莉栖" "「如果是那样的话真的就是鬼畜变态了，真是看走眼了……！」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0044"
    $ current_voice = "voice/DAR03A_DAR0044.ogg"
    "至" "「不对，我还没有说这种话啊。就算再怎么样用工口Ｇａｍｅ的脑子思考对方也是牧濑氏吧常考」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC02"),"True","lh/CRS_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0014"
    $ current_voice = "voice/DAR03A_CRS0014.ogg"
    "红莉栖" "「不对，那个肯定是搞错了……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA09"),"True","lh/CRS_ASA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0015"
    $ current_voice = "voice/DAR03A_CRS0015.ogg"
    "红莉栖" "「……抱歉」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0045"
    $ current_voice = "voice/DAR03A_DAR0045.ogg"
    "至" "「那么，条件就是你脱下来的丝袜」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0016"
    $ current_voice = "voice/DAR03A_CRS0016.ogg"
    "红莉栖" "「给我下地狱去吧变态」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0046"
    $ current_voice = "voice/DAR03A_DAR0046.ogg"
    "至" "「我才不是变态。我是变态绅士」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0017"
    $ current_voice = "voice/DAR03A_CRS0017.ogg"
    "红莉栖" "「如果是绅士的话就不会提出这种无理的要求了，一般来说」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0047"
    $ current_voice = "voice/DAR03A_DAR0047.ogg"
    "至" "「嘛，随便了。ＯＫ，就让它成为秘密吧」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "就现在来说知不知道这情报对我来说都无所谓了"
    play bgm "BGM19"


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0018"
    $ current_voice = "voice/DAR03A_CRS0018.ogg"
    "红莉栖" "「桥田，那个帖子，你也看了吧。暗号的意思知道了吗？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0048"
    $ current_voice = "voice/DAR03A_DAR0048.ogg"
    "至" "「不知，我也是才看到的，还是不清楚」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0019"
    $ current_voice = "voice/DAR03A_CRS0019.ogg"
    "红莉栖" "「我觉得这反正是个钓鱼贴，放出这种问题，因为有点在意，所以不知不觉就认真起来了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0049"
    $ current_voice = "voice/DAR03A_DAR0049.ogg"
    "至" "「牧濑氏啊，就算已经暴露了身份，这么大量地用＠ｃｈ用语也不太好吧……」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0050"
    $ current_voice = "voice/DAR03A_DAR0050.ogg"
    "至" "「这破绽真的太多了，不用我告诉冈部你自己就会暴露的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0020"
    $ current_voice = "voice/DAR03A_CRS0020.ogg"
    "红莉栖" "「……以，以后，会注意的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0051"
    $ current_voice = "voice/DAR03A_DAR0051.ogg"
    "至" "「也就是说，这帖子真的是钓鱼贴吗？」"
    "如果这位就是我白天见到的筷女氏的话，我实在是看不出像是钓鱼的。"
    "新的帖子出现，现在试着追下后续的事情到底是怎么样的。"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_003.txt")



    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0052"
    $ current_voice = "voice/DAR03A_DAR0052.ogg"
    "至" "「哦哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KTKR"])
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0053"
    $ current_voice = "voice/DAR03A_DAR0053.ogg"
    "至" "「本人的ｃｏｓ图片{color=#f00}ｋｔｋｒ{/color}！」"
    "立马就点开附在上面的ＵＲＬ链接。"
    window hide



    $ loadBG(2,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BRKR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BRKR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BRKR"])
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0021"
    $ current_voice = "voice/DAR03A_CRS0021.ogg"
    "红莉栖" "「桥田，我想在网络上面应该更加慎重一点。说不定是{color=#f00}Ｂｒｏｃｏｌｌａ{/color}呢」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0054"
    $ current_voice = "voice/DAR03A_DAR0054.ogg"
    "至" "「看来你在这方面经验蛮丰富的嘛，我知道了」"
    "画面刷新了，显示屏上面显示的是——"
    window hide


    $ loadBG(2,"IBG031A")



    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0055"
    $ current_voice = "voice/DAR03A_DAR0055.ogg"
    "至" "「等，有了！」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0056"
    $ current_voice = "voice/DAR03A_DAR0056.ogg"
    "至" "「不是这样的事情吧。有没有搞错」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0022"
    $ current_voice = "voice/DAR03A_CRS0022.ogg"
    "红莉栖" "「这样期待又失望的样子真像一个小孩子……」"
    "我无视那些匿名的吐槽，继续往下看。"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_004.txt")



    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0057"
    $ current_voice = "voice/DAR03A_DAR0057.ogg"
    "至" "「嗯」"
    "输入完成。"
    "外面的天空什么时候变得这么黑了。"
    window hide



    $ loadBG(2,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0023"
    $ current_voice = "voice/DAR03A_CRS0023.ogg"
    "红莉栖" "「你刚刚在跟帖？　那个ＤａＳＨ就是……」"
    "从牧濑氏坐着的沙发，能看清我屏幕上的东西。"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0058"
    $ current_voice = "voice/DAR03A_DAR0058.ogg"
    "至" "「Ｄａｒｕ・ｔｈｅ・ＳｕｐｅｒＨａｃｋｅｒ。缩写就是ＤａＳＨ。我在接私活的时候，使用的匿名」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0024"
    $ current_voice = "voice/DAR03A_CRS0024.ogg"
    "红莉栖" "「你这家伙大概也是一位{color=#f00}厨二病{/color}吧」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0059"
    $ current_voice = "voice/DAR03A_DAR0059.ogg"
    "至" "「我还没有到冈部那种程度，又没妄想」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0025"
    $ current_voice = "voice/DAR03A_CRS0025.ogg"
    "红莉栖" "「好的好的妄想乙。后面不要把那个帖子往Ｈｅｎｔａｉ方向带就好。明明好不容易才进入暗号的解读方向」"
    "牧濑氏把『栗悟饭与龟波功』这样的网名写了上去完全暴露了自己。 "
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SAHSEN"])
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0060"
    $ current_voice = "voice/DAR03A_DAR0060.ogg"
    "至" "「{color=#f00}抱歉鸟{/color}。问了下胸围的事情反应蛮大的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0061"
    $ current_voice = "voice/DAR03A_DAR0061.ogg"
    "至" "「而且竟然连＠ｃｈａｎｎｅｌ的发帖内容都要管，这是何等的班长属性」"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_005.txt")    



    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0026"
    $ current_voice = "voice/DAR03A_CRS0026.ogg"
    "红莉栖" "「唔……是这样的嘛？」"
    window hide



    $ loadBG(2,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0062"
    $ current_voice = "voice/DAR03A_DAR0062.ogg"
    "红莉栖" "「呼呣……是这样的嘛？」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0027"
    $ current_voice = "voice/DAR03A_CRS0027.ogg"
    "红莉栖" "「桥田你刚刚否定的事情。暗号，可能是程序的一部分，这种可能性完全为０吗？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0063"
    $ current_voice = "voice/DAR03A_DAR0063.ogg"
    "至" "「是０吧。如果稍微懂点程序的话，就不可能问出这种问题。唉，所以啊，跟外行讨论问题就是费劲」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0028"
    $ current_voice = "voice/DAR03A_CRS0028.ogg"
    "红莉栖" "「唔……」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0064"
    $ current_voice = "voice/DAR03A_DAR0064.ogg"
    "至" "「那么我们就全力以赴吧。没准，真的能把暗号解开哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0029"
    $ current_voice = "voice/DAR03A_CRS0029.ogg"
    "红莉栖" "「是的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0065"
    $ current_voice = "voice/DAR03A_DAR0065.ogg"
    "至" "「而且这位助手，看起来已经兴致勃勃了」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0030"
    $ current_voice = "voice/DAR03A_CRS0030.ogg"
    "红莉栖" "「我不讨厌这种烧脑的游戏。反而能转换下心情」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0031"
    $ current_voice = "voice/DAR03A_CRS0031.ogg"
    "红莉栖" "「如果是和冈部还有你说话，聊着聊着话题就会变得很奇怪，然后感觉都不能像平时的自己一样说话了」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0032"
    $ current_voice = "voice/DAR03A_CRS0032.ogg"
    "红莉栖" "「或许是因为不是在说英语的关系吧」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0066"
    $ current_voice = "voice/DAR03A_DAR0066.ogg"
    "至" "「只不过因为牧濑氏你的本性就是变态吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0033"
    $ current_voice = "voice/DAR03A_CRS0033.ogg"
    "红莉栖" "「别把我跟你混为一谈ＨＥＮＴＡＩ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0034"
    $ current_voice = "voice/DAR03A_CRS0034.ogg"
    "红莉栖" "「但是你看，Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ对你的回帖有反应啊」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0067"
    $ current_voice = "voice/DAR03A_DAR0067.ogg"
    "至" "「诶？」"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_006.txt")



    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0068"
    $ current_voice = "voice/DAR03A_DAR0068.ogg"
    "至" "「但是啊，没啥自信啊」"
    "可以确定的是这个不是什么程序代码，那么到底怎样能够解读这个呢，真是搞不清楚。"
    "大言不惭地给自己冠上超级黑客的名号，只不过是为了保险起见才这么自称罢了。要是把自嘲的感觉加进去的话，就会给人一种“果然不是啊”这样的感觉一笑了之。"
    "总之，为了筷女氏，虽然不知道能不能做到但是还是试着调查一下吧。"
    window hide

    stop bgm 



    $ loadBG(0,"BG02N1",trans=fade)

    play bgm "BGM07"
    show screen phonebtn
    show screen phoneSD1
    "花了一个小时进行了一些思考，但完全没有头绪。"
    "那个帖子，我之后就再也没有回复了，后面就跟着很多“超级黑客跑了”“ＤａＳＨ放出失败宣言了嘛”这类的回帖。"
    "真的非常具有煽动力啊ＹＯ！"
    "明明开始的时候写了感觉是ＮＥＴＡ的。"
    "随便了，速度发出败北宣言吧……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0035"
    $ current_voice = "voice/DAR03A_CRS0035.ogg"
    "红莉栖" "「还真说不准到底是不是和秋叶原有关啊。只是在拿到纸条的时候听到了那样的单词而已，但是却没有特指秋叶原的证据」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0036"
    $ current_voice = "voice/DAR03A_CRS0036.ogg"
    "红莉栖" "「我想或许是时候宣布这帖子是钓鱼贴的宣言了」"
    "牧濑氏在这一个小时里面，一直刷着这个帖子并吐槽别人的回复。"
    "虽然说这能当做锻炼大脑的机会，但是真的一点干劲都没有。"
    "被说成是“自尊心肥大的纤细废宅”，恐怕是非常火大吧"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0037"
    $ current_voice = "voice/DAR03A_CRS0037.ogg"
    "红莉栖" "「……嗯？」 "
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0069"
    $ current_voice = "voice/DAR03A_DAR0069.ogg"
    "至" "「怎么了？」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0038"
    $ current_voice = "voice/DAR03A_CRS0038.ogg"
    "红莉栖" "「暗号被解开了，Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌｓ这样回复道」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0070"
    $ current_voice = "voice/DAR03A_DAR0070.ogg"
    "至" "「纳尼？」"
    "慌慌张张地刷新了下帖子。"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_007.txt")



    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0071"
    $ current_voice = "voice/DAR03A_DAR0071.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0072"
    $ current_voice = "voice/DAR03A_DAR0072.ogg"
    "至" "「やばう？」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0039"
    $ current_voice = "voice/DAR03A_CRS0039.ogg"
    "红莉栖" "「是不是打错了」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0040"
    $ current_voice = "voice/DAR03A_CRS0040.ogg"
    "红莉栖" "「如果是用手机输入文字的话，1的按键对应着あ行」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0041"
    $ current_voice = "voice/DAR03A_CRS0041.ogg"
    "红莉栖" "「按一下是“あ”。再按一下是“い”。按三次的话就是“う”」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0042"
    $ current_voice = "voice/DAR03A_CRS0042.ogg"
    "红莉栖" "「不好了（ヤバイ），如果在输入的时候，最后多按了一下的话，就是やばう……这样的情况也会发生吧」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0043"
    $ current_voice = "voice/DAR03A_CRS0043.ogg"
    "红莉栖" "「果然，很像是钓鱼贴」"
    window hide



    $ loadBG(2,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC01"),"True","lh/CRS_ASC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "说完，牧濑氏坐在沙发上面伸了个大懒腰"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0044"
    $ current_voice = "voice/DAR03A_CRS0044.ogg"
    "红莉栖" "「怎么回事，竟然花了那么久时间研究这个。我也是个闲人啊」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0073"
    $ current_voice = "voice/DAR03A_DAR0073.ogg"
    "至" "「牧濑是重度＠ｃｈ使用者这一点算是了解了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0074"
    $ current_voice = "voice/DAR03A_DAR0074.ogg"
    "至" "「但是啊，如果这不是钓鱼帖的话，要是真被卷入了什么不得了的事情的话该怎么办？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0045"
    $ current_voice = "voice/DAR03A_CRS0045.ogg"
    "红莉栖" "「就算是问我该怎么办也……，连Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的样子和本名都不知道，我们的话什么也做不了」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0075"
    $ current_voice = "voice/DAR03A_DAR0075.ogg"
    "至" "「她的脸啊……」"
    "我知道她长什么样。因为在白天的时候见过她。"
    "当然，也不能肯定就是她本人。"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0046"
    $ current_voice = "voice/DAR03A_CRS0046.ogg"
    "红莉栖" "「脸？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0076"
    $ current_voice = "voice/DAR03A_DAR0076.ogg"
    "至" "「虽然不知道她具体长什么样，但是因为穿着Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的ｃｏｓ服所以应该还是挺显眼的」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0047"
    $ current_voice = "voice/DAR03A_CRS0047.ogg"
    "红莉栖" "「没那回事吧。如果是夏Ｃｏｍｉ会场的话还可能些，但是我想她是不会穿着ｃｏｓ服来秋叶原的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0077"
    $ current_voice = "voice/DAR03A_DAR0077.ogg"
    "至" "「但是那种人也有」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0048"
    $ current_voice = "voice/DAR03A_CRS0048.ogg"
    "红莉栖" "「就在她有限的发言里可是只字未提那种事情啊。所以到底穿着Ｃｏｓ服没有是无法判断的」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0078"
    $ current_voice = "voice/DAR03A_DAR0078.ogg"
    "至" "「牧濑氏好烦啊」"
    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0049"
    $ current_voice = "voice/DAR03A_CRS0049.ogg"
    "红莉栖" "「如果是以想象为前提进行推理的话只不过是无稽之谈罢了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0050"
    $ current_voice = "voice/DAR03A_CRS0050.ogg"
    "红莉栖" "「那么，我肚子也饿了，那么我回去了。明天见」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA02"),"True","lh/CRS_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR03A_CRS0051"
    $ current_voice = "voice/DAR03A_CRS0051.ogg"
    "红莉栖" "「姑且，我在回去的时候会注意下跟Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ外貌差不多的人吧。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "这么说着，牧濑氏很快就回去了。"
    "我一边叹着气，一边看着帖子的最新留言"
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    call screen achan("txt/ATCH_008.txt")




    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0079"
    $ current_voice = "voice/DAR03A_DAR0079.ogg"
    "至" "「哦哦，钓鱼贴宣言是真的啊ｋｔｋｒ」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0080"
    $ current_voice = "voice/DAR03A_DAR0080.ogg"
    "至" "「牧濑氏现在肯定是脸上挂满了得意的表情」"
    window hide



    $ loadBG(2,"BG02N1")



    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0081"
    $ current_voice = "voice/DAR03A_DAR0081.ogg"
    "至" "「…………」"
    "跟帖网民也一副知道了的样子然后把帖子给沉了。"
    "但是——"
    "真的吗？"
    "当然最后的回复也确实是由同ＩＤ的人发表的。"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0082"
    $ current_voice = "voice/DAR03A_DAR0082.ogg"
    "至" "「筷女氏呢，应该是不会发布这种钓鱼贴的啊？」"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0083"
    $ current_voice = "voice/DAR03A_DAR0083.ogg"
    "至" "「隐藏＠ｃｈ使用者光是牧濑氏一个就已经足够了……」"
    "但只不过ＩＤ是同一个，完全没有可以确定是她本人写的证据。"
    "尤其是用移动端发布的，就更加……。"
    "确实可以肯定是从那个手机上面发布的，但是帖子里面也没必要写说是她本人发的贴。"
    "也就是说即使是从手机上面发的贴也有可能是其他人。"

    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0084"
    $ current_voice = "voice/DAR03A_DAR0084.ogg"
    "至" "「嗯，但是这样是不是想的太多了，果然」"
    "这也是经常出现的一个ｎｅｔａ。"
    "如果都一一认真回复了的话，就感觉自己被耍了，所谓“认真你就输了”。"
    $ stopvoc("DAR")
    play DAR "DAR03A_DAR0085"
    $ current_voice = "voice/DAR03A_DAR0085.ogg"
    "至" "「睡觉吧」"
    "冈伦今天好像也不会来了。"
    "为了明天，不早点休息可不行。"
    "揣着这满脑子的疑问，我锁定了电脑后横卧在了沙发上。"

    hide screen phonebtn
    $ loadBG(0,"BG_BLACK",trans=Fade(1,1,1))
    window hide
    hide screen phoneSD1
    window hide






    return
