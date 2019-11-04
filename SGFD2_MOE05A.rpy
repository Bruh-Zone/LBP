label SGFD2_MOE05A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide



    $ loadBG(0,"EV_MOE001A")





    play bgm "BGM25"


    $ date="8/10"
    $ day = "TUE"
    hide screen phonebtn
    hide screen phoneSD1

    "不知何时，我已身处大楼屋顶。"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0000"
    $ current_voice = "voice/MOE05A_MOE0000.ogg"
    "萌郁" "「……！？」"
    window hide







    "因为惊讶而后退的时候，发现背后是铁栅栏。"
    "啊，这样啊。"
    "我越过了栅栏，站在屋顶边缘。"




    "对一切都感到厌恶。"
    "也不想继续在屋子里抱着膝盖了。"
    "反正就算我死了，谁也不会注意到，谁也不会感到难过的吧，不如就……"
    "我从口袋里取出手机。"
    "是为什么呢，感觉它突然吸引了我的注意力。"
    "然而。"
    "『未读邮件 没有』"
    "理所当然的事情。"
    "这几年，我的手机一封邮件也未曾收到过。"
    "那为何还要寄望于这样的东西呢？"
    "我歪了歪头，把手机扔了出去。"
    window hide


    $ loadBG(2,"BG_BLACK")




    "手机就这样坠入了下方遥远的街道，被吞没了。"
    "我也，马上就要变成那样了吧。"
    "逐渐变得稀薄而微弱，最终，粉身碎骨。"
    "那样也不错吧。比起成天躲在房间里，一定要好得多。"
    "就好像不小心绊了一跤似的，我从屋顶上一跃而下。"
    play se "SGSE347"
    "然而没想到的是，好像有什么温暖的东西拉住了我。"
    "连“咦？”这么想的时间都没有，就被拉回去了。"
    "我的双手，不知何时被谁握住了。"
    "握住我的手的人，完全不像是要松开的样子。"
    "为什么？为什么要阻止我？明明一切都已经结束了啊。"
    "拜托了，请让这一切结束吧。"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0000"
    $ current_voice = "voice/MOE05A_MAY0000.ogg"
    "？？？" "「萌郁来了，我真的非常开心呢」"
    "握住我右手的人如是道。"
    $ stopvoc("CRS")
    play CRS "MOE05A_CRS0000"
    $ current_voice = "voice/MOE05A_CRS0000.ogg"
    "？？？" "「萌郁、谢谢你」"
    "握住我左手的人继续说。"
    "那声音是如此的温柔。"
    "两人的双手是那样的温暖，以至于让我都想哭了。"
    "那样的温柔，那样的温暖，以至于我不知何时已潸然泪下。"
    "两人就那样一直握住像个孩子一样哭泣着的我的手。"
    "我像是依靠着她们不掉下去一样，也紧握着她们的双手，泣不成声地说道。"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0001"
    $ current_voice = "voice/MOE05A_MOE0001.ogg"
    "萌郁" "「……我，可以活下去吗？」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0002"
    $ current_voice = "voice/MOE05A_MOE0002.ogg"
    "萌郁" "「我……可以继续存在于此吗？」"
    window hide
    stop bgm 




    $ loadBG(0,"BG34A")

    hide screen phonebtn
    hide screen phoneSD1
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0003"
    $ current_voice = "voice/MOE05A_MOE0003.ogg"
    "萌郁" "「……！？」"
    play se "SGSE200L" loop
    "我突然坐了起来。"
    "好像……做了一个梦。"
    "但记不清那是怎样的梦了。"
    "感觉脸颊有些异样，我伸手摸了一下。"
    "——湿了。"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0004"
    $ current_voice = "voice/MOE05A_MOE0004.ogg"
    "萌郁" "「……？」"
    "好像做了一个让我几乎哭出来的梦。"
    "还是记不太清楚了。"
    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_RECV_OKA01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "！？"
    "放在一边的手机，突然提示有新邮件。"
    window hide
    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我连忙打开手机。"
    window hide


    "是ＦＢ和冈部君发来的邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_RECV_TEN01"]
    call read_last_mail (p=True)


    window hide


    "然后，冈部君发来的邮件是——"
    call read_last_mail (id=1, p=True)
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_RECV_OKA01"]




    "……我知道。"
    "我是Ｒｏｕｎｄｅｒ。Ｍ４。不是Ｌａｂｍｅｍ。"
    window hide


    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_RECV_TEN01"]




    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_EDIT_TEN01_00"]


    "于是我无视了冈部君的邮件，只回复了ＦＢ的邮件。"
    "ＦＢ是，这个世界上我唯一能够依赖的人。"
    "为了ＦＢ的话……我什么都可以做。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_SEND_TEN01"]
    call send_mail (id=[171,172,173])




    "但是，不知为何。"
    "我按不下发送按钮。使不出力气。"
    "胸口里仍然有那种奇怪的疙瘩。"
    "为什么呢……？"
    "深深地吸了一口气，我用双指终于按下了发送键。"
    window hide






    call hide_phone

    "收好手机，我站了起来。"
    "嗯，今天也非去 Ｌａｂ 不可。"
    "为了完成ＦＢ的命令。"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG01A")

    $ targetmailid = gc["ScriptMacros"]["RM_MOE_RECV_MAY03_01"]

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    python:
        RcvMail(174)
        ReadMail(174)


    play se "SGSE024"


    show screen phoneSD1
    play bgm "FD2BGM08"



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0000"
    $ current_voice = "voice/MOE05A_OKA0000.ogg"
    "伦太郎" "「哦，这不是指压师么？」"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0001"
    $ current_voice = "voice/MOE05A_MAY0001.ogg"
    "真由理" "「真是的冈伦，人家不是叫指压师是叫萌郁啦」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0005"
    $ current_voice = "voice/MOE05A_MOE0005.ogg"
    "萌郁" "「……」"
    "走进Ｌａｂ 的时候，里面只有冈部君和椎名二人。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0001"
    $ current_voice = "voice/MOE05A_OKA0001.ogg"
    "伦太郎" "「哇哈哈哈哈哈！　来得正好啊指压师！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0002"
    $ current_voice = "voice/MOE05A_OKA0002.ogg"
    "伦太郎" "「比说好的时间晚了三分钟，我还以为是你害怕得不敢来了呢！」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0006"
    $ current_voice = "voice/MOE05A_MOE0006.ogg"
    "萌郁" "「抱歉……迟到了」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0003"
    $ current_voice = "voice/MOE05A_OKA0003.ogg"
    "伦太郎" "「没关系哦，指压师。这一切都是命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择！」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0007"
    $ current_voice = "voice/MOE05A_MOE0007.ogg"
    "萌郁" "「……抱歉了。」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOCPE"])
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0004"
    $ current_voice = "voice/MOE05A_OKA0004.ogg"
    "伦太郎" "「呼……呼哈……哈。……那个、你喝{color=#f00}Ｄｒ．ｐｅｐｐｅｒ{/color}吗？」"


    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0008"
    $ current_voice = "voice/MOE05A_MOE0008.ogg"
    "萌郁" "「……可以。」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0005"
    $ current_voice = "voice/MOE05A_OKA0005.ogg"
    "伦太郎" "「这、这样啊。明白了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0002"
    $ current_voice = "voice/MOE05A_MAY0002.ogg"
    "真由理" "「冈伦，太紧张了哟～」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0006"
    $ current_voice = "voice/MOE05A_OKA0006.ogg"
    "伦太郎" "「这、这样啊。明白了。」"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0003"
    $ current_voice = "voice/MOE05A_MAY0003.ogg"
    "真由理" "「都开始重复自己的话了」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0009"
    $ current_voice = "voice/MOE05A_MOE0009.ogg"
    "萌郁" "「……想问我的事情……是什么？」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0007"
    $ current_voice = "voice/MOE05A_OKA0007.ogg"
    "伦太郎" "「嗯？　啊啊……嘛，那个啥。那个……总而言之，先坐下来吧」"
    "怎么了？今天的冈部君有些吞吞吐吐的。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    $ loadBG(2,"BG02A1")



    "我一边警戒着，一边坐到了沙发上。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0004"
    $ current_voice = "voice/MOE05A_MAY0004.ogg"
    "真由理" "「抱歉呢萌郁。虽然冈伦看起来很紧张，但并不是什么大事所以请你放心吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0008"
    $ current_voice = "voice/MOE05A_OKA0008.ogg"
    "伦太郎" "「你在说什么哦，真由理！」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0009"
    $ current_voice = "voice/MOE05A_OKA0009.ogg"
    "伦太郎" "「我现在要说的话可以说是关系到与机关的最终决战……不如说，就算说是能够左右世界命运的内容也不为过」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0010"
    $ current_voice = "voice/MOE05A_MOE0010.ogg"
    "萌郁" "「……」"
    "能够改变世界？"
    stop bgm 
    "……难道说，我是间谍的这件事暴露了！？"
    "真的吗……那样的事情，不可能的吧……"
    "平时在尾行的时候已经很小心了，情报的处理也很完美。"
    "但是……Ｌａｂｍｅｍ，都是些我看不透的人。"
    "在不知不觉中，我被套了情报，真实身份也说不定暴露了……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC03"),"True","lh/MAY_CSC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0005"
    $ current_voice = "voice/MOE05A_MAY0005.ogg"
    "真由理" "「喂喂，冈伦！」"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0006"
    $ current_voice = "voice/MOE05A_MAY0006.ogg"
    "真由理" "「冈伦是Ｌａｂ的首领吧？那样的话就好好地说清楚哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0010"
    $ current_voice = "voice/MOE05A_OKA0010.ogg"
    "伦太郎" "「那、那种事情我当然知道了！　好了，好好看着哦」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0011"
    $ current_voice = "voice/MOE05A_OKA0011.ogg"
    "伦太郎" "「咳咳……」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0012"
    $ current_voice = "voice/MOE05A_OKA0012.ogg"
    "伦太郎" "「是这样的哦……指压师哦」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0011"
    $ current_voice = "voice/MOE05A_MOE0011.ogg"
    "萌郁" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0013"
    $ current_voice = "voice/MOE05A_OKA0013.ogg"
    "伦太郎" "「昨天，你和红莉栖发生了什么吗？」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0012"
    $ current_voice = "voice/MOE05A_MOE0012.ogg"
    "萌郁" "「……诶？」"
    play bgm "FD2BGM08"
    "从刚才一直绷紧的神经，一下子松了下来。"
    "不仅是我没想到的话题，更是没想到是冈部说出来的。"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0014"
    $ current_voice = "voice/MOE05A_OKA0014.ogg"
    "伦太郎" "「事实上呢。昨天，到Ｌａｂ的时候红莉栖不知为何有些闷闷不乐的，所以就稍微问了一下发生了什么……」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0015"
    $ current_voice = "voice/MOE05A_OKA0015.ogg"
    "伦太郎" "「红莉栖说，昨天指压师话说了一半就突然跑走了，感觉是自己说了什么让她生气的话？　所以有些担心。」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0013"
    $ current_voice = "voice/MOE05A_MOE0013.ogg"
    "萌郁" "「…………」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    call send_mail (id=[175,176,177,178,179,180,181])











    $ targetmailid = gc["ScriptMacros"]["FM_MOE05A_SEND_OKA01"]






    call hide_phone




    play se "SGSE801"


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA04"),"True","lh/OKA_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0016"
    $ current_voice = "voice/MOE05A_OKA0016.ogg"
    "伦太郎" "「明明就在眼前，为啥要发邮件……」"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0007"
    $ current_voice = "voice/MOE05A_MAY0007.ogg"
    "真由理" "「萌郁，面对面讲话的话她会有些不好意思哟。和冈伦一样呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0017"
    $ current_voice = "voice/MOE05A_OKA0017.ogg"
    "伦太郎" "「我刚才明明不是不好意思好吧！」"

    stop se

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0018"
    $ current_voice = "voice/MOE05A_OKA0018.ogg"
    "伦太郎" "「这样……唔，原来如此，是这么回事啊。」"
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0019"
    $ current_voice = "voice/MOE05A_OKA0019.ogg"
    "伦太郎" "「那样的话就说出来啊。那家伙肯定也会安心的吧。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0020"
    $ current_voice = "voice/MOE05A_OKA0020.ogg"
    "伦太郎" "「但是，助手你的心胸还真是狭隘啊！稍微学习学习我这样一个人独自对抗机关的人的豪胆吧。唔哈哈哈哈哈」"

    "……其实，那个时候为什么逃开了呢，我自己也并不是很清楚。"

    $ targetmailid = gc["ScriptMacros"]["RM_MOE_RECV_CRS01_01"]

    $ LR_RM_CHANCE=9
    call CHECK_RM_RECEIVE
    "说到底，那个时候的心情到现在依然没有整理。昨天，回到房间以后，心中一直有个无法解开的心结。"
    call CHECK_RM_RECEIVE
    "为什么。我为什么会对自己欺骗Ｌａｂ的大家而感到有所不快呢？"
    call CHECK_RM_RECEIVE
    "说真的……我有些想和谁谈谈。"
    call CHECK_RM_RECEIVE
    "但是……和Ｌａｂ的众人谈这事，以我的立场来说是不可能的。就算只是说Ｒｏｕｎｄｅｒ什么的，也不可能完全说清楚。如果全盘托出，那就意味着背叛了ＦＢ啊。"
    call CHECK_RM_RECEIVE
    "但是就算如此，也没法和ＦＢ说啊。"
    call CHECK_RM_RECEIVE
    "啊啊……这样啊。"
    call CHECK_RM_RECEIVE
    "现在我又是，只身一人了啊。"
    call CHECK_RM_RECEIVE
    "无法和任何人吐露心声……孤独的存在。"
    call CHECK_RM_RECEIVE
    "到现在为止都是ＦＢ帮我解决的。有什么问题的话我就回去寻求她的帮助。"

    call CHECK_RM_RECEIVE
    "但是，现在不能这样做……因此能称得上是我的伙伴的人并不存在。"
    "我又是……只身一人了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0021"
    $ current_voice = "voice/MOE05A_OKA0021.ogg"
    "伦太郎" "「怎么了指压师？　喂，没问题吧？」"
    stop bgm 

    "回过神来的时候，冈部君和椎名用担心的神情看着我。"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0014"
    $ current_voice = "voice/MOE05A_MOE0014.ogg"
    "萌郁" "「……抱歉了呐……稍微发了会儿呆……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC03"),"True","lh/MAY_CMC03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0008"
    $ current_voice = "voice/MOE05A_MAY0008.ogg"
    "真由理" "「……呐呐，萌郁」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0015"
    $ current_voice = "voice/MOE05A_MOE0015.ogg"
    "萌郁" "「诶……？」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_CRS01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_CRS01_01"])

    "突然，椎名握住了我的手，直直地注视着我。"
    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0009"
    $ current_voice = "voice/MOE05A_MAY0009.ogg"
    "真由理" "「呐，真由喜经常看到萌郁露出在苦恼着什么的表情。」"

    $ targetmailid = cml.setdefault("RM_MOE_SEND_CRS01","")

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0022"
    $ current_voice = "voice/MOE05A_OKA0022.ogg"
    "伦太郎" "「呼，不成熟的指压师哦。心神不定在紧要关头可是会掉链子的哦。这是常年与机关周旋的我的经验教训。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "MOE05A_OKA0023"
    $ current_voice = "voice/MOE05A_OKA0023.ogg"
    "伦太郎" "「在陷入无可挽回的境地之前，把心里话都说出来会比较好！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    "瞥了一眼仰天大笑的冈部君，椎名露出了抱歉的笑容。"
    call CHECK_RM_RECEIVE
    "但是，我却无法告诉任何人，请不要再用这样温柔的笑容，温柔的话语对待我了，这一想法。"
    call CHECK_RM_RECEIVE
    "我只身一人。"
    call CHECK_RM_RECEIVE
    "只能只身一人存在于世。"

    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0016"
    $ current_voice = "voice/MOE05A_MOE0016.ogg"
    "萌郁" "「没关系……」"
    play bgm "FD2BGM05"
    "是啊。这样就好了。"
    "明明这样就好了……为什么心情会如此烦躁呢？"
    "心中仍然涌动着那种躁动。"
    "好难受。为什么，会这么难受呢？"
    "难道我……想把一切都告诉椎名？"
    "就算这么做意味着对ＦＢ的背叛？"
    "难以理解……不知为何，最近自己总是很难理解自己的念头呢。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE05A_MAY0010"
    $ current_voice = "voice/MOE05A_MAY0010.ogg"
    "真由理" "「这样啊——真由喜看来弄错了呢。抱歉啊」"
    $ stopvoc("MOE")
    play MOE "MOE05A_MOE0017"
    $ current_voice = "voice/MOE05A_MOE0017.ogg"
    "萌郁" "「是的……弄错了。没关系。没有在……烦恼着什么。」"
    "椎名的笑容，和刚才相比，多了几分寂寞。"
    "胸口仿佛被针扎了一样疼。"
    "为什么，心情会变成这样？"
    "我明明已经有ＦＢ了。"
    "只要ＦＢ在就好了啊。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_CRS02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_CRS02_01"])

    "为什么……我会变成这样？"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return










    return
