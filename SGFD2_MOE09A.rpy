label SGFD2_MOE09A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG02N1")


    play bgm "FD2BGM05"

    $ date="8/15"
    python:
        RcvMail(257)
        ReadMail(257)
        SndMail(258)
        RcvMail(259)
        ReadMail(259)
        RcvMail(260)
        ReadMail(260)
        RcvMail(261)
        ReadMail(261)
        SndMail(262)
        RcvMail(263)
        ReadMail(263)
    show screen phonebtn
    show screen phoneSD1

    "Ｌａｂ里的派对开始了，大家都兴高采烈的样子。"
    "在那之中，我在Ｌａｂ的角落里，继续给ＦＢ发邮件。"
    "但是，现在应该不会停止本次作战了……也没有从ＦＢ那里收到和其他Ｒｏｕｎｄｅｒ汇合以外的邮件。"
    "注意到的时候，离作战开始就只剩几分钟了。"
    "怎么办啊怎么办啊怎么办啊怎么办啊怎么办啊……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0000"
    $ current_voice = "voice/MOE09A_MAY0000.ogg"
    "真由理" "「……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0000"
    $ current_voice = "voice/MOE09A_MOE0000.ogg"
    "萌郁" "「……真由理？」"
    "注意到的时候，真由理正微笑着摸着我的头。"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0001"
    $ current_voice = "voice/MOE09A_MAY0001.ogg"
    "真由理" "「大家都很担心你哦。但是呐，他们都不太好意思，就派真由喜过来当信使了。」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0001"
    $ current_voice = "voice/MOE09A_MOE0001.ogg"
    "萌郁" "「……抱歉」"
    "接下来……难道把这些告诉大家然后一起逃跑吗？"
    "那样的话，我是Ｒｏｕｎｄｅｒ的背叛者这一点就暴露了。"
    "这样的话……大家肯定，不会把我当做朋友了。"
    "而且，如果说出来的话ＦＢ也肯定抛弃我了。"
    "——不想再变成一个人了。"
    "背叛ＦＢ实在是太恐怖了。"
    "但是，也不希望大家就这么死去。"
    "到底怎么做才好了？我，该怎么办呢……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB03"),"True","lh/MAY_CMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0002"
    $ current_voice = "voice/MOE09A_MAY0002.ogg"
    "真由理" "「虽然真由喜不懂很复杂的事情……」"
    "我一定是苦着一张脸吧。"
    "真由理一如既往地微笑着。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0003"
    $ current_voice = "voice/MOE09A_MAY0003.ogg"
    "真由理" "「但真由喜呢，不论何时都是萌郁的伙伴哦」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0002"
    $ current_voice = "voice/MOE09A_MOE0002.ogg"
    "萌郁" "「……！」"

    stop bgm 
    "真由理的话让我把烦恼抛到了脑后。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0003"
    $ current_voice = "voice/MOE09A_MOE0003.ogg"
    "萌郁" "「真由理……那个……那个呢」"
    "一旦开口说了，就停不下来了。"
    "说出来吧。"
    "把一切都告诉大家——和大家，一起逃跑吧。"
    hide screen phoneSD1
    window hide
    play se "SGSE058"

    play bgm "BGM08"



    $ loadBG(2,"EVX_Z03A")



    hide screen phonebtn
    "突然，全副武装的人冲进了Ｌａｂ。"
    play se "SGSE060"

    $ stopvoc("Y01")
    play KUR "MOE09A_Y010000"
    $ current_voice = "voice/MOE09A_Y010000.ogg"
    "巡行者Ａ" "「不准动！」"
    "因为突然事件，大家都被吓了一跳，在原地动弹不得。"
    "我的决心……看起来下晚了。"
    $ stopvoc("DAR")
    play DAR "MOE09A_DAR0000"
    $ current_voice = "voice/MOE09A_DAR0000.ogg"
    "至" "「什什、什么啊！？」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0000"
    $ current_voice = "voice/MOE09A_OKA0000.ogg"
    "伦太郎" "「诶、等……！？」"
    "因为是相同的存在所以我明白。无法与Ｒｏｕｎｄｅｒ交流。"
    "看起来像头领的男子，用下巴催促我们行动。"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010001"
    $ current_voice = "voice/MOE09A_Y010001.ogg"
    "巡行者Ａ" "「全部举起手来站成一排」"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010002"
    $ current_voice = "voice/MOE09A_Y010002.ogg"
    "巡行者Ａ" "「快点！」"
    "按照他的命令，所有人举起手站成了一排。"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010003"
    $ current_voice = "voice/MOE09A_Y010003.ogg"
    "巡行者Ａ" "「时间机器在哪里？交出来的话就放过你们」"
    "骗人。明明有杀害命令。"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0001"
    $ current_voice = "voice/MOE09A_OKA0001.ogg"
    "伦太郎" "「时间机器吗！？　现、现在就给你，所以不要对我的同伴──」"
    window hide
    play se "SGSE069"



    $ loadBG(2,"BG01N")



    show screen phonebtn
    show screen phoneSD1
    "正在确认大家情况的冈部君的表情，突然变得惊讶起来。"
    "微开的门缝里，有什么被丢进来了。"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010004"
    $ current_voice = "voice/MOE09A_Y010004.ogg"
    "巡行者Ａ" "「烟雾弹吗！？」"
    "Ｒｏｕｎｄｅｒ的视线全部集中到了滚到地板上的东西。"
    "──那是毫无特别之处的手机。"
    "在那些男子被手机吸引了注意力的瞬间，阿万音如同疾风般冲了进来。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"EVX_S11A")



    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0000"
    $ current_voice = "voice/MOE09A_SUZ0000.ogg"
    "铃羽" "「喝！」"
    window hide
    play se "SGSE066"


    "阿万音以流畅的动作，肘击了首领。"
    "从首领手中夺过了落下的手枪，开了枪。"
    play se "SGSE332"

    "枪声有两发。"
    $ stopvoc("Y02")
    play KUR "MOE09A_Y020000"
    $ current_voice = "voice/MOE09A_Y020000.ogg"
    "巡行者Ｂ" "「咕哇！」"
    "有两名Ｒｏｕｎｄｅｒ应声松开了手枪。"
    "Ｒｏｕｎｄｅｒ还有三个人剩余，虽然事出突然有些困惑，但还是架好了手枪。"
    "但是，阿万音的动作更快。"
    play se "SGSE332"
    "她向那些人的方向开了几枪，使得他们慌张地向门附近撤退。"
    window hide



    $ loadBG(2,"BG01N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0001"
    $ current_voice = "voice/MOE09A_SUZ0001.ogg"
    "铃羽" "「窗口边上有绳子，快逃啊！」"
    "不停地向Ｒｏｕｎｄｅｒ射击中的阿万音大叫道。"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0002"
    $ current_voice = "voice/MOE09A_OKA0002.ogg"
    "伦太郎" "「那你怎么办！」"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0002"
    $ current_voice = "voice/MOE09A_SUZ0002.ogg"
    "铃羽" "「我等会过来！先担心你自己吧！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0003"
    $ current_voice = "voice/MOE09A_OKA0003.ogg"
    "伦太郎" "「……了解了！　快走吧各位！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0004"
    $ current_voice = "voice/MOE09A_MAY0004.ogg"
    "真由理" "「嗯，嗯！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE09A_DAR0001"
    $ current_voice = "voice/MOE09A_DAR0001.ogg"
    "至" "「ｏ，ｏ，ｏｋ！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0000"
    $ current_voice = "voice/MOE09A_CRS0000.ogg"
    "红莉栖" "「虽然不太明白是怎么回事！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我正打算和大家一起逃跑的瞬间——"

    stop bgm 

    $ targetmailid = gc["ScriptMacros"]["FM_MOE09A_RECV_TEN04"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "手中的手机响了。"

    "是ＦＢ发来的。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "和平时一样，我打开了手机。"
    window hide
    call read_last_mail (p=True)





    "感觉身体被冻住了一样，我停下了脚步。"
    window hide
    call hide_phone



    $ loadBG(2,"BG02N1")



    play bgm "FD2BGM04"
    "不停地向四周张望。"
    "ＦＢ……在哪里看着现在的情况呢？"
    window hide


    $ loadBG(2,"BG01N")



    "她看得见我吗？"
    "……现在，正在被监视着。"
    "但是，如果不行动的话……会被抛弃。"
    "心中的恐惧汹涌而出。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE09A_RECV_TEN05"]
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
    call read_last_mail



    "像母亲一样的ＦＢ。救了我的ＦＢ。对我来说是必要的ＦＢ。"
    "要是被抛弃的话，又要只身一人了。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0004"
    $ current_voice = "voice/MOE09A_MOE0004.ogg"
    "萌郁" "「不要啊……」"
    "ＦＢ还需要我。"
    "最后的机会。"
    "这是，最后的机会……"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE09A_RECV_TEN06"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call read_last_mail (p=True)







    "看了那封邮件。"
    "我。"
    window hide
    call hide_phone

    hide screen phoneSD1
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE002A"]]["Check"]=True


    $ loadBG(2,"EV_MOE002A")



    hide screen phonebtn
    stop bgm 
    "迅速地捡起了脚下的手枪。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0005"
    $ current_voice = "voice/MOE09A_MOE0005.ogg"
    "萌郁" "「不准，动。」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0001"
    $ current_voice = "voice/MOE09A_CRS0001.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0005"
    $ current_voice = "voice/MOE09A_MAY0005.ogg"
    "真由理" "「萌、郁？」"
    $ stopvoc("DAR")
    play DAR "MOE09A_DAR0002"
    $ current_voice = "voice/MOE09A_DAR0002.ogg"
    "至" "「桐生氏？」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0004"
    $ current_voice = "voice/MOE09A_OKA0004.ogg"
    "伦太郎" "「你在做什么！」"
    play bgm "BGM20"
    "Ｌａｂｍｅｍ的各位，都满脸惊讶地看着我。"
    "……啊啊，暴露了啊。"
    "我是一个……背叛者。"
    "已经，不是大家的朋友了。"
    "——那样的话，不如。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0006"
    $ current_voice = "voice/MOE09A_MOE0006.ogg"
    "萌郁" "「我是……Ｍ４。ＳＥＲＮ的，Ｒｏｕｎｄｅｒ」"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0003"
    $ current_voice = "voice/MOE09A_SUZ0003.ogg"
    "铃羽" "「桐生萌郁！？　为什么！　──咕啊！」"
    "一瞬间走神的阿万音被Ｒｏｕｎｄｅｒ们踢飞了。"
    "倒在地板上的阿万音，被Ｒｏｕｎｄｅｒ给制服了。就连那样厉害的阿万音，也好像动不了了。"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0005"
    $ current_voice = "voice/MOE09A_OKA0005.ogg"
    "伦太郎" "「铃羽！」"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010005"
    $ current_voice = "voice/MOE09A_Y010005.ogg"
    "巡行者Ａ" "「看来很听话呢。你懂的吧，Ｍ４」"
    "向首领点了点头。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE005A"]]["Check"]=True


    $ loadBG(2,"EV_MOE005A")



    "向大家举起手枪，将手指放在扳机上。"
    "……为何，手指却无法用力呢。"
    "拿着手枪的手不停地颤抖着。"
    "为什么。"
    "大家，已经不把我当做伙伴了啊。"
    "明明这里如果不这么做的话，就要被ＦＢ抛弃了。"
    "我又要回到，过去那种孤身一人的生活了。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0007"
    $ current_voice = "voice/MOE09A_MOE0007.ogg"
    "萌郁" "「我是，Ｍ４……！」"
    "我知道的。对于我来说ＦＢ以外的人没有意义。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0008"
    $ current_voice = "voice/MOE09A_MOE0008.ogg"
    "萌郁" "「我是……！」"
    "就算不知何时会被舍弃。就算如此。"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010006"
    $ current_voice = "voice/MOE09A_Y010006.ogg"
    "巡行者Ａ" "「怎么了？　你在干什么！」"
    "开枪吧，开枪吧。"
    "除了那么做已经没有别的选择了……"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0002"
    $ current_voice = "voice/MOE09A_CRS0002.ogg"
    "红莉栖" "「──萌郁」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0006"
    $ current_voice = "voice/MOE09A_OKA0006.ogg"
    "伦太郎" "「红莉栖，别过去！！」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0006"
    $ current_voice = "voice/MOE09A_MAY0006.ogg"
    "真由理" "「萌郁、我觉得呢……」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0007"
    $ current_voice = "voice/MOE09A_OKA0007.ogg"
    "伦太郎" "「真由理，也停下来啊！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0009"
    $ current_voice = "voice/MOE09A_MOE0009.ogg"
    "萌郁" "「已经无所谓了吧。我的事，怎么都好了」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0007"
    $ current_voice = "voice/MOE09A_MAY0007.ogg"
    "真由理" "「才不是那样呢！因为萌郁都在哭了呢。很难过吧！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0010"
    $ current_voice = "voice/MOE09A_MOE0010.ogg"
    "萌郁" "「诶？」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE002B"]]["Check"]=True


    $ loadBG(2,"EV_MOE002B")



    "一听她这么说我才发现。"
    "我……不知何时已经泪流满面。"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0003"
    $ current_voice = "voice/MOE09A_CRS0003.ogg"
    "红莉栖" "「萌郁，虽说这么突然，我搞不太清楚……但，那真的是你的意愿吗？」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0004"
    $ current_voice = "voice/MOE09A_CRS0004.ogg"
    "红莉栖" "「我并不相信你是真的想要杀死我们。」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0008"
    $ current_voice = "voice/MOE09A_MAY0008.ogg"
    "真由理" "「是的呢。真由喜是知道萌郁是一个温柔的人的哦。」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0011"
    $ current_voice = "voice/MOE09A_MOE0011.ogg"
    "萌郁" "「……！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE005A"]]["Check"]=True


    $ loadBG(2,"EV_MOE005A")



    "为什么这些人，还能对我说出这样温柔的话语？"
    "明明我是背叛者。"
    "明明是个无法违抗ＦＢ的懦夫。"
    "现在明明正要杀死大家。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0012"
    $ current_voice = "voice/MOE09A_MOE0012.ogg"
    "萌郁" "「我是……叛徒。」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0013"
    $ current_voice = "voice/MOE09A_MOE0013.ogg"
    "萌郁" "「从最初开始……就是以间谍的身份潜入这里的……」"
    "所以请厌恶我吧。"
    "那样的话我就能扣下扳机了。"
    "我就能变回Ｍ４了。"
    "但是，两人并不为所动。"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0005"
    $ current_voice = "voice/MOE09A_CRS0005.ogg"
    "红莉栖" "「萌郁真的是间谍吗？」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0006"
    $ current_voice = "voice/MOE09A_CRS0006.ogg"
    "红莉栖" "「难道成为我们的伙伴，也只是间谍行为？」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0007"
    $ current_voice = "voice/MOE09A_CRS0007.ogg"
    "红莉栖" "「一起欢笑，一起开女子会，还救了我……也都是间谍行为？」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0009"
    $ current_voice = "voice/MOE09A_MAY0009.ogg"
    "真由理" "「吃真由喜给的炸鸡块，也是工作的一部分？」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0010"
    $ current_voice = "voice/MOE09A_MAY0010.ogg"
    "真由理" "「那样的间谍，真由喜可是从来没有听说过哦」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0014"
    $ current_voice = "voice/MOE09A_MOE0014.ogg"
    "萌郁" "「那是……」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0008"
    $ current_voice = "voice/MOE09A_CRS0008.ogg"
    "红莉栖" "「请不要逃避。看着我们吧！」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0009"
    $ current_voice = "voice/MOE09A_CRS0009.ogg"
    "红莉栖" "「一起度过的时间，真的只是为了完成任务吗，试着想起来吧！」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0011"
    $ current_voice = "voice/MOE09A_MAY0011.ogg"
    "真由理" "「萌郁！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE002B"]]["Check"]=True


    $ loadBG(2,"EV_MOE002B")



    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0015"
    $ current_voice = "voice/MOE09A_MOE0015.ogg"
    "萌郁" "「……为什么」"
    "用颤抖的声音吐出了几个字。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0016"
    $ current_voice = "voice/MOE09A_MOE0016.ogg"
    "萌郁" "「为什么，要对我这么温柔呢」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0012"
    $ current_voice = "voice/MOE09A_MAY0012.ogg"
    "真由理" "「难道不是因为Ｌａｂｍｅｍ 吗！不是伙伴吗！不是朋友吗！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0017"
    $ current_voice = "voice/MOE09A_MOE0017.ogg"
    "萌郁" "「但是，我……」"
    window hide



    $ loadBG(2,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALA01"),"True","lh/CRS_ALA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    "突然，温暖的掌心触摸了我的脸颊。"
    "温柔的指尖，拭去了我的眼泪。"
    "即便胸口堵在枪口上，也接近了我的红莉栖笑了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALA06"),"True","lh/CRS_ALA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0010"
    $ current_voice = "voice/MOE09A_CRS0010.ogg"
    "红莉栖" "「早就说过了哦。如果，萌郁有什么困难，或者有什么痛苦的想法的话，我们一定鼎力相助」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0018"
    $ current_voice = "voice/MOE09A_MOE0018.ogg"
    "萌郁" "「……！！」"
    "果然……我无法伤害这样为我着想的人……"
    "杀死朋友什么的，我做不到。"
    "那么——应该做的是，只有一件。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0019"
    $ current_voice = "voice/MOE09A_MOE0019.ogg"
    "萌郁" "「抱歉……」"
    "虽然对我很温柔，抱歉了呐。"
    "永别了。"
    "——ＦＢ。"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010007"
    $ current_voice = "voice/MOE09A_Y010007.ogg"
    "巡行者Ａ" "「Ｍ４！　你在干什么！　快点开枪！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0020"
    $ current_voice = "voice/MOE09A_MOE0020.ogg"
    "萌郁" "「我……并不是Ｍ４。」"
    "我要守护大家。"
    "守护Ｌａｂｍｅｍ。"
    "守护伙伴。"
    "守护朋友。"
    "绝对要，守护大家。"
    "所以——"
    "不能开枪。"
    "不会开枪。"
    "我是……桐生萌郁！"
    $ stopvoc("Y01")
    play KUR "MOE09A_Y010008"
    $ current_voice = "voice/MOE09A_Y010008.ogg"
    "巡行者Ａ" "「……背叛了吗。那样的话」"
    "压制着阿万音的其中一人举起了手枪。"
    "枪口的正前方是——红莉栖和真由理。"
    window hide


    $ loadBG(2,"BG01N")



    show screen phoneSD1
    "看到那一幕的瞬间，我立刻扔掉了手枪，张开双手飞扑了出去。"
    hide screen phoneSD1
    window hide
    play se "SGSE061"



    $ loadBG(0,"BG_BLACK")

    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0021"
    $ current_voice = "voice/MOE09A_MOE0021.ogg"
    "萌郁" "「──！」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0011"
    $ current_voice = "voice/MOE09A_CRS0011.ogg"
    "红莉栖" "「萌郁！」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0013"
    $ current_voice = "voice/MOE09A_MAY0013.ogg"
    "真由理" "「不要啊啊啊啊！」"
    "啊啊，太好了。"
    "我，派上用场了。"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0004"
    $ current_voice = "voice/MOE09A_SUZ0004.ogg"
    "铃羽" "「哈！」"
    window hide

    $ loadBG(0,"EVX_S11A")


    $ loadBG(0,"BG_BLACK")

    "在模糊的视线的一角，阿万音挣脱了Ｒｏｕｎｄｅｒ的拘束。"
    "然后——"
    window hide
    play se "SGSE066"



    $ stopvoc("Y01")
    play KUR "MOE09A_Y010009"
    $ current_voice = "voice/MOE09A_Y010009.ogg"
    "巡行者Ａ" "「咕啊！」"
    window hide
    play se "SGSE064"



    $ stopvoc("Y02")
    play KUR "MOE09A_Y020001"
    $ current_voice = "voice/MOE09A_Y020001.ogg"
    "巡行者Ｂ" "「呜咕！」"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0005"
    $ current_voice = "voice/MOE09A_SUZ0005.ogg"
    "铃羽" "「太犹豫了呢。两个人就和一个人一样哦」"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0006"
    $ current_voice = "voice/MOE09A_SUZ0006.ogg"
    "铃羽" "「呔──」"
    "阿万音在另一个Ｒｏｕｎｄｅｒ举起手枪之前，就用我扔掉的手枪开了枪。"
    window hide
    play se "SGSE061"



    "一瞬间就击倒了那个袭击者。"
    window hide


    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0022"
    $ current_voice = "voice/MOE09A_MOE0022.ogg"
    "萌郁" "「……」"
    "身体里一阵麻木，然后是痛感。"
    "在地板上的血泊渐渐扩大，身体里的热量慢慢地流失着。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0023"
    $ current_voice = "voice/MOE09A_MOE0023.ogg"
    "萌郁" "「啊啊……」"
    "我很快就要死了吧——本能地察觉到了。"
    "但是不知为何。心情十分平静。"
    "这样满足的心情，出生以来是第一次。"
    "红莉栖和真由理都跑了过来。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE006A"]]["Check"]=True


    $ loadBG(2,"EV_MOE006A")



    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0012"
    $ current_voice = "voice/MOE09A_CRS0012.ogg"
    "红莉栖" "「萌郁，振作起来！」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0014"
    $ current_voice = "voice/MOE09A_MAY0014.ogg"
    "真由理" "「可不能就这么死了哦？呐，萌郁！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0024"
    $ current_voice = "voice/MOE09A_MOE0024.ogg"
    "萌郁" "「红莉栖。真由，理。」"
    "两个人露出了悲伤的表情。但是，她们都安然无恙。"
    "那真是太，令人高兴了。"
    "桥田君和阿万音，还有冈部君都聚集了过来。"
    $ stopvoc("DAR")
    play DAR "MOE09A_DAR0003"
    $ current_voice = "voice/MOE09A_DAR0003.ogg"
    "至" "「桐生氏……」"
    $ stopvoc("SUZ")
    play SUZ "MOE09A_SUZ0007"
    $ current_voice = "voice/MOE09A_SUZ0007.ogg"
    "铃羽" "「可恶……要是我能早点注意到袭击的话」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0008"
    $ current_voice = "voice/MOE09A_OKA0008.ogg"
    "伦太郎" "「为什么啊萌郁。这是为什么啊……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0025"
    $ current_voice = "voice/MOE09A_MOE0025.ogg"
    "萌郁" "「对不……起了……」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0013"
    $ current_voice = "voice/MOE09A_CRS0013.ogg"
    "红莉栖" "「不行，止不住血！真由理！」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0015"
    $ current_voice = "voice/MOE09A_MAY0015.ogg"
    "真由理" "「嗯！」"
    "将自己的手，放在按住伤口的两双手上。"
    "温暖的触感。两双手就像能让我哭泣般的，温暖。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0026"
    $ current_voice = "voice/MOE09A_MOE0026.ogg"
    "萌郁" "「没关系」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0014"
    $ current_voice = "voice/MOE09A_CRS0014.ogg"
    "红莉栖" "「才不好呢！不马上急救的话——」"
    "我又摇了摇头。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0027"
    $ current_voice = "voice/MOE09A_MOE0027.ogg"
    "萌郁" "「……没关系」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0028"
    $ current_voice = "voice/MOE09A_MOE0028.ogg"
    "萌郁" "「冈部君……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0029"
    $ current_voice = "voice/MOE09A_MOE0029.ogg"
    "萌郁" "「你的……ＩＢＮ５１００……应该，是被我回收了……」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0009"
    $ current_voice = "voice/MOE09A_OKA0009.ogg"
    "伦太郎" "「什么？是怎么一回事？」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0030"
    $ current_voice = "voice/MOE09A_MOE0030.ogg"
    "萌郁" "「通过Ｄｍａｉｌ，告诉组织……ＩＢＮ５１００在……柳林神社……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0031"
    $ current_voice = "voice/MOE09A_MOE0031.ogg"
    "萌郁" "「如果是别的……世界线的话……我一定……会这么做的……」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0010"
    $ current_voice = "voice/MOE09A_OKA0010.ogg"
    "伦太郎" "「原来如此……你的任务，是回收ＩＢＮ５１００吗」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0032"
    $ current_voice = "voice/MOE09A_MOE0032.ogg"
    "萌郁" "「所以……将Ｄｍａｉｌ发到四年前……将一切都……」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0011"
    $ current_voice = "voice/MOE09A_OKA0011.ogg"
    "伦太郎" "「啊啊……明白了」"
    "发送目标当然是。ＦＢ。"
    "在我成为ＦＢ之前的那一天，在那一天比我先发送邮件的话——我就不会成为Ｒｏｕｎｄｅｒ。"
    window hide


    $ loadBG(2,"PBG12A")






    $ loadBG(2,"PBG12B")






    $ loadBG(2,"PBG12C")



    hide screen phonebtn


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE006A"]]["Check"]=True
    hide screen phonebtn
    "我用出最后的力气，将手机交到了红莉栖和真由理那两双已经被血染红的手里。"
    "只有打完内容的力气了，连按下发信按钮的力量……也没有了。"
    "所以交给了那两双温暖的手里。那两双拯救了我的温暖的手里，把一切都委托给了她们。"
    "手机，曾经是我的世界。"
    "对于是Ｒｏｕｎｄｅｒ，是Ｍ４的我来说……和ＦＢ的联系是这个世界的全部。"
    "但是……"
    "成为Ｌａｂｍｅｍ的如今，已经不需要了。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0033"
    $ current_voice = "voice/MOE09A_MOE0033.ogg"
    "萌郁" "「将这个……发给过去的ＦＢ……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0034"
    $ current_voice = "voice/MOE09A_MOE0034.ogg"
    "萌郁" "「拜托了……改变……过去……改变……这样的我……」"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0016"
    $ current_voice = "voice/MOE09A_MAY0016.ogg"
    "真由理" "「萌郁！　萌郁！」"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0015"
    $ current_voice = "voice/MOE09A_CRS0015.ogg"
    "红莉栖" "「萌郁！　振作一点！」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0035"
    $ current_voice = "voice/MOE09A_MOE0035.ogg"
    "萌郁" "「能遇到你们……真是太好了……」"
    "朝着流泪的两人，冈部君点了点头。"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0012"
    $ current_voice = "voice/MOE09A_OKA0012.ogg"
    "伦太郎" "「不用担心了。下次醒来的时候，你就是Ｌａｂｍｅｍ了，不是间谍。只是Ｌａｂｍｅｍ，桐生萌郁。」"
    $ stopvoc("OKA")
    play OKA "MOE09A_OKA0013"
    $ current_voice = "voice/MOE09A_OKA0013.ogg"
    "伦太郎" "「所以现在，就安心地睡吧……安心地……」"
    "冈部君说着说着也有些泣不成声了。"
    "Ｌａｂ的众人都流着眼泪，叫着我的名字。"
    "啊啊。被如此的重视也是没想到。"
    "慢慢变冷的身体，切实地感受到了扩散开的喜悦。"
    window hide






    $ loadBG(0,"BG_BLACK")


    stop bgm 
    "变得沉重的眼皮，终于合上了。"
    "好困，我一定就会这样长眠下去吧。"
    "真的是很久，说不定再也醒不来了。"
    "但是，我相信我一定会再次醒来。"
    "一定会被同伴唤醒。"
    "我相信着。现在能够相信了。因为那些信任着我的人。"
    "所以现在，就这样睡下去吧。"
    "醒来之后，就会是和现在不一样，和平的世界，和大家一起欢笑的我，在等待着。"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0036"
    $ current_voice = "voice/MOE09A_MOE0036.ogg"
    "萌郁" "「谢谢……大家……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0037"
    $ current_voice = "voice/MOE09A_MOE0037.ogg"
    "萌郁" "「红莉栖……真由理……」"
    $ stopvoc("MOE")
    play MOE "MOE09A_MOE0038"
    $ current_voice = "voice/MOE09A_MOE0038.ogg"
    "萌郁" "「下次再和我……成为朋友的话，我会……很高兴哦……」"
    "意识逐渐远去——"
    "已经听不到大家的声音了——"
    "真的可以前往别的世界吗——"
    $ stopvoc("CRS")
    play CRS "MOE09A_CRS0016"
    $ current_voice = "voice/MOE09A_CRS0016.ogg"
    "？？？" "「萌郁，起来吧」"
    "咦……？"
    $ stopvoc("MAY")
    play MAY "MOE09A_MAY0017"
    $ current_voice = "voice/MOE09A_MAY0017.ogg"
    "？？？" "「睡懒觉可是不行的哦♪」"
    "听见了两个人的声音……"
    "为什么呢……"
    "啊啊，这样啊。"
    "一定是，到达了另一条世界线——"
    show screen invisible

    window hide




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    $ renpy.movie_cutscene("video/imv12.avi")
    hide screen invisible
    "「昏睡励起的量子·完成」"


    return
