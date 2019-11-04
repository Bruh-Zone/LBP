label SGFD2_FEI05A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide




    $ loadBG(0,"EVX_F01A")
    play se "SGSE202"


    $ date="8/13"
    $ day="FRI"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("MIX")
    play KUR "FEI05A_MIX0000"
    $ current_voice = "voice/FEI05A_MIX0000.ogg"
    "菲利斯＆真由理" "「欢迎回来、主人♪　大小姐♪」\n「欢迎回来、主人♪　大小姐♪」"
    window hide
    play bgm "BGM18"



    $ loadBG(2,"BG28A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") at left_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at right_q1 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at left_q1 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0000"
    $ current_voice = "voice/FEI05A_RUK0000.ogg"
    "琉华" "「大家一起来了哦，菲利斯，真由里」"
    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0000"
    $ current_voice = "voice/FEI05A_DAR0000.ogg"
    "至" "「听说今天菲利斯碳隔了好久才在店里出现一次，就赶来了！」"
    $ stopvoc("MOE")
    play MOE "FEI05A_MOE0000"
    $ current_voice = "voice/FEI05A_MOE0000.ogg"
    "萌郁" "「…………」"
    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0001"
    $ current_voice = "voice/FEI05A_RUK0001.ogg"
    "琉华" "「已经没事了吗？」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0001"
    $ current_voice = "voice/FEI05A_FEI0001.ogg"
    "菲利斯" "「在说什么呢喵。菲利斯可是一直很精神的喵♪」"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISA01"),"True","lh/CRS_ISA01a~ipad.png") at right_q2 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSB01"),"True","lh/OKA_BSB01a~ipad.png") at right_q1 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0000"
    $ current_voice = "voice/FEI05A_OKA0000.ogg"
    "伦太郎" "「哦，你们终于来了啊，嘎嘎嘎！」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0000"
    $ current_voice = "voice/FEI05A_CRS0000.ogg"
    "红莉栖" "「还真都来了啊！？明明不来也没事的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0002"
    $ current_voice = "voice/FEI05A_RUK0002.ogg"
    "琉华" "「听说你们两位又开始活动了，过来加油」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0001"
    $ current_voice = "voice/FEI05A_DAR0001.ogg"
    "至" "「那份打工不做也没关系吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0001"
    $ current_voice = "voice/FEI05A_OKA0001.ogg"
    "伦太郎" "「和Ｍｒ．布朗已经约好了。在盂兰盆节的这段期间作为怪异事件动来搞热秋叶原的气氛」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0001"
    $ current_voice = "voice/FEI05A_CRS0001.ogg"
    "红莉栖" "「虽说必须去各个店铺里去宣传，但我们还是每天为这个店宣传一次。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0002"
    $ current_voice = "voice/FEI05A_DAR0002.ogg"
    "至" "「从那已经过了３天了啊……」"
    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0003"
    $ current_voice = "voice/FEI05A_RUK0003.ogg"
    "琉华" "「阿万音也是突然不见了，感觉很匆忙的样子……」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0002"
    $ current_voice = "voice/FEI05A_FEI0002.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0002"
    $ current_voice = "voice/FEI05A_CRS0002.ogg"
    "红莉栖" "「漆原」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0004"
    $ current_voice = "voice/FEI05A_RUK0004.ogg"
    "琉华" "「啊，对不起，菲利斯……」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0003"
    $ current_voice = "voice/FEI05A_FEI0003.ogg"
    "菲利斯" "「诶？　啊，请不要在意喵，琉华喵」"
    "虽然那样说，但也掩盖不了自己的真实想法，已经察觉到的牧濑和大家也没有再说什么。"
    "只有真由里好像想到什么似的说道。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_BSB03"),"True","lh/MAY_BSB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "FEI05A_MAY0001"
    $ current_voice = "voice/FEI05A_MAY0001.ogg"
    "真由理" "「这么说来，真由喜有点不明白了喵……最后，人间蒸发的都市传说到底是怎么回事喵？」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0004"
    $ current_voice = "voice/FEI05A_FEI0004.ogg"
    "菲利斯" "「只是车站的管理员偶尔进到那里去了，被委员会的人当成了人间蒸发的样子喵」"
    $ stopvoc("MAY")
    play MAY "FEI05A_MAY0002"
    $ current_voice = "voice/FEI05A_MAY0002.ogg"
    "真由理" "「但是但是，据说那里确实有枪击的痕迹啊……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISA01"),"True","lh/CRS_ISA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAVAGEH"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAVAGEH"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SAVAGEH"])
    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0005"
    $ current_voice = "voice/FEI05A_RUK0005.ogg"
    "琉华" "「难道是在玩吗？{color=#f00}生存游戏{/color}吗？」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0003"
    $ current_voice = "voice/FEI05A_CRS0003.ogg"
    "红莉栖" "「也许是太黑了看错了吧」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0005"
    $ current_voice = "voice/FEI05A_FEI0005.ogg"
    "菲利斯" "「恩……是那样吧喵？」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0004"
    $ current_voice = "voice/FEI05A_CRS0004.ogg"
    "红莉栖" "「嘛，哪位还说是恐怖分子的秘密基地呢」"
    window hide
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSB01"),"True","lh/OKA_BSB01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0002"
    $ current_voice = "voice/FEI05A_OKA0002.ogg"
    "伦太郎" "「恩，那是机关的隐蔽处，一定是这样」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISB01"),"True","lh/CRS_ISB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0005"
    $ current_voice = "voice/FEI05A_CRS0005.ogg"
    "红莉栖" "「看吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0003"
    $ current_voice = "voice/FEI05A_OKA0003.ogg"
    "伦太郎" "「不————对！　就是机关的隐蔽处。一定是不用后把证据都处理了……！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0003"
    $ current_voice = "voice/FEI05A_DAR0003.ogg"
    "至" "「是啊……才怪嘞」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISA01"),"True","lh/CRS_ISA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0006"
    $ current_voice = "voice/FEI05A_CRS0006.ogg"
    "红莉栖" "「真的有啊，怀着学校被恐怖分子占领这种妄想的人」"
    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0004"
    $ current_voice = "voice/FEI05A_OKA0004.ogg"
    "伦太郎" "「你在说啥！」"
    window hide
    play se "SGSE809"

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "谁的电话响起来了，然后大家都看着把手伸进口袋的桶子。"
    $ stopvoc("OKA")
    play OKA "FEI05A_OKA0005"
    $ current_voice = "voice/FEI05A_OKA0005.ogg"
    "伦太郎" "「居然有Ｌａｂｍｅｍ以外的人给桶子发邮件……！？」"
    $ stopvoc("CRS")
    play CRS "FEI05A_CRS0007"
    $ current_voice = "voice/FEI05A_CRS0007.ogg"
    "红莉栖" "「等等，这里也有个什么都想发邮件的人在啊！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "听着这句话我们一齐看向了桐生。然而桐生一副非常无辜的表情使劲摇着头否定着。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0004"
    $ current_voice = "voice/FEI05A_DAR0004.ogg"
    "至" "「真失礼啊……。来的是交通信息的邮件」"
    "紧张的空气被这一句话打破了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0005"
    $ current_voice = "voice/FEI05A_DAR0005.ogg"
    "至" "「中央线发生人身事故了，好像全线暂停运转」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0006"
    $ current_voice = "voice/FEI05A_FEI0006.ogg"
    "菲利斯" "「全线暂停运转？」"
    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0006"
    $ current_voice = "voice/FEI05A_DAR0006.ogg"
    "至" "「好像是。全线倒是不常见啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0007"
    $ current_voice = "voice/FEI05A_DAR0007.ogg"
    "至" "「……怎么了，菲利斯炭？」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0007"
    $ current_voice = "voice/FEI05A_FEI0007.ogg"
    "菲利斯" "「今天是……半年不见的妈妈回来的日子喵」"
    window hide
    hide lh7 

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI05A_RUK0006"
    $ current_voice = "voice/FEI05A_RUK0006.ogg"
    "琉华" "「啊……那确实有点担心」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "恩，今天是重要的日子。"
    "那天，铃羽留下了信息。"
    "难得能变得坦率了了，想带着自己真正的想法去解决隔阂。"
    "所以我接受的她的⁮意见，去面对妈妈。"
    "现在为止都是十分小心处事，妈妈回来也只是做些表面上的应对。但是今天不一样。"
    "妈妈一定觉得比起我来觉得工作更为重要。"
    "但是现在就算被那样说也没有关系。"
    "怀着和铃羽的回忆，现在我的话……"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0008"
    $ current_voice = "voice/FEI05A_FEI0008.ogg"
    "菲利斯" "「真由喜，店稍微拜托一下了喵」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI05A_DAR0008"
    $ current_voice = "voice/FEI05A_DAR0008.ogg"
    "至" "「要去哪里啊，菲利斯炭」"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0009"
    $ current_voice = "voice/FEI05A_FEI0009.ogg"
    "菲利斯" "「按照预定应该到了喵，稍微去看看喵」"
    window hide

    stop bgm 



    $ loadBG(0,"BG16A1")

    play bgm "BGM05"
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)





    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0010"
    $ current_voice = "voice/FEI05A_FEI0010.ogg"
    "菲利斯" "「妈妈现在在哪？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020000"
    $ current_voice = "voice/FEI05A_X020000.ogg"
    "菲利斯妈妈" "「留未穗？　我回来了，没想到你会来电话，怎么了吗？」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0011"
    $ current_voice = "voice/FEI05A_FEI0011.ogg"
    "菲利斯" "「……说回来了，也就是已经到了吗？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020001"
    $ current_voice = "voice/FEI05A_X020001.ogg"
    "菲利斯妈妈" "「刚才啊。到电车那里了，车站里迷路的时候被通知发生人身事故了。航班也延迟了真是够呛，已经告诉我了哦」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0012"
    $ current_voice = "voice/FEI05A_FEI0012.ogg"
    "菲利斯" "「告诉你……黑木吗？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020002"
    $ current_voice = "voice/FEI05A_X020002.ogg"
    "菲利斯妈妈" "「恩……话说回来，其实啊留未穗，今天其实还有客人」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0013"
    $ current_voice = "voice/FEI05A_FEI0013.ogg"
    "菲利斯" "「客人？　等一下，我还以为好不容易可以和妈妈好好说上两句的？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020003"
    $ current_voice = "voice/FEI05A_X020003.ogg"
    "菲利斯妈妈" "「对不起呢，但是我希望你好好听我说」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0014"
    $ current_voice = "voice/FEI05A_FEI0014.ogg"
    "菲利斯" "「恩……恩」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020004"
    $ current_voice = "voice/FEI05A_X020004.ogg"
    "菲利斯妈妈" "「以前和你说过的，爸爸的恩人。以前商店街的做保镖的那个人……」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0015"
    $ current_voice = "voice/FEI05A_FEI0015.ogg"
    "菲利斯" "「妈妈，那个人是……黑猫？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020005"
    $ current_voice = "voice/FEI05A_X020005.ogg"
    "菲利斯妈妈" "「啊，好像是这个名字。总之啊，那个人１０年前生了病，在国外接受着治疗。」"
    $ stopvoc("X02")
    play KUR "FEI05A_X020006"
    $ current_voice = "voice/FEI05A_X020006.ogg"
    "菲利斯妈妈" "「但是爸爸１０年前呢……所以妈妈一直代替爸爸，到现在都在照顾着那个人」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0016"
    $ current_voice = "voice/FEI05A_FEI0016.ogg"
    "菲利斯" "「是这样啊……」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020007"
    $ current_voice = "voice/FEI05A_X020007.ogg"
    "菲利斯妈妈" "「对不起，一直没有告诉你。多亏那人已经可以恢复到暂时出院了，机会难得所以就请她来家里了。」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0017"
    $ current_voice = "voice/FEI05A_FEI0017.ogg"
    "菲利斯" "「妈妈去海外不是为了工作吗？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020008"
    $ current_voice = "voice/FEI05A_X020008.ogg"
    "菲利斯妈妈" "「两方都有。所以把你拜托给黑木了……」"
    $ stopvoc("X02")
    play KUR "FEI05A_X020009"
    $ current_voice = "voice/FEI05A_X020009.ogg"
    "菲利斯妈妈" "「到现在为止一直让你分担妈妈那份辛苦。对不起啊，留未穗……」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0018"
    $ current_voice = "voice/FEI05A_FEI0018.ogg"
    "菲利斯" "「妈妈……」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020010"
    $ current_voice = "voice/FEI05A_X020010.ogg"
    "菲利斯妈妈" "「但是我很放心，听黑木说你做的很好不是吗。」"
    $ stopvoc("X02")
    play KUR "FEI05A_X020011"
    $ current_voice = "voice/FEI05A_X020011.ogg"
    "菲利斯妈妈" "「一直觉得你还是个孩子，不知不觉已经长成大人了……」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0019"
    $ current_voice = "voice/FEI05A_FEI0019.ogg"
    "菲利斯" "「没有那回事……」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020012"
    $ current_voice = "voice/FEI05A_X020012.ogg"
    "菲利斯妈妈" "「对不起啊，留未穗。一直没有好好照顾你……」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0020"
    $ current_voice = "voice/FEI05A_FEI0020.ogg"
    "菲利斯" "「不……我才是，要说对不起」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020013"
    $ current_voice = "voice/FEI05A_X020013.ogg"
    "菲利斯妈妈" "「好的，就期待今晚妈妈做的饭吧。蛋包饭，你喜欢那个吧」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0021"
    $ current_voice = "voice/FEI05A_FEI0021.ogg"
    "菲利斯" "「妈妈现在在做什么？」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020014"
    $ current_voice = "voice/FEI05A_X020014.ogg"
    "菲利斯妈妈" "「买东西哦，买东西。所以想让留未穗照看下客……」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0022"
    $ current_voice = "voice/FEI05A_FEI0022.ogg"
    "菲利斯" "「没事的，妈妈。交给我吧」"

    $ stopvoc("X02")
    play KUR "FEI05A_X020015"
    $ current_voice = "voice/FEI05A_X020015.ogg"
    "菲利斯妈妈" "「恩，太好了，那我大概３０分钟以后回来」"

    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0023"
    $ current_voice = "voice/FEI05A_FEI0023.ogg"
    "菲利斯" "「恩，等着你哦」"
    window hide


    call hide_phone
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0024"
    $ current_voice = "voice/FEI05A_FEI0024.ogg"
    "菲利斯" "「……客人、吗」"
    "果然还是母子２人最好...."
    window hide

    stop bgm 



    $ loadBG(0,"BG26A")

    "我打开房门，问了下黑木关于来客的事。"
    "她在客厅里的样子，我一边想着首先该说些什么一边走了进去。"
    "大概是「初次见面」。"
    "或者是「Ｈｅｌｌｏ」？"
    "恩，感觉有点难办……"
    "但是看到坐在桌前的那个人的背影的时候，什么想法都烟消云散了。"
    "……在哪里见过的样子，有这种感觉。"
    "娇小而又优雅，有种很可靠感觉的双肩。"
    "在哪见过的辫子。"
    $ stopvoc("FEI")
    play FEI "FEI05A_FEI0025"
    $ current_voice = "voice/FEI05A_FEI0025.ogg"
    "菲利斯" "「那、那个……」"
    play bgm "FD2BGM09"
    "那个人转过头来，我不由得吃了一惊。"
    "年过５０的样子，在眼睛和脸颊边上都有了皱纹，但是那双眼睛的光芒……不会错……"
    "——是『她』。"
    "『她』温柔地眼神看着一动不动的我。"
    "突然脑中一片空白。"
    "张口结舌。"
    "『她』也是一样。"
    "『她』看着我，无声地站了起来。"
    "脸上老泪纵横。"
    "就像是一直压抑住的情感突然爆发了出来那样，控制不住……"
    "我无意识地向『她』走了过去。"
    "『她』也走了过来。"
    "然后用和之前毫无变化的声音说道。"
    $ stopvoc("SUZ")
    play SUZ "FEI05A_SUZ0000"
    $ current_voice = "voice/FEI05A_SUZ0000.ogg"
    "铃羽" "「什么都没说就消失了真是抱歉啊、……Ｂｏｓｓ」"
    "那个瞬间，我无言地抱住铃羽——"

    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI005A"]]["Check"]=True
    show expression "bg/EV_FEI005A~ipad.jpg" as ev :
        yalign 1.0
        linear 2.0yalign 0.0
    $ loadBG(0,"BG_BLACK",trans=fade)
    show screen invisible
    $ renpy.movie_cutscene("video/imv10.avi")
    hide screen invisible
    "「桃色幻都的黑猫·完成」"




















    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade

    return
