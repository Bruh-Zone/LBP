label SGFD2_RUK01A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade



    $ loadBG(0,"TIT007")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade
    $ date="8/20"
    $ day = "FRI"








    $ loadBG(0,"IBGX048")


    $ RcvMail(270)
    $ ReadMail(270)
    $ SndMail(271)
    play bgm "FD2BGM04"
    hide screen phonebtn
    hide screen phoneSD1


    "真由理酱去世了。"
    "这，也太突然了吧。"
    "到昨天为止也没发现什么奇怪的地方。"
    "明明还是一如既往的朝气蓬勃，光看上去就觉得既温和又不让人操心的笑脸。"
    "真由理酱是在下的朋友。"
    "不，挚友什么的只是我的一厢情愿罢了。"
    "刚进入高中的时候，在人生地不熟的班上第一个跟我说话的人是真由理酱。"
    $ stopvoc("MAY")
    play MAY "RUK01A_MAY0000"
    $ current_voice = "voice/RUK01A_MAY0000.ogg"
    "真由理" "「琉华酱应该更加自信一些哟。」"
    "如此，我一直都被真由理酱鼓励着。"
    "说真的，对于她的离去我完全没有实感。"
    "在葬礼的时候我看见了真由理酱的遗体。"
    "在棺材里的真由理酱如同睡着了一样。"
    "脸上带着一如既往的微笑。"
    "感觉就像随时会起来笑着说早上好一样。"
    "但是，不管等多久真由理酱也没法再活过来了。"
    "就这样一直闭着眼睛长眠下去。 "
    "并没有被吓一跳。"
    "将手放在她的皮肤上，传来的是刺骨的凉意。"
    "非常的——僵硬。"
    "然后在下终于确定了一件事。"
    "真由理酱已经死了。"
    "再也看不到她的笑容了。"
    "连用咕噜咕噜转动着的眼睛看着我的样子都，"
    "连她用那女孩子特有的柔弱的声音叫我的样子都，"
    "已经见不到了。"
    "人死之后会到哪里去呢？"
    "小时候好像也听父亲说过这类事。"
    $ stopvoc("UPP")
    play UPP "RUK01A_UPP0000"
    $ current_voice = "voice/RUK01A_UPP0000.ogg"
    "漆原父" "「人死后啊，就会成为神哟。」"
    "这是父亲告诉我的。"
    "但是，人死后就会被烧成灰烬。"
    "真由理酱化成了灰烬。"
    "化作了青烟飘向了高空。"
    "这本应是非常伤感的事情。"
    "明明是这种事，"
    "明明是这种事，为什么天空如此之蓝。"
    "连眼泪都流不出来的我，就这样失神地望着天空，在恍惚的思绪中思考着这些。"






    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK001A"]]["Check"]=True
    $ loadBG(0,"EV_RUK001A")

    hide screen phonebtn
    hide screen phoneSD1
    "手缓缓地抚过了胸口。"
    "又小又不起眼，但是依然柔和的鼓起。"
    "这就是我是女孩子的证明。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0000"
    $ current_voice = "voice/RUK01A_RUK0000.ogg"
    "琉华" "「女孩子……」"
    "试着说了出来。"

    "对、我是女的。"
    "虽说自称为在下（注：原文为ボク，是男性自称），但我果然是货真价实的女孩子啊。"
    "千真万确的事实。"
    "从前我就不断地做着同样的梦。"
    "已经忘了是从何时开始了。"
    "但是，应该从我懂事的时候开始的吧，所以这么算了应该是很久了。"
    "那真是个非常奇怪的梦啊。"
    "在那个梦里，我是男孩子。"
    "但是样貌并没有变化。"
    "性格也是，缺乏自信的内心性格也和现在一样。"
    "仅仅是性别上的区别。"
    "身边的人都以男孩子的身份对待我。"
    "这是当然的咯，因为梦中我真的就是个男孩子。"
    "所以大家全部，都把我当成男孩子看待。"
    "母亲也好姐姐也好朋友也好。"
    "而且——我心里最重要的那位也是。"
    "所以在梦中的我，不知为何认为自己是男生是一个令人悲伤的事实。"
    "是女孩子就好了呐，一直这么想着。"
    "做了这样的梦后，我睁开眼睛确认着自己的身体。"
    "然后心里的石头终于落下来了。"
    "这样的过程，不知从儿时开始已经重复了几次。"
    "以前，我曾以为大家都做着这样的梦。"
    "然而并不是这样。"
    "问姐姐也好问朋友也好，谁都说没做过那样的梦。"
    "真由理酱也说没有做过。"
    "因为在意这事，也调查过相关信息。"
    "根据梦的诊断来说，性转换的梦啊，是和周围的人际关系变化的暗示。"
    "但是，无论怎么思考，我始终都不认为我周围的人际关系有任何变化。"
    "即便如此，就算这个梦是人际关系变化的暗示，但一直不停地做同一个梦也太奇怪了。"
    "所以我对此一直心存疑虑。"
    "为什么只有我一直做着这个梦呢。"
    "然后那个时候，回答了这个疑问的是，那句话语。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0000"
    $ current_voice = "voice/RUK01A_OKA0000.ogg"
    "伦太郎" "「你啊、真的……曾经是男的啊。」"
    "这个是在下心中很重要的人——冈部伦太郎师傅所说的。"
    "在下真的是男生，但后来变成了女生，冈部师傅如是说。"
    "这句话深深地刺入了我那毫无防备的内心。"
    "宛如晴天霹雳。"
    "从很重要的人那里……从憧憬着的人那里听到这样的话。"
    "难道，在下至此一直被冈部师傅以那样的眼光看待——"
    "——那家伙明明是个男的，却硬要装成女生的样子——"
    "事实是否如此我并不确定。"
    "但是、"
    "要是师傅真的是这样想的话，就太令我伤心了。"
    "因为一直一直喜欢着他。"
    "第一次相遇时就一直。"
    "光是看到冈部师傅的脸就很开心了。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0001"
    $ current_voice = "voice/RUK01A_OKA0001.ogg"
    "伦太郎" "「哦、琉华子」"
    "就算只是向我搭话我也会很高兴。"
    "不知何时就有勇气了。"
    "如果能够变得更强的话……"
    "这样的话，我的心意也许就能够传达给他了吧……？"
    "一直，我就是这么想的。"
    "即使如此冈部师傅还是把我当做男孩子看待——"
    "这么一想，就又难过起来了。"
    "痛彻心扉。"
    "如此痛苦如此难过，以至于泪水已经划过了脸庞。"
    "但是。"
    "心里某处却在接受着这样的自己。"
    "——啊啊，果然。"
    "一直抱有着这样的违和感。"
    "不管看多少次都感觉非常微妙的梦。"
    "自己都不像自己了，这样的感觉。"
    "这一切的真相，感觉正如同冈部师傅所说的那样。"
    "果然我以前是——男生啊。"
    "以那句话作为契机和证据，我略微回忆起了一些我是男孩子的时候的记忆。"
    "啊……“是男孩子的时候”，这么说可能有点不对。"
    "就像冈部师傅所说的那样，没准在下是男孩子的那条世界线是存在的。"
    "虽然在下搞不清楚那到底是怎么一回事，但无论如何我以前真的是一个男孩子。"
    "接着，冈部师傅好像说过想要把我变回男孩子。"




    $ loadBG(0,"BG03A4")


    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    "按冈部师傅的说法就是，之前是男生的我会变成女生的原因是他们制造出的『{color=#f00}电话微波炉（暂）{/color}』的样子。"
    "冈部师傅说用那个机器向过去发送短信就可以改变过去。"
    "然后曾是男生的我，据说许了“想变成女生”这样的愿望。"
    "想变成女生。"
    "&lfCR2;说起来，男孩子的我，讨厌着自己是男孩子，一直想变成女孩子是为什么呢？"

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK001A"]]["Check"]=True


    $ loadBG(2,"EV_RUK001A")




    "那么，作为女孩子的我，能够……？"
    "这样想的话。"
    "结论就很清楚了了。"
    "果然，我不想变成男孩子。"
    "保持女儿身就好了。"
    "但是。"
    window hide


    $ loadBG(2,"BG_BLACK")



    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0002"
    $ current_voice = "voice/RUK01A_OKA0002.ogg"
    "伦太郎" "「拜托了、琉华子，如果不那样做的话……」"
    "被告知这样万万没想到的话。"

    hide screen phoneSD1


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0003"
    $ current_voice = "voice/RUK01A_OKA0003.ogg"
    "伦太郎" "「如果不那样做的话，真由理……真由理就就会死的。」"
    "真由理酱不仅是我的挚友，还是冈部师傅的青梅竹马。"
    "真由理会死这样的事……"

    "一开始我以为是糟糕的玩笑。"
    "但是在我的认知里，冈部师傅不像是会开这样玩笑的人。"
    "虽然平常也有突然性的发言，但是该有样子的时候也会有样子的。"
    "如果不是这样，我也不会变的喜欢上冈部师傅。"
    "冈部师傅说，正是因为我变成了女孩子，“世界线”才发生了变动，因而真由理才会死。"
    "所以为了防止这样的事，必须把我变回男孩子的样子。"
    "这根本不是一时半会能让人相信的话。"
    "冈部师傅讨厌我……虽然肯定不是这样的，但我还是这么想了。"



    $ loadBG(0,"BG_BLACK")


    "但是，５天前的傍晚……"
    "真由理——死掉了。"
    "根据当时在一起的桥田所说，事发的时候真由理没有任何奇怪的地方。"
    "但是，突然就很痛苦的倒在地上，好像之后就渐渐的动不了。"
    "真的就死了。"
    "然后，如果冈部师傅的话是真的，那么就是因为我了。"

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK001A"]]["Check"]=True


    $ loadBG(2,"EV_RUK001A")




    "因为我变成女孩子，真由理才会死的。"
    "因为我是女孩子。"
    "就是因为我说了想变成女孩子，真由理才。"
    "因为我这身体，把真由理给杀了。"
    "即使如此我还是。"
    "在下为何还要这样活下去呢。"
    "一直维持着女儿身到底是为了什么呢。"
    "在下……"
    "就算如此我还是想保持着女儿身……肯定就是这么想的咯。"
    "真是搞不懂。"
    "搞不懂自己的心情。"
    "但是，那样做的话。"
    "我……太差劲了。"


    stop bgm 


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0001"
    $ current_voice = "voice/RUK01A_RUK0001.ogg"
    "琉华" "「啊……」"
    "视线因为无法继续停留在自己的身体上，而转移到了某一样东西上。"
    window hide
    $ loadBG(0,"IBG052A",png=True)


    "是玩具刀。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0002"
    $ current_voice = "voice/RUK01A_RUK0002.ogg"
    "琉华" "「……五月雨」"
    "那是，在在下懦弱得连自己的想法都无法说出口的时候，冈部师傅送给在下的重要的礼物。"
    "如果坚持空挥这把刀的话，就能够变得更强——冈部师傅如是说过。"
    "更强——"
    hide screen phoneSD1
    window hide
    hide background-png 
    with dissolve





    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK002A"]]["Check"]=True
    $ loadBG(0,"EV_RUK002A")

    play se "SGSE360"

    hide screen phonebtn
    hide screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0003"
    $ current_voice = "voice/RUK01A_RUK0003.ogg"
    "琉华" "「十……一，十二……十三……」"
    play bgm "FD2BGM05"

    "我开始拼命地挥动五月雨。"
    "这么做了以后，我便不再迷茫了。"
    "再也不会焦虑和烦恼了。 "
    "我的心中，充斥着那份思念。"
    "因为这份思念，不管是几十次还是几百次，我都能继续挥动下去吧。"
    "但是。"


    play se "SGSE360"


    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0004"
    $ current_voice = "voice/RUK01A_RUK0004.ogg"
    "琉华" "「哈、哈……二十、一……二十、二……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0005"
    $ current_voice = "voice/RUK01A_RUK0005.ogg"
    "琉华" "「二、十…………！」"
    window hide
    play se "SGSE358"

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK002B"]]["Check"]=True


    $ loadBG(2,"EV_RUK002B")



    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0006"
    $ current_voice = "voice/RUK01A_RUK0006.ogg"
    "琉华" "「哈……哈…………」"

    "但我根本就没有这样的力气。"
    "不管是体力上还是精神力上。亦或是毅力和决断力。都没有。"
    "无论打算和哪个做朋友，但在下终究还是那个纤弱的自己。"
    "作为证据，在下连３０次空挥都不能好好地完成。"
    "在下……在下只是胆小鬼而已。"
    "然后，对于我来说胆小鬼是“不可以的事情”——"
    window hide


    $ loadBG(2,"BG15A")



    "对。"
    "不能接受的事情。"
    "对于我来说世界上就只有不可以的事和好事。"
    "并不是由在下来决定“不可以的事”和“好事”的标准。"
    "那么是谁来决定的呢。"
    "除了我之外的，谁呢？"
    "明明是男孩子，却像女孩子一样这件事便属于“不可以的事”。"
    "女孩子就该有女孩子的样子，当然是“好事”咯。"
    "想要变得坚强与自信，对于男孩子才来说是“好事”，而对于女孩子来说变得成熟、可爱温柔才是“好事”。"
    "所以对于身为男孩子的我来说，后者便属于“不可以的事”。"
    "只有我是女孩子才能做到。"
    "但是若是“胆小鬼”的话，无论对于男生还是女生来说，都是属于“不可以的事”吧。"
    "世人或多或少都这么认为吧。"
    "如果是这样的话，果然那是“不可以的事”呢。"
    "不管男女都一样。"
    "不管男女，胆小鬼对于任何人来说。"
    "都是不可以的。"
    "什么都无法改变。"
    "在下、"
    "在下。"

    window hide



    $ loadBG(2,"EVX_R08A")



    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0007"
    $ current_voice = "voice/RUK01A_RUK0007.ogg"
    "琉华" "「真由理……酱……」"

    "然后我曾几何时，连像这样抱着膝盖痛苦都无法做到。"
    "如果哭的话就会有人过来帮忙吧。"
    "「怎么了？」这样来自朋友的话语。"
    "但是，朋友却因为我的错，而……"

    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0008"
    $ current_voice = "voice/RUK01A_RUK0008.ogg"
    "琉华" "「真由理酱 ……呜呜……呜…………」"
    window hide
    play se "SGSE359"

    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0004"
    $ current_voice = "voice/RUK01A_OKA0004.ogg"
    "伦太郎" "「琉华子……」"
    "耳边传来了喁喁细语。"
    "我抬起头来。"
    "对我来说十分重要的人的身影伫立在那里。"
    window hide



    $ loadBG(2,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0009"
    $ current_voice = "voice/RUK01A_RUK0009.ogg"
    "琉华" "「……冈部、师傅……」"
    "发出声音的一瞬间，我再度热泪盈眶。"
    "我一边拼命忍住抽噎，一边继续说了下去。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0010"
    $ current_voice = "voice/RUK01A_RUK0010.ogg"
    "琉华" "「昨天……我去了真由理的告别仪式……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0011"
    $ current_voice = "voice/RUK01A_RUK0011.ogg"
    "琉华" "「大家都哭得不行。看来真由理酱真的是饱受大家喜爱啊……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0012"
    $ current_voice = "voice/RUK01A_RUK0012.ogg"
    "琉华" "「当然，我也最喜欢真由理酱了……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0013"
    $ current_voice = "voice/RUK01A_RUK0013.ogg"
    "琉华" "「我……虽然非常的怕生，但真由理酱还是一如既往地开朗地对待我」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0014"
    $ current_voice = "voice/RUK01A_RUK0014.ogg"
    "琉华" "「对我来说，她曾是最重要的朋友……」"
    "真的是这样的。"
    "我非常的喜欢真由理。"
    "我想她是我最重要的朋友。"
    "但是却。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0015"
    $ current_voice = "voice/RUK01A_RUK0015.ogg"
    "琉华" "「却、呐、冈部师傅……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0016"
    $ current_voice = "voice/RUK01A_RUK0016.ogg"
    "琉华" "「我们大家，到底是为了什么……而活着？」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD01"),"True","lh/OKA_ASD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0005"
    $ current_voice = "voice/RUK01A_OKA0005.ogg"
    "伦太郎" "「…………」"
    "冈部无言以对，只是露出了苦笑。 "
    "看起来是非常的痛苦。"
    "这也是理所当然的了。"
    "她可是冈部的青梅竹马，不管如何都比我要亲近得多。"
    "肯定认为真由理非常的重要。"
    "所以对于冈部来说，这样的问题是绝对不能问的。"
    "是“不可以的事”"
    "即使如此，我也不得不去问。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0017"
    $ current_voice = "voice/RUK01A_RUK0017.ogg"
    "琉华" "「虽然呐，真由理酱死掉了……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0018"
    $ current_voice = "voice/RUK01A_RUK0018.ogg"
    "琉华" "「在下、就像现在这样保持着女儿身」"
    "冈部说这正是我希望的。"
    "但是这并不是我希望看到的世界。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0019"
    $ current_voice = "voice/RUK01A_RUK0019.ogg"
    "琉华" "「我认为，这样下去是什么也改变不了的……所以我觉得这样是不行的……」"
    "就因为我变成了女孩子，而真由理必须死去的世界。"
    "这样的世界，并不是我所期望的。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0006"
    $ current_voice = "voice/RUK01A_OKA0006.ogg"
    "伦太郎" "「并非如此。」"
    "虽然冈部师傅这样说，但是——那果然是“不可以的事”。"
    "所以我——"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0020"
    $ current_voice = "voice/RUK01A_RUK0020.ogg"
    "琉华" "「冈部师傅，难道就没有，救回真由理酱的方法么……？」"
    "我向冈部师傅求助了。"
    "但是冈部师傅回答得很干脆。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0007"
    $ current_voice = "voice/RUK01A_OKA0007.ogg"
    "伦太郎" "「……没有。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0021"
    $ current_voice = "voice/RUK01A_RUK0021.ogg"
    "琉华" "「怎么会……！」"
    "想都没想就脱口而出。"
    "但是，不可以让“不可以的事情”保持着“不可以”的样子。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0022"
    $ current_voice = "voice/RUK01A_RUK0022.ogg"
    "琉华" "「想想看吧……只要能救她我什么都可以做……！」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0023"
    $ current_voice = "voice/RUK01A_RUK0023.ogg"
    "琉华" "「之前也从真由理那里听说过...冈部师傅做了一个时间回溯装置。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0024"
    $ current_voice = "voice/RUK01A_RUK0024.ogg"
    "琉华" "「如果用那个的话──」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA01"),"True","lh/CRS_BSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA08"),"True","lh/DAR_ASA08a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn

    "冈部师傅和桥田君加上牧濑氏一起做了一个很困难的研究。"
    "并不像以前只能向过去发送邮件，而是据说可以真正地回到过去的机器也做出来了。"
    "时间回溯——简直就像科幻小说一般。"
    "对于我来说根本无法相信。"
    "但是，如果是冈部师傅的话是可以做到的——我是这么认为的。"
    "不，并不只有冈部师傅一个人。"
    "桥田君和牧濑氏还有真由理酱一起做出来的。"
    "真的。"
    "真的要我来说，虽然我加入了这个团体。"
    "但我是最没用的。"
    "和桥田君还有牧濑氏不同，我什么都做不到。"
    "时间回溯是件很厉害的事情这点我虽然知道，但是连厉害在哪里都不清楚。"
    "如果不懂一些计算机知识的话，这样的东西确实无法理解。"
    "但是我连“想加入到大家的里面去”这句话都说不出口。"
    "肯定不可能的。"



    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0008"
    $ current_voice = "voice/RUK01A_OKA0008.ogg"
    "伦太郎" "「不可能的。」"
    "冈部师傅缓缓地摇着头，他的脸上写满了苦恼与忧愁。"
    "但就算是这样我也要试试。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0025"
    $ current_voice = "voice/RUK01A_RUK0025.ogg"
    "琉华" "「进行时间回溯的话，总会有什么办法.......」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0009"
    $ current_voice = "voice/RUK01A_OKA0009.ogg"
    "伦太郎" "「没有那样的，方法」"
    "冈部师傅握紧了下垂着的双手说道。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0010"
    $ current_voice = "voice/RUK01A_OKA0010.ogg"
    "伦太郎" "「虽然事实可能十分残酷，但我们除了接受真由理的逝去之外别无他法。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0026"
    $ current_voice = "voice/RUK01A_RUK0026.ogg"
    "琉华" "「不能就这么、轻言放弃啊……！为什么，要放弃呢？ 真由理酱死去了，难道你不难过吗？」"
    "放弃可不是什么好事哦。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0011"
    $ current_voice = "voice/RUK01A_OKA0011.ogg"
    "伦太郎" "「……总而言之，已经穷途末路了。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0027"
    $ current_voice = "voice/RUK01A_RUK0027.ogg"
    "琉华" "「不要……我不想让真由理这样死去！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA06"),"True","lh/OKA_ALA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0012"
    $ current_voice = "voice/RUK01A_OKA0012.ogg"
    "伦太郎" "「琉华子！」"
    "冈部师傅抓住正想继续说下去的我，大声地说道。"
    "这样气势冲天的样子，使我下意识地缩了缩身子。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0013"
    $ current_voice = "voice/RUK01A_OKA0013.ogg"
    "伦太郎" "「你觉得……我会这样简单地放弃么？」"
    "冈部撕心裂肺地吼了出来"
    "靠着自己的努力，试着去救重要的青梅竹马嘛？"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0014"
    $ current_voice = "voice/RUK01A_OKA0014.ogg"
    "伦太郎" "「为了救真由理，已经牺牲了其他人的梦想。就算受伤，只要能救到真由理我就去做。」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD02"),"True","lh/OKA_ALD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0015"
    $ current_voice = "voice/RUK01A_OKA0015.ogg"
    "伦太郎" "「但、已经到极限了……」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0016"
    $ current_voice = "voice/RUK01A_OKA0016.ogg"
    "伦太郎" "「已经、不可能了……」"

    "那是真正的悲鸣。"
    "听到了那样的悲鸣，我顿悟了。"
    "我只有对自己的事情不用脑子。"
    "我见证过冈部师傅所经历的艰辛，但也没有想过。"
    "能够制作时间回溯装置的人是冈部。"
    "他没有理由不知道能不能用这个装置拯救真由理。"
    "冈部不断地回到过去，去改写真由理死去的命运。"
    "一次又一次，一次又一次。"
    "就算是这样，冈部师傅依然宣称宿命无法改写。"
    "不断地回到过去，不断地目击着真由理死去。"
    "自己重要的人不断地......"
    "想让她活下来。"
    "不想让她死去。"
    "即使不断地这样祈祷着，这个愿望也无法传递给神明。"
    "她死了，这无法改变的事实，被不断地重复着。"
    "这真的是痛苦得不行。"

    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0028"
    $ current_voice = "voice/RUK01A_RUK0028.ogg"
    "琉华" "「……十分抱歉。」"
    "这样残酷的现实摆在冈部的眼前，为什么我还会说“放弃是不行的……为什么放弃……？”什么的呢？"
    "但是——"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0029"
    $ current_voice = "voice/RUK01A_RUK0029.ogg"
    "琉华" "「我，完全没有考虑过……冈部的心情」"
    "但是果然我没法忍住不说。"

    stop bgm 
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0030"
    $ current_voice = "voice/RUK01A_RUK0030.ogg"
    "琉华" "「但是并非没办法吧。」"
    "因为。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0031"
    $ current_voice = "voice/RUK01A_RUK0031.ogg"
    "琉华" "「不是，还有一个方法吗……」"
    "剩下的唯一方法。"
    "那便是。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0032"
    $ current_voice = "voice/RUK01A_RUK0032.ogg"
    "琉华" "「如果我变回男孩子的话──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA06"),"True","lh/OKA_ALA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0017"
    $ current_voice = "voice/RUK01A_OKA0017.ogg"
    "伦太郎" "「那样不行」"
    play bgm "FD2BGM08"
    "冈部立马明白了话中的意思立刻回答道。"
    "但是，就算这样我也没法简单地点头赞同。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0033"
    $ current_voice = "voice/RUK01A_RUK0033.ogg"
    "琉华" "「拜托了、冈部师傅。我不想用真由理的牺牲来完成自己的愿望……！」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0034"
    $ current_voice = "voice/RUK01A_RUK0034.ogg"
    "琉华" "「请救救真由理吧……！」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0018"
    $ current_voice = "voice/RUK01A_OKA0018.ogg"
    "伦太郎" "「我不会让你变回男孩子的」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0035"
    $ current_voice = "voice/RUK01A_RUK0035.ogg"
    "琉华" "「为什么……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0036"
    $ current_voice = "voice/RUK01A_RUK0036.ogg"
    "琉华" "「为什么呢……！？」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0019"
    $ current_voice = "voice/RUK01A_OKA0019.ogg"
    "伦太郎" "「我已经下定决心了。再也不能因为我的自私让别人受伤了。」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0020"
    $ current_voice = "voice/RUK01A_OKA0020.ogg"
    "伦太郎" "「而且，就算回到原来的世界线，未必能避免真由理的死去。」"
    "但是。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0021"
    $ current_voice = "voice/RUK01A_OKA0021.ogg"
    "伦太郎" "「我不愿因为那太低的可能性……牺牲任何人……你的想法。」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA07"),"True","lh/OKA_ALA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0022"
    $ current_voice = "voice/RUK01A_OKA0022.ogg"
    "伦太郎" "「所以，已经够了。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0037"
    $ current_voice = "voice/RUK01A_RUK0037.ogg"
    "琉华" "「冈部师傅……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0038"
    $ current_voice = "voice/RUK01A_RUK0038.ogg"
    "琉华" "「但是，就这样的话，我可不同意哦……」"
    "因为这是"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0039"
    $ current_voice = "voice/RUK01A_RUK0039.ogg"
    "琉华" "「我无法……忍受我的存在……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0040"
    $ current_voice = "voice/RUK01A_RUK0040.ogg"
    "琉华" "「我女生的体态是，建立在真由理死的基础上，这一点让我一生都无法接受。」"
    "这是“不可以的事”。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0041"
    $ current_voice = "voice/RUK01A_RUK0041.ogg"
    "琉华" "「这种负担太沉重了……一定会把我压垮的……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0042"
    $ current_voice = "voice/RUK01A_RUK0042.ogg"
    "琉华" "「呐、为什么……」"
    "我是自私的。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PAGER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_PAGER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_PAGER"])
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0043"
    $ current_voice = "voice/RUK01A_RUK0043.ogg"
    "琉华" "「为什么那个时候，我会往１８年前我的母亲的{color=#f00}ＢＰ机{/color}发送那份邮件呢……？」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0044"
    $ current_voice = "voice/RUK01A_RUK0044.ogg"
    "琉华" "「为什么，没有选择真由理，而是……选择了在下……呢？」"
    "真由理死前把我变回男孩子就好，我是这样问的。"
    "那个时候，作为交换条件，我希望与冈部师傅交往，就算只有那么一点点时间也好。我是这么希望的。"
    "但是，冈部最后还是没有把我变回男孩子。"
    "那个时候，那封邮件没有发送，正是因为我的关系。"
    "虽然如此，他却如此地谴责着自己。"
    "就算如此。"
    "果然，这样的显示对我一个人来说是过于沉重的负担。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0023"
    $ current_voice = "voice/RUK01A_OKA0023.ogg"
    "伦太郎" "「你啊，不要有任何负罪感。这一切、都是我的选择。」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0024"
    $ current_voice = "voice/RUK01A_OKA0024.ogg"
    "伦太郎" "「杀掉真由理的，是我。所以，这份罪孽就全部让我来背负吧。」"
    "这话.....让我非常的高兴。"
    "然而，这样说并不能让我的罪恶感消失。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0025"
    $ current_voice = "voice/RUK01A_OKA0025.ogg"
    "伦太郎" "「而且，我也想让你变得幸福。」"
    "就算这么说。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0045"
    $ current_voice = "voice/RUK01A_RUK0045.ogg"
    "琉华" "「幸福什么的……不是不应该变得幸福吗……」"
    "因为。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0046"
    $ current_voice = "voice/RUK01A_RUK0046.ogg"
    "琉华" "「真由理的死，不是有我的关系吗……」"
    "我这副身体的原因。"
    "那么。"
    "那么就使得冈部都没法变得幸福了。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0026"
    $ current_voice = "voice/RUK01A_OKA0026.ogg"
    "伦太郎" "「…………」"

    "冈部师傅的目光朝我的方向移动了。"
    "然而并没有在看着我。"
    "什么都——没再看。"
    "没有像以前那样的光辉、"
    "冈部师傅就必须这样一生背负着，对真由理见死不救的罪孽。"
    "这些都是我的过错。"
    "是我说了想要变成女孩子，才让真由理的死变成冈部师傅不得不一生背负着的罪行。"
    "这样的话，可能非常幸苦吧。"
    "但是还能对冈部师傅说“别放弃”这样的话了吗？"
    "不行。这是“不可以的事”。"
    "不断的重复着这一幕惨状，以至于已经麻木的冈部师傅，又要让他继续这样的轮回。"
    "这样的事不能说。"
    "因为，那是我的任性。"

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0027"
    $ current_voice = "voice/RUK01A_OKA0027.ogg"
    "伦太郎" "「这个不是你的错，不要再这样说了。」"
    "就算冈部师傅这样说。"
    "但是、大概，是想让我高兴点吧。"
    "让我认识到我过去没有犯错，将我的罪恶感消除。"
    "但是因为这样的理由会让冈部师傅更加的痛苦，果然还是“不可以的事”。"
    "但是如果是这样的话。"
    "我力所能及的事情，还有........."
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0028"
    $ current_voice = "voice/RUK01A_OKA0028.ogg"
    "伦太郎" "「虽然你现在可能非常的伤心……但我希望你能看着前方，连同真由理的那份，好好地活下去。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0047"
    $ current_voice = "voice/RUK01A_RUK0047.ogg"
    "琉华" "「怎么会……才不要那样呢」"
    "我抱住冈部师傅的身子。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0048"
    $ current_voice = "voice/RUK01A_RUK0048.ogg"
    "琉华" "「我...........我想跟你一起，担负起这个责任。」"
    "这样的话至少能够使冈部师傅变得轻松点。"
    "冈部师傅的罪恶也。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0029"
    $ current_voice = "voice/RUK01A_OKA0029.ogg"
    "伦太郎" "「一起……背负？……你在说什么傻话啊。」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD01"),"True","lh/OKA_ALD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0030"
    $ current_voice = "voice/RUK01A_OKA0030.ogg"
    "伦太郎" "「我不仅已经是因果轮回之外的人了，还是对真由理见死不救的人──」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0049"
    $ current_voice = "voice/RUK01A_RUK0049.ogg"
    "琉华" "「那样的话、我也要跳出因果轮回……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0050"
    $ current_voice = "voice/RUK01A_RUK0050.ogg"
    "琉华" "「在我想起我曾经是个男孩子的时候，已经跳出去了哦……？」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0051"
    $ current_voice = "voice/RUK01A_RUK0051.ogg"
    "琉华" "「以真由理的生命作为交换，我才能以女生的身份活下去这一点，也不是已经超出因果轮回了么……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0052"
    $ current_voice = "voice/RUK01A_RUK0052.ogg"
    "琉华" "「我们，可是共犯哦……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0053"
    $ current_voice = "voice/RUK01A_RUK0053.ogg"
    "琉华" "「这份悲伤，这份内疚」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0054"
    $ current_voice = "voice/RUK01A_RUK0054.ogg"
    "琉华" "「想要两个人来一起承受下去……」"
    "这样我的罪恶感。"
    " 也会变轻点吧。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA07"),"True","lh/OKA_ALA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0031"
    $ current_voice = "voice/RUK01A_OKA0031.ogg"
    "伦太郎" "「啊啊。我知道了。……」"
    hide screen phonebtn
    "冈部用两手将我拥入怀里"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0032"
    $ current_voice = "voice/RUK01A_OKA0032.ogg"
    "伦太郎" "「与我、一起背负……」"
    "如此温柔的声音"
    "温柔，"
    "而又微弱。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0033"
    $ current_voice = "voice/RUK01A_OKA0033.ogg"
    "伦太郎" "「一起，不忘此事地，活下去吧……」"
    "所以我"
    "终于感到了一点救赎，"
    "虽然对于我是女儿身的事情。"
    "这个罪恶虽然并没有被消除。"
    "但是一个人背负的话就太重太重了。"
    "如果是和冈部一起背负的话。"
    "一直——"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0055"
    $ current_voice = "voice/RUK01A_RUK0055.ogg"
    "琉华" "「可以一直，留在你的身边吗？」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0056"
    $ current_voice = "voice/RUK01A_RUK0056.ogg"
    "琉华" "「因为，我很喜欢冈部师傅……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0057"
    $ current_voice = "voice/RUK01A_RUK0057.ogg"
    "琉华" "「虽然有点对不起真由理……但还是想，和你一直在一起……」"
    "让我留在你身边的话。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0034"
    $ current_voice = "voice/RUK01A_OKA0034.ogg"
    "伦太郎" "「当然了」"
    "——啊啊，对了。"
    "我原来一直想听到的是这句话啊。"
    "我到底是被谁拯救了呢。"
    "然后冈部师傅想追求的东西，应该和我想追求的是同一个东西。"
    "拯救了我的是冈部，而拯救冈部的是我。"
    "我们就这样互相舔舐着对方的伤口。"
    "就只是这样只要有一点都足以拯救彼此了。"
    hide screen phoneSD1
    window hide

    stop bgm 


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "感觉那样也不错呢。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"IBGX033")


    play bgm "FD2BGM05"

    "从那开始直到天空被染成金黄色，我与冈部师傅就在那里抱着，什么也没有做。"
    "感受彼此的温暖。"
    "一边回忆着真由理。"
    "抱歉呢，真由理酱。"
    "对……不起。"
    "结果就是我什么忙都没帮上。"
    "什么都"
    "至少，能回到过去的话……"
    "回到过去……"




    $ loadBG(2,"BG15E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0058"
    $ current_voice = "voice/RUK01A_RUK0058.ogg"
    "琉华" "「呐，冈部师傅」"
    "对了。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0059"
    $ current_voice = "voice/RUK01A_RUK0059.ogg"
    "琉华" "「在下还有一件未能完成的与真由理的约定……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0060"
    $ current_voice = "voice/RUK01A_RUK0060.ogg"
    "琉华" "「因为那个约定的关系，我认为真由理酱十分的难过……」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0035"
    $ current_voice = "voice/RUK01A_OKA0035.ogg"
    "伦太郎" "「未能完成的约定？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0061"
    $ current_voice = "voice/RUK01A_RUK0061.ogg"
    "琉华" "「……是{color=#f00}ＣＯＳＰＬＡＹ。{/color}」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn

    "真由理有制作ＣＯＳ服装的爱好，劝我参加ＣＯＳＰＡＬＹ过好几次。"
    "我好像挺适合ＣＯＳＰＬＡＹ的。"
    "但是除此之外，感觉ＣＯＳＰＬＡＹ的时候我和平时的自己不一样，更加的有自信——真由理酱总是这么对我说的。"
    "因为那天。"



    $ loadBG(0,"IBGX048")

    hide screen phonebtn

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COMIMA"])
    "那天，我实在是无法拒绝真由理酱的邀请，于是定下了去{color=#f00}夏Ｃｏｍｉ{/color}的计划。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "但是，最后还是没有实现约定。"
    "事实上，这个诺言再也实现不了了。"
    "但是，我们还有办法。"
    "我是这样想的。"



    $ loadBG(0,"BG15E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ RcvMail(272)
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0062"
    $ current_voice = "voice/RUK01A_RUK0062.ogg"
    "琉华" "「用时间回溯装置，回到……那天吧？」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0036"
    $ current_voice = "voice/RUK01A_OKA0036.ogg"
    "伦太郎" "「回到过去……你吗！？」"
    "我非常肯定地点了点头。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0037"
    $ current_voice = "voice/RUK01A_OKA0037.ogg"
    "伦太郎" "「真的？」"
    "再一次认真地点头。"
    "冈部师傅沉思了一会后，缓缓地摇了摇头。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0038"
    $ current_voice = "voice/RUK01A_OKA0038.ogg"
    "伦太郎" "「那个太危险了，除了我以外的人都最好别用……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0063"
    $ current_voice = "voice/RUK01A_RUK0063.ogg"
    "琉华" "「拜托了……！」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0064"
    $ current_voice = "voice/RUK01A_RUK0064.ogg"
    "琉华" "「至少再让我看一眼，真由理酱的笑容……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0065"
    $ current_voice = "voice/RUK01A_RUK0065.ogg"
    "琉华" "「因为，我什么都没能给她……」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "至少能够减少点罪恶感……"
    "不对。"
    "这样只不过单纯的满足自己的想法罢了。"
    "但是总比不敢要强吧。"
    "不管是对我还是对冈部师傅来说。"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0039"
    $ current_voice = "voice/RUK01A_OKA0039.ogg"
    "伦太郎" "「但是你不是对于那种满是死宅的环境不太适应么。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0066"
    $ current_voice = "voice/RUK01A_RUK0066.ogg"
    "琉华" "「确实，有点害怕……但是，不用再说那样的话了……」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0067"
    $ current_voice = "voice/RUK01A_RUK0067.ogg"
    "琉华" "「那是因为，在下会变得和冈部师傅一样」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0068"
    $ current_voice = "voice/RUK01A_RUK0068.ogg"
    "琉华" "「只要用这个装置的话……就能过逃出因果轮回了吧？」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0069"
    $ current_voice = "voice/RUK01A_RUK0069.ogg"
    "琉华" "「这样就能和你一起背负这份罪了……」"
    "两人一起分担罪恶。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0070"
    $ current_voice = "voice/RUK01A_RUK0070.ogg"
    "琉华" "「所以说……」"
    hide screen phoneSD1
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade


    $ loadBG(0,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM01"

    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0040"
    $ current_voice = "voice/RUK01A_OKA0040.ogg"
    "伦太郎" "「如果成功了的话，就和我取得联络。这样的话我一定会将你带到真由理的身边的。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0071"
    $ current_voice = "voice/RUK01A_RUK0071.ogg"
    "琉华" "「恩……」"

    "最后，冈部师傅同意了我的请求。"
    "眼前出现的是坏掉了的微波炉。"
    "虽然还是不能立刻相信这个东西能让人回到过去，但使用这个的话好像可以将自己的记忆传送到过去的自己里。"
    "从理论上简单来说和向过去发送邮件是一回事，这样就稍微能够接受了。"
    "但要注意的是，下层的ＭＲ．显像管的超大电视没有打开的话，就无法启动机器，也无法回到48小时之前的世界。"
    "我虽然不清楚是为什么，但听冈部师傅说的没错吧。"
    "现在我正要前往的是１５日——夏Ｃｏｍｉ的早晨。"
    "前一天夜里，不知道发生了什么。"
    "虽然很遗憾，但是我好像动摇了，最后可能没有去成夏Ｃｏｍｉ。"
    "今天是２０号。"
    "这个装置无法回到两天之前的时间，所以至少需要跳跃三次才能回到１５号。"
    "而楼下的显像管工房从正午开到晚上８点左右。"
    "所以，错过一次机会的话，也许就赶不上了。"
    "冈部师傅说为了以防万一，要尽可能的少进行时间跳跃。"
    "这样的话，时间就是有限的。"
    "跳跃时间后就没有让人发呆的时间了。"

    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0072"
    $ current_voice = "voice/RUK01A_RUK0072.ogg"
    "琉华" "「…………」"
    "不可以。现在却开始紧张了。"
    "本身就没有把除了冈部师傅其他人的记忆送回过去的先例。"
    "能够顺利的完成吗"
    "......我这是在说什么。"
    "这不是已经决定了的事吗，为了完成真由理的愿望。"
    "这样，即使如果失败的话。那个时候——"
    "也会高兴的。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0041"
    $ current_voice = "voice/RUK01A_OKA0041.ogg"
    "伦太郎" "「别担心，脑子虽然会有点疼但很快就会好的。」"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0073"
    $ current_voice = "voice/RUK01A_RUK0073.ogg"
    "琉华" "「是、是……」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0042"
    $ current_voice = "voice/RUK01A_OKA0042.ogg"
    "伦太郎" "「就算到了那边，也别慌张，要冷静地调查状况。」"
    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0043"
    $ current_voice = "voice/RUK01A_OKA0043.ogg"
    "伦太郎" "「没事了我会一直在你身边的。」"
    "冈部师傅温柔地摸着我的头。"
    "稍稍中和了我的恐惧感。"

    stop bgm 
    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0074"
    $ current_voice = "voice/RUK01A_RUK0074.ogg"
    "琉华" "「……那么，出发吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "冈部师傅按下微波炉的定时器后，微波炉开始缓缓转动起来。"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0075"
    $ current_voice = "voice/RUK01A_RUK0075.ogg"
    "琉华" "「一定，能够回来的……！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK01A_OKA0044"
    $ current_voice = "voice/RUK01A_OKA0044.ogg"
    "伦太郎" "「嗯。我会等着的。」"
    window hide




    play se "SGSE035L" loop
    show houden 

    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0076"
    $ current_voice = "voice/RUK01A_RUK0076.ogg"
    "琉华" "「──！」"
    "房间中各种游走的电气使得我不禁又缩了缩身子。"
    window hide


    "同时眼前一片恍惚，连冈部师傅的身影都看不清楚。"
    "不要。"
    "虽然以为会很开心，但果然超可怕！"
    "在下……"
    "在下……"
    $ stopvoc("RUK")
    play RUK "RUK01A_RUK0077"
    $ current_voice = "voice/RUK01A_RUK0077.ogg"
    "琉华" "「冈部师──」"

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
    call timeleap (fromtime=[8,20,18,46], totime=[8,18,18,46], fromday=[5])





    return




    stop se




    window hide




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return







    return
