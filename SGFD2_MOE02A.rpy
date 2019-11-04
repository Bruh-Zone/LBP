label SGFD2_MOE02A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG08A2")
    play se "SGSE007L" loop



    $ date="8/5"
    $ day = "THU"
    show screen phonebtn
    show screen phoneSD1

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    "在秋叶原因坠落在{color=#f00}广播馆{/color}而吸引了一大群凑热闹的人的同时，我一直在那里寻找着某样东西。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IBN5100"])
    "传说中的古董ＰＣ『{color=#f00}ＩＢＮ５１００{/color}』。"
    "最近几天一直在秋叶原中奔波着。"
    "但结果却是徒劳无功，连线索都没有。"
    "无奈之下，只好老老实实地发邮件告诉了ＦＢ。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[111,112,113,114])












    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_SEND_TEN01"]






    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""



    "和往常一样，立刻就收到了回复。"
    "ＦＢ从来没有错过我的邮件。"
    window hide
    call read_last_mail




    "他说这是一件危险但重要的任务。"
    "失败了的话，一定会让ＦＢ失望的。"
    "必须完成。"
    "让其成功。"
    "得到ＦＢ的认同。"
    "因为那是我唯一活下去的理由啊。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_EDIT_TEN02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_SEND_TEN02"]

    call send_mail (id=[116,117,118])

    call hide_phone







    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_RECV_TEN02"]

    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call read_last_mail







    "在ＦＢ的邮件里还附有对方组织头目的情报。"
    call hide_phone
    $ loadBG(0,"PACG032",png=True,at=[truecenter])
    window hide




    "让我立刻找到这个人。"
    window hide
    hide background-png 

    hide screen phonebtn


    show screen phonebtn
    show screen phoneSD1
    "正前方突然传来了什么声音。"

    stop se
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0000"
    $ current_voice = "voice/MOE02A_OKA0000.ogg"
    "伦太郎" "「是我。啊啊。果然找不到ＩＢＮ５１００啊。这说不定也是“{color=#f00}机关{/color}”的阴谋呢。」"
    "ＩＢＮ５１００……！！"
    "我停下了脚步，向声音的方向看去。"
    window hide



    $ loadBG(2,"BG13A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC01"),"True","lh/OKA_ASC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM07"
    "一名男性正用手机说着什么。"
    "身披有些破旧的白大褂，体格有些纤细。乱蓬蓬的头发。但有一双不断打量着周围的锐利眼睛。"
    "和ＦＢ的情报相吻合的外表。"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0001"
    $ current_voice = "voice/MOE02A_OKA0001.ogg"
    "伦太郎" "「无须担心。交给我狂气的Ｍａｄ　Ｓｃｉｅｎｔｉｓｔ凤凰院凶真的话，这点小事不费吹灰之力。」"
    "肯定没错。他就是组织的头目。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC05"),"True","lh/OKA_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0002"
    $ current_voice = "voice/MOE02A_OKA0002.ogg"
    "伦太郎" "「这个试炼也是命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择。Ｅｌ　Ｐｓｙ　Ｃｏｎｇｒｏｏ」"


    "不停地说着一些不明所以的话。"
    "应该是暗号吧。"
    "『要小心』"
    "重复着ＦＢ的话，我向他走去。"

    stop bgm 
    hide screen phoneSD1
    window hide




    $ loadBG(0,"EVX_M02D")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0003"
    $ current_voice = "voice/MOE02A_OKA0003.ogg"
    "伦太郎" "「综上所述，她就是Ｌａｂｍｅｍ　００５，桐生萌郁！」"
    play bgm "FD2BGM04"
    "在位于大桧山大楼二楼的未来道具研究所里，冈部君用夸张的肢体语言向大家介绍了我。"
    "牧濑朝他投去了锐利的眼神。"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0000"
    $ current_voice = "voice/MOE02A_CRS0000.ogg"
    "红莉栖" "「综上所述你个头啊。好好地说明一下啊」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0004"
    $ current_voice = "voice/MOE02A_OKA0004.ogg"
    "伦太郎" "「诶呀诶呀……果然助手理解能力低下就是麻烦啊。你到底还想让我说些什么呢？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0001"
    $ current_voice = "voice/MOE02A_CRS0001.ogg"
    "红莉栖" "「谁是助手啊！」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0002"
    $ current_voice = "voice/MOE02A_CRS0002.ogg"
    "红莉栖" "「也就是说……将突然认识的人介绍给大家并且说她也是Ｌａｂｍｅｍ了，啊，是这样的吗。喂，完全无法理解啊」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0003"
    $ current_voice = "voice/MOE02A_CRS0003.ogg"
    "红莉栖" "「好好说明一下理由啊，理由」"
    "牧濑。刚才和我打招呼的时候，还以为是个更加温柔的人……"
    "难道说牧濑很早就注意到了我的真实身份，而刚才的打招呼也许只是为了混淆视听？"
    "不小心点的话……"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC06"),"True","lh/CRS_BMC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    show screen phoneSD1
    "是注意到我的视线了吗，牧濑朝我这边看过来。"
    "正当要露出抱歉的表情的时候，她笑了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA06"),"True","lh/CRS_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0004"
    $ current_voice = "voice/MOE02A_CRS0004.ogg"
    "红莉栖" "「啊，不好意思啊。并不是在说你是什么怪人啦。」"
    "没有多想就移开了视线。"
    "不能被骗了啊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0005"
    $ current_voice = "voice/MOE02A_CRS0005.ogg"
    "红莉栖" "「那我先自我介绍一下吧。名字……啊，虽然已经说过了，我是牧濑红莉栖。是美国维克多·空多利亚大学的研究员，目前在日本短居。你呢？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HEN_PRO"])
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0000"
    $ current_voice = "voice/MOE02A_MOE0000.ogg"
    "萌郁" "「……桐生萌郁。在Ａｒｃ　Ｒｅｗｒｉｔｅ杂志的{color=#f00}编Ｐｒｏ{/color}打工……中。」"
    "这个背景当然是骗人的。为了欺骗他们，事先想好的假身份。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA06"),"True","lh/CRS_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0006"
    $ current_voice = "voice/MOE02A_CRS0006.ogg"
    "红莉栖" "「这样啊。请多指教啊。桐生小姐。」"
    "从ＦＢ那儿也得到了她的情报。"
    "美国维克多·空多利亚大学的研究员。确实如同她所说。"
    "冈部君很喜欢的杂志上载有她的论文。虽然那论文对我来说太难理解了。"
    "因为她头脑很好，一定准备了我想不到的手段来对付我。千万不能大意。"
    window hide



    $ loadBG(2,"BG01A")



    show screen phoneSD1


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0000"
    $ current_voice = "voice/MOE02A_MAY0000.ogg"
    "真由理" "「嘟嘟噜♪　真由喜对于女性Ｌａｂｍｅｍ又增加了感到很开心哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    "椎名真由理。只是个喜欢{color=#f00}Ｃｏｓｐｌａｙ{/color}的女高中生……的样子。"
    "但是，考虑到她是这个Ｌａｂ的一员，应该不只是个女高中生那么简单。要注意。"
    window hide



    $ loadBG(2,"BG02A2")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0000"
    $ current_voice = "voice/MOE02A_DAR0000.ogg"
    "至" "「冈伦，冈伦。你是怎么认识这样的美女的呀？我们现在还没到３０岁，应该是使用不了魔法的呀？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0007"
    $ current_voice = "voice/MOE02A_CRS0007.ogg"
    "红莉栖" "「性骚扰禁止」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAKAR"])
    "桥田至。是冈部君口中厉害的{color=#f00}超级嗨客{/color}。"
    "虽然他自己反驳道“要叫我黑客啦”，但并没有否认“厉害”这一点。如果要进行情报战的话，是个危险的对手。"
    hide screen phoneSD1
    window hide




    $ loadBG(2,"EVX_M02D")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0005"
    $ current_voice = "voice/MOE02A_OKA0005.ogg"
    "伦太郎" "「然后，关于选中了这个女人——指压师的理由呢。」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0008"
    $ current_voice = "voice/MOE02A_CRS0008.ogg"
    "红莉栖" "「指压师？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0009"
    $ current_voice = "voice/MOE02A_CRS0009.ogg"
    "红莉栖" "「又是个奇怪的外号呢……桐生小姐，如果感觉困惑的话请不要有顾虑地提出抗议哦？」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0001"
    $ current_voice = "voice/MOE02A_MOE0001.ogg"
    "萌郁" "「……没关系」"
    "不如说，得到这种能和对方缩短距离的诨名正是我求之不得的。"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0006"
    $ current_voice = "voice/MOE02A_OKA0006.ogg"
    "伦太郎" "「啊哼。继续下去了哦？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0007"
    $ current_voice = "voice/MOE02A_OKA0007.ogg"
    "伦太郎" "「这个女人呢，要作为我们Ｌａｂ的侦察兵，来协助我们找回失去的ＩＢＮ５１００。」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0002"
    $ current_voice = "voice/MOE02A_MOE0002.ogg"
    "萌郁" "「……失去的？」"
    "不是找不到的？"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0010"
    $ current_voice = "voice/MOE02A_CRS0010.ogg"
    "红莉栖" "「等下冈部，话题前进得太快了。桐生小姐满脸疑惑的样子」"
    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0001"
    $ current_voice = "voice/MOE02A_MAY0001.ogg"
    "真由理" "「就是呀，真由喜也完全摸不着头脑呢」"
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0001"
    $ current_voice = "voice/MOE02A_DAR0001.ogg"
    "至" "「稍微自重些吧」"
    "没有机会加入大家的对话。"
    window hide



    $ loadBG(2,"BG01A")



    show screen phoneSD1

    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "没有办法，我只好向冈部君发了一封邮件。不如说比起在这种情况下硬插嘴进去我更喜欢这样的方法。"
    window hide
    call send_mail (id=[120,121,122,123,124])










    $ targetmailid = gc["ScriptMacros"]["FM_MOE02A_SEND_OKA01"]






    call hide_phone

    play se "SGSE801"



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    stop se
    "看了邮件的冈部君意味深长地笑了。"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0008"
    $ current_voice = "voice/MOE02A_OKA0008.ogg"
    "伦太郎" "「是呢。必须将曾经在我们手中爱机的相关信息告诉 Ｌａｂｍｅｍ 」"
    hide screen phoneSD1
    window hide




    $ loadBG(2,"EVX_M02D")



    hide screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_URD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_URD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_URD"])
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0009"
    $ current_voice = "voice/MOE02A_OKA0009.ogg"
    "伦太郎" "「那是关系到Ｌａｂ命运的一大作战，{color=#f00}『掌管过去的女神』作战(Ｏｐｅｒａｔｉｏｎ　Ｖｅｒｔｈａｎｄｉ){/color}的时候……」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0011"
    $ current_voice = "voice/MOE02A_CRS0011.ogg"
    "红莉栖" "「又开始了啊……」"
    "虽然牧濑露出了一脸不耐烦的表情，但冈部君口中说出的内容，对我来说却是冲击性的。"
    "未来道具研究所曾经在柳林神社找到过被供奉着的ＩＢＮ５１００。"
    "但是，本该保管在Ｌａｂ的ＩＢＮ５１００不知何时消失了。"
    "与口若悬河滔滔不绝的冈部君的样子不同，其他人完全不在意他说的。"
    window hide



    $ loadBG(2,"BG02A2")

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0002"
    $ current_voice = "voice/MOE02A_DAR0002.ogg"
    "至" "「冈伦、妄想设定{color=#f00}乙{/color}」"
    hide screen phoneSD1
    window hide




    $ loadBG(2,"EVX_M02D")



    hide screen phonebtn
    "这到底是怎么回事？"
    "难道已经被其他的Ｒｏｕｎｄｅｒ回收了？"
    "而且就算如此……只有冈部君记得这一点很奇怪。"
    "大概是大家计划好了一起来让我感到混乱吧。"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC05"),"True","lh/CRS_BMC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0012"
    $ current_voice = "voice/MOE02A_CRS0012.ogg"
    "红莉栖" "「啊，不要在意，桐生小姐。老毛病了。」"
    hide screen phoneSD1
    window hide




    $ loadBG(2,"EVX_M02D")



    hide screen phonebtn
    "不要被骗了。"
    "这些人，在隐瞒着什么。"
    "必须搞清楚。为了ＦＢ……"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return






    return
