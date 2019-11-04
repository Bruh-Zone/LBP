label SGFD2_CRS07A:
    window hide


    $ loadBG(0,"BG02N1")

    play bgm "BGM20"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("Y13")
    play voc "CRS07A_Y130000"
    $ current_voice = "voice/CRS07A_Y130000.ogg"
    "黒木" "「大小姐，耽误一下可以吗？」"
    $ stopvoc("FEI")
    play FEI "CRS07A_FEI0000"
    $ current_voice = "voice/CRS07A_FEI0000.ogg"
    "菲利斯" "「怎么，黑木你有什么好主意吗？」"
    "面对这突如其来荒诞无稽的情况，我们不知所措地发着愁。"
    "大概是对这样的我们不忍袖手旁观，管家──好像是叫黑木先生的人，开口了。"
    $ stopvoc("Y13")
    play voc "CRS07A_Y130001"
    $ current_voice = "voice/CRS07A_Y130001.ogg"
    "黒木" "「是的，虽说我对事态也没有完全掌握，但首先去找老爷商量一下如何？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS07A_FEI0001"
    $ current_voice = "voice/CRS07A_FEI0001.ogg"
    "菲利斯" "「跟爸爸商量？」"
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5 
    "菲利斯的……父亲。"
    "要说这种状况下能依靠的人，不应该是警察方面的人吗。"
    "不过冈部说了，就连警察也会被ＳＥＲＮ施加压力。"
    "那，到底该向谁求助……？"
    "不管怎样，要去依赖大人，我还是有些抵触的。"
    "因为至今为止的人生中，我无论什么事都是靠自己解决的。"
    "只是我发觉，从实际情况看来，我们已经束手无策了。"
    "即使我在美国的研究所已经作为一个社会人士工作了，我的年龄在日本都还算不上成年。"
    "再怎么挣扎都无法弥补社会经验不足的部分，我还没有学过该如何应对这种事态。"
    "——碰到这种情况的时候，向警察寻求帮助已是我的极限。"
    "说白了，连警察也无法依靠的时候的我就真的无可奈何了。"
    "冈部说他们的势力已经渗透到警察内部了，虽然有点怀疑，但他那拼命的样子实在让我不得不相信。"
    "更重要的是，如果那个导致公共交通系统瘫痪的恐怖袭击预告出自他们，现在连烦恼的时间都不剩了。"
    hide bg2 

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS07A_FEI0002"
    $ current_voice = "voice/CRS07A_FEI0002.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "菲利斯一瞬间露出了犹豫的表情，但下一个瞬间，她已经咬紧双唇一副下定了决心的神色。"
    $ stopvoc("FEI")
    play FEI "CRS07A_FEI0003"
    $ current_voice = "voice/CRS07A_FEI0003.ogg"
    "菲利斯" "「总之在这里也不是办法。到我家去吧。」"
    $ stopvoc("CRS")
    play CRS "CRS07A_CRS0000"
    $ current_voice = "voice/CRS07A_CRS0000.ogg"
    "红莉栖" "「到你家去吗？」"
    "我对她的话稍微有些疑问。"
    "时间跳跃机，已经确定了是只能在这个Ｌａｂ里运行的试作品。"
    "如果我们离开了Ｌａｂ，要保证时间跳跃机的安全就很困难了。"
    "如果冈部所说的都是实情，在这个时间点上时间跳跃机还没被抢走，本身就已经很不可思议了。"
    "然后，黑木替菲利斯回答了我的问题。"
    $ stopvoc("Y13")
    play voc "CRS07A_Y130002"
    $ current_voice = "voice/CRS07A_Y130002.ogg"
    "黒木" "「牧濑，正如大小姐所说，这里可能会被再次袭击。暂且还是离开比较明智。」"
    $ stopvoc("Y13")
    play voc "CRS07A_Y130003"
    $ current_voice = "voice/CRS07A_Y130003.ogg"
    "黒木" "「敬请放心。我们离开之后，会安排人员对这里进行监视。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA01"),"True","lh/FEI_BSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "对黑木的话，菲利斯回应以信任的眼神。"
    "看那信心满满的样子，似乎确实是可以依赖的人。"
    "这些人……到底是什么身份呢。"
    "感觉他们的背后似乎有着什么强大的组织。说是有点可疑也不为过……"
    "不过，于我而言也没有其他可以依靠的人了。"
    $ stopvoc("CRS")
    play CRS "CRS07A_CRS0001"
    $ current_voice = "voice/CRS07A_CRS0001.ogg"
    "红莉栖" "「明白了。」"
    "最重要的是，不能让这种状态的冈部滞留在危险的场所中。"
    "失去了意识的冈部依然一脸痛苦的表情，看着这样的他，我下定了决心。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我们马上开始转移。同时祈祷着不知身在何方的真由理和桥田能平安无事……"

    hide screen phoneSD1
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade





    return
