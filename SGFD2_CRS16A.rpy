label SGFD2_CRS16A:
    window hide


    $ loadBG(0,"BG03A4")

    play bgm "BGM15"

    $ date="8/14"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0000"
    $ current_voice = "voice/CRS16A_CRS0000.ogg"
    "红莉栖" "「接下来，该这样……嗯。」"
    "之后，我们做了各种各样的准备，回到了Ｌａｂ──时间跳跃机前。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA01"),"True","lh/FEI_BSA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS16A_FEI0000"
    $ current_voice = "voice/CRS16A_FEI0000.ogg"
    "菲利斯" "「红喵，已确认下面的巨大电视机接上电源了喵。」"
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0001"
    $ current_voice = "voice/CRS16A_CRS0001.ogg"
    "红莉栖" "「谢谢。这下飘升机也准备OK。」"
    "说罢，我启动了时间跳跃机。之后就只要戴上耳机，按下键盘上的回车键就行了。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC01"),"True","lh/FEI_BSC01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS16A_FEI0001"
    $ current_voice = "voice/CRS16A_FEI0001.ogg"
    "菲利斯" "「终于到最后了喵……」"
    "菲利斯紧紧握住我的手。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0002"
    $ current_voice = "voice/CRS16A_CRS0002.ogg"
    "红莉栖" "「嗯，跨世纪的一瞬间呢。」"
    "因为冈部已经用过时间跳跃机了，算不上世界的首次。但毫无疑问，这正是时间旅行实验黎明前的瞬间。"
    "而我就是先驱者之一。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "至今为止的恐怖，都已销声匿迹，反倒是兴奋感和好奇心环绕着我。"
    "然而与此同时──"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS004A"]]["Check"]=True
    $ loadBG(0,"EV_CRS004A")

    "进行时间跳跃后，我和爸爸的和解、得到便携叉子，都将变成不曾发生过的事。"
    "因为我现在的记忆会传送给那个与爸爸谈话之前时间点的自己。"
    "那之后的我，不是要和爸爸和解，而是要全力地帮助冈部。"
    window hide


    $ loadBG(0,"BG_BLACK")

    "如果，不进行时间跳跃──"
    "我会同已经接受了真由理的死、重新振作起来的冈部一起去青森吧。虽然不知道要多久。"
    "一不小心就想了这么多。"
    "然后，我把心中的这些混沌好好封了起来。"
    "作为研究者的本能与骄傲……对父亲的思念……"
    "比起这些，我有更为重要的东西。"
    "──这样，就好了吧，爸爸。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0003"
    $ current_voice = "voice/CRS16A_CRS0003.ogg"
    "红莉栖" "「冈部……真由里……桥田……」"


    window hide


    $ loadBG(0,"IBGX033")

    "一切就看我下来的行动了。"
    "目标是昨天，下午５点半左右。"
    "一切都染上黄昏色之时。"
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0004"
    $ current_voice = "voice/CRS16A_CRS0004.ogg"
    "红莉栖" "「也就是说，冈部不分昼夜地，在这狭窄的时间里……」"
    "由于黄昏之时不属于昼和夜的任何一边，所以人的眼睛无法很好地调和光线，因此其叫法变化成了“奄奄黄昏”，就是这样的一个时间段。"
    "我又想起了维克多·孔多利亚一个前辈告诉我的他国神话故事。"
    "某天，雷神与魔族做了协定。协定内容是，在昼与夜，无论干燥之物还是潮湿之物都不会伤到魔族。"
    "所以雷神为了打倒魔族，在既非昼也非夜的傍晚时间──"
    "使用了即非干燥也非潮湿的海之泡沫所造出的武器。"
    "一说，魔族得到了“不会被人、神、兽及魔族杀死，无论在昼与夜、在家内与在家外都不会被杀死的身体”。"
    "为了杀死魔族，某个神变化为非人非兽的、狮子和人的融合姿态，在非昼非夜的傍晚──"
    "在非家内也非家外的、房子的门口处打倒了魔族。"
    "前辈是这样说的。"
    "这个神话的寓意大概是，当被迫二选一的时候，该冷静下来考虑，选项真的只有两个吗。"
    "冷静下来思考，或是换一条思路，必定能看到第三个选项。"
    "解开看起来近乎不可能的多重因果缠绕之线，找到正解，这情况还真是与黄昏之时相称。"
    window hide


    $ loadBG(0,"BG03A4")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0005"
    $ current_voice = "voice/CRS16A_CRS0005.ogg"
    "红莉栖" "「……什么的，有这种想法的我也真是的。」"
    "嘛，没办法。原本研究者就大多是浪漫和厨二病的结晶。被这种人包围着，多少有点被同化了。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC01"),"True","lh/FEI_BSC01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS16A_FEI0002"
    $ current_voice = "voice/CRS16A_FEI0002.ogg"
    "菲利斯" "「怎么啦？红喵。」"
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0006"
    $ current_voice = "voice/CRS16A_CRS0006.ogg"
    "红莉栖" "「嗯，没什么。那么，我要跳跃了。之后的就拜托你了。」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA02"),"True","lh/FEI_BSA02a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS16A_FEI0003"
    $ current_voice = "voice/CRS16A_FEI0003.ogg"
    "菲利斯" "「包在我身上喵！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我轻轻笑了笑，戴上了耳机。"
    show houden 

    stop bgm 

    play se "SGSE035L" loop


    play se "SGSE049L" loop
    "放电现象发生，青白色的光在周围乱舞。脚下剧烈地震动起来。"
    $ stopvoc("CRS")
    play CRS "CRS16A_CRS0007"
    $ current_voice = "voice/CRS16A_CRS0007.ogg"
    "红莉栖" "「走了！」"
    "我按下键盘的回车键。"
    "地震般的动摇晃动着我的身体。"
    "就连身体都要被甩出去的冲击。"
    "不光是记忆，仿佛连肉体都要跳跃了。"
    "不对，跳跃的是──"
    "世界？"


    play se "SGSE067"


    play se "SGSE053L" loop

    stop se


    play se "SGSE013"

    hide screen phoneSD1
    window hide


    hide screen phonebtn


    hide houden 
    hide screen phonebtn
    hide screen phoneSD1
    window hide
    stop se
    stop se
    stop bgm
    call timeleap (fromtime=[8,14,14,15], totime=[8,13,17,15], fromday=[6])

    return







    window hide





    return
















































































    return
