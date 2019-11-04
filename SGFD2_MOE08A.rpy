label SGFD2_MOE08A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG34A")

    $ targetmailid = cml.setdefault("RM_MOE_SEND_MAY06","")

    $ LR_RM_CHANCE=1

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY06_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY06_01"])


    play bgm "FD2BGM05"

    $ date="8/15"
    $ day = "SUN"
    hide screen phonebtn
    hide screen phoneSD1

    "从那天开始过了几天我什么都没做，房间也一步都没出过。"
    "正因如此之前囤积的杯面都吃完了。慢慢地连空腹感也感觉不到了，什么也无法思考。"
    "也没有做什么事，就这么一直发呆着。"
    "如果困了就睡一觉，睁开眼睛就起床的日子一天天过去。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0000"
    $ current_voice = "voice/MOE08A_MOE0000.ogg"
    "萌郁" "「…………」"
    "但是现在自己的状态正是求之不得的。"
    "因为根本不知道如何是好。"
    "就这样死了吧什么的，也考虑过。"
    "从ＦＢ那里也没有收到任何邮件。明明之前每天都会给我发的。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "好害怕。和不知道何时到来的死亡相比，活着的现在让我更加害怕。"
    "被ＦＢ抛弃而又一次变得孤独的自己让我更加害怕。"
    "不想失去那个人。不管是给我下达怎样残酷的命令，对我来说她还是重要的人。"
    "所以，只要被命令了什么都能去做。什么都能去破坏。谁都能去杀死。"
    "就算是红莉栖"
    window hide


    $ loadBG(2,"BG34A")



    "想象了一下，心情又变糟了。"
    "那个时候，如果我没有伸手拉住红莉栖的话，她已经死了。"
    "——没有伸手拉住就好了呢。"
    "——伸手拉住真是太好了。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0001"
    $ current_voice = "voice/MOE08A_MOE0001.ogg"
    "萌郁" "「……唔」"
    "感觉脑袋快爆炸了。"
    "细微的呻吟声，最终变成了撕心裂肺的喊叫。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0002"
    $ current_voice = "voice/MOE08A_MOE0002.ogg"
    "萌郁" "「呜呜…………啊啊、啊啊啊啊啊啊啊！」"
    "明明没有喝水，眼泪却止不住地流。还以为自己的眼泪早已流完了。"
    "就算注意到了这一点，也没有什么意义。就算我再怎么哭也不会有人来救我，这一点我很早之前就明白了。"
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_CRS01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "来自ＦＢ的邮件……！？"
    "我跳了起来，取出了手机。"
    window hide
    show screen phoneSD1
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail (p=True)



    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0003"
    $ current_voice = "voice/MOE08A_MOE0003.ogg"
    "萌郁" "「红莉栖……」"
    "并不是ＦＢ发来的邮件。"
    window hide
    call hide_phone

    hide screen phonebtn
    hide screen phoneSD1
    "我关闭了手机，把它扔到了房间的角落里。"
    "在一个人的房间里蜷着身子，等待着ＦＢ的邮件。"
    "因为我除了ＦＢ之外并无所求。ＦＢ是我唯一需要的人。"
    "ＦＢ是我……"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0004"
    $ current_voice = "voice/MOE08A_MOE0004.ogg"
    "萌郁" "「……」"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_CRS01"]
    call read_last_mail

    show screen phoneSD1
    show screen phonebtn

    "从房间的角落里取回了手机。"
    "在屏幕上还显示着来自红莉栖的邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_CRS01"]


    "『我也会等你回来的』"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0005"
    $ current_voice = "voice/MOE08A_MOE0005.ogg"
    "萌郁" "「为什么……要来管我……？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0006"
    $ current_voice = "voice/MOE08A_MOE0006.ogg"
    "萌郁" "「为什么……」"
    window hide
    call hide_phone

    "我握着手机，不知不觉，轻飘飘地站了起来。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG05A2",trans=fade)

    show screen phonebtn
    show screen phoneSD1
    "拖着颤动的脚，花了平时数倍的时间才来到了Ｌａｂ。"
    "走到一半的时候，最近已经无法感受到的空腹感又回来了，肚子咕咕作响。"
    "明明之前还觉得比起被ＦＢ抛弃又变成孤身一人，饿死应该会比较好吧。"
    window hide



    $ loadBG(0,"BG02A2")
    play se "SGSE024"


    "打开了Ｌａｂ的门。突然，欢声笑语洋溢而出。"
    "Ｌａｂ里，很稀奇地全员到齐了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0000"
    $ current_voice = "voice/MOE08A_MAY0000.ogg"
    "真由理" "「啊！　萌郁！」"
    "发现了我的真由理，立刻跑了过来。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA02"),"True","lh/MAY_CLA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0001"
    $ current_voice = "voice/MOE08A_MAY0001.ogg"
    "真由理" "「欢迎欢迎！　等你好久了哦！」"
    hide screen phonebtn
    "就那样抱了上来。我就这么被她用力地抱住了。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0007"
    $ current_voice = "voice/MOE08A_MOE0007.ogg"
    "萌郁" "「那个……」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0002"
    $ current_voice = "voice/MOE08A_MAY0002.ogg"
    "真由理" "「诶——是真的萌郁呢。」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0008"
    $ current_voice = "voice/MOE08A_MOE0008.ogg"
    "萌郁" "「那个……所以说……」"
    "真由理好像不太想放开我的样子。"
    "把脸埋进我的胸部，就好像在确认着我的存在一样，靠了过来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLC04"),"True","lh/MAY_CLC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0003"
    $ current_voice = "voice/MOE08A_MAY0003.ogg"
    "真由理" "「还以为你不会来了呢」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0009"
    $ current_voice = "voice/MOE08A_MOE0009.ogg"
    "萌郁" "「为什么……？」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0004"
    $ current_voice = "voice/MOE08A_MAY0004.ogg"
    "真由理" "「真由喜很迟钝，所以之前肯定是让萌郁生气了吧？　所以一直很担心呐。」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0010"
    $ current_voice = "voice/MOE08A_MOE0010.ogg"
    "萌郁" "「……并不是那样的。」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0011"
    $ current_voice = "voice/MOE08A_MOE0011.ogg"
    "萌郁" "「我……我很高兴哦……你在邮件里说想见我……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA02"),"True","lh/MAY_CLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "真由理从我的胸口抬起头来，温柔地笑了。"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0005"
    $ current_voice = "voice/MOE08A_MAY0005.ogg"
    "真由理" "「因为，本来就很想见面嘛」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0012"
    $ current_voice = "voice/MOE08A_MOE0012.ogg"
    "萌郁" "「真由理……」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA02"),"True","lh/FEI_BSA02a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0000"
    $ current_voice = "voice/MOE08A_FEI0000.ogg"
    "菲利斯" "「萌喵，好久不见喵」"
    "在我被这样抱住的时候，菲利斯也过来了。"
    "像猫咪那样接近了我们，轻轻地拍了拍真由理的肩膀。"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMB01"),"True","lh/FEI_BMB01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0001"
    $ current_voice = "voice/MOE08A_FEI0001.ogg"
    "菲利斯" "「真由喜，真由喜。萌喵有些困扰了喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA04"),"True","lh/MAY_CLA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0006"
    $ current_voice = "voice/MOE08A_MAY0006.ogg"
    "真由理" "「诶？抱歉萌郁，真由喜又失败了么？」"
    "我一个激灵捉住了已经松开的真由理的手。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0013"
    $ current_voice = "voice/MOE08A_MOE0013.ogg"
    "萌郁" "「没关系……完全不困扰……」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0007"
    $ current_voice = "voice/MOE08A_MAY0007.ogg"
    "真由理" "「……真、真的吗？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0014"
    $ current_voice = "voice/MOE08A_MOE0014.ogg"
    "萌郁" "「……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA02"),"True","lh/MAY_CLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA02"),"True","lh/FEI_BMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我一点头，真由理的表情便多云转晴。"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0008"
    $ current_voice = "voice/MOE08A_MAY0008.ogg"
    "真由理" "「诶嘿嘿嘿。谢谢了啊。萌郁果然很温柔呢。」"

    stop bgm 
    "看着她的笑容，本应已经彻底冻结的胸膛又变得温暖起来。"
    window hide
    play se "SGSE031"


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA03"),"True","lh/MAY_CLA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC01"),"True","lh/FEI_BMC01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM09"

    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0015"
    $ current_voice = "voice/MOE08A_MOE0015.ogg"
    "萌郁" "「……」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0009"
    $ current_voice = "voice/MOE08A_MAY0009.ogg"
    "真由理" "「萌郁，肚子饿了吗？」"
    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0002"
    $ current_voice = "voice/MOE08A_FEI0002.ogg"
    "菲利斯" "「发出了好厉害的声音喵」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0016"
    $ current_voice = "voice/MOE08A_MOE0016.ogg"
    "萌郁" "「……最近什么都没吃」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0010"
    $ current_voice = "voice/MOE08A_MAY0010.ogg"
    "真由理" "「那就尝尝这个吧！」"
    "真由理把放在桌子上的炸鸡块拿了过来。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0017"
    $ current_voice = "voice/MOE08A_MOE0017.ogg"
    "萌郁" "「但是……」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0011"
    $ current_voice = "voice/MOE08A_MAY0011.ogg"
    "真由理" "「没关系哦。是真由喜买的所以就放心吃吧」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0018"
    $ current_voice = "voice/MOE08A_MOE0018.ogg"
    "萌郁" "「……谢谢。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我收下了炸鸡块，吃了起来。这时在Ｌａｂ里面的红莉栖走了过来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC01"),"True","lh/CRS_BSC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0000"
    $ current_voice = "voice/MOE08A_CRS0000.ogg"
    "红莉栖" "「好久不见啊，萌郁」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0019"
    $ current_voice = "voice/MOE08A_MOE0019.ogg"
    "萌郁" "「红莉栖」"
    "今天的红莉栖和平时不太一样，没有那种锐气，反而是一副心神不定的样子。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC02"),"True","lh/CRS_BSC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0001"
    $ current_voice = "voice/MOE08A_CRS0001.ogg"
    "红莉栖" "「那个，该说些什么好呢……这种时候」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE08A_DAR0000"
    $ current_voice = "voice/MOE08A_DAR0000.ogg"
    "至" "「只要微笑就可以了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB04"),"True","lh/CRS_BSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0002"
    $ current_voice = "voice/MOE08A_CRS0002.ogg"
    "红莉栖" "「桥田，别说风凉话！冈部也不准笑！……真是的」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "回头瞪了一眼窃笑的冈部之后，红莉栖站在了我的面前。"
    "大大地吸了一口气，微笑着。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA06"),"True","lh/CRS_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0003"
    $ current_voice = "voice/MOE08A_CRS0003.ogg"
    "红莉栖" "「萌郁。你能回来……十分感谢。」"
    "再一次，胸口感受到了温暖。我，不知不觉地回答了她。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0020"
    $ current_voice = "voice/MOE08A_MOE0020.ogg"
    "萌郁" "「……嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA02"),"True","lh/CRS_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0004"
    $ current_voice = "voice/MOE08A_CRS0004.ogg"
    "红莉栖" "「虽然刚才解开了误会，但最近看真由理一副寂寞的样子十分难受呢。」"
    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0000"
    $ current_voice = "voice/MOE08A_OKA0000.ogg"
    "伦太郎" "「你也没好到哪里去嘛。问了我几次“萌郁来了吗？”了啊。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB09"),"True","lh/CRS_BSB09a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖的脸变得通红，狠狠地盯着冈部君。"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0005"
    $ current_voice = "voice/MOE08A_CRS0005.ogg"
    "红莉栖" "「你、你这家伙！」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0021"
    $ current_voice = "voice/MOE08A_MOE0021.ogg"
    "萌郁" "「……是这样吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC02"),"True","lh/CRS_BSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0006"
    $ current_voice = "voice/MOE08A_CRS0006.ogg"
    "红莉栖" "「诶？啊呀，怎么说呢，虽然冈部说的没有错但那个说法听起来，嗯……」"
    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0001"
    $ current_voice = "voice/MOE08A_OKA0001.ogg"
    "伦太郎" "「突然乱了马脚呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB09"),"True","lh/CRS_BSB09a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0007"
    $ current_voice = "voice/MOE08A_CRS0007.ogg"
    "红莉栖" "「你以为是谁的原因啊！」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0008"
    $ current_voice = "voice/MOE08A_CRS0008.ogg"
    "红莉栖" "「……咳咳。总之，你能来让我很高兴啊」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0022"
    $ current_voice = "voice/MOE08A_MOE0022.ogg"
    "萌郁" "「……嗯」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0012"
    $ current_voice = "voice/MOE08A_MAY0012.ogg"
    "真由理" "「今天，我们为萌郁恢复精神召开一个派对吧！」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0002"
    $ current_voice = "voice/MOE08A_OKA0002.ogg"
    "伦太郎" "「说到底，难道不是时间机器完成派对吗！」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB04"),"True","lh/CRS_BSB04a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0009"
    $ current_voice = "voice/MOE08A_CRS0009.ogg"
    "红莉栖" "「别插科打诨」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0003"
    $ current_voice = "voice/MOE08A_OKA0003.ogg"
    "伦太郎" "「……今天我对于刚说的表示抱歉」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB02"),"True","lh/CRS_BSB02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0010"
    $ current_voice = "voice/MOE08A_CRS0010.ogg"
    "红莉栖" "「算你识相」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "这样啊——时间机器完成了啊。"
    "有些温暖的胸口，又冰冷起来。"
    "作为Ｌａｂｍｅｍ ，我当然很高兴。"
    "但是作为Ｒｏｕｎｄｅｒ来说，是很危险的。如果继续研究下去的话，他们的生命会有危险……"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0023"
    $ current_voice = "voice/MOE08A_MOE0023.ogg"
    "萌郁" "「真的……完成了时间机器……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈部君把手忽的放到了我的肩上。"
    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0004"
    $ current_voice = "voice/MOE08A_OKA0004.ogg"
    "伦太郎" "「是呢。多亏了你们去买回来的零件，已经顺利地完成了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA02"),"True","lh/OKA_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0005"
    $ current_voice = "voice/MOE08A_OKA0005.ogg"
    "伦太郎" "「所以说指压师哦，你不来这里的话，派对就没法开始咯！」"
    "大家，一点都没有变。"

    $ targetmailid = 418

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    "还是像以前一样……一如既往地欢迎我来到Ｌａｂ。"
    call CHECK_RM_RECEIVE
    "停止了思考而冻结的心灵，开始慢慢回暖。"
    window hide


    $ loadBG(2,"BG01A")



    play bgm "BGM05"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "MOE08A_SUZ0000"
    $ current_voice = "voice/MOE08A_SUZ0000.ogg"
    "铃羽" "「呐呐。调理的道具已经完成了哦。啊，桐生萌郁如果有空的话能帮个忙吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0024"
    $ current_voice = "voice/MOE08A_MOE0024.ogg"
    "萌郁" "「……调理？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0025"
    $ current_voice = "voice/MOE08A_MOE0025.ogg"
    "萌郁" "「你们……在做什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA02"),"True","lh/SUZ_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "MOE08A_SUZ0001"
    $ current_voice = "voice/MOE08A_SUZ0001.ogg"
    "铃羽" "「咖喱饭。要满足这么多人的口味这个是最适合不过了呢」"

    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0026"
    $ current_voice = "voice/MOE08A_MOE0026.ogg"
    "萌郁" "「咖喱饭……」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_CRS03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_CRS03_01"])

    play se "SGSE031"

    "只是听到了名字，肚子又叫了起来。"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA01"),"True","lh/FEI_BSA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0003"
    $ current_voice = "voice/MOE08A_FEI0003.ogg"
    "菲利斯" "「喵哈哈。稍微多买了点材料果然是正确的喵」"
    window hide





    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)









    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_WARAI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_WARAI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_WARAI"])
    $ stopvoc("DAR")
    play DAR "MOE08A_DAR0001"
    $ current_voice = "voice/MOE08A_DAR0001.ogg"
    "至" "「菲利斯碳要下厨？难道说，是ＭａｙＱｕｅｅｎ的秘传咖喱？唔哦哦哦哦！超{color=#f00}ｗ{/color}级{color=#f00}ｗ{/color}期{color=#f00}ｗ{/color}待{color=#f00}ｗ{/color}的{color=#f00}ｗ{/color}说{color=#f00}ｗ{/color}」"


    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0011"
    $ current_voice = "voice/MOE08A_CRS0011.ogg"
    "红莉栖" "「桥田，给我自重点」"
    $ stopvoc("DAR")
    play DAR "MOE08A_DAR0002"
    $ current_voice = "voice/MOE08A_DAR0002.ogg"
    "至" "「但是我拒绝！」"
    window hide


    $ loadBG(2,"BG01A")



    "接受了邀请的我和阿万音，真由理，红莉栖，漆原还有菲利斯一起做了咖喱。"
    "由在女仆咖啡厅打工的菲利斯指挥，真由理和红莉栖切蔬菜。漆原负责看锅子。"
    "我……由于不擅长做料理，担任了尝味道的工作。"
    "咖喱的制作顺利进行中，锅子里已经散发出诱人的香味了。"
    "这时，红莉栖拿着从罐头里取出来的菠萝站在锅前。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA02"),"True","lh/CRS_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0012"
    $ current_voice = "voice/MOE08A_CRS0012.ogg"
    "红莉栖" "「接下来放这个试试？」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0013"
    $ current_voice = "voice/MOE08A_MAY0013.ogg"
    "真由理" "「啊，是菠萝呢。看起来很好吃的样子♪」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA02"),"True","lh/CRS_BSA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "MOE08A_RUK0000"
    $ current_voice = "voice/MOE08A_RUK0000.ogg"
    "琉华" "「牧，牧濑！？真的是认真的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0013"
    $ current_voice = "voice/MOE08A_CRS0013.ogg"
    "红莉栖" "「怎么了漆原？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "MOE08A_RUK0001"
    $ current_voice = "voice/MOE08A_RUK0001.ogg"
    "琉华" "「不是，这个……不要放菠萝感觉会比较好吃哦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB01"),"True","lh/CRS_BSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0014"
    $ current_voice = "voice/MOE08A_CRS0014.ogg"
    "红莉栖" "「是这样的吗？我觉得实践出真知哦。」"
    $ stopvoc("RUK")
    play RUK "MOE08A_RUK0002"
    $ current_voice = "voice/MOE08A_RUK0002.ogg"
    "琉华" "「请不要把科学和料理，混为一谈……！」"
    "在红莉栖即将把菠萝投入锅中的那一瞬间，菲利斯以极快的速度捉住了她的手腕。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC04"),"True","lh/CRS_BSC04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0004"
    $ current_voice = "voice/MOE08A_FEI0004.ogg"
    "菲利斯" "「红喵，稍等一下喵！」"
    "一直露出明亮的笑容的菲利斯少见地苦笑了一下。"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0015"
    $ current_voice = "voice/MOE08A_CRS0015.ogg"
    "红莉栖" "「好，好的！」"
    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0005"
    $ current_voice = "voice/MOE08A_FEI0005.ogg"
    "菲利斯" "「那个绝对，不能放进去喵」"
    "红莉栖被菲利斯的眼神所震慑，把罐头放下了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA05"),"True","lh/CRS_BSA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0016"
    $ current_voice = "voice/MOE08A_CRS0016.ogg"
    "红莉栖" "「……是。非常抱歉。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0006"
    $ current_voice = "voice/MOE08A_FEI0006.ogg"
    "菲利斯" "「呐凶真。难道说红喵是……」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0006"
    $ current_voice = "voice/MOE08A_OKA0006.ogg"
    "伦太郎" "「不愧是菲利斯。正如你所见，Ｃｈｒｉｓｔｉｎａ是烹饪无能系女子呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA03"),"True","lh/CRS_BSA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0017"
    $ current_voice = "voice/MOE08A_CRS0017.ogg"
    "红莉栖" "「烹饪无能系女子是什么鬼啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0007"
    $ current_voice = "voice/MOE08A_OKA0007.ogg"
    "伦太郎" "「怎么看你那味觉都已经说明你是烹饪无能系女子了吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB05"),"True","lh/CRS_BSB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0018"
    $ current_voice = "voice/MOE08A_CRS0018.ogg"
    "红莉栖" "「你说什么！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0008"
    $ current_voice = "voice/MOE08A_OKA0008.ogg"
    "伦太郎" "「助手哦。你为什么会想往咖喱里面放菠萝呢？」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0019"
    $ current_voice = "voice/MOE08A_CRS0019.ogg"
    "红莉栖" "「那是因为觉得可能会让咖喱更好吃。」"
    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0009"
    $ current_voice = "voice/MOE08A_OKA0009.ogg"
    "伦太郎" "「也就是说有这个可能性你就会这么做咯？」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0020"
    $ current_voice = "voice/MOE08A_CRS0020.ogg"
    "红莉栖" "「难道不是吗。无法证明的东西就否定掉，这可不像你的作风哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0010"
    $ current_voice = "voice/MOE08A_OKA0010.ogg"
    "伦太郎" "「不能把科学家的思维带入料理啊！你是想让我们的舌头都坏掉吗？」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0021"
    $ current_voice = "voice/MOE08A_CRS0021.ogg"
    "红莉栖" "「那种事不试一下怎么会知道呢……」"
    $ stopvoc("RUK")
    play RUK "MOE08A_RUK0003"
    $ current_voice = "voice/MOE08A_RUK0003.ogg"
    "琉华" "「只要有百分之一的可能性会让料理失败，那就还是不要尝试比较好……」"
    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0011"
    $ current_voice = "voice/MOE08A_OKA0011.ogg"
    "伦太郎" "「我知道的！　咖喱里面放菠萝会大失败！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA03"),"True","lh/CRS_BSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0022"
    $ current_voice = "voice/MOE08A_CRS0022.ogg"
    "红莉栖" "「你有什么确切的证据嘛？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0012"
    $ current_voice = "voice/MOE08A_OKA0012.ogg"
    "伦太郎" "「不，不是……那个是……第六感。对，Ｍａｄ　Ｓｃｉｅｎｔｉｓｔ的第六感」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0014"
    $ current_voice = "voice/MOE08A_MAY0014.ogg"
    "真由理" "「其实呢，冈伦家里是开蔬果店的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB06"),"True","lh/OKA_ASB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0013"
    $ current_voice = "voice/MOE08A_OKA0013.ogg"
    "伦太郎" "「等等，真由理！　别把那个说出来啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0015"
    $ current_voice = "voice/MOE08A_MAY0015.ogg"
    "真由理" "「以前，冈伦试过把卖剩下的菠萝加到过咖喱里面去哦，那味道最后变得非常不得了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0014"
    $ current_voice = "voice/MOE08A_OKA0014.ogg"
    "伦太郎" "「啊啊……那真是地狱般的感觉啊」"
    $ stopvoc("RUK")
    play RUK "MOE08A_RUK0004"
    $ current_voice = "voice/MOE08A_RUK0004.ogg"
    "琉华" "「原来如此……难怪知道咖喱和菠萝的组合非常糟糕呢。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0023"
    $ current_voice = "voice/MOE08A_CRS0023.ogg"
    "红莉栖" "「哈。但，冈部开了一家蔬果店……噗，真难以相信啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0015"
    $ current_voice = "voice/MOE08A_OKA0015.ogg"
    "伦太郎" "「咕唔……不要提到我家里的事情啦。」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA01"),"True","lh/FEI_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("FEI")
    play FEI "MOE08A_FEI0007"
    $ current_voice = "voice/MOE08A_FEI0007.ogg"
    "菲利斯" "「咳咳。大家都说完了吗？打破常识之前，要先了解常识是怎样的哦？」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0024"
    $ current_voice = "voice/MOE08A_CRS0024.ogg"
    "红莉栖" "「……明白了。那么这份求知欲就留到下次吧。」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB07"),"True","lh/CRS_BSB07a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE08A_OKA0016"
    $ current_voice = "voice/MOE08A_OKA0016.ogg"
    "伦太郎" "「这算明白什么了呀！」"
    "看着冈部和红莉栖的相互吐槽，大家都笑了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我也不知何时笑了起来。心情十分开心，感到十分满足。"
    "和孤独的时候的心情不一样，现在的心情十分温暖。"
    "不想失去……给了我这样的心情的Ｌａｂ的各位。不想失去……这样的宝贵的日常。"
    "我想要，留在这里……"

    stop bgm 

    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "短暂的震动。"

    "不是电话，而是邮件。Ｌａｂｍｅｍ里谁也没有用手机。"

    "除了Ｌａｂｍｅｍ以外，会给我发邮件的人……只有一个。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail (p=True)








    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0027"
    $ current_voice = "voice/MOE08A_MOE0027.ogg"
    "萌郁" "「…………」"
    play bgm "BGM25"
    "全身的血都聚集到了头上。心跳仿佛要停止了，呼吸也变得慌乱。"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0016"
    $ current_voice = "voice/MOE08A_MAY0016.ogg"
    "真由理" "「萌郁，你没事吧？」"
    window hide
    call hide_phone

    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0028"
    $ current_voice = "voice/MOE08A_MOE0028.ogg"
    "萌郁" "「我、我没事……」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0017"
    $ current_voice = "voice/MOE08A_MAY0017.ogg"
    "真由理" "「但，有什么的话请务必说出来哦？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0029"
    $ current_voice = "voice/MOE08A_MOE0029.ogg"
    "萌郁" "「嗯……」"
    "如果不回复邮件的话，就会被ＦＢ抛弃。"
    "无法执行任务的我没有价值……"
    "不能背叛她。ＦＢ，是将我的命捡回来的人。"
    "但是，要是服从她的命令的话……"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0030"
    $ current_voice = "voice/MOE08A_MOE0030.ogg"
    "萌郁" "「我稍微……去呼吸下新鲜空气……」"
    window hide



    $ loadBG(0,"BG05A1")

    "试着瞄了一眼营业中的显像管工房，天王寺店长正在用大型显像管电视机看着综艺节目。"
    "因为想在店前的长椅坐一会，他没看向这边真是帮了大忙了。"
    window hide


    $ loadBG(2,"BG39A")




    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)


    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_EDIT_TEN01_00"]

    "我坐到了长椅上，写起了给ＦＢ的邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_SEND_TEN01"]
    call send_mail (id=[249,250,251], send=False)


    "不对，这封邮件，不能发……"
    "向ＦＢ提建议什么的……但是……"
    "指尖颤动着。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_SEND_TEN02"]
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[252,253], send=False)


    "不行。这样的话，就救不了和研究无关的菲利斯和真由理等人了。"
    window hide

    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0031"
    $ current_voice = "voice/MOE08A_MOE0031.ogg"
    "萌郁" "「该怎么办……才好呢……」"
    "后来无论怎么考虑，都没有想到在不背叛ＦＢ的前提下帮助大家的办法。"
    "我什么力量也没有。试图反抗什么的果然是愚蠢的想法吧。"
    "感到一阵空虚，我又开始操作起了手机。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[254,255])

    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_EDIT_TEN03_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_SEND_TEN03"]








    call hide_phone

    "这样就好了。"
    "我无法理解。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_TEN02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail (p=True)



    "完全被看透了。"
    "明明这时应该感到安心和喜悦，但如今只是害怕着她。"
    "……不能让她失望。否则的话，就会被抛弃。"
    "被抛弃的话……我就会回到以前的自己。孤身一人的桐生萌郁"
    window hide
    call hide_phone

    "又想起了站在大楼顶上向下看着地面的那一天。"
    "确实我被ＦＢ救了回来。从桐生萌郁变成了Ｍ４。"
    "并没有和ＬＡＢ的各位保证一直在一起。"
    "为了ＦＢ活着的话就不会被抛弃。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA01"),"True","lh/MAY_AMA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0025"
    $ current_voice = "voice/MOE08A_CRS0025.ogg"
    "红莉栖" "「在这里啊。」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0018"
    $ current_voice = "voice/MOE08A_MAY0018.ogg"
    "真由理" "「怎么了吗？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0032"
    $ current_voice = "voice/MOE08A_MOE0032.ogg"
    "萌郁" "「……」"
    "看着两人的眼睛就明白了。"
    "我从现在开始，再也不会考虑些背叛了大家的歪点子了吧。"
    "原因就算不用想也知道。"
    "被信任着。我。作为Ｌａｂｍｅｍ 。"
    "这些人不知道Ｍ４。只是单纯地把我当做Ｌａｂｍｅｍ ……伙伴，信任着我。"
    "但是……我却……"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALA04"),"True","lh/CRS_ALA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0026"
    $ current_voice = "voice/MOE08A_CRS0026.ogg"
    "红莉栖" "「萌郁」"
    "红莉栖坐在了我的身边。"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0027"
    $ current_voice = "voice/MOE08A_CRS0027.ogg"
    "红莉栖" "「真的没关系吗……？看起来好像因为什么难过着哦？」"
    "被这样温柔的声音询问，不由得失神了。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0033"
    $ current_voice = "voice/MOE08A_MOE0033.ogg"
    "萌郁" "「什么也……没有……」"
    "否定的话语说到一半。"
    window hide
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ALA03"),"True","lh/MAY_ALA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0019"
    $ current_voice = "voice/MOE08A_MAY0019.ogg"
    "真由理" "「怎么了，萌郁。真由喜，难道又做错了什么？」"
    "真由理紧紧地握住我的手。"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0034"
    $ current_voice = "voice/MOE08A_MOE0034.ogg"
    "萌郁" "「真的没什么。真的……没什么……」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0028"
    $ current_voice = "voice/MOE08A_CRS0028.ogg"
    "红莉栖" "「并不是真的没什么吧」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0020"
    $ current_voice = "voice/MOE08A_MAY0020.ogg"
    "真由理" "「就是哦。因为，萌郁现在快要哭出来了哦？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0035"
    $ current_voice = "voice/MOE08A_MOE0035.ogg"
    "萌郁" "「真的没什么……所以……」"
    "不该说出来的。"
    "我现在开始要考虑如何杀掉你们，这种话。"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0029"
    $ current_voice = "voice/MOE08A_CRS0029.ogg"
    "红莉栖" "「是什么不能对我们说的话吧？」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0036"
    $ current_voice = "voice/MOE08A_MOE0036.ogg"
    "萌郁" "「……」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0030"
    $ current_voice = "voice/MOE08A_CRS0030.ogg"
    "红莉栖" "「……明白了」"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "是把我的沉默当做肯定了吗，红莉栖离开了我。"
    "被讨厌了吧。"
    "那也好。"
    "再讨厌一点就更好了"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "但是红莉栖很快又用认真的眼神看着我。"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0031"
    $ current_voice = "voice/MOE08A_CRS0031.ogg"
    "红莉栖" "「如果说不了的话，不用说出来也没关系哦。现在。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0032"
    $ current_voice = "voice/MOE08A_CRS0032.ogg"
    "红莉栖" "「但是，请记住呢」"
    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0033"
    $ current_voice = "voice/MOE08A_CRS0033.ogg"
    "红莉栖" "「如果说，萌郁被奇怪的目光所注视，或者有什么不好的回忆的话，我们一定会帮助你的」"
    $ stopvoc("MOE")
    play MOE "MOE08A_MOE0037"
    $ current_voice = "voice/MOE08A_MOE0037.ogg"
    "萌郁" "「……为什么」"
    "为什么不能讨厌我一些呢？"
    "我明明不是能给予你们帮助的人类啊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ALA02"),"True","lh/MAY_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "真由理握着我的手，笑了起来。"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0021"
    $ current_voice = "voice/MOE08A_MAY0021.ogg"
    "真由理" "「要问问什么，当然是因为我们是朋友嘛」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA06"),"True","lh/CRS_AMA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "两人都重重地点了点头。"
    "Ｌａｂｍｅｍ。伙伴。朋友。"
    "那是，一直会呆在身边的吧。"
    "肯定是，不会让我孤身一人的吧。"
    "就算，我是残酷的背叛者……？"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALA06"),"True","lh/CRS_ALA06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE08A_CRS0034"
    $ current_voice = "voice/MOE08A_CRS0034.ogg"
    "红莉栖" "「冷静下来的话，就回Ｌａｂ吧。漆原和菲利斯要提前回去，所以在那之前让我们干杯吧」"
    $ stopvoc("MAY")
    play MAY "MOE08A_MAY0022"
    $ current_voice = "voice/MOE08A_MAY0022.ogg"
    "真由理" "「冷静下来就好了呢」"
    hide screen phonebtn
    "我的双手，被两人温柔的手掌包裹住了。"
    "就算我是背叛者，这两双手也不会松开吗？"
    "并没有问出口。"
    $ targetmailid = gc["ScriptMacros"]["FM_MOE08A_RECV_TEN03"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "口袋里的手机又收到了邮件。"
    "但是两人的手依然保持着之前的姿势，没有松开。"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return





    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    return
