label SGFD2_CRS09A:
    window hide


    $ loadBG(0,"IBGX072")

    play bgm "BGM19"

    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0000"
    $ current_voice = "voice/CRS09A_FPP0000.ogg"
    "菲利斯父亲" "「唔，原来如此……」"
    "在那之后，我们３人——我、菲利斯和黑木先生，花了１小时以上的时间给幸高叔叔叙述了事情经过。"
    "但实际上，进行了时间跳跃，知道ＳＥＲＮ、Ｒｏｕｎｄｅｒ和３００人委员会，多次目击真由理死亡的人，只有冈部而已。"
    "按理来说，要进行详细说明及理论检验，他的证言是不可或缺的。"
    "但是冈部，正因重度的精神疲劳而处于精神失常的状态。"
    "这也不能怪他，在毫无希望的情况下受到如此的精神冲击，就算是受过训练的人也很难承受得住吧。"
    "现在我自己，也是靠着常年累积的理性思考习惯，总算是维持住了自己的精神平衡。"
    "就结果而言，我们在冈部不在场的情况下将他的经历表述出来，对各自的误解和认知不足点相互补充，总算是给幸高叔叔进行完了说明。"
    window hide



    $ loadBG(2,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0001"
    $ current_voice = "voice/CRS09A_FPP0001.ogg"
    "菲利斯父亲" "「…………」"
    "然而，叔叔的反应并不激烈。"
    "他绞起了眉毛，视线下移陷入思考。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "……是感到难以置信吧，这也难怪。"
    "就算是我，如果是从冈部以外的人口中听到这么荒谬的事，也不会相信吧……"
    "不，哪怕就连冈部自己，如果没有人以那副走投无路的样子绝望地诉说的话，应该也不可能会相信的。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
    "这才真的是，他会用「厨二病{color=#f00}乙{/color}！」，来做总结的事情。"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0002"
    $ current_voice = "voice/CRS09A_FPP0002.ogg"
    "菲利斯父亲" "「……红莉栖酱。」"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(2,"BG26N",hide=False)



    "沉默忽然被幸高叔叔打破。"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0000"
    $ current_voice = "voice/CRS09A_CRS0000.ogg"
    "红莉栖" "「嗯、嗯。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0003"
    $ current_voice = "voice/CRS09A_FPP0003.ogg"
    "菲利斯父亲" "「刚才我说过，我和你的父亲──章一，是大学时代的朋友，我给他的研究提供资金对吧。」"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0001"
    $ current_voice = "voice/CRS09A_CRS0001.ogg"
    "红莉栖" "「是的。」"
    "不过突然说起的这件事也太突然了，一时间我还没有什么实感。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "幸高叔叔停止出资，就是爸爸作为研究者的生命线被切断之时。"
    "我隐约记得小时候听爸爸提起过这些事。"
    "不过我听到的是爸爸的主观意见，幸高叔叔应该也有他的理由吧。"
    "所以，当时是什么情况暂且不提，现在我对幸高叔叔并不怨恨。"
    "爸爸当时，为了可以专心于研究，带着我和妈妈一起搬回了不用为资金而担心的老家青森。"
    "说到底，那就是失意的表现吧。"
    "当然我明白幸高叔叔也有自己的难处。爸爸也说过，可能是由于经营的公司资金周转出现了困难，才没有余裕提供资金了吧。"
    "所以，我又怎么会责怪幸高叔叔呢。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(2,"BG26N",hide=False)





    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0004"
    $ current_voice = "voice/CRS09A_FPP0004.ogg"
    "菲利斯父亲" "「那么，“相对性理论超越委员会”的研究内容是什么，你知道吗？」"
    "幸高叔叔的声音……听起来那么的不可思议。"
    "声音之中，悲伤、焦虑和怀念的感情仿佛交织在了一起。"
    "对于他的发问，我不由得有些紧张起来。"
    "那时……由幸高叔叔出资，爸爸进行研究的内容，我并没有问过。"
    "但是，说到爸爸的研究……只有一个无误。"
    "就算没有问过，也能一下子猜出来。"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0002"
    $ current_voice = "voice/CRS09A_CRS0002.ogg"
    "红莉栖" "「……是的，我知道。」"
    "那是，我不想承认的爸爸的身影。"
    "……但是。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0005"
    $ current_voice = "voice/CRS09A_FPP0005.ogg"
    "菲利斯父亲" "「我与章一，还有指导我们的教授……定期见面召开秘密会议。——都是为了制造出某样东西。」"
    "只是，对爸爸和幸高叔叔来说，那恐怕是非常令人怀念而又宝贵的，青春的回忆。"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0006"
    $ current_voice = "voice/CRS09A_FPP0006.ogg"
    "菲利斯父亲" "「对，我们想做的那样东西，和你们一样——」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0007"
    $ current_voice = "voice/CRS09A_FPP0007.ogg"
    "菲利斯父亲" "「时间机器。」"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0003"
    $ current_voice = "voice/CRS09A_CRS0003.ogg"
    "红莉栖" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSA03"),"True","lh/FEI_BSA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS09A_FEI0000"
    $ current_voice = "voice/CRS09A_FEI0000.ogg"
    "菲利斯" "「真，真的？　好厉害……像小孩子一样。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0008"
    $ current_voice = "voice/CRS09A_FPP0008.ogg"
    "菲利斯父亲" "「哈哈哈，至少应该说这是浪漫啊。」"
    window hide


    $ loadBG(2,"IBG041A")



    hide screen phonebtn
    "幸高叔叔向我简要说明了相对性理论超越委员会的情况。"
    "爸爸和幸高叔叔的师父是一个教授。从最开始，研究时间机器的就是那个人。"
    "一切的契机，是爸爸偷看了教授的研究笔记。"
    "爸爸和幸高叔叔，被时间机器这一梦想吸引，说服了起初不情愿的教授，最终结成了一个以制造时间机器为目的的小组。"
    "这就是爸爸所命名的，相对性理论超越委员会。"
    "那位教授虽然有想法和灵感，但缺乏能将之实现的操作技术，实际从事研究开发工作的大概是爸爸。"
    "也就是说，有想法的教授，提供资金的幸高叔叔，以及实际进行开发研究的爸爸，三人的组合。"
    "他们的研究活动，与未来道具研究所——也就是，以冈部为中心，我们所进行的活动很相似。"
    "提出方案的冈部，将之组织成一套理论的我，加上进行实际操作的桥田。"
    "那么说来，爸爸同时担当了我和桥田两方的任务。"
    "幸高叔叔听了时间跳跃机的情况，当然也注意到了这点吧。所以，叔叔的声音中饱含着复杂的感情。"
    "自己的小组没有做出来的东西，被下一代人成功实现。此时他心中的是自豪之情吗？还是嫉妒呢？"
    window hide



    $ loadBG(2,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC01"),"True","lh/FEI_BSC01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    "他的具体想法我无从得知。不过，那大概是很不寻常的……至少能说是非常复杂、百感交集的思绪吧。"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0009"
    $ current_voice = "voice/CRS09A_FPP0009.ogg"
    "菲利斯父亲" "「因为想要制作的东西是同一个，所以我能明白……不，不对。应该说我早就明白了。」"
    "幸高叔叔少有地出现了咬牙切齿的语气。"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0004"
    $ current_voice = "voice/CRS09A_CRS0004.ogg"
    "红莉栖" "「是什么意思呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0010"
    $ current_voice = "voice/CRS09A_FPP0010.ogg"
    "菲利斯父亲" "「嗯……大概，你们所说的ＳＥＲＮ和３００人委员会我是知道的。而且是从两个方面所得知。」"
    "这一回，轮到我对幸高叔叔的话皱起了眉毛。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS09A_FEI0001"
    $ current_voice = "voice/CRS09A_FEI0001.ogg"
    "菲利斯" "「两个方面……爸爸，怎么回事？」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0011"
    $ current_voice = "voice/CRS09A_FPP0011.ogg"
    "菲利斯父亲" "「一方面，与其说是我知道，更准确地说是我们的恩师知道。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0012"
    $ current_voice = "voice/CRS09A_FPP0012.ogg"
    "菲利斯父亲" "「教授对时间机器的研究，一直当作非常机密的事项。为了防止谁走露了风声，协力者的数量也控制在最小范围内。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0013"
    $ current_voice = "voice/CRS09A_FPP0013.ogg"
    "菲利斯父亲" "「虽然章一马上就赞同了这个方针，但我还是希望找到共同出资者，而有点为难的时候呢……」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0014"
    $ current_voice = "voice/CRS09A_FPP0014.ogg"
    "菲利斯父亲" "「不过，现在回想起来，教授对ＳＥＲＮ是有一定了解的吧。」"
    "总之，从现在的情况来看，他们当时的方针的确有先见之明。"
    "不过也有冈部这样进行研究的方式，这种情况是很难判断的吧。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0005"
    $ current_voice = "voice/CRS09A_CRS0005.ogg"
    "红莉栖" "「那么，另一方面是指什么呢？」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0015"
    $ current_voice = "voice/CRS09A_FPP0015.ogg"
    "菲利斯父亲" "「３００人委员会……准确地说，我并不知道这个组织。」"
    "对于幸高叔叔说的这句话，我实在是不能点点头就说我懂了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "看见我满脸写满了疑问，叔叔轻轻地笑了笑就继续说了下去。"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0016"
    $ current_voice = "voice/CRS09A_FPP0016.ogg"
    "菲利斯父亲" "「红莉栖酱，在你看来，秘密结社这种东西，是不是离现实很遥远，像是夸张架空出来的？」"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0006"
    $ current_voice = "voice/CRS09A_CRS0006.ogg"
    "红莉栖" "「诶？」"
    "这个唐突的发问，我一时没反应过来。"
    "我会有这种反应，似乎也在叔叔的预料之内。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0017"
    $ current_voice = "voice/CRS09A_FPP0017.ogg"
    "菲利斯父亲" "「事实上，秘密结社这种东西到处都是，并不是什么罕见的事物……特别是对我这样的企业家而言呢。」"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0007"
    $ current_voice = "voice/CRS09A_CRS0007.ogg"
    "红莉栖" "「…………」"
    "──我们，到底是在和谁战斗啊。"
    "听着叔叔的话，脑中不由地闪过了＠ｃｈ上的梗。"
    "现在我的表情应该是僵住了吧。观察着我的心理活动，幸高叔叔像是咬着牙般继续说了下去。"
    "要解释的话，其实是这样的。"
    window hide


    $ loadBG(2,"IBG042A")



    hide screen phonebtn
    "以前，在产业革命以前。情报的传达、流通和公开，花费的成本要远远高于现在。"
    "再加上，社会的进步日新月异，新的商机不断出现，商人们发现以前的一贯做法已经行不通了。"
    "最大的变化是，现在的经济发展走向，已经与大航海时代前夕对银行的依赖程度高得史无前例的经济完全不同了。"
    "如果再和从前一样的狭小范围、狭小领域、狭小价值观内就能进行商业买卖的话自然再好不过。但已经不能那样了。"
    "于是面对着这种情况，从事商业的人们为了保护自身的利益，开始摸索互相合作的组织构架。"
    "这与国家机关之类不同，是不对外开放门户的封闭组织。"
    "因为组织的活动和存在是极度保密的，很多情况下其成员和团体的活动也受到保护。这样的组织，就成了秘密结社。"
    "当然，除了这样的经济型秘密结社以外还有其它秘密结社。"
    "比如意大利亚·西西里岛上有名的黑手党，是由岛民们抵抗大国横暴的抵抗组织发展而来的。"
    "还有，阴谋论中有名的圣殿骑士团，其实并非秘密结社。"
    "由于法国主导把它定义为异端，人们对它才有了秘密结社的印象，但它在法国以外的国家继续普通地存在着。"
    "特别是在葡萄牙，国王本身就是圣殿骑士团的一员，国家与骑士团一体化了。"
    "也就是说，现在的葡萄牙，就是圣殿骑士团本身。这种例子不能称为秘密结社。"
    "还有，在我出生前就解体的苏维埃联盟，原本也是以秘密结社为基础，发起了革命，最后演化为国家的姿态。"
    window hide



    $ loadBG(2,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0018"
    $ current_voice = "voice/CRS09A_FPP0018.ogg"
    "菲利斯父亲" "「还有很多你们所不知道的秘密结社，在推动的世界。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0019"
    $ current_voice = "voice/CRS09A_FPP0019.ogg"
    "菲利斯父亲" "「但这并不是多么特别的事情，更该说是理所当然的。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0020"
    $ current_voice = "voice/CRS09A_FPP0020.ogg"
    "菲利斯父亲" "「不知道你们能不能理解，就连你们的Ｌａｂ ， 在某种意义上也是秘密结社。首先要认识到这一点。」"
    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0008"
    $ current_voice = "voice/CRS09A_CRS0008.ogg"
    "红莉栖" "「…………」"
    "被这么一说，我有些不知所措。"
    "在我看来，秘密结社是阴谋论里的常客，是从胡说八道的厨二病理论中诞生出的妄想。"
    "事实却是，据说在秘密结社之中，有很多组织能左右一个发达国家的国策。——它们之中也有竞选和投票。"
    "当然，以组织成员利益为首要目标的利润型秘密结社也有很多。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0021"
    $ current_voice = "voice/CRS09A_FPP0021.ogg"
    "菲利斯父亲" "「这个叫３００人委员会的结社，从名字上看不知道是什么等级的组织。但可以确定的是，它是相当不得了的。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0022"
    $ current_voice = "voice/CRS09A_FPP0022.ogg"
    "菲利斯父亲" "「在我从商的角度来看，这不是一个能够挑衅的对手。对方的目的、规模、势力范围，全都还不清楚。」"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0023"
    $ current_voice = "voice/CRS09A_FPP0023.ogg"
    "菲利斯父亲" "「不知道对方的想法才是最大的难点啊。比较好的情况，是摸索着互相间的利益落脚点，与对方达成和解。而现在也不知道这个是否能行得通。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC04"),"True","lh/FEI_BSC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS09A_FEI0002"
    $ current_voice = "voice/CRS09A_FEI0002.ogg"
    "菲利斯" "「……爸爸？」"
    "菲利斯有些不安地向幸高叔叔表示疑问。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "叔叔嘴角向上一扬，轻轻地笑了。"
    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0024"
    $ current_voice = "voice/CRS09A_FPP0024.ogg"
    "菲利斯父亲" "「不过呢，我可不允许那帮家伙在我们的秋叶原里肆意妄为下去……多少要给他们一点教训。」"
    "这时我总算明白了。"
    "幸高叔叔的愤怒是怎样的感情。"
    window hide
    play se "SGSE302L" loop


    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0025"
    $ current_voice = "voice/CRS09A_FPP0025.ogg"
    "菲利斯父亲" "「啊呀，不好意思……」"
    window hide
    hide lh5  with dissolve

    play se "SGSE158"

    stop se
    "接起忽然响起的电话，幸高叔叔不经意地嘴角微微上扬。"
    "然后，他挂掉了电话说道。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS09A_FPP0026"
    $ current_voice = "voice/CRS09A_FPP0026.ogg"
    "菲利斯父亲" "「似乎是有线索了。抓到了一个你们所说的Ｒｏｕｎｄｅｒ的家伙。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC02"),"True","lh/FEI_BSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "CRS09A_CRS0009"
    $ current_voice = "voice/CRS09A_CRS0009.ogg"
    "红莉栖" "「抓，抓到了……？」"
    "冈部说过，Ｒｏｕｎｄｅｒ杀了真由理。"
    "说是，抓住了一个那样杀人不眨眼的恐怖的家伙……"
    "幸高叔叔，到底是什么人呢。越来越没有实感了。"
    "说不定，我现在认知的这个瞬间，是真的在做梦吧。"
    "……不，这种逃避现实的想法还是打住吧。"
    "此时此刻，即使是像漫画一样的情节也无所谓了。幸高叔叔的话对我而言，是黑暗中目之所及的唯一光明。"

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
