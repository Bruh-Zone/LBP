label SGFD2_CRS10A:
    window hide


    $ loadBG(0,"BG27N")




    play bgm "BGM23"


    $ date="8/13"
    hide screen phonebtn
    show screen phoneSD1

    "根据幸高叔叔的叙述，事情是这样的。"
    "受到幸高叔叔的协力委托，“总管”们正推敲对策的时候，一个被五花大绑的男人突然倒在了他们所在的居酒屋前面。"
    "那个男人看起来已经吃了相当的苦头，没剩下多少胆量了。"
    "刚一审问，那个男人就把自己身为Ｒｏｕｎｄｅｒ的事实统统倒了出来。"
    "把那男人带来的是一名“梳着双马尾的女性”，居酒屋的店员说，她把男人丢到店门口之后，没有留名就骑着自行车离开了。"
    "那名女性是什么人尚不清楚。"
    "不过，以意想不到的形式得到了Ｒｏｕｎｄｅｒ的情报。"
    "这简直就像是那名女性送来的礼物一样，但也有是个圈套的可能性。"
    "从那男人那里得到的消息是，Ｒｏｕｎｄｅｒ以复数独立的小队分头行动，并不清楚互相之间的情况。"
    "似乎有一个名为ＦＢ的人物进行指挥，但是这个被抓的Ｒｏｕｎｄｅｒ，是受ＦＢ手下的其他人所指挥的。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IBN5100"])
    "他们原本的目的，是寻找名为{color=#f00}ＩＢＮ５１００{/color}的老式电脑。"
    "但是在昨天，法国派遣了即使是在Ｒｏｕｎｄｅｒ中也很特别的特殊部队进入日本。"
    "那群人的目标是袭击未来道具研究所，以及控制时间跳跃机和其开发者。"
    "这名被抓的Ｒｏｕｎｄｅｒ则负责对各处街道进行监视，防止开发者——冈部等人逃离秋叶原。"
    "然而可惜的是，真由理和桥田已经被Ｒｏｕｎｄｅｒ抓住并带到了某处。至于被带到了哪里，那个男人也并不知情。"
    window hide


    $ loadBG(0,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC05"),"True","lh/FEI_BSC05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0000"
    $ current_voice = "voice/CRS10A_FPP0000.ogg"
    "菲利斯父亲" "「你们制造的时间机器——时间跳跃机……他们计划出动别动队将其回收。」"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0001"
    $ current_voice = "voice/CRS10A_FPP0001.ogg"
    "菲利斯父亲" "「不过，我在警备公司有熟人，让他们对大桧山大楼进行戒备，说不定能观察到些情况。」"
    "……这样看来，转移到菲利斯家是正确的选择。"
    "如果就那样留在Ｌａｂ，现在说不定已经和前来回收时间跳跃机的Ｒｏｕｎｄｅｒ撞个正着了。"
    "想象着这种情况，我不禁全身发寒。"
    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0000"
    $ current_voice = "voice/CRS10A_FEI0000.ogg"
    "菲利斯" "「真由理和桶子喵……到底被带到什么地方去了……」"
    "听了幸高叔叔的话，菲利斯的泪水在眼中打转。"
    "重要的朋友正面临危险，她也感到坐立难安吧。"
    "但也不知该如何是好。就是这种感受吧。"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0000"
    $ current_voice = "voice/CRS10A_CRS0000.ogg"
    "红莉栖" "「如果，能抓到那个叫ＦＢ的Ｒｏｕｎｄｅｒ……」"
    "不由自主地说了出来，明明知道这是很困难的事啊。毕竟线索太少了。"
    "说到底，那个ＦＢ在不在日本国内都不能确定。"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0001"
    $ current_voice = "voice/CRS10A_CRS0001.ogg"
    "红莉栖" "「这种时候要是桥田在的话……」"
    hide screen phoneSD1
    window hide



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(0,"BG03A4",trans=Fade(0.5,0.5,0.5,color="fff"))


    hide screen phonebtn
    "我也知道这是很死乞白赖的想法，但如果桥田在这，他精湛的黑客技术说不定就能开出一条道路了。"
    "进行入侵时最重要的，并不是单纯地用电脑网络去搜索终端或情报源。"
    "而是看透对方设置的防火墙和密码，然后针对对方的心理将计就计，找出超越对方预想的道路。"
    "在这个层面上，哪怕已经四面楚歌，桥田也能另辟蹊径，展开Ｒｏｕｎｄｅｒ预测以外的行动。"
    "但桥田并不在这里。要找到桥田，就必须要有他自身的能力，这种情况也真是讽刺啊。"
    "在时间跳跃机的开发中，他作出的贡献很大。在另一层意义上，他也和冈部一样，是Ｌａｂ不可或缺的重要人物。"
    window hide


    $ loadBG(0,"BG26N",trans=Fade(0.5,0.5,0.5,color="fff"))

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC05"),"True","lh/FEI_BSC05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    "思来想去，也没有什么好主意了。"
    "这时，幸高叔叔再次拿起了电话。"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0002"
    $ current_voice = "voice/CRS10A_FPP0002.ogg"
    "菲利斯父亲" "「看来，这回的事态可不是我们能够解决的了。」"
    "这句话像是要放弃了。可是，幸高叔叔的表情却没有要放弃的意思。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC04"),"True","lh/FEI_BSC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0001"
    $ current_voice = "voice/CRS10A_FEI0001.ogg"
    "菲利斯" "「爸爸，要怎么办？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0003"
    $ current_voice = "voice/CRS10A_FPP0003.ogg"
    "菲利斯父亲" "「正好，也再教留未穗一次吧。当自己感到束手无策的时候，去借助可信之人的力量乃是商务的铁则。」"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0004"
    $ current_voice = "voice/CRS10A_FPP0004.ogg"
    "菲利斯父亲" "「正如刚刚的我，借助了“总管”的力量。」"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0005"
    $ current_voice = "voice/CRS10A_FPP0005.ogg"
    "菲利斯父亲" "「人类并不能只靠一个人活下去。一个人所在的地方，有他身边的人，有社会，有历史。」"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0006"
    $ current_voice = "voice/CRS10A_FPP0006.ogg"
    "菲利斯父亲" "「那个人从过去积累下来的经验，他周围的人，生长的环境，全部加在一起，才成了这个人。」"
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0007"
    $ current_voice = "voice/CRS10A_FPP0007.ogg"
    "菲利斯父亲" "「有给我指明道路的教授，有章一，有留未穗，有这个秋叶原的街道，所在才有现在在这里的我。」"
    "同时，ＳＥＲＮ和３００人委员会也是一样的。幸高叔叔说道。"
    window hide


    $ loadBG(2,"IBG043A")



    hide screen phonebtn
    "无论他们拥有多大的权利，都不可能与其他人毫无关系。"
    "其中的一些成员必定会有家人，有国家和土地，也有人际关系的框架。"
    "即使是座拥强大军事力量的美国，也不可能在当今的国际社会中任由一已之见而随意行动。"
    "历史上曾存在过的许多独裁国家都是如此。即使是暴君，也不可能１００％地在任何情况下都任性到底。"
    "这之中就有隙可乘了。"
    "如果说３００人委员会是欧洲系的组织，考虑到印度系和中东系的秘密结社在的世界范围内也有很多。"
    "在日本、中国和亚洲其他国家也有能给国际社会造成影响的组织和企业。"
    "如果其中的某个组织因某个契机而产生行动……"
    "即使不能让ＳＥＲＮ和３００人委员会撤销计划或改变行动方针，也可能使其活动受到限制，或进行细微调整。"
    window hide



    $ loadBG(2,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC04"),"True","lh/FEI_BSC04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("FPP")
    play FPP "CRS10A_FPP0008"
    $ current_voice = "voice/CRS10A_FPP0008.ogg"
    "菲利斯父亲" "「当然，最后的结果也可能达不到我们的期望。但就算是这样，也比什么都不做干等着强。」"
    window hide
    hide lh5  with dissolve
    "这么说着，幸高叔叔开始给不同的人打电话。"
    "用的几乎都是英语，有时还是连我都听不懂的语言。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("Y13")
    play KUR "CRS10A_Y130000"
    $ current_voice = "voice/CRS10A_Y130000.ogg"
    "黒木" "「大小姐，牧濑。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我们眼睛都不敢眨，紧盯着正在打电话的幸高叔叔时，黑木先生忽然搭话了。"
    $ stopvoc("Y13")
    play KUR "CRS10A_Y130001"
    $ current_voice = "voice/CRS10A_Y130001.ogg"
    "黒木" "「你们在这里坐着也只是白白浪费体力。趁着现在，稍微休息一会吧。」"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0002"
    $ current_voice = "voice/CRS10A_CRS0002.ogg"
    "红莉栖" "「可是……」"
    "我理解黑木先生的意思。如果幸高叔叔以自己的人脉展开了行动，那现在我们就帮不上什么忙了。"
    "但即使是这样，现在这种状况，也没有去休息的心情。"
    window hide
    hide lh6  with dissolve



    $ loadBG(2,"BG26N")





    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC01"),"True","lh/FEI_BMC01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0002"
    $ current_voice = "voice/CRS10A_FEI0002.ogg"
    "菲利斯" "「红喵，黑木说得对。稍微休息一下吧。」"
    "菲利斯挽着我的手劝道。"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0003"
    $ current_voice = "voice/CRS10A_CRS0003.ogg"
    "红莉栖" "「但是！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC04"),"True","lh/FEI_BMC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0003"
    $ current_voice = "voice/CRS10A_FEI0003.ogg"
    "菲利斯" "「红喵，你知道吗？现在你的脸色有多差……就跟凶真一样，必须去休息了。」"
    "诶……？ 脸色？"
    "我自己没有注意，但从菲利斯的话来看，我现在应该是张相当疲惫的脸。"
    "这么一说我似乎已经一整晚没睡了，而且晚饭也没有吃。"
    "再加上现在正是盛夏。情况接连不断地发生，确实已经很疲劳了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0004"
    $ current_voice = "voice/CRS10A_FEI0004.ogg"
    "菲利斯" "「凶真和真由氏，还有桶子喵的情况都那么糟糕，如果红喵再出点什么事，那就真的无力回天了。就当是为了凶真，红喵必须得精神起来啊。」"
    "被她这么一说，我终于注意到了自己的不冷静。"
    "菲利斯说得对，就算我倒下了，对冈部和真由理也没有任何帮助。"
    "心中虽有犹豫，迷茫，焦虑，但在这之上，我是一个十分重理性的研究者。"
    "那么，就应该服从自己的信条。"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0004"
    $ current_voice = "voice/CRS10A_CRS0004.ogg"
    "红莉栖" "「……我明白了。菲利斯，黑木先生，谢谢你们。我休息一下。」"
    $ stopvoc("Y13")
    play KUR "CRS10A_Y130002"
    $ current_voice = "voice/CRS10A_Y130002.ogg"
    "黒木" "「在冈部先生的隔壁准备了寝室。我来带路，这边请。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA01"),"True","lh/FEI_BMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS10A_FEI0005"
    $ current_voice = "voice/CRS10A_FEI0005.ogg"
    "菲利斯" "「如果有什么情况我马上通知你，安心休息吧，红喵。」"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0005"
    $ current_voice = "voice/CRS10A_CRS0005.ogg"
    "红莉栖" "「嗯，拜托了。」"
    window hide

    stop bgm 
    window hide


    $ loadBG(2,"BG26N")



    "我道过别，跟着黑木先生走向寝室──"
    $ stopvoc("CRS")
    play CRS "CRS10A_CRS0006"
    $ current_voice = "voice/CRS10A_CRS0006.ogg"
    "红莉栖" "「……红喵？」"
    "好像，被叫了奇怪的名字……是我……听错了吧？"

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
