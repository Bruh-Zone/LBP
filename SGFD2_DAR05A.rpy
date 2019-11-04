label SGFD2_DAR05A:
    window hide


    $ loadBG(0,"BG05A1")


    play bgm "FD2BGM04"


    $ date="8/16"
    show screen phonebtn
    show screen phoneSD1
    python:
        SndMail(92)
        RcvMail(93)
        ReadMail(93)
        RcvMail(94)
        ReadMail(94)
        RcvMail(95)
        ReadMail(95)
        SndMail(96)
        RcvMail(97)
        ReadMail(97)
        SndMail(98)
        RcvMail(99)
        ReadMail(99)
        RcvMail(100)
        ReadMail(100)
        RcvMail(101)
        ReadMail(101)

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0000"
    $ current_voice = "voice/DAR05A_DAR0000.ogg"
    "至" "「哈！……，最后这么快就回来了……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0001"
    $ current_voice = "voice/DAR05A_DAR0001.ogg"
    "至" "「明明说了今年要战两次的。没想到竟然跳过了购买同人志直接去了Ｃｏｓｐｌａｙ广场了。怎么看都是宅男失格啊非常感谢。」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0002"
    $ current_voice = "voice/DAR05A_DAR0002.ogg"
    "至" "「筷女氏，今天也不会在ｃｏｓｐｌａｙ广场……」"
    "今天未必会和昨天一样ｃｏｓ　Ｃｈｏｐｓｔｉｃｋ　ｇｉｒｌ，没准只是我没有找到，其实是在的吧。"
    window hide



    $ loadBG(0,"BG02A2",trans=Fade(1,1,1))
    play se "SGSE024"


    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0003"
    $ current_voice = "voice/DAR05A_DAR0003.ogg"
    "至" "「乙～」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0000"
    $ current_voice = "voice/DAR05A_OKA0000.ogg"
    "伦太郎" "「也就是说克里斯缇娜，是因为想在夏Ｃｏｍｉ上搜刮ＢＬ本才不得不去的吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0001"
    $ current_voice = "voice/DAR05A_OKA0001.ogg"
    "伦太郎" "「这不就是被你千唾万弃的所谓变态么！　快给我反省一下！」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0000"
    $ current_voice = "voice/DAR05A_CRS0000.ogg"
    "红莉栖" "「有关ＢＬ本的话我好像一句话都没说过。我只不过是对于真实的夏Ｃｏｍｉ到底是什么，想去亲身去体会下。没准会很有趣。」 "
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0004"
    $ current_voice = "voice/DAR05A_DAR0004.ogg"
    "至" "「你们从大中午开始就吵这种秀恩爱的架，爆炸吧现充……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0002"
    $ current_voice = "voice/DAR05A_OKA0002.ogg"
    "伦太郎" "「哦哦，桶子，今天来得好早啊？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0005"
    $ current_voice = "voice/DAR05A_DAR0005.ogg"
    "至" "「不是。因为在意昨天的事情，夏Ｃｏｍｉ的争夺战我一点也没上心」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0006"
    $ current_voice = "voice/DAR05A_DAR0006.ogg"
    "至" "「嘛，今天暂时没有我想要的猎物。第三天才是动真格的时候」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0001"
    $ current_voice = "voice/DAR05A_CRS0001.ogg"
    "红莉栖" "「简直就像输了比赛的拳击手，不对应该说更像是相扑选手的感觉」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0002"
    $ current_voice = "voice/DAR05A_CRS0002.ogg"
    "红莉栖" "「里面包含了很多的汗水……是吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0007"
    $ current_voice = "voice/DAR05A_DAR0007.ogg"
    "至" "「顺便说下已经换过两次衬衫了，但还是不行吗？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0003"
    $ current_voice = "voice/DAR05A_CRS0003.ogg"
    "红莉栖" "「快点去洗个澡吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0008"
    $ current_voice = "voice/DAR05A_DAR0008.ogg"
    "至" "「哦哦，牧濑氏，刚刚的那句话请再说一次。可以的话就用那种让人心动的语气」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0004"
    $ current_voice = "voice/DAR05A_CRS0004.ogg"
    "红莉栖" "「变态（ＨＥＮＴＡＩ）请自重」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0003"
    $ current_voice = "voice/DAR05A_OKA0003.ogg"
    "伦太郎" "「那么，昨天的事情到底是什么事情，能够详细说明吗，Ｍｙ　ｆａｒｏｖｉｔｅ　ｒｉｇｈｔ　ａｒｍ哟」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0009"
    $ current_voice = "voice/DAR05A_DAR0009.ogg"
    "至" "「但是我拒绝」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0004"
    $ current_voice = "voice/DAR05A_OKA0004.ogg"
    "伦太郎" "「诶？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0005"
    $ current_voice = "voice/DAR05A_CRS0005.ogg"
    "红莉栖" "「昨天的事情，那个暗号？　最后，帖子里说这个是胡说八道的」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0010"
    $ current_voice = "voice/DAR05A_DAR0010.ogg"
    "至" "「就是这样」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0005"
    $ current_voice = "voice/DAR05A_OKA0005.ogg"
    "伦太郎" "「暗号，吗。这可不能当作没听到。没准是跟“{color=#f00}机关{/color}”有关的冥咒术刻印(Ｏｃｃｌｕｔｉｃ・Ｅｎｉｇｍａ)」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0011"
    $ current_voice = "voice/DAR05A_DAR0011.ogg"
    "至" "「厨二病乙」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0006"
    $ current_voice = "voice/DAR05A_CRS0006.ogg"
    "红莉栖" "「这是冈部最好别知道的话」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0006"
    $ current_voice = "voice/DAR05A_OKA0006.ogg"
    "伦太郎" "「什么！？　还有对我凤凰院凶真隐瞒的事情，你是不是觉得自己很伟大呢，我的右臂啊，还有助手哦」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0007"
    $ current_voice = "voice/DAR05A_OKA0007.ogg"
    "伦太郎" "「也就是说打算背叛我吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA08"),"True","lh/CRS_AMA08a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0007"
    $ current_voice = "voice/DAR05A_CRS0007.ogg"
    "红莉栖" "「桥田，绝对不能告诉冈部。如果说了的话就把你的脑子削成生火腿那么薄的切片」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0012"
    $ current_voice = "voice/DAR05A_DAR0012.ogg"
    "至" "「牧濑氏，你的眼神太可怕了。那种轻蔑的眼光，虽然对我来说可是褒奖啊」"
    "都到这个地步了看来是暴露了。"
    "嘛，如果让冈伦知道的话，非得刨根问底不成，这种心情我还是知道的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0008"
    $ current_voice = "voice/DAR05A_CRS0008.ogg"
    "红莉栖" "「或者说桥田你真的相信那个说法？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0009"
    $ current_voice = "voice/DAR05A_CRS0009.ogg"
    "红莉栖" "「冈部暂且不说，我想桥田的语言组织能力还是有的」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB06"),"True","lh/OKA_ASB06a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0008"
    $ current_voice = "voice/DAR05A_OKA0008.ogg"
    "伦太郎" "「喂，虽然不知道你们在说什么，但别若无其事地贬低我啊」"
    hide lh6  with dissolve
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0013"
    $ current_voice = "voice/DAR05A_DAR0013.ogg"
    "至" "「虽然昨天没有回应，但在写了那个之后我偶尔还会遇见写帖子的那个筷女氏吧」 "
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0010"
    $ current_voice = "voice/DAR05A_CRS0010.ogg"
    "红莉栖" "「筷女氏？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0014"
    $ current_voice = "voice/DAR05A_DAR0014.ogg"
    "至" "「我是这么叫的」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0015"
    $ current_voice = "voice/DAR05A_DAR0015.ogg"
    "至" "「那个人，我不觉得是那种会写这种恶作剧回复的样子。」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0011"
    $ current_voice = "voice/DAR05A_CRS0011.ogg"
    "红莉栖" "「唔……。难道这就是传说中的一见钟情？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0016"
    $ current_voice = "voice/DAR05A_DAR0016.ogg"
    "至" "「当我看到Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的ｃｏｓ的时候，我就已经决定要娶她为妻了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0012"
    $ current_voice = "voice/DAR05A_CRS0012.ogg"
    "红莉栖" "「……你向她说了吗？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0017"
    $ current_voice = "voice/DAR05A_DAR0017.ogg"
    "至" "「没有，只不过在我心里面认定了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0013"
    $ current_voice = "voice/DAR05A_CRS0013.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0018"
    $ current_voice = "voice/DAR05A_DAR0018.ogg"
    "至" "「牧濑氏，你沉默起来好恐怖啊」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0019"
    $ current_voice = "voice/DAR05A_DAR0019.ogg"
    "至" "「总之就是这样，我的新娘筷女氏看来真的遇上了什么不得了的事情的话，很糟糕吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0020"
    $ current_voice = "voice/DAR05A_DAR0020.ogg"
    "至" "「而且在最后，写着有炸弹的字样」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0009"
    $ current_voice = "voice/DAR05A_OKA0009.ogg"
    "伦太郎" "「也就是说，让桶子一见钟情的那位筷女氏，找到炸弹后就去向不明咯！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC05"),"True","lh/OKA_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0010"
    $ current_voice = "voice/DAR05A_OKA0010.ogg"
    "伦太郎" "「……是我。现在又在听我说吗？　……啊啊，对了。那个女人，很有可能已经卷进了“机关”的阴谋里面」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC01"),"True","lh/OKA_ASC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0011"
    $ current_voice = "voice/DAR05A_OKA0011.ogg"
    "伦太郎" "「……哼，啊，我知道了。请别勉强。虽然是一个人但是被“机关追击”，如果要对抗他们的话还是要我出马的」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0012"
    $ current_voice = "voice/DAR05A_OKA0012.ogg"
    "伦太郎" "「既然知道的话，就行动吧。也不是什么正义感爆发啥的了。是为了向“机关”报一箭之仇。把她救出来只不过是顺便而已」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC05"),"True","lh/OKA_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0013"
    $ current_voice = "voice/DAR05A_OKA0013.ogg"
    "伦太郎" "「……呵呵呵，可能你们会觉得我很愚蠢吧？　但是这就是凤凰院凶真的活法，这就是命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0014"
    $ current_voice = "voice/DAR05A_OKA0014.ogg"
    "伦太郎" "「ＥＬ・ＰＳＹ・Ｃｏｎｇｒｏｏ」 "
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0021"
    $ current_voice = "voice/DAR05A_DAR0021.ogg"
    "至" "「妄想乙」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0015"
    $ current_voice = "voice/DAR05A_OKA0015.ogg"
    "伦太郎" "「所以说桶子啊，我也帮你一把吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0022"
    $ current_voice = "voice/DAR05A_DAR0022.ogg"
    "至" "「明明连详细的事情都不知道却还一副高高在上的表情，冈伦好酷」"
    "就这样，向冈伦解释了下昨天的事情。"

    stop bgm 
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "虽然牧濑氏一直反对向冈伦说这些，但是如果很好地避开“牧濑氏是＠ｃｈ用户”这个事情的话，牧濑氏还是很不情愿地接受了。"
    window hide


    $ loadBG(0,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM19"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0016"
    $ current_voice = "voice/DAR05A_OKA0016.ogg"
    "伦太郎" "「啊哈，原来如此」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0017"
    $ current_voice = "voice/DAR05A_OKA0017.ogg"
    "伦太郎" "「有一点我想问下──」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0018"
    $ current_voice = "voice/DAR05A_OKA0018.ogg"
    "伦太郎" "「为什么助手会知道＠ｃｈａｎｎｅｌ的这场争论？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0014"
    $ current_voice = "voice/DAR05A_CRS0014.ogg"
    "红莉栖" "「那个……是从桥田那里听到的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0019"
    $ current_voice = "voice/DAR05A_OKA0019.ogg"
    "伦太郎" "「什么！？　也就是说桶子是先跟助手说的这件事咯！　相对于我更信赖助手吗！？」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0020"
    $ current_voice = "voice/DAR05A_OKA0020.ogg"
    "伦太郎" "「谁才是未来道具研究所的首领，看来要在这里重申一下了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0023"
    $ current_voice = "voice/DAR05A_DAR0023.ogg"
    "至" "「厨二病就算了，也不会对话题有什么帮助」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0021"
    $ current_voice = "voice/DAR05A_OKA0021.ogg"
    "伦太郎" "「所以说就别无视我了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0022"
    $ current_voice = "voice/DAR05A_OKA0022.ogg"
    "伦太郎" "「……那位女子就这样消失在了秋叶原，肯定是卷入了这个阴谋里面」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0024"
    $ current_voice = "voice/DAR05A_DAR0024.ogg"
    "至" "「看来是冈部的得意领域啊。但是这次我也认同」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0023"
    $ current_voice = "voice/DAR05A_OKA0023.ogg"
    "伦太郎" "「真是少有的意见一致啊，桶子」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0015"
    $ current_voice = "voice/DAR05A_CRS0015.ogg"
    "红莉栖" "「桥田是想往这方面想吧。这可是阴谋论的典型」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0016"
    $ current_voice = "voice/DAR05A_CRS0016.ogg"
    "红莉栖" "「即使反对的人就在眼前，还是认同和自己意见一致的。」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0017"
    $ current_voice = "voice/DAR05A_CRS0017.ogg"
    "红莉栖" "「如果重视后者的意见的话，就只会被诱导到非常巧合的解释上去。这是一种有意无意的做法呢」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0024"
    $ current_voice = "voice/DAR05A_OKA0024.ogg"
    "伦太郎" "「不要因为说了无视你的意见就闹别扭啊克里斯提娜。身为助手可是很丢面子的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0018"
    $ current_voice = "voice/DAR05A_CRS0018.ogg"
    "红莉栖" "「才没有闹别扭」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0019"
    $ current_voice = "voice/DAR05A_CRS0019.ogg"
    "红莉栖" "「本来，明明连判断的根据都没有，就开始商谈关于Ｃｈｏｐｓｔｉｃｋ　ｇｉｒｌ被卷入事件的事宜，完全没有意义」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0020"
    $ current_voice = "voice/DAR05A_CRS0020.ogg"
    "红莉栖" "「如果是这样的话，还不如想办法去解读暗号，这样不是更有建设性么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0025"
    $ current_voice = "voice/DAR05A_OKA0025.ogg"
    "伦太郎" "「啊，这个的话绝对是关于机关的暗号。给我端正点态度。暗号的解读可是关系到生命的」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0021"
    $ current_voice = "voice/DAR05A_CRS0021.ogg"
    "红莉栖" "「冈部，你就别捣乱了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0026"
    $ current_voice = "voice/DAR05A_OKA0026.ogg"
    "伦太郎" "「你说什么！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0025"
    $ current_voice = "voice/DAR05A_DAR0025.ogg"
    "至" "「说起来牧濑氏，虽说你昨天没有参加暗号的解读，但回去后想到了什么吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0022"
    $ current_voice = "voice/DAR05A_CRS0022.ogg"
    "红莉栖" "「那之后，回去想了一会。但是，没法解出来」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0023"
    $ current_voice = "voice/DAR05A_CRS0023.ogg"
    "红莉栖" "「例如、试着把这暗号当成键盘的按键」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0027"
    $ current_voice = "voice/DAR05A_OKA0027.ogg"
    "伦太郎" "「嚯嚯、着眼点不错」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0024"
    $ current_voice = "voice/DAR05A_CRS0024.ogg"
    "红莉栖" "「根据日式键盘的话，用这顺序输入下假名」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0025"
    $ current_voice = "voice/DAR05A_CRS0025.ogg"
    "红莉栖" "「就这样把『Ｂ１４　７Ｈ　８Ｈ　Ｙ９１』试着按假名的输入方式打出来后」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0026"
    $ current_voice = "voice/DAR05A_CRS0026.ogg"
    "红莉栖" "「结果就是，完全不能变成一段话」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0026"
    $ current_voice = "voice/DAR05A_DAR0026.ogg"
    "至" "「有好好地试吗？」"
    "试着用实际的ＰＣ键盘输入。"
    window hide


    $ loadBG(2,"IBG032A")



    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0027"
    $ current_voice = "voice/DAR05A_DAR0027.ogg"
    "至" "「こぬう　やく　ゆく　んよぬ」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0027"
    $ current_voice = "voice/DAR05A_CRS0027.ogg"
    "红莉栖" "「呐？　能够成为一句话吗」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ANAGRAM"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ANAGRAM"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ANAGRAM"])
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0028"
    $ current_voice = "voice/DAR05A_OKA0028.ogg"
    "伦太郎" "「那么，这样按照{color=#f00}重排字谜{/color}的顺序进行顺序替换的话……如何？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0028"
    $ current_voice = "voice/DAR05A_DAR0028.ogg"
    "至" "「噢，冈伦挺行的嘛」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0028"
    $ current_voice = "voice/DAR05A_CRS0028.ogg"
    "红莉栖" "「嗯。重排字谜啊。那个，不怎么喜欢」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0029"
    $ current_voice = "voice/DAR05A_OKA0029.ogg"
    "伦太郎" "「才没有在问你喜欢什么讨厌什么。桶子试试看吧！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0029"
    $ current_voice = "voice/DAR05A_DAR0029.ogg"
    "至" "「嗯，等下。稍微试着想一下哈。而且，你们两位也想想啊」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0030"
    $ current_voice = "voice/DAR05A_DAR0030.ogg"
    "至" "「…………」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0030"
    $ current_voice = "voice/DAR05A_OKA0030.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0029"
    $ current_voice = "voice/DAR05A_CRS0029.ogg"
    "红莉栖" "「…………」"
    window hide


    $ loadBG(2,"BG02A2")



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0031"
    $ current_voice = "voice/DAR05A_DAR0031.ogg"
    "至" "「啊……有了……！　有了有了有了！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0030"
    $ current_voice = "voice/DAR05A_CRS0030.ogg"
    "红莉栖" "「真快啊」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0031"
    $ current_voice = "voice/DAR05A_OKA0031.ogg"
    "伦太郎" "「怎么了？　知道答案了吗！？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0032"
    $ current_voice = "voice/DAR05A_DAR0032.ogg"
    "至" "「『ぬくぬくゆう』，不是上个月新开的女仆按摩店吗！」"
    "正确的说是写成『ぬくぬくＹＯＵ』"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0031"
    $ current_voice = "voice/DAR05A_CRS0031.ogg"
    "红莉栖" "「女，女仆按摩店……。真是不入流」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0033"
    $ current_voice = "voice/DAR05A_DAR0033.ogg"
    "至" "「不，又不是风俗店。只不过是女仆加按摩而已」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA09"),"True","lh/CRS_ASA09a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0032"
    $ current_voice = "voice/DAR05A_CRS0032.ogg"
    "红莉栖" "「诶，啊，是，是这样的吗……。看来我搞混了……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0034"
    $ current_voice = "voice/DAR05A_DAR0034.ogg"
    "至" "「不过这天才少女，有着一个工口游戏的脑子啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA03"),"True","lh/CRS_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0032"
    $ current_voice = "voice/DAR05A_OKA0032.ogg"
    "伦太郎" "「但从知道的状况来看，那个店子里面确定有什么东西吧。没准有一扇通往异世界的大门」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0033"
    $ current_voice = "voice/DAR05A_OKA0033.ogg"
    "伦太郎" "「如果知道了的话，现在立马潜入到店子里搜查吧！　把现在手头有空的ｌａｂｍｅｍ找过来！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0035"
    $ current_voice = "voice/DAR05A_DAR0035.ogg"
    "至" "「噢，我也去。对那家店，有点感兴趣」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0036"
    $ current_voice = "voice/DAR05A_DAR0036.ogg"
    "至" "「也就是说，筷女氏是这家女仆按摩店的女仆咯，这样我就放心了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0037"
    $ current_voice = "voice/DAR05A_DAR0037.ogg"
    "至" "「虽然也有这种可能性。就算这是个陷阱也没有关系，多谢了哈」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0033"
    $ current_voice = "voice/DAR05A_CRS0033.ogg"
    "红莉栖" "「别给我过早地下结论。即使『ぬくぬくゆう』不错，但是没有用到所有的文字」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0034"
    $ current_voice = "voice/DAR05A_CRS0034.ogg"
    "红莉栖" "「剩下的还有『こ』『や』『ん』『よ』请解释下？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0034"
    $ current_voice = "voice/DAR05A_OKA0034.ogg"
    "伦太郎" "「唔？　唔，也是啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0035"
    $ current_voice = "voice/DAR05A_OKA0035.ogg"
    "伦太郎" "「哈，是这样啊！　这剩下的『よんこや』，也就是代表着『４５８』！"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0035"
    $ current_voice = "voice/DAR05A_CRS0035.ogg"
    "红莉栖" "「意思呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0036"
    $ current_voice = "voice/DAR05A_OKA0036.ogg"
    "伦太郎" "「实际上是全局的关键所在！」 "
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0036"
    $ current_voice = "voice/DAR05A_CRS0036.ogg"
    "红莉栖" "「别发病了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0037"
    $ current_voice = "voice/DAR05A_OKA0037.ogg"
    "伦太郎" "「哼，连这都不知道啊助手！　记着这些数字，去店内找！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0038"
    $ current_voice = "voice/DAR05A_DAR0038.ogg"
    "至" "「哦哦哦哦，冈伦好厉害！　今天简直文曲星附体！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0038"
    $ current_voice = "voice/DAR05A_OKA0038.ogg"
    "伦太郎" "「唔哈哈哈哈！　这是凤凰院凶真，所熟知的机关暗号！」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0039"
    $ current_voice = "voice/DAR05A_OKA0039.ogg"
    "伦太郎" "「好的，现在能够行动的Ｌａｂｍｅm有……真由理和指压师在夏Ｃｏｍｉ。刚刚Mr.布朗跟我说了打工战士在休息……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0039"
    $ current_voice = "voice/DAR05A_DAR0039.ogg"
    "至" "「可能阿万音氏也在夏Ｃｏｍｉ」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0040"
    $ current_voice = "voice/DAR05A_OKA0040.ogg"
    "伦太郎" "「那么，带着菲利斯和琉华子一起潜入吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0040"
    $ current_voice = "voice/DAR05A_DAR0040.ogg"
    "至" "「等下，冈伦真狡猾。我也要去」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0041"
    $ current_voice = "voice/DAR05A_OKA0041.ogg"
    "伦太郎" "「不行。这任务太危险了。桶子，你就在这里支援我吧。知道了吧？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0041"
    $ current_voice = "voice/DAR05A_DAR0041.ogg"
    "至" "「别开玩笑了！　你是准备抢我功劳吧！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0037"
    $ current_voice = "voice/DAR05A_CRS0037.ogg"
    "红莉栖" "「桥田，你没必要去」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0042"
    $ current_voice = "voice/DAR05A_DAR0042.ogg"
    "至" "「等下，牧濑氏你为什么也？　我虽然是处男但是我应该还是有去做个按摩的权利的！」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0038"
    $ current_voice = "voice/DAR05A_CRS0038.ogg"
    "红莉栖" "「你，现在，臭气熏天」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0043"
    $ current_voice = "voice/DAR05A_DAR0043.ogg"
    "至" "「什……什么？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0039"
    $ current_voice = "voice/DAR05A_CRS0039.ogg"
    "红莉栖" "「你觉得你能以连续两天去了夏Ｃｏｍｉ还不洗澡的状态去做按摩吗？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0040"
    $ current_voice = "voice/DAR05A_CRS0040.ogg"
    "红莉栖" "「结果就是被赶出去不让你进去。请想想女仆们的感受吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0044"
    $ current_voice = "voice/DAR05A_DAR0044.ogg"
    "至" "「牧濑氏……，真的非常感谢。终于让我注意到了，我现在就去洗澡」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0042"
    $ current_voice = "voice/DAR05A_OKA0042.ogg"
    "伦太郎" "「好的，这样的话你和助手就在这里待命。等着我的回复」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOCPE"])
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0043"
    $ current_voice = "voice/DAR05A_OKA0043.ogg"
    "伦太郎" "「如果我一个小时后还没有回来的话……助手啊，冰箱里的{color=#f00}Ｄｒ．Ｐｅｐｐｅｒ{/color}呢，全部都给你。还有请向我的父母，说声我爱他们」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0044"
    $ current_voice = "voice/DAR05A_OKA0044.ogg"
    "伦太郎" "「那么永别了！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE024"

    "冈部一个人找了个无理的借口从Ｌａｂ出发了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0041"
    $ current_voice = "voice/DAR05A_CRS0041.ogg"
    "红莉栖" "「反正潜入什么的是白费力气」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0045"
    $ current_voice = "voice/DAR05A_DAR0045.ogg"
    "至" "「诶？　什么意思？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0042"
    $ current_voice = "voice/DAR05A_CRS0042.ogg"
    "红莉栖" "「『ぬくぬくＹＯＵ』的存在，都已经是很大的巧合了，而且。恐怕不太可能跟这家店有关系」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0043"
    $ current_voice = "voice/DAR05A_CRS0043.ogg"
    "红莉栖" "「因为有字谜的存在真的非常讨厌。这种肆意的解释要多少有多少」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0046"
    $ current_voice = "voice/DAR05A_DAR0046.ogg"
    "至" "「你也不是在瞎猜？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0044"
    $ current_voice = "voice/DAR05A_CRS0044.ogg"
    "红莉栖" "「你就得了吧快给我去洗澡」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0047"
    $ current_voice = "voice/DAR05A_DAR0047.ogg"
    "至" "「你要偷窥的话……也不是不可以哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0045"
    $ current_voice = "voice/DAR05A_CRS0045.ogg"
    "红莉栖" "「谁要偷窥你啊变态！」"
    "就这样，一边等着冈伦的报告一边爽快地去洗澡。"

    stop bgm 
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG02A2")

    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM10"
    "就这样，过了将近一个小时冈伦都没有联系我们。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0048"
    $ current_voice = "voice/DAR05A_DAR0048.ogg"
    "至" "「果然是立了死亡ＦＬＡＧ啊」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0046"
    $ current_voice = "voice/DAR05A_CRS0046.ogg"
    "红莉栖" "「反正这时候，被可爱的女仆按摩按到爽吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0049"
    $ current_voice = "voice/DAR05A_DAR0049.ogg"
    "至" "「哦？　为什么这么生气呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0047"
    $ current_voice = "voice/DAR05A_CRS0047.ogg"
    "红莉栖" "「才没有生气呢。只不过在想事情而已」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0050"
    $ current_voice = "voice/DAR05A_DAR0050.ogg"
    "至" "「想啥？」"

    stop bgm 
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0048"
    $ current_voice = "voice/DAR05A_CRS0048.ogg"
    "红莉栖" "「那个暗号。难道就没有别的什么解读方法了吗」"
    play bgm "BGM15"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0051"
    $ current_voice = "voice/DAR05A_DAR0051.ogg"
    "至" "「也就是说，筷女氏被卷入了什么不得了的事情的可能性，还是有的咯？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0049"
    $ current_voice = "voice/DAR05A_CRS0049.ogg"
    "红莉栖" "「关于这个的话我已开始还是持有否定的观点的。万事不绝对，就算是现在也不能下定论」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0052"
    $ current_voice = "voice/DAR05A_DAR0052.ogg"
    "至" "「等下，别这么说嘛？　被你这样说，我感到好慌……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0050"
    $ current_voice = "voice/DAR05A_CRS0050.ogg"
    "红莉栖" "「Ｂ１４……７Ｈ……８Ｈ……Ｙ９１」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0051"
    $ current_voice = "voice/DAR05A_CRS0051.ogg"
    "红莉栖" "「Ｙ９１，没准是指９１年」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0052"
    $ current_voice = "voice/DAR05A_CRS0052.ogg"
    "红莉栖" "「７Ｈ和８Ｈ的话，７点和８点？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0053"
    $ current_voice = "voice/DAR05A_CRS0053.ogg"
    "红莉栖" "「但是这样理解的话Ｂ１４就没法解释了……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0053"
    $ current_voice = "voice/DAR05A_DAR0053.ogg"
    "至" "「Ｂ１４……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0054"
    $ current_voice = "voice/DAR05A_DAR0054.ogg"
    "至" "「哦！　就是那个，没准是展区号！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0054"
    $ current_voice = "voice/DAR05A_CRS0054.ogg"
    "红莉栖" "「哈？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0055"
    $ current_voice = "voice/DAR05A_DAR0055.ogg"
    "至" "「那个，Ｂ的话就是东馆」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    "从帆布背包里面拿出了一本很厚的夏Ｃｏｍｉ会展指南"
    "不出所料，Ｂ１４的摊位果然在东馆。"
    "今天上午，我虽然在东馆到处转悠，但并没有去这个展位。"
    "如果是这样的话不是又要回秋叶原了么。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0056"
    $ current_voice = "voice/DAR05A_DAR0056.ogg"
    "至" "「真由氏还在会场吧」"
    window hide
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "赶紧打个电话吧。"
    window hide






    $ stopvoc("X05")
    play voc "DAR05A_X050000"
    $ current_voice = "voice/DAR05A_X050000.ogg"
    "手机播音" "「您所拨打的电话，因信号原因，或电池没电，导致无法接听」"

    "啊呀。对了，在夏Ｃｏｍｉ这鬼地方打电话太困难了……。"
    window hide





    "然后我就一直拨着号继续打，终于在大概第五次的时候打通了。"
    window hide



    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0000"
    $ current_voice = "voice/DAR05A_MAY0000.ogg"
    "真由理" "「嘟嘟噜♪　我是真由喜」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0057"
    $ current_voice = "voice/DAR05A_DAR0057.ogg"
    "至" "「啊，真由氏？　是我」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0001"
    $ current_voice = "voice/DAR05A_MAY0001.ogg"
    "真由理" "「桶子君，你现在在哪？　虽然上午的时候还看到过你」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0058"
    $ current_voice = "voice/DAR05A_DAR0058.ogg"
    "至" "「我已经在回秋叶原的路上了。话说能拜托你一件事吗？」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0002"
    $ current_voice = "voice/DAR05A_MAY0002.ogg"
    "真由理" "「嗯。什么事？」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0059"
    $ current_voice = "voice/DAR05A_DAR0059.ogg"
    "至" "「我想拜托你现在赶紧去东馆的Ｂ１４的“腐食的苹果”的社团那里看看」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0003"
    $ current_voice = "voice/DAR05A_MAY0003.ogg"
    "真由理" "「那是桶子君的熟人吗？」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0060"
    $ current_voice = "voice/DAR05A_DAR0060.ogg"
    "至" "「不，完全不熟。如果那里有Ｃｈｏｐｓｔｉｃｋ　ｇｉｒｌ的ｃｏｓｅｒ的话，请通知我下」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0004"
    $ current_voice = "voice/DAR05A_MAY0004.ogg"
    "真由理" "「嗯，但是……」"
    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0005"
    $ current_voice = "voice/DAR05A_MAY0005.ogg"
    "真由理" "「那个，今天也没有见到萌郁。我一直在等她的说」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0061"
    $ current_voice = "voice/DAR05A_DAR0061.ogg"
    "至" "「诶，什么？」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0006"
    $ current_voice = "voice/DAR05A_MAY0006.ogg"
    "真由理" "「所以，不太好离开ｃｏｓｐｌａｙ广场……」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0062"
    $ current_voice = "voice/DAR05A_DAR0062.ogg"
    "至" "「阿万音氏呢？　今天来了没有？　来了的话让她帮你顶下」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0007"
    $ current_voice = "voice/DAR05A_MAY0007.ogg"
    "真由理" "「嗯，但是没有看见」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0063"
    $ current_voice = "voice/DAR05A_DAR0063.ogg"
    "至" "「是嘛……」"
    "我可做不到强行让别人去做事。"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0008"
    $ current_voice = "voice/DAR05A_MAY0008.ogg"
    "真由理" "「嗯，情况我清楚了。现在就去现场看看。Ｂ１４是不是？」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0064"
    $ current_voice = "voice/DAR05A_DAR0064.ogg"
    "至" "「嗯，真是抱歉啊。真的你只要去看一眼就行了」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0009"
    $ current_voice = "voice/DAR05A_MAY0009.ogg"
    "真由理" "「了解了的说♪　那么我挂了」"
    call hide_phone

    window hide


    hide screen phonemenu
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0065"
    $ current_voice = "voice/DAR05A_DAR0065.ogg"
    "至" "「唔……。真由氏，真的是天使」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0055"
    $ current_voice = "voice/DAR05A_CRS0055.ogg"
    "红莉栖" "「桥田，是不是太赶了点？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0056"
    $ current_voice = "voice/DAR05A_CRS0056.ogg"
    "红莉栖" "「虽然符合Ｂ１４。但是其他的暗号怎么解释呢？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0066"
    $ current_voice = "voice/DAR05A_DAR0066.ogg"
    "至" "「那个你想啊……，如果你真的去哪个摊位的话，肯定会有其他暗示的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0057"
    $ current_voice = "voice/DAR05A_CRS0057.ogg"
    "红莉栖" "「唔……」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0058"
    $ current_voice = "voice/DAR05A_CRS0058.ogg"
    "红莉栖" "「有显示符合Ｂ１４。如果去那里的话，就有可能找到跟７Ｈ有关的情报吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0059"
    $ current_voice = "voice/DAR05A_CRS0059.ogg"
    "红莉栖" "「比起『ぬくぬくＹＯＵ』的话，确实靠谱多了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0060"
    $ current_voice = "voice/DAR05A_CRS0060.ogg"
    "红莉栖" "「不过，如果这样的话就和递上纸条的黑衣男子还有秋叶原和说的那些话，没有什么太大的关系了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0067"
    $ current_voice = "voice/DAR05A_DAR0067.ogg"
    "至" "「这样子的话可能就能够得出答案了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0061"
    $ current_voice = "voice/DAR05A_CRS0061.ogg"
    "红莉栖" "「是这样的吧……」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0062"
    $ current_voice = "voice/DAR05A_CRS0062.ogg"
    "红莉栖" "「还有一个就是。夏Ｃｏｍｉ的举办时间有三天是不是？　如果Ｂ１４即是正确的，今天可能就不是昨天那个展台了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0068"
    $ current_voice = "voice/DAR05A_DAR0068.ogg"
    "至" "「那么就进下昨天和明天Ｂ１４展台团队的主页看看吧，试试发个邮件」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0069"
    $ current_voice = "voice/DAR05A_DAR0069.ogg"
    "至" "「虽然会被认为是奇怪的家伙」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0063"
    $ current_voice = "voice/DAR05A_CRS0063.ogg"
    "红莉栖" "「都做到这种地步了，你看来是不见棺材不落泪啊。那样的话，就去做好了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0070"
    $ current_voice = "voice/DAR05A_DAR0070.ogg"
    "至" "「难道说牧濑氏你也非常在意吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0064"
    $ current_voice = "voice/DAR05A_CRS0064.ogg"
    "红莉栖" "「嗯。关于暗号的解读我也想验证下。说成在意的话感觉有点不好」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0065"
    $ current_voice = "voice/DAR05A_CRS0065.ogg"
    "红莉栖" "「不管如何，现在还是等待报告吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "立马从电脑中找出了那两家参展团队的主页邮件地址，发送了咨询邮件。"
    "能在今天之内回复就好了。"
    stop bgm 




    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0071"
    $ current_voice = "voice/DAR05A_DAR0071.ogg"
    "至" "「噢！　冈伦的电话终于打过来了」"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)





    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0072"
    $ current_voice = "voice/DAR05A_DAR0072.ogg"
    "至" "「好的，喂」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0045"
    $ current_voice = "voice/DAR05A_OKA0045.ogg"
    "伦太郎" "「是我……」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0073"
    $ current_voice = "voice/DAR05A_DAR0073.ogg"
    "至" "「冈伦你怎么这么久不打电话过来」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0046"
    $ current_voice = "voice/DAR05A_OKA0046.ogg"
    "伦太郎" "「队伍太长了，没想到排了一个小时以上」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0074"
    $ current_voice = "voice/DAR05A_DAR0074.ogg"
    "至" "「啊，是啊。因为在开夏Ｃｏｍｉ所以秋叶原也有点乱」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0075"
    $ current_voice = "voice/DAR05A_DAR0075.ogg"
    "至" "「也就是说你终于进里面了咯？」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0047"
    $ current_voice = "voice/DAR05A_OKA0047.ogg"
    "伦太郎" "「啊啊……对了。唔……咕咕咕」"

    play bgm "BGM24"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0076"
    $ current_voice = "voice/DAR05A_DAR0076.ogg"
    "至" "「嗯？　怎么了？」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0048"
    $ current_voice = "voice/DAR05A_OKA0048.ogg"
    "伦太郎" "「没啥……已经，没问题了。菲利斯和琉华子，也安然无恙地潜入进去了──」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0049"
    $ current_voice = "voice/DAR05A_OKA0049.ogg"
    "伦太郎" "「稍微……微微微微！」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0077"
    $ current_voice = "voice/DAR05A_DAR0077.ogg"
    "至" "「稍微？，冈部？　冈部！？」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0050"
    $ current_voice = "voice/DAR05A_OKA0050.ogg"
    "伦太郎" "「但是，我好巧不巧地已经暴露了。现在，我在被困在手术台……接受拷问……」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0051"
    $ current_voice = "voice/DAR05A_OKA0051.ogg"
    "伦太郎" "「唔咿咿咿咿！　别这样……求你别这样！　脚心！　好疼！　别，啊啊啊……！」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0078"
    $ current_voice = "voice/DAR05A_DAR0078.ogg"
    "至" "「冈部……」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0052"
    $ current_voice = "voice/DAR05A_OKA0052.ogg"
    "伦太郎" "「可，可，可能，我中埋伏了。抱歉了，超级嗨客。之后的事情，就拜托……」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0079"
    $ current_voice = "voice/DAR05A_DAR0079.ogg"
    "至" "「稍微等下！　店里面有些什么线索吗？」"

    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0053"
    $ current_voice = "voice/DAR05A_OKA0053.ogg"
    "伦太郎" "「线索……没有。什么，都木有」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0054"
    $ current_voice = "voice/DAR05A_OKA0054.ogg"
    "伦太郎" "「Ｃｈｏｐｓｔｉｃｋ　ｇｉｒｌ也不在。昨天，好像也没有去夏Ｃｏｍｉ的服务员」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0055"
    $ current_voice = "voice/DAR05A_OKA0055.ogg"
    "伦太郎" "「关于４５８这数字的提示也没有……毫无，头绪──」"
    $ stopvoc("OKA")
    play OKA "DAR05A_OKA0056"
    $ current_voice = "voice/DAR05A_OKA0056.ogg"
    "伦太郎" "「我说了很痛啊啊啊啊！」"
    call hide_phone


    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0080"
    $ current_voice = "voice/DAR05A_DAR0080.ogg"
    "至" "「…………」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0066"
    $ current_voice = "voice/DAR05A_CRS0066.ogg"
    "红莉栖" "「…………」"
    window hide
    hide screen phonemenu

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0081"
    $ current_voice = "voice/DAR05A_DAR0081.ogg"
    "至" "「刚刚的对话，听到了吗？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0067"
    $ current_voice = "voice/DAR05A_CRS0067.ogg"
    "红莉栖" "「诶，诶诶……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0082"
    $ current_voice = "voice/DAR05A_DAR0082.ogg"
    "至" "「你怎么看？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0068"
    $ current_voice = "voice/DAR05A_CRS0068.ogg"
    "红莉栖" "「没想到，事情会变成这样。真是担心冈部。我们现在不快点赶过去的话……！」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0069"
    $ current_voice = "voice/DAR05A_CRS0069.ogg"
    "红莉栖" "「如果在被拷问的话，可能会把“没有线索”这话说出来──」"

    stop bgm 
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0083"
    $ current_voice = "voice/DAR05A_DAR0083.ogg"
    "至" "「可能……才不会有」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0070"
    $ current_voice = "voice/DAR05A_CRS0070.ogg"
    "红莉栖" "「怎么了明白了什么了嘛！？」"
    play bgm "FD2BGM10"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0084"
    $ current_voice = "voice/DAR05A_DAR0084.ogg"
    "至" "「不管怎么看，只不过是在做足疗而已（电疗）了，太痛了所以昏了过去。真是非常感谢」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0071"
    $ current_voice = "voice/DAR05A_CRS0071.ogg"
    "红莉栖" "「……诶，是……这样的嘛？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0085"
    $ current_voice = "voice/DAR05A_DAR0085.ogg"
    "至" "「因为，是那种店嘛」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0072"
    $ current_voice = "voice/DAR05A_CRS0072.ogg"
    "红莉栖" "「……可恶！　那我岂不是白担心了！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0086"
    $ current_voice = "voice/DAR05A_DAR0086.ogg"
    "至" "「牧濑氏真是意外的单纯啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA08"),"True","lh/CRS_ASA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0073"
    $ current_voice = "voice/DAR05A_CRS0073.ogg"
    "红莉栖" "「烦，烦死了别开玩笑啊」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0074"
    $ current_voice = "voice/DAR05A_CRS0074.ogg"
    "红莉栖" "「真是，扶不上墙的那个凤凰院！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0087"
    $ current_voice = "voice/DAR05A_DAR0087.ogg"
    "至" "「总之，好像和『ぬくぬくＹＯＵ』没有什么关系」 "
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0075"
    $ current_voice = "voice/DAR05A_CRS0075.ogg"
    "红莉栖" "「和我预想的一样。我一开始就说了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0088"
    $ current_voice = "voice/DAR05A_DAR0088.ogg"
    "至" "「好了好了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0089"
    $ current_voice = "voice/DAR05A_DAR0089.ogg"
    "至" "「之后，就是真由氏那边……」"
    "已经决定等待真由氏的电话了"

    stop bgm 
    window hide



    $ loadBG(0,"BG02A2")

    "过了大概１０分钟之后——"


    stop bgm 



    "真由氏打了电话过来。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)


