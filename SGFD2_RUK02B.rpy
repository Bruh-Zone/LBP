label SGFD2_RUK02B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG36N")








    $ date="8/16"
    $ day="MON"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0000"
    $ current_voice = "voice/RUK02B_RUK0000.ogg"
    "琉华" "「咕……啊啊啊啊啊啊！！」"
    "又是这种似乎把利刃刺入大脑的痛苦。"
    "但是，最终这种感觉开始退去。"
    window hide











    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0001"
    $ current_voice = "voice/RUK02B_RUK0001.ogg"
    "琉华" "「哈……哈，哈……」"
    "是因为已经经历过一次了吗，和刚才相比感觉痛苦少了一些。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0002"
    $ current_voice = "voice/RUK02B_RUK0002.ogg"
    "琉华" "「这里是……」"
    play bgm "FD2BGM08"
    "我身处秋叶原的电器街的内侧。"
    "想了想为什么自己会在这里，于是就想起了我在那一天的晚上曾经去过未来道具研究所。"

    "如果我不变回男生的话，真由理酱就会死去。"
    "虽然听到冈部师傅这么说，但是完全不相信会发生。"
    "所以感觉自己如果去了研究所的话，就会在那里遇到真由理——"
    "虽然到了那里发现并没有灯光，所以感觉没人在里面，就回去了。"
    "其实那个时候冈部师傅在里面，我却完全没有注意到……"
    "后来，果然还是想和谁说说话，于是造访了菲利斯的店。"
    "但是菲利斯也不在。"
    "最后谁也没能遇到。"
    "结果，只能回家一个人抱着膝盖无聊地蹲墙角……"

    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0003"
    $ current_voice = "voice/RUK02B_RUK0003.ogg"
    "琉华" "「…………」"
    "虽然对于那时候的自己的行动感到十分厌恶，但是，多亏了那时的想法，现在我才能得以尽早赶往研究所。"
    "我对于自己在那一天的行动表示感谢。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0004"
    $ current_voice = "voice/RUK02B_RUK0004.ogg"
    "琉华" "「对了……！」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我用我还握着的手机给刚刚打过电话的牧濑打了个电话。"



    "一次，两次……"
    "怀着祈祷般的心情等待着她的接听。"
    "然而。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0005"
    $ current_voice = "voice/RUK02B_RUK0005.ogg"
    "琉华" "「…………」"
    "不管打几次，只能听到机械的电子音，牧濑并没有接。"
    "是因为不知道的号码打来的电话吧？"
    "至少如果能切换到语音信箱的话，我还能把要说的话留个言，但结果那也没做成。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0006"
    $ current_voice = "voice/RUK02B_RUK0006.ogg"
    "琉华" "「该怎么办呢……」"
    "明明能够依赖的只有牧濑啊……"
    "到晚上８点只有１５分钟不到了。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0007"
    $ current_voice = "voice/RUK02B_RUK0007.ogg"
    "琉华" "「…………！」"
    window hide


    call hide_phone


    "总而言之在这里发呆也无济于事。"
    "我朝着研究所前进了。"
    window hide

    stop bgm 



    $ loadBG(0,"BG02N5")
    play se "SGSE024"


    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0008"
    $ current_voice = "voice/RUK02B_RUK0008.ogg"
    "琉华" "「冈部师傅！！」"
    "我打开门，呼唤起了冈部师傅。"
    "说不定，冈部师傅会听我说话！"
    "怀着这样的希望。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0009"
    $ current_voice = "voice/RUK02B_RUK0009.ogg"
    "琉华" "「冈部……师傅……」"
    "然而，现实是残酷的。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK003C"]]["Check"]=True


    $ loadBG(2,"EV_RUK003C")



    hide screen phonebtn
    play bgm "FD2BGM05"

    $ stopvoc("OKA")
    play OKA "RUK02B_OKA0000"
    $ current_voice = "voice/RUK02B_OKA0000.ogg"
    "伦太郎" "「…………」"
    "冈部师傅和我刚才看到的一样，失神地注视着前方。"
    "稍微有些不同的是，还没有刚才看到的那么憔悴。"
    "就算如此，我也不能这么旁观下去。"
    "我来到冈部师傅边上倾诉道。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0010"
    $ current_voice = "voice/RUK02B_RUK0010.ogg"
    "琉华" "「冈部师傅。拜托了，请听我说。在下，想回到过去！」"
    $ stopvoc("OKA")
    play OKA "RUK02B_OKA0001"
    $ current_voice = "voice/RUK02B_OKA0001.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0011"
    $ current_voice = "voice/RUK02B_RUK0011.ogg"
    "琉华" "「回到过去以后，我想和真由理酱见面！所以──」"
    $ stopvoc("OKA")
    play OKA "RUK02B_OKA0002"
    $ current_voice = "voice/RUK02B_OKA0002.ogg"
    "伦太郎" "「真由……理……」"
    "有反应了！"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0012"
    $ current_voice = "voice/RUK02B_RUK0012.ogg"
    "琉华" "「是这样的！在下，是为了实现真由理酱的愿望才想要回到过去的！」"
    $ stopvoc("OKA")
    play OKA "RUK02B_OKA0003"
    $ current_voice = "voice/RUK02B_OKA0003.ogg"
    "伦太郎" "「真由理……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0013"
    $ current_voice = "voice/RUK02B_RUK0013.ogg"
    "琉华" "「所以，冈部师傅的帮助是必要的！」"
    $ stopvoc("OKA")
    play OKA "RUK02B_OKA0004"
    $ current_voice = "voice/RUK02B_OKA0004.ogg"
    "伦太郎" "「……真由理……、对不起……真由理……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0014"
    $ current_voice = "voice/RUK02B_RUK0014.ogg"
    "琉华" "「冈部师傅……」"
    "在那之后，虽然不知道叫了几次师傅的名字，但冈部师傅依然是一副恍惚的样子。"
    window hide


    $ loadBG(2,"BG02N5")





    "马上就要到晚上８点了。"
    "如果那样的话，今天就没法回到过去了。"
    "如果今天不能回去的话，要等到明天白天才可以。"
    "如果是那时候的两天的话，也就是１５日的白天。"
    "真由理——还活着的时候。"
    "就算回到那个时候，大家都去了夏Ｃｏｍｉ了，也就没法使用机器了。"
    window hide


    $ loadBG(0,"BG_BLACK")


    "如果到了晚上的话——"
    "估计又赶不上这边。"
    "这样的话也就会变成又要等到１６日的白天了么……"
    "那个时候冈部师傅肯定还是会保持这个状态。"
    "如果那时候还是联系不到牧濑的话，我就会这么连真由理的心愿都无法实现，只是在浪费时间而已。"
    "只是那样循环往复而已。"
    "冈部师傅也说过。"
    "如果回到过去就能重新来过，虽然这么认为着，但是现实确实残酷的。"
    "无法改写已经决定了的命运。"
    "那就是说，我连真由理的小小心愿都无法实现的意思吗。"
    "那样的事。"
    "那种事情……"

    stop bgm 


    $ loadBG(0,"BG01N5")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0015"
    $ current_voice = "voice/RUK02B_RUK0015.ogg"
    "琉华" "「……？」"
    play bgm "BGM25"
    "这个时候，我感到房间外好像有什么动静。"
    "是人的……感觉。"
    "谁？"
    "这么说起来……"
    "一下子想起来了。"
    "已经不知道救过真由理酱几次的冈部师傅说的话。"
    "最初开始的时候，确实是有过几个拿着手枪袭击这个房间的人什么的——冈部师傅确实那么说过。"
    "难道说，在外面的是……"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0016"
    $ current_voice = "voice/RUK02B_RUK0016.ogg"
    "琉华" "「！……」"
    "怎么办啊。"
    "如果是那样的话……"
    "冈部师傅现在这样的话，一定是无法抵抗袭击过来的人的吧。"
    "而且我也想不到我能做点什么。"
    "在这么想着的时候，外面的人说不定就破门而入了呢。"
    "但是……"
    "如果那样就能让我们的罪恶消失的话，那也……"
    "诶……？"
    "刚才，虽然很轻，但我好像听到了下楼的脚步声……"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0017"
    $ current_voice = "voice/RUK02B_RUK0017.ogg"
    "琉华" "「──！」"
    "在外面的人不是我想象中的那些人，而是——"
    window hide
    play se "SGSE024"

    stop bgm 


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn

    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0018"
    $ current_voice = "voice/RUK02B_RUK0018.ogg"
    "琉华" "「牧，牧濑──！」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0000"
    $ current_voice = "voice/RUK02B_CRS0000.ogg"
    "红莉栖" "「……诶！？」"
    window hide


    $ loadBG(0,"BG01N5")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC04"),"True","lh/CRS_HSC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM08"

    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0019"
    $ current_voice = "voice/RUK02B_RUK0019.ogg"
    "琉华" "「不，不好意思，吓到你了……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0001"
    $ current_voice = "voice/RUK02B_CRS0001.ogg"
    "红莉栖" "「还，还好。嘛确实把我吓到了，但并不是很在意，所以不用那么自责」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0020"
    $ current_voice = "voice/RUK02B_RUK0020.ogg"
    "琉华" "「十分抱歉……」"
    "和我想的一样，在房间外面的不是恐怖的那群人，而是牧濑。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0002"
    $ current_voice = "voice/RUK02B_CRS0002.ogg"
    "红莉栖" "「但是，为什么会知道是我？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0021"
    $ current_voice = "voice/RUK02B_RUK0021.ogg"
    "琉华" "「那是因为……觉得刚才牧濑就好像很担心冈部师傅的样子，所以才会那么想」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA04"),"True","lh/CRS_HSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0003"
    $ current_voice = "voice/RUK02B_CRS0003.ogg"
    "红莉栖" "「是吗……」"
    "牧濑露出悲伤的表情小小地说了一句。"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0004"
    $ current_voice = "voice/RUK02B_CRS0004.ogg"
    "红莉栖" "「……恩，是啊。我担心着他呢，冈部……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0005"
    $ current_voice = "voice/RUK02B_CRS0005.ogg"
    "红莉栖" "「因为，发生了这种事……那家伙不可能受得了吧……」"
    "看着就这么听着我们说话也无动于衷的冈部师傅，牧濑脸上露出了悲伤的神色。"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0006"
    $ current_voice = "voice/RUK02B_CRS0006.ogg"
    "红莉栖" "「而且，我的话……一个人，也很难受啊……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0022"
    $ current_voice = "voice/RUK02B_RUK0022.ogg"
    "琉华" "「牧濑……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0007"
    $ current_voice = "voice/RUK02B_CRS0007.ogg"
    "红莉栖" "「但是，很意外呢……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0023"
    $ current_voice = "voice/RUK02B_RUK0023.ogg"
    "琉华" "「……？」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0008"
    $ current_voice = "voice/RUK02B_CRS0008.ogg"
    "红莉栖" "「啊，不好意思。漆原和真由理……关系很好吧？」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0009"
    $ current_voice = "voice/RUK02B_CRS0009.ogg"
    "红莉栖" "「因为她发生了这种事，我还以为你一直在哭着呢……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0024"
    $ current_voice = "voice/RUK02B_RUK0024.ogg"
    "琉华" "「啊，我的话，那个……当然也很难过，但是可以说是比大家经历过更多的时间吧……」"
    "墙上的时钟进入了我的眼帘。"
    "时间是——８点过５分了！"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB07"),"True","lh/CRS_HSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0010"
    $ current_voice = "voice/RUK02B_CRS0010.ogg"
    "红莉栖" "「时间？等等，说起来刚才你也说过一些奇怪的话呢」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0011"
    $ current_voice = "voice/RUK02B_CRS0011.ogg"
    "红莉栖" "「“刚才也”什么的……就好像刚刚还和我见过一样……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0025"
    $ current_voice = "voice/RUK02B_RUK0025.ogg"
    "琉华" "「牧，牧濑！希望你能帮帮我！我想要！我想要回到过去！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC04"),"True","lh/CRS_HSC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0012"
    $ current_voice = "voice/RUK02B_CRS0012.ogg"
    "红莉栖" "「……！」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0013"
    $ current_voice = "voice/RUK02B_CRS0013.ogg"
    "红莉栖" "「过去……难道说，是在说时间跳跃机器？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0026"
    $ current_voice = "voice/RUK02B_RUK0026.ogg"
    "琉华" "「是的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA03"),"True","lh/CRS_HSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0014"
    $ current_voice = "voice/RUK02B_CRS0014.ogg"
    "红莉栖" "「不行哦，那个还……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0027"
    $ current_voice = "voice/RUK02B_RUK0027.ogg"
    "琉华" "「我没关系的！刚才已经成功了！」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0015"
    $ current_voice = "voice/RUK02B_CRS0015.ogg"
    "红莉栖" "「刚才什么的……那也就是说，你果然……」"

    "好怀念的感觉。"
    "我和刚才的牧濑氏也说过一样的事。"
    "但是，现在牧濑却不知道那些。"
    "我们应该共有的时间只存在我的大脑里，却不存在于这个时间里。"
    "这么想着，我突然有了来到一个陌生世界的感觉。"
    "那是孤独。"
    "难以言喻的孤独。"
    "就好像，这世界只剩下我一个人一样。"
    "原来与他人不共享相同的时间，原来是这么孤单的事情"
    "冈部师傅就这么一个人不停地重复这这样的时间。"
    "为了救真由理酱。"
    "就那么在一个人的世界里。"
    "只有一个人的孤独的战斗，一次又一次……"


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0016"
    $ current_voice = "voice/RUK02B_CRS0016.ogg"
    "红莉栖" "「漆原」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0028"
    $ current_voice = "voice/RUK02B_RUK0028.ogg"
    "琉华" "「诶？」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0017"
    $ current_voice = "voice/RUK02B_CRS0017.ogg"
    "红莉栖" "「慌张先放一下，现在先冷静下来把事情详细地和我说一下可以吗？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0029"
    $ current_voice = "voice/RUK02B_RUK0029.ogg"
    "琉华" "「啊……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0018"
    $ current_voice = "voice/RUK02B_CRS0018.ogg"
    "红莉栖" "「是很重要的事情吧？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0030"
    $ current_voice = "voice/RUK02B_RUK0030.ogg"
    "琉华" "「是，是的，其实呢……」"

    "我利索地点了点头，又把事情和牧濑说了一遍。"
    "是因为刚才刚说过一遍吗，现在说起来感觉井井有条。"
    "牧濑在我说的时候不时提一些问题，很快就掌握了情况。"

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0019"
    $ current_voice = "voice/RUK02B_CRS0019.ogg"
    "红莉栖" "「这样啊……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0031"
    $ current_voice = "voice/RUK02B_RUK0031.ogg"
    "琉华" "「…………」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0020"
    $ current_voice = "voice/RUK02B_CRS0020.ogg"
    "红莉栖" "「虽然想关于冈部的做法和你的想法说很多，但是很遗憾现在好像没有那么做的时间了」"
    "看了一下墙上的时钟，已经８点过１０分了。"
    "是因为我太啰嗦了么……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB01"),"True","lh/CRS_HSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0021"
    $ current_voice = "voice/RUK02B_CRS0021.ogg"
    "红莉栖" "「好啦，失落什么的也等会再说。要去实现真由理的愿望吧。那样的话，现在要做的事只有一件。对吧？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0032"
    $ current_voice = "voice/RUK02B_RUK0032.ogg"
    "琉华" "「是的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB07"),"True","lh/CRS_HSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0022"
    $ current_voice = "voice/RUK02B_CRS0022.ogg"
    "红莉栖" "「但是……糟糕了呢。时间上来说各种……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0033"
    $ current_voice = "voice/RUK02B_RUK0033.ogg"
    "琉华" "「──！」"

    stop bgm 
    $ stopvoc("NAE")
    play NAE "RUK02B_NAE0000"
    $ current_voice = "voice/RUK02B_NAE0000.ogg"
    "綯" "「爸爸！」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0000"
    $ current_voice = "voice/RUK02B_TEN0000.ogg"
    "天王寺" "「哦，绹，是特意来迎接我的吗？」"
    $ stopvoc("NAE")
    play NAE "RUK02B_NAE0001"
    $ current_voice = "voice/RUK02B_NAE0001.ogg"
    "綯" "「恩」"
    "楼下的店长和他的女儿的声音从窗户外传来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB03"),"True","lh/CRS_HSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM07"

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0023"
    $ current_voice = "voice/RUK02B_CRS0023.ogg"
    "红莉栖" "「果然……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0024"
    $ current_voice = "voice/RUK02B_CRS0024.ogg"
    "红莉栖" "「漆原！　你已经用过两次时间机器了吧？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0034"
    $ current_voice = "voice/RUK02B_RUK0034.ogg"
    "琉华" "「是，是的。但是，虽说使用过，我只是把头盔那样的东西放在头上而已……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0025"
    $ current_voice = "voice/RUK02B_CRS0025.ogg"
    "红莉栖" "「是的。在那之后只要输入数字后按下回车就好。设置我来做，在那之前你先想办法拖住显像管店长关门！」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0035"
    $ current_voice = "voice/RUK02B_RUK0035.ogg"
    "琉华" "「诶诶！？　我来做吗！？」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0026"
    $ current_voice = "voice/RUK02B_CRS0026.ogg"
    "红莉栖" "「除你之外还有谁吗？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0036"
    $ current_voice = "voice/RUK02B_RUK0036.ogg"
    "琉华" "「但是……」"
    "看着店长那样雄伟的身材，只是看着就觉得双腿打颤……"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0027"
    $ current_voice = "voice/RUK02B_CRS0027.ogg"
    "红莉栖" "「设定完成后就交给我来拖住他。那样的话，你应该就能从这里跳到昨天的早上！可以的哦！？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0037"
    $ current_voice = "voice/RUK02B_RUK0037.ogg"
    "琉华" "「恩……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0028"
    $ current_voice = "voice/RUK02B_CRS0028.ogg"
    "红莉栖" "「没关系，只要按一下键盘就行了」"
    "我……一个人……"
    "但是……"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0029"
    $ current_voice = "voice/RUK02B_CRS0029.ogg"
    "红莉栖" "「想实现真由理的愿望吧！？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0038"
    $ current_voice = "voice/RUK02B_RUK0038.ogg"
    "琉华" "「……明白了。我，现在就去！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC03"),"True","lh/CRS_HSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0030"
    $ current_voice = "voice/RUK02B_CRS0030.ogg"
    "红莉栖" "「……恩！　那么，就拜托了哦！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "牧濑重重地说道，然后就走向了房间内侧的电脑。"
    "我感受着她的强有力的背影，赶紧跑出了房间。"
    window hide



    $ loadBG(0,"BG05N1")

    "下了楼梯来到大楼前面的时候，店长刚好要为了关闭店门而走到了外面。"
    "千钧一发。"
    "但是，还不能放心。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0039"
    $ current_voice = "voice/RUK02B_RUK0039.ogg"
    "琉华" "「那，那个！！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0001"
    $ current_voice = "voice/RUK02B_TEN0001.ogg"
    "天王寺" "「恩？」"
    "听到了我的声音，已经把手放在了卷闸门上的店长回过头来。"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0002"
    $ current_voice = "voice/RUK02B_TEN0002.ogg"
    "天王寺" "「小姑娘你是……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0040"
    $ current_voice = "voice/RUK02B_RUK0040.ogg"
    "琉华" "「呜……」"
    "在眼前的是放在硕大胸板前的粗腕。"
    "仅仅那样我就感觉脚在发抖了。"
    "而且，这么叫住他了以后，我却不知道该说些什么。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0041"
    $ current_voice = "voice/RUK02B_RUK0041.ogg"
    "琉华" "「那，那个，这个……」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0003"
    $ current_voice = "voice/RUK02B_TEN0003.ogg"
    "天王寺" "「确实，是冈部那家伙的……有什么事吗？」"
    "……咦？"
    "向我投来的声音，却比想象中的要温柔。"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0004"
    $ current_voice = "voice/RUK02B_TEN0004.ogg"
    "天王寺" "「怎么了？难道不是有什么事才朝我搭话的吗？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0042"
    $ current_voice = "voice/RUK02B_RUK0042.ogg"
    "琉华" "「啊，是的……」"
    "然后……"
    "通透的双目。"
    "不仅没有凶狠狠地瞪着我，反而是意想不到的温柔视线。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0005"
    $ current_voice = "voice/RUK02B_TEN0005.ogg"
    "天王寺" "「难道说，是在说那位小姑娘的事？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0043"
    $ current_voice = "voice/RUK02B_RUK0043.ogg"
    "琉华" "「啊……」"
    play bgm "FD2BGM05"
    "店长在说谁的事，我马上就知道了。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0044"
    $ current_voice = "voice/RUK02B_RUK0044.ogg"
    "琉华" "「是说真由理酱……吧？」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0006"
    $ current_voice = "voice/RUK02B_TEN0006.ogg"
    "天王寺" "「啊啊。确实是叫那个名字呢。那个姑娘……真是遗憾呢。」"
    "为什么呢。"
    "我感受到了那声音中的悲痛。"
    "就好像在哭泣一样……"
    $ stopvoc("NAE")
    play NAE "RUK02B_NAE0002"
    $ current_voice = "voice/RUK02B_NAE0002.ogg"
    "綯" "「爸爸，真由理姐姐怎么了吗？」"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "不知何时，店长的孩子从店里探出了头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0007"
    $ current_voice = "voice/RUK02B_TEN0007.ogg"
    "天王寺" "「恩？啊啊，不。什么也没有。先不说那个，爸爸现在正在谈事情，绹的话在这段时间里先去看电视就好」"
    $ stopvoc("NAE")
    play NAE "RUK02B_NAE0003"
    $ current_voice = "voice/RUK02B_NAE0003.ogg"
    "綯" "「好的」"
    window hide
    hide lh6  with dissolve
    "叫做绹的女孩子就老实地回到了店里。"
    "端坐在巨大的显像管电视前，看着动画。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0045"
    $ current_voice = "voice/RUK02B_RUK0045.ogg"
    "琉华" "「令媛真是可爱呢」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0008"
    $ current_voice = "voice/RUK02B_TEN0008.ogg"
    "天王寺" "「恩？嘛……说起来这种时候，一般的反应不应该就是谦虚一下么。但我觉得是可爱到爆那种程度就是了」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0046"
    $ current_voice = "voice/RUK02B_RUK0046.ogg"
    "琉华" "「不不，以父亲的身份来说我认为那是理所当然的」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0009"
    $ current_voice = "voice/RUK02B_TEN0009.ogg"
    "天王寺" "「嘿嘿。那么说真是帮了大忙了」"
    "店长害羞的表情，果然十分温柔。"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0010"
    $ current_voice = "voice/RUK02B_TEN0010.ogg"
    "天王寺" "「……那家伙的事……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0047"
    $ current_voice = "voice/RUK02B_RUK0047.ogg"
    "琉华" "「诶？」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0011"
    $ current_voice = "voice/RUK02B_TEN0011.ogg"
    "天王寺" "「不要把那个小姑娘的事情告诉绹哦」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0012"
    $ current_voice = "voice/RUK02B_TEN0012.ogg"
    "天王寺" "「那家伙可亲椎名真由理了……」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0048"
    $ current_voice = "voice/RUK02B_RUK0048.ogg"
    "琉华" "「店长……」"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0013"
    $ current_voice = "voice/RUK02B_TEN0013.ogg"
    "天王寺" "「冈部在干嘛？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0049"
    $ current_voice = "voice/RUK02B_RUK0049.ogg"
    "琉华" "「……一直消沉着」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0014"
    $ current_voice = "voice/RUK02B_TEN0014.ogg"
    "天王寺" "「是吗。嘛，也不是没有道理呢。人的逝去是……令人悲伤的事呢……」"
    "天王寺像是想起了什么久远的回忆一样说道。"
    "看起来是想起了谁的事情。"
    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0015"
    $ current_voice = "voice/RUK02B_TEN0015.ogg"
    "天王寺" "「但是呢……那说不定也是那姑娘的命运的一部分呢……」"

    "命运——"
    "不论怎么做都无法改变，那样的话确实是命运也说不定。"
    "但是，如果无法改变已经被决定的命运的话。"
    "我们又为何……要活在这个世界上呢。"
    "为什么呢……"

    stop bgm 
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0031"
    $ current_voice = "voice/RUK02B_CRS0031.ogg"
    "红莉栖" "「漆原！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "陷入了沉思的我，被牧濑的声音唤醒了。"
    play bgm "FD2BGM11"

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0032"
    $ current_voice = "voice/RUK02B_CRS0032.ogg"
    "红莉栖" "「稍等我一下啊」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0050"
    $ current_voice = "voice/RUK02B_RUK0050.ogg"
    "琉华" "「那也就是说，已经……？」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0033"
    $ current_voice = "voice/RUK02B_CRS0033.ogg"
    "红莉栖" "「恩恩，之后只要和我刚才说的那么做就行了」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0051"
    $ current_voice = "voice/RUK02B_RUK0051.ogg"
    "琉华" "「……」"
    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0034"
    $ current_voice = "voice/RUK02B_CRS0034.ogg"
    "红莉栖" "「可以的吧？」"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0052"
    $ current_voice = "voice/RUK02B_RUK0052.ogg"
    "琉华" "「恩。我……会努力的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA06"),"True","lh/CRS_HSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0035"
    $ current_voice = "voice/RUK02B_CRS0035.ogg"
    "红莉栖" "「恩」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "RUK02B_TEN0016"
    $ current_voice = "voice/RUK02B_TEN0016.ogg"
    "天王寺" "「喂喂，你们在说什么啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC01"),"True","lh/CRS_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02B_CRS0036"
    $ current_voice = "voice/RUK02B_CRS0036.ogg"
    "红莉栖" "「不好意思，能稍微占用一些时间吗？其实是关于显像管……」"
    window hide
    scene expression Solid("000000")  with fade

    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "趁着店长的注意力被牧濑吸引住的时候，我再次向研究室走去。"
    window hide


    $ loadBG(0,"BG03A4")

    show screen phonebtn
    "走进房间，然后就马上朝着电子微波炉的房间走去。"
    "冈部师傅的样子和刚才没有区别，似乎并没有注意到我的行动。"
    "一想到我要一个人跳回到过去这一点，又有些毛骨悚然。"
    "但是，牧濑正在为我争取时间，所以没有磨蹭的时间可以浪费了。"
    hide screen phonebtn
    hide screen phoneSD1

    stop bgm 
    "我将装置戴到头上，深深地呼吸了几次。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0053"
    $ current_voice = "voice/RUK02B_RUK0053.ogg"
    "琉华" "「呼……」"
    show houden 
    window hide

    play se "SGSE035L" loop

    "将颤抖的手指放到有些古老的键盘上面。"
    $ stopvoc("RUK")
    play RUK "RUK02B_RUK0054"
    $ current_voice = "voice/RUK02B_RUK0054.ogg"
    "琉华" "「──！」"
    "下定决心按下回车。"

    window hide

    stop se

    play se "SGSE067"


    play se "SGSE053L" loop

    stop se


    play se "SGSE013"

    hide screen phoneSD1
    window hide


    hide screen phonebtn
    hide houden 
    scene expression Solid("000000")  with fade
    call timeleap (fromtime=[8,16,20,30], totime=[8,15,5,30], fromday=[1])


    return




    stop se







    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
