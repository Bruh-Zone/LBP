label SGFD2_TEN03A:
    window hide



    $ loadBG(0,"BG23A")


    $ date="8/17"
    $ day="TUE"
    show screen phonebtn
    show screen phoneSD1

    "虽然一直在考虑到底要不要重建大楼……"
    "想了几天也没得出结论。"
    "虽然为了绹想建新的大楼，但对于现在的这栋也有些不舍。"
    "住在２楼的那些人中看起来也是反对者居多。"
    "但是冈部是例外呢。"
    "再加上……"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0000"
    $ current_voice = "voice/TEN03A_TEN0000.ogg"
    "天王寺" "「如果要重建的话，店的经营也必须考虑进去啊」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PROPERTY_TAX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PROPERTY_TAX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PROPERTY_TAX"])
    "{color=#f00}固定资产税{/color}会上涨，用三亿元翻新后肯定没那么简单就结束了。"
    "我真的能好好经营这栋大楼吗？"
    "虽然打算要去和企业家咨询一下……"
    window hide
    show expression "bg/BG27A~ipad.jpg" as background :
        yalign 1.0
        linear 1.0yalign 0.0




















    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0001"
    $ current_voice = "voice/TEN03A_TEN0001.ogg"
    "天王寺" "「喂，这什么啊」"
    "这大得不像话的大楼。"
    "所以所谓的企业家就是住在这种地方的么。"
    "总感觉和我不是一个等级的。"
    window hide
    play se "SGSE094"



    $ loadBG(0,"BG_BLACK")

    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0002"
    $ current_voice = "voice/TEN03A_TEN0002.ogg"
    "天王寺" "「那个，我是之前预约过的天王寺」"
    $ stopvoc("Y11")
    play voc "TEN03A_Y110000"
    $ current_voice = "voice/TEN03A_Y110000.ogg"
    "管家" "「了解了。请进。」"
    window hide


    $ loadBG(0,"BG26A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM26"

    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0003"
    $ current_voice = "voice/TEN03A_TEN0003.ogg"
    "天王寺" "「打扰了」"
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0000"
    $ current_voice = "voice/TEN03A_FPP0000.ogg"
    "秋叶" "「天王寺裕吾先生呢。欢迎。鄙人名为秋叶幸高。」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0004"
    $ current_voice = "voice/TEN03A_TEN0004.ogg"
    "天王寺" "「多谢。想借这次和您交流的机会谈谈……」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0005"
    $ current_voice = "voice/TEN03A_TEN0005.ogg"
    "天王寺" "「半导体商店的婆婆说“我认识个不错的人哦”，就过来拜访了。没想到是您这样的名士啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0001"
    $ current_voice = "voice/TEN03A_FPP0001.ogg"
    "秋叶" "「哈哈哈，名士什么的真是过奖了。只是和你一样做生意的商人罢了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0002"
    $ current_voice = "voice/TEN03A_FPP0002.ogg"
    "秋叶" "「那，要谈的事是什么？」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0006"
    $ current_voice = "voice/TEN03A_TEN0006.ogg"
    "天王寺" "「好。实际上是为了女儿想重建大楼，但不知道到底该怎么办」"
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0003"
    $ current_voice = "voice/TEN03A_FPP0003.ogg"
    "秋叶" "「为了女儿……哈，挺像的呢」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0007"
    $ current_voice = "voice/TEN03A_TEN0007.ogg"
    "天王寺" "「诶？是在说什么？」"
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0004"
    $ current_voice = "voice/TEN03A_FPP0004.ogg"
    "秋叶" "「其实呢我也有个女儿哦。虽然平时工作很忙，不太抽得出时间去陪她，但是也是一直想着她的事情的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0005"
    $ current_voice = "voice/TEN03A_FPP0005.ogg"
    "秋叶" "「可怜天下父母心呢。请务必告诉我能帮上忙的地方。」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0008"
    $ current_voice = "voice/TEN03A_TEN0008.ogg"
    "天王寺" "「不胜感激。那就尽快来谈谈大楼的运营方面……」"
    window hide
    with Fade(1,1,1)



    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA02"),"True","lh/FPP_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ targetmailid = gc["ScriptMacros"]["RM_TEN_RECV_FEI01_01"]

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0006"
    $ current_voice = "voice/TEN03A_FPP0006.ogg"
    "秋叶" "「那，基本上来说就是这样。大体掌握了吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0009"
    $ current_voice = "voice/TEN03A_TEN0009.ogg"
    "天王寺" "「唔，原来如此。大概都了解了。」"
    call CHECK_RM_RECEIVE
    "果然大楼的运营，认真做和随便做做果然不是差的一点两点。"
    call CHECK_RM_RECEIVE
    "但，听了这位先生的一席介绍之后，心中已经有了大概的方向。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0007"
    $ current_voice = "voice/TEN03A_FPP0007.ogg"
    "秋叶" "「那，得出结论了吗。到底要不要重建」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0010"
    $ current_voice = "voice/TEN03A_TEN0010.ogg"
    "天王寺" "「托您的福虽然已经有眉目了……但还没能下定把大楼完全拆掉的决心」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0008"
    $ current_voice = "voice/TEN03A_FPP0008.ogg"
    "秋叶" "「原来如此。天王寺先生，现在和我出门转转吧。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0011"
    $ current_voice = "voice/TEN03A_TEN0011.ogg"
    "天王寺" "「到哪儿转转呢？」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0009"
    $ current_voice = "voice/TEN03A_FPP0009.ogg"
    "秋叶" "「请跟我来。如果要进行这样的咨询的话，有个必须要去的地方哦」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_FEI01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_FEI01_01"])

    window hide

    stop bgm 


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM14"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0012"
    $ current_voice = "voice/TEN03A_TEN0012.ogg"
    "天王寺" "「这里是……」"
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0010"
    $ current_voice = "voice/TEN03A_FPP0010.ogg"
    "秋叶" "「柳林(やなばやし)神社哦。您知道吗？」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0013"
    $ current_voice = "voice/TEN03A_TEN0013.ogg"
    "天王寺" "「诶诶，确实在节日的时候和绹来过几次」"

    $ targetmailid = cml.setdefault("RM_TEN_SEND_FEI01","")

    $ LR_RM_CHANCE=17
    call CHECK_RM_RECEIVE
    "但是一般的时候是不会来的。"
    call CHECK_RM_RECEIVE
    "因为我也不怎么信这方面嘛。"
    call CHECK_RM_RECEIVE
    "越近越不会来呢。"
    call CHECK_RM_RECEIVE
    "听说是这一区域有名的场所，这样。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0011"
    $ current_voice = "voice/TEN03A_FPP0011.ogg"
    "秋叶" "「虽然这间神社很小，但是相当古老哦。就在那里静静地见证了秋叶原的变迁，将这片土地一直守护下去」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0012"
    $ current_voice = "voice/TEN03A_FPP0012.ogg"
    "秋叶" "「每次到这儿来我都会这么想哟。“对于一条街区来说最重要的到底是什么呢”。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0014"
    $ current_voice = "voice/TEN03A_TEN0014.ogg"
    "天王寺" "「最重要的，东西吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0013"
    $ current_voice = "voice/TEN03A_FPP0013.ogg"
    "秋叶" "「诶诶，１０年之前，秋叶原是一条以电器闻名的街区。这您想必是知道的吧。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0015"
    $ current_voice = "voice/TEN03A_TEN0015.ogg"
    "天王寺" "「啊啊，我确实在这里生活了很久了呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0014"
    $ current_voice = "voice/TEN03A_FPP0014.ogg"
    "秋叶" "「如今它却已经变成这幅模样了呢。所谓的萌文化，吗。独特的流行文化在这条街里生根发芽」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0015"
    $ current_voice = "voice/TEN03A_FPP0015.ogg"
    "秋叶" "「说到底那是我的责任啊。听取了作为顾问的女儿的建议，推进了萌文化的发展」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0016"
    $ current_voice = "voice/TEN03A_TEN0016.ogg"
    "天王寺" "「哦。能提出这样的提案的女儿，还真是厉害呢。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0016"
    $ current_voice = "voice/TEN03A_FPP0016.ogg"
    "秋叶" "「确实街区看起来变化了。但是，这条街的本质也发生变化了吧」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0017"
    $ current_voice = "voice/TEN03A_TEN0017.ogg"
    "天王寺" "「本质，吗。嘛要说变化的话确实变了呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0017"
    $ current_voice = "voice/TEN03A_FPP0017.ogg"
    "秋叶" "「看看那些人们的表情吧。１０年前，这里满是追求着最新家电的人们的笑脸」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0018"
    $ current_voice = "voice/TEN03A_FPP0018.ogg"
    "秋叶" "「然后现在街上也满是笑脸。就算流行的东西或者追求的东西变化了，人们幸福的样子未曾改变。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0019"
    $ current_voice = "voice/TEN03A_FPP0019.ogg"
    "秋叶" "「我偶尔会想。对于街区来说最重要的东西并不是守护传统，而是守护人们的笑容啊。」"

    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0018"
    $ current_voice = "voice/TEN03A_TEN0018.ogg"
    "天王寺" "「笑容吗」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_FEI02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_FEI02_01"])

    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "确实我留恋着那幢大楼。"
    "但是就算重新建造，里面的人们并没有改变。"
    "绹还在那里，萌郁还在那里，２楼的那些人也是。"
    "大家还能和过去一样欢笑的话，或许那样也不错呢。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "TEN03A_FPP0020"
    $ current_voice = "voice/TEN03A_FPP0020.ogg"
    "秋叶" "「天王寺先生。我带你来这里的理由，现在明白了吗」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0019"
    $ current_voice = "voice/TEN03A_TEN0019.ogg"
    "天王寺" "「啊啊。确实和你说的一样，这条街虽然变化了，但是实际上未曾改变啊」"
    $ stopvoc("TEN")
    play TEN "TEN03A_TEN0020"
    $ current_voice = "voice/TEN03A_TEN0020.ogg"
    "天王寺" "「说不定是我把问题考虑得太复杂了。」"

    hide screen phoneSD1
    window hide

    stop bgm 
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade





    return
