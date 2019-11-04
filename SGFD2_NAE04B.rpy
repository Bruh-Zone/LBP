label SGFD2_NAE04B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide



    $ loadBG(0,"BG73N")

    play bgm "FD2BGM09"

    $ date="7/9"
    $ day="SAT"
    show screen phonebtn
    show screen phoneSD1

    "从明天开始就是考试周了。"
    "不仅要把课上学过的知识都记到脑子里，还要好好地预习一下新知识，才能取得好成绩。"
    "吃了晚饭之后，将睡意一扫而尽，我学习了好几个小时。"
    "看了眼闹钟，发现已经过了午夜了。"
    "感觉不能很好地集中精神了。"
    "说不定会比春季的考试的分数还要低。"
    "桶子叔叔再晚一周来就好了。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0034"
    $ current_voice = "voice/NAE04A_NAE0034.ogg"
    "绹" "「啊唔……」"
    "憋住了一个哈欠。"
    "喝点热茶吧。"
    window hide


    $ loadBG(2,"BG26N")



    "来到了客厅，发现留未穗姐姐在那。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA03"),"True","lh/FEI_HSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0004"
    $ current_voice = "voice/NAE04A_FEI0004.ogg"
    "菲利斯" "「喵？　绹，怎么还醒着？　明天是星期一，你知道的吧喵？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0035"
    $ current_voice = "voice/NAE04A_NAE0035.ogg"
    "绹" "「恩，明天开始是考试周」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0005"
    $ current_voice = "voice/NAE04A_FEI0005.ogg"
    "菲利斯" "「在学习吗？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0036"
    $ current_voice = "voice/NAE04A_NAE0036.ogg"
    "绹" "「没法好好集中了」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0006"
    $ current_voice = "voice/NAE04A_FEI0006.ogg"
    "菲利斯" "「那就来试试我的印度阿萨姆红茶吧喵。放了很多牛奶喵」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0037"
    $ current_voice = "voice/NAE04A_NAE0037.ogg"
    "绹" "「哇，好像很不错的样子♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA01"),"True","lh/FEI_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0007"
    $ current_voice = "voice/NAE04A_FEI0007.ogg"
    "菲利斯" "「喵哈♪　坐着等一下喵」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "留未穗姐姐高兴地走进了厨房。"
    "不一会儿，就端来了一杯温暖的奶茶。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSB01"),"True","lh/FEI_HSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0008"
    $ current_voice = "voice/NAE04A_FEI0008.ogg"
    "菲利斯" "「请用吧，大小姐♪」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0038"
    $ current_voice = "voice/NAE04A_NAE0038.ogg"
    "绹" "「我不客气了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA02"),"True","lh/FEI_HSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "从茶杯中传来美妙的香味。"
    "虽然不是很懂红茶，但是姐姐泡的茶真的超级好喝。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0039"
    $ current_voice = "voice/NAE04A_NAE0039.ogg"
    "绹" "「呐，姐姐」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0009"
    $ current_voice = "voice/NAE04A_FEI0009.ogg"
    "菲利斯" "「恩？　怎么了吗？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0040"
    $ current_voice = "voice/NAE04A_NAE0040.ogg"
    "绹" "「……有叫桶子叔叔这么一个人吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSB01"),"True","lh/FEI_HSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0010"
    $ current_voice = "voice/NAE04A_FEI0010.ogg"
    "菲利斯" "「哇，你说桶喵啊」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0011"
    $ current_voice = "voice/NAE04A_FEI0011.ogg"
    "菲利斯" "「好怀念的名字喵。我还叫做菲利斯玩雷Ｎｅｔ的时候，他可是我的头号粉丝呢」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0012"
    $ current_voice = "voice/NAE04A_FEI0012.ogg"
    "菲利斯" "「还有……」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0041"
    $ current_voice = "voice/NAE04A_NAE0041.ogg"
    "绹" "「“Ｌａｂｍｅｍ”」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA03"),"True","lh/FEI_HSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0013"
    $ current_voice = "voice/NAE04A_FEI0013.ogg"
    "菲利斯" "「…………」"
    "我说出这个词的时候，留未穗姐姐露出了少许寂寞的表情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0014"
    $ current_voice = "voice/NAE04A_FEI0014.ogg"
    "菲利斯" "「是的，Ｌａｂｍｅｍ喵」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0015"
    $ current_voice = "voice/NAE04A_FEI0015.ogg"
    "菲利斯" "「难道说绹你在哪里遇到了桶喵吗喵？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0042"
    $ current_voice = "voice/NAE04A_NAE0042.ogg"
    "绹" "「啊，那个……并不是这样」"
    "眼睛……没被看到吧。"
    "又撒谎了。"
    "明明没有必要隐瞒的。"
    "我，难道说不信任留未穗姐姐？"
    "并不是那样。"
    "在这２年间，我和留未穗姐姐谈过很多事。"
    "如果没有留未穗姐姐的话，我会在这个家里更加地关闭心扉，生活下去吧。"
    "但是，为什么现在就不小心撒了个谎呢。"
    "是想独占发送Ｄｍａｉｌ的好处？"
    "还是说，是在害怕如果在这里告诉了谁的话，我就无法成为当事者了这一点？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA02"),"True","lh/FEI_HSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0016"
    $ current_voice = "voice/NAE04A_FEI0016.ogg"
    "菲利斯" "「桶喵，好想念他啊。现在在哪里做着什么呢喵。还想和他对战呢喵」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0043"
    $ current_voice = "voice/NAE04A_NAE0043.ogg"
    "绹" "「那个……留未穗姐姐和桶子叔叔是恋人吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0017"
    $ current_voice = "voice/NAE04A_FEI0017.ogg"
    "菲利斯" "「喵？　恋人……并不是哦」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0044"
    $ current_voice = "voice/NAE04A_NAE0044.ogg"
    "绹" "「不是吗？」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0018"
    $ current_voice = "voice/NAE04A_FEI0018.ogg"
    "菲利斯" "「关系很好喵。曾经是非常好的朋友喵。」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0045"
    $ current_voice = "voice/NAE04A_NAE0045.ogg"
    "绹" "「…………」"
    "桶子叔叔对我说谎了。"
    "为什么，要说那样的谎呢。"
    "深受打击。"
    "于是……我明白了别人对你撒谎时的感受。"
    "不好意思了，留未穗姐姐。"
    "我并没有责备桶子叔叔的资格。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "心情有些失落，我喝完了奶茶，回去继续学习。"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
