label SGFD2_DAR01A:




    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT004")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade
    $ date="8/14"
    $ day="SAT"







    $ loadBG(0,"IBGX072")

    play bgm "FD2BGM01"

    hide screen phonebtn
    show screen phoneSD1

    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0000"
    $ current_voice = "voice/DAR01A_DAR0000.ogg"
    "至" "「诸位，相信命运的存在吗？」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0001"
    $ current_voice = "voice/DAR01A_DAR0001.ogg"
    "至" "「我呢，到最近为止也是不相信的。那种满嘴命运的人呢，我只会觉得他们脑袋不太好使」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0002"
    $ current_voice = "voice/DAR01A_DAR0002.ogg"
    "至" "「是啊……直到最近才……！」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0003"
    $ current_voice = "voice/DAR01A_DAR0003.ogg"
    "至" "「但是就算是在那样的我身上，也发生了那种让我感到命运存在的邂逅。」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0004"
    $ current_voice = "voice/DAR01A_DAR0004.ogg"
    "至" "「最近，无论是醒着还是在梦中我都只是想着“她”」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0005"
    $ current_voice = "voice/DAR01A_DAR0005.ogg"
    "至" "「那种胸口被紧紧牵住的感觉……」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0006"
    $ current_voice = "voice/DAR01A_DAR0006.ogg"
    "至" "「那就是，恋爱……！」"
    stop bgm 
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0000"
    $ current_voice = "voice/DAR01A_OKA0000.ogg"
    "伦太郎" "「桶子，好恶心所以自重点」"
    window hide




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(2,"BG01N",hide=False)



    play bgm "BGM05"

    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0007"
    $ current_voice = "voice/DAR01A_DAR0007.ogg"
    "至" "「喂，冈伦你这家伙，是要妨碍别人的恋爱之路嘛！」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0001"
    $ current_voice = "voice/DAR01A_OKA0001.ogg"
    "伦太郎" "「并没有那种打算。但光是听着你的妄想就够烦了啊。」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0000"
    $ current_voice = "voice/DAR01A_CRS0000.ogg"
    "红莉栖" "「关于这点我也只能同意冈部的意见了」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0008"
    $ current_voice = "voice/DAR01A_DAR0008.ogg"
    "至" "「喂，偶尔配合一下听我说说恋爱的话题都不行吗？」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0001"
    $ current_voice = "voice/DAR01A_CRS0001.ogg"
    "红莉栖" "「那就先姑且问一下吧，桥田的恋爱对象，是哪家的谁啊？」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0009"
    $ current_voice = "voice/DAR01A_DAR0009.ogg"
    "至" "「这个问题问的好啊，牧濑氏！　下面就为各位隆重介绍！」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0010"
    $ current_voice = "voice/DAR01A_DAR0010.ogg"
    "至" "「看，就是她！」"
    "我给冈伦还有牧濑氏看了一张同人游戏的传单。"
    window hide
    play se "SGSE221"



    $ loadBG(2,"IBG028A")



    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0011"
    $ current_voice = "voice/DAR01A_DAR0011.ogg"
    "至" "「忽滑谷冰果子！　她叫冰果子碳！」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0002"
    $ current_voice = "voice/DAR01A_CRS0002.ogg"
    "红莉栖" "「……桥田，那只是，画哦。」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0012"
    $ current_voice = "voice/DAR01A_DAR0012.ogg"
    "至" "「牧濑氏牧濑氏。禁止和二次元人物恋爱什么的法律，就算找遍全世界也是找不到的哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAKAR"])
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0002"
    $ current_voice = "voice/DAR01A_OKA0002.ogg"
    "伦太郎" "「不愧是{color=#f00}超级嗨客{/color}啊。名不虚传。但是，好恶心」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0013"
    $ current_voice = "voice/DAR01A_DAR0013.ogg"
    "至" "「说起来啊，好好看看啊这质量。你敢相信这是同人吗？嘛，如果看了这个社团里的成员的话，那肯定就会觉得是个专家的手笔啊。」"
    "最近这种画也变多了啊。"
    "而且也不打算隐藏自己社团里有大触了么。"
    "好极了，再多来点吧。"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0003"
    $ current_voice = "voice/DAR01A_CRS0003.ogg"
    "红莉栖" "「说起来这个是什么啊。动漫？」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0014"
    $ current_voice = "voice/DAR01A_DAR0014.ogg"
    "至" "「社团『Ｗｉｚａｒｄ３０』的、名为『忽滑谷冰果子太喜欢寄生虫以至于不知为何就住到我的内脏里了』的同人游戏哦。简称是『寄生住内』」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COMIMA"])
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0015"
    $ current_voice = "voice/DAR01A_DAR0015.ogg"
    "至" "「虽然在{color=#f00}夏Ｃｏｍｉ{/color}的第三日才发卖，但是在最近去虎之穴的时候看到了这个传单，就一见钟情了啊！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0016"
    $ current_voice = "voice/DAR01A_DAR0016.ogg"
    "至" "「从{color=#f00}＠ｃｈａｎｎｅｌ{/color}的情报来看，不仅预制的作品数量很少，也不能通过店铺来预定，看起来会是一场恶战呢」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0017"
    $ current_voice = "voice/DAR01A_DAR0017.ogg"
    "至" "「第三天就已经是战争了啊……」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0018"
    $ current_voice = "voice/DAR01A_DAR0018.ogg"
    "至" "「但是我绝对会搞到手的！要问为什么的话，我要让冰果子碳成为被我攻略的第１０００个女主！」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0003"
    $ current_voice = "voice/DAR01A_OKA0003.ogg"
    "伦太郎" "「哦，哦……」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0004"
    $ current_voice = "voice/DAR01A_CRS0004.ogg"
    "红莉栖" "「不行了这家伙，不赶快做点什么的话……」"
    window hide




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(2,"BG01N",hide=False)



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0019"
    $ current_voice = "voice/DAR01A_DAR0019.ogg"
    "至" "「诶？」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0004"
    $ current_voice = "voice/DAR01A_OKA0004.ogg"
    "伦太郎" "「诶？」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0005"
    $ current_voice = "voice/DAR01A_CRS0005.ogg"
    "红莉栖" "「诶？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSTUME"])
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0000"
    $ current_voice = "voice/DAR01A_MAY0000.ogg"
    "真由理" "「呐呐，比起那个，大家觉得这个{color=#f00}Ｃｏｓ{/color}服怎么样啊？」"


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0001"
    $ current_voice = "voice/DAR01A_MAY0001.ogg"
    "真由理" "「锵！黑色紧身衣可以很好地衬托出事业线哦。很Ｓｅｘｙ吧？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ loadBG(0,"IBG005A",png=True,trans=moveinbottom)


    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0020"
    $ current_voice = "voice/DAR01A_DAR0020.ogg"
    "至" "「哦哦，真由氏，难道要穿这件？」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0006"
    $ current_voice = "voice/DAR01A_CRS0006.ogg"
    "红莉栖" "「好，好大胆啊……」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0002"
    $ current_voice = "voice/DAR01A_MAY0002.ogg"
    "真由理" "「不是哦。这件是，为萌郁做的」"
    window hide
    hide background-png 
    with moveoutbottom


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("MOE")
    play MOE "DAR01A_MOE0000"
    $ current_voice = "voice/DAR01A_MOE0000.ogg"
    "萌郁" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "从刚才开始存在感就一直很稀薄的桐生氏开始敲打起了手机，不一会儿冈伦的手机就震动了起来。"
    window hide
    play se "SGSE801"

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
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0005"
    $ current_voice = "voice/DAR01A_OKA0005.ogg"
    "伦太郎" "「指压师哦，我和你说过，在眼前的话就不要发邮件了，直接和我说就好吧……」"
    $ stopvoc("MOE")
    play MOE "DAR01A_MOE0001"
    $ current_voice = "voice/DAR01A_MOE0001.ogg"
    "萌郁" "「…………」"
    "说起来，这两个人什么时候关系这么好了……"
    "桐生氏也是，就没见过会给冈伦以外的人发邮件。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ loadBG(0,"IBG005A",png=True,trans=moveinbottom)


    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0003"
    $ current_voice = "voice/DAR01A_MAY0003.ogg"
    "真由理" "「呐，怎么样啊？萌郁，身材很棒，所以说肯定会很适合的吧！」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0007"
    $ current_voice = "voice/DAR01A_CRS0007.ogg"
    "红莉栖" "「夏Ｃｏｍｉ真是恐怖啊……也就是说要穿着这个，给大家看是吧？而且，还可能会被拍照吧？明明不是什么模特」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0008"
    $ current_voice = "voice/DAR01A_CRS0008.ogg"
    "红莉栖" "「那种勇气，我果然还是……」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0006"
    $ current_voice = "voice/DAR01A_OKA0006.ogg"
    "伦太郎" "「哼，肯定是因为克里斯提娜臀部的蒙古斑再加上有小肚腩才不敢穿的吧。反正谁也不会想拍你的。」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0009"
    $ current_voice = "voice/DAR01A_CRS0009.ogg"
    "红莉栖" "「才没有蒙古斑和小肚腩呢！」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True










    hide screen phonebtn
    hide background-png 
    $ loadBG(0,"EV_MOE007D")
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0007"
    $ current_voice = "voice/DAR01A_OKA0007.ogg"
    "伦太郎" "「但是指压师去{color=#f00}Ｃｏｓｐｌａｙ{/color}什么的，有些令人意外呢。平时都是一副不用邮件就说不了话的样子」"
    $ stopvoc("MOE")
    play MOE "DAR01A_MOE0002"
    $ current_voice = "voice/DAR01A_MOE0002.ogg"
    "萌郁" "「…………」"
    play se "SGSE801"

    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0008"
    $ current_voice = "voice/DAR01A_OKA0008.ogg"
    "伦太郎" "「唔？　什么什么……」"
    play se "SGSE158"

    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0009"
    $ current_voice = "voice/DAR01A_OKA0009.ogg"
    "伦太郎" "「因为杂志的计划，结果被迫身体力行去当取材对象，是吗？」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0010"
    $ current_voice = "voice/DAR01A_CRS0010.ogg"
    "红莉栖" "「不容易呢」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0004"
    $ current_voice = "voice/DAR01A_MAY0004.ogg"
    "真由理" "「但是但是，如果萌郁穿这个的话明天绝对会成为众人焦点的哟」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0005"
    $ current_voice = "voice/DAR01A_MAY0005.ogg"
    "真由理" "「说不定还能被选为有名的博客的头条呢」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0021"
    $ current_voice = "voice/DAR01A_DAR0021.ogg"
    "至" "「那必须的啊。桐生氏的傲人的身材和紧身衣的搭配，简直超工口啊笑」"
    $ stopvoc("MOE")
    play MOE "DAR01A_MOE0003"
    $ current_voice = "voice/DAR01A_MOE0003.ogg"
    "萌郁" "「……很不好……意思……」"
    window hide
    $ loadBG(0,"IBG005A",png=True,trans=moveinbottom)


    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HASHI_GIRL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HASHI_GIRL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HASHI_GIRL"])

    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0022"
    $ current_voice = "voice/DAR01A_DAR0022.ogg"
    "至" "「说起来啊，真由氏，那个Ｃｏｓ难道说是{color=#f00}雷Ｎｅｔ翔{/color}的{color=#f00}Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ{/color}吗？」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0023"
    $ current_voice = "voice/DAR01A_DAR0023.ogg"
    "至" "「如果是那样的话，这个选择简直有品位啊。真由氏ＧＪ啊。」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0024"
    $ current_voice = "voice/DAR01A_DAR0024.ogg"
    "至" "「筷女的Ｃｏｓ什么的，不要说到现在连一次都没看到过了，就连真有人会做她的Ｃｏｓ这一点都没有想到」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0025"
    $ current_voice = "voice/DAR01A_DAR0025.ogg"
    "至" "「虽然看不出来，但我其实很喜欢筷女哦。差点以为就是为了投我所好才做的了」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0006"
    $ current_voice = "voice/DAR01A_MAY0006.ogg"
    "真由理" "「诶？Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ筷女？在雷Ｎｅｔ翔里有那种角色么。」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0026"
    $ current_voice = "voice/DAR01A_DAR0026.ogg"
    "至" "「Ｃｈｏｐｓｔｉｃｋ　ｇｉｒｌ，简称筷女。」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0007"
    $ current_voice = "voice/DAR01A_MAY0007.ogg"
    "真由理" "「这个Ｃｏｓ呢，不是那个筷女的哦。是黑猫的」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0027"
    $ current_voice = "voice/DAR01A_DAR0027.ogg"
    "至" "「哦哦，是那个啊。我完全把那个角色给忘记掉了啊。是呢是呢。还是现在最流行的动画之一呢。」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIEF_NOIR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIEF_NOIR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_THIEF_NOIR"])
    "从７月开始放送的『{color=#f00}千夜怪盗黑猫{/color}』，是目前这一季的动漫中评价最好的一部。"
    window hide
    hide background-png 
    with moveoutbottom

    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0028"
    $ current_voice = "voice/DAR01A_DAR0028.ogg"
    "至" "「嘛，不管怎么说，Ｃｏｓ成黑猫的桐生氏么……感觉有些过火了呢」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0029"
    $ current_voice = "voice/DAR01A_DAR0029.ogg"
    "至" "「那看来明天在争夺战结束之后，有必要去Ｃｏｓｐｌａｙ广场里转一圈了。」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0010"
    $ current_voice = "voice/DAR01A_OKA0010.ogg"
    "伦太郎" "「争夺战不是第三日么？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOKO"])
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0030"
    $ current_voice = "voice/DAR01A_DAR0030.ogg"
    "至" "「哈？冈伦，你是在小看夏Ｃｏｍｉ么？第一天肯定是在展位排队里度过的啊{color=#f00}常考{/color}」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0031"
    $ current_voice = "voice/DAR01A_DAR0031.ogg"
    "至" "「确实这次的夏Ｃｏｍｉ里，我的本命是『寄生住内』，但是除了那个以外应该入手的宝物也是要多少有多少啊」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0032"
    $ current_voice = "voice/DAR01A_DAR0032.ogg"
    "至" "「我的脑袋里已经完成了如何在各个展位排队的分析，以及在各个社团之间应该以怎样的顺序来浏览的路线选择。」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0033"
    $ current_voice = "voice/DAR01A_DAR0033.ogg"
    "至" "「当然像我手足一样行动着的伙伴们也已经确定有三个人了」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0011"
    $ current_voice = "voice/DAR01A_CRS0011.ogg"
    "红莉栖" "「这种热情要是能对社会做点贡献就好了啊……」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0034"
    $ current_voice = "voice/DAR01A_DAR0034.ogg"
    "至" "「但是我拒绝」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0035"
    $ current_voice = "voice/DAR01A_DAR0035.ogg"
    "至" "「为自己的欲望而活着的人才是美丽的。这便是，我的美学。」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0012"
    $ current_voice = "voice/DAR01A_CRS0012.ogg"
    "红莉栖" "「好直接啊……」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0011"
    $ current_voice = "voice/DAR01A_OKA0011.ogg"
    "伦太郎" "「对于现在的桶子说什么都是没用的。他已经到达了我们无法企及的境界了」"
    window hide


    $ loadBG(2,"BG01N")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0036"
    $ current_voice = "voice/DAR01A_DAR0036.ogg"
    "至" "「那么，我差不多该去睡觉了，大家也要走了吗？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at left_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at left_q1 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at right_q1 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC05"),"True","lh/CRS_BSC05a~ipad.png") at right_q2 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0012"
    $ current_voice = "voice/DAR01A_OKA0012.ogg"
    "伦太郎" "「什么！？　回去是什么意思！」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0013"
    $ current_voice = "voice/DAR01A_CRS0013.ogg"
    "红莉栖" "「现在才晚上８点哦？」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0037"
    $ current_voice = "voice/DAR01A_DAR0037.ogg"
    "至" "「因为明天天没亮就要出发的关系，为了让自己有体力进行一整天的活动还是早点休息比较好」"
    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0008"
    $ current_voice = "voice/DAR01A_MAY0008.ogg"
    "真由理" "「嗯，确实如此呢。真由喜也差不多要回去了」"
    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0014"
    $ current_voice = "voice/DAR01A_CRS0014.ogg"
    "红莉栖" "「竟然要做到这个地步啊……」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0013"
    $ current_voice = "voice/DAR01A_OKA0013.ogg"
    "伦太郎" "「如果这么说的话，为什么还要睡觉呢！如果要坐头班电车去的话，现在就出发去排队等着不就好了！」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0038"
    $ current_voice = "voice/DAR01A_DAR0038.ogg"
    "至" "「喂喂，冈伦，不能做那种过分的事啊。在场地通宵排队可是被明令禁止的」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0039"
    $ current_voice = "voice/DAR01A_DAR0039.ogg"
    "至" "「不通过那样的不正当手段，而是堂堂正正地和大家一起挤头班电车，才是真正的死宅啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB05"),"True","lh/CRS_BSB05a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR01A_CRS0015"
    $ current_voice = "voice/DAR01A_CRS0015.ogg"
    "红莉栖" "「虽然觉得说着话的架势很酷，但是并不能太理解说的内容」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0014"
    $ current_voice = "voice/DAR01A_OKA0014.ogg"
    "伦太郎" "「你以为这个未来道具研究所的创始人是谁啊！　可是我凤凰院凶真啊！」"
    $ stopvoc("OKA")
    play OKA "DAR01A_OKA0015"
    $ current_voice = "voice/DAR01A_OKA0015.ogg"
    "伦太郎" "「不准就这么随便地把我轰出去！超级嗨客！」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0040"
    $ current_voice = "voice/DAR01A_DAR0040.ogg"
    "至" "「嗯，那不出去也行啊，给我安静点就行。我去里面的房间睡一会」"
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0041"
    $ current_voice = "voice/DAR01A_DAR0041.ogg"
    "至" "「那，真由氏，桐生氏，明天会场见了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR01A_MAY0009"
    $ current_voice = "voice/DAR01A_MAY0009.ogg"
    "真由理" "「嗯，桶子君晚安呐」"
    $ stopvoc("MOE")
    play MOE "DAR01A_MOE0004"
    $ current_voice = "voice/DAR01A_MOE0004.ogg"
    "萌郁" "「晚安哦……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
    $ stopvoc("DAR")
    play DAR "DAR01A_DAR0042"
    $ current_voice = "voice/DAR01A_DAR0042.ogg"
    "至" "「{color=#f00}乙{/color}～」"
label L_END:

    hide screen phoneSD1
    hide screen phonebtn
    $ loadBG(0,"BG_BLACK",trans=Fade(1,1,1))
    window hide

    stop bgm 
    play se "SGSE110"








    return
