label SGFD2_MOE02B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG05A1")


    play bgm "BGM25"

    $ date="8/7"
    $ day = "SAT"
    python:
        RcvMail(125)
        ReadMail(125)
        SndMail(126)
    show screen phonebtn
    show screen phoneSD1

    "几天后，受冈部君的邀请去了Ｌａｂ。"
    "说要进行Ｄｍａｉｌ实验……Ｄｍａｉｌ是什么鬼啦。"
    "从ＦＢ那里得到的资料也没有记载。"
    "难道说是什么危险的武器？兵器？"
    window hide



    $ loadBG(0,"BG02A2")
    play se "SGSE024"


    "到了Ｌａｂ后，发现还有除了桥田君，牧濑，椎名以外初次见面的人。"
    "没有多想地将身体朝向他们。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "MOE02A_SUZ0000"
    $ current_voice = "voice/MOE02A_SUZ0000.ogg"
    "铃羽" "「请多指教呢。桐生萌郁」"


    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    "首先自我介绍的是阿万音小姐，她在Ｌａｂ下面的{color=#f00}显像管工房{/color}打工。"
    "虽然看起来天真无邪，但实际上难以捉摸。"
    "和这个Ｌａｂ有关的人，肯定不是泛泛之辈。"
    window hide



    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA02"),"True","lh/FEI_BSA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MOE02A_FEI0000"
    $ current_voice = "voice/MOE02A_FEI0000.ogg"
    "菲利斯" "「萌郁喵。请多指教喵」"
    $ stopvoc("RUK")
    play RUK "MOE02A_RUK0000"
    $ current_voice = "voice/MOE02A_RUK0000.ogg"
    "琉华" "「请、请多指教」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0003"
    $ current_voice = "voice/MOE02A_MOE0003.ogg"
    "萌郁" "「请多指教……」"


    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAID_CAFE"])
    "菲利斯・喵喵啊……估计是假名吧。她好像是在秋叶原的{color=#f00}女仆咖啡厅{/color}『ＭａｙＱｕｅｅｎ＋Ｎｙａ2』打工。"




    "漆原琉华自称是柳林神社主祭的儿子。"


    "菲利斯小姐的说话方式很奇特，而且漆原君到底是……性别搞不太清楚啊。"
    "因为突然多了的几个人感到有些困惑。这个Ｌａｂ的情报网好像很厉害啊……。"
    "有些不安，我看着身份……连性别都捉摸不透的漆原君，注意到了这一点的冈部君用深沉的语气说道——"
    window hide



    $ loadBG(2,"BG01A")

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0010"
    $ current_voice = "voice/MOE02A_OKA0010.ogg"
    "伦太郎" "「但是，是男的。」"
    "不懂他在说什么。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_RECV_TEN01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call read_last_mail
    hide screen phonebtn
    hide screen phonebtn2




    "果然，很危险啊……"
    "我立刻给ＦＢ回信了。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_EDIT_TEN02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_SEND_TEN02"]
    pause 2
    call send_mail (id=[128,129,130])
    call hide_phone
    $ ReplyMail(127)











    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0011"
    $ current_voice = "voice/MOE02A_OKA0011.ogg"
    "伦太郎" "「那么现在开始第二次Ｄｍａｉｌ试验！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0004"
    $ current_voice = "voice/MOE02A_MOE0004.ogg"
    "萌郁" "「实验吗……要做些什么呢？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0012"
    $ current_voice = "voice/MOE02A_OKA0012.ogg"
    "伦太郎" "「也就是说呢──」"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB01"),"True","lh/CRS_BMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0013"
    $ current_voice = "voice/MOE02A_CRS0013.ogg"
    "红莉栖" "「简单来说，就是向过去发送邮件」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0005"
    $ current_voice = "voice/MOE02A_MOE0005.ogg"
    "萌郁" "「……向过去？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0014"
    $ current_voice = "voice/MOE02A_CRS0014.ogg"
    "红莉栖" "「嗯」"
    "诶，他们这些人……到底在说些什么呢？"
    "向过去发送邮件什么的……"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0013"
    $ current_voice = "voice/MOE02A_OKA0013.ogg"
    "伦太郎" "「助手哟。不要随便抢我的——」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0015"
    $ current_voice = "voice/MOE02A_CRS0015.ogg"
    "红莉栖" "「用那个电话微波炉发送邮件的话，可以把邮件发到过去」"
    window hide



    $ loadBG(2,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB01"),"True","lh/CRS_BSB01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0014"
    $ current_voice = "voice/MOE02A_OKA0014.ogg"
    "伦太郎" "「喂，Ｃｈｒｉｓｔｉｎａ！让我也说一些吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0016"
    $ current_voice = "voice/MOE02A_CRS0016.ogg"
    "红莉栖" "「让你来说的话你会在那里一直爆{color=#f00}厨二病{/color}ＮＥＴＡ所以还是算了」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0015"
    $ current_voice = "voice/MOE02A_OKA0015.ogg"
    "伦太郎" "「可恶……」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0006"
    $ current_voice = "voice/MOE02A_MOE0006.ogg"
    "萌郁" "「……我觉得那样的事是不可能的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0016"
    $ current_voice = "voice/MOE02A_OKA0016.ogg"
    "伦太郎" "「不，是可能的！　要问为什么的话其实这个{color=#f00}电话微波炉（暂）{/color}是──」"


    window hide
    play se "SGSE110"




    $ loadBG(2,"BG03A4")



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0017"
    $ current_voice = "voice/MOE02A_OKA0017.ogg"
    "伦太郎" "「是时间机器！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0007"
    $ current_voice = "voice/MOE02A_MOE0007.ogg"
    "萌郁" "「……！」"
    "时间……机器……！？"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0008"
    $ current_voice = "voice/MOE02A_MOE0008.ogg"
    "萌郁" "「开玩笑……的吧……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0018"
    $ current_voice = "voice/MOE02A_OKA0018.ogg"
    "伦太郎" "「如果你觉得是玩笑的话，指压师哦。那就让你来当第一个试验者吧！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0009"
    $ current_voice = "voice/MOE02A_MOE0009.ogg"
    "萌郁" "「我来当……试验者……？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA04"),"True","lh/CRS_BSA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0017"
    $ current_voice = "voice/MOE02A_CRS0017.ogg"
    "红莉栖" "「冈部，那样说的话，感觉不就是人体试验了嘛。桐生小姐明显害怕了。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA06"),"True","lh/CRS_BMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0018"
    $ current_voice = "voice/MOE02A_CRS0018.ogg"
    "红莉栖" "「桐生小姐，没关系的哦。一点都不危险的。」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0010"
    $ current_voice = "voice/MOE02A_MOE0010.ogg"
    "萌郁" "「是这样……吗？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0019"
    $ current_voice = "voice/MOE02A_CRS0019.ogg"
    "红莉栖" "「嗯嗯。只是向指定的手机号发送邮件而已。」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0011"
    $ current_voice = "voice/MOE02A_MOE0011.ogg"
    "萌郁" "「……明白了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0020"
    $ current_voice = "voice/MOE02A_CRS0020.ogg"
    "红莉栖" "「那就写邮件吧。文字尽可能的简洁一些，因为有字数限制。」"
    "这是我的机会。"
    "参加这个实验的话就可以写出详细的报告了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)




    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_SEND_FG801"]
    call send_mail (id=[132,133])


    "写好了邮件以后被称为电话微波炉（暂）的道具动了起来。"

    show houden 
    play se "SGSE035L" loop


    stop bgm 
    "白色的电流在微波炉里流走着。"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0012"
    $ current_voice = "voice/MOE02A_MOE0012.ogg"
    "萌郁" "「──！？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0021"
    $ current_voice = "voice/MOE02A_CRS0021.ogg"
    "红莉栖" "「就是现在。发送！」"

    "我颤颤巍巍地按下了发送按钮后，放电现象渐渐地停了下来。"
    window hide



    stop se
    play se "SGSE020"



    hide houden 
    call hide_phone


    "牧濑淡然地从微波炉上取下了手机。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB01"),"True","lh/CRS_BMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0022"
    $ current_voice = "voice/MOE02A_CRS0022.ogg"
    "红莉栖" "「看吧」"
    "牧濑给我看了冈部君的手机。"
    play bgm "BGM23"
    "屏幕上显示着令人惊讶的结果。"
    window hide


    $ loadBG(2,"PBG10A")



    hide screen phonebtn
    "刚刚发送的邮件在冈部君的手机上的收信日期是过去的时间。"
    window hide


    $ loadBG(2,"PBG10B")



    "而且那个时间在我与冈部君相遇之前。"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0013"
    $ current_voice = "voice/MOE02A_MOE0013.ogg"
    "萌郁" "「这不科学……」"
    window hide


    $ loadBG(2,"BG03A4")




    show screen phoneSD1



    $ loadBG(2,"BG03A4D1")



    hide screen phonebtn
    "难道真的说是时间机器……？"
    window hide



    $ loadBG(2,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB01"),"True","lh/CRS_BSB01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0019"
    $ current_voice = "voice/MOE02A_OKA0019.ogg"
    "伦太郎" "「虽然不科学，但这是事实。眼见为实啊。你自己刚刚向过去发送了邮件。」"
    hide screen phoneSD1
    window hide



    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE008A"]]["Check"]=True
    $ loadBG(0,"EV_MOE008A")

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0023"
    $ current_voice = "voice/MOE02A_CRS0023.ogg"
    "红莉栖" "「那么，现在的那什么世界线发生变化了吗？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0020"
    $ current_voice = "voice/MOE02A_OKA0020.ogg"
    "伦太郎" "「没有。Ｒｅａｄｉｎｇ　Ｓｔｅｉｎｅｒ并没有发动。」"
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0003"
    $ current_voice = "voice/MOE02A_DAR0003.ogg"
    "至" "「说起来啊，那个真的是特殊能力？不是妄想？」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE008B"]]["Check"]=True

    $ loadBG(2,"EV_MOE008B")



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0021"
    $ current_voice = "voice/MOE02A_OKA0021.ogg"
    "伦太郎" "「才不是妄想！其实，我也存在于别的世界线」"
    "听不懂冈部君到底在说什么。"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0014"
    $ current_voice = "voice/MOE02A_MOE0014.ogg"
    "萌郁" "「世界线……？」"
    $ stopvoc("RUK")
    play RUK "MOE02A_RUK0001"
    $ current_voice = "voice/MOE02A_RUK0001.ogg"
    "琉华" "「世界线是什么东西啊？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOHN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOHN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOHN"])

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KOTEHAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KOTEHAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KOTEHAN"])

    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0004"
    $ current_voice = "voice/MOE02A_DAR0004.ogg"
    "至" "「在{color=#f00}＠Ｃｈaｎｎｅｌ{/color}上一个叫做{color=#f00}Ｊｏｈｎ　Ｔｉｔｏｒ{/color}的{color=#f00}固定用户{/color}所提出的理论」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0022"
    $ current_voice = "voice/MOE02A_OKA0022.ogg"
    "伦太郎" "「是这样的。世界线是——」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0024"
    $ current_voice = "voice/MOE02A_CRS0024.ogg"
    "红莉栖" "「Ｓｔｏｐ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0023"
    $ current_voice = "voice/MOE02A_OKA0023.ogg"
    "伦太郎" "「……助手哟，从刚才开始你就好像一直在故意针对我？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC01"),"True","lh/CRS_BSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0025"
    $ current_voice = "voice/MOE02A_CRS0025.ogg"
    "红莉栖" "「针对什么？」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0015"
    $ current_voice = "voice/MOE02A_MOE0015.ogg"
    "萌郁" "「冈部君……请详细地，告诉我」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0024"
    $ current_voice = "voice/MOE02A_OKA0024.ogg"
    "伦太郎" "「当然没问题。所以说呢……真由理，有毛线吗？」"
    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0002"
    $ current_voice = "voice/MOE02A_MAY0002.ogg"
    "真由理" "「嗯，有的哟」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "椎名从Ｃｏｓｐｌａｙ用的裁缝箱中取出了一些毛线，递给了冈部君。"
    "冈部君剪下了一段长度适中的毛线，放在桌子上。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0025"
    $ current_voice = "voice/MOE02A_OKA0025.ogg"
    "伦太郎" "「那么开始咯。准备好了吗？」"

    stop bgm 
    "所有人都点了点头。冈部君的说话方式变得和刚才截然不同了。"
    "这是他真实的面目。"
    "作为掌控者Ｌａｂ的Ｍａｄ　Ｓｃｉｅｎｔｉｓｔ的……真实的面目。"
    "我在这样的氛围里也稍微有些紧张起来。"
    window hide


    $ loadBG(2,"IBGX063")



    play bgm "BGM19"
    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0026"
    $ current_voice = "voice/MOE02A_OKA0026.ogg"
    "伦太郎" "「世界可以说是毛线一样的东西。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0027"
    $ current_voice = "voice/MOE02A_OKA0027.ogg"
    "伦太郎" "「毛线是由许多更细的线组合起来的。然后这样的一根根细线代表了有着不同可能性的世界。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0028"
    $ current_voice = "voice/MOE02A_OKA0028.ogg"
    "伦太郎" "「Ｔｉｔｏｒ是用河流打比方的，但那样的话就没办法用具体事物来表示了。所以我用的是毛线。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0029"
    $ current_voice = "voice/MOE02A_OKA0029.ogg"
    "伦太郎" "「世界恐怕是像这一根巨大的毛线，在其中有无数的细线代表着无数的可能性，因此这些世界线是非常的密集的。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0030"
    $ current_voice = "voice/MOE02A_OKA0030.ogg"
    "伦太郎" "「所以说这其中的某根细线就代表着我们现在所处的世界。到目前为止都能理解吗？」"
    "我无言地点了点头。"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("RUK")
    play RUK "MOE02A_RUK0002"
    $ current_voice = "voice/MOE02A_RUK0002.ogg"
    "琉华" "「虽然有些……但还是可以理解的。」"
    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0003"
    $ current_voice = "voice/MOE02A_MAY0003.ogg"
    "真由理" "「那个，也就是说真由喜其实是住在一根毛线里咯？」"
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0005"
    $ current_voice = "voice/MOE02A_DAR0005.ogg"
    "至" "「真由氏，大概就是那样的感觉ｏｋ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0004"
    $ current_voice = "voice/MOE02A_MAY0004.ogg"
    "真由理" "「真的吗？　太好了——」"
    "望了一眼开心的椎名，冈部君又继续说了下去。"
    window hide


    $ loadBG(2,"IBGX063")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0031"
    $ current_voice = "voice/MOE02A_OKA0031.ogg"
    "伦太郎" "「世界就像毛线那样有无数的可能性。但是，只存在一个世界。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0032"
    $ current_voice = "voice/MOE02A_OKA0032.ogg"
    "伦太郎" "「向别的世界线跳跃。那意味着这个世界将被看不见的神之手所重构。」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0026"
    $ current_voice = "voice/MOE02A_CRS0026.ogg"
    "红莉栖" "「这意味着否定多世界理论咯？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0033"
    $ current_voice = "voice/MOE02A_OKA0033.ogg"
    "伦太郎" "「不，这个最多只能算是通过Ｒｅａｄｉｎｇ　Ｓｔｅｉｎｅｒ体验过的传说而已。」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0016"
    $ current_voice = "voice/MOE02A_MOE0016.ogg"
    "萌郁" "「Ｒｅａｄｉｎｇ……Ｓｔｅｉｎｅｒ？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0034"
    $ current_voice = "voice/MOE02A_OKA0034.ogg"
    "伦太郎" "「那是我拥有的力量，唯一能够观测到世界线变动的手段」"
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0006"
    $ current_voice = "voice/MOE02A_DAR0006.ogg"
    "至" "「也就是说从一条世界线跳到另外一条线的话是那种抽搐的感觉，对吧。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0035"
    $ current_voice = "voice/MOE02A_OKA0035.ogg"
    "伦太郎" "「虽然表达方式很绅士但是没有错。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0036"
    $ current_voice = "voice/MOE02A_OKA0036.ogg"
    "伦太郎" "「就比如说……桶子是作为电脑宅界的超级嗨客和不是电脑宅界的超级嗨客的世界都是可以存在的。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0037"
    $ current_voice = "voice/MOE02A_OKA0037.ogg"
    "伦太郎" "「如果向过去发送Ｄｍａｉｌ的话，向着另一条世界线移动的可能性是很高的。」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0038"
    $ current_voice = "voice/MOE02A_OKA0038.ogg"
    "伦太郎" "「然后，世界线变动导致世界再构成的话……桶子说不定会变成蹲在Ｌａｂ里的二次元宅。」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0007"
    $ current_voice = "voice/MOE02A_DAR0007.ogg"
    "至" "「说到底还不是宅男啊！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0039"
    $ current_voice = "voice/MOE02A_OKA0039.ogg"
    "伦太郎" "「无法想象不是宅的桶子。不如说，不是宅男的话还是桶子吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0008"
    $ current_voice = "voice/MOE02A_DAR0008.ogg"
    "至" "「咕呜……感觉无法反驳了。」"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB02"),"True","lh/CRS_BMB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0027"
    $ current_voice = "voice/MOE02A_CRS0027.ogg"
    "红莉栖" "「也可能存在桥田不在这个Ｌａｂ的世界线呢。」"
    $ stopvoc("SUZ")
    play SUZ "MOE02A_SUZ0001"
    $ current_voice = "voice/MOE02A_SUZ0001.ogg"
    "铃羽" "「嗯。听起来不错的世界线。」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0040"
    $ current_voice = "voice/MOE02A_OKA0040.ogg"
    "伦太郎" "「什么意思？」"
    $ stopvoc("SUZ")
    play SUZ "MOE02A_SUZ0002"
    $ current_voice = "voice/MOE02A_SUZ0002.ogg"
    "铃羽" "「啊呀，只是说那样的世界线还不错。啊哈哈」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE008A"]]["Check"]=True


    $ loadBG(2,"EV_MOE008A")



    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "MOE02A_RUK0003"
    $ current_voice = "voice/MOE02A_RUK0003.ogg"
    "琉华" "「我，有点害怕……」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0028"
    $ current_voice = "voice/MOE02A_CRS0028.ogg"
    "红莉栖" "「是呢。令人担心的是蝴蝶效应呢」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0017"
    $ current_voice = "voice/MOE02A_MOE0017.ogg"
    "萌郁" "「蝴蝶……效应？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0029"
    $ current_voice = "voice/MOE02A_CRS0029.ogg"
    "红莉栖" "「在北京的蝴蝶扇动了一下翅膀，却在纽约造成了一场风暴。改变过去的话，就好像蝴蝶的翅膀一样，些许的变动也可能造成后来历史的巨大变化。」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0030"
    $ current_voice = "voice/MOE02A_CRS0030.ogg"
    "红莉栖" "「是这样的寓意哦。」"
    $ stopvoc("FEI")
    play FEI "MOE02A_FEI0001"
    $ current_voice = "voice/MOE02A_FEI0001.ogg"
    "菲利斯" "「不知为何有些兴奋起来了喵」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0041"
    $ current_voice = "voice/MOE02A_OKA0041.ogg"
    "伦太郎" "「先说明一下，目前还没有任何证据。虽然是机密事项，但实验的目标是观测由Ｄｍａｉｌ造成的世界线变动。」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0031"
    $ current_voice = "voice/MOE02A_CRS0031.ogg"
    "红莉栖" "「话虽如此，但刚才似乎并没有发生那边的凤凰院先生所说的世界线变动啊。」"
    window hide


    $ loadBG(2,"BG02A1")



    show screen phonebtn
    show screen phoneSD1
    "我突然打了个寒战。"
    "说实话，刚才的话题实在有些过于宏大，以至于有些难以跟上。"
    "但是了解了一些事。"
    "冈部君他们在这个小小的Ｌａｂ里，操纵着世界。"
    "世界线。蝴蝶效应。都是第一次听说的东西。"
    "这些人的情报量和关系网实在是太惊人了。"
    "感觉明白了ＦＢ派我来的原因。"

    stop bgm 

    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_RECV_TEN02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "这时，收到了ＦＢ的邮件。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2

    call read_last_mail







    play bgm "FD2BGM04"
    "确实也许是这样。"
    "冈部君是Ｌａｂ的发起人，也是谈话的主导者。"
    "但是在做重要的决议时，冈部君会征询牧濑的意见。"
    "看起来有必要了解更多关于牧濑的情报。"
    window hide
    call hide_phone






    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0018"
    $ current_voice = "voice/MOE02A_MOE0018.ogg"
    "萌郁" "「……牧瀬小姐」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0032"
    $ current_voice = "voice/MOE02A_CRS0032.ogg"
    "红莉栖" "「嗯？　怎么了？」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0019"
    $ current_voice = "voice/MOE02A_MOE0019.ogg"
    "萌郁" "「牧濑在……美国的大学，做的是哪方面的研究呢……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB01"),"True","lh/CRS_BMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0033"
    $ current_voice = "voice/MOE02A_CRS0033.ogg"
    "红莉栖" "「在大学做什么？　是呢……专业是脑科学，最近在研究ＶＲ技术」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0020"
    $ current_voice = "voice/MOE02A_MOE0020.ogg"
    "萌郁" "「……ＶＲ技术？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0034"
    $ current_voice = "voice/MOE02A_CRS0034.ogg"
    "红莉栖" "「Ｖｉｓｕａｌ　Ｒｅｂｕｉｌｄｉｎｇ」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0035"
    $ current_voice = "voice/MOE02A_CRS0035.ogg"
    "红莉栖" "「简单来说的话，就是将人的记忆变成视频信号……也就是数据的技术。反过来就可以把数据直接变成人的记忆。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB02"),"True","lh/CRS_BMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0036"
    $ current_voice = "voice/MOE02A_CRS0036.ogg"
    "红莉栖" "「这么说可以吗？」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0021"
    $ current_voice = "voice/MOE02A_MOE0021.ogg"
    "萌郁" "「那么……为什么现在会在日本……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0037"
    $ current_voice = "voice/MOE02A_CRS0037.ogg"
    "红莉栖" "「嗯，不知道是不是因果轮回呢，总之被委托来做一个关于时间机器的讲座」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0022"
    $ current_voice = "voice/MOE02A_MOE0022.ogg"
    "萌郁" "「年龄是……几岁？」"
    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0038"
    $ current_voice = "voice/MOE02A_CRS0038.ogg"
    "红莉栖" "「１８岁哦」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0023"
    $ current_voice = "voice/MOE02A_MOE0023.ogg"
    "萌郁" "「……这个年纪是怎么考上大学的呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC05"),"True","lh/CRS_BMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0039"
    $ current_voice = "voice/MOE02A_CRS0039.ogg"
    "红莉栖" "「嗯，是呢。以前的学校如果有能力的话就可以跳级……所以……」"
    "牧濑红莉栖说到一半开始注意起周围的气氛。"
    "怎么了——"
    stop bgm 
    $ stopvoc("MAY")
    play MAY "MOE02A_MAY0005"
    $ current_voice = "voice/MOE02A_MAY0005.ogg"
    "真由理" "「萌郁……？」"
    window hide


    $ loadBG(2,"BG02A1")



    "不知何时不光是椎名，Ｌａｂ里的大家都呆呆地看着我。"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "冈部君一个人猥琐地笑着。"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0042"
    $ current_voice = "voice/MOE02A_OKA0042.ogg"
    "伦太郎" "「怎么了嘛指压师。对助手这么感兴趣？」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0024"
    $ current_voice = "voice/MOE02A_MOE0024.ogg"
    "萌郁" "「……！」"
    play bgm "FD2BGM05"
    "完蛋了。"
    "这样的问法，起疑心也是在所难免的。"
    "心跳开始加速。"
    "慌张地考虑要怎么蒙混过去，但是头脑一片空白。"
    "看着焦急的我，冈部君的笑容变深了。"
    "难道说……被看穿了吗……！？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0043"
    $ current_voice = "voice/MOE02A_OKA0043.ogg"
    "伦太郎" "「其实挺好的啊！了解其他Ｌａｂｍｅｍ，和他们友好相处的那份心意。指压师啊，看来你为了成为一个优秀的Ｌａｂｍｅｍ正在不懈努力着啊！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0025"
    $ current_voice = "voice/MOE02A_MOE0025.ogg"
    "萌郁" "「……诶？」"
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0044"
    $ current_voice = "voice/MOE02A_OKA0044.ogg"
    "伦太郎" "「那么我就作为凤凰院凶真告诉你一些助手的特别情报吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0045"
    $ current_voice = "voice/MOE02A_OKA0045.ogg"
    "伦太郎" "「这家伙的屁股上有蒙古斑！」"
    window hide



    $ loadBG(2,"BG02AS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA07"),"True","lh/CRS_BMA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0040"
    $ current_voice = "voice/MOE02A_CRS0040.ogg"
    "红莉栖" "「才没有呢！没看过就别信口开河啊！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0026"
    $ current_voice = "voice/MOE02A_MOE0026.ogg"
    "萌郁" "「蒙古斑……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB04"),"True","lh/CRS_BMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0041"
    $ current_voice = "voice/MOE02A_CRS0041.ogg"
    "红莉栖" "「说了没有！　刚刚好好确认过了啦」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0027"
    $ current_voice = "voice/MOE02A_MOE0027.ogg"
    "萌郁" "「没有……蒙古斑」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC02"),"True","lh/CRS_BMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0042"
    $ current_voice = "voice/MOE02A_CRS0042.ogg"
    "红莉栖" "「那个就算忘掉也没关系啦！」"
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0028"
    $ current_voice = "voice/MOE02A_MOE0028.ogg"
    "萌郁" "「这样啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA05"),"True","lh/CRS_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0043"
    $ current_voice = "voice/MOE02A_CRS0043.ogg"
    "红莉栖" "「为啥会感觉有些遗憾啦……？」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA05"),"True","lh/CRS_BSA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0046"
    $ current_voice = "voice/MOE02A_OKA0046.ogg"
    "伦太郎" "「确认了嘛、蒙古斑」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA08"),"True","lh/CRS_BSA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0044"
    $ current_voice = "voice/MOE02A_CRS0044.ogg"
    "红莉栖" "「Ｓｈｕｔ　ｕｐ！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0047"
    $ current_voice = "voice/MOE02A_OKA0047.ogg"
    "伦太郎" "「这样啊。虽然刚才忘记说了，我的名字是凤凰院──」"
    show screen phonebtn
    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0029"
    $ current_voice = "voice/MOE02A_MOE0029.ogg"
    "萌郁" "「那个……已经知道了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0048"
    $ current_voice = "voice/MOE02A_OKA0048.ogg"
    "伦太郎" "「咕呶！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC03"),"True","lh/CRS_BSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE02A_CRS0045"
    $ current_voice = "voice/MOE02A_CRS0045.ogg"
    "红莉栖" "「桐生小姐，干得漂亮」"
    $ stopvoc("DAR")
    play DAR "MOE02A_DAR0009"
    $ current_voice = "voice/MOE02A_DAR0009.ogg"
    "至" "「那个不是只要是Ｌａｂｍｅｍ都知道的Ｎｅｔａ么……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE02A_OKA0049"
    $ current_voice = "voice/MOE02A_OKA0049.ogg"
    "伦太郎" "「才不是Ｎｅｔａ！是我的魂之名！」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE008B"]]["Check"]=True


    $ loadBG(2,"EV_MOE008B")



    hide screen phonebtn
    "在大家交谈的时候，我用手轻轻抚胸。"
    "太好了。没有暴露。"
    "但是从那时候开始，紧张的心情并没有平复下来。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG34N2",trans=fade)

    show screen phonebtn
    show screen phoneSD1
    "回到了公寓。"
    "一如既往的只是为了睡觉的无趣之地。"
    "从那时候起又去了几次Ｌａｂ。"
    "结果都成功了。邮件都发送到了过去。"
    "但是冈部所期望的结果——世界线的变动并没有发生。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "昏暗的房间里，连灯都没有开，我在用邮件向ＦＢ报告今日的详情。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_EDIT_TEN03_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_SEND_TEN03"]








    call send_mail (id=[135,136,137,138,139,140,141,142,143])
    $ targetmailid = gc["ScriptMacros"]["FM_MOE02B_RECV_TEN03"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call read_last_mail







    $ stopvoc("MOE")
    play MOE "MOE02A_MOE0030"
    $ current_voice = "voice/MOE02A_MOE0030.ogg"
    "萌郁" "「……？」"
    "为什么ＦＢ会给我发这样的东西？"
    "不必他多说。"
    "没有必要下定决心。"
    "因为相信我的伙伴在这个世界上明明只有一个人，那就是ＦＢ。"
    "为什么ＦＢ会说那样的话，我并不清楚。"

    hide screen phoneSD1
    window hide

    call hide_phone






    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return






    return
