label SGFD2_CRS11A:
    window hide


    $ loadBG(0,"BG_BLACK")

    play bgm "FD2BGM04"

    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0000"
    $ current_voice = "voice/CRS11A_CRS0000.ogg"
    "红莉栖" "「…………」"
    "睡不着。"
    "无论身还是心都已疲惫不堪，偏偏意识却无比清醒……怎么都睡不着。"
    "在床上翻来覆去，试着调整各种睡姿和呼吸方式让自己入睡，但睡意就是迟迟不肯到访。"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)









    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0001"
    $ current_voice = "voice/CRS11A_CRS0001.ogg"
    "红莉栖" "「真由理……桥田……」"



    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)









    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0002"
    $ current_voice = "voice/CRS11A_CRS0002.ogg"
    "红莉栖" "「冈部……」"


    "就算什么也不做，涌上心头的也尽是那些糟糕的事情。"
    window hide


    $ loadBG(3,"BG_CHI",trans=ImageDissolve(im.Scale("mask/mask10.png",1024,576),0.5))

    $ loadBG(0,"BG_BLACK")










    "脑海中不知多少次冒出最坏的情况，因此我一直全身僵硬地摇着头发抖。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0003"
    $ current_voice = "voice/CRS11A_CRS0003.ogg"
    "红莉栖" "「…………」"
    "束手无策，唯有叹息。"
    "想救朋友，却有心无力。"
    "为了能在幸高叔叔帮我们找到什么线索的时候及时把握，此刻最重要的是尽可能多地回复体力。"
    "这点小事，我明明是清楚的。明明懂的。可是，我却……"
    "我却，不行。"
    "不行啊。"
    "束手无策的无力感，绠短汲深的人生经验，让我万分悔恨。"
    window hide


    $ loadBG(0,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("FPP")
    play FPP "CRS11A_FPP0000"
    $ current_voice = "voice/CRS11A_FPP0000.ogg"
    "菲利斯爸爸" "当自己已经毫无办法的时候，去借助可信之人的力量乃是商务的铁则"
    window hide


    $ loadBG(0,"BG_BLACK")


    "幸高叔叔刚才的话在我脑海中回响。这句话是在给不知如何是好的我们指出道路，但同时──"
    "也包含着让我们不要轻举妄动的意义吧。"
    "拙劣的行动时常会让事态更加糟糕。如果我们在焦虑的支配下再出面到处乱跑，被哪个Ｒｏｕｎｄｅｒ给抓到的话...."
    "幸高叔叔所做的一切就都没有意义了。"
    "现在的状况下没有我们能做的事，只能借助幸高叔叔的帮助。那么，就这么老实地待着才是最好的选择。"
    "按理来说……应该，是这样……"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0004"
    $ current_voice = "voice/CRS11A_CRS0004.ogg"
    "红莉栖" "「到头来……我还是什么都做不到啊……」"
    "我为自己的不成熟感到万分惭愧，强求着办不到的事情，就如同小孩子耍赖一般。"
    "人都有各自能力和经验的范畴，应当在自己可掌握的事物范围内作最大的努力。"
    "这才是社会运转的规则，适才所用，才能让每个人在社会中有固定的生存场所。"
    "如果这个世界上全都是无所不能的超人，那人类间的个性与差异就没有任何意义了。"
    "那样的世界将是多么的单调乏味，在美国那个承认文化多样化的国家生活过的我再明白不过了。"
    "同时我又再次认识到，在对社会的残酷性认识得越多时，越会发现自己人格里不成熟的地方。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0005"
    $ current_voice = "voice/CRS11A_CRS0005.ogg"
    "红莉栖" "「如果是教授和前辈的话……大概会说，不成熟也是你个性的一部分呢。或是说，有些事只有在不成熟的时候才能办到。」"
    "我如此这般试着说出了口，然后想到。"
    "……教授和前辈？"
    "脑中再次响起幸高叔叔的话。"
    window hide


    $ loadBG(0,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    $ stopvoc("FPP")
    play FPP "CRS11A_FPP0001"
    $ current_voice = "voice/CRS11A_FPP0001.ogg"
    "菲利斯爸爸" "人类并不能只靠一个人活下去。一个人所在的地方，有他身边的人，有社会，有历史。"
    $ stopvoc("FPP")
    play FPP "CRS11A_FPP0002"
    $ current_voice = "voice/CRS11A_FPP0002.ogg"
    "菲利斯爸爸" "那个人从过去积累下来的经验，他周围的人，生长的环境，全部加在一起，才成了这个人。"
    $ stopvoc("FPP")
    play FPP "CRS11A_FPP0003"
    $ current_voice = "voice/CRS11A_FPP0003.ogg"
    "菲利斯爸爸" "有给我指明道路的教授，有章一，有留未穗，有这个秋叶原的街道，所以才有现在在这里的我。"







    window hide


    $ loadBG(0,"BG_BLACK")





    $ loadBG(1,"BG72N")







    play se "SGSE056"







    hide screen phonebtn
    hide screen phoneSD1
    "我一个打挺坐了起来。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0006"
    $ current_voice = "voice/CRS11A_CRS0006.ogg"
    "红莉栖" "「对……对啊！」"
    "就像幸高叔叔身边有各种各样的人，我也同样和身边各种各样的人联系在一起。"
    "虽然我和叔叔年龄不同，人际关系方面也不可同日而语，但是我并不孤独。"
    "我有爸爸，妈妈……菲利斯和幸高叔叔，黑木先生。"
    "还有维克多·孔多利亚的教授和前辈们，冈部和桥田，真由理……"
    "在我的身边，有许多的人。就像幸高叔叔刚才拜托的人们一样，我也一定有可以求助的对象。"
    window hide
    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "现在，时间已过２３点……美国时间是早上。"
    "考虑了时间和时机，我把能向其求助的熟人在脑子里过了一遍。不过，符合的也只有１到２人而已。"
    "……可是这时，我想起某件事。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0007"
    $ current_voice = "voice/CRS11A_CRS0007.ogg"
    "红莉栖" "「今天……是教授开演讲会的日子。」"
    "实在是太糟糕的撞车。"
    "在维克多·孔多利亚大学脑科学研究所之中，相当于我恩师的教授，今天正好要向其它大学的教授披露研究成果。"
    "平时倒还罢了，但是今天，很有可能用电话和邮件都联系不上他。"
    "而且，就连平时马上就会回复的前辈，现在也没法马上联系到。"
    window hide
    call hide_phone

    "──除了他们以外我就不知道维克多·孔多利亚中其他人的个人联系方式了。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0008"
    $ current_voice = "voice/CRS11A_CRS0008.ogg"
    "红莉栖" "「怎么这样……为什么，偏在这个节骨眼上……」"
    "此时我想起了冈部的话。"
    $ stopvoc("OKA")
    play OKA "CRS11A_OKA0000"
    $ current_voice = "voice/CRS11A_OKA0000.ogg"
    "伦太郎" "「简直就像，世界的意志在期盼着真由理的死……」"
    "世界的意志……时间悖论……"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBGX012")



    hide screen phonebtn
    "难不成，我自己也已经被卷入到了「世界的意志」的影响之下？"
    "冈部说过，即使不是Ｒｏｕｎｄｅｒ亲自下手，最终真由理也会因为某个理由死去。无论多少次返回重来，无论怎么改变行动，真由理一定会死。"
    "世界的意志。自然的真理。冈部说只能如此描述，让人感觉这是如同命运般的东西。"
    "像现在这样，我去联络可能会给我提供帮助的人却很不顺利，也是同样的理由吗？"
    "是冈部口中的世界的意志，在妨碍我的行动吗？"
    "不，不是的。这种决定论的世界，我不承认。"
    "命运从一开始就已被决定了什么的，这种愚蠢的理论我不可能承认。"
    "那么，这个现象产生的原因应该是曾经发生的某种事件造成的。分析这个原因，然后消除掉的话，就有可能改变这个状态……"
    window hide




    $ loadBG(1,"BG72N")
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0009"
    $ current_voice = "voice/CRS11A_CRS0009.ogg"
    "红莉栖" "「问题在于，如何才能找出这个原因……如何才能，消除掉这个起因……」"
    "仅凭我的一已之力，果然是不可能的吧？"
    "我握紧了还没拨出去的手机。"
    "想不到一点能派上用场的知识。方才好像看到了一点曙光，却又立刻消逝无踪。"
    "如果这是在做研究，大概就会以真相与发现就是这样反复无常为借口而放弃了，但唯有这一回不行。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0010"
    $ current_voice = "voice/CRS11A_CRS0010.ogg"
    "红莉栖" "「到底怎样才好？」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "百般苦恼着，我像是在渴求什么似的打开手机。"
    "不经意间，通讯录中的一个名字映入我的眼睛。"
    "爸爸……"
    "几天前通过一次电话，但被对方极为冷淡地对待了。"
    "但是现在的我，已经恨不得把能拜托的人全拜托一遍了。而且，这还是我最喜欢的爸爸，更想要依赖他了……"
    "就是因为这种心情吧，我很自然地操作手机，拨通了爸爸的电话。"
    window hide



    "可是……"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0011"
    $ current_voice = "voice/CRS11A_CRS0011.ogg"
    "红莉栖" "「……不接，吗。也是啊，当然了，在这个点打电话——还是说，因为打电话的是我？」"
    "爸爸不喜欢我。唔，说不定是讨厌我吧。他怎么会接一个讨厌之人的电话呢。"
    window hide


    call hide_phone

    "合上手机，下意识地从床上爬起来。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "然后，出了我所在的客房，悄悄地打开了旁边房间的门……"
    window hide


    $ loadBG(0,"BG72N")

    show screen phonebtn
    "旁边的房间，和刚刚我待的房间一样黑暗。"
    "但那有规律的呼吸声，传达出这里有人在的信息。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS002A"]]["Check"]=True


    $ loadBG(2,"EV_CRS002A")



    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0012"
    $ current_voice = "voice/CRS11A_CRS0012.ogg"
    "红莉栖" "「……冈部。」"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0013"
    $ current_voice = "voice/CRS11A_CRS0013.ogg"
    "红莉栖" "「冈部……对不起。」"
    "我该怎么办才好？"
    "冈部憔悴得好厉害，他一直一直这样痛苦着……我是那么地想救救他，却没有办法。"
    "能为喜欢的人做些什么，我完全不知道啊……！"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0014"
    $ current_voice = "voice/CRS11A_CRS0014.ogg"
    "红莉栖" "「算什么……天才啊……像我这种人……」"
    "我一直都有努力下去的自信。能做的事都努力去做，也曾做出不少实绩。"
    "但是，那些东西在现在这个瞬间都没有任何用。"
    "不能让爸爸开心，不能救朋友，也帮不上喜欢的人……"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS002B"]]["Check"]=True


    $ loadBG(2,"EV_CRS002B")



    "轻轻地触碰冈部的脸。"
    "不知道是不是我多心，他好像瘦了。"
    "大概是被时间跳跃机覆写了未来的记忆之后，他的大脑进行了高强度的运作，所以异常地消耗卡路里吧。"
    "又或者是，当时他绝望地从Ｌａｂ跑出去之后，不停地在秋叶原东奔西跑的缘故。"
    "真是让人心碎的模样。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0015"
    $ current_voice = "voice/CRS11A_CRS0015.ogg"
    "红莉栖" "「对不起……我，我是这么的没用。什么都办不到……」"
    "眼泪划过了脸颊。"
    "一滴一滴地落在碰触着冈部的手指上。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0016"
    $ current_voice = "voice/CRS11A_CRS0016.ogg"
    "红莉栖" "「不行……不能叹气啊。痛苦的人——最痛苦的人，是冈部才对。我不能在这里哭……」"
    "对。最痛苦的人，最难受的人，是一次又一次重复着重复着见证真由理死亡的冈部。"
    "那么，我到底该……"
    window hide


    $ loadBG(0,"IBG040A")




    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS002B"]]["Check"]=True
    $ loadBG(0,"EV_CRS002B")

    "这时，我的脑海里出现了一个影像。"
    "时间跳跃机……我们在冈部的带领下制造的，时间机器。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS002A"]]["Check"]=True


    $ loadBG(2,"EV_CRS002A")



    "目前的状况下，要救真由理和桥田已经要到不择手段的地步了。"
    "可是改变了过去之后会变成怎样？"
    "用时间跳跃机回到过去，来改变现状？"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0017"
    $ current_voice = "voice/CRS11A_CRS0017.ogg"
    "红莉栖" "「……不行啊。」"
    "逆时间而行，改变过去的行为，究竟建立在什么法则和理论之上，还没有完全弄清楚。"
    "目前为止的Ｄｍａｉｌ实验能确定的是，对过去的事情进行干涉，会对世界造成巨大的变化。"
    "只不过对于世界的变化，我们是察觉不到的。"
    "这一切都是拥有Ｒｅａｄｉｎｇ；ｓｔｅｉｎｅｒ这一能力的冈部独自一人作出的“正是如此”的判断。"
    "如果他是在说谎或妄想而作出了这样的主张，一切都会在某个瞬间瓦解，仅仅成为一个假说。"
    "不可否认，我一直陪伴他到现在，相信着他的能力和主张，才基于这个主张做出了时间跳跃机。"
    "但即使是这样，能观测到时间变化的也只有冈部一人，实在太过主观和暧昧。"
    "反过来说，即使过去发生了改变，冈部以外的人都是察觉不到变化的。"
    "就算我改变了过去，在那个世界改变的瞬间，我的记忆也会消失。"
    "这样一来，即使再次发展到真由理死亡的事态，也无法展开阻止其死亡的行动。"
    "而且现在已经知道真由理会一次又一次地重复经历死亡，这样做的风险太高了。"
    "说到底，当前现状下要改变过去的这一行动，没有冈部的观测是无法成立的。"
    "没有Ｒｅａｄｉｎｇ；ｓｔｅｉｎｅｒ的观测，对过去的时间进行干涉本身就没有意义。"
    "这是只有冈部能办到的事，一切希望只能寄托在冈部身上。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0018"
    $ current_voice = "voice/CRS11A_CRS0018.ogg"
    "红莉栖" "「这样下去冈部的负担实在太大了……要想想什么其它办法。」"
    "注意到自己说话的语气，发现一直以来的焦燥感已经大多都消失掉了。"
    "焦虑的心情还在。但现在已经不是被这种情绪所左右，无法思考的状态了。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0019"
    $ current_voice = "voice/CRS11A_CRS0019.ogg"
    "红莉栖" "「多亏看到了你的脸呢，冈部。」"
    "开玩笑地嘟囔了一句，但说不定也真是这样。沉沉的睡意终于来袭了。"
    $ stopvoc("CRS")
    play CRS "CRS11A_CRS0020"
    $ current_voice = "voice/CRS11A_CRS0020.ogg"
    "红莉栖" "「……还是回房间吧。睡上一觉，然后再想改变局面的办法。」"
    window hide


    $ loadBG(2,"BG72N")



    show screen phonebtn
    show screen phoneSD1
    "为了不要吵醒冈部，我轻轻地起身，回到旁边为我准备的卧室。"

    hide screen phoneSD1
    window hide

    stop bgm 





    scene expression Solid("000000")  with fade
    return









    return





    return
