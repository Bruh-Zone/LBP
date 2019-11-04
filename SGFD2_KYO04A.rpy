label SGFD2_KYO04A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG02A1")
    play se "SGSE054"



    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "鼓膜被尖锐的声音所刺痛。"
    "感觉脑子里有无数片玻璃渣子那样难受。"
    "感觉视野里一瞬间有一阵波动划过，最终归于平静。"
    "就好像被那阵波动抹去了一样，脑袋里的痛苦消失了。"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0000"
    $ current_voice = "voice/KYO04A_OKA0000.ogg"
    "伦太郎" "「研究所……」"
    "就算不看周围也知道。"
    "在眼前是青梅竹马坐在那里一如既往的光景。"
    "右手握着手机。"
    "左手什么也没握。"
    "什么都没有就好。"
    "我两只手的手心也好，衣服上也好，都没有血迹。"
    "看了下手表。现在是『１７点４１分』——"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0001"
    $ current_voice = "voice/KYO04A_OKA0001.ogg"
    "伦太郎" "「时间跳跃，顺利地成功了吗……」"
    "记忆呢……？"
    "会这么想这一点，就已经说明记忆的传送也成功了。"
    "跳跃之前的事情记得很清楚。"
    "房间里到处都是的血迹也还历历在目。"
    hide screen phoneSD1
    window hide

    hide screen phonebtn
    "…………"
    window hide

    "…………"
    window hide

    "…………"
    window hide


    $ loadBG(2,"BG02A1")



    show screen phonebtn
    show screen phoneSD1
    "但是现在却看不到那些血迹。"
    "不管是在墙壁上，地板上，还是在桌上的素描簿……"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBG023A")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0000"
    $ current_voice = "voice/KYO04A_MAY0000.ogg"
    "真由理" "「呐呐冈伦、在干什么呀？」"
    "突然，从背后传来了声音——"
    play se "SGSE056"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM13"
    "回过头去看，是不知道发生了什么呆在那里的真由理。"
    "真由理……"
    "被一阵没有经过大脑的冲动所驱动，想要抱住她。"
    "但是在抱上去前一瞬间被自己阻止了。"
    "虽然没有看到血迹是在预想之中的，但这样直接确认了真由理的安全这一点，让我凝固的心又慢慢消融了。"
    "我在没有让真由理察觉到的前提下舒了一口气。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0002"
    $ current_voice = "voice/KYO04A_OKA0002.ogg"
    "伦太郎" "「说起来真由理，你现在在这里干什么呀？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0001"
    $ current_voice = "voice/KYO04A_MAY0001.ogg"
    "真由理" "「干什么……明明和冈伦一直在一起，又问了奇怪的事呢」"
    "不打算和她说什么Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ呀时间跳跃的事情。"
    "就算说了应该也理解不了吧。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0002a"
    $ current_voice = "voice/KYO04A_OKA0002a.ogg"
    "伦太郎" "「刚才头不小心撞了一下，这几个小时的记忆消失了」"
    "这么说的话真由理就……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0002"
    $ current_voice = "voice/KYO04A_MAY0002.ogg"
    "真由理" "「诶诶，没事吗？　去医生那里看看会比较……」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0003"
    $ current_voice = "voice/KYO04A_OKA0003.ogg"
    "伦太郎" "「不，没关系的，真由理哦。不是什么大问题。如果你能把那些告诉我的话，应该马上就能想起来了」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0004"
    $ current_voice = "voice/KYO04A_OKA0004.ogg"
    "伦太郎" "「那，我们是在……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0003"
    $ current_voice = "voice/KYO04A_MAY0003.ogg"
    "真由理" "「那个，我们就是在看看完成了的Ｃｏｓ服，还有想想琉华君穿着它们的样子发出『诶嘿嘿』的笑声而已」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0005"
    $ current_voice = "voice/KYO04A_OKA0005.ogg"
    "伦太郎" "「等等，难道你去过琉华子那里了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0004"
    $ current_voice = "voice/KYO04A_MAY0004.ogg"
    "真由理" "「没有，并没有去哦。因为冈伦说了『绝对不准外出』嘛」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0006"
    $ current_voice = "voice/KYO04A_OKA0006.ogg"
    "伦太郎" "「助手和桶子呢？　看起来好像不在研究所啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0005"
    $ current_voice = "voice/KYO04A_MAY0005.ogg"
    "真由理" "「恩，是不在啊。还没有回来的说。说起来，今天不是不会回来了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0006"
    $ current_voice = "voice/KYO04A_MAY0006.ogg"
    "真由理" "「桶子君说去银座看电影了哦，电话里说的」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0007"
    $ current_voice = "voice/KYO04A_MAY0007.ogg"
    "真由理" "「『叛逆的鲁路修』的剧场版，现在正在上映吧？　说是要看１８点的那一场」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0008"
    $ current_voice = "voice/KYO04A_MAY0008.ogg"
    "真由理" "「红莉栖酱呢，那个，虽然不太清楚……但是果然今晚不会回来了吧」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0007"
    $ current_voice = "voice/KYO04A_OKA0007.ogg"
    "伦太郎" "「为什么？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0009"
    $ current_voice = "voice/KYO04A_MAY0009.ogg"
    "真由理" "「生气了呀」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0008"
    $ current_voice = "voice/KYO04A_OKA0008.ogg"
    "伦太郎" "「为啥生气？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0010"
    $ current_voice = "voice/KYO04A_MAY0010.ogg"
    "真由理" "「冈伦突然说『开发评议会终止』」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0011"
    $ current_voice = "voice/KYO04A_MAY0011.ogg"
    "真由理" "「桶子君和红莉栖酱在外面买东西的途中，突然接到冈伦的电话说『开发评议会终止』……」"
    "原来如此，大致的情况我都了解了。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我为了确认这些，取出了手机，打开了收件箱。"
    window hide


    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY03"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY02"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY01"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO03A_RECV_OKA03"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO03A_RECV_OKA02"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO03A_RECV_OKA01"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO02A_RECV_MAY01"]


    "最下面有三封（正确地来说是被拆成３封的１封Ｄｍａｉｌ）是我从最初的世界线发送过来的。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_KYO03A_RECV_OKA01"]


    "另一方面，上面的三封是为了阻止火灾的发生从上一条世界线发来的。"
    "在『１５時２０分』左右收到这些邮件的我，恐怕按照邮件里的指示忠实地行动了。"
    "首先阻止了真由理去别的地方，然后给出去买东西的桶子和红莉栖打了电话，说评议会不开了。"
    "两个人会生气也是理所当然的。"
    window hide
    call hide_phone




    $ loadBG(2,"BG02A1")



    "说起来真由理应该知道诱拐的事情吧？"
    "过去的我说过『说不定会被人诱拐的所以不要出门』吧？"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "但是看真由理的样子，似乎不是这样。"
    "那天真烂漫的表情……感觉不到丝毫危机感。"
    "不对，这家伙一直都是这幅样子，所以不能通过表情来判断……"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0012"
    $ current_voice = "voice/KYO04A_MAY0012.ogg"
    "真由理" "「冈伦，御手洗团子，吃吗？」"
    "不知何时，真由理从包装袋里取出了御手洗团子。"
    "是那种便利店里很常见的３串一包的包装。"
    "３串中的一串已经被真由理握在手里了。"
    "还有两串……"
    "吃呢，还是不吃呢……"
    "…………"
    "吃吧。"

    stop bgm 
    "这么想着把手伸过去的时候，突然，我的脑海里划过某个场景。"
    "御手洗团子的鲜艳颜色，唤醒了那个场景。"
    hide screen phoneSD1
    window hide

    hide screen phonebtn
    play bgm "BGM23"
    "血——"
    "在Ｌａｂ的墙壁和地板上飞溅的鲜血——"
    "那到底是谁的血呢……？"
    window hide

    "如果真由理说的都是真的话，那么今天红莉栖和桶子都不会回Ｌａｂ了。"
    "这么想的话除了一个人之外就别无可能了。"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0009"
    $ current_voice = "voice/KYO04A_OKA0009.ogg"
    "伦太郎" "「真由理，现在马上把那些团子放好！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0013"
    $ current_voice = "voice/KYO04A_MAY0013.ogg"
    "真由理" "「诶诶、我才刚刚开始吃诶」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0010"
    $ current_voice = "voice/KYO04A_OKA0010.ogg"
    "伦太郎" "「所以已经吃过的那一串拿着也可以！　剩下的两串就放在桌子上吧！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0014"
    $ current_voice = "voice/KYO04A_MAY0014.ogg"
    "真由理" "「为什么？」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0011"
    $ current_voice = "voice/KYO04A_OKA0011.ogg"
    "伦太郎" "「因为要出门了！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0015"
    $ current_voice = "voice/KYO04A_MAY0015.ogg"
    "真由理" "「为什么啊？」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0012"
    $ current_voice = "voice/KYO04A_OKA0012.ogg"
    "伦太郎" "「不为什么！」"
    "在这里这么呆着的话，恐怕会被谁袭击吧。"
    "不对，不是恐怕。——是确定事项。"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0016"
    $ current_voice = "voice/KYO04A_MAY0016.ogg"
    "真由理" "「但是，冈伦不是说『绝对不能外出』吗？还说了两次」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0013"
    $ current_voice = "voice/KYO04A_OKA0013.ogg"
    "伦太郎" "「两次……？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0017"
    $ current_voice = "voice/KYO04A_MAY0017.ogg"
    "真由理" "「恩，第一次是冈伦的手机收到邮件的时候，第二次是真由喜的手机收到邮件的时候」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0018"
    $ current_voice = "voice/KYO04A_MAY0018.ogg"
    "真由理" "「给冈伦看了那封邮件以后，冈伦是那么说的」"
    "真由理那么说着，将手机的画面朝向我这边。"
    window hide


    $ loadBG(2,"PBG17A")






    $ loadBG(2,"PBG17B")






    $ loadBG(2,"PBG17C")



    "收件时间是『１５点２６分』。"
    "也就是我的手机收到『评议会终止』这封邮件后的４分钟。"
    "在那个时候真由理的手机，收到了这封Ｄｍａｉｌ。"
    "是的，那是由６个全角字符×３封构成的Ｄｍａｉｌ。"
    "肯定是从别的世界线的未来发送过来的。"
    "『黑万十』是什么东西？"
    "『黑Ｍａｎｊｙｕ』……『黑色的馒头(Ｍａｎｊｙｕ)』吗？"
    "不对，那样的话这个意思就不太自然了。"
    "要怎么才能和『黑色的馒头』战斗呢？"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MANJI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MANJI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MANJI"])
    "我想象了一下对着闪烁着黑色光芒的巨大温泉馒头使用着{color=#f00}卍解{/color}的自己。"
    "太超现实了，嘴角开始抽搐。"
    "然后，虽然很在意那个邮件的内容，但除那之外还有一个难以理解的地方。"
    "那就是邮件的发送者。"
    "『菲利斯酱』"
    "『菲利斯酱』是真由理对于菲利斯的称呼。"
    "为什么……？为什么那个猫娘会发送这样的Ｄｍａｉｌ……？"
    "谜……谜……谜……"
    "因为这些完全无法理解的事情，头脑中感觉一片云雾缭绕。"
    "还有一个让我混乱的要素。"
    "Ｄｍａｉｌ里写着的内容——"
    "『绝对禁止外出』"
    "『安全待机于此』"
    "这样的邮件内容让我陷入了极度的纠结状态。"
    hide screen phoneSD1
    window hide

    hide screen phonebtn
    "这样在Ｌａｂ里呆下去的话，肯定会受到谁的袭击。"
    window hide





    "但是根据菲利斯发送的Ｄｍａｉｌ来看，呆在Ｌａｂ才是安全的选择。"
    "还发送了『绝对禁止外出』这样语气强烈的信息……"
    "到底怎么做才好……？到底该怎么办……？"
    "在那个时候——"
    window hide
    play se "SGSE320"




    $ loadBG(0,"BG_BLACK")

    "突然，真由理的手机里传来了响亮的电子音。"
    "画面上出现了红色的窗口。"
    "『电池电量过低，设备将自动关闭』"
    "在那数秒后——"
    window hide


    $ loadBG(0,"BG02A1")

    show screen phonebtn
    show screen phoneSD1
    "真由理的手机沉默了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0019"
    $ current_voice = "voice/KYO04A_MAY0019.ogg"
    "真由理" "「啊、没电了呢」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0014"
    $ current_voice = "voice/KYO04A_OKA0014.ogg"
    "伦太郎" "「…………」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0020"
    $ current_voice = "voice/KYO04A_MAY0020.ogg"
    "真由理" "「说起来冈伦、御手洗团子，我再吃一串可以吗？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TARE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TARE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TARE"])
    "真由理满嘴{color=#f00}酱汁{/color}地问我。"
    "我叹了口气回答道。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0015"
    $ current_voice = "voice/KYO04A_OKA0015.ogg"
    "伦太郎" "「随你便吧……」"
    window hide


    $ loadBG(2,"BG01A")



    "总之，还有时间。"
    "感觉那时在Ｌａｂ见到的血迹并没有经过太长时间，"
    "大概惨剧发生的时间是在我进入Ｌａｂ的１５分钟或者３０分钟之前……"
    "不对，就算算的长一点１小时的话，从现在开始到那时还有４０分钟的余裕。"
    "总之我先给自己下了一个２０分钟的时间限制，也就是剩下时间的一半。"
    "在那２０分钟里，我要想好该怎么行动。"
    "是留在这里呢，还是带着真由理跑到哪里去呢……"
    "在决定之前先留在这里吧。"
    "虽然这么说，但不知道什么时候会发生什么，以防万一，先检查一遍电话微波炉（暂）兼时间机器吧。"
    "我向着开发室走去。"
    window hide


    $ loadBG(2,"BG03A4")



    "捉住了我的眼球的是一张纸片——借用书。"
    "刚刚已经被我撕得粉碎的那张纸，又出现在了桌子上。"
    "本来就该那样。这张纸的复活当然是理所当然的。"
    "因为我进行了时间跳跃啊……"
    "我又一次拿起那张讨厌的纸片。"
    window hide


    $ loadBG(2,"IBG026A",png=True)



    hide screen phonebtn
    "『甲方向乙方于本日，借出叁百万日元，乙方收到了这封借用书。』"
    "日期是今年的８月１２日。"
    "也就是昨天。"
    "好像我昨天从门音信贩那里借了３００万日元的样子。"
    "为什么……？"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0021"
    $ current_voice = "voice/KYO04A_MAY0021.ogg"
    "真由理" "「冈伦、在看什么呀？」"
    "突然传来的声音……"
    window hide
    hide background-png 




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    "抬起头来一看，出现在我面前的是真由理的脸。"
    "嘴巴里满是御手洗团子，不停地嚼着。"
    "这幅样子看来，是不会知道和这封借用书相关的事情了。"
    "我若无其事地将借用书放回了原来的敌法，用手搭着真由理的肩膀把她带回了客厅。"
    window hide


    $ loadBG(2,"BG01A")



    "为了确认是怎么回事，试着问问她吧。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0016"
    $ current_voice = "voice/KYO04A_OKA0016.ogg"
    "伦太郎" "「真由理，说起３００万日元的话，你能想到些什么吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA04"),"True","lh/MAY_CMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "一瞬间，真由理的视线呆滞了下来。"
    "与此同时，嘴巴里的咀嚼也停止了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB03"),"True","lh/MAY_CMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0022"
    $ current_voice = "voice/KYO04A_MAY0022.ogg"
    "真由理" "「那，那个，真由喜中的彩票的金额，吧？」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0017"
    $ current_voice = "voice/KYO04A_OKA0017.ogg"
    "伦太郎" "「彩票？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0023"
    $ current_voice = "voice/KYO04A_MAY0023.ogg"
    "真由理" "「不是用作Ｌａｂ的共有财产了吗。没告诉大家的时候，真由喜偷偷买的啦。很有能干的主妇的作风吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC02"),"True","lh/MAY_CMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0024"
    $ current_voice = "voice/KYO04A_MAY0024.ogg"
    "真由理" "「诶？　冈伦，刚才你是说『没有这几个小时的记忆吧』？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0025"
    $ current_voice = "voice/KYO04A_MAY0025.ogg"
    "真由理" "「彩票中奖的时间是１个月之前……那时候的事也不记得了？」"
    "唔……一如既往的很敏锐呢。"
    "那这种时候就要使用平时惯用的那一招了。"
    "我抱住头大声地叫了起来。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0018"
    $ current_voice = "voice/KYO04A_OKA0018.ogg"
    "伦太郎" "「唔哦哦哦────！　头───！　头要裂开了────！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA04"),"True","lh/MAY_CMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0026"
    $ current_voice = "voice/KYO04A_MAY0026.ogg"
    "真由理" "「怎，怎么了，冈伦！」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0019"
    $ current_voice = "voice/KYO04A_OKA0019.ogg"
    "伦太郎" "「“机关”所植入的记忆排灭集积回路(Ｒｅｃｏｌｌｅｃｔ　Ｒｅｊｅｃｔ　Ａｎｎｉｈｉｌａｔｅ)──通称Ｒ２Ａ的装置开始发动了！」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0020"
    $ current_voice = "voice/KYO04A_OKA0020.ogg"
    "伦太郎" "「想不起彩票的事情肯定也是因为那个……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0027"
    $ current_voice = "voice/KYO04A_MAY0027.ogg"
    "真由理" "「那，那样的话！　没事吗！？」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0021"
    $ current_voice = "voice/KYO04A_OKA0021.ogg"
    "伦太郎" "「是不是没事就要看你了」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0028"
    $ current_voice = "voice/KYO04A_MAY0028.ogg"
    "真由理" "「诶诶，此话怎讲！？」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0022"
    $ current_voice = "voice/KYO04A_OKA0022.ogg"
    "伦太郎" "「如果能取回被夺走的记忆的话，就能逆向向Ｒ２Ａ发送脑电波。那样的话也许就能破坏Ｒ２Ａ了」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0023"
    $ current_voice = "voice/KYO04A_OKA0023.ogg"
    "伦太郎" "「那，所以说快告诉我吧，真由理！在中了奖以后那３００万日元怎么了？」"
    "真由理握住两手，皱着眉头说。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC04"),"True","lh/MAY_CMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0029"
    $ current_voice = "voice/KYO04A_MAY0029.ogg"
    "真由理" "「那个，用掉了哦！」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0024"
    $ current_voice = "voice/KYO04A_OKA0024.ogg"
    "伦太郎" "「用在哪儿了……？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0030"
    $ current_voice = "voice/KYO04A_MAY0030.ogg"
    "真由理" "「用在未来道具魔改造计划上了……！」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0025"
    $ current_voice = "voice/KYO04A_OKA0025.ogg"
    "伦太郎" "「也就是用在了改造道具上面？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0031"
    $ current_voice = "voice/KYO04A_MAY0031.ogg"
    "真由理" "「因为，刚才不就说过了吗，本来彩票就是用Ｌａｂ的钱买的！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0032"
    $ current_voice = "voice/KYO04A_MAY0032.ogg"
    "真由理" "「所以最终打算用到Ｌａｂ上面，大家不是这么说好了吗！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0033"
    $ current_voice = "voice/KYO04A_MAY0033.ogg"
    "真由理" "「而且，如果获得了发明竞赛的大奖的话，那３００万日元不就又回来了吗！？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0034"
    $ current_voice = "voice/KYO04A_MAY0034.ogg"
    "真由理" "「也就是说，最后变成为了未来道具研究所的光明未来而做出的投资了哟！」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0035"
    $ current_voice = "voice/KYO04A_MAY0035.ogg"
    "真由理" "「啊，最后那个说法是冈伦提出的就是了……」"
    "真由理一边挥舞着御手洗团子，一边用尽了全身力气说道。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0026"
    $ current_voice = "voice/KYO04A_OKA0026.ogg"
    "伦太郎" "「顺便一提，竞赛用的道具已经提交了吗？」"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0036"
    $ current_voice = "voice/KYO04A_MAY0036.ogg"
    "真由理" "「没有，因为截止日期是８月３１日，所以说要持续改良到那天为止……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC04"),"True","lh/MAY_CMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0037"
    $ current_voice = "voice/KYO04A_MAY0037.ogg"
    "真由理" "「呐冈伦，真的没事吗……？」"
    "真由理露出不安的表情，窥视着我的脸。"
    "我用手指顶住太阳穴，轻轻地摇头说道。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0027"
    $ current_voice = "voice/KYO04A_OKA0027.ogg"
    "伦太郎" "「啊啊，已经没事了，Ｒ２Ａ好像被成功地破坏了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC02"),"True","lh/MAY_CMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0038"
    $ current_voice = "voice/KYO04A_MAY0038.ogg"
    "真由理" "「呼，太好了ー」"
    "真由理两眼发光，深深舒了口气，就好像想起来的样子将手里的团子又往嘴里送。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0039"
    $ current_voice = "voice/KYO04A_MAY0039.ogg"
    "真由理" "「啊呜」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "这样就解决了一个谜题。"
    "找到了魔改造计划的资金来源。"
    "但是，那并不是我想要知道的问题的答案。"
    window hide



    $ loadBG(0,"BG_BLACK")


    $ loadBG(2,"IBG026A",png=True)





    hide screen phonebtn
    "借用书的事情依然迷雾重重……"
    "我为什么会借那３００万日元这一点，至今仍毫无头绪。"
    "如果不是用于魔改造计划的资金的话，到底是……"
    window hide





    hide screen phonebtn
    "难道是……赎金？"
    "突然，这样的想法出现在脑海里。"
    "用于交换人质的赎金——如果那刚好是３００万日元的话……？"
    "作为一般的诱拐事件的赎金金额也太低了，但如果是以我为目标的话也不是说不过去。"
    "只是个学生的我怎么可能搞到几千万几亿日元呢。"
    "说起来，诱拐事件是最初的世界线里发生的……"
    "这条世界线上真由理并没有下落不明，所以不是人质。"
    "恩……？等等……“人质”……？"
    window hide

    stop bgm
    hide background-png 
    $ loadBG(2,"BG01A")




    show screen phonebtn
    show screen phoneSD1
    "回头的时候，真由理正在将手伸向第三串团子。"
    "是感到了我的视线了吗，真由理缓缓地把头转了过来……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0040"
    $ current_voice = "voice/KYO04A_MAY0040.ogg"
    "真由理" "「诶嘿嘿♪」"
    "有些害羞地笑了。"
    "然后将团子一口吃了进去。"
    "嘴边已经满是酱汁了……"
    "用舌尖舔着嘴边的酱汁。"
    "和那个时候并没有区别。"
    "露出幸福的微笑，吃着团子的真由理……"
    "成为了我的“人质”的那一天开始，真由理便取回了那个笑容。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    play bgm "FD2BGM05"
    hide screen phonebtn
    "真由理最喜欢的婆婆死去的时候，是她的１１岁的夏天。"
    "从那以后真由理便失去了语言与笑容。"
    "好像连别人的话都听不懂了。"
    "不管我叫几次她的名字，真由理都不会回答我。"
    window hide


    $ loadBG(0,"EVX_M06A")
    play se "SGSE068L" loop


    "那里是陵园——已经不在的婆婆的长眠之处。"
    "在超过半年的时间里，真由理每天都会去她的墓碑前。"
    "风雨无阻。"
    "虽然我那时正在上中学，但是因为担心真由理，所以有事没事就会去陵园看看。"
    "真由理总是会在那块墓石前，呆然地望着头顶上的天空。"
    "那姿态十分的空灵……就好像要消失了一样……"
    "所以我就像是为了将她留在这里一样，一遍又一遍不停地叫唤着她的名字。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0028"
    $ current_voice = "voice/KYO04A_OKA0028.ogg"
    "伦太郎" "「真由理……」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0029"
    $ current_voice = "voice/KYO04A_OKA0029.ogg"
    "伦太郎" "「……真由理？」"
    "但是真由理并没有回答我……"
    "只是握着手中的怀表，仰望着头顶上的天空……"
    $ loadBG(0,"IBGX090",png=True)
    "那怀表是婆婆的遗物。"
    "是对于真由理来说最重要的宝物……"
    "真由理无论何时都会寸不离身地带着它。"
    "有些年头的怀表——"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWAICHUH"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWAICHUH"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KWAICHUH"])
    "知道那个怀表叫做『{color=#f00}怀酱{/color}』也是很久之后的事了。"

    "那是那一天的事……那一天也下着雨。"
    "真由理撑着伞站在墓碑前，向着落雨的天空注视着。"

    stop se
    "终于雨停了，在云的之间透过一道光。"
    window hide

    stop se


    hide background-png 
    $ loadBG(2,"IBGX077")



    "云隙光——好像是被称为天使的梯子(Ａｎｇｅｌ・Ｌａｄｄｅｒ)的现象。"
    "在那幻想般庄严的景色前，我失神了。"
    "然后一阵风吹过——伞瞬间就在天空中翩翩起舞起来。"
    "但是真由理好像没有注意到伞的事。"
    "慢慢地，就好像被引诱了一样，向着倾泻下来的光线伸出了手。"
    "仿佛抓住了看不见的梯子一样……"
    "拼命地踮起脚尖……"
    "升了起来……慢慢浮了上去……"
    "这样下去要被带走了……！"
    "那样想着的我赶紧——"
    window hide
    play se "SGSE056"


    $ loadBG(2,"BG_BLACK")



    "注意到的时候，已经拉住了真由理的手背。"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0030"
    $ current_voice = "voice/KYO04A_OKA0030.ogg"
    "伦太郎" "「哪里也不会，让你去的……」"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0031"
    $ current_voice = "voice/KYO04A_OKA0031.ogg"
    "伦太郎" "「不会让你被带走的……」"
    "说出来以后，才发现自己好像说了很令人害羞的话……"
    $ stopvoc("OKA")
    play OKA "KYO04A_OKA0032"
    $ current_voice = "voice/KYO04A_OKA0032.ogg"
    "伦太郎" "「真，真由理是，我的人质啊。人体实验的对象！」"
    "好像是为了隐瞒自己的害羞，没多想就说了那样的话。"
    "那台词是我和真由理都很喜欢的特摄节目里敌人的头目经常说的话。"
    "因为敌人的头目被设定为Ｍａｄ　Ｓｃｉｅｎｔｉｓｔ，所以我很善于模仿那样的角色。"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0041"
    $ current_voice = "voice/KYO04A_MAY0041.ogg"
    "真由理" "「是吗……诶嘿」"
    "真由理在我的手腕中说道。"
    "小小的肩膀仍在颤抖着……"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0042"
    $ current_voice = "voice/KYO04A_MAY0042.ogg"
    "真由理" "「真由理原来，是人质啊……」"
    "听到了半年未曾听到的声音，有些嘶哑。"
    "但是让我感觉心情愉快……"
    $ stopvoc("MAY")
    play MAY "KYO04A_MAY0043"
    $ current_voice = "voice/KYO04A_MAY0043.ogg"
    "真由理" "「那样的话，就没办法了呢。诶嘿嘿……」"
    window hide


    $ loadBG(2,"IBGX077")



    "真由理这么说着，把头埋在了我的胸口。"
    "感觉到了眼泪的温度。"
    window hide

    stop se


    $ loadBG(2,"IBGX048")



    "于是从那天开始真由理就成为了我的“人质”。"
    "虽然成为了“人质”的真由理又取回了语言，但是仍然保持着定期去陵园的习惯。"
    "那个时候我就会和真由理一起，去她婆婆的坟前献花。"
    "然后扫墓归来的时候总是会在附近的货摊边上，两个人一起吃团子。"
    "真由理经常会吃御手洗团子——"
    "她因为感到食物的美味而张开嘴巴，脸上再次出现那一如既往的笑容。"

    window hide

    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
