label SGFD2_DAR10A:
    window hide


    $ loadBG(0,"IBG044B")
    play se "SGSE200L" loop


    $ date="8/17"
    hide screen phonebtn
    hide screen phoneSD1
    $ bad_denpa = False

    "东方既白。"
    "竟然，还能再次看到太阳，我想都没想过。"
    "那次爆炸后。"
    "赶到的警察和消防人员把我们救了出来。"
    "秋叶原因为大型爆炸事故引起了大骚乱。新闻电视台在大晚上一直在做报道。"
    "顺带一提桐生氏一直联系不到。"
    "肯定已经不会再回到秋叶原了吧。"
    "我和由季碳被送到了医院接受治疗。"
    "幸运的是我仅仅是擦伤并没有什么大碍。"
    "由季碳呢，被困了一整天，非常的衰弱，好像已经住院了。"
    "最后应该还是平安无事地出院吧。"
    window hide


    $ loadBG(0,"BG39N2")

    show screen phonebtn
    show screen phoneSD1
    "花了相当长的时间才到了Ｌａｂ。"
    "虽然中央大道还是很繁忙，但是因为情况尚未清楚所以这边还是完全没有人走动的状态。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0000"
    $ current_voice = "voice/DAR10A_OKA0000.ogg"
    "伦太郎" "「没事吧」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0000"
    $ current_voice = "voice/DAR10A_DAR0000.ogg"
    "至" "「没事没事」"
    "其实稍微有点事，因为脚上的痛还没有退去。"
    "而且眼镜的碎片也有些嵌在了皮肤里。"
    "虽然我因为要检查身体不得不住院观察，但是也没能接触到她。"
    "所以说要让冈伦帮我从医院里出去。"
    "虽然叫了的士但是我和冈伦都没有带钱，只能郁闷地从医院走到这来。"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0001"
    $ current_voice = "voice/DAR10A_DAR0001.ogg"
    "至" "「那个……冈伦」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0001"
    $ current_voice = "voice/DAR10A_OKA0001.ogg"
    "伦太郎" "「嗯？ 咋了？」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0002"
    $ current_voice = "voice/DAR10A_DAR0002.ogg"
    "至" "「铃羽氏，新闻里面提到了吗？」"
    "终于鼓起勇气，问了从医院出来开始想问但没能问出来的问题。"
    "我把铃羽的真实身份，以及为了救我和由季碳而带走了炸弹的事情告诉了冈伦。"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0002"
    $ current_voice = "voice/DAR10A_OKA0002.ogg"
    "伦太郎" "「不知道」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0003"
    $ current_voice = "voice/DAR10A_DAR0003.ogg"
    "至" "「不是说看了新闻吗，难道没有提到吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0003"
    $ current_voice = "voice/DAR10A_OKA0003.ogg"
    "伦太郎" "「啊啊，是看了！但是，关于铃羽一字未提啊！」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0004"
    $ current_voice = "voice/DAR10A_OKA0004.ogg"
    "伦太郎" "「到现在为止，暂时没有那场爆炸的牺牲者。一个人都没有」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0005"
    $ current_voice = "voice/DAR10A_OKA0005.ogg"
    "伦太郎" "「也就是说，铃羽没死。是不是啊？」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0004"
    $ current_voice = "voice/DAR10A_DAR0004.ogg"
    "至" "「……是这样的啊」"
    "在那个情况下，也不是没有想过铃羽抱着炸弹离开然后被炸死。但是如果冈伦说的话是真的话，也就是说没有发现遗体咯。"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0006"
    $ current_voice = "voice/DAR10A_OKA0006.ogg"
    "伦太郎" "「能够证明铃羽还活着的证据，已经只有一个了」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0005"
    $ current_voice = "voice/DAR10A_DAR0005.ogg"
    "至" "「什么？」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0007"
    $ current_voice = "voice/DAR10A_OKA0007.ogg"
    "伦太郎" "「你不是说建筑物上面有时间机器吗？」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0008"
    $ current_voice = "voice/DAR10A_OKA0008.ogg"
    "伦太郎" "「你住进医院的时候，我和助手就去那里看了──」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0009"
    $ current_voice = "voice/DAR10A_OKA0009.ogg"
    "伦太郎" "「并没有看见」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0006"
    $ current_voice = "voice/DAR10A_DAR0006.ogg"
    "至" "「什……什么？」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0007"
    $ current_voice = "voice/DAR10A_DAR0007.ogg"
    "至" "「但是，确实有个像人造卫星的东西，咚的一声……」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0010"
    $ current_voice = "voice/DAR10A_OKA0010.ogg"
    "伦太郎" "「然而并没有」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0008"
    $ current_voice = "voice/DAR10A_DAR0008.ogg"
    "至" "「也就是说，这都是我的妄想咯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0011"
    $ current_voice = "voice/DAR10A_OKA0011.ogg"
    "伦太郎" "「亦或是，救了你之后，铃羽乘坐时间机器到了别的时间」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0009"
    $ current_voice = "voice/DAR10A_DAR0009.ogg"
    "至" "「噢……」"
    "也有这种可能。"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0012"
    $ current_voice = "voice/DAR10A_OKA0012.ogg"
    "伦太郎" "「所以说，就相信我吧」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0010"
    $ current_voice = "voice/DAR10A_DAR0010.ogg"
    "至" "「……嗯」"
    window hide

    stop se



    $ loadBG(0,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play se "SGSE024"


    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0000"
    $ current_voice = "voice/DAR10A_CRS0000.ogg"
    "红莉栖" "「欢迎回来」"
    "在这个点，牧濑氏已经在Ｌａｂ了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0013"
    $ current_voice = "voice/DAR10A_OKA0013.ogg"
    "伦太郎" "「助手，你没回酒店吗？」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0001"
    $ current_voice = "voice/DAR10A_CRS0001.ogg"
    "红莉栖" "「在这里想会儿事」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0011"
    $ current_voice = "voice/DAR10A_DAR0011.ogg"
    "至" "「牧瀬氏牧瀬氏，这里不是这样说的」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0012"
    $ current_voice = "voice/DAR10A_DAR0012.ogg"
    "至" "「“也，也不是特意为了桥田所以才等到现在的”应该这样说。说起来拜托了求你这样说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0002"
    $ current_voice = "voice/DAR10A_CRS0002.ogg"
    "红莉栖" "「你啊……」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0003"
    $ current_voice = "voice/DAR10A_CRS0003.ogg"
    "红莉栖" "「说起来，不住院真的好吗？　为什么要在这种时候特意跑出来？」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0014"
    $ current_voice = "voice/DAR10A_OKA0014.ogg"
    "伦太郎" "「我也想知道啊。桶子，为什么这样着急？」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0013"
    $ current_voice = "voice/DAR10A_DAR0013.ogg"
    "至" "「按常理来说只有一个理由咯」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0004"
    $ current_voice = "voice/DAR10A_CRS0004.ogg"
    "红莉栖" "「什么呀？」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0014"
    $ current_voice = "voice/DAR10A_DAR0014.ogg"
    "至" "「为了夏Ｃｏｍｉ的第三天！　起立！！"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC06"),"True","lh/CRS_BSC06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM10"

    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0005"
    $ current_voice = "voice/DAR10A_CRS0005.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0015"
    $ current_voice = "voice/DAR10A_OKA0015.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0015"
    $ current_voice = "voice/DAR10A_DAR0015.ogg"
    "至" "「因为如果不把『忽滑谷冰果子太喜欢寄生虫以至于不知为何就住到我的内脏里了』简称『寄生住内』搞到手，我真是太失职了！」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0016"
    $ current_voice = "voice/DAR10A_DAR0016.ogg"
    "至" "「啊啊，好想早点见到冰果子碳啊！」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0017"
    $ current_voice = "voice/DAR10A_DAR0017.ogg"
    "至" "「我想之前也说过，我打算攻略的第１０００个妹子，就决定是她了！」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0018"
    $ current_voice = "voice/DAR10A_DAR0018.ogg"
    "至" "「『寄生住内』的争夺战可是非常残酷的。即使是坐第一班电车去排队也不能保证一定入手的程度，就算是这样──」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0019"
    $ current_voice = "voice/DAR10A_DAR0019.ogg"
    "至" "「这是一场绝对不能输的战斗，目标就在前方！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0016"
    $ current_voice = "voice/DAR10A_OKA0016.ogg"
    "伦太郎" "「桶子，你……别闹了」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0020"
    $ current_voice = "voice/DAR10A_DAR0020.ogg"
    "至" "「切……说起来，我从现在就开始等着天亮了」"
    "用昨天的时间准备好的背包。"
    "那个包里面，放着今天作战所需要的所有物资。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB06"),"True","lh/CRS_BSB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0006"
    $ current_voice = "voice/DAR10A_CRS0006.ogg"
    "红莉栖" "「等一下，桥田。我，我一直在想」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0007"
    $ current_voice = "voice/DAR10A_CRS0007.ogg"
    "红莉栖" "「阿万音小姐的事情我从冈部那里听说了」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0008"
    $ current_voice = "voice/DAR10A_CRS0008.ogg"
    "红莉栖" "「根据昨天的事情，在想到发生在你身上的事情的时候，发现了矛盾。可以说是时间悖论」"
    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0017"
    $ current_voice = "voice/DAR10A_OKA0017.ogg"
    "伦太郎" "「到底是怎么一回事？」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0009"
    $ current_voice = "voice/DAR10A_CRS0009.ogg"
    "红莉栖" "「就像是先有鸡还是先有蛋一样」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0010"
    $ current_voice = "voice/DAR10A_CRS0010.ogg"
    "红莉栖" "「帮助桥田和由季的人是，阿万音铃羽」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0011"
    $ current_voice = "voice/DAR10A_CRS0011.ogg"
    "红莉栖" "「也就是说，桥田和由季在２０１０年８月１６日之后还活着的这个结果，是因为铃羽去救了他们」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0012"
    $ current_voice = "voice/DAR10A_CRS0012.ogg"
    "红莉栖" "「但是，铃羽是时间旅行者。是从２０３６年过来的桥田和由季所生的女儿。但是如果两人无法活过２０１０年８月１６日的话，铃羽是无法存在的」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0013"
    $ current_voice = "voice/DAR10A_CRS0013.ogg"
    "红莉栖" "「这两件事互为因果，于是产生了悖论」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0014"
    $ current_voice = "voice/DAR10A_CRS0014.ogg"
    "红莉栖" "「如果是这样的话，桥田，你也有可能不是铃羽的父亲──」"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0021"
    $ current_voice = "voice/DAR10A_DAR0021.ogg"
    "至" "「不用在意这些细节了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC04"),"True","lh/CRS_BSC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0015"
    $ current_voice = "voice/DAR10A_CRS0015.ogg"
    "红莉栖" "「唔！？」"
    "我将更换的衣物，矿泉水和掌机塞进背包，然后轻快地站了起来。"
    $ stopvoc("DAR")
    play DAR "DAR10A_DAR0022"
    $ current_voice = "voice/DAR10A_DAR0022.ogg"
    "至" "「那么，现在就出发去将我的第１０００个攻略对象娶回家吧」"
    $ stopvoc("CRS")
    play CRS "DAR10A_CRS0016"
    $ current_voice = "voice/DAR10A_CRS0016.ogg"
    "红莉栖" "「呀，稍微，等……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB02"),"True","lh/OKA_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "DAR10A_OKA0018"
    $ current_voice = "voice/DAR10A_OKA0018.ogg"
    "伦太郎" "「桶子，祝你武运昌盛」"
    "在混乱的牧濑氏和笑着摆出敬礼的Ｐｏｓｓ的冈伦的目送下，我走出了Ｌａｂ。"
    window hide


    $ loadBG(0,"BG39N2",trans=fade)

    "微微看了下被贴在手指上的创可贴。"
    "在虽有少许灯光，但是尚未醒来的街道上，朝着车站走去。"
    "我到底是不是铃羽的父亲这件事，再过１０年就知道了。"
    "因为和由季碳也没有做过什么特殊的约定，最后连个自我介绍都没做。"
    "如果有缘的话肯定还会再见面的。"
    "所以现在。"
    "我就和往常一样。"
    "不去改变。"
    "只向着二次元的新娘前进了就行了！"
    "等着吧，冰果子碳～♪"

    hide screen phoneSD1
    hide screen phonebtn
    window hide

    stop bgm
    $ loadBG(0,"BG_BLACK")
    show screen invisible
    $ renpy.movie_cutscene("video/imv08.avi")
    hide screen invisible
    "「绚烂假想的蛇蝎美人·完成」"







    return
