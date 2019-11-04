label SGFD2_TEN06A:
    window hide



    $ loadBG(0,"BG05N1")


    $ date="8/18"
    hide screen phonebtn
    show screen phoneSD1






    $ stopvoc("MIX")
    play voc "TEN06A_MIX0000"
    $ current_voice = "voice/TEN06A_MIX0000.ogg"
    "Ｌａｂｍｅｍ们" "「「「「「「诶！？　那算，什么啊ー？」」」」」」"


    window hide


    $ loadBG(0,"BG02N2")

    play bgm "BGM06"
    show screen phonebtn
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0000"
    $ current_voice = "voice/TEN06A_TEN0000.ogg"
    "天王寺" "「诶呀，要是给你们看资金有多紧张你们就不会有意见了吧？」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0001"
    $ current_voice = "voice/TEN06A_TEN0001.ogg"
    "天王寺" "「说实话３亿感觉还有些不够，所以那家伙简直是雪中送炭啊」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC04"),"True","lh/FEI_DSC04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN06A_RUK0001"
    $ current_voice = "voice/TEN06A_RUK0001.ogg"
    "琉华" "「这样啊。听到一半还以为肯定是拒绝了呢……明明我还一直想成为天王寺先生那样能做出帅气的决定的男人呢……」"
    $ stopvoc("FEI")
    play FEI "TEN06A_FEI0001"
    $ current_voice = "voice/TEN06A_FEI0001.ogg"
    "菲利斯" "「财迷心窍了喵？」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0002"
    $ current_voice = "voice/TEN06A_TEN0002.ogg"
    "天王寺" "「不是那样的。后来仔细谈了一下发现是我的结论下得太早了哦」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0003"
    $ current_voice = "voice/TEN06A_TEN0003.ogg"
    "天王寺" "「其实以前他也是古董ＰＣ的狂热者，所以也明白我的心情。并不是想要否定旧东西的意思」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC03"),"True","lh/FEI_DSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN06A_FEI0002"
    $ current_voice = "voice/TEN06A_FEI0002.ogg"
    "菲利斯" "「古董ＰＣ狂热者？　难道说……」"
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN06A_DAR0001"
    $ current_voice = "voice/TEN06A_DAR0001.ogg"
    "至" "「菲利斯炭，想到什么了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN06A_FEI0003"
    $ current_voice = "voice/TEN06A_FEI0003.ogg"
    "菲利斯" "「没有，什么也没有哦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN06A_OKA0001"
    $ current_voice = "voice/TEN06A_OKA0001.ogg"
    "伦太郎" "「嘛，这也不错嘛。虽然中间有些波折，最后还是和原来一样啊」"
    $ stopvoc("MAY")
    play MAY "TEN06A_MAY0001"
    $ current_voice = "voice/TEN06A_MAY0001.ogg"
    "真由理" "「嗯，绹酱也同意那样了吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN06A_FEI0004"
    $ current_voice = "voice/TEN06A_FEI0004.ogg"
    "菲利斯" "「啊，是喵！最开始就说是为了绹喵才要重建的，要是不听听她的意见就很奇怪了喵」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0004"
    $ current_voice = "voice/TEN06A_TEN0004.ogg"
    "天王寺" "「我觉得不问也没有问题啦。绹，你怎么想的？现在的古董大楼和新大楼，哪个更好？」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0005"
    $ current_voice = "voice/TEN06A_TEN0005.ogg"
    "天王寺" "「如果你说现在的更好的话我就要重新考虑了呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN06A_NAE0000"
    $ current_voice = "voice/TEN06A_NAE0000.ogg"
    "绹" "「唔。哪个更好呢。唔，唔……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN06A_NAE0001"
    $ current_voice = "voice/TEN06A_NAE0001.ogg"
    "绹" "「呐，爸爸，虽然是最近才这么想的，但这栋大楼……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN06A_NAE0002"
    $ current_voice = "voice/TEN06A_NAE0002.ogg"
    "绹" "「总感觉有什么让人不满足的地方。呆在这里，该说是感觉有些无聊吗」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN06A_CRS0001"
    $ current_voice = "voice/TEN06A_CRS0001.ogg"
    "红莉栖" "「无聊，吗。如果是这样的负面印象的话，看起来已经决定了呢」"
    $ stopvoc("DAR")
    play DAR "TEN06A_DAR0002"
    $ current_voice = "voice/TEN06A_DAR0002.ogg"
    "至" "「小绹既然如此说来，那就只能重建了。卡哇伊的幼女就是正义！」"
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN06A_MOE0000"
    $ current_voice = "voice/TEN06A_MOE0000.ogg"
    "萌郁" "「新大楼……乐趣」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0006"
    $ current_voice = "voice/TEN06A_TEN0006.ogg"
    "天王寺" "「好了，那就这样定了。重建咯。虽然已经说了这么多了，但最后问一遍，没有意见了？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN06A_MAY0002"
    $ current_voice = "voice/TEN06A_MAY0002.ogg"
    "真由理" "「嗯。冈伦，真由喜也觉得就让自己接受这个事实吧。新的Ｌａｂ建好了以后，也来创造很多回忆吧」"
    $ stopvoc("OKA")
    play OKA "TEN06A_OKA0002"
    $ current_voice = "voice/TEN06A_OKA0002.ogg"
    "伦太郎" "「正是如此，真由理。没有什么好悲伤的」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "终于把话说完了。"
    "虽然花了挺长的时间，但终于得出了全员都能够接受的结论。"
    "让大桧山重生。"
    "作为绹理想的家(Ｈｏｍｅ)"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0007"
    $ current_voice = "voice/TEN06A_TEN0007.ogg"
    "天王寺" "「好嘞绹，现在起就要让你们享受新大楼的快乐咯」"
    $ stopvoc("TEN")
    play TEN "TEN06A_TEN0008"
    $ current_voice = "voice/TEN06A_TEN0008.ogg"
    "天王寺" "「要建一座让你心情最棒的大楼给你！新大桧山大楼计划，始动！」"

    hide screen phoneSD1
    window hide

    stop bgm
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade






    return













    return
