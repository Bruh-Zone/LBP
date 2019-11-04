label SGFD2_RUK04C:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")

    play se "SGSE004L" loop


    $ date="8/31"
    $ day = "TUE"
    hide screen phonebtn
    show screen phoneSD1

    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0000"
    $ current_voice = "voice/RUK04C_MAY0000.ogg"
    "真由理" "「喂喂，琉华君！　这边哦」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0000"
    $ current_voice = "voice/RUK04C_RUK0000.ogg"
    "琉华" "「等等我，真由理酱」"
    window hide

    stop se


    $ loadBG(0,"BG_BLACK")

    play se "SGSE022"

    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0001"
    $ current_voice = "voice/RUK04C_MAY0001.ogg"
    "真由理" "「冈伦，进去了哦」"
    window hide
    play se "SGSE361"



    $ loadBG(2,"IBG054A")



    hide screen phonebtn
    play bgm "FD2BGM01"

    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0002"
    $ current_voice = "voice/RUK04C_MAY0002.ogg"
    "真由理" "「嘟嘟噜。冈伦，状态如何？」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0000"
    $ current_voice = "voice/RUK04C_OKA0000.ogg"
    "伦太郎" "「真由理，请告诉我，会有状态好的人进医院的吗」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0003"
    $ current_voice = "voice/RUK04C_MAY0003.ogg"
    "真由理" "「恩，看起来挺精神的。太好了」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0001"
    $ current_voice = "voice/RUK04C_OKA0001.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0004"
    $ current_voice = "voice/RUK04C_MAY0004.ogg"
    "真由理" "「但是，突然就受了这么重的伤，真是吓坏我了」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0002"
    $ current_voice = "voice/RUK04C_OKA0002.ogg"
    "伦太郎" "「你这家伙会听人说话嘛……恩？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0001"
    $ current_voice = "voice/RUK04C_RUK0001.ogg"
    "琉华" "「那个，冈部师傅你好」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0003"
    $ current_voice = "voice/RUK04C_OKA0003.ogg"
    "伦太郎" "「啊啊，琉华子，你来……看我了啊」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0002"
    $ current_voice = "voice/RUK04C_RUK0002.ogg"
    "琉华" "「恩」"

    "８月２１日。"
    "冈部突然受了很重的伤，把我们都吓了一跳。"
    "真是非常严重的伤啊，而且看起来像是刺伤。没准还会失血过多而死。"
    "到底发生了什么呢，冈部也不告诉我们。肯定是发生了非常了不得的事情，我是这样子想的。"

    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0005"
    $ current_voice = "voice/RUK04C_MAY0005.ogg"
    "真由理" "「但是真是太好了，好像能够动了。」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0006"
    $ current_voice = "voice/RUK04C_MAY0006.ogg"
    "真由理" "「但是暂时没法去厕所，所以尿布肯定还是要用的吧」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0004"
    $ current_voice = "voice/RUK04C_OKA0004.ogg"
    "伦太郎" "「喂，真由理！　那件事──」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0003"
    $ current_voice = "voice/RUK04C_RUK0003.ogg"
    "琉华" "「尿，尿布！？　也就是说，是真由理来换的？」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0007"
    $ current_voice = "voice/RUK04C_MAY0007.ogg"
    "真由理" "「是的哦ー」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0005"
    $ current_voice = "voice/RUK04C_OKA0005.ogg"
    "伦太郎" "「咕……」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0004"
    $ current_voice = "voice/RUK04C_RUK0004.ogg"
    "琉华" "「这，这真是不容易啊……如果告诉我的话我明明可以过来照顾的……」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0006"
    $ current_voice = "voice/RUK04C_OKA0006.ogg"
    "伦太郎" "「啥？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0005"
    $ current_voice = "voice/RUK04C_RUK0005.ogg"
    "琉华" "「不，不对！　什么都没有！　什么都……」"
    "我到底在说什么吧……"
    "就算是都是男性这样也未免……"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0008"
    $ current_voice = "voice/RUK04C_MAY0008.ogg"
    "真由理" "「对了对了，冈伦听我说听我说。琉华君已经答应下次和我一起去Ｃｏｓ了。做凯拉林酱的Ｃｏｓ哦♪」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0007"
    $ current_voice = "voice/RUK04C_OKA0007.ogg"
    "伦太郎" "「什么，这是真的吗？」"
    "真由里酱有做Ｃｏｓ服的爱好，很久之前就一直想让我穿上这样的衣服了。"
    "虽然我一直都是拒绝的。"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0009"
    $ current_voice = "voice/RUK04C_MAY0009.ogg"
    "真由理" "「是真的吧，琉华君」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0006"
    $ current_voice = "voice/RUK04C_RUK0006.ogg"
    "琉华" "「恩，恩。我很乐意哦」"

    "不是因为发生了什么。"
    "只不过，总觉得。"
    "如果这么做的话，就能改变一下自己。"
    "所以。"

    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0007"
    $ current_voice = "voice/RUK04C_RUK0007.ogg"
    "琉华" "「果然……有点奇怪吧？」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0008"
    $ current_voice = "voice/RUK04C_OKA0008.ogg"
    "伦太郎" "「不，很不错哦」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0008"
    $ current_voice = "voice/RUK04C_RUK0008.ogg"
    "琉华" "「诶？」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0009"
    $ current_voice = "voice/RUK04C_OKA0009.ogg"
    "伦太郎" "「没听到吗？我说很不错哦」"
    "真是意外啊。"
    "冈部师傅到底是闹哪样啊——到底听了些什么才会这样的。"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0010"
    $ current_voice = "voice/RUK04C_MAY0010.ogg"
    "真由理" "「琉华君，非常可爱所以肯定人气超高的」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0011"
    $ current_voice = "voice/RUK04C_MAY0011.ogg"
    "真由理" "「说不定还会上杂志哦」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0012"
    $ current_voice = "voice/RUK04C_MAY0012.ogg"
    "真由理" "「如果那样的话，我就会为你做更多的衣服哦」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0013"
    $ current_voice = "voice/RUK04C_MAY0013.ogg"
    "真由理" "「呐呐冈伦。冈伦想让琉华君穿怎样的衣服呢。真由喜的话呢……」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0014"
    $ current_voice = "voice/RUK04C_MAY0014.ogg"
    "真由理" "「下次来点男生风格的吧。但是闪亮的魔法少女也很难取舍啊……」"
    "我只不过是去Ｃｏｓ一下而已，真由理酱却说得很起劲。"
    "但是。"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0015"
    $ current_voice = "voice/RUK04C_MAY0015.ogg"
    "真由理" "「对了！冈伦，冬Ｃｏｍｉ你也一起去吧」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0010"
    $ current_voice = "voice/RUK04C_OKA0010.ogg"
    "伦太郎" "「恩恩，好的」"
    "冈部师傅说着这话，脸上越发温柔。"
    "看着这两人这幅样子，我感觉非常的——"

    stop bgm 
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0016"
    $ current_voice = "voice/RUK04C_MAY0016.ogg"
    "真由理" "「琉华君……怎么了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0009"
    $ current_voice = "voice/RUK04C_RUK0009.ogg"
    "琉华" "「诶？」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0017"
    $ current_voice = "voice/RUK04C_MAY0017.ogg"
    "真由理" "「因为，眼泪……」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0010"
    $ current_voice = "voice/RUK04C_RUK0010.ogg"
    "琉华" "「骗人……。我，在哭……」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0018"
    $ current_voice = "voice/RUK04C_MAY0018.ogg"
    "真由理" "「没事吧？　是哪里痛吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0011"
    $ current_voice = "voice/RUK04C_RUK0011.ogg"
    "琉华" "「不是哦。不是这样的，虽然不是这样……」"
    "到底是怎么了呢。"
    "眼泪停不下来——"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0012"
    $ current_voice = "voice/RUK04C_RUK0012.ogg"
    "琉华" "「那，那个……我去削个苹果！」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0019"
    $ current_voice = "voice/RUK04C_MAY0019.ogg"
    "真由理" "「……真的没事吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0013"
    $ current_voice = "voice/RUK04C_RUK0013.ogg"
    "琉华" "「恩，放心吧。没问题的」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0020"
    $ current_voice = "voice/RUK04C_MAY0020.ogg"
    "真由理" "「那样的话好吧……」"
    "这并不是难过。"
    "虽然我自己也不是很清楚但是我。"
    window hide


    $ loadBG(2,"BG_BLACK")




    "感觉还是非常的幸福。"

    window hide

    $ loadBG(0,"IBGX048")

    play se "SGSE004L" loop

    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0021"
    $ current_voice = "voice/RUK04C_MAY0021.ogg"
    "真由理" "「那么就下次再见了，真由喜会再来的。要好好地听护士的话哦」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0011"
    $ current_voice = "voice/RUK04C_OKA0011.ogg"
    "伦太郎" "「不用每次都说了，又不是小孩子知道的啦」"
    "伤势虽然已经没有大碍了，但伤势还是比想象中的要严重。冈部师傅想要出院的话估计还是要花一段时间。"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0014"
    $ current_voice = "voice/RUK04C_RUK0014.ogg"
    "琉华" "「…………」"
    "这天，我刚好想起了向冈部师傅说的话。"
    "到现在为止都因为没找到时机而没能说出来。"
    "但是正因为今日是。"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0012"
    $ current_voice = "voice/RUK04C_OKA0012.ogg"
    "伦太郎" "「琉华子。你可以不要忘记了你的修行哦。清心斩魔流可是每天都必须练的。」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0015"
    $ current_voice = "voice/RUK04C_RUK0015.ogg"
    "琉华" "「啊！好的。」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0022"
    $ current_voice = "voice/RUK04C_MAY0022.ogg"
    "真由理" "「那就再见了，冈伦」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0013"
    $ current_voice = "voice/RUK04C_OKA0013.ogg"
    "伦太郎" "「恩」"

    "正因为今天是！"

    window hide

    stop se


    $ loadBG(2,"IBG054A")



    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0016"
    $ current_voice = "voice/RUK04C_RUK0016.ogg"
    "琉华" "「那个，冈，冈部师傅！！」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0014"
    $ current_voice = "voice/RUK04C_OKA0014.ogg"
    "伦太郎" "「恩？」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0023"
    $ current_voice = "voice/RUK04C_MAY0023.ogg"
    "真由理" "「怎么了，琉华君？」"

    "我一直在想的事。"

    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0017"
    $ current_voice = "voice/RUK04C_RUK0017.ogg"
    "琉华" "「我有件事想要拜托冈部师傅」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0015"
    $ current_voice = "voice/RUK04C_OKA0015.ogg"
    "伦太郎" "「什么事？」"

    "我想拜托的事。"
    "那是……"

    show screen phoneSD1
    play bgm "FD2BGM09"

    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0018"
    $ current_voice = "voice/RUK04C_RUK0018.ogg"
    "琉华" "「请让我……请让我加入Ｌａｂ！」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0016"
    $ current_voice = "voice/RUK04C_OKA0016.ogg"
    "伦太郎" "「什么？」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0019"
    $ current_voice = "voice/RUK04C_RUK0019.ogg"
    "琉华" "「我一直非常羡慕，非常希望和大家一起作为Ｌａｂ的一员度过快乐的时光。」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0020"
    $ current_voice = "voice/RUK04C_RUK0020.ogg"
    "琉华" "「虽然到现在为止都不能够很好地说出来……但是已经下定决心鼓起勇气说出来了。」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0021"
    $ current_voice = "voice/RUK04C_RUK0021.ogg"
    "琉华" "「虽然我觉得我可能什么都没法做到，但是……」"

    "已经不能说的事"
    "已经做不到的事。"
    "但是如果一直这样下去的话是不行的。"
    "如果不鼓起勇气的话是不行的。"

    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0017"
    $ current_voice = "voice/RUK04C_OKA0017.ogg"
    "伦太郎" "「琉华子……」"

    "虽然我还不是很有自信。"
    "但是至少能够改变点什么。"

    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0022"
    $ current_voice = "voice/RUK04C_RUK0022.ogg"
    "琉华" "「拜托了，冈部师傅！请让我加入Ｌａｂ！！」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0018"
    $ current_voice = "voice/RUK04C_OKA0018.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0024"
    $ current_voice = "voice/RUK04C_MAY0024.ogg"
    "真由理" "「冈伦？」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0019"
    $ current_voice = "voice/RUK04C_OKA0019.ogg"
    "伦太郎" "「是吗……本来打算出院了以后就告诉你的……」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0020"
    $ current_voice = "voice/RUK04C_OKA0020.ogg"
    "伦太郎" "「琉华子，你已经，而且很久之前就是我们的伙伴——Ｌａｂｍｅｍ了」"

    "那么说着的冈部师傅非常的温柔。"
    "所以我。"

    show screen phoneSD1
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK005A"]]["Check"]=True


    $ loadBG(2,"EV_RUK005A")



    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0023"
    $ current_voice = "voice/RUK04C_RUK0023.ogg"
    "琉华" "「非，非常感谢！　我好高兴啊！　超开心！」"

    "想要忍住眼泪真是困难啊。"

    $ stopvoc("MAY")
    play MAY "RUK04C_MAY0025"
    $ current_voice = "voice/RUK04C_MAY0025.ogg"
    "真由理" "「太棒了，这样的话琉华君也是Ｌａｂｍｅｍ了呢」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0024"
    $ current_voice = "voice/RUK04C_RUK0024.ogg"
    "琉华" "「恩！鼓起勇气真是太棒了呢」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0021"
    $ current_voice = "voice/RUK04C_OKA0021.ogg"
    "伦太郎" "「呼……让我告诉你吧，琉华子。你很坚强。你比你想象中的要坚强的多」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0025"
    $ current_voice = "voice/RUK04C_RUK0025.ogg"
    "琉华" "「我很……坚强？」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0022"
    $ current_voice = "voice/RUK04C_OKA0022.ogg"
    "伦太郎" "「是啊……」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0026"
    $ current_voice = "voice/RUK04C_RUK0026.ogg"
    "琉华" "「冈部师傅……」"

    "就凭这句话，好像我就能够变强了呢。"


    stop bgm 
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0023"
    $ current_voice = "voice/RUK04C_OKA0023.ogg"
    "伦太郎" "「虽然还有一件想说的事情……」"
    $ stopvoc("OKA")
    play OKA "RUK04C_OKA0024"
    $ current_voice = "voice/RUK04C_OKA0024.ogg"
    "伦太郎" "「我的名字是凤凰院凶真！　不要随随便便地就忘了！」"
    $ stopvoc("RUK")
    play RUK "RUK04C_RUK0027"
    $ current_voice = "voice/RUK04C_RUK0027.ogg"
    "琉华" "「好的，冈……凶真师傅！」"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn

    play bgm "BGM05"

    "时已至夏末，秋天终究如期而至。"
    "在那之后，好像会发生很多不错的事情。"
    "不知为何我有些高兴起来了。"


    hide screen phoneSD1
    window hide

    stop bgm 
    scene expression Solid("000000")  with Fade(3,3,1)
    show screen invisible
    $ renpy.movie_cutscene("video/imv11.avi")
    hide screen invisible
    "「迷宫错综的雌雄共体·完成」"




    hide screen phonebtn
    scene expression Solid("000000")  with fade

    return
