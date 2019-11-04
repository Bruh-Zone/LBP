label SGFD2_KYO05A:
    python:
        rml = []
        sml = []
        RcvMail(12)
        ReadMail(12)
        RcvMail(11)
        ReadMail(11)
        RcvMail(10)
        ReadMail(10)
    window hide
    stop se


    $ loadBG(0,"BG_BLACK")




    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    scene expression Solid("000000")  with fade


    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "我紧紧地闭着眼睛，等着一如既往的眩晕感退去。"
    "好不容易取回平衡感之后，我缓缓地睁开了眼睛。"
    "站在我眼前的是……"
    window hide

    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)













    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    "红莉栖。"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0000"
    $ current_voice = "voice/KYO05A_CRS0000.ogg"
    "红莉栖" "「怎么了？　看起来颜色很差的样子……」"
    "红莉栖好像有些担心我，看着我的脸。"
    "我朝她身后看去。"
    window hide

    hide screen phonebtn
    "是保险柜。大楼前面的投币式保险柜。"
    "虽然和平时一样知道Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ发动了，但是并不知道自己为什么会在这里。"
    "我将视线移回红莉栖身上，向她问道。"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0000"
    $ current_voice = "voice/KYO05A_OKA0000.ogg"
    "伦太郎" "「为什么我会在这种地方……！？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0001"
    $ current_voice = "voice/KYO05A_CRS0001.ogg"
    "红莉栖" "「哈……？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0001"
    $ current_voice = "voice/KYO05A_OKA0001.ogg"
    "伦太郎" "「真由理怎么样了……！？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0002"
    $ current_voice = "voice/KYO05A_CRS0002.ogg"
    "红莉栖" "「怎么样了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0003"
    $ current_voice = "voice/KYO05A_CRS0003.ogg"
    "红莉栖" "「不是说不知道在哪里，所以才在这里继续找的吗？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0004"
    $ current_voice = "voice/KYO05A_CRS0004.ogg"
    "红莉栖" "「虽说和冈部说的一样，就算在这里继续等下去，ｉｃｈｓ出现的概率也非常的低……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0002"
    $ current_voice = "voice/KYO05A_OKA0002.ogg"
    "伦太郎" "「ｉｃｈｓ……？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0005"
    $ current_voice = "voice/KYO05A_CRS0005.ogg"
    "红莉栖" "「『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』──是可能将真由理诱拐了的人」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0006"
    $ current_voice = "voice/KYO05A_CRS0006.ogg"
    "红莉栖" "「不是你决定这么叫的么。忘记了？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0003"
    $ current_voice = "voice/KYO05A_OKA0003.ogg"
    "伦太郎" "「等等等等等等等等！　你到底在说什么啊！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB05"),"True","lh/CRS_AMB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0007"
    $ current_voice = "voice/KYO05A_CRS0007.ogg"
    "红莉栖" "「这才是我想说的，你在说什么啊！　难道你打算说你失忆了！？」"
    "我重重地吸了一口气，睁大双眼……"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0004"
    $ current_voice = "voice/KYO05A_OKA0004.ogg"
    "伦太郎" "「啊啊啊啊────！　啊啊啊啊────！」"
    "不停地用手挠着脑袋，发出不成语句的嘶吼。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0008"
    $ current_voice = "voice/KYO05A_CRS0008.ogg"
    "红莉栖" "「什，什么啊，突然……！　怎么了！？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0005"
    $ current_voice = "voice/KYO05A_OKA0005.ogg"
    "伦太郎" "「关于我发生了什么等会和你讲！　但是在那之前先让我确认一下情况吧！　到底——发生了什么！」"
    "是被我的气势压倒了吗，红莉栖用一只手挠着脸颊说道。"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0009"
    $ current_voice = "voice/KYO05A_CRS0009.ogg"
    "红莉栖" "「虽然不知道发生了什么，但可以啊，告诉你就是了……在这几个小时发生了什么」"
    hide screen phoneSD1
    window hide

    stop bgm 






    play bgm "BGM19"
    hide screen phonebtn
    "根据红莉栖所说的，在这条世界线上的『１６点３分』我似乎收到了ｉｃｈｓ的恐吓信。"
    "然后，红莉栖去了柳林神社和琉华子见了面。"
    "琉华子说『真由理没有来过』。"
    "另一方面在那个时候，我在大楼前面的投币式保险柜附近侦查。"
    "但是没有见到ｉｃｈｓ的样子……"
    "然后这样那样以后就和红莉栖汇合了——"
    "不久在那里出现了手持铁棒的４℃。"
    window hide










    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0006"
    $ current_voice = "voice/KYO05A_OKA0006.ogg"
    "伦太郎" "「哈，你在说什么啊……。那不就是和最初的世界线一样了吗……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0010"
    $ current_voice = "voice/KYO05A_CRS0010.ogg"
    "红莉栖" "「最初的世界线……？　怎么说……？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我没有回答她的问题，而是取出了手机打开了收件箱。"
    window hide


    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH03"]


    "在那里确实有如红莉栖所受的恐吓信Ｄｍａｉｌ。"
    window hide




    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH02"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH01"]




    "不可能……！"
    "感到万分不解的我为了否认这个现实，继续寻找着其他证据。"
    "我又看了一遍收件箱。"
    window hide


    "注意到了一个无法理解的事实。"
    "没有……"
    "不管是『真由理的外出』『必须尽力阻止』的邮件……"
    "还是『评议会终止』『不要用火！』的邮件……"
    "消失了……消失了……为什么……？"
    "我茫然地将手机放回口袋。"
    window hide
    call hide_phone

    "感到指尖碰到了什么。"
    "试着取了出来。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG03A")



    hide screen phonebtn
    "是真由理的手机。"
    "虽然打开着，但是画面是暗的。"
    "长按电源键也没有反应……"
    "没电了，吗……"
    "而现在也没有办法给它充电……"
    window hide


    $ loadBG(2,"BG21E")



    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "没有办法，我只得把真由理的手机放回口袋，然后给桶子打了电话。"
    window hide

    call hide_phone


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "和红莉栖一样，我问了他这几个小时发生的事情。"
    "但是得到的答案和红莉栖给我的是一样的。"
    "『１６点３分』──我的手机收到了ｉｃｈｓ的恐吓信……。"
    "…………"
    "说完这一通后，桶子用颤动着身影说道。"
    $ stopvoc("DAR")
    play DAR "KYO05A_DAR0000"
    $ current_voice = "voice/KYO05A_DAR0000.ogg"
    "至" "「冈伦，到底怎么办……？　是时候报警了吧……」"
    "我告诉桶子暂时在Ｌａｂ待机，挂掉了电话。"

    stop bgm 
    window hide

    $ loadBG(0,"BG21E")

    show screen phonebtn
    show screen phoneSD1
    "真由理被诱拐了。"
    "真由理被诱拐了。"
    "真由理被诱拐了。"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0007"
    $ current_voice = "voice/KYO05A_OKA0007.ogg"
    "伦太郎" "「为什么……。怎么会……」"
    "有气无力的声音从嘴唇之间漏出。"
    "感觉失去了力气，我颓坐在地上。"
    hide screen phoneSD1
    window hide
    play se "SGSE080"



    $ loadBG(2,"BG_BLACK")





    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0011"
    $ current_voice = "voice/KYO05A_CRS0011.ogg"
    "红莉栖" "「等，等等冈部，没事吧！？　振作起来！」"
    "红莉栖从一侧扶住我，试图让我站起来。"
    "但是脚也好腰也好都使不上力气。"
    "我就跪在那里，静静地看着红莉栖。"
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC05"),"True","lh/CRS_ALC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    show screen phoneSD1
    "视线重合了。"
    "红莉栖那背后仿佛要融化一般的晚霞……"
    "红莉栖抱住了我的头，轻轻地在我耳边说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALA01"),"True","lh/CRS_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0012"
    $ current_voice = "voice/KYO05A_CRS0012.ogg"
    "红莉栖" "「没关系的，我会帮助你的……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0013"
    $ current_voice = "voice/KYO05A_CRS0013.ogg"
    "红莉栖" "「所以拜托了……。全部告诉我吧……？」"
    "我保持着将脸埋在红莉栖胸口的状态，慢慢地小声说了起来。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"IBGX072")

    hide screen phonebtn
    show screen phoneSD1
    "话说完的时候，天空中的红色已经消失了。"
    "被夜幕所笼罩的天空中，闪烁着千千万万颗星星。"
    "突然，想起了真由理的“与星屑握手(Ｓｔａｒｄｕｓｔ・Ｓｈａｋｅｈａｎｄ)”。"
    "那种伸出手去就好像能抓到星星的心情，我好像不知怎么地明白了。"
    window hide



    $ loadBG(2,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM07"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0014"
    $ current_voice = "voice/KYO05A_CRS0014.ogg"
    "红莉栖" "「那我从结论开始说吧。」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0015"
    $ current_voice = "voice/KYO05A_CRS0015.ogg"
    "红莉栖" "「你肯定是回到最先的那条世界线上来了哦。在最后的Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ发动的时候」"
    "红莉栖所说的话语超过了我的理解能力。"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0008"
    $ current_voice = "voice/KYO05A_OKA0008.ogg"
    "伦太郎" "「返回了……原来的世界线……？」"
    "我只能呆呆地重复着红莉栖的话。"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0016"
    $ current_voice = "voice/KYO05A_CRS0016.ogg"
    "红莉栖" "「总之为了方便起见，我们将你最先经历的世界线称为『第一世界线』，之后的世界线称为『第二世界线』，第三次经历的世界线称为『第三世界线』，ＯＫ吗？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0017"
    $ current_voice = "voice/KYO05A_CRS0017.ogg"
    "红莉栖" "「『第１世界线』上，从ｉｃｈｓ那里收到了恐吓信」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG79N6",at=[Transform(yalign=0.5)])






    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0018"
    $ current_voice = "voice/KYO05A_CRS0018.ogg"
    "红莉栖" "「『第２世界线』上，Ｌａｂ发生了火灾」"
    window hide


    $ loadBG(0,"BG02N4")

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0019"
    $ current_voice = "voice/KYO05A_CRS0019.ogg"
    "红莉栖" "「『第３世界线』上，Ｌａｂ里有血迹的残留。……到这里为止ＯＫ吗？」"
    window hide


    $ loadBG(0,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    "我笨拙地点了点头。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"PBG16D")

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0020"
    $ current_voice = "voice/KYO05A_CRS0020.ogg"
    "红莉栖" "「首先，你在『第１世界线』发送了『真由理的外出／绝对要阻止她』的Ｄｍａｉｌ，于是来到了『第２世界线』」"
    window hide


    $ loadBG(0,"BG03A4")
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    $ targetmailid = gc["ScriptMacros"]["FM_KYO02B_SEND_FG801"]



    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0021"
    $ current_voice = "voice/KYO05A_CRS0021.ogg"
    "红莉栖" "「然后在『第２世界线』发送了『评议会已终止／不要使用火！』的Ｄｍａｉｌ，于是移动了『第３世界线』─」"
    window hide

    call hide_phone

    $ loadBG(0,"BG02N4")

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0022"
    $ current_voice = "voice/KYO05A_CRS0022.ogg"
    "红莉栖" "「在那里看到血迹的你，向着相同的『第３世界线』的过去的『１７时４０分』进行了时间跳跃──」"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002B"]]["Check"]=True
    $ loadBG(0,"EV_KYO002B")

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0023"
    $ current_voice = "voice/KYO05A_CRS0023.ogg"
    "红莉栖" "「在Ｌａｂ的时候你和真由理被黑斗篷的家伙们包围了，于是受到你求助的我向『１８点１８分』发送了Ｄｍａｉｌ……吧？」"
    window hide


    $ loadBG(0,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0024"
    $ current_voice = "voice/KYO05A_CRS0024.ogg"
    "红莉栖" "「然后，作为结果，就是你回到了现在所在的『第１世界线』。……明白了吗？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0009"
    $ current_voice = "voice/KYO05A_OKA0009.ogg"
    "伦太郎" "「理解……怎么可能吗！　难道不是很奇怪吗！」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0025"
    $ current_voice = "voice/KYO05A_CRS0025.ogg"
    "红莉栖" "「什么很奇怪？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0010"
    $ current_voice = "voice/KYO05A_OKA0010.ogg"
    "伦太郎" "「如果这里是『第１世界线』的话，为什么我和你还会存在啊！」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0011"
    $ current_voice = "voice/KYO05A_OKA0011.ogg"
    "伦太郎" "「不对，不光是我们！这个世界上所有的人，还有动植物，包括所有的物质以及一切东西，都不应该存在与此啊！」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0026"
    $ current_voice = "voice/KYO05A_CRS0026.ogg"
    "红莉栖" "「为什么？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0012"
    $ current_voice = "voice/KYO05A_OKA0012.ogg"
    "伦太郎" "「因为我在『第１世界线』发送了『真由理的外出／绝对要阻止她』的Ｄｍａｉｌ啊！」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0013"
    $ current_voice = "voice/KYO05A_OKA0013.ogg"
    "伦太郎" "「作为结果，就是世界的历史向着『第２世界线』进行了再构成！　所以──」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0027"
    $ current_voice = "voice/KYO05A_CRS0027.ogg"
    "红莉栖" "「如果你没有发送呢？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0014"
    $ current_voice = "voice/KYO05A_OKA0014.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0028"
    $ current_voice = "voice/KYO05A_CRS0028.ogg"
    "红莉栖" "「…………」"

    stop bgm 
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0015"
    $ current_voice = "voice/KYO05A_OKA0015.ogg"
    "伦太郎" "「什么……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0029"
    $ current_voice = "voice/KYO05A_CRS0029.ogg"
    "红莉栖" "「所以，你没有发哟，那封Ｄｍａｉｌ」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0030"
    $ current_voice = "voice/KYO05A_CRS0030.ogg"
    "红莉栖" "「虽然你可能在最初经历的那个『第１世界线』上发送了，但是在这条『第１世界线』并没有发送」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0016"
    $ current_voice = "voice/KYO05A_OKA0016.ogg"
    "伦太郎" "「希望用日语来说明」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0031"
    $ current_voice = "voice/KYO05A_CRS0031.ogg"
    "红莉栖" "「我就是用日语说的」"
    "不明白什么意思……"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我取出手机，确认了邮件的发送历史。"
    "不是收件箱，而是发件箱，然后……"
    window hide


    play bgm "BGM20"
    "没有……没有了。"
    "原本我在『第１世界线』上应该发送过的『真由理的外出／绝对要阻止她』的邮件的发送记录……"
    "只有在Ｌａｂ里向ｉｃｈｓ发的那个『有话要说』的邮件。"
    "诶……？等等……"
    "不如说，这样不是挺好的吗……？"
    "没有发送过那封邮件，就意味着这里不是『第１世界线』了！"
    window hide
    call hide_phone

    "我将刚刚想到的事情告诉了红莉栖。"
    "这么说了以后，红莉栖意外爽快地承认了自己的错误。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0032"
    $ current_voice = "voice/KYO05A_CRS0032.ogg"
    "红莉栖" "「是呢，确实刚才说的方法有点不太合适。」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0033"
    $ current_voice = "voice/KYO05A_CRS0033.ogg"
    "红莉栖" "「那么我们重新说一次」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0034"
    $ current_voice = "voice/KYO05A_CRS0034.ogg"
    "红莉栖" "「你移动到了，和你最初经历的『第１世界线』无限接近的世界线上。……这么说行吗？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0017"
    $ current_voice = "voice/KYO05A_OKA0017.ogg"
    "伦太郎" "「什么呀，那什么『无限接近的世界线』……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0035"
    $ current_voice = "voice/KYO05A_CRS0035.ogg"
    "红莉栖" "「总之先叫它『近似第１世界线』吧」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0036"
    $ current_voice = "voice/KYO05A_CRS0036.ogg"
    "红莉栖" "「『第１世界线』和『近似第１世界线』只有一个区别——『真由理的外出／必须阻止下来』的Ｄｍａｉｌ是否发送了」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0037"
    $ current_voice = "voice/KYO05A_CRS0037.ogg"
    "红莉栖" "「除了那点以外一切都是一样的，这么考虑也可以。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0038"
    $ current_voice = "voice/KYO05A_CRS0038.ogg"
    "红莉栖" "「说到底，也只是假设呢。从我的立场来看，无法验证这到底是对的还是错的，从原理上来说」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0039"
    $ current_voice = "voice/KYO05A_CRS0039.ogg"
    "红莉栖" "「但是这条世界线上只有一个人，能够说出这到底是不是正确的。那个人不用说就是──」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0040"
    $ current_voice = "voice/KYO05A_CRS0040.ogg"
    "红莉栖" "「冈部伦太郎──你哦」"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "『近似第１世界线』──。"
    "和我最初经历的『第１世界线』无限接近的世界线……"
    "从情况来考虑，确实红莉栖所说的都是对的。"
    "那样的话，果然真由理……"
    window hide



    $ loadBG(2,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0018"
    $ current_voice = "voice/KYO05A_OKA0018.ogg"
    "伦太郎" "「呐，告诉我把……。为什么我会回到这条『近似第１世界线』上来呢……？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0041"
    $ current_voice = "voice/KYO05A_CRS0041.ogg"
    "红莉栖" "「呼，这问题有点难啊……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0042"
    $ current_voice = "voice/KYO05A_CRS0042.ogg"
    "红莉栖" "「『第３世界线』上我发送过来的Ｄｍａｉｌ——我认为那是解决这一切问题的关键所在……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0019"
    $ current_voice = "voice/KYO05A_OKA0019.ogg"
    "伦太郎" "「是啊，那个时候你到底发送了怎样的Ｄｍａｉｌ啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0043"
    $ current_voice = "voice/KYO05A_CRS0043.ogg"
    "红莉栖" "「谁知道呢……？你问这『近似第１世界线』上的我也没用啊……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0020"
    $ current_voice = "voice/KYO05A_OKA0020.ogg"
    "伦太郎" "「说起来你在让我设定电话微波炉（暂）的时候还让我等了３分钟？　那个时候你去干什么了？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0044"
    $ current_voice = "voice/KYO05A_CRS0044.ogg"
    "红莉栖" "「所以说问我我也不知道啊」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0021"
    $ current_voice = "voice/KYO05A_OKA0021.ogg"
    "伦太郎" "「那在发送之前那个时间点，为什么将Ｄｍａｉｌ的收件人从我改成了真由理？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0045"
    $ current_voice = "voice/KYO05A_CRS0045.ogg"
    "红莉栖" "「不知道啊，那种事……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0022"
    $ current_voice = "voice/KYO05A_OKA0022.ogg"
    "伦太郎" "「那时间方面是为什么？为啥要发送到三小时前？」"
    "Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ发动的时间是『１８点１８分』，３小时前也就是『１５点１８分』……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0046"
    $ current_voice = "voice/KYO05A_CRS0046.ogg"
    "红莉栖" "「啊啊，如果是这个问题的话，或许没什么不能理解的」"
    "红莉栖将手伸进了口袋里说道。"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0047"
    $ current_voice = "voice/KYO05A_CRS0047.ogg"
    "红莉栖" "「大概是『第３世界线』的我、想让坏掉的手机复原吧」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0048"
    $ current_voice = "voice/KYO05A_CRS0048.ogg"
    "红莉栖" "「Ｄｍａｉｌ发送到的时间是『１５点１８分』──」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0049"
    $ current_voice = "voice/KYO05A_CRS0049.ogg"
    "红莉栖" "「冈部的手机收到『评议会已终止』的Ｄｍａｉｌ是『１５点２２分』，所以是在那个４分钟之前呢」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0050"
    $ current_voice = "voice/KYO05A_CRS0050.ogg"
    "红莉栖" "「也就是发送到收到『评议会已终止』的时间点之前，那样的话──」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0023"
    $ current_voice = "voice/KYO05A_OKA0023.ogg"
    "伦太郎" "「认为就能让『评议会已终止』这封Ｄｍａｉｌ消失吧……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0024"
    $ current_voice = "voice/KYO05A_OKA0024.ogg"
    "伦太郎" "「这样的话，你去网咖的历史就会被消灭，然后手机就获救了……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0051"
    $ current_voice = "voice/KYO05A_CRS0051.ogg"
    "红莉栖" "「然后事实上『评议会已终止』Ｄｍａｉｌ的邮件确实消失了，于是我就这样──」"
    "红莉栖摇着她拿出来的手机。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0052"
    $ current_voice = "voice/KYO05A_CRS0052.ogg"
    "红莉栖" "「成功地救到了自己的手机」"
    window hide



    $ loadBG(2,"IBGX072")

    stop bgm 



    hide screen phonebtn
    "我抬起头。"
    "感觉和刚才相比星星的数量增加了。"
    "就算如此还是没有办法用手摸到星星。"
    "不管多么用力地伸手，也是捉不到星星的。"
    "开始焦躁起来。"
    "白白地浪费了时间。"
    "在大楼附近的街道充斥着喧嚣。"
    "我被年轻人开朗的笑声搞得更加不爽了。"
    window hide



    $ loadBG(2,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0053"
    $ current_voice = "voice/KYO05A_CRS0053.ogg"
    "红莉栖" "「呐，有一件很想和你说的事情，可以说嘛？」"
    "突然红莉栖说道。稍稍皱着眉头……"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0054"
    $ current_voice = "voice/KYO05A_CRS0054.ogg"
    "红莉栖" "「『第３世界线』上真由理说的──是谎话。」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0025"
    $ current_voice = "voice/KYO05A_OKA0025.ogg"
    "伦太郎" "「谎话……？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0055"
    $ current_voice = "voice/KYO05A_CRS0055.ogg"
    "红莉栖" "「她不是说彩票中奖了吗？但那是谎话哦」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0056"
    $ current_voice = "voice/KYO05A_CRS0056.ogg"
    "红莉栖" "「虽然本人以为没有暴露，但是我和桥田是知道的哦。然后几个小时前的冈部也是」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0026"
    $ current_voice = "voice/KYO05A_OKA0026.ogg"
    "伦太郎" "「这是怎么回事……？」"
    play bgm "BGM31"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0057"
    $ current_voice = "voice/KYO05A_CRS0057.ogg"
    "红莉栖" "「３００万日元──实际上，是真由理将她最珍惜的宝物拿到当铺里换到的」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0058"
    $ current_voice = "voice/KYO05A_CRS0058.ogg"
    "红莉栖" "「但是如果直接说出那样的事情的话，肯定会让大家担心的，她肯定是这么想的」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0059"
    $ current_voice = "voice/KYO05A_CRS0059.ogg"
    "红莉栖" "「恩，担心了以后她觉得冈部会说『不能用那样的钱！　现在马上去当铺里还了吧！』」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0060"
    $ current_voice = "voice/KYO05A_CRS0060.ogg"
    "红莉栖" "「所以真由理就说了那样一个谎……」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0027"
    $ current_voice = "voice/KYO05A_OKA0027.ogg"
    "伦太郎" "「那个，非常珍惜的宝物是……什么啊？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0061"
    $ current_voice = "voice/KYO05A_CRS0061.ogg"
    "红莉栖" "「怀表。好像叫『怀酱～』的样子……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")
    $ loadBG(2,"IBGX090",png=True)








    hide screen phonebtn
    "这什么呀……"
    "『怀酱～』是，真由理已经不在的婆婆的遗物……"
    "对于真由理来说无可替代的宝物……"
    "这一点我比谁都要更清楚。"
    window hide


    $ loadBG(0,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0028"
    $ current_voice = "voice/KYO05A_OKA0028.ogg"
    "伦太郎" "「克里斯提娜，那个当铺在哪里！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0062"
    $ current_voice = "voice/KYO05A_CRS0062.ogg"
    "红莉栖" "「诶……？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0029"
    $ current_voice = "voice/KYO05A_OKA0029.ogg"
    "伦太郎" "「我在问你当铺的名字和位置！　现在马上就去取回来！」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0063"
    $ current_voice = "voice/KYO05A_CRS0063.ogg"
    "红莉栖" "「已经去过了哟」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0030"
    $ current_voice = "voice/KYO05A_OKA0030.ogg"
    "伦太郎" "「什么……？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0064"
    $ current_voice = "voice/KYO05A_CRS0064.ogg"
    "红莉栖" "「已经去过了啊，昨天，冈部一个人……。准备了３００万日元以后……」"
    "连起来了，连起来了啊……"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0031"
    $ current_voice = "voice/KYO05A_OKA0031.ogg"
    "伦太郎" "「因为那个我才会向门音（カドネ）信贩金融会社借了钱啊……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0065"
    $ current_voice = "voice/KYO05A_CRS0065.ogg"
    "红莉栖" "「门音？　……啊啊，是门音（モンド）信贩啊」"
    "好像是门音读作モンド的样子。"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0032"
    $ current_voice = "voice/KYO05A_OKA0032.ogg"
    "伦太郎" "「那么果然是已经安全地取回了『怀酱』了吗？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0066"
    $ current_voice = "voice/KYO05A_CRS0066.ogg"
    "红莉栖" "「那个……冈部，你两手空空地回来了哦」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0033"
    $ current_voice = "voice/KYO05A_OKA0033.ogg"
    "伦太郎" "「为什么啊……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0067"
    $ current_voice = "voice/KYO05A_CRS0067.ogg"
    "红莉栖" "「那是我想问的啊。发生了什么？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0034"
    $ current_voice = "voice/KYO05A_OKA0034.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0068"
    $ current_voice = "voice/KYO05A_CRS0068.ogg"
    "红莉栖" "「啊啊顺便一提，那个借款是不需要还的了」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RISOKU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RISOKU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RISOKU"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHUSSHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHUSSHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHUSSHI"])

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GANPON"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GANPON"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GANPON"])

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0069"
    $ current_voice = "voice/KYO05A_CRS0069.ogg"
    "红莉栖" "「因为违反了{color=#f00}利息制限法{/color}以及{color=#f00}出资法{/color}，连{color=#f00}本钱{/color}都不需要还」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0070"
    $ current_voice = "voice/KYO05A_CRS0070.ogg"
    "红莉栖" "「因为拜托了一个认识的律师，所以注意到了这一点，不用担心了哦？」"
    "就算你不说我也不是很在意。"
    "怎样都好了，那种事情。"
    "但是真由理的心情……仿佛传进了我的心里。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"EVX_M06A")

    hide screen phonebtn
    "那家伙竟然将比什么都重要，甚至比生命都重要的宝物去典当了。"
    "为了什么……？"
    "为了Ｌａｂ啊！为了我们未来道具研究所的光明未来啊。"
    window hide


    $ loadBG(0,"IBG024A")

    "恐怕一个月之前的我，看到了传单，然后高声宣布道『我们参加秋叶原发明大赛吧！』。"
    "同时『未来道具魔改造计划』开始——"
    "但是因为资金不足，所以无法按照想要的方式改良……"
    "然后真由理在一边看到了因此抱着头的我和桶子的身影。"
    "马上就理解了。"
    "所以那家伙才会说自己中了奖……"
    window hide



    $ loadBG(0,"EVX_M06A")

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0071"
    $ current_voice = "voice/KYO05A_CRS0071.ogg"
    "红莉栖" "「真由理，好像相信过哦？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0072"
    $ current_voice = "voice/KYO05A_CRS0072.ogg"
    "红莉栖" "「不对，现在还相信着呢。我们能在秋叶原发明大赛上面得到大奖……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0073"
    $ current_voice = "voice/KYO05A_CRS0073.ogg"
    "红莉栖" "「因为，和我说的时候，她说过……」"
    $ stopvoc("MAY")
    play MAY "KYO05A_MAY0000"
    $ current_voice = "voice/KYO05A_MAY0000.ogg"
    "真由理" "「小冈伦做的道具真的超厉害哦！真的真的非常优秀的说」"
    $ stopvoc("MAY")
    play MAY "KYO05A_MAY0001"
    $ current_voice = "voice/KYO05A_MAY0001.ogg"
    "真由理" "「如果加上克里斯酱的帮助的话，已经是最强的了！绝对会得大奖的哦！」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0074"
    $ current_voice = "voice/KYO05A_CRS0074.ogg"
    "红莉栖" "「所以就算『怀酱』拿去典当了都没有不安」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0075"
    $ current_voice = "voice/KYO05A_CRS0075.ogg"
    "红莉栖" "「大赛的大奖奖金也是３００万──」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0076"
    $ current_voice = "voice/KYO05A_CRS0076.ogg"
    "红莉栖" "「用那笔钱肯定能把表赎回来的，她一定这么坚信着吧」"
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    hide screen phoneSD1
    "我闭着眼睛，咬牙切齿。"
    "紧握双手，肩膀不住震动。"
    "真由理相信着我，为了我们的未来，赌上了她自己最重要的宝物。"
    "但是那样的真由理现在，却不在我们身边。"
    "说不定一个人在哪里寂寞地哭着。"
    "如果那样的话——"
    "如果那样的话，现在，我们要做的事只有一件！"
    window hide

    stop bgm 

    $ loadBG(0,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    "我睁开眼睛静静地说道。"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0035"
    $ current_voice = "voice/KYO05A_OKA0035.ogg"
    "伦太郎" "「克里斯提娜，发Ｄｍａｉｌ吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM11"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0077"
    $ current_voice = "voice/KYO05A_CRS0077.ogg"
    "红莉栖" "「我就知道你会这么说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0078"
    $ current_voice = "voice/KYO05A_CRS0078.ogg"
    "红莉栖" "「但那样的话我有个主意。能交给我吗？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0036"
    $ current_voice = "voice/KYO05A_OKA0036.ogg"
    "伦太郎" "「不行。交给『第３世界线』的你之后，现在变成这样了」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0079"
    $ current_voice = "voice/KYO05A_CRS0079.ogg"
    "红莉栖" "「这条世界线的我不会犯这种错啦」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0037"
    $ current_voice = "voice/KYO05A_OKA0037.ogg"
    "伦太郎" "「不都是牧濑红莉栖吗」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0080"
    $ current_voice = "voice/KYO05A_CRS0080.ogg"
    "红莉栖" "「但是，肯定没关系」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0038"
    $ current_voice = "voice/KYO05A_OKA0038.ogg"
    "伦太郎" "「到底会怎样呢……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0081"
    $ current_voice = "voice/KYO05A_CRS0081.ogg"
    "红莉栖" "「内容我也会告诉你的」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0039"
    $ current_voice = "voice/KYO05A_OKA0039.ogg"
    "伦太郎" "「打算发什么？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0082"
    $ current_voice = "voice/KYO05A_CRS0082.ogg"
    "红莉栖" "「之前的『第１世界线』上发了Ｄｍａｉｌ之后，真由理留在了Ｌａｂ了吧？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0083"
    $ current_voice = "voice/KYO05A_CRS0083.ogg"
    "红莉栖" "「那样的话『第２世界线』的Ｌａｂ就会发生火灾……」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0084"
    $ current_voice = "voice/KYO05A_CRS0084.ogg"
    "红莉栖" "「那样的话只能放真由理出去了啊」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0040"
    $ current_voice = "voice/KYO05A_OKA0040.ogg"
    "伦太郎" "「放她出去？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0085"
    $ current_voice = "voice/KYO05A_CRS0085.ogg"
    "红莉栖" "「尾行她来抓住诱拐犯啊。这样就全部解决了。」"
    "这么说着的红莉栖取出了手机，开始输入文字。"
    "突然她的手指停了下来。"
    "朝着这边的话面上，显示着这样的内容。"
    window hide


    $ loadBG(2,"PBG18A")



    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0041"
    $ current_voice = "voice/KYO05A_OKA0041.ogg"
    "伦太郎" "「想到了啊。眉毛的眉加上片假名リ就是真由理了啊」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0086"
    $ current_voice = "voice/KYO05A_CRS0086.ogg"
    "红莉栖" "「如果用平假名的话文字数量不就超了么？」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0042"
    $ current_voice = "voice/KYO05A_OKA0042.ogg"
    "伦太郎" "「问题是，过去的我能不能理解呢……」"
    window hide



    $ loadBG(2,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0087"
    $ current_voice = "voice/KYO05A_CRS0087.ogg"
    "红莉栖" "「放心吧，发送到的是我的手机」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0043"
    $ current_voice = "voice/KYO05A_OKA0043.ogg"
    "伦太郎" "「等等，那么做有什么理由吗？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0088"
    $ current_voice = "voice/KYO05A_CRS0088.ogg"
    "红莉栖" "「现在这里来说，对于下一条世界线不就像是蚊帐的外面吗？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0089"
    $ current_voice = "voice/KYO05A_CRS0089.ogg"
    "红莉栖" "「我也要帮忙。我想帮你。还因为，这个作战一个人太危险了」"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0044"
    $ current_voice = "voice/KYO05A_OKA0044.ogg"
    "伦太郎" "「发送到的时间是？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0090"
    $ current_voice = "voice/KYO05A_CRS0090.ogg"
    "红莉栖" "「那个……」"
    "红莉栖看了一眼手表说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0091"
    $ current_voice = "voice/KYO05A_CRS0091.ogg"
    "红莉栖" "「４小时前──『２４０分前』怎么样？」"
    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0092"
    $ current_voice = "voice/KYO05A_CRS0092.ogg"
    "红莉栖" "「现在时间是『１９点２１分』，所以４小时之前的话，真由理不是肯定会在Ｌａｂ里嘛」"
    "不知何时，完全按照红莉栖的步调走了。"
    "注意到的我做出了肯定的答复。"
    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0045"
    $ current_voice = "voice/KYO05A_OKA0045.ogg"
    "伦太郎" "「好啊」"
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "已经变成这样的话就无路可退了。"
    "我给桶子打了个电话，将刚刚想好的要求告诉他，让他设定好了电话微波炉。"
    "然后过了一会……"

    window hide


    $ loadBG(0,"BG21N")
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    show screen phoneSD1

    $ stopvoc("DAR")
    play DAR "KYO05A_DAR0001"
    $ current_voice = "voice/KYO05A_DAR0001.ogg"
    "至" "「冈伦，准备好了哦！」"

    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0046"
    $ current_voice = "voice/KYO05A_OKA0046.ogg"
    "伦太郎" "「好的，桶子！　启动电话微波炉（暂）！」"
    "…………"

    $ stopvoc("DAR")
    play DAR "KYO05A_DAR0002"
    $ current_voice = "voice/KYO05A_DAR0002.ogg"
    "至" "「放电现象来了啊！」"

    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "KYO05A_OKA0047"
    $ current_voice = "voice/KYO05A_OKA0047.ogg"
    "伦太郎" "「克里斯缇娜，就是现在！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO05A_CRS0093"
    $ current_voice = "voice/KYO05A_CRS0093.ogg"
    "红莉栖" "「了解！」"
    "就这么回答了一句，红莉栖按下了——手机的发送按钮。"

    hide screen phoneSD1
    call hide_phone



    stop bgm 



    $ loadBG(2,"BG_BLACK")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_04A.avi")
    hide screen invisible









    return
