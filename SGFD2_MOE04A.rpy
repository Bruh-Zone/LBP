label SGFD2_MOE04A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG34A")
    play se "SGSE200L" loop


    $ date="8/9"
    $ day = "MON"
    show screen phonebtn
    show screen phoneSD1

    "注意到的时候，天已经亮了。"
    "虽然是坐在地板上入睡的，但感觉还是睡得很好。"
    "昨天虽然自己好像没有注意到，但可能已经积累了相当的疲劳。"


    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0000"
    $ current_voice = "voice/MOE04A_MOE0000.ogg"
    "萌郁" "「啊……邮件」"

    "一直握在手中的手机短促地震动起来。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2


    "我急忙打开收件箱，确认邮件。"
    "是ＦＢ发过来的。"
    "每天早晨，收到ＦＢ发来邮件的话就会安心。"
    "果然我是为了这个人活着的。"
    window hide



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail










    "胸口稍稍有些疼痛。"
    "昨天夜里产生的那心结……依然还在胸口骚动。"
    "确实ＦＢ说是对的。"
    "只要是她说的，不会有错。"
    "但是呢……"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0001"
    $ current_voice = "voice/MOE04A_MOE0001.ogg"
    "萌郁" "「哈……」"
    "一不注意叹了口气。"
    "不能这样一直迷茫下去了。"
    window hide
    call hide_phone

    "不管怎样，先按照ＦＢ说的那样试着离间那些和时间机器有关的人员吧。"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG05A2",trans=fade)

    show screen phoneSD1
    "走到Ｌａｂ附近的时候──"
    hide screen phoneSD1
    window hide



    $ loadBG(2,"EVX_C06A")



    hide screen phonebtn
    play bgm "BGM23"

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0000"
    $ current_voice = "voice/MOE04A_CRS0000.ogg"
    "红莉栖" "「你啊，究竟为什么一直讨厌着我呢？」"

    $ targetmailid = gc["ScriptMacros"]["RM_MOE_RECV_MAY01_01"]

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0000"
    $ current_voice = "voice/MOE04A_SUZ0000.ogg"
    "铃羽" "「并没有什么。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0001"
    $ current_voice = "voice/MOE04A_CRS0001.ogg"
    "红莉栖" "「那，每次见面的时候一直都盯着我的理由是？」"
    call CHECK_RM_RECEIVE
    "牧濑和……大概、在显像管工房打工的阿万音小姐？"
    call CHECK_RM_RECEIVE
    "两个人面对面不知在争论着什么。"

    call CHECK_RM_RECEIVE
    window hide



    $ loadBG(2,"BG05A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB01"),"True","lh/SUZ_ASB01a~ipad.png") at left as lh5 zorder (10-5) :
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
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0002"
    $ current_voice = "voice/MOE04A_CRS0002.ogg"
    "红莉栖" "「没有理由就摆出那副态度很失礼诶」"
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0001"
    $ current_voice = "voice/MOE04A_SUZ0001.ogg"
    "铃羽" "「理由……也并非没有。」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0003"
    $ current_voice = "voice/MOE04A_CRS0003.ogg"
    "红莉栖" "「那样的话，就明明白白地说出来啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0002"
    $ current_voice = "voice/MOE04A_SUZ0002.ogg"
    "铃羽" "「……明白了。那样的话，就明明白白地告诉你吧。」"
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0003"
    $ current_voice = "voice/MOE04A_SUZ0003.ogg"
    "铃羽" "「牧濑红莉栖……你，知道ＳＥＲＮ吧？」"
    "ＳＥＲＮ……！？"
    "为什么她会提到ＳＥＲＮ……？"
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0004"
    $ current_voice = "voice/MOE04A_SUZ0004.ogg"
    "铃羽" "「说白了吧，我是在想你会不会是ＳＥＲＮ的间谍。」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0004"
    $ current_voice = "voice/MOE04A_CRS0004.ogg"
    "红莉栖" "「…………」"
    "牧濑是……ＳＥＲＮ的间谍？"
    "为什么会是这样？"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY01_01"])

    "从来没听说过那种事。"
    "从ＦＢ那里得到的个人情报里也只字未提这个。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我慌慌张张地向ＦＢ发送了邮件。"
    window hide
    call send_mail (id=[160,161,162,163])
    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_EDIT_TEN01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_SEND_TEN01"]






    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_RECV_TEN02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call hide_phone
    "立刻收到了回信。"
    call read_last_mail
    window hide


    "……果然，牧濑不是ＳＥＲＮ这边的。"
    "她如果真的是ＳＥＲＮ的间谍的话，ＦＢ事先应该会告诉我。"
    "那么，为什么阿万音小姐会怀疑牧濑是ＳＥＲＮ的间谍呢？"
    "……可以试着直接向本人确认一下吧。"
    window hide
    call hide_phone



    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0002"
    $ current_voice = "voice/MOE04A_MOE0002.ogg"
    "萌郁" "「那个……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA06"),"True","lh/CRS_ASA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0005"
    $ current_voice = "voice/MOE04A_CRS0005.ogg"
    "红莉栖" "「啊，是桐生小姐啊。早上好。」"
    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0006"
    $ current_voice = "voice/MOE04A_CRS0006.ogg"
    "红莉栖" "「难道说是在去 Ｌａｂ 的途中？那样的话一起──」"
    show screen phonebtn
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0003"
    $ current_voice = "voice/MOE04A_MOE0003.ogg"
    "萌郁" "「我有些想问的事情……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0007"
    $ current_voice = "voice/MOE04A_CRS0007.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0004"
    $ current_voice = "voice/MOE04A_MOE0004.ogg"
    "萌郁" "「刚才……你们在讨论的关于ＳＥＲＮ的话题……是真的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0008"
    $ current_voice = "voice/MOE04A_CRS0008.ogg"
    "红莉栖" "「Ｓ、ＳＥＲＮ的话题？」"

    $ targetmailid = cml.setdefault("RM_MOE_SEND_MAY01","")

    $ LR_RM_CHANCE=20
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0005"
    $ current_voice = "voice/MOE04A_MOE0005.ogg"
    "萌郁" "「嗯。牧濑是……ＳＥＲＮ的间谍什么的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0005"
    $ current_voice = "voice/MOE04A_SUZ0005.ogg"
    "铃羽" "「刚才听到了吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0006"
    $ current_voice = "voice/MOE04A_MOE0006.ogg"
    "萌郁" "「…………」"
    call CHECK_RM_RECEIVE
    "我轻轻地点了点头。"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0009"
    $ current_voice = "voice/MOE04A_CRS0009.ogg"
    "红莉栖" "「桐生小姐，连你都那么说吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0010"
    $ current_voice = "voice/MOE04A_CRS0010.ogg"
    "红莉栖" "「难道说，从冈部还是桥田那里听来的？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0007"
    $ current_voice = "voice/MOE04A_MOE0007.ogg"
    "萌郁" "「……？」"
    call CHECK_RM_RECEIVE
    "冈部君？桥田君？"
    call CHECK_RM_RECEIVE
    "为什么会出现这两个人的名字啊……"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0011"
    $ current_voice = "voice/MOE04A_CRS0011.ogg"
    "红莉栖" "「确实ＳＥＲＮ除了研究基本粒子以外，也在进行时间机器的研究。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0008"
    $ current_voice = "voice/MOE04A_MOE0008.ogg"
    "萌郁" "「……！？」"
    call CHECK_RM_RECEIVE
    "诶？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0006"
    $ current_voice = "voice/MOE04A_SUZ0006.ogg"
    "铃羽" "「牧濑红莉栖，你果然是……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0012"
    $ current_voice = "voice/MOE04A_CRS0012.ogg"
    "红莉栖" "「请不要误会了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0013"
    $ current_voice = "voice/MOE04A_CRS0013.ogg"
    "红莉栖" "「是桥田黑进ＳＥＲＮ的服务器得到的结果哦。他告诉了冈部，然后我当时也在场所以知道了。」"
    call CHECK_RM_RECEIVE
    "那样的事……"
    call CHECK_RM_RECEIVE
    "就算作为ＲＯＵＮＤＥＲ一员的我，也不知道那样的情报……"
    call CHECK_RM_RECEIVE
    "除了知道ＲＯＵＮＤＥＲ是ＳＥＲＮ的非正式下部机构以外一无所知。"
    call CHECK_RM_RECEIVE
    "ＳＥＲＮ竟然在……研究时间机器……"
    call CHECK_RM_RECEIVE
    "ＦＢ肯定知道这件事吧？"

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0014"
    $ current_voice = "voice/MOE04A_CRS0014.ogg"
    "红莉栖" "「从常识来考虑，我根本不可能是ＳＥＲＮ的什么间谍吧。欧洲也没有去过呢。」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0009"
    $ current_voice = "voice/MOE04A_MOE0009.ogg"
    "萌郁" "「……」"
    "……牧濑到底是不是ＳＥＲＮ的间谍怎样都好了。"
    "比起那个有更严重的问题。"
    "她——还有冈部君和桥田君，知道了ＳＥＲＮ的秘密。"
    "知道了连我都不知道的秘密……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0015"
    $ current_voice = "voice/MOE04A_CRS0015.ogg"
    "红莉栖" "「总而言之。我和ＳＥＲＮ没有任何关系，阿万音小姐也没有任何讨厌我的理由了吧。」"
    "就算牧濑那么说，看起来阿万音小姐还是没法接受。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB04"),"True","lh/SUZ_AMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0007"
    $ current_voice = "voice/MOE04A_SUZ0007.ogg"
    "铃羽" "「是叫桐生萌郁……吧？」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0010"
    $ current_voice = "voice/MOE04A_MOE0010.ogg"
    "萌郁" "「……诶诶」"
    $ stopvoc("SUZ")
    play SUZ "MOE04A_SUZ0008"
    $ current_voice = "voice/MOE04A_SUZ0008.ogg"
    "铃羽" "「不管牧濑红莉栖是不是ＳＥＲＮ的间谍，你还是对她留个心眼比较好」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE017"

    "留下了这样的话，她转身走进了显像管工房。"
    "……她也应该知道ＳＥＲＮ的秘密吧？"
    "虽然想要再追问下去，但还是换个场合继续吧。"
    "那现在去问问牧濑。"
    "必须得到更加详细的情报。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY02_01"])

    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0011"
    $ current_voice = "voice/MOE04A_MOE0011.ogg"
    "萌郁" "「牧濑……对于刚才的发言有何感想……？」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0016"
    $ current_voice = "voice/MOE04A_CRS0016.ogg"
    "红莉栖" "「你问我怎么想……不如说我还想问你呢。为什么阿万音小姐会怀疑我是ＳＥＲＮ的间谍呢。」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0012"
    $ current_voice = "voice/MOE04A_MOE0012.ogg"
    "萌郁" "「……」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    call send_mail (id=[165,166,167,168])


    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_EDIT_CRS01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE04A_SEND_CRS01"]










    play se "SGSE802"


    stop se


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0017"
    $ current_voice = "voice/MOE04A_CRS0017.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0018"
    $ current_voice = "voice/MOE04A_CRS0018.ogg"
    "红莉栖" "「等、等一下，你从哪里知道我父亲是中钵博士的？」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0013"
    $ current_voice = "voice/MOE04A_MOE0013.ogg"
    "萌郁" "「我，在杂志编ｐｒｏ打工所以……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0019"
    $ current_voice = "voice/MOE04A_CRS0019.ogg"
    "红莉栖" "「啊。啊啊……原来如此」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0020"
    $ current_voice = "voice/MOE04A_CRS0020.ogg"
    "红莉栖" "「阿万音小姐，应该也知道这一点……然后从父亲的时间机器相关研究和ＳＥＲＮ的研究联想到一块了吧。原来如此……这样一来就说的通了。」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0014"
    $ current_voice = "voice/MOE04A_MOE0014.ogg"
    "萌郁" "「……嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0021"
    $ current_voice = "voice/MOE04A_CRS0021.ogg"
    "红莉栖" "「确实，我的父亲是在进行时间机器的研究」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0022"
    $ current_voice = "voice/MOE04A_CRS0022.ogg"
    "红莉栖" "「但是，要是这样就说我和ＳＥＲＮ有关系的话……答案是ＮＯ」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0023"
    $ current_voice = "voice/MOE04A_CRS0023.ogg"
    "红莉栖" "「而且，我在 Ｌａｂ 进行时间机器的研究这件事，既和我父亲没有关系，也和ＳＥＲＮ无关。」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0024"
    $ current_voice = "voice/MOE04A_CRS0024.ogg"
    "红莉栖" "「只是单纯地为了满足自己的研究者之心罢了」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0015"
    $ current_voice = "voice/MOE04A_MOE0015.ogg"
    "萌郁" "「是……这样啊……」"
    "好像没有什么别的隐瞒着的事了。"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0025"
    $ current_voice = "voice/MOE04A_CRS0025.ogg"
    "红莉栖" "「但是呢……真的是那样的吗？」"
    "与其说是在对我说话，不如说牧濑是在自言自语。"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0016"
    $ current_voice = "voice/MOE04A_MOE0016.ogg"
    "萌郁" "「诶？」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0026"
    $ current_voice = "voice/MOE04A_CRS0026.ogg"
    "红莉栖" "「虽然说不是因为父亲才去进行时间机器的研究……」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0027"
    $ current_voice = "voice/MOE04A_CRS0027.ogg"
    "红莉栖" "「但说不定是为了得到他的承认才去做的。」"
    "像是自问自答。她似乎并没有期待着我的回复。"
    play bgm "FD2BGM08"
    "但是我却重重地点了点头。"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0017"
    $ current_voice = "voice/MOE04A_MOE0017.ogg"
    "萌郁" "「我也……很理解那样的心情。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑突然睁大了眼睛。"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0028"
    $ current_voice = "voice/MOE04A_CRS0028.ogg"
    "红莉栖" "「桐生小姐也？」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0018"
    $ current_voice = "voice/MOE04A_MOE0018.ogg"
    "萌郁" "「我也是……为了得到别人的承认……一直拼命努力着」"
    "说出了自己的心声，因此有些失语。"
    "这样说的话，好像就在表述我和ＦＢ之间的关系一样。"
    "说不定聪明的牧濑就会注意到呢。"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0019"
    $ current_voice = "voice/MOE04A_MOE0019.ogg"
    "萌郁" "「啊……」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0020"
    $ current_voice = "voice/MOE04A_MOE0020.ogg"
    "萌郁" "「那个……不是，没有特别深的含义啦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA06"),"True","lh/CRS_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0029"
    $ current_voice = "voice/MOE04A_CRS0029.ogg"
    "红莉栖" "「呼呼呼，桐生小姐。ＴＨＡＮＫＳ」"
    "不知为何有些高兴起来的牧濑露出了笑容。"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0021"
    $ current_voice = "voice/MOE04A_MOE0021.ogg"
    "萌郁" "「…………」"
    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0030"
    $ current_voice = "voice/MOE04A_CRS0030.ogg"
    "红莉栖" "「稍微有些开心呢。」"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0022"
    $ current_voice = "voice/MOE04A_MOE0022.ogg"
    "萌郁" "「……开心？为什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0031"
    $ current_voice = "voice/MOE04A_CRS0031.ogg"
    "红莉栖" "「最近发生了很多事情呢……为什么呢，听你说理解我的心情就变得高兴起来了」"
    stop bgm 
    "面对牧濑突然的注视，我没有多想就移开了视线。"
    $ stopvoc("MOE")
    play MOE "MOE04A_MOE0023"
    $ current_voice = "voice/MOE04A_MOE0023.ogg"
    "萌郁" "「……我，今天先回去了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE04A_CRS0032"
    $ current_voice = "voice/MOE04A_CRS0032.ogg"
    "红莉栖" "「诶？等等，桐生小姐！？」"
    hide screen phoneSD1
    window hide
    play se "SGSE182"



    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "我不知为何，就下意识地避开了那样的视线……"
    "就算回到了房间，牧濑的那个笑脸依然在脑海里徘徊不去……"

    hide screen phoneSD1
    window hide
    stop se
    stop se





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
