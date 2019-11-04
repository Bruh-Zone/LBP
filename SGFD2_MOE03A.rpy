label SGFD2_MOE03A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG05A3")

    play se "SGSE200L" loop


    $ date="8/8"
    $ day ="SUN"
    python:
        RcvMail(145)
        ReadMail(145)
    show screen phonebtn
    show screen phoneSD1

    "小心地避免发出脚步声，我轻轻地走上了Ｌａｂ的楼梯。"
    "这个时间点的话，Ｌａｂ里应该是没有人的。"
    window hide


    $ loadBG(2,"BG_BLACK")


    "钥匙……在了。"
    "在电表的箱子里。被藏在那里了。"
    "以前看的刑事剧派上了用场。"
    "现在，无疑是个机会。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2


    "我又确认了一次今天早上ＦＢ发来的邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_RECV_TEN01"]
    call read_last_mail




    "时间机器……"
    "那种东西是真实存在的，昨天的我还难以相信。"
    "但是……亲眼所见，我无法反驳。"
    "就算不是ＦＢ，应该也有很多想要毁掉它的人。"
    window hide
    call hide_phone

    "所以说——"
    "我用钥匙打开了Ｌａｂ的门，静静地闯进了室内。"
    window hide
    stop se


    $ loadBG(0,"BG01A")


    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0000"
    $ current_voice = "voice/MOE03A_MAY0000.ogg"
    "？？？" "「咦？」"
    "走进Ｌａｂ以后，我注意到了有人在那里。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0001"
    $ current_voice = "voice/MOE03A_MAY0001.ogg"
    "真由理" "「啊、是萌郁啊♪」"
    play bgm "FD2BGM05"

    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0000"
    $ current_voice = "voice/MOE03A_MOE0000.ogg"
    "萌郁" "「！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0002"
    $ current_voice = "voice/MOE03A_MAY0002.ogg"
    "真由理" "「萌郁、嘟嘟噜♪」"
    "椎名……这个点为什么会在这里？"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0003"
    $ current_voice = "voice/MOE03A_MAY0003.ogg"
    "真由理" "「怎么了吗？这么早来Ｌａｂ。」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0001"
    $ current_voice = "voice/MOE03A_MOE0001.ogg"
    "萌郁" "「……醒来以后没有什么事情能做所以过来了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0004"
    $ current_voice = "voice/MOE03A_MAY0004.ogg"
    "真由理" "「是这样吗？　起得真早啊」"
    "椎名好像完全没有怀疑的样子对我笑脸相迎。"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0002"
    $ current_voice = "voice/MOE03A_MOE0002.ogg"
    "萌郁" "「椎名也……来得很早呢。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COMIMA"])
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0005"
    $ current_voice = "voice/MOE03A_MAY0005.ogg"
    "真由理" "「真由喜因为要制作{color=#f00}夏Ｃｏｍｉ{/color}的服装所以留宿在这里了哟。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0006"
    $ current_voice = "voice/MOE03A_MAY0006.ogg"
    "真由理" "「所以说，所以说啊。锵！　终于完成了♪」"
    "这真是预想以外的展开……椎名在Ｌａｂ什么里的。"
    "这样就不能随便摆弄电话微波炉了。"
    "趁她不注意的时候，把电话微波炉破坏掉？"
    "虽然应该马上会暴露，但装作是不小心弄坏的话……"
    "但是……"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET"])
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0007"
    $ current_voice = "voice/MOE03A_MAY0007.ogg"
    "真由理" "「啊，看呀看呀。这次用的服装是{color=#f00}雷Ｎｅｔ翔{/color}的── 」"
    "椎名一直不停地和我说着话。根本没有什么空隙可以让我那么做。"


    hide screen phonebtn
    "为啥今天刚好她就留宿在这里啊？"
    "而且还和没有怎么说过话的我一直这样搭话，真奇怪。"
    "！？　难道说……"
    "她受 Ｌａｂｍｅｍ 的命令，来监视我的行动？"
    "这种可能性很高。"
    "能通过向过去发送邮件来改变世界的机器，不可能毫无防备地被放在这里。"
    "这样的话……必须从椎名身边离开。"

    show screen phonebtn
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0003"
    $ current_voice = "voice/MOE03A_MOE0003.ogg"
    "萌郁" "「椎……椎名」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0008"
    $ current_voice = "voice/MOE03A_MAY0008.ogg"
    "真由理" "「嗯？　怎么了萌郁？」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0004"
    $ current_voice = "voice/MOE03A_MOE0004.ogg"
    "萌郁" "「我……不擅长，和别人说话」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0005"
    $ current_voice = "voice/MOE03A_MOE0005.ogg"
    "萌郁" "「所以说……那个……能不能稍微让我静一下」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0009"
    $ current_voice = "voice/MOE03A_MAY0009.ogg"
    "真由理" "「啊……说起来是呢」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0010"
    $ current_voice = "voice/MOE03A_MAY0010.ogg"
    "真由理" "「没有注意到真抱歉呢。这个是真由喜的坏习惯的说。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0011"
    $ current_voice = "voice/MOE03A_MAY0011.ogg"
    "真由理" "「那个……诶嘿嘿。那么，真由喜就去吃早饭了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0012"
    $ current_voice = "voice/MOE03A_MAY0012.ogg"
    "真由理" "「萌郁，有什么事的话请尽管说哦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "这么说着椎名开始匆匆忙忙地准备起了早餐。"
    "现在就是破坏电话微波炉的机会。"
    window hide


    $ loadBG(2,"BG02A1")



    "背朝着椎名，我向电话微波炉走去。"
    "但是——为什么呢。感觉心总牵挂着她。"
    window hide


    $ loadBG(2,"BG01A")


    "回头看见椎名的背影，总觉得有一种平静下来的感觉。"
    "看着她的背影……不知为何，有一种被吸引的感觉。"
    window hide


    $ loadBG(2,"BG02A1")



    "反复看了几遍眼前的电话微波炉和背后的椎名之后——我取出了手机。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2











    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_SEND_MAY01"]
    call send_mail (id=[146,147,148,149,150])








    play se "SGSE803"

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0013"
    $ current_voice = "voice/MOE03A_MAY0013.ogg"
    "真由理" "「咦？　是萌郁发过来的邮件啊。」"
    "昨天，集合后我与全员交换了邮件地址。"
    "没想到会在这个地方发挥作用。"
    stop se
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0014"
    $ current_voice = "voice/MOE03A_MAY0014.ogg"
    "真由理" "「……是吗。是这样啊。」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "我转过身去，背朝着电话微波炉，脸朝着椎名。"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0006"
    $ current_voice = "voice/MOE03A_MOE0006.ogg"
    "萌郁" "「那个……刚才的发言……请允许我撤回」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0007"
    $ current_voice = "voice/MOE03A_MOE0007.ogg"
    "萌郁" "「就像邮件里所说的那样……其实，我还是想和Ｌａｂｍｅｍ的大家好好相处的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0015"
    $ current_voice = "voice/MOE03A_MAY0015.ogg"
    "真由理" "「真的吗！？　太好了♪」"
    "椎名立刻喜笑颜开。"
    "然后——"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0016"
    $ current_voice = "voice/MOE03A_MAY0016.ogg"
    "真由理" "「然后呢……给你，这个♪」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0017"
    $ current_voice = "voice/MOE03A_MAY0017.ogg"
    "真由理" "「真由喜最喜欢的食物，多汁炸鸡Ｎo.１，一起吃吧？」"
    "她向我递出装着炸鸡块的小小器皿。"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0008"
    $ current_voice = "voice/MOE03A_MOE0008.ogg"
    "萌郁" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0018"
    $ current_voice = "voice/MOE03A_MAY0018.ogg"
    "真由理" "「诶？　难道说，不喜欢吃炸鸡？」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0009"
    $ current_voice = "voice/MOE03A_MOE0009.ogg"
    "萌郁" "「并不是那样……」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0019"
    $ current_voice = "voice/MOE03A_MAY0019.ogg"
    "真由理" "「？」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0010"
    $ current_voice = "voice/MOE03A_MOE0010.ogg"
    "萌郁" "「为什么……对我这么温柔？」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0011"
    $ current_voice = "voice/MOE03A_MOE0011.ogg"
    "萌郁" "「明明我刚才……对你说了这么过分的话……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB01"),"True","lh/MAY_CMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0020"
    $ current_voice = "voice/MOE03A_MAY0020.ogg"
    "真由理" "「诶？　理由什么的很简单哟」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0021"
    $ current_voice = "voice/MOE03A_MAY0021.ogg"
    "真由理" "「因为呢，直到刚才 Ｌａｂ 里只有真由喜一个人，非常的寂寞呢。萌郁来了真由喜非常开心哦♪」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0012"
    $ current_voice = "voice/MOE03A_MOE0012.ogg"
    "萌郁" "「…………」"
    "听着椎名的话，我忽地想起了过去的自己。"
    "我那时也……直到收到ＦＢ的邮件之前，一直都是只身一人住在房间里。"
    "独自一人的房间里，谁也不会前来造访，只是抱着膝盖度过的每一日。"
    "我被ＦＢ的那封邮件从那样的孤独里拯救出来。"
    "椎名刚刚难道也是被我救了吗？"
    "就好像我被ＦＢ拯救了那样，椎名……因我来到这里这件事而高兴起来了？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0022"
    $ current_voice = "voice/MOE03A_MAY0022.ogg"
    "真由理" "「呐呐、萌郁」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0013"
    $ current_voice = "voice/MOE03A_MOE0013.ogg"
    "萌郁" "「……怎么了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0023"
    $ current_voice = "voice/MOE03A_MAY0023.ogg"
    "真由理" "「那个呢，真由喜想和萌郁，成为更好的朋友呢」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0014"
    $ current_voice = "voice/MOE03A_MOE0014.ogg"
    "萌郁" "「…………」"
    "椎名那天真无邪的笑容。"
    "自然能感受到她是真心的。"
    "然而——"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0015"
    $ current_voice = "voice/MOE03A_MOE0015.ogg"
    "萌郁" "「我觉得……我没有被那样对待的资格……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA04"),"True","lh/MAY_CMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0024"
    $ current_voice = "voice/MOE03A_MAY0024.ogg"
    "真由理" "「诶？　没有那种事哟」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0016"
    $ current_voice = "voice/MOE03A_MOE0016.ogg"
    "萌郁" "「因为……因为我……」"
    "正欺骗着你们啊。"
    "绝对不能说出口的话语卡在了喉咙里……微妙地难受起来了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0025"
    $ current_voice = "voice/MOE03A_MAY0025.ogg"
    "真由理" "「萌郁」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0017"
    $ current_voice = "voice/MOE03A_MOE0017.ogg"
    "萌郁" "「……怎么了？」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0026"
    $ current_voice = "voice/MOE03A_MAY0026.ogg"
    "真由理" "「萌郁果然，很温柔呢」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0018"
    $ current_voice = "voice/MOE03A_MOE0018.ogg"
    "萌郁" "「才没有……那种事」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0027"
    $ current_voice = "voice/MOE03A_MAY0027.ogg"
    "真由理" "「不哦。因为刚才，真由喜看起来有些丧气的时候，还担心着我呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0028"
    $ current_voice = "voice/MOE03A_MAY0028.ogg"
    "真由理" "「像萌郁这样的人能成为Ｌａｂｍｅｍ我很开心哦」"
    $ stopvoc("MAY")
    play MAY "MOE03A_MAY0029"
    $ current_voice = "voice/MOE03A_MAY0029.ogg"
    "真由理" "「谢谢你能来到Ｌａｂ♪」"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0019"
    $ current_voice = "voice/MOE03A_MOE0019.ogg"
    "萌郁" "「……」"
    "我，欺骗着她们。"
    "她们……她们也一定在欺骗着我。一定是这样的。"
    "ＦＢ是这么说的。ＦＢ永远是正确的。"

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG34N1")
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_EDIT_TEN01_00"]



    show screen phoneSD1
    "回到自己的房间以后，我将在Ｌａｂ里遇到了椎名的事，没能破坏电话微波炉的事，以及……她的不可思议的言行相关的事，通过邮件向ＦＢ进行了报告。"
    window hide
    call send_mail (id=[151,152,153])
    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_SEND_TEN01"]






    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_RECV_TEN02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    "马上收到了回信。"
    window hide
    call read_last_mail


    "来自ＦＢ的回信里，一如既往的是挂念着我的充满柔情的内容。"
    "但是……那些内容不知为何让我有些生气。"
    "椎名真的在欺骗着我吗？"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_EDIT_TEN02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MOE03A_SEND_TEN02"]
    call send_mail (id=[156,157,158], send=False)


    "注意到的时候，我发现我正在写着质疑ＦＢ的说法的邮件。"
    "但是……"
    $ stopvoc("MOE")
    play MOE "MOE03A_MOE0020"
    $ current_voice = "voice/MOE03A_MOE0020.ogg"
    "萌郁" "「……」"
    play bgm "FD2BGM08"
    "像母亲一样接近这样的我的ＦＢ。"
    "将我从孤独中拯救出来的ＦＢ。"
    "向那样的她发送这种邮件简直就是……恩将仇报。"
    "这封邮件说不定会让她生气。"
    "如果被她讨厌的话，我就真的不愿意苟活于世了。"

    "还是算了吧。"
    "仔细想想的话，ＦＢ说的是真的的可能性也并非为零。"
    "一定是今天我太感性了。"
    window hide

    "嘛……现在睡一觉也许会更好一些。"
    "但今天就算是上床睡觉都感到很麻烦。"
    "就这么闭上眼睛，很快就会睡着的吧。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "不要想多余的东西啊，我。"
    "明天的话——不管结果如何，都要向ＦＢ交一份好报告。"
    "抱着膝盖闭上眼的时候，不知为何，脑海中浮现出了椎名的温柔笑颜。"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
