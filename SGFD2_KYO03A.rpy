label SGFD2_KYO03A:
    window hide



    hide screen phonebtn
    scene expression Solid("000000")  with fade
    $ loadBG(0,"BG21N2")


    python:
        RcvMail(26)
        ReadMail(26)
        RcvMail(25)
        ReadMail(25)
        RcvMail(24)
        ReadMail(24)
    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "世界在摇晃……视野在摇晃……"
    "就好像心中的邪恶小人在大脑中央肆无忌惮地折腾一样。"
    "没关系，只是普通的眩晕而已。很快就会好的。"
    "我等待着眩晕退去，缓缓地环顾四周。"
    show screen phonebtn
    show screen phoneSD1
    "在眼前站着的是一个不认识的男性。"
    "这家伙是，谁啊……"
    "虽然完全没有见过的影响，但是他一直朝着这边看。"
    "不知为何有些心情不好。"
    "感觉还是别和他扯上关系为妙。"
    "这么想着，我立刻就离开了他的面前。"
    play bgm "BGM25"
    "再次调整视线。"
    "是在大楼的前面的……投币式保险柜吗。"
    "和之前一样，对于自己会在这里的原因完全不清楚。"
    "但是“Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ”发动了这一点是确确实实的——"
    "世界线已经改变了。"
    "在那个时候，我的目光停在了保险柜的一角。"
    window hide


    $ loadBG(2,"BG21N2R")



    "左下角的保险柜的门微开着。"
    "仿佛被吸引了一般，我走了过去。"
    "蹲下身子，朝里面看去。"
    window hide


    $ loadBG(2,"IBG025A",png=True)



    hide screen phonebtn
    "空的……"
    "里面什么也没有。"
    "所以……该说什么呢？"
    "保险柜什么的，怎样都好了。"
    window hide



    $ loadBG(3,"BG21N2")
    hide background-png 



    show screen phonebtn
    "比起那个Ｌａｂ怎样了！"
    "必须赶快确认Ｌａｂ的情况！"
    "这么想着，朝Ｌａｂ方向跑去了。"
    $ stopvoc("Y15")
    play KUR "KYO03A_Y150000"
    $ current_voice = "voice/KYO03A_Y150000.ogg"
    "新一" "「啊，等等……！」"
    "是刚才的那个男的吗，好像在从背后叫我的样子，但是我没有在意。"
    "我没有回头，继续向前。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG39N")

    show screen phonebtn
    show screen phoneSD1
    "１９点３１分——来到了显像管工房前。"
    "用手扶着膝盖，我调整了一下呼吸，然后慢慢地抬起头。"

    window hide


    $ loadBG(2,"BG79N3",at=[Transform(yalign=0.5)])




    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0000"
    $ current_voice = "voice/KYO03A_OKA0000.ogg"
    "伦太郎" "「消失了……。火灾……消失了……」"
    "窗户的另一侧并没有飘动的火光。"
    "周围没有看热闹的人，Ｍｒ．布朗也在店里什么事都没有的样子看着４２寸显像管电视里的综艺节目。"
    "呼……我扶着胸口深深地舒了一口气。"
    "擦去额头上的汗水，我登上了Ｌａｂ的阶梯。"

    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG01N4")
    play se "SGSE024"


    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0001"
    $ current_voice = "voice/KYO03A_OKA0001.ogg"
    "伦太郎" "「我回来──」"
    show screen phonebtn
    "『了』……在说出那个字之前就察觉到了怪异的气氛。"
    "走进Ｌａｂ的时候，我几乎被吓得六神无主。"
    hide screen phoneSD1
    window hide
    $ loadBG(0,"IBG023C")















    play se "SGSE013"











    play se "SGSE013"


















    show screen phoneSD1
    play bgm "BGM21"

    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0002"
    $ current_voice = "voice/KYO03A_OKA0002.ogg"
    "伦太郎" "「这──这是、什么啊……」"
    window hide


    $ loadBG(2,"BG02N4")



    "室内到处飞溅着红色的鲜血。"
    "血迹还尚未干透，一片潮湿而鲜艳的感觉。"
    "冷静下来，冷静下来，仔细想想……"
    "到底发生了什么呢……"
    "我在之前的世界线上发送了Ｄｍａｉｌ，于是移动到了现在的世界线上。"
    "结果便是，开发评议会被终止，而Ｌａｂ也没有发生火灾。"
    "然而作为代价……"
    "代价……"
    "————"

    $ loadBG(2,"IBG023C")
    play se "SGSE013"


    "————"
    "————"
    window hide


    $ loadBG(2,"BG01N4")



    "看了看手表。现在的时间是『１９点３４分』——"
    "难道说……是Ｒｏｕｎｄｅｒ的袭击……！？"
    "不对，不是这样。应该不会是这样的，应该……"
    "那是别的世界线的事情。"
    "那样的话这里大片的血迹是怎么回事……？"
    "到底是谁的血……？"
    window hide


    $ loadBG(2,"BG02N4")



    "说起来，各位Ｌａｂｍｅｍ都在哪里？"
    "室内没有人影。"
    "真由理也好，红莉栖也好，桶子也不在。"
    window hide


    $ loadBG(2,"BG03A4")



    "跑进开发室里一看，果然那里也空无人影。"
    "３个人都不见了。"
    "开发室里没有血迹。"
    "但是有一件，没有印象的东西。"
    "在桌子上放着的一张纸片……"
    "我将其拿起来，仔细看了看。"
    "那里记载着这样的内容。"
    window hide


    $ loadBG(2,"IBG026A",png=True)



    hide screen phonebtn
    "借用书"
    "门音信贩有限公司（以下称为甲方）和，冈部伦太郎（以下称为乙方），缔结了如下的金钱消费借贷契约。"
    "第一条　甲方向乙方于本日，借出叁百万日元，乙方收到了这封借用书。"
    "第二条　乙方必须在平成２３年８月１１日之前，向甲方将前条所提的叁百万日元及利息全部偿还。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TOICHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TOICHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TOICHI"])
    "第三条　利息计算方法为，直到平成２２年９月１１日为止不收取任何利息，从９月１２日起{color=#f00}每十天收取１０％的复利{/color}。"
    "平成２２年８月１２日"
    hide screen phoneSD1
    window hide
    hide background-png 


    $ loadBG(0,"BG_BLACK")

    "在下面的『借主（乙）』的下面，前者我的名字，还有指印。"
    "『冈部伦太郎』的笔迹无疑是出自我手。"
    window hide


    $ loadBG(0,"BG03A4")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0003"
    $ current_voice = "voice/KYO03A_OKA0003.ogg"
    "伦太郎" "「不可能！　三百万日元！？　我可没有借过那么多钱的印象！」"
    play se "SGSE318"

    "我生气地咆哮着，将借用书撕得粉碎丢进了垃圾箱。"

    stop bgm 
    "在那时候——"
    "我才发现了我自己身上的异变。"
    play bgm "BGM23"
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0004"
    $ current_voice = "voice/KYO03A_OKA0004.ogg"
    "伦太郎" "「血……。是血……」"
    "我两手都沾满了血。"
    "而且不光光是手里。"
    "仔细看一下的话，衣服的各个地方也留着已经变成深红色的血液。"
    "这是什么啊……这是，什么啊……"
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我战战兢兢地取出了手机。"
    "总之先确认Ｌａｂｍｅｍ的安全。"
    "用晃动的指尖操作着手机，我首先给真由理打了电话。"
    window hide



    "…………"
    "没有声音……没有拨通的声音。"

    "然后便是机械的语音信箱提示。"

    $ stopvoc("Y16")
    play KUR "KYO03A_Y160000"
    $ current_voice = "voice/KYO03A_Y160000.ogg"
    "自动语音回复" "「您拨打的电话暂时无人接听，请在提示音之后留言」"

    play se "SGSE071"

    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0005"
    $ current_voice = "voice/KYO03A_OKA0005.ogg"
    "伦太郎" "「是我！　真由理、火速联系我！」"
    window hide


    call hide_phone
    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "在那之后，我又给红莉栖和桶子打了电话，但结果都是一样的。"
    "没有拨通的声音，从手机里传来的只有机械的自动语音信箱的提示声。"
    window hide


    $ loadBG(2,"BG03A4")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0006"
    $ current_voice = "voice/KYO03A_OKA0006.ogg"
    "伦太郎" "「可恶！　到底怎么了！」"
    play se "SGSE319"

    "焦躁得让我忍不住踢了一脚附近的柜子。"
    "连拨通的声音都没有就说明，手机没有电了，或者是没有信号了，还是已经……"
    hide screen phoneSD1
    window hide

    hide screen phonebtn
    "————"
    window hide

    "————"
    window hide

    "————"
    window hide


    show screen phonebtn
    show screen phoneSD1
    "我摇了摇头，摆脱了那些无聊的想法，无意中向桌子下面看了一眼。"
    window hide


    $ loadBG(2,"BG03A4D1")



    hide screen phonebtn
    "在那里放着的是电话微波炉（暂）兼时间跳跃机器。"
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0007"
    $ current_voice = "voice/KYO03A_OKA0007.ogg"
    "伦太郎" "「跳跃吧……」"
    "立刻就下了决断。"
    "想尽快知道发送了Ｄｍａｉｌ之后到底发生了什么。"
    "就算曾经一度避开了惨剧的发生，也不能保证第二次第三次相同的惨剧就还能避开。"
    "这一点已经被我在其他的世界线上的经历所证实……"
    "所以——跳跃吧！来进行Ｔｉｍｅ　Ｌｅａｐ吧！"
    "为了阻止在这Ｌａｂ发生的什么，从根本上解决问题。"
    "除此以外就没有能让事态好转的方法了，我如此想到。"
    "红莉栖说过时间机器还是残次品，因此有记忆输送失败的可能性，所以这次也不例外。"
    "有值得一试的价值。"
    "为了阻止事态朝最坏的情况发展……"
    "我无论如何也要进行跳跃！"
    window hide


    $ loadBG(2,"BG03A4")



    show screen phonebtn
    "启动了Ｘ６８０００，设定好了参数。"
    "恐怕是因为魔改造计划的关系，不光光Ｄｍａｉｌ的性能提高了，时间跳跃的机能也得到了提升……"
    "『＃１２０』"
    "１２０分钟前——我打算前往２小时前。"
    "１小时太近了，而３小时又太远。"
    "所以选择了在此之间的时间。"
    "带上头罩。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "瞬间，心头掠过一丝记忆再度消失的不安，但我闭上了眼睛之后，那份不安就消失了。"
    "已经下了决心了，不会回头。"

    window hide


    $ loadBG(2,"BG03A4")



    show screen phonebtn
    show screen phoneSD1
    "好了准备就绪，接下来就是启动装置。"
    window hide
    show houden 

    play se "SGSE035L" loop

    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)








    "我高举右手，大声宣布道。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZURVAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZURVAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ZURVAN"])
    $ stopvoc("OKA")
    play OKA "KYO03A_OKA0008"
    $ current_voice = "voice/KYO03A_OKA0008.ogg"
    "伦太郎" "「出来吧、{color=#f00}祖尔宛{/color}！　服从我们的契约！　将我引向过去时空的冥界之门吧！」"
    call hide_phone

    window hide




    stop bgm 

    stop se

    play se "SGSE067"


    play se "SGSE053L" loop

    stop se


    play se "SGSE013"

    hide screen phoneSD1
    window hide


    hide screen phonebtn
    hide houden 
    call timeleap (fromtime=[8,13,19,40], totime=[8,13,17,40], fromday=[5])



    return







    hide screen phonebtn
    scene expression Solid("000000")  with fade

    return
