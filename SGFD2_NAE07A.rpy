label SGFD2_NAE07A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")

    play bgm "FD2BGM01"

    $ date="7/13"
    $ day="FRI"
    hide screen phonebtn
    show screen phoneSD1

    "之后那天——"
    "我比平时起得更早，在去学校之前去了一趟父亲的大楼。"
    "不知道桶子叔叔还在不在那里。"
    "但是比起那个，现在我更想确认我自己的心情。"
    "那么……"
    hide screen phoneSD1
    window hide
    stop bgm 
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE003A"]]["Check"]=True


    $ loadBG(2,"EV_NAE003A")



    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0000"
    $ current_voice = "voice/NAE07A_NAE0000.ogg"
    "绹" "「…………」"
    play bgm "FD2BGM10"
    "在确认自己的心情之前，遇到了大尻。"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0000"
    $ current_voice = "voice/NAE07A_DAR0000.ogg"
    "至" "「哦，是，是谁？谁在哪里？虽然十分不好意思，但是能帮我推一下么？」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0001"
    $ current_voice = "voice/NAE07A_NAE0001.ogg"
    "绹" "「这人完了……」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0001"
    $ current_voice = "voice/NAE07A_DAR0001.ogg"
    "至" "「哦唔，原来是绹酱来了啊。我，我还以为你不会来了呢」"
    "桶子叔叔的胖胖的短腿在空中蹦跶。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0002"
    $ current_voice = "voice/NAE07A_NAE0002.ogg"
    "绹" "「……什么时候卡在那里的？」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0002"
    $ current_voice = "voice/NAE07A_DAR0002.ogg"
    "至" "「大概已经过了８个小时吧？」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0003"
    $ current_voice = "voice/NAE07A_DAR0003.ogg"
    "至" "「附近也许有那群家伙在，所以肯定不能大声呼救的吧，常考」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0004"
    $ current_voice = "voice/NAE07A_DAR0004.ogg"
    "至" "「本来想打电话给绹酱呀冈伦来着的，结果手机在裤子的口袋里。这幅样子拿不出来啊」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0003"
    $ current_voice = "voice/NAE07A_NAE0003.ogg"
    "绹" "「…………」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZENORE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZENORE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ZENORE"])
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0005"
    $ current_voice = "voice/NAE07A_DAR0005.ogg"
    "至" "「这样谁都来的话，几天之后我就变成干尸啦。想想那种惨烈的死法{color=#f00}整个我都哭了{/color}……」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0004"
    $ current_voice = "voice/NAE07A_NAE0004.ogg"
    "绹" "「……噗」"
    "我要是早上没有过来的话，会变成怎么样呢。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0005"
    $ current_voice = "voice/NAE07A_NAE0005.ogg"
    "绹" "「真没办法啊。桶子叔叔如果没有我的话，就什么也做不到了呢」"
    "为什么呢……"
    "昨天明明是那么讨厌桶子叔叔的，而且明明是那么后悔来着的。"
    "看到桶子叔叔现在的样子，那种心情就突然烟消云散了。"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0006"
    $ current_voice = "voice/NAE07A_DAR0006.ogg"
    "至" "「好了啦，赶快推我一把让我解脱吧Ｐｌｅａｓｅ……」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0007"
    $ current_voice = "voice/NAE07A_DAR0007.ogg"
    "至" "「差不多肚子这边的痛感就要忍不住了……」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0008"
    $ current_voice = "voice/NAE07A_DAR0008.ogg"
    "至" "「好想去厕所啊。虽然说绹酱如果能想看护师一样来照顾我的话这个样子也不是不能解决」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0006"
    $ current_voice = "voice/NAE07A_NAE0006.ogg"
    "绹" "「诶，那可不行……」"
    "难道说这个人根本没有考虑昨天留未穗姐姐说的那些话？"
    "说不定真的只是个变态而已，我现在开始认真地这么觉得了。"
    window hide

    stop bgm 



    $ loadBG(0,"BG04A4")

    show screen phonebtn
    show screen phoneSD1
    "救出了桶子叔叔以后，我一个人来到了１楼。"
    "坐在了爸爸经常坐的椅子上。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn

    "闭上眼睛。"
    "面对自己的内心。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0007"
    $ current_voice = "voice/NAE07A_NAE0007.ogg"
    "绹" "「…………」"
    "回想起来，直到留未穗姐姐２年前牵着我的手离开之前，我在这里度过了不知道多少个日夜。"
    "所以，当我闭上眼睛的时候，脑海里浮现出的都是那个夏天的事情。"
    "那个时候，并不觉得我会喜欢来这样又昏暗又满是灰尘的店。"
    "虽然喜欢爸爸，但是店的环境并不好，而且我也不是很喜欢显像管电视机。感觉里面会显示出什么恐怖的东西。"
    "但是，那个夏天，和平时不一样。"
    "那个夏天，那幢大楼里非常的热闹。"
    "我在这里过得很开心。"
    "于是来到这里变得理所当然。"
    window hide
    play bgm "FD2BGM09"


    $ loadBG(0,"BG05A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "NAE07A_MAY0000"
    $ current_voice = "voice/NAE07A_MAY0000.ogg"
    "真由理" "「啊，绹酱，嘟嘟噜♪」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0008"
    $ current_voice = "voice/NAE07A_NAE0008.ogg"
    "绹" "「真由理姐姐！」"
    "真由理姐姐总是悠闲地微笑着。"
    "只是看着她的脸，我就感觉幸福起来了，于是开心地抱上去，让她温柔地摸我的头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA01"),"True","lh/MAY_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "NAE07A_MAY0001"
    $ current_voice = "voice/NAE07A_MAY0001.ogg"
    "真由理" "「绹酱，这是我刚刚买的冰激凌，吃一个吗？」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0009"
    $ current_voice = "voice/NAE07A_NAE0009.ogg"
    "绹" "「哇，谢谢你」"
    "真由理姐姐总是在吃东西，也经常分给我吃。她说过她最喜欢的是炸鸡。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "NAE07A_MAY0002"
    $ current_voice = "voice/NAE07A_MAY0002.ogg"
    "真由理" "「那，再见咯♪」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0010"
    $ current_voice = "voice/NAE07A_NAE0010.ogg"
    "绹" "「再见啊～♪」"
    window hide


    $ loadBG(0,"BG04A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA02"),"True","lh/SUZ_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0000"
    $ current_voice = "voice/NAE07A_TEN0000.ogg"
    "天王寺" "「哦哦，绹，今天也来了啊」"
    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0000"
    $ current_voice = "voice/NAE07A_SUZ0000.ogg"
    "铃羽" "「绹，早上～好」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0011"
    $ current_voice = "voice/NAE07A_NAE0011.ogg"
    "绹" "「早上～好」"
    "爸爸总是在店里。"
    "打工的姐姐看起来很闲。"
    "我很喜欢打工的姐姐的那种悠然的氛围。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0001"
    $ current_voice = "voice/NAE07A_TEN0001.ogg"
    "天王寺" "「喂打工的，不要教我们家女儿奇怪的打招呼方式」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0001"
    $ current_voice = "voice/NAE07A_SUZ0001.ogg"
    "铃羽" "「诶诶～？　那样的话椎名真由理的“嘟嘟噜♪”不是也不行么？」"
    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0002"
    $ current_voice = "voice/NAE07A_TEN0002.ogg"
    "天王寺" "「那个也有点问题。到底是什么意思。？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0002"
    $ current_voice = "voice/NAE07A_SUZ0002.ogg"
    "铃羽" "「谁知道呢？」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0012"
    $ current_voice = "voice/NAE07A_NAE0012.ogg"
    "绹" "「但是，很可爱哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0003"
    $ current_voice = "voice/NAE07A_TEN0003.ogg"
    "天王寺" "「这样啊。很可爱啊。那样的话说一下也没关系哦」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0013"
    $ current_voice = "voice/NAE07A_NAE0013.ogg"
    "绹" "「恩♪　爸爸，嘟嘟噜♪」"
    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0004"
    $ current_voice = "voice/NAE07A_TEN0004.ogg"
    "天王寺" "「哦哦，嘟，嘟噜？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB03"),"True","lh/SUZ_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0003"
    $ current_voice = "voice/NAE07A_SUZ0003.ogg"
    "铃羽" "「店长，真的很溺爱女儿啊」"
    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0004"
    $ current_voice = "voice/NAE07A_SUZ0004.ogg"
    "铃羽" "「那么溺爱的话，给绹买一辆自行车不也不错么」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0005"
    $ current_voice = "voice/NAE07A_TEN0005.ogg"
    "天王寺" "「那可不行。要是骑着自行车摔了一跤受重伤了那可怎么办啊」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0014"
    $ current_voice = "voice/NAE07A_NAE0014.ogg"
    "绹" "「爸爸，保护过度了啊」"
    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0006"
    $ current_voice = "voice/NAE07A_TEN0006.ogg"
    "天王寺" "「绹，这样好么，上了中学以后就给你买，到那之前先忍一下」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "偶尔，当天花板上传来咚咚声的时候，爸爸肯定会啧一下嘴。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0007"
    $ current_voice = "voice/NAE07A_TEN0007.ogg"
    "天王寺" "「……什么啊？　２楼的那群家伙，又闹腾起来的啊？」"
    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0008"
    $ current_voice = "voice/NAE07A_TEN0008.ogg"
    "天王寺" "「真是的，这群家伙还真安静不下来呢。是时候真的把他们赶出去了」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0005"
    $ current_voice = "voice/NAE07A_SUZ0005.ogg"
    "铃羽" "「诶——赶出去什么的好无情啊」"
    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0009"
    $ current_voice = "voice/NAE07A_TEN0009.ogg"
    "天王寺" "「你说啥？你是想替他们说话吗？」"
    $ stopvoc("SUZ")
    play SUZ "NAE07A_SUZ0006"
    $ current_voice = "voice/NAE07A_SUZ0006.ogg"
    "铃羽" "「那种程度就当没看到吧。那些人现在正在做和这个世界的命运息息相关的事情啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0010"
    $ current_voice = "voice/NAE07A_TEN0010.ogg"
    "天王寺" "「哈，这家伙不行了，也中冈部的毒了」"
    "爸爸总是对于楼上的喧哗有些不满。"
    "好几次，都想要把他们赶出去了。"
    "但是，我感觉并不是动真格的。"
    "最后总是用手抚住光亮的脑袋——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "NAE07A_TEN0011"
    $ current_voice = "voice/NAE07A_TEN0011.ogg"
    "天王寺" "「诶，真是没办法。这次就放过他们了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这么说着温柔地笑着，不知看到过几次。"
    window hide


    $ loadBG(0,"BG05A2")

    "我喜欢有爸爸，有打工的姐姐，还有楼上那群欢闹的“Ｌａｂｍｅｍ”的地方。"
    "虽然说和冈伦叔叔或者桶子叔叔直接说话还有些害怕。"
    "但是在我的记忆中，这个夏天，与在家里等爸爸回来相比，在这里要快乐的多。"

    stop bgm 
    window hide


    $ loadBG(0,"BG04A4")

    show screen phonebtn
    show screen phoneSD1
    "睁开眼睛。"
    "这是，２年之间未曾来过的，爸爸的店。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0015"
    $ current_voice = "voice/NAE07A_NAE0015.ogg"
    "绹" "「……噗嗤」"
    "不行，眼泪又要流出来了。"
    play bgm "FD2BGM01"
    "那个时候。我只是感到“快乐”的时候，其实大家都在守护着我。"
    "现在已经是，谁也不在了。"
    "但是，闭上眼睛的话，我仿佛能穿越时空，听到大家的声音。"
    "大家，一定会继续守护着我的吧。"
    "擦了擦眼泪。"
    "抬起头。"
    show screen phoneSD1
    window hide



    $ loadBG(0,"BG02A3")

    show screen phonebtn
    show screen phoneSD1
    "朝着Ｌａｂ里看去的话，桶子叔叔一副疲劳的样子瘫坐在沙发里。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = 477

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0009"
    $ current_voice = "voice/NAE07A_DAR0009.ogg"
    "至" "「绹酱，学校没问题吗？」"
    call CHECK_RM_RECEIVE
    "看了一下时间，已经过了８点了。"
    call CHECK_RM_RECEIVE
    "如果从这里出发的话，确实是迟到了。"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0016"
    $ current_voice = "voice/NAE07A_NAE0016.ogg"
    "绹" "「偶尔迟到一下，没关系」"

    call CHECK_RM_RECEIVE


    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0010"
    $ current_voice = "voice/NAE07A_DAR0010.ogg"
    "至" "「唔」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0017"
    $ current_voice = "voice/NAE07A_NAE0017.ogg"
    "绹" "「桶子叔叔……我，虽然昨天说了那样的话，果然还是，来帮忙吧？」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0018"
    $ current_voice = "voice/NAE07A_NAE0018.ogg"
    "绹" "「就算什么都不告诉我也好」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0019"
    $ current_voice = "voice/NAE07A_NAE0019.ogg"
    "绹" "「请至少让我把爸爸的电视机修好吧」"
    "桶子叔叔无法完成４２寸显像管电视机的修理。"
    "那是我才能做的事。"
    "是身材娇小的我才能做到的事。"
    "是从爸爸那里学会修理方法的我才能做到的事。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0020"
    $ current_voice = "voice/NAE07A_NAE0020.ogg"
    "绹" "「所以，拜托了……」"
    "低下了头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB06"),"True","lh/DAR_CSB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0011"
    $ current_voice = "voice/NAE07A_DAR0011.ogg"
    "至" "「比起那种事，我快要饿死了啦」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0012"
    $ current_voice = "voice/NAE07A_DAR0012.ogg"
    "至" "「不好意思绹酱，但是能帮我去买点吃的吗？上课迟到也没问题吧？」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0021"
    $ current_voice = "voice/NAE07A_NAE0021.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0013"
    $ current_voice = "voice/NAE07A_DAR0013.ogg"
    "至" "「主要是水。２升装的买１０瓶拜托了。因为又要擦身子又要拿来喝，所以用的很快啊」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0014"
    $ current_voice = "voice/NAE07A_DAR0014.ogg"
    "至" "「无论如何拜托了就算看不起我也没关系。不如说在我们业界这种行为算是赞美所以我没关系的啦」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0015"
    $ current_voice = "voice/NAE07A_DAR0015.ogg"
    "至" "「诶？　难道说要帮我擦身子？绝对没问题啊！让女中学生做这种事我就算马上死了也ＯＫ哦」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0022"
    $ current_voice = "voice/NAE07A_NAE0022.ogg"
    "绹" "「……哈」"
    "我又没说要那么做。"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0023"
    $ current_voice = "voice/NAE07A_NAE0023.ogg"
    "绹" "「桶子叔叔，果然是变态呢……」"
    $ stopvoc("DAR")
    play DAR "NAE07A_DAR0016"
    $ current_voice = "voice/NAE07A_DAR0016.ogg"
    "至" "「不是变态，是变态绅士哦」"
    $ stopvoc("NAE")
    play NAE "NAE07A_NAE0024"
    $ current_voice = "voice/NAE07A_NAE0024.ogg"
    "绹" "「是，是这样吗……」"
    "完全不懂他在说什么。"
    "用不着我请求，桶子叔叔好像现在还是把我当做一个协力者。"
    "对于这一点，我为之一振。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "顺便一提，１０瓶２升的矿泉水我拿不动，所以只买了两瓶。"


    stop bgm 
    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
