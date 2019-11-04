label SGFD2_OKA03A:


    window hide


    $ loadBG(0,"BG05A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = cml.setdefault("RM_OKA1_SEND_SUZ01","")

    $ LR_RM_CHANCE=0
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




    $ date="8/11"
    show screen phoneSD1
    python:
        cml = {}
        while len(rml)>0 and rml[0]["MetaData"]["Time"] > 814 and rml[0]["MetaData"]["Date"] == 811:
            UnreadMail(rml[0]["MailNumber"])
            notLate(rml[0]["MailNumber"])
            del rml[0]
        while len(sml)>0 and sml[0]["MetaData"]["Time"] > 814 and sml[0]["MetaData"]["Date"] == 811:
            del sml[0]
        while len(sml)>0 and gc["MailData"][lml[0]]["MetaData"]["Time"] > 814 and gc["MailData"][lml[0]]["MetaData"]["Date"] == 811:
            notLate(lml[0])
            del lml[0]
        UnreadMail(317)
        notLate(317)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0000"
    $ current_voice = "voice/OKA03A_TEN0000.ogg"
    "天王寺" "「可恶！　要不是必须去外面办点事，我肯定会好好陪你们去的啊……」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0001"
    $ current_voice = "voice/OKA03A_TEN0001.ogg"
    "天王寺" "「冈部，给我听好了！　你要是敢让绹哭的话，我一定不会放过你的！　从头到尾都要照顾好她哦！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0002"
    $ current_voice = "voice/OKA03A_TEN0002.ogg"
    "天王寺" "「冈部？　喂！　在听吗！？　现在不是打电话的时──」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0000"
    $ current_voice = "voice/OKA03A_OKA0000.ogg"
    "伦太郎" "「呼！」"
    window hide
    call hide_phone
    show screen phonebtn




    play bgm "FD2BGM01"

    "将手机从耳旁移开，我露出了微笑。"
    "虽然头还有些晕，不过时间跳跃平安无事地成功了。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0001"
    $ current_voice = "voice/OKA03A_OKA0001.ogg"
    "伦太郎" "「既然我已经回到了这里，绝不会让恶人的阴谋得逞！」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0000"
    $ current_voice = "voice/OKA03A_NAE0000.ogg"
    "绹" "「诶？？？」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0003"
    $ current_voice = "voice/OKA03A_TEN0003.ogg"
    "天王寺" "「喂，喂冈部。脑袋被热坏了吗？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0002"
    $ current_voice = "voice/OKA03A_OKA0002.ogg"
    "伦太郎" "「走吧，小动物！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0001"
    $ current_voice = "voice/OKA03A_NAE0001.ogg"
    "绹" "「好……好的」"
    "我牵起不安地点着头的绹的手，朝着友都八喜走去。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]]["late"]=True

    hide screen phoneSD1
    window hide




    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ01","")

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""


    $ loadBG(0,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0002"
    $ current_voice = "voice/OKA03A_NAE0002.ogg"
    "绹" "「真的能买到吗？」"
    "和以前一样，以「雷ＮｅｔＡＢ３Ｄ」为目标的人群排成了长龙。"
    "我们的前方，依旧是之前的４℃的伙伴。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0003"
    $ current_voice = "voice/OKA03A_OKA0003.ogg"
    "伦太郎" "「我稍微走开一下」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0003"
    $ current_voice = "voice/OKA03A_NAE0003.ogg"
    "绹" "「诶？　去哪里？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0004"
    $ current_voice = "voice/OKA03A_OKA0004.ogg"
    "伦太郎" "「厕所。等一下马上回来」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0004"
    $ current_voice = "voice/OKA03A_NAE0004.ogg"
    "绹" "「冈伦叔叔？　最近的厕所在那里──」"

    stop bgm 
    "没有理会绹的话，我从队伍中离开了。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG22B0")

    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ02","")

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE



    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"])


    show screen phoneSD1
    "秋叶原对我来说就是我的故乡。"
    "为了能作为羊驼人展开行动，我对于能够掩人耳目变身的场所也做过一番调查。"
    window hide


    $ loadBG(2,"BG32A")



    "在这附近的话，人流量比起中央地段会少很多。"
    "只要躲在道路的阴影里，就能够安心地变身为羊驼人。"
    window hide
    $ loadBG(0,"IBG017A",png=True,hold=True)
    with moveinbottom


    "我从白衣的内侧拿出藏好的羊驼面具──"
    window hide
    hide background-png 
    with moveoutbottom


    hide screen phoneSD1
    hide phonebtn 

    $ loadBG(0,"IBG019A",png=True,trans=moveintop,hide=False)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    hide background-png 
    with dissolve




    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0000"
    $ current_voice = "voice/OKA03A_MAY0000.ogg"
    "真由理" "「冈伦。买来了哟」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0005"
    $ current_voice = "voice/OKA03A_OKA0005.ogg"
    "伦太郎" "「别用这个名字叫我！　现在我不是冈部伦太郎」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0006"
    $ current_voice = "voice/OKA03A_OKA0006.ogg"
    "伦太郎" "「而是天在呼唤，地在呼唤，安第斯也在呼唤的！　秋叶原中诞生的神秘英雄！　羊驼人！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0001"
    $ current_voice = "voice/OKA03A_MAY0001.ogg"
    "真由理" "「哦哦！」"
    "不知为何一次又一次感到吃惊的同时，真由理将罗森的购物袋递给我。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0002"
    $ current_voice = "voice/OKA03A_MAY0002.ogg"
    "真由理" "「这是献给羊驼人的供品哦」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0007"
    $ current_voice = "voice/OKA03A_OKA0007.ogg"
    "伦太郎" "「嗯。做得好真由理」"
    "我从购物袋里取出了事先准备好的注射器。"
    "里面装满了会被人误认为是血的鲜红色液体。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0008"
    $ current_voice = "voice/OKA03A_OKA0008.ogg"
    "伦太郎" "「之后就要用这个羊驼七道具( Seven gear )，『Ｓａｌｓａ・Ｄｒａｓｔｉｃ』──」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0009"
    $ current_voice = "voice/OKA03A_OKA0009.ogg"
    "伦太郎" "「让那个叫４℃的家伙，知道我的厉害！　呼唔哈哈哈！」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phoneSD1
    play bgm "FD2BGM02"

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0000"
    $ current_voice = "voice/OKA03A_SDO0000.ogg"
    "４℃" "「喂，大家！」"
    $ stopvoc("Y06")
    play voc "OKA03A_Y060000"
    $ current_voice = "voice/OKA03A_Y060000.ogg"
    "４℃的伙伴Ａ" "「哦，４℃。今天也是最棒的堕天使呢」"
    $ stopvoc("Y07")
    play voc "OKA03A_Y070000"
    $ current_voice = "voice/OKA03A_Y070000.ogg"
    "４℃的伙伴Ｂ" "「啊啊，人间的堕天使」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0001"
    $ current_voice = "voice/OKA03A_SDO0001.ogg"
    "４℃" "「哼。溢出来的灵力没办法隐藏啊……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0005"
    $ current_voice = "voice/OKA03A_NAE0005.ogg"
    "绹" "「那，那个……」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0002"
    $ current_voice = "voice/OKA03A_SDO0002.ogg"
    "４℃" "「啊啊，小姑娘。不好意思,１０年之后再来找我吧──」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0006"
    $ current_voice = "voice/OKA03A_NAE0006.ogg"
    "绹" "「喂……为什么要插队呢？」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0003"
    $ current_voice = "voice/OKA03A_SDO0003.ogg"
    "４℃" "「……Ｗｈｙ？」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0004"
    $ current_voice = "voice/OKA03A_SDO0004.ogg"
    "４℃" "「喂，刚才，你说我插队了？」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0007"
    $ current_voice = "voice/OKA03A_NAE0007.ogg"
    "绹" "「诶，那个，嗯……」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0005"
    $ current_voice = "voice/OKA03A_SDO0005.ogg"
    "４℃" "「因为是小孩子所以就得意忘形了吗？　好吧，就让我来教你一些好东西吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0006"
    $ current_voice = "voice/OKA03A_SDO0006.ogg"
    "４℃" "「老虎，就算是在狩猎兔子的时候也是会拼尽全力的……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0008"
    $ current_voice = "voice/OKA03A_NAE0008.ogg"
    "绹" "「吓──」"
    "４℃朝着稚气未脱的绹逼近着。"
    "跟在他后面的两个人（暂时叫他们５℃和６℃）也缩短了距离。"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0007"
    $ current_voice = "voice/OKA03A_SDO0007.ogg"
    "４℃" "「怎么了可爱的小白兔？　不快点道歉的话就会发生不得了的事情了不是吗？」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0009"
    $ current_voice = "voice/OKA03A_NAE0009.ogg"
    "绹" "「诶，不要，那个……」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0008"
    $ current_voice = "voice/OKA03A_SDO0008.ogg"
    "４℃" "「啊啊～嗯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0010"
    $ current_voice = "voice/OKA03A_NAE0010.ogg"
    "绹" "「那，那个……吓」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0009"
    $ current_voice = "voice/OKA03A_SDO0009.ogg"
    "４℃" "「啊啊啊啊啊啊啊～～～～嗯？」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0011"
    $ current_voice = "voice/OKA03A_NAE0011.ogg"
    "绹" "「吸呜，呜，呜呜呜呜────！！」"
    "在眼看着绹将要掉下眼泪之际──"
    stop bgm 
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0010"
    $ current_voice = "voice/OKA03A_OKA0010.ogg"
    "伦太郎" "「别哭，小动物哟！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0012"
    $ current_voice = "voice/OKA03A_NAE0012.ogg"
    "绹" "「诶？」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0010"
    $ current_voice = "voice/OKA03A_SDO0010.ogg"
    "４℃" "「怎么了？」"
    "队伍里的视线，一齐聚集在我身上。"
    "我回应着大家的期待，从台阶上飞落下来！"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0011"
    $ current_voice = "voice/OKA03A_OKA0011.ogg"
    "伦太郎" "「咚！！」"
    hide screen phoneSD1
    window hide

    show screen phoneSD1
    play bgm "FD2BGM03"
    "我已着陆──！"
    "从２楼的跳跃＆落地──是英雄的扎实训练得到回报的瞬间。"
    "之前练过无数遍真是太好了……"
    window hide

    hide lh6 
    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0011"
    $ current_voice = "voice/OKA03A_SDO0011.ogg"
    "４℃" "「你……你要干什么，你这家伙！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0012"
    $ current_voice = "voice/OKA03A_OKA0012.ogg"
    "伦太郎" "「我吗？　我的名字是──」"
    hide screen phoneSD1
    hide lh5 
    window hide
    play se "SGSE347"

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001A"]]["Check"]=True
    show EVOKA001A_BG1 
    show EVOKA001A_FACE_R 

    hide screen phonebtn
    with Fade(0.1,0.1,0.1,color="fff")
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0013"
    $ current_voice = "voice/OKA03A_OKA0013.ogg"
    "伦太郎" "「天在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001B"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG1 
    hide EVOKA001A_FACE_R 
    show EVOKA001A_BG2 
    show EVOKA001A_FACE_L 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA03A_OKA0014"
    $ current_voice = "voice/OKA03A_OKA0014.ogg"
    "伦太郎" "「地在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001C"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG2 
    hide EVOKA001A_FACE_L 
    show EVOKA001A_BG3 
    show EVOKA001A_FACE_C 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA03A_OKA0015"
    $ current_voice = "voice/OKA03A_OKA0015.ogg"
    "伦太郎" "「安第斯在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001D"]]["Check"]=True

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0016"
    hide EVOKA001A_BG3 
    hide EVOKA001A_FACE_C 
    show EVOKA001A_BG4 
    show EVOKA001A_FACE_H 
    with Fade(0.1,0.1,0.1,color="fff")
    $ current_voice = "voice/OKA03A_OKA0016.ogg"
    "伦太郎" "「秋叶原中诞生的神秘英雄！」"
    window hide







    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001E"]]["Check"]=True






    $ stopvoc("OKA")
    hide EVOKA001A_FACE_H 
    show EVOKA001A_HAND 
    show EVOKA001A_FACE 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA03A_OKA0017"
    $ current_voice = "voice/OKA03A_OKA0017.ogg"
    "伦太郎" "「羊驼人，登场！」"


    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0013"
    $ current_voice = "voice/OKA03A_NAE0013.ogg"
    "绹" "「羊驼人！　真的有啊……」"
    "守护和平的正义伙伴，羊驼人。"
    "作为秋叶原的英雄活跃的我，在当地人之间无人不晓。"
    window hide







    hide EVOKA001A_HAND 
    hide EVOKA001A_BG4 
    hide EVOKA001A_FACE 
    $ loadBG(2,"BG14A",hold=True)
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)























    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0018"
    $ current_voice = "voice/OKA03A_OKA0018.ogg"
    "伦太郎" "「你在队伍里面插队，事情暴露之后还威胁年龄这么小的小动物，真是罪大恶极！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0019"
    $ current_voice = "voice/OKA03A_OKA0019.ogg"
    "伦太郎" "「就让你尝尝羊驼人的厉害！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0012"
    $ current_voice = "voice/OKA03A_SDO0012.ogg"
    "４℃" "「哼！　很有趣不是吗！」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0013"
    $ current_voice = "voice/OKA03A_SDO0013.ogg"
    "４℃" "「羊驼人──」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0014"
    $ current_voice = "voice/OKA03A_SDO0014.ogg"
    "４℃" "「小白兔──」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0015"
    $ current_voice = "voice/OKA03A_SDO0015.ogg"
    "４℃" "「给秋叶原带来黑暗的老虎」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0016"
    $ current_voice = "voice/OKA03A_SDO0016.ogg"
    "４℃" "「就让我来告诉你们这些家伙什么是食物链吧！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0020"
    $ current_voice = "voice/OKA03A_OKA0020.ogg"
    "伦太郎" "「你这家伙才是，乖乖地回到动物园去吧，恶党哟！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0017"
    $ current_voice = "voice/OKA03A_SDO0017.ogg"
    "４℃" "「唔哦哦哦哦哦────！！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0021"
    $ current_voice = "voice/OKA03A_OKA0021.ogg"
    "伦太郎" "「嘿哈啊啊啊────！！」"
    hide screen phoneSD1
    window hide


    stop bgm 
    play se "SGSE349"

    python:
        loadBG(0,"IBGX048",trans=
            Fade(0.5,3,0.5))
    stop se
    hide screen phonebtn
    show screen phoneSD1
    "──１０分钟后。"
    window hide



    $ loadBG(2,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    show screen phonebtn
    play bgm "BGM13"

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0014"
    $ current_voice = "voice/OKA03A_NAE0014.ogg"
    "绹" "「啊，终于来了！　冈伦叔叔，你好慢。这边刚才发生了不得了的事呢──啊咧？」"

    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0022"
    $ current_voice = "voice/OKA03A_OKA0022.ogg"
    "伦太郎" "「小动物哟。你没事吧」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0015"
    $ current_voice = "voice/OKA03A_NAE0015.ogg"
    "绹" "「怎么了吗？　没事吧？　脸肿起来了哦──」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0023"
    $ current_voice = "voice/OKA03A_OKA0023.ogg"
    "伦太郎" "「在那里摔了一跤。不是什么大事」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0016"
    $ current_voice = "voice/OKA03A_NAE0016.ogg"
    "绹" "「是，是这样吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0024"
    $ current_voice = "voice/OKA03A_OKA0024.ogg"
    "伦太郎" "「比起那个，发生什么事了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0017"
    $ current_voice = "voice/OKA03A_NAE0017.ogg"
    "绹" "「嗯，那个啊！　刚才，羊驼人出现了哦！」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0025"
    $ current_voice = "voice/OKA03A_OKA0025.ogg"
    "伦太郎" "「喔，说起羊驼人的话，是那个？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0018"
    $ current_voice = "voice/OKA03A_NAE0018.ogg"
    "绹" "「对。带着奇怪假面的，奇怪的英雄！」"


    "奇怪是多余的……"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"])

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0019"
    $ current_voice = "voice/OKA03A_NAE0019.ogg"
    "绹" "「然后，他和前面这些人战斗了──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0020"
    $ current_voice = "voice/OKA03A_NAE0020.ogg"
    "绹" "「被打败了！」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0021"
    $ current_voice = "voice/OKA03A_NAE0021.ogg"
    "绹" "「明明是正义的伙伴，可是却那么弱，让我吓了一跳！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0026"
    $ current_voice = "voice/OKA03A_OKA0026.ogg"
    "伦太郎" "「小动物哟，你还不懂什么是『真正的强大』」"

    $ targetmailid = cml.setdefault("RM_OKA_SEND_FEI03","")

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0027"
    $ current_voice = "voice/OKA03A_OKA0027.ogg"
    "伦太郎" "「真正的强大即是──永不放弃的心！」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0022"
    $ current_voice = "voice/OKA03A_NAE0022.ogg"
    "绹" "「永不放弃……？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0028"
    $ current_voice = "voice/OKA03A_OKA0028.ogg"
    "伦太郎" "「嘛，总有一天你会明白的」"





    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG22A")
    play se "SGSE007L" loop

    show screen phoneSD1
    "与记忆中的时间一样，队伍前进了。"
    "之前故意输给４℃他们，是为了把他们的注意力吸引到羊驼人身上。"
    "然后在这个时候队伍前进的话──"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0018"
    $ current_voice = "voice/OKA03A_SDO0018.ogg"
    "４℃" "「咕！」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0019"
    $ current_voice = "voice/OKA03A_SDO0019.ogg"
    "４℃" "「呜……喂，喂。我，稍微去下厕所──」"
    $ stopvoc("Y06")
    play voc "OKA03A_Y060001"
    $ current_voice = "voice/OKA03A_Y060001.ogg"
    "５℃" "「等，等一下！　我也──」"
    $ stopvoc("Y07")
    play voc "OKA03A_Y070001"
    $ current_voice = "voice/OKA03A_Y070001.ogg"
    "６℃" "「我也是，突然──」"
    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0020"
    $ current_voice = "voice/OKA03A_SDO0020.ogg"
    "４℃" "「可恶。吃坏什么东西了吗──？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0021"
    $ current_voice = "voice/OKA03A_SDO0021.ogg"
    "４℃" "「喂，那边穿白大袍的！　我们的位置，帮我们留着！？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0029"
    $ current_voice = "voice/OKA03A_OKA0029.ogg"
    "伦太郎" "「为什么我要做这种事？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0022"
    $ current_voice = "voice/OKA03A_SDO0022.ogg"
    "４℃" "「笨蛋！　你难道听不见这盖亚的细声──」"
    window hide

    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0023"
    $ current_voice = "voice/OKA03A_SDO0023.ogg"
    "４℃" "「可，可恶！　总之，拜托你了！！」"
    stop se
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "抱着肚子，４℃～６℃朝厕所跑去了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0023"
    $ current_voice = "voice/OKA03A_NAE0023.ogg"
    "绹" "「他们的肚子……很痛吗」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0030"
    $ current_voice = "voice/OKA03A_OKA0030.ogg"
    "伦太郎" "「谁知道呢。啊对了，这个要吃吗？」"
    play se "SGSE337"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0024"
    $ current_voice = "voice/OKA03A_NAE0024.ogg"
    "绹" "「啊……炸鸡炸鸡君！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0031"
    $ current_voice = "voice/OKA03A_OKA0031.ogg"
    "伦太郎" "「虽然有些冷了」"
    window hide
    $ loadBG(0,"IBG015A",png=True,hide=False,trans=moveinbottom)


    hide screen phonebtn
    "……没错，我故意出演那场激烈的打斗的原因。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_DRASTIC"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_DRASTIC"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SALSA_DRASTIC"])
    "那就是，为了把他们吃的炸鸡炸鸡君和投入了羊驼七道具「{color=#f00}Ｓａｌｓａ・Ｄｒａｓｔｉｃ{/color}」（泻药）的炸鸡炸鸡君调包。"
    "只要使用倾注安第斯的恩惠的「Ｓａｌｓａ・Ｄｒａｓｔｉｃ」，不消片刻就能够催发激烈的便意！"
    "纷争会带来憎恨──所以，直接战斗是没有必要取胜的。"
    "虽然可能有些拐弯抹角，在看透未来的基础上，能够这样解决问题也不错。"
    hide screen phoneSD1
    window hide
    hide screen phonebtn
    hide background-png 

    stop se





    $ loadBG(0,"BG05A1",trans=Fade(1,1,1))

    show screen phoneSD1
    play bgm "BGM18"

    play se "SGSE017"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0025"
    $ current_voice = "voice/OKA03A_NAE0025.ogg"
    "绹" "「我回来了！」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0004"
    $ current_voice = "voice/OKA03A_TEN0004.ogg"
    "天王寺" "「哦哦，总算回来了！」"
    "小动物跳跃着飞入店内，我发觉Ｍｒ．布朗似乎下意识地从一张恐怖的脸换成笑脸迎接我们。"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0005"
    $ current_voice = "voice/OKA03A_TEN0005.ogg"
    "天王寺" "「游戏，买到了吗？」"
    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0026"
    $ current_voice = "voice/OKA03A_NAE0026.ogg"
    "绹" "「嗯，买到了哦！」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0006"
    $ current_voice = "voice/OKA03A_TEN0006.ogg"
    "天王寺" "「很好很好，太好了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0027"
    $ current_voice = "voice/OKA03A_NAE0027.ogg"
    "绹" "「冈伦叔叔，谢谢你！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0032"
    $ current_voice = "voice/OKA03A_OKA0032.ogg"
    "伦太郎" "「啊啊，这样约定就兑现了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0028"
    $ current_voice = "voice/OKA03A_NAE0028.ogg"
    "绹" "「约定？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0033"
    $ current_voice = "voice/OKA03A_OKA0033.ogg"
    "伦太郎" "「啊不是，什么也没有」"
    "绹并没有有关我在进行时间跳跃之前有过约定的记忆。"
    "英雄通常都是寂寞的生物。"
    "尽管如此──"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0029"
    $ current_voice = "voice/OKA03A_NAE0029.ogg"
    "绹" "「诶嘿嘿嘿……」"
    "能够看到同伴的笑脸，我想这就是我的回报。"
    "对吧，真由理？"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0007"
    $ current_voice = "voice/OKA03A_TEN0007.ogg"
    "天王寺" "「冈部，给你！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0034"
    $ current_voice = "voice/OKA03A_OKA0034.ogg"
    "伦太郎" "「诶，这是……」"
    "显像管氏递给我的，是五千日元。"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0008"
    $ current_voice = "voice/OKA03A_TEN0008.ogg"
    "天王寺" "「那个游戏太有人气所以几乎快脱销了不是吗。嘛，这是打工的奖金」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0035"
    $ current_voice = "voice/OKA03A_OKA0035.ogg"
    "伦太郎" "「……喂喂，是我。看来我正在掉入陷阱」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0036"
    $ current_voice = "voice/OKA03A_OKA0036.ogg"
    "伦太郎" "「嗯，说的也是。不入虎穴焉得虎子──在这个时刻，难道不该为对方手中的钞票而起舞吗」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0037"
    $ current_voice = "voice/OKA03A_OKA0037.ogg"
    "伦太郎" "「祈祷幸运眷顾我吧。Ｅｌ・Ｐｓｙ・Ｃｏｎｇｒｏｏ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0009"
    $ current_voice = "voice/OKA03A_TEN0009.ogg"
    "天王寺" "「你这家伙，好好接受别人的好意啊！」"
    window hide
    hide screen phonemenu
    call hide_phone


    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0038"
    $ current_voice = "voice/OKA03A_OKA0038.ogg"
    "伦太郎" "「我，我明白了。满怀感激地接受了」"
    "意料之外的临时收入啊。"
    "不挥霍一下的话……"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0010"
    $ current_voice = "voice/OKA03A_TEN0010.ogg"
    "天王寺" "「那么，我接下来还有别的工作。绹要好好回家哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA03A_NAE0030"
    $ current_voice = "voice/OKA03A_NAE0030.ogg"
    "绹" "「好！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0039"
    $ current_voice = "voice/OKA03A_OKA0039.ogg"
    "伦太郎" "「Ｍｒ．布朗又要出去吗？」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0011"
    $ current_voice = "voice/OKA03A_TEN0011.ogg"
    "天王寺" "「啊啊。我家打工的应该会来看店的」"
    "无论如何都要出门的工作……这么说的话，还没有结束吗。"
    "看到一直都很闲的Ｍｒ．布朗这个样子，总觉得很稀奇。"
    hide screen phoneSD1
    window hide


    stop bgm 

    $ loadBG(0,"BG02E2",trans=Fade(1,1,1))

    show screen phoneSD1
    play bgm "FDBGM02"

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0040"
    $ current_voice = "voice/OKA03A_OKA0040.ogg"
    "伦太郎" "「于是乎」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KTKR"])
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0000"
    $ current_voice = "voice/OKA03A_DAR0000.ogg"
    "至" "「临时收入{color=#f00}ｋｔｋｒ(出现啦){/color}！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0001"
    $ current_voice = "voice/OKA03A_DAR0001.ogg"
    "至" "「这么说来，就是──挥霍吗」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0041"
    $ current_voice = "voice/OKA03A_OKA0041.ogg"
    "伦太郎" "「挥霍哟」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0002"
    $ current_voice = "voice/OKA03A_DAR0002.ogg"
    "至" "「Ｓａｍｐｏ吗」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0042"
    $ current_voice = "voice/OKA03A_OKA0042.ogg"
    "伦太郎" "「嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0003"
    $ current_voice = "voice/OKA03A_DAR0003.ogg"
    "至" "「想，想去」"
    call CHECK_RM_RECEIVE
    "桶子点头。"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0043"
    $ current_voice = "voice/OKA03A_OKA0043.ogg"
    "伦太郎" "「走吧」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0004"
    $ current_voice = "voice/OKA03A_DAR0004.ogg"
    "至" "「走吧」"


    "事情便水到渠成了。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"])

    window hide



    $ loadBG(0,"BG05E2")


    $ targetmailid = cml.setdefault("RM_OKA_SEND_RUK03","")

    $ LR_RM_CHANCE=12
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0000"
    $ current_voice = "voice/OKA03A_SUZ0000.ogg"
    "铃羽" "「冈部伦太郎！　还有桥田至」"
    window hide



    $ loadBG(2,"BG39E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0044"
    $ current_voice = "voice/OKA03A_OKA0044.ogg"
    "伦太郎" "「哦，打工战士」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0005"
    $ current_voice = "voice/OKA03A_DAR0005.ogg"
    "至" "「呣哈！　今天的紧身裤也很美味！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0001"
    $ current_voice = "voice/OKA03A_SUZ0001.ogg"
    "铃羽" "「诶！？　那东西能吃吗！？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0045"
    $ current_voice = "voice/OKA03A_OKA0045.ogg"
    "伦太郎" "「怎么可能能吃啊。话说，你肚子饿吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB03"),"True","lh/SUZ_AMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0002"
    $ current_voice = "voice/OKA03A_SUZ0002.ogg"
    "铃羽" "「那，那种事──」"
    window hide
    play se "SGSE031"


    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA04"),"True","lh/SUZ_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0003"
    $ current_voice = "voice/OKA03A_SUZ0003.ogg"
    "铃羽" "「啊哈哈哈哈……」"
    call CHECK_RM_RECEIVE
    "铃羽笑着敷衍过去。"
    call CHECK_RM_RECEIVE
    "她最近，除了显像管工房之外还接了几份打工的工作，就像是在痴迷什么东西似地拼命攒钱。"
    call CHECK_RM_RECEIVE
    "听她说有一个无论如何都想修好的东西，更详细的内容就不知道了。"
    call CHECK_RM_RECEIVE
    "好像还说过如果能得到有知识的人的帮助的话，资金方面就可以好过一些……"
    call CHECK_RM_RECEIVE
    "即便是向ｌａｂｍｅｍ，铃羽也没有透露过更多的内容了。"


    "再稍稍地，做一些亲密的交流比较好吧？"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK04_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_RUK04_01"])


    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0046"
    $ current_voice = "voice/OKA03A_OKA0046.ogg"
    "伦太郎" "「偶尔一起去Ｓａｍｐｏ吗？　我请客哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0004"
    $ current_voice = "voice/OKA03A_SUZ0004.ogg"
    "铃羽" "「请客！？　是真的吗！？」"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0006"
    $ current_voice = "voice/OKA03A_DAR0006.ogg"
    "至" "「冈伦，是因为给店长帮忙拿到了临时收入，所以才变得大方了吧」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0047"
    $ current_voice = "voice/OKA03A_OKA0047.ogg"
    "伦太郎" "「怎么样？　反正店里也没事情可以做？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0005"
    $ current_voice = "voice/OKA03A_SUZ0005.ogg"
    "铃羽" "「嗯，虽然从来没有忙的时候」"
    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0006"
    $ current_voice = "voice/OKA03A_SUZ0006.ogg"
    "铃羽" "「虽然店长不在，可是就这样把店丢下不管，果然还是有些……」"
    "果然打工战士做事是很认真的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0007"
    $ current_voice = "voice/OKA03A_SUZ0007.ogg"
    "铃羽" "「你的心意我心领了」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0048"
    $ current_voice = "voice/OKA03A_OKA0048.ogg"
    "伦太郎" "「呣，是吗。那就下次再找机会──」"
    stop bgm 
    $ stopvoc("Y08")
    play voc "OKA03A_Y080000"
    $ current_voice = "voice/OKA03A_Y080000.ogg"
    "Ｓａｍｐｏ店员" "「站住呜呜呜────！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB04"),"True","lh/SUZ_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0049"
    $ current_voice = "voice/OKA03A_OKA0049.ogg"
    "伦太郎" "「嗯？　这声音是──」"
    window hide


    $ loadBG(2,"BG05E2")



    play bgm "BGM08"

    $ stopvoc("Y08")
    play voc "OKA03A_Y080001"
    $ current_voice = "voice/OKA03A_Y080001.ogg"
    "Ｓａｍｐｏ店员" "「请帮我抓住这个吃霸王餐的──！！」"
    "朝声音的方向看去，是Ｓａｍｐｏ的店员。"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0007"
    $ current_voice = "voice/OKA03A_DAR0007.ogg"
    "至" "「实况机会ｋｔｋｒ(出现啦)！」"
    "桶子快速拿出手机开始打字。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0050"
    $ current_voice = "voice/OKA03A_OKA0050.ogg"
    "伦太郎" "「哼，不过是个吃霸王餐的，爱凑热闹的家伙……」"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0008"
    $ current_voice = "voice/OKA03A_DAR0008.ogg"
    "至" "「嗯？」"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0009"
    $ current_voice = "voice/OKA03A_DAR0009.ogg"
    "至" "「那些人应该是病毒攻击的──」"
    window hide



    $ loadBG(2,"BG18E2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("SDO")
    play SDO "OKA03A_SDO0024"
    $ current_voice = "voice/OKA03A_SDO0024.ogg"
    "４℃" "「风啊！　我将化为飞驰在秋叶原的疾风！」"
    $ stopvoc("Y06")
    play voc "OKA03A_Y060002"
    $ current_voice = "voice/OKA03A_Y060002.ogg"
    "５℃" "「风！」"
    $ stopvoc("Y07")
    play voc "OKA03A_Y070002"
    $ current_voice = "voice/OKA03A_Y070002.ogg"
    "６℃" "「风！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0051"
    $ current_voice = "voice/OKA03A_OKA0051.ogg"
    "伦太郎" "「４～６℃！！」"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0010"
    $ current_voice = "voice/OKA03A_DAR0010.ogg"
    "至" "「那是神马？　──喂，阿万音氏！？」"
    window hide


    $ loadBG(2,"BG05E2")



    "正在看店的打工战士，突然从店里骑出一辆自行车急驶出去。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB01"),"True","lh/SUZ_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0008"
    $ current_voice = "voice/OKA03A_SUZ0008.ogg"
    "铃羽" "「盗窃别人的食物是死刑！　这是铁一般的规则！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve



    $ loadBG(2,"BG05E1")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DYSTOPIA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DYSTOPIA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DYSTOPIA"])
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0011"
    $ current_voice = "voice/OKA03A_DAR0011.ogg"
    "至" "「这是，多么的{color=#f00}Ｄｅｓｔｏｐｉａ{/color}啊……」"
    window hide

    stop bgm 

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0012"
    $ current_voice = "voice/OKA03A_DAR0012.ogg"
    "至" "「冈伦，要追吗？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0052"
    $ current_voice = "voice/OKA03A_OKA0052.ogg"
    "伦太郎" "「打工战士的话就放心吧。收拾４℃他们是小菜一碟」"
    "也没有正义的伙伴，羊驼人出场的机会吧。"
    "而且，未来的记忆里也没有这些……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0013"
    $ current_voice = "voice/OKA03A_DAR0013.ogg"
    "至" "「那么，去Ｓａｍｐｏ吗」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0053"
    $ current_voice = "voice/OKA03A_OKA0053.ogg"
    "伦太郎" "「啊啊，说的也是」"
    hide screen phoneSD1
    window hide




    $ loadBG(0,"BG18N2",trans=Fade(1,1,1))

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phoneSD1
    play bgm "BGM05"

    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0014"
    $ current_voice = "voice/OKA03A_DAR0014.ogg"
    "至" "「呼……Ｓａｍｐｏ好治愈。是秋叶原的良心」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0054"
    $ current_voice = "voice/OKA03A_OKA0054.ogg"
    "伦太郎" "「嗯。没有异议」"
    "吃完饭散步回到Ｌａｂ的时候，四周已经暗下来了。"
    window hide


    $ loadBG(2,"BG05N1")



    "饱腹感催生了困意，在走上楼梯的时候，Ｍｒ．布朗的身影从店里走出来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0012"
    $ current_voice = "voice/OKA03A_TEN0012.ogg"
    "天王寺" "「哦，冈部！　看到打工的了吗？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0055"
    $ current_voice = "voice/OKA03A_OKA0055.ogg"
    "伦太郎" "「嗯？　啊啊……」"
    "难道说去追４℃之后，就这样没有回来了吗？"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0056"
    $ current_voice = "voice/OKA03A_OKA0056.ogg"
    "伦太郎" "「这么说来，好像看到了又好像没有看到」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0013"
    $ current_voice = "voice/OKA03A_TEN0013.ogg"
    "天王寺" "「真是的！　那家伙，丢下店跑到哪里去了……」"
    $ stopvoc("TEN")
    play TEN "OKA03A_TEN0014"
    $ current_voice = "voice/OKA03A_TEN0014.ogg"
    "天王寺" "「如果你能联络到她，就帮我问一下」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0057"
    $ current_voice = "voice/OKA03A_OKA0057.ogg"
    "伦太郎" "「啊啊，我知道了──」"
    hide screen phonebtn
    window hide
    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    $ targetmailid = gc["ScriptMacros"]["FM_OKA03A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "我点点头，这个时候刚好收到了一封邮件。"

    "难道是铃羽发来的……？"

    "这么想着，我看向屏幕画面──"

    window hide


    call read_last_mail






    play bgm "FD2BGM04"

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0058"
    $ current_voice = "voice/OKA03A_OKA0058.ogg"
    "伦太郎" "「────！？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0015"
    $ current_voice = "voice/OKA03A_DAR0015.ogg"
    "至" "「冈伦怎么了？」"
    window hide
    call hide_phone

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0059"
    $ current_voice = "voice/OKA03A_OKA0059.ogg"
    "伦太郎" "「电视！」"
    window hide
    play se "SGSE017"



    $ loadBG(2,"BG04A1")



    "将面前的巨大电视机插上电源。"
    window hide
    play se "SGSE323"



    $ loadBG(2,"BG04A2")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHIDIGI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHIDIGI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHIDIGI"])
    "特地连接上调谐器后显示在显像管上的，正好是通过{color=#f00}地数{/color}播放的首都圈Ｎｅｗｓ的当地新闻。"
    window hide


    $ loadBG(2,"IBG016A")



    hide screen phonebtn
    "字幕上显示的是「秋叶原闹市发生强盗伤人事件」的文字。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0060"
    $ current_voice = "voice/OKA03A_OKA0060.ogg"
    "伦太郎" "「４℃！？」"
    "看到照片上犯人的脸，我不由得大声叫道。"
    $ stopvoc("X01")
    play voc "OKA03A_X010000"
    $ current_voice = "voice/OKA03A_X010000.ogg"
    "播音员" "『犯人是住所不定的无业男性，做出了「吃饭没有给钱。电击枪是在秋叶原偷的，可是没有想要伤害人质的意思」的供述──』"
    "是路人拍的吧，写着「目击者提供」的字样的照片里，出现了打工战士的身影。"
    "然后，面对镜头的４℃拿着电击枪威胁的人是──"
    $ stopvoc("DAR")
    play DAR "OKA03A_DAR0016"
    $ current_voice = "voice/OKA03A_DAR0016.ogg"
    "至" "「琉华氏！　怎么会……」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0061"
    $ current_voice = "voice/OKA03A_OKA0061.ogg"
    "伦太郎" "「────！！」"
    window hide
    play se "SGSE017"



    $ loadBG(2,"IBGX072")



    "看到琉华子的同时，我跑了出去。"
    hide screen phoneSD1
    window hide
    stop bgm 



    $ loadBG(0,"BG15N1",trans=Fade(1,1,1))

    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM05"

    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0062"
    $ current_voice = "voice/OKA03A_OKA0062.ogg"
    "伦太郎" "「琉华子！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA01"),"True","lh/RUK_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA03A_RUK0000"
    $ current_voice = "voice/OKA03A_RUK0000.ogg"
    "琉华" "「啊……冈，不对，凶真师傅」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0063"
    $ current_voice = "voice/OKA03A_OKA0063.ogg"
    "伦太郎" "「受的伤不要紧吧！？」"
    $ stopvoc("RUK")
    play RUK "OKA03A_RUK0001"
    $ current_voice = "voice/OKA03A_RUK0001.ogg"
    "琉华" "「嗯。在医院接受过检查了，其实根本没有受伤」"
    "尽管这么说，琉华子的脸上还是显出了疲态。"
    "为了不给琉华子添加过多的负担，我让他尽可能简单地描述了一下事件的大概。"
    "在秋叶原前买东西的琉华子走在街上，碰巧与追赶４℃那些人的铃羽擦身而过，于是便被当成了人质。"
    "随后被犯人用电击枪威胁之后便昏了过去。"
    "最后多亏了铃羽，４℃才被移交给了警察……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA06"),"True","lh/RUK_BSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "OKA03A_RUK0002"
    $ current_voice = "voice/OKA03A_RUK0002.ogg"
    "琉华" "「在这之后必须要去配合事件调查。所以，五月雨的空挥就没办法──」"
    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0064"
    $ current_voice = "voice/OKA03A_OKA0064.ogg"
    "伦太郎" "「琉华子，对不起！　都是因为我才让这种事发生──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA02"),"True","lh/RUK_BSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA03A_RUK0003"
    $ current_voice = "voice/OKA03A_RUK0003.ogg"
    "琉华" "「诶，为什么要道歉呢！？　冈部师傅，没有做错什么哦」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0065"
    $ current_voice = "voice/OKA03A_OKA0065.ogg"
    "伦太郎" "「要是我再可靠一点的话，这种事──」"
    "琉华子是无法理解的吧。"
    "不过对我来说，有着作为英雄保护秋叶原的责任。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0066"
    $ current_voice = "voice/OKA03A_OKA0066.ogg"
    "伦太郎" "「下次，我一定会保护你的。知道了吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA05"),"True","lh/RUK_BSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA03A_RUK0004"
    $ current_voice = "voice/OKA03A_RUK0004.ogg"
    "琉华" "「啊……好的」"
    "不知为何，琉华子很开心地微笑着。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG05N3",trans=Fade(1,1,1))

    show screen phoneSD1
    "回到显像管工房，带着疲倦的表情的铃羽等在那里。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0009"
    $ current_voice = "voice/OKA03A_SUZ0009.ogg"
    "铃羽" "「冈部伦太郎……！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0067"
    $ current_voice = "voice/OKA03A_OKA0067.ogg"
    "伦太郎" "「啊，回来了吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0010"
    $ current_voice = "voice/OKA03A_SUZ0010.ogg"
    "铃羽" "「嗯。被警察缠了半天」"
    "说起来，铃羽有些异常地讨厌警察。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0011"
    $ current_voice = "voice/OKA03A_SUZ0011.ogg"
    "铃羽" "「漆原琉华怎么样了？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0068"
    $ current_voice = "voice/OKA03A_OKA0068.ogg"
    "伦太郎" "「不用担心。他结实着呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0012"
    $ current_voice = "voice/OKA03A_SUZ0012.ogg"
    "铃羽" "「是吗……太好了」"
    "打工的时间早就已经结束了。"
    "为了打听琉华子的情况，才会一直等在这里吧。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0013"
    $ current_voice = "voice/OKA03A_SUZ0013.ogg"
    "铃羽" "「到最后偏偏让自己的伙伴受伤什么的……我作为战士，很失败啊」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0069"
    $ current_voice = "voice/OKA03A_OKA0069.ogg"
    "伦太郎" "「这么说的话，我作为正义的伙伴也很失败」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0014"
    $ current_voice = "voice/OKA03A_SUZ0014.ogg"
    "铃羽" "「诶……？」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0070"
    $ current_voice = "voice/OKA03A_OKA0070.ogg"
    "伦太郎" "「铃羽，４℃拿着电击枪对吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0015"
    $ current_voice = "voice/OKA03A_SUZ0015.ogg"
    "铃羽" "「嗯。非常大的家伙。没想到，他真的会拿来用……」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0071"
    $ current_voice = "voice/OKA03A_OKA0071.ogg"
    "伦太郎" "「别在意。下次不会再让他用了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA03A_SUZ0016"
    $ current_voice = "voice/OKA03A_SUZ0016.ogg"
    "铃羽" "「下次……？」"
    "没有理会露出不可思议的表情的铃羽，我上了二楼。"
    window hide
    stop bgm 



    $ loadBG(0,"BG02N1",hold=True)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(3,"IBG019A",png=True,hide=False,hold=True)
    with Dissolve(.5)
    $ renpy.pause(0.5,hard=True)
    hide background-png 
    with Dissolve(.5)



    play bgm "FD2BGM08"


    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0003"
    $ current_voice = "voice/OKA03A_MAY0003.ogg"
    "真由理" "「啊！　欢伦回来！！」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0072"
    $ current_voice = "voice/OKA03A_OKA0072.ogg"
    "伦太郎" "「真由理，我回来了」"
    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0004"
    $ current_voice = "voice/OKA03A_MAY0004.ogg"
    "真由理" "「果然是这身打扮呢」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0073"
    $ current_voice = "voice/OKA03A_OKA0073.ogg"
    "伦太郎" "「啊」"
    "真由理也，看到琉华子的新闻了吧。"
    "我接下来要做的事情，只有她能够理解。"
    $ stopvoc("MAY")
    play MAY "OKA03A_MAY0005"
    $ current_voice = "voice/OKA03A_MAY0005.ogg"
    "真由理" "「司令也已经准备好了哦」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0074"
    $ current_voice = "voice/OKA03A_OKA0074.ogg"
    "伦太郎" "「哦」"
    window hide


    $ loadBG(2,"IBGX007")



    hide screen phonebtn
    "我朝着在和真由理玩的羊驼司令搭话。"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0075"
    $ current_voice = "voice/OKA03A_OKA0075.ogg"
    "伦太郎" "「羊驼司令哟」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0076"
    $ current_voice = "voice/OKA03A_OKA0076.ogg"
    "伦太郎" "「我，决定了。为了正义，再次回到过去」"
    $ stopvoc("Y05")
    play voc "OKA03A_Y050000"
    $ current_voice = "voice/OKA03A_Y050000.ogg"
    "羊驼司令" "「正义吗……」"
    "司令的语音识别功能十分难得地做出了正常的反应。"
    $ stopvoc("Y05")
    play voc "OKA03A_Y050001"
    $ current_voice = "voice/OKA03A_Y050001.ogg"
    "羊驼司令" "「你知道吗？」"
    $ stopvoc("Y05")
    play voc "OKA03A_Y050002"
    $ current_voice = "voice/OKA03A_Y050002.ogg"
    "羊驼司令" "「为了正义的光辉，恶的存在是必要的」"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0077"
    $ current_voice = "voice/OKA03A_OKA0077.ogg"
    "伦太郎" "「……你在说什么蠢话」"
    "这么说就好像，我一直在等待着恶的出现一样不是吗。"
    "怎么可能，我是那种坏人吗？"
    $ stopvoc("OKA")
    play OKA "OKA03A_OKA0078"
    $ current_voice = "voice/OKA03A_OKA0078.ogg"
    "伦太郎" "「哼，还是老样子，让人生气的家伙」"
    "我怎么可能被区区ＡＩ迷惑呢。"
    window hide



    $ loadBG(0,"BG03A4",trans=Fade(0.5,1,0.5))

    "设定好时间跳跃的时间，带上耳机。"
    window hide
    stop bgm 
    show houden 

    play se "SGSE035L" loop

    "作为正义的伙伴羊驼人，回到过去──"

    hide houden 
    hide screen phoneSD1
    window hide
    stop se
    stop se
    stop bgm
    call timeleap (fromtime=[8,11,20,15], totime=[8,11,18,15], fromday=[4])

    return








    return