label L_RING_RECEIVE_10:




    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0090"
    $ current_voice = "voice/DAR05A_DAR0090.ogg"
    "至" "「喂！」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0010"
    $ current_voice = "voice/DAR05A_MAY0010.ogg"
    "真由理" "「嘟嘟噜♪　我是真由喜」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0091"
    $ current_voice = "voice/DAR05A_DAR0091.ogg"
    "至" "「情况怎样？」 "

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0011"
    $ current_voice = "voice/DAR05A_MAY0011.ogg"
    "真由理" "「那个，大发现哟」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0092"
    $ current_voice = "voice/DAR05A_DAR0092.ogg"
    "至" "「诶！？　大发现！？　什么！？」"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BETTARIA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BETTARIA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BETTARIA"])

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0012"
    $ current_voice = "voice/DAR05A_MAY0012.ogg"
    "真由理" "「那个，『Ｐｅｔａｌｉａ』的伦敦先生的本子！」"

    play bgm "BGM22"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0093"
    $ current_voice = "voice/DAR05A_DAR0093.ogg"
    "至" "「……诶？」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0013"
    $ current_voice = "voice/DAR05A_MAY0013.ogg"
    "真由理" "「去了Ｂ１４之后，因为有非常棒的『Ｐｅｔａｌｉａ』本，情不自禁地就买买买了」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0094"
    $ current_voice = "voice/DAR05A_DAR0094.ogg"
    "至" "「不对，那个，真由氏，Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ呢……」"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHIMA"])

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0014"
    $ current_voice = "voice/DAR05A_MAY0014.ogg"
    "真由理" "「诶？　但是那附近是，不是雷ＮＥＴ翔岛而是Ｐｅｔａｌｉａ区，所以没有那种ＣＯＳＥＲ哟？」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0095"
    $ current_voice = "voice/DAR05A_DAR0095.ogg"
    "至" "「那么，你不能理解的暗号也没有咯？　Ｂ１４　７Ｈ　８Ｈ　Ｙ９１啥的」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0015"
    $ current_voice = "voice/DAR05A_MAY0015.ogg"
    "真由理" "「诶？　到底怎么一回事？　没有看到什么特别的」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0096"
    $ current_voice = "voice/DAR05A_DAR0096.ogg"
    "至" "「７Ｈ！　特别是７Ｈ有关的重要情报，有没有头绪？」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0016"
    $ current_voice = "voice/DAR05A_MAY0016.ogg"
    "真由理" "「那个……」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0017"
    $ current_voice = "voice/DAR05A_MAY0017.ogg"
    "真由理" "「四周都找不到」"
    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0018"
    $ current_voice = "voice/DAR05A_MAY0018.ogg"
    "真由理" "「虽然一边走，一边看同人志，但是也找不到」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0097"
    $ current_voice = "voice/DAR05A_DAR0097.ogg"
    "至" "「那么啊，试着问下那边展位的人吧？　还有，问下昨天在cosplay广场的」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0019"
    $ current_voice = "voice/DAR05A_MAY0019.ogg"
    "真由理" "「嗯，好的。稍微等下」"

    "电话另一头的真由氏的声音越来越小。"
    "好像在和别人交谈的样子。"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0020"
    $ current_voice = "voice/DAR05A_MAY0020.ogg"
    "真由理" "「久等了。７Ｈ啥的还有Ｂ１４，听都没听说过」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0098"
    $ current_voice = "voice/DAR05A_DAR0098.ogg"
    "至" "「那个ＣＯＳＥＲ呢？」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0021"
    $ current_voice = "voice/DAR05A_MAY0021.ogg"
    "真由理" "「那个呢，昨天好像没有来夏Ｃｏｍｉ」 "

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0099"
    $ current_voice = "voice/DAR05A_DAR0099.ogg"
    "至" "「是，是嘛……。真由氏，真是麻烦你了」"

    $ stopvoc("MAY")
    play MAY "DAR05A_MAY0022"
    $ current_voice = "voice/DAR05A_MAY0022.ogg"
    "真由理" "「嗯，给我介绍了不错的社团，我这边才要感谢你呢♪」"
    call hide_phone

    window hide



    stop bgm 
    hide screen phonemenu

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0076"
    $ current_voice = "voice/DAR05A_CRS0076.ogg"
    "红莉栖" "「看来是没戏了」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0100"
    $ current_voice = "voice/DAR05A_DAR0100.ogg"
    "至" "「哈……。我现在已经没辙了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0077"
    $ current_voice = "voice/DAR05A_CRS0077.ogg"
    "红莉栖" "「已经放弃了吗？　本身，这事情就没有你想象的那么严重的吧，你这么拼命也没有意义了」"
    "这个时候，贴在电脑显示屏上的创可贴映入眼帘。"
    "把它拿到手上，呆呆地看着。"
    "我反复地审视着呜啪萌萌的外表。"
    $ stopvoc("X06")
    play voc "DAR05A_X060000"
    $ current_voice = "voice/DAR05A_X060000.ogg"
    "？？？" "「这个创口贴，可以的话就用吧」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0101"
    $ current_voice = "voice/DAR05A_DAR0101.ogg"
    "至" "「真是能够让人守护一生的笑脸！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0078"
    $ current_voice = "voice/DAR05A_CRS0078.ogg"
    "红莉栖" "「哈！？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0102"
    $ current_voice = "voice/DAR05A_DAR0102.ogg"
    "至" "「我就是这位女神的骑士」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0079"
    $ current_voice = "voice/DAR05A_CRS0079.ogg"
    "红莉栖" "「等等，我眼前就有一个跟踪狂啊。你还是有点自觉吧？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0103"
    $ current_voice = "voice/DAR05A_DAR0103.ogg"
    "至" "「哎没事了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0080"
    $ current_voice = "voice/DAR05A_CRS0080.ogg"
    "红莉栖" "「你啊……」"
    play bgm "FD2BGM07"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0104"
    $ current_voice = "voice/DAR05A_DAR0104.ogg"
    "至" "「也就是说，看来要稍微用下我的独门秘技了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0081"
    $ current_voice = "voice/DAR05A_CRS0081.ogg"
    "红莉栖" "「秘技？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0105"
    $ current_voice = "voice/DAR05A_DAR0105.ogg"
    "至" "「把筷女氏的电话的位置，给找出来」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0082"
    $ current_voice = "voice/DAR05A_CRS0082.ogg"
    "红莉栖" "「怎样做？　难道说要黑进去吗？」 "
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0106"
    $ current_voice = "voice/DAR05A_DAR0106.ogg"
    "至" "「不对不对，并不是那么丧心病狂的事情了，现在这个时代，要确定个人情报还是很容易的」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0107"
    $ current_voice = "voice/DAR05A_DAR0107.ogg"
    "至" "「网络上不是经常发生这种事么。总之先去各种综合网站看看好了。」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0108"
    $ current_voice = "voice/DAR05A_DAR0108.ogg"
    "至" "「以正义的战士自居的＠ｃｈ们会自发地将网络上的细小的线索收集起来，最终来确定本人的方位」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0083"
    $ current_voice = "voice/DAR05A_CRS0083.ogg"
    "红莉栖" "「也就是说一个人也能搞咯？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0109"
    $ current_voice = "voice/DAR05A_DAR0109.ogg"
    "至" "「怎么就不行呢，常考」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0110"
    $ current_voice = "voice/DAR05A_DAR0110.ogg"
    "至" "「姑且，我在深网界还是蛮有名的黑客」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0084"
    $ current_voice = "voice/DAR05A_CRS0084.ogg"
    "红莉栖" "「你到底在说什么啊」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0111"
    $ current_voice = "voice/DAR05A_DAR0111.ogg"
    "至" "「真的啊」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0112"
    $ current_voice = "voice/DAR05A_DAR0112.ogg"
    "至" "「也就是说，这方面的朋友很多。要使用这样的人海战术什么的关系网还是有的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0085"
    $ current_voice = "voice/DAR05A_CRS0085.ogg"
    "红莉栖" "「……你不想跟敌人周旋了也就是说，现在，是认真考虑了的咯」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0113"
    $ current_voice = "voice/DAR05A_DAR0113.ogg"
    "至" "「嘛，因为筷女氏是Ｃｏｓｐｌａｙｅｒ，她的信息应该比普通人更多才对」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0114"
    $ current_voice = "voice/DAR05A_DAR0114.ogg"
    "至" "「而且最近使用网络的妹子，ＳＮＳ之类的都是把自己的信息毫无防备地暴露出来」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0115"
    $ current_voice = "voice/DAR05A_DAR0115.ogg"
    "至" "「筷女氏因为经常使用网络，应该查得很快的」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0086"
    $ current_voice = "voice/DAR05A_CRS0086.ogg"
    "红莉栖" "「会变成怎么样我可不知道啊……」"
    "果然还是被冈伦传染了么……"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "无视在一边发呆的牧濑氏，赶快进行作战。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG02A2",trans=fade)

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0116"
    $ current_voice = "voice/DAR05A_DAR0116.ogg"
    "至" "「来了来了！　查询完成！」"
    "连两个小时都没花，真的是神级技术啊。"
    "我的这群狐朋狗友还真是靠谱。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0087"
    $ current_voice = "voice/DAR05A_CRS0087.ogg"
    "红莉栖" "「没想到还真去干了啊……。桥田是和冈部无法与之相比的恐怖存在，现在终于了解了……」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0117"
    $ current_voice = "voice/DAR05A_DAR0117.ogg"
    "至" "「随时接受委托哦。如果你有想要找的人，跟我直接说就是」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0088"
    $ current_voice = "voice/DAR05A_CRS0088.ogg"
    "红莉栖" "「不要。我可没这种偷窥别人隐私的爱好」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0118"
    $ current_voice = "voice/DAR05A_DAR0118.ogg"
    "至" "「唔（吞口水）……那么，就是有被偷窥的爱好咯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0089"
    $ current_voice = "voice/DAR05A_CRS0089.ogg"
    "红莉栖" "「…………」"
    window hide


    $ loadBG(2,"IBG033A")



    hide screen phonebtn
    "丝毫不在意牧濑氏那杀人一般的眼神甩了甩膀子，我浏览了一遍通过同伴的帮助搞到手的个人情报。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0119"
    $ current_voice = "voice/DAR05A_DAR0119.ogg"
    "至" "「名字是……阿万音由季……」"
    "由季……由季碳啊。呵呵～"
    "说起来，阿万音这个姓氏我只知道和一个人有关系。"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0090"
    $ current_voice = "voice/DAR05A_CRS0090.ogg"
    "红莉栖" "「阿万音……可能是阿万音铃羽的家人」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0120"
    $ current_voice = "voice/DAR05A_DAR0120.ogg"
    "至" "「向她本人去询问下吧」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0091"
    $ current_voice = "voice/DAR05A_CRS0091.ogg"
    "红莉栖" "「但是今天她休息，冈部刚刚不是说了吗。她不在下面」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0121"
    $ current_voice = "voice/DAR05A_DAR0121.ogg"
    "至" "「啊，是这样的啊。时机真差啊。牧濑氏，你知道她的电话号码吗？」"
    "牧濑氏摇了摇头。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0122"
    $ current_voice = "voice/DAR05A_DAR0122.ogg"
    "至" "「我也不知道……」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0092"
    $ current_voice = "voice/DAR05A_CRS0092.ogg"
    "红莉栖" "「冈部的话可能知道」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0123"
    $ current_voice = "voice/DAR05A_DAR0123.ogg"
    "至" "「那么，就麻烦你再跟冈部打个电话吧」"
    window hide


    $ loadBG(2,"IBG033A")



    hide screen phonebtn
    "那边的话就拜托牧濑氏吧，我这边继续看关于阿万音由季的情报。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0124"
    $ current_voice = "voice/DAR05A_DAR0124.ogg"
    "至" "「哦哦，女子大学生……还是大四的。姐姐类型的角色啊，真是受不了了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0093"
    $ current_voice = "voice/DAR05A_CRS0093.ogg"
    "红莉栖" "「我还以为你是萝莉控呢」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0125"
    $ current_voice = "voice/DAR05A_DAR0125.ogg"
    "至" "「不管是萝莉系还是姐系都ＯＫ哦」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0094"
    $ current_voice = "voice/DAR05A_CRS0094.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0126"
    $ current_voice = "voice/DAR05A_DAR0126.ogg"
    "至" "「好的，电话号码也完美到手。这样目的就达成了」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0095"
    $ current_voice = "voice/DAR05A_CRS0095.ogg"
    "红莉栖" "「不行，冈部没有接电话」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0127"
    $ current_voice = "voice/DAR05A_DAR0127.ogg"
    "至" "「切，冈伦真是废物」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0096"
    $ current_voice = "voice/DAR05A_CRS0096.ogg"
    "红莉栖" "「那个，连手机号都搞到了，你打算怎么办？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0128"
    $ current_voice = "voice/DAR05A_DAR0128.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0129"
    $ current_voice = "voice/DAR05A_DAR0129.ogg"
    "至" "「打下试试吧」"
    window hide


    $ loadBG(2,"IBG034A")



    hide screen phonebtn
    "在＠ｃｈ的筷女氏——由季碳是在这写了最后的留言，已经有２４小时之久。"
    "如果真的卷入了什么不得了的事情的话，就没有时间可以浪费了。"
    "就算是我多虑了也好。不如说是期待着是我多虑了。"
    window hide


    $ loadBG(2,"BG02A2")




    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)




    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0130"
    $ current_voice = "voice/DAR05A_DAR0130.ogg"
    "至" "「…………」"
    "电话的铃声非常清晰。"
    "没法切断电源了。"
    "但是，也不能很自然地通话"
    "如果接通了的话该怎么说好呢？"
    "例如“您好，我是昨天您见到的那位胖子”啥的？"
    "“通过情报搜索知道了您的电话号码”啥的？"
    "谁说的出来啊！"
    window hide
    stop bgm 


    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0131"
    $ current_voice = "voice/DAR05A_DAR0131.ogg"
    "至" "「……！」"
    "接通了……！"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0132"
    $ current_voice = "voice/DAR05A_DAR0132.ogg"
    "至" "「………………」"
    "无言。"
    "对面什么话都没有说。"
    "但是确定是有人在听。"
    "为什么什么话都不说？"
    "难道电话对面的人不是由季碳吗？"
    "对面的人肯定是想通过声音来判断大致的样子。"
    "那个，那个。"
    "糟了，脑子里面一片空白。"
    "可能真的不说一句话就挂掉了。"
    "什么……说些什么！？"
    "就在这时"

    $ stopvoc("X06")
    play voc "DAR05A_X060001"
    $ current_voice = "voice/DAR05A_X060001.ogg"
    "由季？" "「唔…………」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0133"
    $ current_voice = "voice/DAR05A_DAR0133.ogg"
    "至" "「…………！」"
    "刚刚是女孩子的声音！"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0134"
    $ current_voice = "voice/DAR05A_DAR0134.ogg"
    "至" "「那，那个啊，现在，能不能告诉我你穿着什么颜色的胖次！？」"
    "……啊啊啊，真是失败啊，我到底是在说什么啊。想知道的只不过是发生了什么事而已"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0135"
    $ current_voice = "voice/DAR05A_DAR0135.ogg"
    "至" "「你啊，是不是写了点关于炸弹什么的东西！？　我想你是不是卷入了什么麻烦之中，就稍微用了些秘技得到了你的电话号码！」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0136"
    $ current_voice = "voice/DAR05A_DAR0136.ogg"
    "至" "「为什么我能做到这样的事情呢，因为我是深网里面有名的黑客──」"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0137"
    $ current_voice = "voice/DAR05A_DAR0137.ogg"
    "至" "「啊，挂掉了……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB03"),"True","lh/CRS_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0097"
    $ current_voice = "voice/DAR05A_CRS0097.ogg"
    "红莉栖" "「这是当然的了！」"
    play bgm "FD2BGM05"
    "牧濑氏怒发冲冠。"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0098"
    $ current_voice = "voice/DAR05A_CRS0098.ogg"
    "红莉栖" "「你是傻子吗！？　可以去死吗！？　如果说出了这样的话，即使是本人也好不是本人也好都会挂掉的了！」"
    window hide
    call hide_phone

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0138"
    $ current_voice = "voice/DAR05A_DAR0138.ogg"
    "至" "「……这，这样还不是因为，一时间我也没有想到说什么好」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0099"
    $ current_voice = "voice/DAR05A_CRS0099.ogg"
    "红莉栖" "「真是拿你没办法。这下真是束手无策了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0100"
    $ current_voice = "voice/DAR05A_CRS0100.ogg"
    "红莉栖" "「只说变态般的发言我还是把你当爷们的，结果还自称超级黑客，真是让人恶心。这和冈部有什么区别。」"
    "和冈伦不一样的是我可是认真的。"
    "但是，确实真是毫无办法。因为太过于紧张所以一直处于胡言乱语的状态，对面肯定什么也没听懂。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0139"
    $ current_voice = "voice/DAR05A_DAR0139.ogg"
    "至" "「事已至此只好破罐子破摔了。再打过去试试吧」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)




    "那么就再试一次吧。"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0101"
    $ current_voice = "voice/DAR05A_CRS0101.ogg"
    "红莉栖" "「这已经没法打了吧」"



    $ stopvoc("X05")
    play voc "DAR05A_X050001"
    $ current_voice = "voice/DAR05A_X050001.ogg"
    "手机语音" "「您所拨打的电话，因在无信号区域或电源不足暂时无法接通」"


    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0140"
    $ current_voice = "voice/DAR05A_DAR0140.ogg"
    "至" "「ｏｆｆ……，连电池都卸了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0102"
    $ current_voice = "voice/DAR05A_CRS0102.ogg"
    "红莉栖" "「因为有个变态的男子打这种工口电话过来，肯定会这样做咯」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0141"
    $ current_voice = "voice/DAR05A_DAR0141.ogg"
    "至" "「即使这样还是要继续下去……！」"
    "确实从听到的声音来看里面确实给人一种痛苦的感觉。"
    call hide_phone

    stop bgm 
    hide screen phoneSD1
    window hide

    hide screen phonemenu
    $ loadBG(0,"IBG034A")









    hide screen phonebtn
    show screen phoneSD1
    "一直向切断了电源的手机的由季那打电话，经过了３０～４０分左右。"
    window hide
    $ loadBG(0,"BG02A2")

    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)






    show screen phoneSD1



    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0142"
    $ current_voice = "voice/DAR05A_DAR0142.ogg"
    "至" "「打通了……！」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0103"
    $ current_voice = "voice/DAR05A_CRS0103.ogg"
    "红莉栖" "「她把电池重新装上了吗？」"
    window hide


    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0143"
    $ current_voice = "voice/DAR05A_DAR0143.ogg"
    "至" "「喂，喂喂！」"
    "电话的另一头能够感觉到有人在听。"
    "并且能够听见一些车子的杂音。"
    "到底是哪里呢？"
    "难道在秋叶原车站前？"
    "中央大街？"

    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0144"
    $ current_voice = "voice/DAR05A_DAR0144.ogg"
    "至" "「挂掉了……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0104"
    $ current_voice = "voice/DAR05A_CRS0104.ogg"
    "红莉栖" "「说了些什么呢？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0145"
    $ current_voice = "voice/DAR05A_DAR0145.ogg"
    "至" "「又是一句话没有说」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0105"
    $ current_voice = "voice/DAR05A_CRS0105.ogg"
    "红莉栖" "「果然被警戒着吗？　所以刚刚，你要是没说那种话的话──」"
    window hide
    call hide_phone
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0146"
    $ current_voice = "voice/DAR05A_DAR0146.ogg"
    "至" "「嘛，但是仅仅只开了一下机，我也达到目的了」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0106"
    $ current_voice = "voice/DAR05A_CRS0106.ogg"
    "红莉栖" "「目的？」"
    window hide


    $ loadBG(2,"IBG035A")



    hide screen phonebtn
    play bgm "FD2BGM07"
    "从电脑的地图上面显示是在秋叶原附近。"
    "但是这不仅仅是地图而已。"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0107"
    $ current_voice = "voice/DAR05A_CRS0107.ogg"
    "红莉栖" "「那是？」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0147"
    $ current_voice = "voice/DAR05A_DAR0147.ogg"
    "至" "「她的手机位置情报」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0148"
    $ current_voice = "voice/DAR05A_DAR0148.ogg"
    "至" "「手机呢，只要接通电源的话就有可能知道位置。只不过一般不会公开这事」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0108"
    $ current_voice = "voice/DAR05A_CRS0108.ogg"
    "红莉栖" "「……还真是考虑周全啊，你这位超级嗨客」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0149"
    $ current_voice = "voice/DAR05A_DAR0149.ogg"
    "至" "「不是嗨客是黑客」"
    "利用等待电话接通的时间，做了下准备，果然是正确的啊。哥真是犀利。"
    "从地图上来看，显示的位置就是秋叶原车站附近。"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0150"
    $ current_voice = "voice/DAR05A_DAR0150.ogg"
    "至" "「车站附近……难道是要坐电车？」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0109"
    $ current_voice = "voice/DAR05A_CRS0109.ogg"
    "红莉栖" "「直到刚刚电源一直都是关闭的，害怕桥田的变态电话骚扰可能是一个原因」"
    $ stopvoc("CRS")
    play CRS "DAR05A_CRS0110"
    $ current_voice = "voice/DAR05A_CRS0110.ogg"
    "红莉栖" "「或是说，从一台车，换乘到另一台车，所以才关掉电话」"
    $ stopvoc("DAR")
    play DAR "DAR05A_DAR0151"
    $ current_voice = "voice/DAR05A_DAR0151.ogg"
    "至" "「总之，去车站附近找找看吧。虽然可能无功而返」 "
    window hide


    $ loadBG(2,"BG01A")



    show screen phonebtn
    "之后，拜托牧濑氏守下家，我立马就从Ｌａｂ出发了。"


    stop bgm 
    hide screen phoneSD1
    window hide






    return
