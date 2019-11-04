label SGFD2_OKA04A:
    window hide


    $ loadBG(0,"BG05E2")
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)




    $ date="8/11"
    show screen phoneSD1
    python:
        cml = {}
        while len(rml)>0 and rml[0]["MetaData"]["Time"] > 1814 and rml[0]["MetaData"]["Date"] == 811:
            UnreadMail(rml[0]["MailNumber"])
            notLate(rml[0]["MailNumber"])
            del rml[0]

    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0000"
    $ current_voice = "voice/OKA04A_DAR0000.ogg"
    "至" "「那是神马? ──喂，阿万音氏！？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB01"),"True","lh/SUZ_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0000"
    $ current_voice = "voice/OKA04A_SUZ0000.ogg"
    "铃羽" "「盗窃别人的食物是死刑！　这是铁一般的规则！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve







    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0001"
    $ current_voice = "voice/OKA04A_DAR0001.ogg"
    "至" "「这是，多么的Ｄｅｓｔｏｐｉａ啊……」"
    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0002"
    $ current_voice = "voice/OKA04A_DAR0002.ogg"
    "至" "「冈伦，要追吗？」"
    window hide
    play bgm "FD2BGM04"

    call hide_phone




    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0000"
    $ current_voice = "voice/OKA04A_OKA0000.ogg"
    "伦太郎" "「嗯呣哈哈哈！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0003"
    $ current_voice = "voice/OKA04A_DAR0003.ogg"
    "至" "「冈，冈伦怎么了？　拿着电话就突然笑起来了──」"
    "似乎是想要把传送之后的恶心感驱散一般，我放声大笑着。"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0001"
    $ current_voice = "voice/OKA04A_OKA0001.ogg"
    "伦太郎" "「在转卖屋干得还不够，现在又来吃霸王餐，最后还让ｌａｂｍｅｍ受伤，不能原谅不能原谅！　绝──对不能原谅！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0004"
    $ current_voice = "voice/OKA04A_DAR0004.ogg"
    "至" "「受伤？　是，怎么回事？」"
    window hide
    play se "SGSE182"



    $ loadBG(2,"BG18E2")



    $ stopvoc("DAR")
    play DAR "OKA04A_DAR0005"
    $ current_voice = "voice/OKA04A_DAR0005.ogg"
    "至" "「喂，冈伦？　等！　一下！　已经不见了！」"
    "虽然很对不起桶子，可是不单独行动的话就无法变身为羊驼人。"
    "我只身一人，跑到秋叶原的街上。"
    hide screen phoneSD1
    window hide
    stop bgm 
    stop se



    $ loadBG(0,"IBGX033",trans=fade)


    hide screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM02"

    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0000"
    $ current_voice = "voice/OKA04A_SDO0000.ogg"
    "４℃" "「哈，哈，哈……！　马上就要到车站了……！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0001"
    $ current_voice = "voice/OKA04A_SDO0001.ogg"
    "４℃" "「风啊……将风拾起来吧！」（此处NETA2011年举行的人力滑翔机大赛中中村拓磨选手的中二病发言，后两句同）"
    $ stopvoc("Y06")
    play voc "OKA04A_Y060000"
    $ current_voice = "voice/OKA04A_Y060000.ogg"
    "５℃" "「左脚……抽筋了……脚脚脚脚啊啊啊啊……！！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0002"
    $ current_voice = "voice/OKA04A_SDO0002.ogg"
    "４℃" "「别放弃！　我们是病毒攻击吧！」"
    $ stopvoc("Y07")
    play voc "OKA04A_Y070000"
    $ current_voice = "voice/OKA04A_Y070000.ogg"
    "６℃" "「４℃！　还有多少米──」"
    window hide
    play se "SGSE040"

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0001"
    $ current_voice = "voice/OKA04A_SUZ0001.ogg"
    "铃羽" "「到此为止了哦」"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0003"
    $ current_voice = "voice/OKA04A_SDO0003.ogg"
    "４℃" "「！？　被追上了──！」"
    "事先抄近路绕过来的铃羽，轻巧地从自行车上跳下。"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0002"
    $ current_voice = "voice/OKA04A_SUZ0002.ogg"
    "铃羽" "「逃脱者的追踪路线，事先模拟过一遍真是太好了」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0004"
    $ current_voice = "voice/OKA04A_SDO0004.ogg"
    "４℃" "「逃脱者？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB01"),"True","lh/SUZ_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0003"
    $ current_voice = "voice/OKA04A_SUZ0003.ogg"
    "铃羽" "「为了防止这种事情发生，事先已经做过准备了。被出卖的话，情报让那些家伙得手就糟糕了」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0005"
    $ current_voice = "voice/OKA04A_SDO0005.ogg"
    "４℃" "「哼。你这家伙，想一个人跟政府对着干吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0004"
    $ current_voice = "voice/OKA04A_SUZ0004.ogg"
    "铃羽" "「我呢，是在拯救世界哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0006"
    $ current_voice = "voice/OKA04A_SDO0006.ogg"
    "４℃" "「{color=#f00}厨二病{/color}啊」"
    "轮不到你来说。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0005"
    $ current_voice = "voice/OKA04A_SUZ0005.ogg"
    "铃羽" "「正因如此，霸王餐犯人！　做好觉悟吧！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0007"
    $ current_voice = "voice/OKA04A_SDO0007.ogg"
    "４℃" "「哈！　就一个女的能做什么！　上」"
    "在４℃的一声令下，５℃和６℃朝铃羽扑了过去──"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0006"
    $ current_voice = "voice/OKA04A_SUZ0006.ogg"
    "铃羽" "「呀！」"
    window hide
    play se "SGSE064"
    with Fade(0.1,0.1,0.1,color="fff")



    $ stopvoc("Y06")
    play voc "OKA04A_Y060001"
    $ current_voice = "voice/OKA04A_Y060001.ogg"
    "５℃" "「噫！」"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0007"
    $ current_voice = "voice/OKA04A_SUZ0007.ogg"
    "铃羽" "「哒！」"
    window hide
    play se "SGSE066"
    with Fade(0.1,0.1,0.1,color="fff")



    $ stopvoc("Y07")
    play voc "OKA04A_Y070001"
    $ current_voice = "voice/OKA04A_Y070001.ogg"
    "６℃" "「咩！」"
    window hide
    stop bgm 

    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0008"
    $ current_voice = "voice/OKA04A_SUZ0008.ogg"
    "铃羽" "「啊，已经结束了？」"
    "十分轻易地就被干掉了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0009"
    $ current_voice = "voice/OKA04A_SUZ0009.ogg"
    "铃羽" "「这种程度，可不能被称作是独当一面的战士啊」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0008"
    $ current_voice = "voice/OKA04A_SDO0008.ogg"
    "４℃" "「可，可恶！　既然这样的话──」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA002B"]]["Check"]=True


    $ loadBG(2,"EV_OKA002B")



    play bgm "BGM08"

    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0000"
    $ current_voice = "voice/OKA04A_RUK0000.ogg"
    "琉华" "「呀啊啊啊啊！！」"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0000"
    $ current_voice = "voice/OKA04A_MAY0000.ogg"
    "真由理" "「不，不要啊！！」"
    "４℃突然扑向了一旁偶然路过的琉华子和真由理。"
    "琉华子被他从身后抱住身体，同时雪白的脖颈被电击枪顶住。"
    "人质。"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0010"
    $ current_voice = "voice/OKA04A_SUZ0010.ogg"
    "铃羽" "「什！　卑鄙小人！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0009"
    $ current_voice = "voice/OKA04A_SDO0009.ogg"
    "４℃" "「不许动！！」"
    play se "SGSE154"
    "像是在炫耀它的威力一般，电击枪发出四散的火花。"
    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0001"
    $ current_voice = "voice/OKA04A_RUK0001.ogg"
    "琉华" "「噫！　这，这种事……」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0010"
    $ current_voice = "voice/OKA04A_SDO0010.ogg"
    "４℃" "「这家伙是在看不起我吗？　我的理性可不会刹车啊……」"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0011"
    $ current_voice = "voice/OKA04A_SUZ0011.ogg"
    "铃羽" "「…………！」"
    "打工战士痛苦地咬着嘴唇。"
    "可是，面对两个人都被当做人质的她，却没有能力打破这一现状。"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0011"
    $ current_voice = "voice/OKA04A_SDO0011.ogg"
    "４℃" "「咕咕咕！　听话一点不是挺好的吗。喂，大家！」"
    $ stopvoc("Y06")
    play voc "OKA04A_Y060002"
    $ current_voice = "voice/OKA04A_Y060002.ogg"
    "５℃" "「哦，哦」"
    $ stopvoc("Y07")
    play voc "OKA04A_Y070002"
    $ current_voice = "voice/OKA04A_Y070002.ogg"
    "６℃" "「刚才的债──现在还给你哟」"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0012"
    $ current_voice = "voice/OKA04A_SUZ0012.ogg"
    "铃羽" "「…………」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA002A"]]["Check"]=True


    $ loadBG(2,"EV_OKA002A")



    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0002"
    $ current_voice = "voice/OKA04A_RUK0002.ogg"
    "琉华" "「铃羽小姐！」"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0001"
    $ current_voice = "voice/OKA04A_MAY0001.ogg"
    "真由理" "「大家，不可以使用暴力哟！」"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    show screen phoneSD1
    "打工战士，没有动。"
    "她不是那种会出卖伙伴的人。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA002A"]]["Check"]=True


    $ loadBG(2,"EV_OKA002A")



    hide screen phonebtn
    "这样下去的话，为了不让铃羽受到单方面的殴打，琉华子会挣脱出来。"
    "４℃则为了阻止他，使用了电击枪。"
    "结果是，琉华子昏过去了。"
    "本该是这样的。"
    "不过──那种未来，我决不会允许！"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0002"
    $ current_voice = "voice/OKA04A_OKA0002.ogg"
    "伦太郎" "「住手！！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0012"
    $ current_voice = "voice/OKA04A_SDO0012.ogg"
    "４℃" "「嗯？」"
    "突然，从其他的地方传来声音。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA002C"]]["Check"]=True


    $ loadBG(2,"EV_OKA002C")



    "大家的视线，集中在了小巷旁边的证件照相机上。"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0003"
    $ current_voice = "voice/OKA04A_OKA0003.ogg"
    "伦太郎" "「咚！！」"
    stop bgm 
    "揭开窗帘里面出现的是──"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0013"
    $ current_voice = "voice/OKA04A_SDO0013.ogg"
    "４℃" "「什……什么！？」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0004"
    $ current_voice = "voice/OKA04A_OKA0004.ogg"
    "伦太郎" "「我的名字是──」"
    hide screen phoneSD1
    window hide
    play se "SGSE347"

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001A"]]["Check"]=True

    hide screen phonebtn
    play bgm "FD2BGM03"
    show EVOKA001A_BG1 
    show EVOKA001A_FACE_R 

    with Fade(0.1,0.1,0.1,color="fff")

    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0005"
    $ current_voice = "voice/OKA04A_OKA0005.ogg"
    "伦太郎" "「天在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001B"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG1 
    hide EVOKA001A_FACE_R 
    show EVOKA001A_BG2 
    show EVOKA001A_FACE_L 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA04A_OKA0006"
    $ current_voice = "voice/OKA04A_OKA0006.ogg"
    "伦太郎" "「地在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001C"]]["Check"]=True

    $ stopvoc("OKA")
    hide EVOKA001A_BG2 
    hide EVOKA001A_FACE_L 
    show EVOKA001A_BG3 
    show EVOKA001A_FACE_C 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA04A_OKA0007"
    $ current_voice = "voice/OKA04A_OKA0007.ogg"
    "伦太郎" "「安第斯在呼唤！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001D"]]["Check"]=True

    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0008"
    hide EVOKA001A_BG3 
    hide EVOKA001A_FACE_C 
    show EVOKA001A_BG4 
    show EVOKA001A_FACE_H 
    with Fade(0.1,0.1,0.1,color="fff")
    $ current_voice = "voice/OKA04A_OKA0008.ogg"
    "伦太郎" "「秋叶原中诞生的神秘英雄！」"
    window hide







    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA001E"]]["Check"]=True






    $ stopvoc("OKA")
    hide EVOKA001A_FACE_H 
    show EVOKA001A_HAND 
    show EVOKA001A_FACE 
    with Fade(0.1,0.1,0.1,color="fff")
    play OKA "OKA04A_OKA0009"
    $ current_voice = "voice/OKA04A_OKA0009.ogg"
    "伦太郎" "「羊驼人，登场！」"


    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0013"
    $ current_voice = "voice/OKA04A_SUZ0013.ogg"
    "铃羽" "「嘿？」"
    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0003"
    $ current_voice = "voice/OKA04A_RUK0003.ogg"
    "琉华" "「羊驼……人先生？」"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0002"
    $ current_voice = "voice/OKA04A_MAY0002.ogg"
    "真由理" "「好棒！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0014"
    $ current_voice = "voice/OKA04A_SDO0014.ogg"
    "４℃" "「又是你这家伙吗！」"
    "４℃威胁的话完全暴露了他是个笨蛋。"
    "不好意思，我没空把时间浪费在这种杂鱼身上。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BANK_SYSTEM"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BANK_SYSTEM"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BANK_SYSTEM"])
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0010"
    $ current_voice = "voice/OKA04A_OKA0010.ogg"
    "伦太郎" "「你们这些家伙，{color=#f00}ＢＡＮＫ演出{/color}已经足够了！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_P38"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALSA_P38"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SALSA_P38"])
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0011"
    $ current_voice = "voice/OKA04A_OKA0011.ogg"
    "伦太郎" "「尝尝吧！　羊驼七道具( seven gear )之一！　『{color=#f00}Ｓａｌｓａ－Ｐ３８{/color}』！！」"
    "反复使用时间跳跃训练过的，行云流水般的操作。"
    "４℃应该没有时间做出反应。"
    "我瞬间从白衣里拿出Ｓａｌｓａ，扣下扳机。"

    hide EVOKA001A_HAND 
    hide EVOKA001A_BG4 
    hide EVOKA001A_FACE 
    window hide




    play se "SGSE157"





    with Fade(0.2,0.5,0.2,color="f00")
    pause 1
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA002C"]]["Check"]=True
    $ loadBG(0,"EV_OKA002C")


    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0015"
    $ current_voice = "voice/OKA04A_SDO0015.ogg"
    "４℃" "「什，什──」"
    "４℃被Ｓａｌｓａ－Ｐ３８放出的莎莎酱侵袭。"
    "仿佛连血都被喷出来一般，身体被涂得鲜红。"
    window hide



    $ loadBG(3,"EV_OKA002C")






    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0016"
    $ current_voice = "voice/OKA04A_SDO0016.ogg"
    "４℃" "「这是啥啊啊啊啊啊啊！？」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0012"
    $ current_voice = "voice/OKA04A_OKA0012.ogg"
    "伦太郎" "「让你感受到安第斯的恩惠的！　特制莎莎酱！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0017"
    $ current_voice = "voice/OKA04A_SDO0017.ogg"
    "４℃" "「小，小看我的话，人质就──」"
    window hide
    play se "SGSE154"

    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0004"
    $ current_voice = "voice/OKA04A_RUK0004.ogg"
    "琉华" "「呀！！」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0013"
    $ current_voice = "voice/OKA04A_OKA0013.ogg"
    "伦太郎" "「哎哟！　不要用那个东西比较好哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ELECTROLITE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ELECTROLITE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ELECTROLITE"])
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0014"
    $ current_voice = "voice/OKA04A_OKA0014.ogg"
    "伦太郎" "「那个汁液是{color=#f00}电解质{/color}──就这样使用电击器的话，它会自爆哦」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0018"
    $ current_voice = "voice/OKA04A_SDO0018.ogg"
    "４℃" "「什──！」"
    "他手中握着的电击枪也沾满了莎莎酱。"
    "看上去不像是靠简单擦拭就能擦干净的。"
    "这样，就相当于使对手的武器失去了伤害性。"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0003"
    $ current_voice = "voice/OKA04A_MAY0003.ogg"
    "真由理" "「羊驼人，好厉害哦！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0019"
    $ current_voice = "voice/OKA04A_SDO0019.ogg"
    "４℃" "「可，可恶！」"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play se "SGSE069"
    "４℃丢掉了已经变成没用的棍子的电击枪。"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0020"
    $ current_voice = "voice/OKA04A_SDO0020.ogg"
    "４℃" "「你们这些家伙，给我记住──」"
    stop bgm 
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0014"
    $ current_voice = "voice/OKA04A_SUZ0014.ogg"
    "铃羽" "「哎哟，你想逃到哪里去呢？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM12"

    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0021"
    $ current_voice = "voice/OKA04A_SDO0021.ogg"
    "４℃" "「什──！？」"
    $ stopvoc("Y06")
    play voc "OKA04A_Y060003"
    $ current_voice = "voice/OKA04A_Y060003.ogg"
    "５℃" "「抱……抱歉，４℃……」"
    $ stopvoc("Y07")
    play voc "OKA04A_Y070003"
    $ current_voice = "voice/OKA04A_Y070003.ogg"
    "６℃" "「又被揍了……」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0022"
    $ current_voice = "voice/OKA04A_SDO0022.ogg"
    "４℃" "「什，什么时候！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA05"),"True","lh/SUZ_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0015"
    $ current_voice = "voice/OKA04A_SUZ0015.ogg"
    "铃羽" "「竟敢做出伤害我的伙伴的事情，好大的胆子呢」"
    $ stopvoc("RUK")
    play RUK "OKA04A_RUK0005"
    $ current_voice = "voice/OKA04A_RUK0005.ogg"
    "琉华" "「那……那个，铃羽小姐？　我没有事──」"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0016"
    $ current_voice = "voice/OKA04A_SUZ0016.ogg"
    "铃羽" "「不可以哦。这样的话，是没办法让他们用身体记住的」"
    "铃羽面色平静地说道，简直就好像是在训练狗一样。"
    "光是她不带色彩的声音，就使人感到一丝寒意。"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0017"
    $ current_voice = "voice/OKA04A_SUZ0017.ogg"
    "铃羽" "「那么，就先让你做完祈祷吧？」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0023"
    $ current_voice = "voice/OKA04A_SDO0023.ogg"
    "４℃" "「噫，噫诶诶诶诶诶诶────！！」"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0018"
    $ current_voice = "voice/OKA04A_SUZ0018.ogg"
    "铃羽" "「────！！」"
    $ stopvoc("SDO")
    play SDO "OKA04A_SDO0024"
    $ current_voice = "voice/OKA04A_SDO0024.ogg"
    "４℃" "「呀啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」"
    "嗖！　铃羽腿下生风作响。"
    window hide
    play se "SGSE065"

    stop bgm
    with Fade(0.1,0.1,0.1)




    $ loadBG(0,"BG_BLACK")

    "可怜的４℃。"
    "尝过这次苦头之后，能够金盆洗手就好了……"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG05N3")

    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    "已经日暮西山了，我们回到了显像管工房。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA02"),"True","lh/SUZ_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0019"
    $ current_voice = "voice/OKA04A_SUZ0019.ogg"
    "铃羽" "「呀，好厉害哟，羊驼人！」"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0020"
    $ current_voice = "voice/OKA04A_SUZ0020.ogg"
    "铃羽" "「那是经过训练的人才能做到的行动！　简直就好像能猜到对手的下一个动作一般！」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0015"
    $ current_voice = "voice/OKA04A_OKA0015.ogg"
    "伦太郎" "「啊嗯嗯是吗是吗那真是厉害」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA04"),"True","lh/SUZ_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0021"
    $ current_voice = "voice/OKA04A_SUZ0021.ogg"
    "铃羽" "「好棒啊……好崇拜。我也有一天，可以成为羊驼人的吧……」"
    $ stopvoc("TEN")
    play TEN "OKA04A_TEN0000"
    $ current_voice = "voice/OKA04A_TEN0000.ogg"
    "天王寺" "「放弃吧」"
    window hide

    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0022"
    $ current_voice = "voice/OKA04A_SUZ0022.ogg"
    "铃羽" "「啊……店长！」"
    "打工战士的表情瞬间凝固了。"
    "Ｍｒ．布朗的眼中，充满了对翘班的铃羽的杀意。"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0023"
    $ current_voice = "voice/OKA04A_SUZ0023.ogg"
    "铃羽" "「那，那个对对对对对不起！　看店的时候，眼前出现了吃霸王餐的犯人──」"
    $ stopvoc("TEN")
    play TEN "OKA04A_TEN0001"
    $ current_voice = "voice/OKA04A_TEN0001.ogg"
    "天王寺" "「霸王餐？　你说的不会是那家伙吧？」"
    "Ｍｒ．布朗指向店内。"
    window hide


    $ loadBG(2,"BG04A2")



    play bgm "FD2BGM05"
    "十分难得地，显像管工房里的电视接通了电源。"
    "屏幕里出现的是４℃。"
    window hide


    $ loadBG(2,"IBG016A")



    hide screen phonebtn
    $ stopvoc("X01")
    play voc "OKA04A_X010000"
    $ current_voice = "voice/OKA04A_X010000.ogg"
    "播音员" "『犯人是住所不定的无业男性，做出了「吃饭没有给钱。电击枪是在秋叶原偷的，可是没有想要伤害人质的意思」的供述──』"
    $ stopvoc("SUZ")
    play SUZ "OKA04A_SUZ0024"
    $ current_voice = "voice/OKA04A_SUZ0024.ogg"
    "铃羽" "「没错，就是那家伙！　做出吃霸王餐这种事，实在是岂有此理的犯罪者！」"
    $ stopvoc("TEN")
    play TEN "OKA04A_TEN0002"
    $ current_voice = "voice/OKA04A_TEN0002.ogg"
    "天王寺" "「要我说的话。连吃饭的钱都没有的人，一定是窘迫到极点了吧」"
    "窘迫……？"
    "像是在回答我的疑问一般，电视里的评论员在后面继续说道。"
    window hide


    $ loadBG(2,"IBG016C")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NET_CAFE"])
    $ stopvoc("Y09")
    play voc "OKA04A_Y090000"
    $ current_voice = "voice/OKA04A_Y090000.ogg"
    "播音员" "『最近像这个犯人一样，在{color=#f00}Ｎｅｔ　Ｃａｆｅ{/color}夜宿的二十几岁的贫困层的数量在增加』"
    $ stopvoc("Y09")
    play voc "OKA04A_Y090001"
    $ current_voice = "voice/OKA04A_Y090001.ogg"
    "播音员" "『一部分情报指出，犯人是靠着做些一早开始帮转卖屋排队之类的日结工资的工作来赚取生活费的──』"
    $ stopvoc("TEN")
    play TEN "OKA04A_TEN0003"
    $ current_voice = "voice/OKA04A_TEN0003.ogg"
    "天王寺" "「没有哪个家伙喜欢以偷盗为生」"
    $ stopvoc("TEN")
    play TEN "OKA04A_TEN0004"
    $ current_voice = "voice/OKA04A_TEN0004.ogg"
    "天王寺" "「那个家伙，也是社会的被害者哟」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG02N1")

    show screen phonebtn
    show screen phoneSD1
    "４℃他也并不是因为喜欢才沾染上恶人的行为的。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG18E2",hold=True)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Fade(0.5,0.5,0.5,color="fff")


    hide screen phonebtn
    "今天，做出在Ｓａｍｐｏ吃霸王餐的事情，是因为没有钱。"
    window hide


    $ loadBG(0,"BG22B0",hold=True)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Fade(0.5,0.5,0.5,color="fff")


    "之所以没有钱──是因为我从中作梗，使他为转卖屋排队的工作泡了汤。"
    "如果当时能够如愿拿到工钱的话，他也不会做出吃霸王餐的事情。"
    window hide


    $ loadBG(0,"BG02N1",trans=Fade(0.5,0.5,0.5,color="fff"))

    show screen phonebtn
    show screen phoneSD1
    "因此，他沾染上犯罪的原因，在于我。"
    window hide


    $ loadBG(2,"IBGX007")



    hide screen phonebtn
    $ stopvoc("Y05")
    play voc "OKA04A_Y050000"
    $ current_voice = "voice/OKA04A_Y050000.ogg"
    "羊驼司令" "「为了正义的光辉，恶的存在是必要的」"
    "诚如司令所说。"
    "我作为正义的伙伴，惩罚了扮演恶人的４℃。"
    "可是，真的有必要做那种事吗？"
    "使用时间跳跃的话，本来就能够阻止４℃沾染上恶行的不是吗？"
    "但我们的目标应该是，连「正义伙伴」都不需要的──"
    "从一开始，就没有「恶」的存在的世界才对吧？"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0004"
    $ current_voice = "voice/OKA04A_MAY0004.ogg"
    "真由理" "「冈伦」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0016"
    $ current_voice = "voice/OKA04A_OKA0016.ogg"
    "伦太郎" "「啊啊，真由理啊」"
    window hide



    $ loadBG(2,"BG01N",hold=True)




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(3,"IBG019A",png=True,hide=False,hold=True)
    with Dissolve(.5)
    $ renpy.pause(0.5,hard=True)
    hide background-png 
    with Dissolve(.5)





    show screen phonebtn
    "不经意间，真由理已经站在我的身后。"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0005"
    $ current_voice = "voice/OKA04A_MAY0005.ogg"
    "真由理" "「又要去了吗？」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0017"
    $ current_voice = "voice/OKA04A_OKA0017.ogg"
    "伦太郎" "「……啊啊」"
    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0006"
    $ current_voice = "voice/OKA04A_MAY0006.ogg"
    "真由理" "「又要，去做正义的伙伴了吗」"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0018"
    $ current_voice = "voice/OKA04A_OKA0018.ogg"
    "伦太郎" "「这次，是为了帮助那些坏蛋们去的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA04A_MAY0007"
    $ current_voice = "voice/OKA04A_MAY0007.ogg"
    "真由理" "「我知道了。冈伦果然，很温柔呢」"
    "她的话里既没有惊讶也没有夸耀，反而让我有些害羞。"
    "我摆摆手含糊地掩饰过去。"
    $ stopvoc("OKA")
    play OKA "OKA04A_OKA0019"
    $ current_voice = "voice/OKA04A_OKA0019.ogg"
    "伦太郎" "「再见了，真由理」"
    window hide



    $ loadBG(0,"BG03A4")

    "我套上羊驼面具，戴上头套。"
    window hide
    stop bgm 
    show houden 

    play se "SGSE035L" loop

    "为了打倒真正的恶，出发──"
    hide houden 

    hide screen phoneSD1
    hide screen phonebtn
    window hide
    stop se
    stop se
    stop bgm
    call timeleap (fromtime=[8,11,19,40], totime=[8,11,7,40], fromday=[4])

    return








    return
