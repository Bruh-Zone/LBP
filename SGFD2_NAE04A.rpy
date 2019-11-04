label SGFD2_NAE04A:

    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide




    $ loadBG(0,"BG04A1")

    play bgm "FD2BGM04"

    $ date="7/8"
    $ day = "MON"
    hide screen phonebtn
    hide screen phoneSD1

    "２年前──"
    "父亲的葬礼结束之后。"
    "我在一堆布朗管电视包围之中，孤单一人抱膝在地。"
    "自己记不很清楚，后来听说好像是在两天里不吃不喝，就快进入脱水症状了。"
    "即使这样，在那个时候，我还是认为，只要呆在那儿一直等下去，父亲就会回来的。我一直在小声而不断地呼唤着父亲。"
    "然后随之意识远去。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "闭上眼，一片黑暗。"
    "感觉就像是掉进了深而又深的陷阱之中，一直一直地下落。"
    "感到明白了和白兔一起坠落的爱丽丝的心情。"
    "但是，没有发出悲鸣的力气。"
    "想着这样落下去，身体摔得四分五裂，惊惧万分。"
    "在这样的时候，我的呼声有人听到了。"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0000"
    $ current_voice = "voice/NAE04A_FEI0000.ogg"
    "菲利斯" "「绹喵……！」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0001"
    $ current_voice = "voice/NAE04A_FEI0001.ogg"
    "菲利斯" "「绹！」"
    window hide

    $ loadBG(0,"BG04A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BLC04"),"True","lh/FEI_BLC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "睁开眼，留未穗姐站在那里。"
    "脸上一副要哭出来的样子。"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0002"
    $ current_voice = "voice/NAE04A_FEI0002.ogg"
    "菲利斯" "「来和我们一起住吗？」"
    $ stopvoc("FEI")
    play FEI "NAE04A_FEI0003"
    $ current_voice = "voice/NAE04A_FEI0003.ogg"
    "菲利斯" "「一起、过来住」"
    "留未穗姐姐握起了我的手。"
    "于是，我被秋叶家所接受了。"
    window hide

    stop bgm 





    $ loadBG(0,"BG02A3")


    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM07"
    "桶子叔叔，真的第二天开始就拿出干劲了。"
    "昨天明明只是盯着只有１６页薄的同人志看了２个小时以上的。"
    "今早，到实验室里一看──"
    window hide


    $ loadBG(2,"BG03A7")



    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0000"
    $ current_voice = "voice/NAE04A_NAE0000.ogg"
    "绹" "「电子微波炉……！」"
    window hide


    $ loadBG(2,"BG03A7S")



    hide screen phonebtn
    "有些紧凑的大小的电子微波炉在房间里处摆放着。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0001"
    $ current_voice = "voice/NAE04A_NAE0001.ogg"
    "绹" "「是谁……在什么时候……」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0002"
    $ current_voice = "voice/NAE04A_NAE0002.ogg"
    "绹" "「难道是、冈伦叔吗？」"
    window hide



    $ loadBG(2,"BG03A7")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VALKYRIE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VALKYRIE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_VALKYRIE"])
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0000"
    $ current_voice = "voice/NAE04A_DAR0000.ogg"
    "至" "「不。冈伦来都没来。不过我们『{color=#f00}瓦尔基里{/color}』的活动啊、支持的人可是有很多呢」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0003"
    $ current_voice = "voice/NAE04A_NAE0003.ogg"
    "绹" "「瓦尔基里？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0001"
    $ current_voice = "voice/NAE04A_DAR0001.ogg"
    "至" "「嗯ー、简单地来说就是社团名一样的东西。更多的还是为了安全不要问的好。也不是随便就能谈论的东西」"
    "桶子叔叔说的话，是真的还是谎话真难以区分。"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0002"
    $ current_voice = "voice/NAE04A_DAR0002.ogg"
    "至" "「也就是，这些支持者们一起，今天一个大早给我送来的」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0003"
    $ current_voice = "voice/NAE04A_DAR0003.ogg"
    "至" "「不过，从厕所窗户不发出声音地过来还真费了一番功夫」"
    "房间里还散乱摆着昨天我买来的零件。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0004"
    $ current_voice = "voice/NAE04A_NAE0004.ogg"
    "绹" "「要花多久能做出来呢？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0004"
    $ current_voice = "voice/NAE04A_DAR0004.ogg"
    "至" "「既不能发出很大声音、晚上会漏出光线不能作业……」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0005"
    $ current_voice = "voice/NAE04A_DAR0005.ogg"
    "至" "「综合考虑、一个星期能够做好就好了呢。」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0005"
    $ current_voice = "voice/NAE04A_NAE0005.ogg"
    "绹" "「一个星期……」"
    "明天开始就是考试周了。"
    "虽然能从学校早些回来……"
    "考试的复习该怎么办才好啊。"
    "嗯嗯，只要不睡觉地学习就好了。"
    "也不能一周都彻夜不眠，但一定会有办法的。"

    $ targetmailid = 471

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0006"
    $ current_voice = "voice/NAE04A_NAE0006.ogg"
    "绹" "「我该做什么好呢？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0006"
    $ current_voice = "voice/NAE04A_DAR0006.ogg"
    "至" "「当然了、也有给绹酱你的工作哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0007"
    $ current_voice = "voice/NAE04A_NAE0007.ogg"
    "绹" "「真的？」"

    call CHECK_RM_RECEIVE
    "采购完之后我还以为会被晾在一边，听到这话，真有些开心。"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0007"
    $ current_voice = "voice/NAE04A_DAR0007.ogg"
    "至" "「请你帮我把洞打开一点吧」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0008"
    $ current_voice = "voice/NAE04A_NAE0008.ogg"
    "绹" "「扩开，洞？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0008"
    $ current_voice = "voice/NAE04A_DAR0008.ogg"
    "至" "「啊……刚才的、能够请你再说一遍吗？　可以的话我要感极而泣了」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0009"
    $ current_voice = "voice/NAE04A_NAE0009.ogg"
    "绹" "「扩开」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB02"),"True","lh/DAR_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0009"
    $ current_voice = "voice/NAE04A_DAR0009.ogg"
    "至" "「不是这个」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0010"
    $ current_voice = "voice/NAE04A_NAE0010.ogg"
    "绹" "「洞」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB07"),"True","lh/DAR_CSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0010"
    $ current_voice = "voice/NAE04A_DAR0010.ogg"
    "至" "「请，从头完整地说」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0011"
    $ current_voice = "voice/NAE04A_NAE0011.ogg"
    "绹" "「…………」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0011"
    $ current_voice = "voice/NAE04A_DAR0011.ogg"
    "至" "「…………」"
    window hide


    $ loadBG(2,"BG03A7R")



    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0012"
    $ current_voice = "voice/NAE04A_NAE0012.ogg"
    "绹" "「洞、是那个地板上的洞吗？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KTKR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KTKR"])
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0012"
    $ current_voice = "voice/NAE04A_DAR0012.ogg"
    "至" "「喂，被冷冷地无视了啊{color=#f00}ｋｔｋｒ{/color}！」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_FMM01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_FMM01_01"])

    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我在昏暗房间的地上蹲下，朝洞里望去。"
    "看不到楼下店中的状况。"
    "没有贯通，所有自然。"
    window hide

    $ loadBG(0,"BG03A7")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0013"
    $ current_voice = "voice/NAE04A_DAR0013.ogg"
    "至" "「这次的任务，不去{color=#f00}布朗管工房{/color}里的话就没法开始的哦」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0014"
    $ current_voice = "voice/NAE04A_DAR0014.ogg"
    "至" "「所以我想让绹酱、把那个洞打穿，扩大到人能通过的程度」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0015"
    $ current_voice = "voice/NAE04A_DAR0015.ogg"
    "至" "「但是要、不出声地」"
    "所以要使用五金工具。"
    "不过，不能发出声音什么的，感觉相当的难办啊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA09"),"True","lh/DAR_CSA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0016"
    $ current_voice = "voice/NAE04A_DAR0016.ogg"
    "至" "「贯通、扩张。之后明白的吧？　贯通、扩张」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0013"
    $ current_voice = "voice/NAE04A_NAE0013.ogg"
    "绹" "「为什么要说两遍啊？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0017"
    $ current_voice = "voice/NAE04A_DAR0017.ogg"
    "至" "「我是绅士，不得不说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA07"),"True","lh/DAR_CSA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0018"
    $ current_voice = "voice/NAE04A_DAR0018.ogg"
    "至" "「不发出声音地打通洞、我这说着、太工口了吧。哈哈」"
    "怎么好像在喘着粗气……。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0014"
    $ current_voice = "voice/NAE04A_NAE0014.ogg"
    "绹" "「小学生的时候，我倒是很擅长手工」"
    "比起画画，我更喜欢动手。"
    "所以，我不会说我做不到。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0019"
    $ current_voice = "voice/NAE04A_DAR0019.ogg"
    "至" "「嘛，在我做电话微波炉的时间里想办法帮我弄好就行了」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0015"
    $ current_voice = "voice/NAE04A_NAE0015.ogg"
    "绹" "「……唔」"
    "这么说也就是，在桶子叔叔做完之前，就是时间限制。"
    "可以做好吗……"
    "嗯嗯，也只有开始做了"
    "不能成为累赘啊。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG03A7R")
    play se "SGSE338L" loop


    hide screen phonebtn
    show screen phoneSD1
    "这个洞的话，如果避开钢筋，取除二层地板和一层天花板之间的众多管道，就能到达下面了。"
    "只是，不发出声音地使用锯子，确实非常的难。"
    "而且，轻手轻脚地锯的话，完全不会有进展。"
    "有什么巧妙的技巧就好了啊……。"
    "我在昏暗的房间里，向下默不作声地工作着。"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0020"
    $ current_voice = "voice/NAE04A_DAR0020.ogg"
    "至" "「喂、绹酱、为什么突然之间就变得无表情了啊。看着好可怕哇」"
    stop se
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0016"
    $ current_voice = "voice/NAE04A_NAE0016.ogg"
    "绹" "「…………」"
    play bgm "FD2BGM04"
    "确实我在集中注意力的时候会变得面无表情，总是被朋友这么说。"
    "所以，说女孩子恐怖什么的，桶子叔叔简直是烂透了。"
    "而且这个房间里还非常热。"
    "……嗯，不对。是热得要命。"
    "要是知道会要干活的话，带件便服过来就好了。要是穿着校服继续作业的话，不知道受不受得住。"
    "汗水从额头上落下，在地上就快要形成了小小的水洼。"
    "为了不被“黑衣人”发现，关紧了窗户，也没有开冷气。"
    "即使有冷气，因为没有电，本来就也用不了。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0017"
    $ current_voice = "voice/NAE04A_NAE0017.ogg"
    "绹" "「啊……电」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0018"
    $ current_voice = "voice/NAE04A_NAE0018.ogg"
    "绹" "「要运转时间机器，没有电岂不是不行吗……？」"
    window hide


    $ loadBG(2,"BG03A7")



    show screen phonebtn
    "自然，这栋大楼里已经停电了。"
    "因为两年里、从未付过电费。"
    "水和煤气也是一样，煤气现在使用不了。水的话，包括冲马桶的水在内，都是买来成堆的瓶装矿泉水代替使用。"
    "电什么的，已经没救了。"
    "要是用在节日里经常被使用的小型发电机的话，夸张的声音立刻会被外面听到。"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0019"
    $ current_voice = "voice/NAE04A_NAE0019.ogg"
    "绹" "「在电气公司办好手续、重新、供电？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0021"
    $ current_voice = "voice/NAE04A_DAR0021.ogg"
    "至" "「嗯ー、不、等等。要重新供电的话、工作人员不就要来吗？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0020"
    $ current_voice = "voice/NAE04A_NAE0020.ogg"
    "绹" "「啊……！」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0021"
    $ current_voice = "voice/NAE04A_NAE0021.ogg"
    "绹" "「这样、就暴露了啊」"
    "该怎么办啊……。"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0022"
    $ current_voice = "voice/NAE04A_DAR0022.ogg"
    "至" "「再说了绹酱、你还未成年，只能由监护人来办的吧」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0022"
    $ current_voice = "voice/NAE04A_NAE0022.ogg"
    "绹" "「是……这样的吗？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0023"
    $ current_voice = "voice/NAE04A_DAR0023.ogg"
    "至" "「再有、我在这儿的事情、也不想让别人知道啊」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0023"
    $ current_voice = "voice/NAE04A_NAE0023.ogg"
    "绹" "「那么、拜托留未穗姐、也不行呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0024"
    $ current_voice = "voice/NAE04A_DAR0024.ogg"
    "至" "「留未穗？　谁啊这是？　绹酱的姐姐？　巨乳？　声优？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0024"
    $ current_voice = "voice/NAE04A_NAE0024.ogg"
    "绹" "「……是桶子叔叔认识的人啊。真名、不知道吗？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0025"
    $ current_voice = "voice/NAE04A_DAR0025.ogg"
    "至" "「真名？　啊？　诶？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0025"
    $ current_voice = "voice/NAE04A_NAE0025.ogg"
    "绹" "「那个，两年前，是叫做菲利斯・喵喵这个名字」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    stop bgm 
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0026"
    $ current_voice = "voice/NAE04A_DAR0026.ogg"
    "至" "「什……么……」"
    "桶子叔叔像突然受到冲击一样瞪大了眼。"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0027"
    $ current_voice = "voice/NAE04A_DAR0027.ogg"
    "至" "「菲利斯碳的、真名……」"
    "怎么好像在抖着。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA08"),"True","lh/DAR_CSA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM10"

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0028"
    $ current_voice = "voice/NAE04A_DAR0028.ogg"
    "至" "「ＨＡＨＡＨＡ、讨厌啦。菲利斯碳没有本名哦。菲利斯碳就是菲利斯碳。不要搞错了啊？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0026"
    $ current_voice = "voice/NAE04A_NAE0026.ogg"
    "绹" "「呃……」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0029"
    $ current_voice = "voice/NAE04A_DAR0029.ogg"
    "至" "「菲利斯碳她啊、是从喵喵星来、有着猫耳的雷Ｎｅｔ人哦。永远的１７岁哦」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0027"
    $ current_voice = "voice/NAE04A_NAE0027.ogg"
    "绹" "「桶子叔叔……还好吧？」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0030"
    $ current_voice = "voice/NAE04A_DAR0030.ogg"
    "至" "「大丈夫。没问题」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB02"),"True","lh/DAR_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0031"
    $ current_voice = "voice/NAE04A_DAR0031.ogg"
    "至" "「绹酱、请记住一件事。生活中社会中、幻想有时也是必要的一部分」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0028"
    $ current_voice = "voice/NAE04A_NAE0028.ogg"
    "绹" "「哈啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0032"
    $ current_voice = "voice/NAE04A_DAR0032.ogg"
    "至" "「我啊、在那个夏天、每周都会以雷ＮｅｔＡＢ向菲利斯碳挑战哦」"
    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0033"
    $ current_voice = "voice/NAE04A_DAR0033.ogg"
    "至" "「那个时候、菲利斯碳还是不知败为何物的雷Ｎｅｔ冠军，与我的实力完全没有接点的天外之人的存在」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB07"),"True","lh/DAR_CSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0034"
    $ current_voice = "voice/NAE04A_DAR0034.ogg"
    "至" "「可是、我很幸福哦。菲利斯碳是我的……是我一个人的恋人、总是为了我、空出对战的时间」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0029"
    $ current_voice = "voice/NAE04A_NAE0029.ogg"
    "绹" "「桶子叔叔和留未穗姐是恋人吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0035"
    $ current_voice = "voice/NAE04A_DAR0035.ogg"
    "至" "「比起恋人、不如说是被悲哀的命运割裂开的二人？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0030"
    $ current_voice = "voice/NAE04A_NAE0030.ogg"
    "绹" "「是……这样啊……！」"
    "我吓了一跳。"
    "留未穗姐姐，确实是个奇怪的人。"
    "奇怪的人或许会互相吸引吧。"
    "虽然、稍微有点对留未穗姐的兴趣有点怀疑。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0036"
    $ current_voice = "voice/NAE04A_DAR0036.ogg"
    "至" "「那、为何绹酱、会知道菲利斯碳的事？」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0031"
    $ current_voice = "voice/NAE04A_NAE0031.ogg"
    "绹" "「因为，我一直寄住在留未穗姐家中」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0037"
    $ current_voice = "voice/NAE04A_DAR0037.ogg"
    "至" "「请称呼她为菲利斯碳」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0032"
    $ current_voice = "voice/NAE04A_NAE0032.ogg"
    "绹" "「诶……不要」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0038"
    $ current_voice = "voice/NAE04A_DAR0038.ogg"
    "至" "「喂、这么干脆地就拒绝了（笑）！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE04A_DAR0039"
    $ current_voice = "voice/NAE04A_DAR0039.ogg"
    "至" "「还有，绹酱，每天晚上你都和菲利斯碳睡同一张床吧。和姐姐交换了玫瑰经了吗」"
    $ stopvoc("NAE")
    play NAE "NAE04A_NAE0033"
    $ current_voice = "voice/NAE04A_NAE0033.ogg"
    "绹" "「…………？」"
    "难道是，在开玩笑吗？"
    "要是这样还是不要再和他说话了。"
    "说玩笑话也不能降温。"
    "买来的瓶装水都起雾了。"

    hide screen phoneSD1
    window hide

    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
