label SGFD2_TEN04A:
    window hide



    $ loadBG(0,"BG02A2")
    play bgm "BGM05"


    $ date="8/18"
    $ day="WED"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0000"
    $ current_voice = "voice/TEN04A_TEN0000.ogg"
    "天王寺" "「所以就是这么回事，怎么样，这个故事挺感人的吧！我已经决定了。重建吧！」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN04A_RUK0000"
    $ current_voice = "voice/TEN04A_RUK0000.ogg"
    "琉华" "「诶，结果还是要重建吗？还以为只是一个听起来很棒的故事呢……」"
    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0000"
    $ current_voice = "voice/TEN04A_MAY0000.ogg"
    "真由理" "「真由喜也感觉有些遗憾呢」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0000"
    $ current_voice = "voice/TEN04A_OKA0000.ogg"
    "伦太郎" "「诶呀，就不要再抵抗了嘛。一直这么说的话，Ｍｒ．布朗不就一直都下不了决定了吗」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN04A_DAR0000"
    $ current_voice = "voice/TEN04A_DAR0000.ogg"
    "至" "「是啊是啊。店长的心，就只会一直在青梅竹马和有钱的大小姐之间摇摆不定了嘛」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0000"
    $ current_voice = "voice/TEN04A_CRS0000.ogg"
    "红莉栖" "「这个比喻完全无法理解呢」"
    window hide
    hide lh7 

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSB01"),"True","lh/FEI_DSB01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AFFINITY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AFFINITY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_AFFINITY"])
    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0000"
    $ current_voice = "voice/TEN04A_FEI0000.ogg"
    "菲利斯" "「那个喵，肯定是{color=#f00}某ＲＰＧ的选新娘事件{/color}喵」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0001"
    $ current_voice = "voice/TEN04A_TEN0001.ogg"
    "天王寺" "「你们这些人，从刚才开始就有些太随意了啊，真是的」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN04A_MOE0000"
    $ current_voice = "voice/TEN04A_MOE0000.ogg"
    "萌郁" "「…………」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0002"
    $ current_voice = "voice/TEN04A_TEN0002.ogg"
    "天王寺" "「萌郁、你也再说几句啊。保持一下两边意见的平衡」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0001"
    $ current_voice = "voice/TEN04A_OKA0001.ogg"
    "伦太郎" "「好啊，Ｍｒ．布朗。那样的话我们就少数服从多数。用投票来决定吧？」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0003"
    $ current_voice = "voice/TEN04A_TEN0003.ogg"
    "天王寺" "「投票？那样能够立刻得出结论的话倒是没关系」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0002"
    $ current_voice = "voice/TEN04A_OKA0002.ogg"
    "伦太郎" "「显像管小姐也觉得没问题吧？」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at left_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN04A_NAE0000"
    $ current_voice = "voice/TEN04A_NAE0000.ogg"
    "绹" "「嗯……虽，虽然不太明白是怎么回事」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0004"
    $ current_voice = "voice/TEN04A_TEN0004.ogg"
    "天王寺" "「喂，冈部。虽然平时已经一直在和你说了，但你不准用奇怪的名字来叫我女儿！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0003"
    $ current_voice = "voice/TEN04A_OKA0003.ogg"
    "伦太郎" "「明白了。那么，绹！」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0005"
    $ current_voice = "voice/TEN04A_TEN0005.ogg"
    "天王寺" "「想吃拳头吗！姓也不能少啊。……明白了，明白了，那什么小姐的就行了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0004"
    $ current_voice = "voice/TEN04A_OKA0004.ogg"
    "伦太郎" "「明明开始就接受不就好了」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0006"
    $ current_voice = "voice/TEN04A_TEN0006.ogg"
    "天王寺" "「切，你这家伙老是来触碰我的底线啊」"
    hide lh7 

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0005"
    $ current_voice = "voice/TEN04A_OKA0005.ogg"
    "伦太郎" "「那么现在，我们就通过投票的方式来决定Ｌａｂ的意见。首先是同意新建大楼的人请举手」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0006"
    $ current_voice = "voice/TEN04A_OKA0006.ogg"
    "伦太郎" "「是，是是！我觉得新大楼比较好」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0001"
    $ current_voice = "voice/TEN04A_CRS0001.ogg"
    "红莉栖" "「……你到底是什么角色哦，冈部」"
    hide lh6  with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN04A_DAR0001"
    $ current_voice = "voice/TEN04A_DAR0001.ogg"
    "至" "「我也赞成啊。基建什么的果然还是新的比较舒服呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0007"
    $ current_voice = "voice/TEN04A_OKA0007.ogg"
    "伦太郎" "「２人了啊。还有吗？」"
    window hide
    play se "SGSE801"


    play se "SGSE158"

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0008"
    $ current_voice = "voice/TEN04A_OKA0008.ogg"
    "伦太郎" "「什么什么。『好的，赞成。我也比较喜欢新大楼。』」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN04A_MOE0001"
    $ current_voice = "voice/TEN04A_MOE0001.ogg"
    "萌郁" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0009"
    $ current_voice = "voice/TEN04A_OKA0009.ogg"
    "伦太郎" "「喂，指压师，用嘴巴说出来啊，用嘴巴！至少举个手也行啊」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0007"
    $ current_voice = "voice/TEN04A_TEN0007.ogg"
    "天王寺" "「诶呀诶呀」"
    "看来萌郁的无口并不是针对我的。"
    "冈部那家伙看起来也拿她没辙。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0010"
    $ current_voice = "voice/TEN04A_OKA0010.ogg"
    "伦太郎" "「好的，赞成者有三名。接下来是反对者」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0001"
    $ current_voice = "voice/TEN04A_MAY0001.ogg"
    "真由理" "「我。真由喜觉得现在的比较好呢」"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") at right_t as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN04A_RUK0001"
    $ current_voice = "voice/TEN04A_RUK0001.ogg"
    "琉华" "「那个……不好意思，我也反对。总觉得这里是个充满回忆的场所呢」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0011"
    $ current_voice = "voice/TEN04A_OKA0011.ogg"
    "伦太郎" "「什么？你要背叛我吗，琉华子」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA03"),"True","lh/RUK_CSA03a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB04"),"True","lh/MAY_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0002"
    $ current_voice = "voice/TEN04A_MAY0002.ogg"
    "真由理" "「不行哦冈伦。这么欺负琉华君的话，就不是投票了呢」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0012"
    $ current_voice = "voice/TEN04A_OKA0012.ogg"
    "伦太郎" "「唔，说的也是」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") at left_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0001"
    $ current_voice = "voice/TEN04A_FEI0001.ogg"
    "菲利斯" "「菲利斯也是投反对票喵」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0013"
    $ current_voice = "voice/TEN04A_OKA0013.ogg"
    "伦太郎" "「喂，菲利斯，难道放弃２号店的野望了吗？」"
    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0002"
    $ current_voice = "voice/TEN04A_FEI0002.ogg"
    "菲利斯" "「嗯，仔细想了很多，果然在楼上是店的话就没法悠闲地在这里玩耍了喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA02"),"True","lh/FEI_DSA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0003"
    $ current_voice = "voice/TEN04A_FEI0003.ogg"
    "菲利斯" "「肯定会很在意，一直想去看一眼什么的。所以这里还是和真由喜统一战线了喵♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0003"
    $ current_voice = "voice/TEN04A_MAY0003.ogg"
    "真由理" "「谢谢——。菲利斯也是属于对工作很热心的那种人，所以肯定放不下心来吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN04A_RUK0002"
    $ current_voice = "voice/TEN04A_RUK0002.ogg"
    "琉华" "「冈部师傅，这样的话变成三比三了」"
    window hide

    stop bgm 



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0014"
    $ current_voice = "voice/TEN04A_OKA0014.ogg"
    "伦太郎" "「看起来好像还有一个人没有表态呢，Ｃｈｒｉｓｔｉｎａ」"
    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0002"
    $ current_voice = "voice/TEN04A_CRS0002.ogg"
    "红莉栖" "「我保持中立呢。虽然觉得干净的Ｌａｂ挺好的，但是要是变成美国的研究室那样的话就太无聊了」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0015"
    $ current_voice = "voice/TEN04A_OKA0015.ogg"
    "伦太郎" "「如果你那么说的话，就确定不下来了。不接受中立」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0016"
    $ current_voice = "voice/TEN04A_OKA0016.ogg"
    "伦太郎" "「那么就告诉我你的想法吧，吾之助手哦。你到底是投赞成票呢还是反对票呢？」"
    $ stopvoc("DAR")
    play DAR "TEN04A_DAR0002"
    $ current_voice = "voice/TEN04A_DAR0002.ogg"
    "至" "「咳咳」"
    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0004"
    $ current_voice = "voice/TEN04A_MAY0004.ogg"
    "真由理" "「红莉栖酱……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA02"),"True","lh/CRS_ASA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0003"
    $ current_voice = "voice/TEN04A_CRS0003.ogg"
    "红莉栖" "「是呢。要说是哪一边的话……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0004"
    $ current_voice = "voice/TEN04A_CRS0004.ogg"
    "红莉栖" "「我——赞成新大楼哦」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC02"),"True","lh/FEI_DSC02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("RUK")
    play RUK "TEN04A_RUK0003"
    $ current_voice = "voice/TEN04A_RUK0003.ogg"
    "琉华" "「诶诶，结果是这样啊……」"
    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0004"
    $ current_voice = "voice/TEN04A_FEI0004.ogg"
    "菲利斯" "「这难道就是最终投票(Ｆｉｎａｌ　Ｊｕｄｇｅｍｅｎｔ)了喵」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    play bgm "BGM05"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0017"
    $ current_voice = "voice/TEN04A_OKA0017.ogg"
    "伦太郎" "「哇哈哈哈，看吧！刚刚还是摆着架子的Ｈｅｌｐｅｒ也转投到我方门下了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0005"
    $ current_voice = "voice/TEN04A_CRS0005.ogg"
    "红莉栖" "「才没有什么投到你方门下呢！谁是什么摆着架子的Ｈｅｌｐｅｒ啦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0006"
    $ current_voice = "voice/TEN04A_CRS0006.ogg"
    "红莉栖" "「这是我遵从自己的意志做出的选择。那个……新大楼听起来很方便」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0018"
    $ current_voice = "voice/TEN04A_OKA0018.ogg"
    "伦太郎" "「看到了吗Ｍｒ．布朗。这就是我们Ｌａｂｍｅｍ的意见呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0019"
    $ current_voice = "voice/TEN04A_OKA0019.ogg"
    "伦太郎" "「果然没有违逆作为绝对君主凤凰院凶真的意向呢。唔哈哈哈哈！」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0008"
    $ current_voice = "voice/TEN04A_TEN0008.ogg"
    "天王寺" "「诶呀诶呀。冈部，不管怎么说，你有点太吵了哦？」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0009"
    $ current_voice = "voice/TEN04A_TEN0009.ogg"
    "天王寺" "「果然，不应该把２楼租给这家伙。如果那时候把二楼租给另外的人的话，现在就该很安静了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC01"),"True","lh/CRS_ASC01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0007"
    $ current_voice = "voice/TEN04A_CRS0007.ogg"
    "红莉栖" "「诶？有要租这里的其他人吗？」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0010"
    $ current_voice = "voice/TEN04A_TEN0010.ogg"
    "天王寺" "「啊啊，半年前都快要谈成了呢。但是……」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG04A2")

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    play bgm "BGM13"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0011"
    $ current_voice = "voice/TEN04A_TEN0011.ogg"
    "天王寺" "「所以说，已经没事了。他是个有教养的人呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0020"
    $ current_voice = "voice/TEN04A_OKA0020.ogg"
    "伦太郎" "「不，给我等等。这边还没完啊！」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0012"
    $ current_voice = "voice/TEN04A_TEN0012.ogg"
    "天王寺" "「就差合同没签了呢。和你不一样，他的身份和对于这层楼的用途都很明确」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0013"
    $ current_voice = "voice/TEN04A_TEN0013.ogg"
    "天王寺" "「说实话你完全比不过他呢。借给你这样的无业青年的可能性大概连１％都没有」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0021"
    $ current_voice = "voice/TEN04A_OKA0021.ogg"
    "伦太郎" "「不，不是那样的！！归处……对，这地方对于我来说是必要的归处」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0014"
    $ current_voice = "voice/TEN04A_TEN0014.ogg"
    "天王寺" "「归处？你有这么和我说过吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0022"
    $ current_voice = "voice/TEN04A_OKA0022.ogg"
    "伦太郎" "「我不论如何……都要创建这个Ｌａｂ！」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0015"
    $ current_voice = "voice/TEN04A_TEN0015.ogg"
    "天王寺" "「喂喂，为什么我一定要迎合你的想法啊。给我搞搞清楚。」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0016"
    $ current_voice = "voice/TEN04A_TEN0016.ogg"
    "天王寺" "「通常来说，没钱的话去租些便宜的郊区房子不就行了。不是这里也没有关系吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0023"
    $ current_voice = "voice/TEN04A_OKA0023.ogg"
    "伦太郎" "「但是！！」"
    window hide

    stop bgm 


    $ loadBG(0,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM22"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PIYORI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PIYORI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PIYORI"])
    $ stopvoc("DAR")
    play DAR "TEN04A_DAR0003"
    $ current_voice = "voice/TEN04A_DAR0003.ogg"
    "至" "「唔哇，不管怎么想都是{color=#f00}Ｂｉｕ的一下就输了{/color}这种固定展开呢」"
    $ stopvoc("CRS")
    play CRS "TEN04A_CRS0008"
    $ current_voice = "voice/TEN04A_CRS0008.ogg"
    "红莉栖" "「……开始觉得Ｌａｂ能在这里真是个奇迹呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC02"),"True","lh/FEI_DSC02a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN04A_FEI0005"
    $ current_voice = "voice/TEN04A_FEI0005.ogg"
    "菲利斯" "「明明对于凶真这么不利，为什么最后还是租给他了喵？」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0017"
    $ current_voice = "voice/TEN04A_TEN0017.ogg"
    "天王寺" "「那是因为呢……嗯？」"

    stop bgm 
    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0005"
    $ current_voice = "voice/TEN04A_MAY0005.ogg"
    "真由理" "「…………」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0018"
    $ current_voice = "voice/TEN04A_TEN0018.ogg"
    "天王寺" "「怎么了小姑娘？一直盯着墙壁看。在回想以前的事吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FDBGM03"
    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0006"
    $ current_voice = "voice/TEN04A_MAY0006.ogg"
    "真由理" "「不是哦。就要告别了呢，在这么想」"
    $ stopvoc("RUK")
    play RUK "TEN04A_RUK0004"
    $ current_voice = "voice/TEN04A_RUK0004.ogg"
    "琉华" "「真由理酱……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0007"
    $ current_voice = "voice/TEN04A_MAY0007.ogg"
    "真由理" "「虽然确实和大家说的一样有点脏，但真由喜还是喜欢这个地方哦……」"
    $ stopvoc("OKA")
    play OKA "TEN04A_OKA0024"
    $ current_voice = "voice/TEN04A_OKA0024.ogg"
    "伦太郎" "「真由理……」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0019"
    $ current_voice = "voice/TEN04A_TEN0019.ogg"
    "天王寺" "「啊，先说清楚了，我可不是对这里没什么感情」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0020"
    $ current_voice = "voice/TEN04A_TEN0020.ogg"
    "天王寺" "「我对于这幢大楼有着深刻的回忆。在绹出生之前更久呢」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0021"
    $ current_voice = "voice/TEN04A_TEN0021.ogg"
    "天王寺" "「但是，那样不是挺好的吗。在新大楼也能留下回忆啊。重建又不会使旧的回忆消失」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0022"
    $ current_voice = "voice/TEN04A_TEN0022.ogg"
    "天王寺" "「我要为了你们还有绹着想的话，总得要建一幢新大楼的啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN04A_MAY0008"
    $ current_voice = "voice/TEN04A_MAY0008.ogg"
    "真由理" "「店长……我很抱歉」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0023"
    $ current_voice = "voice/TEN04A_TEN0023.ogg"
    "天王寺" "「没什么需要道歉的哦。我也明白你的心情所以不如说我要向你道歉呢」"
    $ stopvoc("TEN")
    play TEN "TEN04A_TEN0024"
    $ current_voice = "voice/TEN04A_TEN0024.ogg"
    "天王寺" "「嘛，就是这么回事，所以请接受吧。那我去把这个最终决定告诉那个人了。」"

    hide screen phoneSD1
    window hide

    stop bgm
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade





    return
