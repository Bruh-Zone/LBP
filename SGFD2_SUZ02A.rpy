label SGFD2_SUZ02A:
    window hide


    $ loadBG(0,"BG04A1")

    play bgm "BGM07"

    $ date="8/11"
    $ day = "WED"
    show screen phonebtn
    show screen phoneSD1

    "他看着我的目光的变化让我感到很恐怖。"
    "虽然一直没能和他交流过发生了什么，但感觉他的目光变化并不是我这边的原因。"
    play se "SGSE017"


    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0000"
    $ current_voice = "voice/SUZ02A_OKA0000.ogg"
    "伦太郎" "「打工战士，你在吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0000"
    $ current_voice = "voice/SUZ02A_SUZ0000.ogg"
    "铃羽" "「怎么了，冈部？」"
    "冈部来到我打工的地方时，我最开始并没有注意到他。"
    "简直和换了个人似的。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0001"
    $ current_voice = "voice/SUZ02A_OKA0001.ogg"
    "伦太郎" "「手没事吧？ 」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0001"
    $ current_voice = "voice/SUZ02A_SUZ0001.ogg"
    "铃羽" "「手？手怎么了？难道还醉着吗？ 」"
    "昨天就觉得他有些怪怪的了，没想到今天更胜一筹。"
    "果然仅仅解释为发酒疯是说不通的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0002"
    $ current_voice = "voice/SUZ02A_OKA0002.ogg"
    "伦太郎" "「我问你的手有没有事」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0002"
    $ current_voice = "voice/SUZ02A_SUZ0002.ogg"
    "铃羽" "「没事啊！ 」"
    "虽然不明白他为什么这么问，但看到冈部伦太郎那一脸“我是认真的请你回答我”的表情，我把双手举到了胸前让他看清手心和手背。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0003"
    $ current_voice = "voice/SUZ02A_SUZ0003.ogg"
    "铃羽" "「你觉不觉得有点暗？ 」"
    "因为有些担心所以试着问了一下，但是他完全没有反应。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0003"
    $ current_voice = "voice/SUZ02A_OKA0003.ogg"
    "伦太郎" "「对呢……现在还不是受伤的时候」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0004"
    $ current_voice = "voice/SUZ02A_SUZ0004.ogg"
    "铃羽" "「……怎么了？受伤的时间是怎么回事？ 」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0004"
    $ current_voice = "voice/SUZ02A_OKA0004.ogg"
    "伦太郎" "「你的时间机器坏了」"
    "冈部现在才第一次正视着我。"
    "我也盯着他的眼睛，看见了我来这个时代之后，从未没有见到过的呆滞眼神。"
    "那种眼神与我在反抗组织的同伴如出一辙。"
    "饱含着失去了重要的人的悲伤。"
    "而且是那种因为自己的无能为力而反复失去的绝望。"
    "只是一两人的话是不足以到达这样的程度的。"
    "是那种内心不断地被击溃，不断地站起来，然而依然不断地失去挚爱，最终对自己感到愤怒才会有的眼神。"
    "从昨天的冈部来看根本无法想象他会有这样的眼神。"
    "与昨天还自信地断定网络的约翰·提托就是我的父亲，然后意气风发地回去的他相比，就仿佛是另外一个人一样。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0005"
    $ current_voice = "voice/SUZ02A_SUZ0005.ogg"
    "铃羽" "「我的时间机器…… 诶？我的？ 」"
    "他所说的话解答了我心中的疑惑。"
    "如果是昨天的他的话，应该不可能说出这样的话。"
    "也就是说站在我眼前的，并不是昨天的那个冈部伦太郎。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0005"
    $ current_voice = "voice/SUZ02A_OKA0005.ogg"
    "伦太郎" "「没错，你的时间机器」"
    "在昨天到今天这段时间里，他度过了相当长的时间。"
    "虽然说出来有些矛盾，但确实如此。"
    "他用了某些方法，让这事成为可能。"
    "某些方法？"
    "那肯定没有其他选项了。"
    "一定是时间机器。"
    "就像我阿万音铃羽是从未来来的约翰·提托一样，他也成为了时间旅行者。"
    "使用的是除了我的时间机器之外的其他的时间机器。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0006"
    $ current_voice = "voice/SUZ02A_SUZ0006.ogg"
    "铃羽" "「你是从哪个时间点来的？ 」"
    "但是这样并不能解开全部的谜题。"
    "他的内在的确换了一个人。"
    "但是从外表上看起来还是和昨天一样。"
    "虽然不知道他是从如何绝望的情况下回到今天的，但是在现在这个和平的时代，一定是遭遇了多次痛彻心扉的打击吧？"
    "那是就算在我所处的时代也是需要很多年才会形成的伤。"
    "他的年龄并没有变化，但是他的内心却产生了如此大的变化，让人有一种不协调感。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0006"
    $ current_voice = "voice/SUZ02A_OKA0006.ogg"
    "伦太郎" "「你这么敏锐真是太好了」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0007"
    $ current_voice = "voice/SUZ02A_OKA0007.ogg"
    "伦太郎" "「我是从８月１３日……两天后来的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0007"
    $ current_voice = "voice/SUZ02A_SUZ0007.ogg"
    "铃羽" "「两天后…… 」"
    "让我明白了他为什么外表没变老的原因。"
    "这种情况下没变老是正常的。"
    "但是这样的话他的内心就很奇怪了。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0008"
    $ current_voice = "voice/SUZ02A_OKA0008.ogg"
    "伦太郎" "「我们完成了电话微波炉（暂定）的改良，将记忆变成数据送到过去，这一人类最大的伟业」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0009"
    $ current_voice = "voice/SUZ02A_OKA0009.ogg"
    "伦太郎" "「我们根据这个特性，将这台机器命名为『时间跳跃机器』 」"
    window hide


    $ loadBG(2,"IBGX012",over=True)




    hide screen phonebtn
    "冈部伦太郎开始说出超乎我的想象的关于未来的故事。"
    "冈部伦太郎通过这台时间机器，想起了未来两天内的记忆。"
    "并不是物理上进行时间跳跃。"
    "而是在过去回忆起未来。"
    "先不提是什么原理，但是还是能算是时间旅行。"
    "但我好歹也是时间旅行者。"
    "如果只是这样并不让人惊奇。"
    window hide
    hide background-over 



    show screen phonebtn
    "超出我想象的是，冈部伦太郎回到——虽然这么说很奇怪——“今天”的理由。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0008"
    $ current_voice = "voice/SUZ02A_SUZ0008.ogg"
    "铃羽" "「椎名真由理……被杀了？」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0010"
    $ current_voice = "voice/SUZ02A_OKA0010.ogg"
    "伦太郎" "「没错」"
    "冈部伦太郎声音突然变得似乎突然喘不过气来，但还是清楚地回答了。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0011"
    $ current_voice = "voice/SUZ02A_OKA0011.ogg"
    "伦太郎" "「被杀了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0012"
    $ current_voice = "voice/SUZ02A_OKA0012.ogg"
    "伦太郎" "「被他们杀了──被ＳＥＲＮ」"
    "此后冈部伦太郎多次回忆起了「可能的未来」，寻找着能拯救椎名真由理的未来。"
    "但是，椎名真由理在任何情况下都死了。"
    "无法回避这个未来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0013"
    $ current_voice = "voice/SUZ02A_OKA0013.ogg"
    "伦太郎" "「我原以为只要躲开ＳＥＲＮ就能得救。但是不行。从那之后进行了无数次时间跳跃，试遍了各种方法」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD02"),"True","lh/OKA_ASD02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0014"
    $ current_voice = "voice/SUZ02A_OKA0014.ogg"
    "伦太郎" "「但是……１３日的晚上，真由理一定会死去。唯独这个'结果'无法被改变」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0009"
    $ current_voice = "voice/SUZ02A_SUZ0009.ogg"
    "铃羽" "「这是世界线的收缩」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0015"
    $ current_voice = "voice/SUZ02A_OKA0015.ogg"
    "伦太郎" "「我之前从你那听说过了。从对你来说还没有发生过的未来中，我已经听说了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0010"
    $ current_voice = "voice/SUZ02A_SUZ0010.ogg"
    "铃羽" "「如果不是这样，你也不会说我的时间机器坏了这种话了呢」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0016"
    $ current_voice = "voice/SUZ02A_OKA0016.ogg"
    "伦太郎" "「嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0017"
    $ current_voice = "voice/SUZ02A_OKA0017.ogg"
    "伦太郎" "「……你不担心时间机器坏掉这件事吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0011"
    $ current_voice = "voice/SUZ02A_SUZ0011.ogg"
    "铃羽" "「我已经知道了。而且昨天还在烦恼该不该跟你说。说到能在这个时代修好的人就只有冈部伦太郎你们几个了」"
    window hide





    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0012"
    $ current_voice="voice/SUZ02A_SUZ0012.ogg"
    "铃羽β" "「关于这件事，α」"
    "因为冈部伦太郎所说的话带来的冲击性太强，我忘记了我身边还有两个「另一个我」。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0013"
    $ current_voice = "voice/SUZ02A_SUZ0013.ogg"
    "铃羽" "「什么？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0014"
    $ current_voice="voice/SUZ02A_SUZ0014.ogg"
    "铃羽β" "「我基本已经将时间机器相关的基础讲座听过了一遍。当然修理的方法也包括其中」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0015"
    $ current_voice="voice/SUZ02A_SUZ0015.ogg"
    "铃羽β" "「所以，这个时代的人修好它的可能性很高」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0016"
    $ current_voice = "voice/SUZ02A_SUZ0016.ogg"
    "铃羽" "「诶！这么重要的事你怎么不早点说！？」"
    "听我发出惊讶的声音，冈部伦太郎用一副奇怪的表情看着我。也难怪他。从他的角度来看，我所说的完全意义不明。"
    window hide
    hide lh7 
    hide lh6 




    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0018"
    $ current_voice = "voice/SUZ02A_OKA0018.ogg"
    "伦太郎" "「怎么了，打工战士……你在跟谁说话？」"
    "又要再说明一次吗……。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0017"
    $ current_voice = "voice/SUZ02A_SUZ0017.ogg"
    "铃羽" "「现在在我周围还有另外两个我。其中的一个说，也许时间机器能够修好……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0019"
    $ current_voice = "voice/SUZ02A_OKA0019.ogg"
    "伦太郎" "「虽说不觉得现在是讲笑话的时候，但老实说，我不清楚你在说什么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0018"
    $ current_voice = "voice/SUZ02A_SUZ0018.ogg"
    "铃羽" "「说的也是……。总之你先将刚刚的事详细说给我听听」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0020"
    $ current_voice = "voice/SUZ02A_OKA0020.ogg"
    "伦太郎" "「啊，好……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0019"
    $ current_voice = "voice/SUZ02A_SUZ0019.ogg"
    "铃羽" "「所以说……」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BLB04"),"True","lh/SUZ_BLB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我面向β。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0020"
    $ current_voice = "voice/SUZ02A_SUZ0020.ogg"
    "铃羽" "「真的能修好吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0021"
    $ current_voice="voice/SUZ02A_SUZ0021.ogg"
    "铃羽β" "「我没见过实物，现在无法作定论」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VGL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VGL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_VGL"])
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0022"
    $ current_voice = "voice/SUZ02A_SUZ0022.ogg"
    "铃羽" "「你知道时间机器的状态吗？因为{color=#f00}ＶＧＬ{/color}不稳定，本应该出现在电台馆的屋顶上，却因为误差镶入了墙壁之中。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0023"
    $ current_voice = "voice/SUZ02A_SUZ0023.ogg"
    "铃羽" "「正因如此各个部分都有所破损」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0024"
    $ current_voice = "voice/SUZ02A_SUZ0024.ogg"
    "铃羽" "「只是淋了雨就故障了肯定是因为原来就有受损的地方」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BLA06"),"True","lh/SUZ_BLA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0025"
    $ current_voice="voice/SUZ02A_SUZ0025.ogg"
    "铃羽β" "「原来如此。看起来性能比我父亲做的时间机器要差」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0026"
    $ current_voice = "voice/SUZ02A_SUZ0026.ogg"
    "铃羽" "「我的时间机器也是父亲做的。只不过是未完成的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BLB04"),"True","lh/SUZ_BLB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0027"
    $ current_voice="voice/SUZ02A_SUZ0027.ogg"
    "铃羽β" "「无论怎么说，如果只是因为下雨就产生的故障，应该不会有这么严重。我深信这一点」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0028"
    $ current_voice="voice/SUZ02A_SUZ0028.ogg"
    "铃羽β" "「不过，ＶＧＬ就是黑匣子的部分，我也不能修。也不知道修理的方法。如果那个坏掉了就没办法了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0029"
    $ current_voice = "voice/SUZ02A_SUZ0029.ogg"
    "铃羽" "「不稳定与坏掉有区别吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0030"
    $ current_voice="voice/SUZ02A_SUZ0030.ogg"
    "铃羽β" "「如果是不稳定，本应该出现在屋顶上的出现在了同一栋大厦的墙壁中，这应该是在误差范围内的」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0031"
    $ current_voice="voice/SUZ02A_SUZ0031.ogg"
    "铃羽β" "「但如果坏了，不能修理的话，过去未来就都不能去了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0032"
    $ current_voice = "voice/SUZ02A_SUZ0032.ogg"
    "铃羽" "「未来？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0033"
    $ current_voice="voice/SUZ02A_SUZ0033.ogg"
    "铃羽β" "「没错」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0034"
    $ current_voice = "voice/SUZ02A_SUZ0034.ogg"
    "铃羽" "「未来也能去……」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0035"
    $ current_voice="voice/SUZ02A_SUZ0035.ogg"
    "铃羽β" "「什么意思？」"
    "β的话让我很惊讶。"
    "她所在的世界线中的时间机器比我的要优秀很多。"
    "因为可以去向未来。"
    "与我的那个只能单向回到过去的时间机器有很大的不同。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0036"
    $ current_voice="voice/SUZ02A_SUZ0036.ogg"
    "铃羽β" "「无论怎么说，还是要先看看才行」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0037"
    $ current_voice = "voice/SUZ02A_SUZ0037.ogg"
    "铃羽" "「嗯」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0038"
    $ current_voice = "voice/SUZ02A_SUZ0038.ogg"
    "铃羽" "「冈部伦太郎，她说我的时间机器好像可以修好了」"
    "我心中充满了希望，这样对他说。"

    stop bgm 
    "但是。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0021"
    $ current_voice = "voice/SUZ02A_OKA0021.ogg"
    "伦太郎" "「这样啊……」"
    "他看起来不怎么高兴。"
    "让我再度思考冈部伦太郎究竟是经过了多少次时间轮回才回到今天的。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0039"
    $ current_voice = "voice/SUZ02A_SUZ0039.ogg"
    "铃羽" "「之后……能见到父亲就好了，但是这个愿望真是奢侈」"





    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0040"
    $ current_voice="voice/SUZ02A_SUZ0040.ogg"
    "铃羽β" "「父亲？怎么了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0041"
    $ current_voice = "voice/SUZ02A_SUZ0041.ogg"
    "铃羽" "「没什么。什么事都没有……」"
    "于是我们立刻往时间机器那去了。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG06A1")





    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0042"
    $ current_voice = "voice/SUZ02A_SUZ0042.ogg"
    "铃羽" "「怎样？能修好吗？」"
    "β进入时间机器的驾驶舱，已经过去差不多10分钟了。稍微有些不耐烦，我试着出声问道。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0043"
    $ current_voice="voice/SUZ02A_SUZ0043.ogg"
    "铃羽β" "「基本是一样的。但是，是比我所知道的更加古老的型号。是被称为原型机的那台」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0044"
    $ current_voice = "voice/SUZ02A_SUZ0044.ogg"
    "铃羽" "「也就是说？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0045"
    $ current_voice="voice/SUZ02A_SUZ0045.ogg"
    "铃羽β" "「半天就能修好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0046"
    $ current_voice = "voice/SUZ02A_SUZ0046.ogg"
    "铃羽" "「啊啊……太好了……」"
    "说完话后全身都没力了，一屁股坐在了地上。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "β走过来将我拉了起来。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0047"
    $ current_voice="voice/SUZ02A_SUZ0047.ogg"
    "铃羽β" "「没事吧？」"
    "握住β的手时我的力气回来了，一下子站了起来。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0048"
    $ current_voice = "voice/SUZ02A_SUZ0048.ogg"
    "铃羽" "「只是松了口气」"
    "话说，我能握住β的手了。"
    "现在才发现。果然不仅仅是幻觉。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0049"
    $ current_voice="voice/SUZ02A_SUZ0049.ogg"
    "铃羽β" "「如果你这么想修好的话，早点跟我说不就行了吗」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0050"
    $ current_voice = "voice/SUZ02A_SUZ0050.ogg"
    "铃羽" "「我没说过吗？」"
    "因为没提起过导致她不知道这点让我有些不快。时间机器对β来说，与对我来说有相当大的不同。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0051"
    $ current_voice="voice/SUZ02A_SUZ0051.ogg"
    "铃羽β" "「我听说过坏了对你打击很大，但是你应该没说过你想修好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0052"
    $ current_voice = "voice/SUZ02A_SUZ0052.ogg"
    "铃羽" "「是吗……」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0053"
    $ current_voice="voice/SUZ02A_SUZ0053.ogg"
    "铃羽β" "「况且我也不知道你为什么要来这个时代。在我没听到你跟冈伦叔叔的对话之前。」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0054"
    $ current_voice = "voice/SUZ02A_SUZ0054.ogg"
    "铃羽" "「你那边的情况很不同吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0055"
    $ current_voice="voice/SUZ02A_SUZ0055.ogg"
    "铃羽β" "「是呢。但是还是不要详细说比较好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0056"
    $ current_voice = "voice/SUZ02A_SUZ0056.ogg"
    "铃羽" "「为什么？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0057"
    $ current_voice="voice/SUZ02A_SUZ0057.ogg"
    "铃羽β" "「也有不想让冈伦叔叔知道的事情」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0058"
    $ current_voice = "voice/SUZ02A_SUZ0058.ogg"
    "铃羽" "「是Ｒｅａｄｉｎｇ　Ｓｔｅｉｎｅｒ的关系啊」"
    "冈部伦太郎有特殊的能力。"
    "就算世界线发生变化，他也能保留过去的记忆这一特殊能力。"
    "本来对于一般的人类来说，其他世界线的知识并没有意义，也不需要记得。"
    "但是冈部伦太郎不同。"
    "β的世界线中冈部伦太郎知道了的话会很麻烦的事情，也不能让让这个世界的冈部伦太郎知道的可能性也是有的。"
    "那个不希望被冈部知道的事情，也许并不限于β的时间线中。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0059"
    $ current_voice="voice/SUZ02A_SUZ0059.ogg"
    "铃羽β" "「与那个能力也有关，在我的世界中冈伦叔叔是很重要的人物」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0060"
    $ current_voice = "voice/SUZ02A_SUZ0060.ogg"
    "铃羽" "「哦」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0022"
    $ current_voice = "voice/SUZ02A_OKA0022.ogg"
    "伦太郎" "「怎样，能修好吗？」"
    window hide



    $ loadBG(2,"BG06A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "说曹操曹操到。冈部伦太郎出现了。"
    "身边的椎名真由理也一起。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0061"
    $ current_voice = "voice/SUZ02A_SUZ0061.ogg"
    "铃羽" "「说是半天就能修好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0023"
    $ current_voice = "voice/SUZ02A_OKA0023.ogg"
    "伦太郎" "「这样啊。可以说是已经度过了一个难关了嘛？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0062"
    $ current_voice = "voice/SUZ02A_SUZ0062.ogg"
    "铃羽" "「应该是」"
    "这样父亲受挫的计划就能按原定的进行了。虽然比预定的晚了几天，但还处于能接受的范围。"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0000"
    $ current_voice = "voice/SUZ02A_MAY0000.ogg"
    "真由理" "「时间机器，真大啊。这个有没有取什么名字？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0024"
    $ current_voice = "voice/SUZ02A_OKA0024.ogg"
    "伦太郎" "「真由理，现在还是不要问那种无关紧要的事了」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0025"
    $ current_voice = "voice/SUZ02A_OKA0025.ogg"
    "伦太郎" "「铃羽，如果需要人手的话，我去拜托桶子帮忙」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0026"
    $ current_voice = "voice/SUZ02A_OKA0026.ogg"
    "伦太郎" "「别看他那样，手可灵巧了。未来道具的一大半都是他制作的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0063"
    $ current_voice = "voice/SUZ02A_SUZ0063.ogg"
    "铃羽" "「这件事还是不和他说比较好吧」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0027"
    $ current_voice = "voice/SUZ02A_OKA0027.ogg"
    "伦太郎" "「需要的零件，也可以问桶子。秋叶原哪儿有什么样的零件卖，桶子大概全都知道」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0028"
    $ current_voice = "voice/SUZ02A_OKA0028.ogg"
    "伦太郎" "「话说，是该把桶子叫过来吧……。果然是天气太热的原因吗，都感觉有些松懈下来了。」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0064"
    $ current_voice = "voice/SUZ02A_SUZ0064.ogg"
    "铃羽" "「我有时会想，冈部伦太郎在未来道具研究所中，究竟做些什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0029"
    $ current_voice = "voice/SUZ02A_OKA0029.ogg"
    "伦太郎" "「……都说我是出点子的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0065"
    $ current_voice = "voice/SUZ02A_SUZ0065.ogg"
    "铃羽" "「实际工作并没有怎么做呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0001"
    $ current_voice = "voice/SUZ02A_MAY0001.ogg"
    "真由理" "「呐呐，冈伦，我忘记说一件重要的事了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0030"
    $ current_voice = "voice/SUZ02A_OKA0030.ogg"
    "伦太郎" "「重要的事？」"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0002"
    $ current_voice = "voice/SUZ02A_MAY0002.ogg"
    "真由理" "「铃小姐的父亲，现在在哪？」"
    "好不容易忘掉的事情，又被椎名真由理挖了出来，让我有种突然无力感。明明如果时间机器能修好的话，对其他的事就应该不再奢望了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0066"
    $ current_voice = "voice/SUZ02A_SUZ0066.ogg"
    "铃羽" "「……父亲是谁，怎样都行吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC03"),"True","lh/MAY_ASC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0003"
    $ current_voice = "voice/SUZ02A_MAY0003.ogg"
    "真由理" "「不是怎样都行」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0004"
    $ current_voice = "voice/SUZ02A_MAY0004.ogg"
    "真由理" "「而且时间机器只需要半天就修好吧？那在这段时间里，麻由氏就去找铃小姐的父亲」"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0005"
    $ current_voice = "voice/SUZ02A_MAY0005.ogg"
    "真由理" "「怎样？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0031"
    $ current_voice = "voice/SUZ02A_OKA0031.ogg"
    "伦太郎" "「呃，不过……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB04"),"True","lh/MAY_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0006"
    $ current_voice = "voice/SUZ02A_MAY0006.ogg"
    "真由理" "「啊，小冈伦这样可不行哦。与朋友的约定呢，一定要好好遵守才行」"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0007"
    $ current_voice = "voice/SUZ02A_MAY0007.ogg"
    "真由理" "「之前不是约定好了吗？大家一起去找铃小姐的父亲」"
    "约定。的确之前开安慰派对的时候，我想起冈部伦太郎他们说过这样的话。"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0032"
    $ current_voice = "voice/SUZ02A_OKA0032.ogg"
    "伦太郎" "「的确，是这样呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0008"
    $ current_voice = "voice/SUZ02A_MAY0008.ogg"
    "真由理" "「那个，虽然铃小姐来这里，是有使命的，但我觉得果然她还是想见到父亲的吧」"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0009"
    $ current_voice = "voice/SUZ02A_MAY0009.ogg"
    "真由理" "「如果是的话，麻由氏就想让你们见面」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0067"
    $ current_voice = "voice/SUZ02A_SUZ0067.ogg"
    "铃羽" "「椎名真由理，你，真是好孩子……」"
    "等我回过神来才发现自己都快要落泪了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0068"
    $ current_voice = "voice/SUZ02A_SUZ0068.ogg"
    "铃羽" "「……就是这样」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0069"
    $ current_voice = "voice/SUZ02A_SUZ0069.ogg"
    "铃羽" "「来到这里，我以为能见到……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0070"
    $ current_voice = "voice/SUZ02A_SUZ0070.ogg"
    "铃羽" "「我知道父亲２０１０年的时候在秋叶原」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0033"
    $ current_voice = "voice/SUZ02A_OKA0033.ogg"
    "伦太郎" "「啊，真的在这里吗!？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0071"
    $ current_voice = "voice/SUZ02A_SUZ0071.ogg"
    "铃羽" "「在哦，真是失礼啊。在这时代的话，肯定是既年轻又帅气吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0034"
    $ current_voice = "voice/SUZ02A_OKA0034.ogg"
    "伦太郎" "「名字是……巴雷鲁·提托吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0072"
    $ current_voice = "voice/SUZ02A_SUZ0072.ogg"
    "铃羽" "「嗯，是呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0010"
    $ current_voice = "voice/SUZ02A_MAY0010.ogg"
    "真由理" "「哇，是外国人？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0073"
    $ current_voice = "voice/SUZ02A_SUZ0073.ogg"
    "铃羽" "「不是。大概是日本人。是他在抵抗时代的代号名。所以在现在的２０１０年，大概还没用这个名字」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0074"
    $ current_voice = "voice/SUZ02A_SUZ0074.ogg"
    "铃羽" "「父亲的真名，我……不知道」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0075"
    $ current_voice = "voice/SUZ02A_SUZ0075.ogg"
    "铃羽" "「明明是亲生女儿」"
    "发现自己真的快要哭出来的时候，我强迫自己露出了笑容。"
    "因为是强迫的，果然看起来就像是苦笑吧。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0076"
    $ current_voice = "voice/SUZ02A_SUZ0076.ogg"
    "铃羽" "「没有告诉我，在我问之前，就死了」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0035"
    $ current_voice = "voice/SUZ02A_OKA0035.ogg"
    "伦太郎" "「阿万音是假名吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0077"
    $ current_voice = "voice/SUZ02A_SUZ0077.ogg"
    "铃羽" "「不是不是。是我母亲的姓」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0036"
    $ current_voice = "voice/SUZ02A_OKA0036.ogg"
    "伦太郎" "「那，从这里入手也不行呢」"
    window hide



    $ loadBG(2,"BG06A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "就在这时，房间的门开了，熟悉的桶装男子，满头大汗的出现了。"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0000"
    $ current_voice = "voice/SUZ02A_DAR0000.ogg"
    "至" "「啊，为什么电梯不能用了？这么炎热的时候，在没有空调的大楼内爬8层楼，想杀了我吗……」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0001"
    $ current_voice = "voice/SUZ02A_DAR0001.ogg"
    "至" "「嗯，咦？大家怎么全都一副忧郁的表情？」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0037"
    $ current_voice = "voice/SUZ02A_OKA0037.ogg"
    "伦太郎" "「桶子，太慢了！」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0002"
    $ current_voice = "voice/SUZ02A_DAR0002.ogg"
    "至" "「太慢也好怎样也好都是因为你要强拉我过来，至少也该说句谢谢我来了这种话吧」"
    "在冈部伦太郎和桥田至进行像相声一样的对话时，我听到了只有我能听见的惊呼声。"

    stop bgm 
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0078"
    $ current_voice="voice/SUZ02A_SUZ0078.ogg"
    "铃羽ω" "「啊！是父亲！真年轻！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0079"
    $ current_voice = "voice/SUZ02A_SUZ0079.ogg"
    "铃羽" "「诶？」"
    "我还以为自己听错了ω所说的。"
    "虽说能听到ω的声音还是令人感到奇怪，但现在不是关心这些的时候。"
    window hide



    $ loadBG(2,"BG06A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM22"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0080"
    $ current_voice = "voice/SUZ02A_SUZ0080.ogg"
    "铃羽" "「父亲？你刚刚说的是父亲？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0081"
    $ current_voice="voice/SUZ02A_SUZ0081.ogg"
    "铃羽ω" "「嗯。在那里的是我父亲哦」"
    "铃羽ω所指的是刚刚进来的桥田至。"
    "无论眨几次眼，看起来依旧是桥田至。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0082"
    $ current_voice = "voice/SUZ02A_SUZ0082.ogg"
    "铃羽" "「……真的吗？」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0038"
    $ current_voice = "voice/SUZ02A_OKA0038.ogg"
    "伦太郎" "「怎么了，打工战士。热晕头了？」"
    $ stopvoc("MAY")
    play MAY "SUZ02A_MAY0011"
    $ current_voice = "voice/SUZ02A_MAY0011.ogg"
    "真由理" "「铃小姐，你脸色不太好，没事吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0083"
    $ current_voice = "voice/SUZ02A_SUZ0083.ogg"
    "铃羽" "「等，等等。刚刚听到了冲击性的话，现在还在混乱中，不知道该如何是好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0084"
    $ current_voice="voice/SUZ02A_SUZ0084.ogg"
    "铃羽ω" "「咦？但是我的父亲是那边的那个人，α的父亲是不是不一样？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0085"
    $ current_voice="voice/SUZ02A_SUZ0085.ogg"
    "铃羽β" "「在我的世界线中桥田至也是我父亲」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0086"
    $ current_voice = "voice/SUZ02A_SUZ0086.ogg"
    "铃羽" "「那，肯定这个世界线中也是吧……」"

    stop bgm 
    "还打算去找父亲呢，原来早就见到了。"
    "在时间机器线下会上见不到那样子的人的理由，现在也知道了。"
    window hide



    $ loadBG(2,"BG06A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0003"
    $ current_voice = "voice/SUZ02A_DAR0003.ogg"
    "至" "「怎么了，阿万音氏？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0087"
    $ current_voice = "voice/SUZ02A_SUZ0087.ogg"
    "铃羽" "「啊，嗯，没事」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0004"
    $ current_voice = "voice/SUZ02A_DAR0004.ogg"
    "至" "「那就好……你脸很红哦」"
    "虽然让桥田至担心让我很高兴，但是脸红是由他造成这点……让人心情复杂。"
    play bgm "BGM26"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0005"
    $ current_voice = "voice/SUZ02A_DAR0005.ogg"
    "至" "「那，冈伦，你要让我做什么？」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0039"
    $ current_voice = "voice/SUZ02A_OKA0039.ogg"
    "伦太郎" "「修好时间机器！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0006"
    $ current_voice = "voice/SUZ02A_DAR0006.ogg"
    "至" "「肯定不可能吧常考」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0007"
    $ current_voice = "voice/SUZ02A_DAR0007.ogg"
    "至" "「我们连电话微波炉都不能让它运转起来哦？现在让我去修时间机器？怎么想都不可能的吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0088"
    $ current_voice = "voice/SUZ02A_SUZ0088.ogg"
    "铃羽" "「技术上的问题，另一个世界线上的我很了解，会来帮忙」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0008"
    $ current_voice = "voice/SUZ02A_DAR0008.ogg"
    "至" "「另一个世界线上的阿万音氏？」"
    "就在桥田至对我的话产生疑虑时，β已经在开始检查时间机器了。因此周围开始响起时间机器被到处开开关关的声音。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0009"
    $ current_voice = "voice/SUZ02A_DAR0009.ogg"
    "至" "「哦哦哦！？难道是灵异现象吗，这个！？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0089"
    $ current_voice = "voice/SUZ02A_SUZ0089.ogg"
    "铃羽" "「另一个我正在检查，大家放心吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0010"
    $ current_voice = "voice/SUZ02A_DAR0010.ogg"
    "至" "「也就是说幽灵会修好，就轮不到我出场了吧。那我回去了。太热了所以要回去了。」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0040"
    $ current_voice = "voice/SUZ02A_OKA0040.ogg"
    "伦太郎" "「等等，桶子！」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0011"
    $ current_voice = "voice/SUZ02A_DAR0011.ogg"
    "至" "「不是说幽灵会……」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0041"
    $ current_voice = "voice/SUZ02A_OKA0041.ogg"
    "伦太郎" "「希望你也帮帮忙」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0012"
    $ current_voice = "voice/SUZ02A_DAR0012.ogg"
    "至" "「不要，没我帮忙又没事。我，超怕热的。打杂什么的冈伦来做不就行了，说真的啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0042"
    $ current_voice = "voice/SUZ02A_OKA0042.ogg"
    "伦太郎" "「话虽如此……但是你对时间机器没有兴趣吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0013"
    $ current_voice = "voice/SUZ02A_DAR0013.ogg"
    "至" "「兴趣倒是有，但是要在这么热的地方工作就不想。如果是凉爽的夜晚的话拜托让我学习一下」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0043"
    $ current_voice = "voice/SUZ02A_OKA0043.ogg"
    "伦太郎" "「那，那打杂就行了。不过，希望你能帮忙买东西！能买回坏掉部件代替品的人只有你吧！？」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0014"
    $ current_voice = "voice/SUZ02A_DAR0014.ogg"
    "至" "「不能等到凉爽点吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0044"
    $ current_voice = "voice/SUZ02A_OKA0044.ogg"
    "伦太郎" "「如果现在让你回去了，夜晚之前你就不会出现了。感觉你会这样。我们没有这么多时间了」"
    $ stopvoc("OKA")
    play OKA "SUZ02A_OKA0045"
    $ current_voice = "voice/SUZ02A_OKA0045.ogg"
    "伦太郎" "「铃羽！你知道必须的零件吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0090"
    $ current_voice = "voice/SUZ02A_SUZ0090.ogg"
    "铃羽" "「现在正在检查」"
    "我又叫了一次时间机器中的β。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0091"
    $ current_voice = "voice/SUZ02A_SUZ0091.ogg"
    "铃羽" "「能弄清吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0092"
    $ current_voice="voice/SUZ02A_SUZ0092.ogg"
    "铃羽β" "「被闪电烧坏了三个电路板」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0093"
    $ current_voice = "voice/SUZ02A_SUZ0093.ogg"
    "铃羽" "「需要的配件呢？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0094"
    $ current_voice="voice/SUZ02A_SUZ0094.ogg"
    "铃羽β" "「我写下来，给我纸笔」"
    "β拿到笔记本后立刻就写了下来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0015"
    $ current_voice = "voice/SUZ02A_DAR0015.ogg"
    "至" "「哦哦，好厉害！真不愧是幽灵，动作真快！」"
    "我将纸条递给桥田至。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0095"
    $ current_voice = "voice/SUZ02A_SUZ0095.ogg"
    "铃羽" "「就是这些，这个时代能找到替代品吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0016"
    $ current_voice = "voice/SUZ02A_DAR0016.ogg"
    "至" "「嗯。这点东西很容易就找到了。话说就在我经常去的那家店中就全部有卖」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0017"
    $ current_voice = "voice/SUZ02A_DAR0017.ogg"
    "至" "「这些配件的选择……，制作这个东西的人真是有眼光啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0096"
    $ current_voice = "voice/SUZ02A_SUZ0096.ogg"
    "铃羽" "「啊哈哈」"
    "我只能苦笑，如果桥田至真的是父亲的话，用他喜欢的配件来制作也是说的通的。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0097"
    $ current_voice="voice/SUZ02A_SUZ0097.ogg"
    "铃羽β" "「铃羽……不对，α」"
    window hide



    $ loadBG(2,"BG06A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "我正在思考时，突然听到β叫我的声音。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0098"
    $ current_voice="voice/SUZ02A_SUZ0098.ogg"
    "铃羽β" "「等到配件搜集齐全后，我就可以修理了，你去跟大家交流一下吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0099"
    $ current_voice = "voice/SUZ02A_SUZ0099.ogg"
    "铃羽" "「不能全部都让你一个人来做」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0100"
    $ current_voice="voice/SUZ02A_SUZ0100.ogg"
    "铃羽β" "「有这么多人也没什么用啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0101"
    $ current_voice = "voice/SUZ02A_SUZ0101.ogg"
    "铃羽" "「这倒也是」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0102"
    $ current_voice="voice/SUZ02A_SUZ0102.ogg"
    "铃羽β" "「还有，因为现在父亲听不到我才说的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA06"),"True","lh/SUZ_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    stop bgm 
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0103"
    $ current_voice="voice/SUZ02A_SUZ0103.ogg"
    "铃羽β" "「这个时间机器只有回到过去的功能」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0104"
    $ current_voice = "voice/SUZ02A_SUZ0104.ogg"
    "铃羽" "「…………」"
    "我没有回答。"
    "但是在β看来这就已经是肯定的回答了。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0105"
    $ current_voice="voice/SUZ02A_SUZ0105.ogg"
    "铃羽β" "「所以你能留在这里的时间也不会长了吧？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0106"
    $ current_voice="voice/SUZ02A_SUZ0106.ogg"
    "铃羽β" "「知道了这点，但还要让你把仅剩的时间花在修理上，我做不了这样的事」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0107"
    $ current_voice = "voice/SUZ02A_SUZ0107.ogg"
    "铃羽" "「嗯」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0108"
    $ current_voice="voice/SUZ02A_SUZ0108.ogg"
    "铃羽β" "「到你明天出发前，还是跟父亲他们交流一下比较好」"
    "因为不想让别人知道所以一直保持沉默。"
    "但是β是在场唯一熟悉时间机器的人。"
    "不可能发现不了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ02A_SUZ0109"
    $ current_voice="voice/SUZ02A_SUZ0109.ogg"
    "铃羽β" "「而且ω……不对，铃羽在的话会打扰修理」"
    "但是β却很轻快地继续说了下去。"
    "不过ω就有些不开心。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0110"
    $ current_voice="voice/SUZ02A_SUZ0110.ogg"
    "铃羽ω" "「这，这算什么！为什么是我？α也一样吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMC01"),"True","lh/SUZ_DMC01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "……一样吗？"
    "嗯，的确。"
    "总之我还是接受了β的好意。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG17A",trans=fade)

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0111"
    $ current_voice = "voice/SUZ02A_SUZ0111.ogg"
    "铃羽" "「…………」"
    "好不容易找到了父亲，关键时刻却没能说出口。"
    "多亏了她们，现在变成了我们两人出去买东西的状况。"
    "不过，ω也在一起，也算是三个人吧。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM05"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0112"
    $ current_voice = "voice/SUZ02A_SUZ0112.ogg"
    "铃羽" "「真不好意思，桥田至。让你陪我出来买东西」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB05"),"True","lh/DAR_AMB05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0018"
    $ current_voice = "voice/SUZ02A_DAR0018.ogg"
    "至" "「没有，跟阿万音氏一起这点我没有意见，就只是不爽是被冈伦命令的这点，怎么说呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0019"
    $ current_voice = "voice/SUZ02A_DAR0019.ogg"
    "至" "「哦，就是这个。大叔，这个给我三个」"
    "在我眼中桥田至就是坐着实验室椅子敲电脑的人。"
    "像现在这样在外面见到他总有一种违和感。"
    window hide





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0113"
    $ current_voice="voice/SUZ02A_SUZ0113.ogg"
    "铃羽ω" "「父亲他，衣服虽然穿的很土，但是总觉得很帅气的样子」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0114"
    $ current_voice = "voice/SUZ02A_SUZ0114.ogg"
    "铃羽" "「诶！？是吗……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0115"
    $ current_voice="voice/SUZ02A_SUZ0115.ogg"
    "铃羽ω" "「虽然刚刚还在不爽地跟冈伦叔叔讨价还价，现在就已经干劲满满了。虽然胖胖的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0116"
    $ current_voice = "voice/SUZ02A_SUZ0116.ogg"
    "铃羽" "「这点……倒也是」"
    "看起来他似乎经常这样到配件店买东西。"
    "既不用考虑到哪去买，也不用因为要在店中买什么感到困惑。"
    "的确很帅气……也说不定。"
    window hide



    hide lh5  with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0020"
    $ current_voice = "voice/SUZ02A_DAR0020.ogg"
    "至" "「怎么，怎么啦？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0117"
    $ current_voice = "voice/SUZ02A_SUZ0117.ogg"
    "铃羽" "「没有，没什么事！没什么事！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0021"
    $ current_voice = "voice/SUZ02A_DAR0021.ogg"
    "至" "「今天的阿万音氏，说了很多没事呢？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0118"
    $ current_voice = "voice/SUZ02A_SUZ0118.ogg"
    "铃羽" "「是呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0022"
    $ current_voice = "voice/SUZ02A_DAR0022.ogg"
    "至" "「这样啊。另一位幽灵碳一起跟来了吧。那位是怎样的幽灵？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0119"
    $ current_voice = "voice/SUZ02A_SUZ0119.ogg"
    "铃羽" "「是为很注重服装打扮，身穿女仆服的幽灵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0023"
    $ current_voice = "voice/SUZ02A_DAR0023.ogg"
    "至" "「女仆幽灵经常跟你一起吗，羡慕嫉妒恨人难过。我也想要啊喂」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0024"
    $ current_voice = "voice/SUZ02A_DAR0024.ogg"
    "至" "「话说，我应该被那位女仆幽灵批判得很厉害吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0120"
    $ current_voice = "voice/SUZ02A_SUZ0120.ogg"
    "铃羽" "「似乎评价很高的样子」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0025"
    $ current_voice = "voice/SUZ02A_DAR0025.ogg"
    "至" "「诶？是吗？哪里？果然是戴帽子的方法吧？」"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_MAY01_01"]

    $ LR_RM_CHANCE=5
    window hide





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB02"),"True","lh/SUZ_DMB02a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0121"
    $ current_voice="voice/SUZ02A_SUZ0121.ogg"
    "铃羽ω" "「完全不是那里。那种体型不能用黄色」"
    window hide



    hide lh5  with dissolve
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0026"
    $ current_voice = "voice/SUZ02A_DAR0026.ogg"
    "至" "「她说什么了吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0122"
    $ current_voice = "voice/SUZ02A_SUZ0122.ogg"
    "铃羽" "「……男人不用看外表」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0027"
    $ current_voice = "voice/SUZ02A_DAR0027.ogg"
    "至" "「这是表扬的话吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0123"
    $ current_voice = "voice/SUZ02A_SUZ0123.ogg"
    "铃羽" "「大，大概」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0028"
    $ current_voice = "voice/SUZ02A_DAR0028.ogg"
    "至" "「那就好——好，这样幽灵所需要的第一张单子上的东西就买齐了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0124"
    $ current_voice = "voice/SUZ02A_SUZ0124.ogg"
    "铃羽" "「这么快？」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0029"
    $ current_voice = "voice/SUZ02A_DAR0029.ogg"
    "至" "「数量不是很多，刚刚去的那家店就全有」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0030"
    $ current_voice = "voice/SUZ02A_DAR0030.ogg"
    "至" "「这样等到电台馆时就任务完成了。真是轻松」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB06"),"True","lh/DAR_AMB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0031"
    $ current_voice = "voice/SUZ02A_DAR0031.ogg"
    "至" "「啊，不对，最困难的是爬上电台馆的楼梯……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0125"
    $ current_voice = "voice/SUZ02A_SUZ0125.ogg"
    "铃羽" "「我来拿吧。你这种没怎么锻炼的身体，上楼梯很辛苦吧？」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0032"
    $ current_voice = "voice/SUZ02A_DAR0032.ogg"
    "至" "「辛苦倒是辛苦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0033"
    $ current_voice = "voice/SUZ02A_DAR0033.ogg"
    "至" "「但我觉得我似乎一定要知道时间机器才行。拿回去，与幽灵碳一起修理」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0034"
    $ current_voice = "voice/SUZ02A_DAR0034.ogg"
    "至" "「所以阿万音氏就先去打工吧，继续寻找父亲也行」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0126"
    $ current_voice = "voice/SUZ02A_SUZ0126.ogg"
    "铃羽" "「………」"
    "桥田至提到父亲的话题这点让我说不出话来。"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0035"
    $ current_voice = "voice/SUZ02A_DAR0035.ogg"
    "至" "「踏上旅途之前，能找到父亲就好了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0127"
    $ current_voice = "voice/SUZ02A_SUZ0127.ogg"
    "铃羽" "「话虽这么说……我，该向椎名真由理和冈部伦太郎道谢才行」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_MAY02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_MAY02_01"])


    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0036"
    $ current_voice = "voice/SUZ02A_DAR0036.ogg"
    "至" "「诶？为什么？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0128"
    $ current_voice = "voice/SUZ02A_SUZ0128.ogg"
    "铃羽" "「我找到父亲了」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0037"
    $ current_voice = "voice/SUZ02A_DAR0037.ogg"
    "至" "「诶？是吗？什么时候？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0129"
    $ current_voice = "voice/SUZ02A_SUZ0129.ogg"
    "铃羽" "「我告诉过你幽灵是其他世界的我吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0038"
    $ current_voice = "voice/SUZ02A_DAR0038.ogg"
    "至" "「嗯」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0130"
    $ current_voice = "voice/SUZ02A_SUZ0130.ogg"
    "铃羽" "「其他世界的父亲，似乎还好好活着。所以幽灵们知道名字和长相」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0039"
    $ current_voice = "voice/SUZ02A_DAR0039.ogg"
    "至" "「这样啊。那由我去告诉小冈伦他们吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0131"
    $ current_voice = "voice/SUZ02A_SUZ0131.ogg"
    "铃羽" "「……嗯」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0040"
    $ current_voice = "voice/SUZ02A_DAR0040.ogg"
    "至" "「那现在去见父亲吗？那人叫什么名字？是我认识的人吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0132"
    $ current_voice = "voice/SUZ02A_SUZ0132.ogg"
    "铃羽" "「父亲的名字是……桥田至」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0041"
    $ current_voice = "voice/SUZ02A_DAR0041.ogg"
    "至" "「桥田至。好像是很常听到的名字呢？或者说是我听腻了的名字，话说……是我吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0133"
    $ current_voice = "voice/SUZ02A_SUZ0133.ogg"
    "铃羽" "「嗯。似乎是这样的」"
    window hide

    stop bgm 
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ002A"]]["Check"]=True


    $ loadBG(2,"EV_SUZ002A")



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0042"
    $ current_voice = "voice/SUZ02A_DAR0042.ogg"
    "至" "「………」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ002B"]]["Check"]=True


    $ loadBG(2,"EV_SUZ002B")



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0043"
    $ current_voice = "voice/SUZ02A_DAR0043.ogg"
    "至" "「…………………」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ002C"]]["Check"]=True


    $ loadBG(2,"EV_SUZ002C")



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0044"
    $ current_voice = "voice/SUZ02A_DAR0044.ogg"
    "至" "「也，也也，也就是说是怎么回事！？」"
    play bgm "FD2BGM10"
    "桥田至似乎相当混乱。"
    "这也不怪他。我从ω那里听到这事也很惊讶，直到现在还没能完全接受。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0134"
    $ current_voice = "voice/SUZ02A_SUZ0134.ogg"
    "铃羽" "「那个……如果从桥田至的角度来看，我应该是未来的女儿，吧」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0045"
    $ current_voice = "voice/SUZ02A_DAR0045.ogg"
    "至" "「这个，也就是说，我未来的女儿是阿万音氏？」"
    "已经混乱到开始学我说话了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0135"
    $ current_voice = "voice/SUZ02A_SUZ0135.ogg"
    "铃羽" "「就，就是这样……」"
    "虽然这是正确的回答，但是桥田至似乎已经不知道自己刚刚问了什么。"
    "只是开口说话但脑中并没有思考。"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0046"
    $ current_voice = "voice/SUZ02A_DAR0046.ogg"
    "至" "「也就是说阿万音氏的父亲……就是我？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0136"
    $ current_voice = "voice/SUZ02A_SUZ0136.ogg"
    "铃羽" "「是的」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0047"
    $ current_voice = "voice/SUZ02A_DAR0047.ogg"
    "至" "「……原来如此我不知道」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0137"
    $ current_voice = "voice/SUZ02A_SUZ0137.ogg"
    "铃羽" "「不知道？」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0048"
    $ current_voice = "voice/SUZ02A_DAR0048.ogg"
    "至" "「不是，我知道，但稍微等等」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ002D"]]["Check"]=True


    $ loadBG(2,"EV_SUZ002D")



    "桥田至说完后就沉默了。"
    "表情也僵住了。"
    "我无法知道桥田至究竟在想些什么。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0138"
    $ current_voice = "voice/SUZ02A_SUZ0138.ogg"
    "铃羽" "「不知道会比较好吗？」"
    "我有些不安地问了一句。"
    "我自己知道的时候也很惊讶。"
    "所以明白他现在很难立刻说出什么。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0139"
    $ current_voice = "voice/SUZ02A_SUZ0139.ogg"
    "铃羽" "「我是你女儿的话会让你很困惑吗？」"
    "但是什么都不说果然让人很害怕。"
    "对方是好不容易见到的父亲时更是如此。"
    "正确来说现在还不是我的父亲。"
    "总之，还是希望桥田至说些什么。"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0049"
    $ current_voice = "voice/SUZ02A_DAR0049.ogg"
    "至" "「对不起，这种时候我不知道该露出什么样的表情啊？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0140"
    $ current_voice = "voice/SUZ02A_SUZ0140.ogg"
    "铃羽" "「诶」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0050"
    $ current_voice = "voice/SUZ02A_DAR0050.ogg"
    "至" "「不对，抱歉。还是认真地回答比较好吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0141"
    $ current_voice = "voice/SUZ02A_SUZ0141.ogg"
    "铃羽" "「……嗯」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ002E"]]["Check"]=True


    $ loadBG(2,"EV_SUZ002E")



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0051"
    $ current_voice = "voice/SUZ02A_DAR0051.ogg"
    "至" "「虽然让我很惊讶，但是并没有给我添麻烦。」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0052"
    $ current_voice = "voice/SUZ02A_DAR0052.ogg"
    "至" "「况且知道未来的女儿是这么的可爱，我，大胜利——」"
    "不过看起来并不是很开心。"
    "也许现在惊讶还是大过喜悦。"
    window hide



    $ loadBG(2,"BG17A")

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0053"
    $ current_voice = "voice/SUZ02A_DAR0053.ogg"
    "至" "「那，这个……我能问一个问题吗？」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0054"
    $ current_voice = "voice/SUZ02A_DAR0054.ogg"
    "至" "「你，你母亲可爱吗？萝莉脸萝莉身，但是却有巨乳预定」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0142"
    $ current_voice = "voice/SUZ02A_SUZ0142.ogg"
    "铃羽" "「……这点先保密」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0055"
    $ current_voice = "voice/SUZ02A_DAR0055.ogg"
    "至" "「保密啊。但是既然还有没见过的未来妻子，我的人生又有希望了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0143"
    $ current_voice = "voice/SUZ02A_SUZ0143.ogg"
    "铃羽" "「这个，嗯，可以值得期待」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0056"
    $ current_voice = "voice/SUZ02A_DAR0056.ogg"
    "至" "「你这样一说一点都期待不起来了！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0144"
    $ current_voice = "voice/SUZ02A_SUZ0144.ogg"
    "铃羽" "「啊哈哈」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0057"
    $ current_voice = "voice/SUZ02A_DAR0057.ogg"
    "至" "「哈哈……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0145"
    $ current_voice = "voice/SUZ02A_SUZ0145.ogg"
    "铃羽" "「………」"
    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0058"
    $ current_voice = "voice/SUZ02A_DAR0058.ogg"
    "至" "「………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB02"),"True","lh/DAR_AMB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ02A_DAR0059"
    $ current_voice = "voice/SUZ02A_DAR0059.ogg"
    "至" "「那，那我回电台馆了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0146"
    $ current_voice = "voice/SUZ02A_SUZ0146.ogg"
    "铃羽" "「嗯，请路上小心」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我看着渐渐远去的桥田至——渐渐远去的父亲。"
    "感觉他的背影比之前见到的都要高大。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG04A1",trans=fade)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_DAR01_01"]

    $ LR_RM_CHANCE=1

    call CHECK_RM_RECEIVE
    play se "SGSE017"


    play bgm "BGM18"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0147"
    $ current_voice = "voice/SUZ02A_SUZ0147.ogg"
    "铃羽" "「安～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0000"
    $ current_voice = "voice/SUZ02A_TEN0000.ogg"
    "天王寺" "「打工的，你去什么地方闲逛了！」"
    "回到打工地点后，果然被骂了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0148"
    $ current_voice = "voice/SUZ02A_SUZ0148.ogg"
    "铃羽" "「抱歉，店长！」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0001"
    $ current_voice = "voice/SUZ02A_TEN0001.ogg"
    "天王寺" "「真是的，我马上就要去送东西了。」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0149"
    $ current_voice = "voice/SUZ02A_SUZ0149.ogg"
    "铃羽" "「这点，我刚刚已经说了抱歉了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0002"
    $ current_voice = "voice/SUZ02A_TEN0002.ogg"
    "天王寺" "「话说，你丫今天精神很好啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0150"
    $ current_voice = "voice/SUZ02A_SUZ0150.ogg"
    "铃羽" "「啊，嗯。烦恼已经解决了所以」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0003"
    $ current_voice = "voice/SUZ02A_TEN0003.ogg"
    "天王寺" "「那，重影现象也好了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0151"
    $ current_voice = "voice/SUZ02A_SUZ0151.ogg"
    "铃羽" "「诶？啊……这个还没有」"
    "现在只有ω一个人，β在别的地方。"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0004"
    $ current_voice = "voice/SUZ02A_TEN0004.ogg"
    "天王寺" "「这样啊。嘛，总之有精神了我也不用担心了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0152"
    $ current_voice = "voice/SUZ02A_SUZ0152.ogg"
    "铃羽" "「……嗯」"
    "我以为还会被更严厉地责备，想不到店长看起来更担心我。"
    "就这么在意重影现象这件事啊。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0153"
    $ current_voice = "voice/SUZ02A_SUZ0153.ogg"
    "铃羽" "「店长？为什么这么担心我？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA03"),"True","lh/TEN_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0005"
    $ current_voice = "voice/SUZ02A_TEN0005.ogg"
    "天王寺" "「啊？谁担心你丫的了——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0006"
    $ current_voice = "voice/SUZ02A_TEN0006.ogg"
    "天王寺" "「担心了吗。不对，担心了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0154"
    $ current_voice = "voice/SUZ02A_SUZ0154.ogg"
    "铃羽" "「为什么？我只是一个偶然来打工的人吧？虽然不知道店里之前有没有过打工的人」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA03"),"True","lh/TEN_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0007"
    $ current_voice = "voice/SUZ02A_TEN0007.ogg"
    "天王寺" "「怎么回事呢，看见你这家伙，总觉得不像是外人」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0155"
    $ current_voice = "voice/SUZ02A_SUZ0155.ogg"
    "铃羽" "「跟某个你认识的人很像吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0008"
    $ current_voice = "voice/SUZ02A_TEN0008.ogg"
    "天王寺" "「虽然年龄完全不同。但是跟我年轻时照顾过我的人，总有一点相似。」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0156"
    $ current_voice = "voice/SUZ02A_SUZ0156.ogg"
    "铃羽" "「诶！也就是说我看起来像老奶奶？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0009"
    $ current_voice = "voice/SUZ02A_TEN0009.ogg"
    "天王寺" "「别说失礼的话。那位可是位伟大的人」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0157"
    $ current_voice = "voice/SUZ02A_SUZ0157.ogg"
    "铃羽" "「诶？那我是伟大的女性？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA03"),"True","lh/TEN_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0010"
    $ current_voice = "voice/SUZ02A_TEN0010.ogg"
    "天王寺" "「……这样一说感觉又不像了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0158"
    $ current_voice = "voice/SUZ02A_SUZ0158.ogg"
    "铃羽" "「哇，真是过分啊，店长！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0011"
    $ current_voice = "voice/SUZ02A_TEN0011.ogg"
    "天王寺" "「总之是我尊敬的人，那位」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0012"
    $ current_voice = "voice/SUZ02A_TEN0012.ogg"
    "天王寺" "「租这里给冈部他们，也是因为那个人说要帮助年轻人。我自己年轻的时候也得过那个人的帮助」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0159"
    $ current_voice = "voice/SUZ02A_SUZ0159.ogg"
    "铃羽" "「诶。因果循环呢」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0013"
    $ current_voice = "voice/SUZ02A_TEN0013.ogg"
    "天王寺" "「是吧。你也感谢她吧。没有那个人就没有现在的我，你也就没有工作了」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_DAR01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_DAR01_01"])

    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0160"
    $ current_voice = "voice/SUZ02A_SUZ0160.ogg"
    "铃羽" "「是呢。那个人，叫什么名字？」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0014"
    $ current_voice = "voice/SUZ02A_TEN0014.ogg"
    "天王寺" "「叫铃小姐。说起来，跟你的名字也很像」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0161"
    $ current_voice = "voice/SUZ02A_SUZ0161.ogg"
    "铃羽" "「的确。椎名真由理就这么叫我的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0162"
    $ current_voice = "voice/SUZ02A_SUZ0162.ogg"
    "铃羽" "「那个铃小姐，铃是她的姓？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0015"
    $ current_voice = "voice/SUZ02A_TEN0015.ogg"
    "天王寺" "「不是。姓是桥田，桥田玲。难道你认识她？」"

    stop bgm 
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0163"
    $ current_voice = "voice/SUZ02A_SUZ0163.ogg"
    "铃羽" "「…………！」"
    "我不由自主地忘记了呼吸。"
    "这个名字不可能仅仅是偶然。"
    "而且ω也是这么认为，惊讶地看着我。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0164"
    $ current_voice="voice/SUZ02A_SUZ0164.ogg"
    "铃羽ω" "「难道是我的奶奶？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0165"
    $ current_voice = "voice/SUZ02A_SUZ0165.ogg"
    "铃羽" "「……应该不是」"
    "我吐槽的是ω，但是店长却以为是我在对他说话。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0016"
    $ current_voice = "voice/SUZ02A_TEN0016.ogg"
    "天王寺" "「不是。总之，应该不是」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0166"
    $ current_voice = "voice/SUZ02A_SUZ0166.ogg"
    "铃羽" "「啊，不是对店长……但是，嗯，应该不是」"
    "姓桥田名铃。"
    "如果是昨天的我，听到这些话应该不会有什么想法。"
    "但是现在我明白了。"
    "桥田玲是我。"
    "坐时间机器回到过去的我在这条世界线上。"
    "也就是说时间机器顺利地修好了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0167"
    $ current_voice = "voice/SUZ02A_SUZ0167.ogg"
    "铃羽" "「呐，店长。那位桥田玲女士现在在做什么？」"
    "这是我一时兴起地问出来的。"
    "对店长来说是过去的事情，对我来说却是未来的事。"
    "本来是不应该知道的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0017"
    $ current_voice = "voice/SUZ02A_TEN0017.ogg"
    "天王寺" "「死了」"
    play bgm "BGM31"
    "也不会知道了。"
    "这份感情比店长那句简短的话带来的冲击更强烈。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0168"
    $ current_voice = "voice/SUZ02A_SUZ0168.ogg"
    "铃羽" "「………死了？」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0018"
    $ current_voice = "voice/SUZ02A_TEN0018.ogg"
    "天王寺" "「明明那时候还没到该死的时候呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0169"
    $ current_voice = "voice/SUZ02A_SUZ0169.ogg"
    "铃羽" "「……这样啊」"
    "桥田玲如果是回到１９７５年的我，今年还活着的话应该只是５０岁出头。"
    "活着也并不奇怪。"
    "去世的原因是……"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0170"
    $ current_voice = "voice/SUZ02A_SUZ0170.ogg"
    "铃羽" "「为……」"
    "……不行。不能问。"
    "太害怕了，问不出口。"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0019"
    $ current_voice = "voice/SUZ02A_TEN0019.ogg"
    "天王寺" "「如果还活着就能介绍给冈部他们了。你们能这样乱来也是多亏了那位……」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0020"
    $ current_voice = "voice/SUZ02A_TEN0020.ogg"
    "天王寺" "「也许能跟你说上话。铃小姐，很珍惜一台跟你骑过的自行车相似的自行车」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0171"
    $ current_voice = "voice/SUZ02A_SUZ0171.ogg"
    "铃羽" "「那，肯定——」"
    "不是相似的自行车，就是那台自行车。"
    "我很想说但还是忍住了。"
    "不能跟店长说出实情。"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0021"
    $ current_voice = "voice/SUZ02A_TEN0021.ogg"
    "天王寺" "「怎么？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0172"
    $ current_voice = "voice/SUZ02A_SUZ0172.ogg"
    "铃羽" "「我觉得店长说的没错。我也想见见那个人」"
    "但见通过时间机器回到过去的我是危险的。"
    "况且，实际上也不能见了。"
    "但是希望「桥田玲」现在还活着。"
    "不然的话，回到过去的我就再也见不到冈部伦太郎他们了。"
    "这是已经发生过的过去了。"
    "就算我知道这件事后想去改变，因为世界线的收束，也绝对不会改变。"
    "这个世界的桥田玲肯定还是死的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0022"
    $ current_voice = "voice/SUZ02A_TEN0022.ogg"
    "天王寺" "「总之就是这样了，你小子以后也要成为伟大的人去帮助年轻人啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0173"
    $ current_voice = "voice/SUZ02A_SUZ0173.ogg"
    "铃羽" "「嗯。因为因果循环」"
    "虽然刚刚还说不想知道，但事实真的是这样。"
    "现在的我受店长照顾，回到过去的我去帮助店长。"
    "因为我跟店长之间有不可思议的因果循环。"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0023"
    $ current_voice = "voice/SUZ02A_TEN0023.ogg"
    "天王寺" "「哦，那我也该出去了，拜托你看家了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0174"
    $ current_voice = "voice/SUZ02A_SUZ0174.ogg"
    "铃羽" "「了解，店长！」"

    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "就这样店长出去了。"
    "只剩下我一个人时就像他说的那样，认真地看家……像平时一样，没有客人来。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0175"
    $ current_voice = "voice/SUZ02A_SUZ0175.ogg"
    "铃羽" "「有必要看家吗」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "因为太闲了，于是我开始跟ω聊天。"
    "ω似乎很喜欢这间店，还是像平时一样四处打量，发现某样东西后充满好奇地盯着看。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0176"
    $ current_voice="voice/SUZ02A_SUZ0176.ogg"
    "铃羽ω" "「看家的工作不就是待在那里么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0177"
    $ current_voice = "voice/SUZ02A_SUZ0177.ogg"
    "铃羽" "「这倒也是……」"
    "ω认真地回答了我。"
    "不过认真说起来的话，这家店为什么会开起来一样无法理解，因为这家店根本没客人来。"
    "也许店长还有其他的业务也说不定。"
    "还是说其实是资本家，开这家店只是兴趣而已。"
    play bgm "BGM26"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0178"
    $ current_voice = "voice/SUZ02A_SUZ0178.ogg"
    "铃羽" "「ω……铃羽打过工吗？」"
    "果然还是不习惯用我的名字去称呼我之外的人。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0179"
    $ current_voice="voice/SUZ02A_SUZ0179.ogg"
    "铃羽ω" "「有啊。就是很普通的打工」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0180"
    $ current_voice = "voice/SUZ02A_SUZ0180.ogg"
    "铃羽" "「普通的打工是什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_McDy"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_McDy"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_McDy"])
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0181"
    $ current_voice="voice/SUZ02A_SUZ0181.ogg"
    "铃羽ω" "「普通就是普通啊。{color=#f00}ＭａｃＤｏｎ·ｌｄ{/color}之类的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0182"
    $ current_voice = "voice/SUZ02A_SUZ0182.ogg"
    "铃羽" "「ＭａｃＤｏｎ·ｌｄ……就是那家卖汉堡包的店？你在那里做着说「欢迎光临！」这种工作吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0183"
    $ current_voice="voice/SUZ02A_SUZ0183.ogg"
    "铃羽ω" "「嗯。很奇怪吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0184"
    $ current_voice = "voice/SUZ02A_SUZ0184.ogg"
    "铃羽" "「也不是奇怪」"
    "虽然是ω，但是想象有着同样的脸的自己做那种工作时，总觉得有几分违和感。"
    "是我的人生中完全不可能发生的事情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB02"),"True","lh/SUZ_DMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0185"
    $ current_voice="voice/SUZ02A_SUZ0185.ogg"
    "铃羽ω" "「但是你的表情好像在说那很奇怪啊」"
    "但是ω让人意外地开始了尖锐的吐槽。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0186"
    $ current_voice = "voice/SUZ02A_SUZ0186.ogg"
    "铃羽" "「没，没有没有。不是在想你的事」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0187"
    $ current_voice="voice/SUZ02A_SUZ0187.ogg"
    "铃羽ω" "「不是？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0188"
    $ current_voice = "voice/SUZ02A_SUZ0188.ogg"
    "铃羽" "「我是在想我去做的话，会有些微妙的感觉」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB03"),"True","lh/SUZ_DMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "听了我的话ω一副「怪人」的表情。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ02A_SUZ0189"
    $ current_voice="voice/SUZ02A_SUZ0189.ogg"
    "铃羽ω" "「这个……嗯，倒也是」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0190"
    $ current_voice = "voice/SUZ02A_SUZ0190.ogg"
    "铃羽" "「……你呐」"
    "然后ω也没打算隐藏自己的想法。"
    "将自己所想的说了出来。"
    "ω就是这样的女孩子。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG05N2",trans=fade)

    show screen phonebtn
    show screen phoneSD1
    "结果今天也没有顾客来就到了打烊时间。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0191"
    $ current_voice = "voice/SUZ02A_SUZ0191.ogg"
    "铃羽" "「那，店长。明天见」"
    $ stopvoc("TEN")
    play TEN "SUZ02A_TEN0024"
    $ current_voice = "voice/SUZ02A_TEN0024.ogg"
    "天王寺" "「嗯，回家路上小心」"
    "我是回去呢还是稍微绕去β那里呢，稍微考虑了一下。"
    "结果被意外的人搭了话。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0000"
    $ current_voice = "voice/SUZ02A_CRS0000.ogg"
    "红莉栖" "「阿万音小姐，现在回去吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0192"
    $ current_voice = "voice/SUZ02A_SUZ0192.ogg"
    "铃羽" "「牧濑红莉栖……」"
    play bgm "BGM23"
    "我反射性地扫了她一眼。"
    "她在未来是在ＳＥＲＮ那边制作时间机器的女人。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DYSTOPIA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DYSTOPIA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DYSTOPIA"])
    "也就是成为{color=#f00}绝望乡{/color}的开端的「时间机器之母」。"
    "抵抗者的同伴们说过多少次了。"
    "「假如那个女人没造出时间机器的话」这种话。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0001"
    $ current_voice = "voice/SUZ02A_CRS0001.ogg"
    "红莉栖" "「又是那个？我还想向你道贺呢，你就这种态度」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0193"
    $ current_voice = "voice/SUZ02A_SUZ0193.ogg"
    "铃羽" "「什么道贺」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0002"
    $ current_voice = "voice/SUZ02A_CRS0002.ogg"
    "红莉栖" "「时间机器好像要修好了吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0194"
    $ current_voice = "voice/SUZ02A_SUZ0194.ogg"
    "铃羽" "「啊，嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0003"
    $ current_voice = "voice/SUZ02A_CRS0003.ogg"
    "红莉栖" "「还有，你见到父亲了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0195"
    $ current_voice = "voice/SUZ02A_SUZ0195.ogg"
    "铃羽" "「嗯」"
    "说到父亲的事情，我心中那些尖尖的刺都消了下去。"
    "如果她知道这点才这么说的话，牧濑红莉栖可是个了不起的策士。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0004"
    $ current_voice = "voice/SUZ02A_CRS0004.ogg"
    "红莉栖" "「恭喜你啊。不过如果是那位桥田的话，有点难以说出祝贺的话呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0196"
    $ current_voice = "voice/SUZ02A_SUZ0196.ogg"
    "铃羽" "「谢谢」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0005"
    $ current_voice = "voice/SUZ02A_CRS0005.ogg"
    "红莉栖" "「这个虽然有点小」"
    "牧濑红莉栖从手中的便利店袋子中拿出蛋糕。"
    "是一人份的草莓蛋糕。"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_OKA01_01"]

    $ LR_RM_CHANCE=8
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0197"
    $ current_voice = "voice/SUZ02A_SUZ0197.ogg"
    "铃羽" "「这个，给我？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0006"
    $ current_voice = "voice/SUZ02A_CRS0006.ogg"
    "红莉栖" "「如果你不讨厌的话」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0198"
    $ current_voice = "voice/SUZ02A_SUZ0198.ogg"
    "铃羽" "「如果不是做的我就收下」"
    call CHECK_RM_RECEIVE
    "说成这么厌恶的样子是因为之前吃的苹果派很难吃。"
    call CHECK_RM_RECEIVE
    "还以为是为了杀了我，实际上也这样说出了口。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0007"
    $ current_voice = "voice/SUZ02A_CRS0007.ogg"
    "红莉栖" "「我就知道你会这么说，所以我特地去便利店买的」"
    call CHECK_RM_RECEIVE
    "牧濑红莉栖虽然有些不乐意但是不像在生气。"
    call CHECK_RM_RECEIVE
    "这件事让我觉得有些不可思议。"

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0199"
    $ current_voice = "voice/SUZ02A_SUZ0199.ogg"
    "铃羽" "「为什么要像我道贺？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0008"
    $ current_voice = "voice/SUZ02A_CRS0008.ogg"
    "红莉栖" "「你在找父亲，然后顺利地找到了。以上，证明完毕」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0200"
    $ current_voice = "voice/SUZ02A_SUZ0200.ogg"
    "铃羽" "「但是我对你只有敌对态度」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0009"
    $ current_voice = "voice/SUZ02A_CRS0009.ogg"
    "红莉栖" "「是呢。但我没法和我的父亲相处的很好呢」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0010"
    $ current_voice = "voice/SUZ02A_CRS0010.ogg"
    "红莉栖" "「听说你见到了父亲，我有些高兴」"
    play bgm "FDBGM03"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0201"
    $ current_voice = "voice/SUZ02A_SUZ0201.ogg"
    "铃羽" "「牧濑红莉栖的父亲……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0011"
    $ current_voice = "voice/SUZ02A_CRS0011.ogg"
    "红莉栖" "「所以正确来说这不是祝贺。只是分享喜悦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0012"
    $ current_voice = "voice/SUZ02A_CRS0012.ogg"
    "红莉栖" "「如果能让你对我的态度软化，就帮了大忙了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0202"
    $ current_voice = "voice/SUZ02A_SUZ0202.ogg"
    "铃羽" "「如果是这样的话我就收下了」"
    "我接受了牧濑红莉栖的蛋糕。"
    "这时我已经没有在死盯着她了。"
    "回过神来时露出了笑容。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0203"
    $ current_voice = "voice/SUZ02A_SUZ0203.ogg"
    "铃羽" "「你也能跟父亲关系改善就好了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0013"
    $ current_voice = "voice/SUZ02A_CRS0013.ogg"
    "红莉栖" "「是呢」"
    "然后我再次考虑为什么她会拿着便利店袋子。"
    "应该不止是为了买我的蛋糕而去的。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0204"
    $ current_voice = "voice/SUZ02A_SUZ0204.ogg"
    "铃羽" "「今天住在实验室吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0014"
    $ current_voice = "voice/SUZ02A_CRS0014.ogg"
    "红莉栖" "「我想把刚刚做好的装置送到能用上的地方」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0205"
    $ current_voice = "voice/SUZ02A_SUZ0205.ogg"
    "铃羽" "「那，如果我不打扰你的话，能不能让我也住在实验室？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "听到我的请求，牧濑红莉栖用奇怪的表情看着我。"
    "这也没什么奇怪。我也没想到自己会说出这样的话。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0015"
    $ current_voice = "voice/SUZ02A_CRS0015.ogg"
    "红莉栖" "「……嘛，可以啊」"
    "但是牧濑红莉栖没有拒绝，也没有推辞。"
    "老实说我不知道这是为什么，但是我觉得肯定是因为父亲的关系。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_OKA01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_OKA01_01"])

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG02N2",trans=fade)

    play bgm "FD2BGM05"
    show screen phonebtn
    show screen phoneSD1
    "这一晚从牧濑红莉栖那里听到，她对于时间机器还真是怀着一种矛盾的感情。"
    "刚来实验室时她似乎很敌视时间机器。"
    "但是现在，她正在完成人类史上第一台时间机器。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0016"
    $ current_voice = "voice/SUZ02A_CRS0016.ogg"
    "红莉栖" "「我的父亲，在研究时间机器」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0017"
    $ current_voice = "voice/SUZ02A_CRS0017.ogg"
    "红莉栖" "「但就因为这样，父亲被学会开除了」"
    "牧濑红莉栖一边灵巧地工作着一边自言自语。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0206"
    $ current_voice = "voice/SUZ02A_SUZ0206.ogg"
    "铃羽" "「在这个时代，时间机器还是幻想中的吧」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0018"
    $ current_voice = "voice/SUZ02A_CRS0018.ogg"
    "红莉栖" "「正规学者不会在学会中说这种话」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0207"
    $ current_voice = "voice/SUZ02A_SUZ0207.ogg"
    "铃羽" "「你的父亲不是正规的学者吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0019"
    $ current_voice = "voice/SUZ02A_CRS0019.ogg"
    "红莉栖" "「我小时候时是个正规的学者」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC06"),"True","lh/CRS_BMC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑红莉栖停下手来，我感觉好像说了什么不该说的事情。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0020"
    $ current_voice = "voice/SUZ02A_CRS0020.ogg"
    "红莉栖" "「是我让他成了不正规的学者」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0208"
    $ current_voice = "voice/SUZ02A_SUZ0208.ogg"
    "铃羽" "「这是怎么回事？」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0021"
    $ current_voice = "voice/SUZ02A_CRS0021.ogg"
    "红莉栖" "「我很喜欢父亲说的学术相关的话题。当然当时的我并不能全部理解。所以我为了听到更多父亲的话而学习」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0022"
    $ current_voice = "voice/SUZ02A_CRS0022.ogg"
    "红莉栖" "「我相信如果能弄懂他的话，他一定会跟我说更多的。但结果却完全相反」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0023"
    $ current_voice = "voice/SUZ02A_CRS0023.ogg"
    "红莉栖" "「我不仅能理解父亲的话，连父亲说错的地方也能发现了。然后我就指出了他的错误。我相信学术就是这样的东西。」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0024"
    $ current_voice = "voice/SUZ02A_CRS0024.ogg"
    "红莉栖" "「但是这伤到了父亲的自尊。这是肯定的。就算是学者也是普通人。被还在读小学的女儿指责……肯定会觉得丢脸」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0025"
    $ current_voice = "voice/SUZ02A_CRS0025.ogg"
    "红莉栖" "「我并没有发现这点，一直持续这样的情况。结果，父亲他变成无法进行与其他人竞争的正当研究，只能逃向谁都没办法反驳的领域。」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0209"
    $ current_voice = "voice/SUZ02A_SUZ0209.ogg"
    "铃羽" "「那就是关于时间机器的研究」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0026"
    $ current_voice = "voice/SUZ02A_CRS0026.ogg"
    "红莉栖" "「所以我认为时间机器的研究绝对不能进行。是不能进行的研究。但是这不是时间机器的错，只是为了从自己的罪恶感中逃脱」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0210"
    $ current_voice = "voice/SUZ02A_SUZ0210.ogg"
    "铃羽" "「牧濑红莉栖很像父亲呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC04"),"True","lh/CRS_BMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我的话让牧濑红莉栖狠狠地盯着我。"
    "我好像又说了多余的话。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0027"
    $ current_voice = "voice/SUZ02A_CRS0027.ogg"
    "红莉栖" "「像父亲？哪里？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0211"
    $ current_voice = "voice/SUZ02A_SUZ0211.ogg"
    "铃羽" "「虽然我没有见过你的父亲，但是能感到你们两都是认真又天真的人。天真是不是贬义词？不是说你们神经质，而是说你们很纤细」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC05"),"True","lh/CRS_BMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0028"
    $ current_voice = "voice/SUZ02A_CRS0028.ogg"
    "红莉栖" "「……也许是这样」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0212"
    $ current_voice = "voice/SUZ02A_SUZ0212.ogg"
    "铃羽" "「此外，先不论理由，还是对时间机器产生了兴趣。你们肯定认为穿越时空是浪漫的吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB06"),"True","lh/CRS_BMB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0029"
    $ current_voice = "voice/SUZ02A_CRS0029.ogg"
    "红莉栖" "「科学家也可以很浪漫嘛」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0213"
    $ current_voice = "voice/SUZ02A_SUZ0213.ogg"
    "铃羽" "「我认为科学家是非常浪漫的人。将谁都不知道的真理当成目标，这除了浪漫之外就没有什么了吧」"
    "未来的父亲……将时间机器交给我的父亲也很浪漫。我这样认为。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0030"
    $ current_voice = "voice/SUZ02A_CRS0030.ogg"
    "红莉栖" "「……这倒……也是」"
    "牧濑红莉栖稍微冷静了一些。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "证据就是她再度开始了工作。"
    "那让我觉得她一定是和她的父亲很像的吧。"
    "正直的行为会伤到周围的人。"
    "这也许并不是什么好事，但这也是她无法改变的性格吧。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0214"
    $ current_voice = "voice/SUZ02A_SUZ0214.ogg"
    "铃羽" "「就算如此牧濑红莉栖的父亲也还是选择研究时间机器吧」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0031"
    $ current_voice = "voice/SUZ02A_CRS0031.ogg"
    "红莉栖" "「你有意见吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0215"
    $ current_voice = "voice/SUZ02A_SUZ0215.ogg"
    "铃羽" "「没有。不如说正好相反。我对你有亲近感」"
    "这不是说谎。"
    "父亲没头研究时间机器，离开女儿。"
    "这是我的故事。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0032"
    $ current_voice = "voice/SUZ02A_CRS0032.ogg"
    "红莉栖" "「亲近感啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0216"
    $ current_voice = "voice/SUZ02A_SUZ0216.ogg"
    "铃羽" "「没错，亲近感」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0217"
    $ current_voice = "voice/SUZ02A_SUZ0217.ogg"
    "铃羽" "「我跟你都过着被时间机器囚禁的人生。我跟你令人意外地挺相像。」"
    "对于到目前为止被我当成敌人的牧濑红莉栖来说，这是我能说出的最大的赞美。"
    "但是牧濑红莉栖却露骨地露出讨厌的表情。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0033"
    $ current_voice = "voice/SUZ02A_CRS0033.ogg"
    "红莉栖" "「……该不会吧，应该就是这样，因为我跟你是母女关系？所以关系才不好」"
    "但是这个理由是我没想过的。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0218"
    $ current_voice = "voice/SUZ02A_SUZ0218.ogg"
    "铃羽" "「不是这样。我的母亲不是你。母亲的名字叫阿万音」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0034"
    $ current_voice = "voice/SUZ02A_CRS0034.ogg"
    "红莉栖" "「是吗……那就好」"
    "牧濑红莉栖的脸上露出打从心底里放心的表情。"
    "不是我的母亲这点让她这么高兴吗？感觉她好像说了非常失礼的事情。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0219"
    $ current_voice = "voice/SUZ02A_SUZ0219.ogg"
    "铃羽" "「说到母亲」"
    "因此我对牧濑红莉栖的敌意又苏醒了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0220"
    $ current_voice = "voice/SUZ02A_SUZ0220.ogg"
    "铃羽" "「你在我所在的未来被称为「时间机器之母」」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0035"
    $ current_voice = "voice/SUZ02A_CRS0035.ogg"
    "红莉栖" "「我是「时间机器之母」。听起来挺妥当的。这台机器完成了的话，就是世界上第一台时间机器」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0221"
    $ current_voice = "voice/SUZ02A_SUZ0221.ogg"
    "铃羽" "「如果只是这样就好了。但你跟冈部伦太郎制作的时间机器的技术被ＳＥＲＮ独占了。结果，世界变成了没有争端的绝望乡」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0222"
    $ current_voice = "voice/SUZ02A_SUZ0222.ogg"
    "铃羽" "「在我所在的未来，是任何争议都被时间机器防范于未然，被完全管理了的世界。造成这一切的原因都是你牧濑红莉栖造成的」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0036"
    $ current_voice = "voice/SUZ02A_CRS0036.ogg"
    "红莉栖" "「原来如此。你是为世界和平而战斗的战士吧，难怪看我的表情总是一副杀了你父母的表情」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0223"
    $ current_voice = "voice/SUZ02A_SUZ0223.ogg"
    "铃羽" "「想不到你这么冷静」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0037"
    $ current_voice = "voice/SUZ02A_CRS0037.ogg"
    "红莉栖" "「我在意的只是为什么我会被你恨」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0038"
    $ current_voice = "voice/SUZ02A_CRS0038.ogg"
    "红莉栖" "「但是如果理由是跟未来相关的话就没有办法了」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0039"
    $ current_voice = "voice/SUZ02A_CRS0039.ogg"
    "红莉栖" "「对你来说是过去的事情，但是对我来说是还没有发生的未来吧？」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0040"
    $ current_voice = "voice/SUZ02A_CRS0040.ogg"
    "红莉栖" "「但是也是事实吧。实际上我就像现在这样制作时间机器的话，完成了就有被称为时间机器之母的资格了」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0041"
    $ current_voice = "voice/SUZ02A_CRS0041.ogg"
    "红莉栖" "「ＳＥＲＮ现在对我来说还没有任何意义，但是是我知道他们正在进行人体试验。如果他们知道我们先完成的话，立刻就来夺取也不奇怪」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0224"
    $ current_voice = "voice/SUZ02A_SUZ0224.ogg"
    "铃羽" "「如果那样的话你会成为ＳＥＲＮ的爪牙继续研究时间机器？」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0042"
    $ current_voice = "voice/SUZ02A_CRS0042.ogg"
    "红莉栖" "「这件事我也不知道」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB01"),"True","lh/CRS_BMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑红莉栖又停下了手中的活，看着我。"
    "这次她没有死盯着我，反而露出了笑容。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0043"
    $ current_voice = "voice/SUZ02A_CRS0043.ogg"
    "红莉栖" "「如果他们以死相挟的话那我肯定不会帮助ＳＥＲＮ吧」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0044"
    $ current_voice = "voice/SUZ02A_CRS0044.ogg"
    "红莉栖" "「但是在你看到的事实中，我与ＳＥＲＮ合作，制作了能管理全世界的时间机器。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB05"),"True","lh/CRS_BMB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0045"
    $ current_voice = "voice/SUZ02A_CRS0045.ogg"
    "红莉栖" "「这个矛盾究竟是从哪出现的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0225"
    $ current_voice = "voice/SUZ02A_SUZ0225.ogg"
    "铃羽" "「我从来没想过这件事」"
    "我并不知道牧瀬红莉栖这个人的经历。"
    "在未来我与她也没有说过话。"
    "只是将她当成敌人尝试去暗杀，但是失败了。"
    "但是这样与牧濑红莉栖对话后，她的确不是那种为了保全自己性命而去帮助ＳＥＲＮ的人。"
    "那为什么牧濑红莉栖要去帮助ＳＥＲＮ？"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0046"
    $ current_voice = "voice/SUZ02A_CRS0046.ogg"
    "红莉栖" "「桥田变成了抵抗者，制作了你的时间机器吧？那冈部呢？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0226"
    $ current_voice = "voice/SUZ02A_SUZ0226.ogg"
    "铃羽" "「冈部伦太郎是创造反抗组织的人之一」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0047"
    $ current_voice = "voice/SUZ02A_CRS0047.ogg"
    "红莉栖" "「那在未来我站在了实验室的对立面呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0227"
    $ current_voice = "voice/SUZ02A_SUZ0227.ogg"
    "铃羽" "「是呢」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0048"
    $ current_voice = "voice/SUZ02A_CRS0048.ogg"
    "红莉栖" "「冈部和桥田是抵抗者的话，那真由理也是？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0228"
    $ current_voice = "voice/SUZ02A_SUZ0228.ogg"
    "铃羽" "「……我没有听过椎名真由理这个人」"
    "既不是抵抗者也不是ＳＥＲＮ的协力者。"
    "这倒也是。她几天后就会死了。"
    "被ＳＥＲＮ送出的ＲＯＵＮＤＥＲ们杀死了。"
    "这是我来这个时代后知道的事情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB06"),"True","lh/CRS_BMB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0049"
    $ current_voice = "voice/SUZ02A_CRS0049.ogg"
    "红莉栖" "「更加不明白你说的话了。我究竟是为什么要帮助ＳＥＲＮ？而且还跟冈部和桥田对立？为什么会变成这种情况？」"
    "牧濑红莉栖满脸的不解，但是我总觉得自己能明白她选择的道路。"
    "牧濑红莉栖非常想帮椎名真由理。"
    "但是世界线的收束不允许这种事发生。"
    "时间循环不允许椎名真由理得救这种事发生。"
    "救椎名的方法只有一个。"
    "只有改变世界。"
    "不在这条世界线上。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AT_FIELD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AT_FIELD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_AT_FIELD"])
    "{color=#f00}穿越世界线收束范围{/color}，移动到有更多其他可能等着的时间线中。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IBN5100"])
    "要完成这点必须要有时间机器和{color=#f00}ＩＢＮ５１００{/color}这两样东西。"
    "不是只能旅行数日的时间机器，而是需要穿越多年还能回到那个原点的时间机器。"
    "牧濑红莉栖无论如何都要救椎名真由理。"
    "无论如何。"
    "所以选择了与全世界为敌。"
    "牧濑红莉栖比起这个世界，比起自己的信念选择了椎名真由理。"
    "没错，全部都是为了救椎名真由理一个人。"
    "就算离开朋友与伙伴，就算只剩一个人，也要尽自己最大的努力。"
    "也许，牧濑红莉栖，冈部伦太郎，还有父亲……的目的全都是一个也说不定。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0229"
    $ current_voice = "voice/SUZ02A_SUZ0229.ogg"
    "铃羽" "「原来是这样……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0050"
    $ current_voice = "voice/SUZ02A_CRS0050.ogg"
    "红莉栖" "「什么？阿万音小姐明白了什么吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0230"
    $ current_voice = "voice/SUZ02A_SUZ0230.ogg"
    "铃羽" "「……嗯。但是现在，不能由我说出来。」"
    "这不光是因为这是未来的事情，还因为冈部伦太郎还没有跟牧濑红莉栖说过。"
    "椎名真由理死掉这件事，应该由冈部伦太郎说。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0051"
    $ current_voice = "voice/SUZ02A_CRS0051.ogg"
    "红莉栖" "「你这种欲言又止算什么，算了，未来的事不能说也没办法」"
    "牧濑红莉栖爽快地放下了。"
    "单是反过来说，也就是确信了自己不是被ＳＥＲＮ逼迫这件事吧。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0231"
    $ current_voice = "voice/SUZ02A_SUZ0231.ogg"
    "铃羽" "「真厉害啊，牧濑红莉栖」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC04"),"True","lh/CRS_BMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0052"
    $ current_voice = "voice/SUZ02A_CRS0052.ogg"
    "红莉栖" "「干嘛突然说这个」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0232"
    $ current_voice = "voice/SUZ02A_SUZ0232.ogg"
    "铃羽" "「我完全不像你」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0233"
    $ current_voice = "voice/SUZ02A_SUZ0233.ogg"
    "铃羽" "「抱歉啊。擅自将你当成了坏人然后瞪你」"
    "我的决意能不能像她那样坚定呢。"
    "相信着世界会变的更好而做到那种地步。"
    "我为了全世界决定来到过去。"
    "但牧濑红莉栖不同。"
    "为了椎名真由理一个人，与全世界为敌。"
    "结果，我还敌视她，想要暗杀她。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMC01"),"True","lh/CRS_BMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0053"
    $ current_voice = "voice/SUZ02A_CRS0053.ogg"
    "红莉栖" "「算了，虽然让我不太爽，但也不至于要让你道歉」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0234"
    $ current_voice = "voice/SUZ02A_SUZ0234.ogg"
    "铃羽" "「但我还是想道歉」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0054"
    $ current_voice = "voice/SUZ02A_CRS0054.ogg"
    "红莉栖" "「那就请便吧」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0055"
    $ current_voice = "voice/SUZ02A_CRS0055.ogg"
    "红莉栖" "「怎么说呢，虽然不知道你知道了什么，也许只是高看我了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0235"
    $ current_voice = "voice/SUZ02A_SUZ0235.ogg"
    "铃羽" "「这点我不否定」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA05"),"True","lh/CRS_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0056"
    $ current_voice = "voice/SUZ02A_CRS0056.ogg"
    "红莉栖" "「所以才像冈部说的那样，我只是个想做实验的女人也说不定」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0236"
    $ current_voice = "voice/SUZ02A_SUZ0236.ogg"
    "铃羽" "「这点也是」"
    "但是自己的兴趣会夺走重要人的性命的话，牧濑红莉栖绝对会认真地对这件事感到后悔。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0057"
    $ current_voice = "voice/SUZ02A_CRS0057.ogg"
    "红莉栖" "「想不到我会为了制作时间机器而从属ＳＥＲＮ」"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0058"
    $ current_voice = "voice/SUZ02A_CRS0058.ogg"
    "红莉栖" "「无论怎么说研究都需要钱，优秀的部下也是必须的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA02"),"True","lh/CRS_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0059"
    $ current_voice = "voice/SUZ02A_CRS0059.ogg"
    "红莉栖" "「「时间机器之母」听起来很中二啊。也许取这个名字的是冈部也说不定」"
    "这么想着，还坦率地自嘲。"
    "所以我一脸深沉的表情认真地阻止了对话的继续。"
    "只用微笑来回答他的话语。"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0237"
    $ current_voice = "voice/SUZ02A_SUZ0237.ogg"
    "铃羽" "「是呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0238"
    $ current_voice = "voice/SUZ02A_SUZ0238.ogg"
    "铃羽" "「但是我相信会这样想的人。牧濑红莉栖，你是好人」"
    "然后牧濑红莉栖似乎有些害羞，转开了视线。"
    "但是现在看来还真是符合她的形象。"
    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0060"
    $ current_voice = "voice/SUZ02A_CRS0060.ogg"
    "红莉栖" "「擅自敌视别人，接下来又擅自认定别人是好人？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ02A_SUZ0239"
    $ current_voice = "voice/SUZ02A_SUZ0239.ogg"
    "铃羽" "「不行吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMA01"),"True","lh/CRS_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ02A_CRS0061"
    $ current_voice = "voice/SUZ02A_CRS0061.ogg"
    "红莉栖" "「比起不明缘由的被瞪，现在这样好多了」"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "就这样，直到我睡之前都一直在聊些无意义的事。"
    "虽然来这个时代前的我不会相信，但是她和我相处得很愉快。"
    "这可以从与那位牧濑红莉栖进行没有意义的对话中体现出来。"

    hide screen phoneSD1
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    stop bgm 





    return
