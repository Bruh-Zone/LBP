    transform scrolldown:
        yalign 0.0
        linear 0.5yalign 1.0
    label SGFD2_CRS08A:
    window hide


    $ loadBG(0,"BG27N",at=[Transform(yalign=0.0)])





    play bgm "BGM26"

    $ date="8/13"
    hide screen phonebtn
    show screen phoneSD1

    "秋叶原Ｔｉｍｅｓ　Ｔｏｗｅｒ。秋叶原最高的分售式公寓，在最顶层连东京塔和富士山都能尽收眼底。"
    "这个离秋叶原车站很近的高楼最顶层，就是菲利斯的家。"
    "高级公寓，还有门卫驻守着，确实是比大桧山大楼安全的地方。"
    window hide





    $ loadBG(0,"BG27N",at=[scrolldown])
    "当前状态下，整个秋叶原中最能放心安置冈部的地方大概就是这里了。"
    window hide
    play se "SGSE094"




    $ loadBG(0,"BG_BLACK")

    "在路上，菲利斯进行了联络后，她父亲已经回家了。"
    "因此，一些基本的事情已经安排好了，详细情况等见面后再说。"
    window hide


    $ loadBG(0,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0000"
    $ current_voice = "voice/CRS08A_FPP0000.ogg"
    "菲利斯父亲" "「留未穂！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSB01"),"True","lh/FEI_BSB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS08A_FEI0000"
    $ current_voice = "voice/CRS08A_FEI0000.ogg"
    "菲利斯" "「爸爸！」"
    "留未穗……这是菲利斯的真名吗？"
    "菲利斯的父亲——张开双臂以拥抱迎接女儿归来。"
    "看到这种在日本少有的亲情流露，我的内心深处泛起了难以言喻的什么东西。"
    "——我明明是可以明白那是什么的。"
    "就算再怎么不愿意承认，那种感情的真面目我还是知道的。"
    "……不过，现在不是想这种事的时候。"
    window hide


    $ loadBG(0,"BG_BLACK")

    "我帮着黑木先生，将冈部抬到了客房的床上。"
    "黑木先生说，待会儿会将家庭医生叫来，给冈部打一针镇静剂。"
    "我终于也松了口气。"
    "我回到了客厅，总之先跟菲利斯的父亲打个招呼。"
    window hide


    $ loadBG(0,"BG26N")

    "结束了和女儿的拥抱，菲利斯的父亲注意到我后温和地笑着伸出了手。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0001"
    $ current_voice = "voice/CRS08A_FPP0001.ogg"
    "菲利斯父亲" "「你就是留未穗的朋友吧。我是秋叶留未穗的父亲，秋叶幸高。请多关照。」"
    "很自然地握了握手。是因为在美国生活的时间长了吧，不握手的问候方式反而让我感觉不习惯了。"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0000"
    $ current_voice = "voice/CRS08A_CRS0000.ogg"
    "红莉栖" "「我是牧濑红莉栖……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0002"
    $ current_voice = "voice/CRS08A_FPP0002.ogg"
    "菲利斯父亲" "「……嗯？ 牧濑，红莉栖？」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0001"
    $ current_voice = "voice/CRS08A_CRS0001.ogg"
    "红莉栖" "「对，是的。」"
    "幸高叔叔，就这么握着我的手，微微地歪了歪头。"
    "然后仔细地端详起我的脸。"
    "难道，他身上有些ＨＥＮＴＡＩ大叔的成份吗。"
    "我正想向菲莉斯求助的时候，幸高叔叔口中冒出了一个让我深感意外的名字。"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0003"
    $ current_voice = "voice/CRS08A_FPP0003.ogg"
    "菲利斯父亲" "「你父亲的名字，是不是叫牧濑章一？」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0002"
    $ current_voice = "voice/CRS08A_CRS0002.ogg"
    "红莉栖" "「……！」"
    "诶……"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0003"
    $ current_voice = "voice/CRS08A_CRS0003.ogg"
    "红莉栖" "「为……什么……知道爸爸的名字……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0004"
    $ current_voice = "voice/CRS08A_FPP0004.ogg"
    "菲利斯父亲" "「果然是这样啊！原来是你，那个红莉栖酱，真是不得了的偶然啊。已经出落得这么漂亮了。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS08A_FEI0001"
    $ current_voice = "voice/CRS08A_FEI0001.ogg"
    "菲利斯" "「爸爸，你认识牧濑？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0005"
    $ current_voice = "voice/CRS08A_FPP0005.ogg"
    "菲利斯父亲" "「我和牧濑章一，是大学时期的朋友。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0004"
    $ current_voice = "voice/CRS08A_CRS0004.ogg"
    "红莉栖" "「骗……人……」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0006"
    $ current_voice = "voice/CRS08A_FPP0006.ogg"
    "菲利斯父亲" "「而且有一段时间，我还给他的研究提供过资助。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0007"
    $ current_voice = "voice/CRS08A_FPP0007.ogg"
    "菲利斯父亲" "「我提供资金赞助，章一进行实际研究得出成果。还有给我们做顾问的教授……可以说是我们俩的师父吧。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0005"
    $ current_voice = "voice/CRS08A_CRS0005.ogg"
    "红莉栖" "「资金……」"
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5 
    "这么一说，我似乎在小时候就听说过这些事。"
    "这正是我们家搬到青森的理由。"
    "当时，我们住在东京。爸爸不隶属于任何机构，独自进行着研究。"
    "之所以突然要搬回爸爸的老家青森，正是因为一直以来的资金赞助中止了。"
    "那，这个人就是……"
    hide bg2 

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0008"
    $ current_voice = "voice/CRS08A_FPP0008.ogg"
    "菲利斯父亲" "「在我们大学毕业之后，这个小组也维持了一段时间。章一把它称为“相对性理论超越委员会”。」"
    "第一次听说。这厨二病发作的命名是怎么回事……"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0009"
    $ current_voice = "voice/CRS08A_FPP0009.ogg"
    "菲利斯父亲" "「红莉栖酱，以前你经常被章一带着来我们家玩呢。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0010"
    $ current_voice = "voice/CRS08A_FPP0010.ogg"
    "菲利斯父亲" "「那时候的家在御茶水那边。后来我的公司遇到困难就卖掉了，当时的房子连院子都有呢。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0011"
    $ current_voice = "voice/CRS08A_FPP0011.ogg"
    "菲利斯父亲" "「你和留未穗还一起在院子里玩过呢。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS08A_FEI0002"
    $ current_voice = "voice/CRS08A_FEI0002.ogg"
    "菲利斯" "「喵！？」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0006"
    $ current_voice = "voice/CRS08A_CRS0006.ogg"
    "红莉栖" "「诶……」"
    $ stopvoc("FEI")
    play FEI "CRS08A_FEI0003"
    $ current_voice = "voice/CRS08A_FEI0003.ogg"
    "菲利斯" "「这么说的话，我和牧濑……小时候就认识了？」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0007"
    $ current_voice = "voice/CRS08A_CRS0007.ogg"
    "红莉栖" "「…………」"
    "我和菲利斯，两个人带着难以置信的表情面面相觑着。"
    "今天实在是发生了太多各种各样的事情了，感觉神经都要短路了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0012"
    $ current_voice = "voice/CRS08A_FPP0012.ogg"
    "菲利斯父亲" "「说起来，黑木你应该还记得吧？ 没有注意到她吗？」"
    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("Y13")
    play KUR "CRS08A_Y130000"
    $ current_voice = "voice/CRS08A_Y130000.ogg"
    "黒木" "「记得。虽然注意到了，当时还是优先处理冈部先生的情况了。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0013"
    $ current_voice = "voice/CRS08A_FPP0013.ogg"
    "菲利斯父亲" "「是这样啊，谢谢。多亏你照顾了女儿的朋友。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0014"
    $ current_voice = "voice/CRS08A_FPP0014.ogg"
    "菲利斯父亲" "「那么，进入正题吧。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0008"
    $ current_voice = "voice/CRS08A_CRS0008.ogg"
    "红莉栖" "「……嗯。」"
    "没错，现在……爸爸的事、我和菲利斯间意外的缘分，都先放到一边。"
    "不得不最优先考虑的，是冈部的事情。"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0009"
    $ current_voice = "voice/CRS08A_CRS0009.ogg"
    "红莉栖" "「真是抱歉，这么突然地来拜托您……」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0015"
    $ current_voice = "voice/CRS08A_FPP0015.ogg"
    "菲利斯父亲" "「哪里……你会来拜托我真是太好了。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0010"
    $ current_voice = "voice/CRS08A_CRS0010.ogg"
    "红莉栖" "「诶？」"
    window hide
    play bgm "BGM21"



    $ loadBG(2,"BG26NS1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA02"),"True","lh/FPP_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "他的语气，与刚刚关怀我时的温和语调完全不同，变得睿智又锋利。"
    "不是作为一名父亲，而是干练的实业家的面孔。"
    "他的目光像是能斩断所及一切的匕首，犹如一丝不苟俯瞰着万物的鹰之眼。"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0016"
    $ current_voice = "voice/CRS08A_FPP0016.ogg"
    "菲利斯父亲" "「留未穗和我联络的时候我也是半信半疑，为防万一我联系了信得过的人……然后呢。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0011"
    $ current_voice = "voice/CRS08A_CRS0011.ogg"
    "红莉栖" "「信得过的人……是？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KANDA_MATSURI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KANDA_MATSURI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KANDA_MATSURI"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TEKIYA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TEKIYA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TEKIYA"])

    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0017"
    $ current_voice = "voice/CRS08A_FPP0017.ogg"
    "菲利斯父亲" "「啊，是正在秋叶原举办的庙会——神田神社的{color=#f00}神田祭{/color}里，负责城内夜市{color=#f00}的屋{/color}的总管，向他了解了一下。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0018"
    $ current_voice = "voice/CRS08A_FPP0018.ogg"
    "菲利斯父亲" "「……还真是吓了我一跳，说真的。正如你们在电话里说的，警察和地铁公司受到了干涉。似乎连总管都被打了招呼。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0012"
    $ current_voice = "voice/CRS08A_CRS0012.ogg"
    "红莉栖" "「……！」"
    "已经数不清这是今天第几回被震惊了，我只能再次倒吸一口凉气。"
    "冈部的那些话，真的不得不相信了。"
    "此时此刻，当明白ＳＥＲＮ真的能给警察之类的组织施加影响时，我只能战栗不已。"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0019"
    $ current_voice = "voice/CRS08A_FPP0019.ogg"
    "菲利斯父亲" "「在你们回来之前我进行了各种调查，发现秋叶原这一带已经被封锁，出入人流都被限制了。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0020"
    $ current_voice = "voice/CRS08A_FPP0020.ogg"
    "菲利斯父亲" "「虽然表面上看起来不是那样，嘛，就跟警察的盘问差不多。」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0021"
    $ current_voice = "voice/CRS08A_FPP0021.ogg"
    "菲利斯父亲" "「这大概多半是为了抓捕想要离开秋叶原的红莉栖酱和冈部君吧。」"
    $ stopvoc("CRS")
    play CRS "CRS08A_CRS0013"
    $ current_voice = "voice/CRS08A_CRS0013.ogg"
    "红莉栖" "「抓捕……」"
    window hide


    $ loadBG(2,"BG_BLACK")




    "不寒而栗。"
    "能做到如此地步的大组织，确确实实是在盯着我们。"
    "特别是开发机器的核心人员，我、冈部和桥田３人，应该是最优先要抓捕的目标吧。"
    "这么一想，我愈发地担心起真由理和桥田来。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA02"),"True","lh/FPP_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(2,"BG26NS1",hide=False)





    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0022"
    $ current_voice = "voice/CRS08A_FPP0022.ogg"
    "菲利斯父亲" "「……你们，到底被卷入了什么事？」"
    $ stopvoc("FPP")
    play FPP "CRS08A_FPP0023"
    $ current_voice = "voice/CRS08A_FPP0023.ogg"
    "菲利斯父亲" "「我希望知道详细的情况。到底，现在秋叶原的街上，发生着什么事情。」"
    "幸高叔叔的声调中，有着少许愤怒的色彩。"
    "并不是针对我们。"
    "那是指向踏入了自己所居住、所建设的秋叶原这片土地的入侵者的愤怒。"
    "那是作为这片街区——秋叶原的居民应有的、作为守卫者的愤怒，作为护巢的雌鸟的愤怒。"

    hide screen phoneSD1
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade





    return
