label SGFD2_MOE07A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG01A")
    python:
        RcvMail(199)
        ReplyMail(199)
        SndMail(200)
        RcvMail(201)
        ReplyMail(201)
        SndMail(202)
        RcvMail(203)
        ReplyMail(203)
        SndMail(204)
        RcvMail(205)
        ReplyMail(205)
        SndMail(206)
        RcvMail(207)
        ReplyMail(207)
        SndMail(208)
        RcvMail(209)
        ReplyMail(209)
        SndMail(210)
        RcvMail(211)
        ReplyMail(211)
        SndMail(212)


    $ targetmailid = cml.setdefault("RM_MOE_SEND_MAY04","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    play bgm "FD2BGM11"

    $ date="8/12"
    $ day="THU"
    show screen phonebtn
    show screen phoneSD1

    "今天的Ｌａｂ，从早上开始就很繁忙。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VERDANDI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VERDANDI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_VERDANDI"])
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0000"
    $ current_voice = "voice/MOE07A_OKA0000.ogg"
    "伦太郎" "「那么现在……{color=#f00}『掌管现在的女神』作战( Ｏｐｅｒａｔｉｏｎ　Ｖｅｒｔｈａｎｄｉ){/color}开始！」"
    hide screen phoneSD1
    window hide



    $ loadBG(2,"EVX_M02C")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0001"
    $ current_voice = "voice/MOE07A_OKA0001.ogg"
    "伦太郎" "「虽然这么说……打工战士和菲利斯，还有琉华子还没到吗？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0000"
    $ current_voice = "voice/MOE07A_MAY0000.ogg"
    "真由理" "「冈伦，菲利斯今天也要打工哦～」"
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0000"
    $ current_voice = "voice/MOE07A_DAR0000.ogg"
    "至" "「阿万音氏刚才在楼下遇到的时候也在打工哦」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0000"
    $ current_voice = "voice/MOE07A_CRS0000.ogg"
    "红莉栖" "「漆原那边也是要给神社帮忙，已经联络过了。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0002"
    $ current_voice = "voice/MOE07A_OKA0002.ogg"
    "伦太郎" "「怎么这样？咕……说这是巧合也太难以置信了。这难道也是机关从中作梗的结果吗？」"
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0001"
    $ current_voice = "voice/MOE07A_DAR0001.ogg"
    "至" "「我倒是觉得只是冈伦太闲了。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0003"
    $ current_voice = "voice/MOE07A_OKA0003.ogg"
    "伦太郎" "「桶子，注意你说的话！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KTKR"])
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0002"
    $ current_voice = "voice/MOE07A_DAR0002.ogg"
    "至" "「呜哇，强词夺理{color=#f00}ｋｔｋｒ{/color}！」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0004"
    $ current_voice = "voice/MOE07A_OKA0004.ogg"
    "伦太郎" "「嘛，来不了的人也没办法了。在这里的成员一起进行作战吧。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0005"
    $ current_voice = "voice/MOE07A_OKA0005.ogg"
    "伦太郎" "「大家，都准备好了么？」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB07"),"True","lh/CRS_BSB07a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0001"
    $ current_voice = "voice/MOE07A_CRS0001.ogg"
    "红莉栖" "「做准备之前，请先检讨一下你那没品的命名方式。」"
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0003"
    $ current_voice = "voice/MOE07A_DAR0003.ogg"
    "至" "「牧濑氏……虽然我很清楚你想说些什么，但要想让现在的冈伦听进去纯粹是浪费时间啦。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "昨天的圆桌会议的结果是，将时间机器的研究进行到下个阶段。得出了这样的结论。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY02_02"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY02_02"])

    "明明必须按照ＦＢ的指示阻止那样的展开……我却连帮助他们进行研究这样的约定都说好了。"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0006"
    $ current_voice = "voice/MOE07A_OKA0006.ogg"
    "伦太郎" "「嗯？怎么了指压师。脸色很难看哦？」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0000"
    $ current_voice = "voice/MOE07A_MOE0000.ogg"
    "萌郁" "「……诶？」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0007"
    $ current_voice = "voice/MOE07A_OKA0007.ogg"
    "伦太郎" "「有好好睡觉吗？」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0001"
    $ current_voice = "voice/MOE07A_MOE0001.ogg"
    "萌郁" "「并没有……睡得太好。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0008"
    $ current_voice = "voice/MOE07A_OKA0008.ogg"
    "伦太郎" "「原来如此。哼，在能够左右世界命运的大战之前，紧张得都睡不着觉了么。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0009"
    $ current_voice = "voice/MOE07A_OKA0009.ogg"
    "伦太郎" "「这种事我也经常有。嘛，我倒不是紧张，而是因为明天世界是否又可以改变一点而感到高兴。」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0002"
    $ current_voice = "voice/MOE07A_CRS0002.ogg"
    "红莉栖" "「别拉着萌郁和你一起犯厨二病」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0010"
    $ current_voice = "voice/MOE07A_OKA0010.ogg"
    "伦太郎" "「但是，这个重要的作战是必须结集这个Ｌａｂ所有成员的力量才能成功的，缺少一个都不行」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0011"
    $ current_voice = "voice/MOE07A_OKA0011.ogg"
    "伦太郎" "「指压师哦，健康管理可不要松懈了」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0002"
    $ current_voice = "voice/MOE07A_MOE0002.ogg"
    "萌郁" "「……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 

    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_CRS08"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "收到了一封邮件。"

    "但是，身体却突然变得僵硬起来。"

    "也许是从ＦＢ那里来的邮件……"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    call read_last_mail (p=True)






    "不是啊……"
    "松了一口气。"
    play bgm "FD2BGM01"
    window hide


    "是呢，昨天，因为交到了朋友而太过于兴奋，很晚的时候给别人发了邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_CRS03"]


    "在那个点给ＦＢ以外的人写邮件，还是头一回。"
    "昨天的邮件里，红莉栖说希望我能叫她的名字。"
    "所以从今天开始，不再叫她牧濑了，要叫“红莉栖”。"
    "虽然有些不好意思，但这么叫超有朋友的感觉……很高兴。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_CRS08"]




    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_EDIT_CRS08_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_CRS08"]







    call send_mail (id=[214,215,216,217,218])

    "我给红莉栖发了邮件，几秒钟后她打开了手机。"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA06"),"True","lh/CRS_BMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "然后，她看着我温柔地笑了。"
    "啊啊，有朋友真好啊。"
    hide screen phoneSD1
    window hide



    $ loadBG(2,"EVX_M02D")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0012"
    $ current_voice = "voice/MOE07A_OKA0012.ogg"
    "伦太郎" "「那么，话说回来。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0013"
    $ current_voice = "voice/MOE07A_OKA0013.ogg"
    "伦太郎" "「现在对于本次的『掌管现在的女神』作战(Ｏｐｅｒａｔｉｏｎ　Ｖｅｒｔｈａｎｄｉ)的概要进行说明」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0014"
    $ current_voice = "voice/MOE07A_OKA0014.ogg"
    "伦太郎" "「本次作战的最终目标是——完成时间机器。」"
    "由目前的电话微波炉改良而成的时间机器似乎可以把自己的意识传送到过去的身体里。"
    "虽然这么说，但是自己并不会失去现在的记忆。冈部君是这么说明的。"
    "好像使用了以前红莉栖在美国研究的ＶＲ技术。"
    "我虽然不能很好地理解谈话的内容，但是感觉如果时间跳跃机真的能够实现的话……真心觉得非常厉害。"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0015"
    $ current_voice = "voice/MOE07A_OKA0015.ogg"
    "伦太郎" "「也就是说，本次作战是本Ｌａｂ自建立以来最大规模的作战。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0016"
    $ current_voice = "voice/MOE07A_OKA0016.ogg"
    "伦太郎" "「所以才需要Ｌａｂ全员齐心协力──」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0001"
    $ current_voice = "voice/MOE07A_MAY0001.ogg"
    "真由理" "「呐呐冈伦」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0017"
    $ current_voice = "voice/MOE07A_OKA0017.ogg"
    "伦太郎" "「嗯？怎么了吗真由理？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0002"
    $ current_voice = "voice/MOE07A_MAY0002.ogg"
    "真由理" "「那个，有什么真由喜可以帮到忙的地方吗？」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0018"
    $ current_voice = "voice/MOE07A_OKA0018.ogg"
    "伦太郎" "「唔……真由理对于未来道具的开发这么积极很少见啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC03"),"True","lh/MAY_CSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0003"
    $ current_voice = "voice/MOE07A_MAY0003.ogg"
    "真由理" "「嗯。真由理也是Ｌａｂｍｅｍ的一员嘛。」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0004"
    $ current_voice = "voice/MOE07A_MAY0004.ogg"
    "真由理" "「所以说，也想帮上大家的忙嘛——」"

    "是啊。Ｌａｂｍｅｍ并不是因为利害关系而在一起。"
    "我觉得真由理一定是因为真心想帮上忙。"
    "这样说的话我也应该——"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[219,220,221,222,223])












    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_OKA01"]










    play se "SGSE801"


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0019"
    $ current_voice = "voice/MOE07A_OKA0019.ogg"
    "伦太郎" "「嗯？　……什、什么！？」"


    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0020"
    $ current_voice = "voice/MOE07A_OKA0020.ogg"
    "伦太郎" "「指压师你说也想要帮忙……是吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0021"
    $ current_voice = "voice/MOE07A_OKA0021.ogg"
    "伦太郎" "「没想到……没想到连指压师都对于未来道具的研究都如此地充满干劲……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0022"
    $ current_voice = "voice/MOE07A_OKA0022.ogg"
    "伦太郎" "「我好感动啊！ 你们两位也终于注意到我们的研究是多么的伟大了吗！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0023"
    $ current_voice = "voice/MOE07A_OKA0023.ogg"
    "伦太郎" "「那好，这样的话我就把最重要最关键的任务交给你们！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0005"
    $ current_voice = "voice/MOE07A_MAY0005.ogg"
    "真由理" "「最重要最关键？」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0003"
    $ current_voice = "voice/MOE07A_MOE0003.ogg"
    "萌郁" "「……任务？」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0024"
    $ current_voice = "voice/MOE07A_OKA0024.ogg"
    "伦太郎" "「啊啊。不允许失败的艰难任务……能行吗？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0006"
    $ current_voice = "voice/MOE07A_MAY0006.ogg"
    "真由理" "「是怎样的任务？」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0025"
    $ current_voice = "voice/MOE07A_OKA0025.ogg"
    "伦太郎" "「真由理，还有指压师。你们两个人──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0026"
    $ current_voice = "voice/MOE07A_OKA0026.ogg"
    "伦太郎" "「去帮我把时间机器需要的零件买回来！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0007"
    $ current_voice = "voice/MOE07A_MAY0007.ogg"
    "真由理" "「诶诶？让真由喜去买时间机器的零件？」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0027"
    $ current_voice = "voice/MOE07A_OKA0027.ogg"
    "伦太郎" "「啊啊，是的。」"
    "冈部君重重地点了点头……"
    "说实话，我对于这个任务的内容……有些不自信。"
    window hide



    $ loadBG(2,"BG02A2")

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0004"
    $ current_voice = "voice/MOE07A_DAR0004.ogg"
    "至" "「冈伦，我和你直说吧，你是怎么想才会选择她们的……」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0028"
    $ current_voice = "voice/MOE07A_OKA0028.ogg"
    "伦太郎" "「唔？有什么问题吗？」"
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0005"
    $ current_voice = "voice/MOE07A_DAR0005.ogg"
    "至" "「就是说啊，就算只是去采购，ＰＣ改造要用到的零件的名称和规格呀都很复杂哟」"
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0006"
    $ current_voice = "voice/MOE07A_DAR0006.ogg"
    "至" "「然后还有，真由氏和桐生氏要在魔窟那样的秋叶原里找到那种细小的零件怎么想都很困难不是吗。」"
    "确实，我没有能够把零件准确地买回来的自信。"
    "恐怕，真由理也不擅长这方面。"
    "让这样的我们去买零件，说真的我挺不安的。"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0029"
    $ current_voice = "voice/MOE07A_OKA0029.ogg"
    "伦太郎" "「那样的话，桶子你也跟着去。那样的话就没问题了吧。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0007"
    $ current_voice = "voice/MOE07A_DAR0007.ogg"
    "至" "「哦哦，这是什么后宫型约会……但是，我拒绝。我稍后要去赴一个对我来说非常重要的人的约。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0030"
    $ current_voice = "voice/MOE07A_OKA0030.ogg"
    "伦太郎" "「一个对我来说非常重要的人的约！？难道说……是女人嘛！？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_REAJU"])
    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0008"
    $ current_voice = "voice/MOE07A_DAR0008.ogg"
    "至" "「诶呀，虽然不能那么说啦……是和女孩子见面，某种程度上来说我是{color=#f00}现充{/color}也不为过啦。诶嘿。」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0031"
    $ current_voice = "voice/MOE07A_OKA0031.ogg"
    "伦太郎" "「咕唔唔，你这家伙！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0032"
    $ current_voice = "voice/MOE07A_OKA0032.ogg"
    "伦太郎" "「不，就算退一百步来说允许你这家伙当现充吧。但，比起世纪性的大研究你居然选择去和女人赴约……」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0033"
    $ current_voice = "voice/MOE07A_OKA0033.ogg"
    "伦太郎" "「你还算超级嗨客么！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE07A_DAR0009"
    $ current_voice = "voice/MOE07A_DAR0009.ogg"
    "至" "「诶哟。那差不多我必须得走了。先告辞了。」"
    window hide
    hide lh6  with dissolve




    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0008"
    $ current_voice = "voice/MOE07A_MAY0008.ogg"
    "真由理" "「桶子君，再见哦♪」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0003"
    $ current_voice = "voice/MOE07A_CRS0003.ogg"
    "红莉栖" "「嘛，肯定是他的二次元老婆之类的吧？再怎么样，他也没法钻到显示器里面去吧。」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0004"
    $ current_voice = "voice/MOE07A_MOE0004.ogg"
    "萌郁" "「……」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[224,225,226,227])











    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_DAR01"]







    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0034"
    $ current_voice = "voice/MOE07A_OKA0034.ogg"
    "伦太郎" "「桶子这个叛徒！！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE024"




    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD02"),"True","lh/OKA_ASD02a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0035"
    $ current_voice = "voice/MOE07A_OKA0035.ogg"
    "伦太郎" "「可恶……难道桶子真的化身现充了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0009"
    $ current_voice = "voice/MOE07A_MAY0009.ogg"
    "真由理" "「因为呢，没办法的呀——」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0010"
    $ current_voice = "voice/MOE07A_MAY0010.ogg"
    "真由理" "「桶子君呢，几个月之前就和菲利斯约好了哟」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0036"
    $ current_voice = "voice/MOE07A_OKA0036.ogg"
    "伦太郎" "「是和菲利斯约好的么？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0011"
    $ current_voice = "voice/MOE07A_MAY0011.ogg"
    "真由理" "「嗯♪　今天呢，是明天要在ＭａｙＱｕｅｅｎ＋Ｎｙａ²召开的菲利斯杯的前夜祭哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB01"),"True","lh/CRS_BSB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0004"
    $ current_voice = "voice/MOE07A_CRS0004.ogg"
    "红莉栖" "「菲利斯杯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET_AB"])
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0012"
    $ current_voice = "voice/MOE07A_MAY0012.ogg"
    "真由理" "「由菲利斯酱举办的{color=#f00}雷ＮＥＴＡＢ{/color}这种卡牌游戏的非正式大赛哦♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0037"
    $ current_voice = "voice/MOE07A_OKA0037.ogg"
    "伦太郎" "「那家伙……」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0038"
    $ current_voice = "voice/MOE07A_OKA0038.ogg"
    "伦太郎" "「不把话说清楚还把自己升格为现充……不愧是我Ｌａｂ得意的超级嗨客啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB07"),"True","lh/CRS_BSB07a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0005"
    $ current_voice = "voice/MOE07A_CRS0005.ogg"
    "红莉栖" "「现充和黑客的技术没有关系吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0006"
    $ current_voice = "voice/MOE07A_CRS0006.ogg"
    "红莉栖" "「嘛，桥田的事先放一边」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0007"
    $ current_voice = "voice/MOE07A_CRS0007.ogg"
    "红莉栖" "「要去买东西的话，我可以一起去哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0039"
    $ current_voice = "voice/MOE07A_OKA0039.ogg"
    "伦太郎" "「我倒是没想过让Ｃｈｒｉｓｔｉｎａ代替桶子去采购呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA02"),"True","lh/CRS_BSA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0008"
    $ current_voice = "voice/MOE07A_CRS0008.ogg"
    "红莉栖" "「既有便签，要去的地方我大概也知道的所以没关系的」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0040"
    $ current_voice = "voice/MOE07A_OKA0040.ogg"
    "伦太郎" "「这样啊……那就这么定了，交给你了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA06"),"True","lh/CRS_BSA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0013"
    $ current_voice = "voice/MOE07A_MAY0013.ogg"
    "真由理" "「哇♪　那就这样，我和红莉栖酱还有萌郁出发了哦」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0005"
    $ current_voice = "voice/MOE07A_MOE0005.ogg"
    "萌郁" "「因为我们靠不住所以才麻烦你……抱歉……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0009"
    $ current_voice = "voice/MOE07A_CRS0009.ogg"
    "红莉栖" "「在说什么呢，没关系的不用在意」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0010"
    $ current_voice = "voice/MOE07A_CRS0010.ogg"
    "红莉栖" "「这个昨天就说过了吧？这点事是理所当然的咯」"
    "是哦……红莉栖和真由理都已经把我当做朋友了。"
    "是朋友的话，做这些也是理所当然的什么的……"
    "怎么说呢……稍微有些高兴。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0041"
    $ current_voice = "voice/MOE07A_OKA0041.ogg"
    "伦太郎" "「等一下，发生了什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0042"
    $ current_voice = "voice/MOE07A_OKA0042.ogg"
    "伦太郎" "「三个人之间的氛围，和之前有明显的区别。……哈，难道说！」"


    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0043"
    $ current_voice = "voice/MOE07A_OKA0043.ogg"
    "伦太郎" "「被“机关”洗脑了！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC06"),"True","lh/CRS_BSC06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0011"
    $ current_voice = "voice/MOE07A_CRS0011.ogg"
    "红莉栖" "「哈……为什么各种方面都那么迟钝啊，你」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0044"
    $ current_voice = "voice/MOE07A_OKA0044.ogg"
    "伦太郎" "「什，什么呀？」"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0012"
    $ current_voice = "voice/MOE07A_CRS0012.ogg"
    "红莉栖" "「没什么。那么，我们出发了，等会儿就拜托了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0045"
    $ current_voice = "voice/MOE07A_OKA0045.ogg"
    "伦太郎" "「喂，就这么无视我的问题啊！？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0014"
    $ current_voice = "voice/MOE07A_MAY0014.ogg"
    "真由理" "「我出发咯♪」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0006"
    $ current_voice = "voice/MOE07A_MOE0006.ogg"
    "萌郁" "「……冈部君……再见了呐」"
    hide screen phoneSD1
    window hide
    stop bgm 



    $ loadBG(0,"BG17A")

    play bgm "BGM18"





    $ loadBG(2,"BG16A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0013"
    $ current_voice = "voice/MOE07A_CRS0013.ogg"
    "红莉栖" "「总而言之，这就是所有需要的零件了呢」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0015"
    $ current_voice = "voice/MOE07A_MAY0015.ogg"
    "真由理" "「比想象中花的时间要长呢」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0007"
    $ current_voice = "voice/MOE07A_MOE0007.ogg"
    "萌郁" "「……」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[228,229,230,231,232])











    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_LAB01"]










    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0014"
    $ current_voice = "voice/MOE07A_CRS0014.ogg"
    "红莉栖" "「是萌郁发来的邮件？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0016"
    $ current_voice = "voice/MOE07A_MAY0016.ogg"
    "真由理" "「真的呐——」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0015"
    $ current_voice = "voice/MOE07A_CRS0015.ogg"
    "红莉栖" "「为何要特地发邮件说呀」"
    stop se
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[233,234,235])

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_EDIT_LAB02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_LAB02"]










    stop se

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA06"),"True","lh/CRS_ASA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "看了邮件，红莉栖和真由理都柔和地笑了起来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0017"
    $ current_voice = "voice/MOE07A_MAY0017.ogg"
    "真由理" "「但是呢，但是呢，和萌郁说的一样，今天真的很开心呢♪」"
    "其实呢，托红莉栖的福，采购早就已经结束了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    "因为采购已经结束了，我们在{color=#f00}ＵＰＸ{/color}内的咖啡厅喝了一些茶，真由理又进行了一些个人的购物。"
    "说实话，感觉有点对不起在Ｌａｂ等着我们的冈部君呐……"
    "对于至今为止从未和同性的朋友出游的我来说，今天的体验十分新鲜……一定会成为一生的回忆吧。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0016"
    $ current_voice = "voice/MOE07A_CRS0016.ogg"
    "红莉栖" "「难道说……今天这样的日子，就是之前只在杂志上读到过的叫做“女子会”的东西？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB03"),"True","lh/MAY_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0018"
    $ current_voice = "voice/MOE07A_MAY0018.ogg"
    "真由理" "「是呢。红莉栖酱住在美国，所以不知道这样的事情呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0019"
    $ current_voice = "voice/MOE07A_MAY0019.ogg"
    "真由理" "「确实说的就是今天这样的活动」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB08"),"True","lh/CRS_ASB08a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0017"
    $ current_voice = "voice/MOE07A_CRS0017.ogg"
    "红莉栖" "「原来如此。这样的话，下次再来开女子会吧，呼呼呼」"
    "两个人都是好孩子呢。"
    "可能的话，就这样大家一直在一起——"

    stop bgm 

    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "！？"


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0018"
    $ current_voice = "voice/MOE07A_CRS0018.ogg"
    "红莉栖" "「啊。萌郁，手机响了呢」"

    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0008"
    $ current_voice = "voice/MOE07A_MOE0008.ogg"
    "萌郁" "「诶……诶诶……多谢提醒。」"

    "难道说——"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail (p=True)







    play bgm "BGM21"


    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0009"
    $ current_voice = "voice/MOE07A_MOE0009.ogg"
    "萌郁" "「……」"
    "突然觉得刚才那样开心的时光宛若一纸荒唐言。"
    "一瞬间气血上涌。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_EDIT_TEN02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_TEN02"]
    call send_mail (id=[237,238])








    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_TEN03"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    pause 2
    call read_last_mail





    "骗人……"
    "杀死牧濑……？"
    "开玩笑的吧……？"
    "骗人……骗人，骗人，骗人，骗人。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0019"
    $ current_voice = "voice/MOE07A_CRS0019.ogg"
    "红莉栖" "「怎么了，萌郁？看你脸色不太好的样子……」"
    window hide
    call hide_phone

    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0010"
    $ current_voice = "voice/MOE07A_MOE0010.ogg"
    "萌郁" "「没……没什么……没关系」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "我，想起了那个潜伏在秋叶原的科学家的事情。"
    "将她带到既定的地方……然后将红莉栖杀害。"
    "我该……怎么做呢？"
    "身处Ｒｏｕｎｄｅｒ这个组织的我，对于来自ＦＢ的命令应该是绝对服从的。"
    "不对。就算不考虑Ｒｏｕｎｄｅｒ的身份，是因为ＦＢ我今天才会在这里。如果失去了她的话……我活着这一点都很令人奇怪。"
    "就算与这个世界为敌，我也不愿意让ＦＢ讨厌我。"
    "但是，要是遵从她的命令的话红莉栖就会……"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0020"
    $ current_voice = "voice/MOE07A_CRS0020.ogg"
    "红莉栖" "「呐，萌郁。真的没问题？看起来你很难过的样子，回Ｌａｂ也许会比较好？」"
    window hide


    $ loadBG(0,"BG16A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0011"
    $ current_voice = "voice/MOE07A_MOE0011.ogg"
    "萌郁" "「红莉栖……」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0021"
    $ current_voice = "voice/MOE07A_CRS0021.ogg"
    "红莉栖" "「嗯？怎么了么？」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0012"
    $ current_voice = "voice/MOE07A_MOE0012.ogg"
    "萌郁" "「那个……这个……」"
    "好害怕……只是说话就让我感到如此恐怖。"
    "但是，如果不把她带向那里的话就等于背叛了ＦＢ——"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0013"
    $ current_voice = "voice/MOE07A_MOE0013.ogg"
    "萌郁" "「……」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[240,241,242,243])

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_EDIT_LAB03_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_LAB03"]











    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0020"
    $ current_voice = "voice/MOE07A_MAY0020.ogg"
    "真由理" "「咦？又是从萌郁那里发来的邮件呢」"
    stop se
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0022"
    $ current_voice = "voice/MOE07A_CRS0022.ogg"
    "红莉栖" "「那个，我倒是没关系……萌郁真的没关系吗？」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 
    call send_mail (id=[244,245])

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_EDIT_LAB04_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_SEND_LAB04"]










    stop se

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0021"
    $ current_voice = "voice/MOE07A_MAY0021.ogg"
    "真由理" "「那，就这样决定了♪」"
    "最差劲了……"
    "我，在面对ＦＢ和朋友的选择题中——舍弃了朋友。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG32A")

    show screen phoneSD1
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0014"
    $ current_voice = "voice/MOE07A_MOE0014.ogg"
    "萌郁" "「我……在那幢大楼里的编辑部打工……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0022"
    $ current_voice = "voice/MOE07A_MAY0022.ogg"
    "真由理" "「这样啊——萌郁是编辑呢——」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0023"
    $ current_voice = "voice/MOE07A_CRS0023.ogg"
    "红莉栖" "「说起来，之前确实有这么说过呢。」"
    "我带着红莉栖和真由理，来到了我编造出来的编辑部门口。"
    "根据命令，我必须带着她们穿过这个人行横道。"
    "信号灯变成了绿色。"
    "恐怕……走过这里的话就会——"
    window hide
    hide lh6  with dissolve
    "红莉栖刚走出一步时……"
    "当然，她不知道接下来会发生什么。"
    "“有什么事”，为什么就这么相信了我的谎言，特地往这边走了呢……"
    "不行，红莉栖……！"
    "如果这么走下去的话你就……！！"
    play se "SGSE137"


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC04"),"True","lh/MAY_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    stop bgm 
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0015"
    $ current_voice = "voice/MOE07A_MOE0015.ogg"
    "萌郁" "「危险……！」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0024"
    $ current_voice = "voice/MOE07A_CRS0024.ogg"
    "红莉栖" "「咿呀！？」"
    hide screen phoneSD1
    window hide

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0025"
    $ current_voice = "voice/MOE07A_CRS0025.ogg"
    "红莉栖" "「痛痛痛……」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0023"
    $ current_voice = "voice/MOE07A_MAY0023.ogg"
    "真由理" "「红莉栖酱没事吧！？」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0026"
    $ current_voice = "voice/MOE07A_CRS0026.ogg"
    "红莉栖" "「唔……唔嗯……我没事……」"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE004A"]]["Check"]=True
    $ loadBG(0,"EV_MOE004A")

    play bgm "BGM24"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0016"
    $ current_voice = "voice/MOE07A_MOE0016.ogg"
    "萌郁" "「……！？」"
    "红莉栖好像失去了力气一般靠在了我身上。"
    "整个人完全地靠在了我身上，紧紧地抱着。"
    "红莉栖的身体感觉十分冰冷，直冒冷汗，连衣服都有些湿了。"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0027"
    $ current_voice = "voice/MOE07A_CRS0027.ogg"
    "红莉栖" "「谢谢你……萌郁」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0028"
    $ current_voice = "voice/MOE07A_CRS0028.ogg"
    "红莉栖" "「要不是你那个瞬间出手相助，我……我就……」"
    "红莉栖的声音，慢慢变成了哽咽。"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0029"
    $ current_voice = "voice/MOE07A_CRS0029.ogg"
    "红莉栖" "「真的是……谢谢你了」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0017"
    $ current_voice = "voice/MOE07A_MOE0017.ogg"
    "萌郁" "「…………」"
    "在一旁，红莉栖手里拿着的时间机器的零件已经碎了一地。"
    "但是，红莉栖本身并无大恙。"
    "救了她真是太好了……"
    "但是——"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0024"
    $ current_voice = "voice/MOE07A_MAY0024.ogg"
    "真由理" "「就算那样，刚才的车好可怕啊」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0025"
    $ current_voice = "voice/MOE07A_MAY0025.ogg"
    "真由理" "「因为是红灯，完全没有想到它会冲过来呢。」"
    window hide


    $ loadBG(2,"BG32A")





    show screen phonebtn
    show screen phoneSD1
    "……怎么办啊。"
    "我，帮助了红莉栖就意味着背叛了ＦＢ。"
    "这无疑是背叛行为……恐怕，Ｒｏｕｎｄｅｒ已经向ＦＢ去报告了。"
    "我……背叛了将我从绝望中拯救出来的……ＦＢ。"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0018"
    $ current_voice = "voice/MOE07A_MOE0018.ogg"
    "萌郁" "「对不……起……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC04"),"True","lh/CRS_ALC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0030"
    $ current_voice = "voice/MOE07A_CRS0030.ogg"
    "红莉栖" "「萌郁……？」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0019"
    $ current_voice = "voice/MOE07A_MOE0019.ogg"
    "萌郁" "「对不起……对不起……」"
    "我现在……只能想着怎么办才好呢……已经不知道在对谁道歉了。"
    "我为什么要道歉呢？"
    "因为背叛了ＦＢ？"
    "因为把红莉栖引向了险境？"
    "不明白。"
    "但是一句话来说……我现在在后悔着什么。"
    window hide
    play se "SGSE803"

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0026"
    $ current_voice = "voice/MOE07A_MAY0026.ogg"
    "真由理" "「咦？　是从冈伦那里发来的邮件」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0027"
    $ current_voice = "voice/MOE07A_MAY0027.ogg"
    "真由理" "「而且有三封？」"

    stop se
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0028"
    $ current_voice = "voice/MOE07A_MAY0028.ogg"
    "真由理" "「呐呐，你们也看看。刚刚冈伦发过来的邮件，这是不是那个啊」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA04"),"True","lh/MAY_ASA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "真由理将她的手机放在我的眼前。"
    "上面有冈部君发来的三封邮件。"
    window hide


    $ loadBG(2,"PBG11A")






    $ loadBG(2,"PBG11B")






    $ loadBG(2,"PBG11C")



    hide screen phonebtn
    "奇怪的邮件……"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0031"
    $ current_voice = "voice/MOE07A_CRS0031.ogg"
    "红莉栖" "「啊啊……这个大概是Ｄｍａｉｌ吧？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0029"
    $ current_voice = "voice/MOE07A_MAY0029.ogg"
    "真由理" "「全部都只有六个文字呢」"
    window hide



    $ loadBG(2,"BG32A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0032"
    $ current_voice = "voice/MOE07A_CRS0032.ogg"
    "红莉栖" "「萌郁」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0020"
    $ current_voice = "voice/MOE07A_MOE0020.ogg"
    "萌郁" "「对…不起…」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0033"
    $ current_voice = "voice/MOE07A_CRS0033.ogg"
    "红莉栖" "「请不要再道歉了。多亏了萌郁我没有受伤，零件的话再买就好了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA06"),"True","lh/CRS_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0034"
    $ current_voice = "voice/MOE07A_CRS0034.ogg"
    "红莉栖" "「所以说，呐？就不要在意零件的事了」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0035"
    $ current_voice = "voice/MOE07A_CRS0035.ogg"
    "红莉栖" "「正好有些要多买的零件，我们再跑一趟吧？」"
    "果然……她一点都没有起疑心。"
    "所以这个时候以为我是因为弄坏了零件在向她道歉。"
    "为什么？　为什么Ｌａｂ的大家都是如此的温柔？"
    "我……明明是为了不让ＦＢ讨厌而要去杀掉红莉栖的。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0036"
    $ current_voice = "voice/MOE07A_CRS0036.ogg"
    "红莉栖" "「好了，走吧」"
    "我无法好好地握住，红莉栖向我伸出的手。"
    "握住那样温柔的手的资格，我并没有。"
    "我，是为了ＦＢ而活着的。"
    "那么为什么……我会这么难过呢？"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG02N2")


    show screen phonebtn
    show screen phoneSD1
    "回到Ｌａｂ的时候，冈部君出来迎接了我们。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0046"
    $ current_voice = "voice/MOE07A_OKA0046.ogg"
    "伦太郎" "「终于回来了啊你们！　那么，快让我看看胜利大门的钥匙吧！！」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0037"
    $ current_voice = "voice/MOE07A_CRS0037.ogg"
    "红莉栖" "「胜利大门的钥匙没有，零件可是好好地买回来了哦」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0038"
    $ current_voice = "voice/MOE07A_CRS0038.ogg"
    "红莉栖" "「给，拿好」"
    play se "SGSE331"


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0047"
    $ current_voice = "voice/MOE07A_OKA0047.ogg"
    "伦太郎" "「……」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0039"
    $ current_voice = "voice/MOE07A_CRS0039.ogg"
    "红莉栖" "「说起来，你刚才用了Ｄｍａｉｌ吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD02"),"True","lh/OKA_ASD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0048"
    $ current_voice = "voice/MOE07A_OKA0048.ogg"
    "伦太郎" "「……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0040"
    $ current_voice = "voice/MOE07A_CRS0040.ogg"
    "红莉栖" "「……等等冈部？有在听吗？」"
    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0030"
    $ current_voice = "voice/MOE07A_MAY0030.ogg"
    "真由理" "「冈伦？没事吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB03"),"True","lh/CRS_ASB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0041"
    $ current_voice = "voice/MOE07A_CRS0041.ogg"
    "红莉栖" "「冈部。喂！发什么呆呀！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0049"
    $ current_voice = "voice/MOE07A_OKA0049.ogg"
    "伦太郎" "「……哈！」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0050"
    $ current_voice = "voice/MOE07A_OKA0050.ogg"
    "伦太郎" "「零件？　零件还好吗！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0042"
    $ current_voice = "voice/MOE07A_CRS0042.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0043"
    $ current_voice = "voice/MOE07A_CRS0043.ogg"
    "红莉栖" "「零件……」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0044"
    $ current_voice = "voice/MOE07A_CRS0044.ogg"
    "红莉栖" "「你手里的拿着的不就是零件嘛」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0051"
    $ current_voice = "voice/MOE07A_OKA0051.ogg"
    "伦太郎" "「我手里……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM23"

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0052"
    $ current_voice = "voice/MOE07A_OKA0052.ogg"
    "伦太郎" "「哦！哦哦！噢噢噢噢噢！确实，这就是我梦寐以求的改变世界的钥匙！」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0053"
    $ current_voice = "voice/MOE07A_OKA0053.ogg"
    "伦太郎" "「呼哈哈哈哈！这次的实验也成功了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0054"
    $ current_voice = "voice/MOE07A_OKA0054.ogg"
    "伦太郎" "「寄宿于我身的魔眼，Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ确实发动了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0045"
    $ current_voice = "voice/MOE07A_CRS0045.ogg"
    "红莉栖" "「是是。厨二妄想，乙」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0055"
    $ current_voice = "voice/MOE07A_OKA0055.ogg"
    "伦太郎" "「才不是妄想！」"
    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0056"
    $ current_voice = "voice/MOE07A_OKA0056.ogg"
    "伦太郎" "「因为我刚刚从另一条你们带着损坏的零件回到Ｌａｂ的世界线过来！」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0046"
    $ current_voice = "voice/MOE07A_CRS0046.ogg"
    "红莉栖" "「……那个，是说真的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0057"
    $ current_voice = "voice/MOE07A_OKA0057.ogg"
    "伦太郎" "「当然是真的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC01"),"True","lh/CRS_ASC01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0047"
    $ current_voice = "voice/MOE07A_CRS0047.ogg"
    "红莉栖" "「这样的话……这一切都说得通了」"
    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0021"
    $ current_voice = "voice/MOE07A_MOE0021.ogg"
    "萌郁" "「……什么意思？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0031"
    $ current_voice = "voice/MOE07A_MAY0031.ogg"
    "真由理" "「真由喜不太理解冈伦说的话呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0048"
    $ current_voice = "voice/MOE07A_CRS0048.ogg"
    "红莉栖" "「就是说刚才还在别的世界线的冈部，跑到我们这条世界线了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0032"
    $ current_voice = "voice/MOE07A_MAY0032.ogg"
    "真由理" "「诶诶！？」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0049"
    $ current_voice = "voice/MOE07A_CRS0049.ogg"
    "红莉栖" "「真由理，让我看看那封邮件」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE07A_MAY0033"
    $ current_voice = "voice/MOE07A_MAY0033.ogg"
    "真由理" "「唔，明白了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0058"
    $ current_voice = "voice/MOE07A_OKA0058.ogg"
    "伦太郎" "「哦哦，看来顺利收到了呢」"
    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0050"
    $ current_voice = "voice/MOE07A_CRS0050.ogg"
    "红莉栖" "「你是利用了这个Ｄｍａｉｌ让我有了再去买一遍零件的机会吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0059"
    $ current_voice = "voice/MOE07A_OKA0059.ogg"
    "伦太郎" "「洞察力不错嘛助手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE07A_CRS0051"
    $ current_voice = "voice/MOE07A_CRS0051.ogg"
    "红莉栖" "「那……看来这个冈部真的是从别的世界线来的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE07A_OKA0060"
    $ current_voice = "voice/MOE07A_OKA0060.ogg"
    "伦太郎" "「呼哈哈哈！那么，有了完好无损的零件，作战继续！」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG34N2")


    play bgm "BGM20"
    show screen phonebtn
    show screen phoneSD1
    "说有些事情的我回到了公寓。"


    $ targetmailid = gc["ScriptMacros"]["FM_MOE07A_RECV_TEN04"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "一回到房间，ＦＢ就发来了邮件。"

    "肯定是要说些关于任务失败的话吧。"

    "绝对不要把我救了红莉栖这件事暴露出去……！"

    "仿佛祈祷一般，用双手操作着手机。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail (p=True)






    "太好了，ＦＢ没有注意到的样子。"
    window hide
    call hide_phone

    $ stopvoc("MOE")
    play MOE "MOE07A_MOE0022"
    $ current_voice = "voice/MOE07A_MOE0022.ogg"
    "萌郁" "「哈……」"

    $ targetmailid = cml.setdefault("RM_MOE_SEND_MAY05","")

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    "……安心下来了。"
    call CHECK_RM_RECEIVE
    "但Ｌａｂｍｅｍ的击杀命令应该还没结束。"
    call CHECK_RM_RECEIVE
    "虽然现在还是间接的击杀命令，但要是一直失败的话，应该会有直接击杀的命令。"
    call CHECK_RM_RECEIVE
    "如果到了那个时候，我能完成吗？杀死他们？"
    call CHECK_RM_RECEIVE
    "……应该不能，吧。"
    call CHECK_RM_RECEIVE
    "不能再和大家呆在一起了。"
    call CHECK_RM_RECEIVE
    "和我在一起的话，Ｌａｂ的各位绝对会变得不幸的。"
    call CHECK_RM_RECEIVE
    "讨厌。好害怕。好痛苦。谁来救救我。冈部君。红莉栖。真由理。……ＦＢ。"

    call CHECK_RM_RECEIVE
    "从那天开始，我就再也没有出现在Ｌａｂ过。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY05_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY05_01"])


    hide screen phoneSD1
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return





    stop se





    return







    return
