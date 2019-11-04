label SGFD2_KYO06A:
    window hide


    $ loadBG(0,"BG79N6")









    hide screen phonebtn


    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "不管过了多久视线都没有停止摇晃。"
    "就好像大气中所有的热气都冒了出来一样摇晃着。"
    "在酷热的路上升起来的热气……"
    "摇晃无法消失。"
    "折射率一片混乱。"
    "也就是说……"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0000"
    $ current_voice = "voice/KYO06A_OKA0000.ogg"
    "伦太郎" "「好热……。什么呀，这股热气是……」"
    "热浪仿佛是从正上方倾注下来一样。"
    "有不好的预感……"
    "我惶惶恐恐地抬起头来，然后……"
    show screen phoneSD1
    window hide





    hide screen phonebtn
    "Ｌａｂ里大火正肆虐着。"
    play bgm "BGM08"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0001"
    $ current_voice = "voice/KYO06A_OKA0001.ogg"
    "伦太郎" "「唔哇──！　什么啊！」"
    "在窗户另一侧的火焰，比刚才更猛烈了。"
    "就算只是站在那里，肌肤上也会有灼烧感。"
    "恩……？等等……『刚才』是什么……？"
    "难道说……我又回来了吗……？"
    "已经经历过的世界线……"
    "也就是说这里是——"
    "『第２世界线』……。"
    "不可能……为什么……"
    "这种时候『近似』什么的怎么都好了。"
    "无论如何，和之前经历过的『第２世界线』是相同的情况。"
    "原因不明。"
    "到底为什么才会变成这样呢……"
    "向红莉栖的手机发送的Ｄｍａｉｌ的内容是『尾行真由理吧』。"
    "到底是怎么的因果作用下才会变成这样的啊……"
    "可恶……！"
    "总而言之——"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0002"
    $ current_voice = "voice/KYO06A_OKA0002.ogg"
    "伦太郎" "「总之不赶紧采取些行动的话──！」"
    "虽然这么说，但不知为何没有那样的实感。"
    window hide


    $ loadBG(2,"IBG044C")



    hide screen phonebtn
    $ stopvoc("Y17")
    play KUR "KYO06A_Y170000"
    $ current_voice = "voice/KYO06A_Y170000.ogg"
    "看热闹的男性" "「呐，消防车，到现在还没有来嘛？」"
    $ stopvoc("X04")
    play KUR "KYO06A_X040000"
    $ current_voice = "voice/KYO06A_X040000.ogg"
    "看热闹的女性" "「在车站附近好像也有大楼起火了，所以就都往那里赶了」"
    $ stopvoc("Y17")
    play KUR "KYO06A_Y170001"
    $ current_voice = "voice/KYO06A_Y170001.ogg"
    "看热闹的男性" "「这样下去烧到隔壁的房子也只是时间的问题了啊」"
    "耳边传来围观群众的声音……"
    "朝那边看去，真由理出现在我的眼里。"
    "真由理——真由理——！"
    "明明是这种危机情况，我在看到真由理的声音以后，胸口却莫名地激动起来。"
    "但是却发不出欢喜的声音。"
    "那是因为真由理……正在哭着。"
    "躲在路边的角落里，颤抖着肩膀。"
    "在她边上安慰着她的是红莉栖。"
    "红莉栖抱着真由理的肩膀，好像在向她说着什么。"
    "我自然地朝着那里走了过去。"
    "站到了两个人的边上。"
    "是感到了我的气息了吗，真由理缓缓地抬起头说道。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO003A"]]["Check"]=True


    $ loadBG(2,"EV_KYO003A")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0000"
    $ current_voice = "voice/KYO06A_MAY0000.ogg"
    "真由理" "「抱歉啊……冈伦……」"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0001"
    $ current_voice = "voice/KYO06A_MAY0001.ogg"
    "真由理" "「我真的……十分抱歉……」"
    "不知道现在该说些什么。"
    "在我搜肠刮肚想着怎么回答的时候，真由理继续说了下去。"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0002"
    $ current_voice = "voice/KYO06A_MAY0002.ogg"
    "真由理" "「还有……谢谢你。……」"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0003"
    $ current_voice = "voice/KYO06A_MAY0003.ogg"
    "真由理" "「刚才没能……好好说出来……」"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0004"
    $ current_voice = "voice/KYO06A_MAY0004.ogg"
    "真由理" "「谢谢你……救了我……」"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0005"
    $ current_voice = "voice/KYO06A_MAY0005.ogg"
    "真由理" "「那样下去的话……真由理肯定……会在火里……」"
    "好像我在这条世界线上也从大火里把她救出来了。"
    "渐渐确信了这里不是『第２世界线』就是『近似第２世界线』。"
    $ stopvoc("MAY")
    play MAY "KYO06A_MAY0006"
    $ current_voice = "voice/KYO06A_MAY0006.ogg"
    "真由理" "「谢谢你……谢谢你……冈伦……」"
    "真由理就这么一边不停地重复着，一边大颗大颗地流着眼泪。"
    "我什么都没有说，只是安静地将手放在她的头上，温柔地抚摸着她沾满烟尘的头发。"
    window hide



    $ loadBG(2,"BG79N6",at=[Transform(yalign=1.0)])






    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "然后，桶子出现了……"
    "桶子看着被熊熊大火吞没的Ｌａｂ，轻声低语着。"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0000"
    $ current_voice = "voice/KYO06A_DAR0000.ogg"
    "至" "「在那里的Ｓｋｅｂｏ也一起没有了啊……」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0001"
    $ current_voice = "voice/KYO06A_DAR0001.ogg"
    "至" "「冈伦，别泄气哦……」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0003"
    $ current_voice = "voice/KYO06A_OKA0003.ogg"
    "伦太郎" "「为什么我会泄气啊……」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0002"
    $ current_voice = "voice/KYO06A_DAR0002.ogg"
    "至" "「因为冈伦也很珍惜那本Ｓｋｅｂｏ，不是吗」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0003"
    $ current_voice = "voice/KYO06A_DAR0003.ogg"
    "至" "「从高中开始两个人就一起逛各种漫展啊」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0004"
    $ current_voice = "voice/KYO06A_DAR0004.ogg"
    "至" "「然后将那些一点一点收集起来的插图，放在那本素描簿里……」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0004"
    $ current_voice = "voice/KYO06A_OKA0004.ogg"
    "伦太郎" "「等等。『两个人一起』……你刚才这么说了吧？」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0005"
    $ current_voice = "voice/KYO06A_DAR0005.ogg"
    "至" "「有什么问题吗？」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0005"
    $ current_voice = "voice/KYO06A_OKA0005.ogg"
    "伦太郎" "「那两个人也就是桶子和……」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0006"
    $ current_voice = "voice/KYO06A_DAR0006.ogg"
    "至" "「当然还有冈伦你啦」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0006"
    $ current_voice = "voice/KYO06A_OKA0006.ogg"
    "伦太郎" "「不可能！　我没有去过那种活动的印象！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0007"
    $ current_voice = "voice/KYO06A_DAR0007.ogg"
    "至" "「一氧化碳中毒？　脑细胞死光了？　我和冈伦一起收集了那些插图是肯定没有错的哦」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0007"
    $ current_voice = "voice/KYO06A_OKA0007.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0008"
    $ current_voice = "voice/KYO06A_DAR0008.ogg"
    "至" "「但是不管怎样这个就要没掉了就是了，因为要拿去还钱……」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0008"
    $ current_voice = "voice/KYO06A_OKA0008.ogg"
    "伦太郎" "「等下，那两件事有什么关系吗？」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0009"
    $ current_voice = "voice/KYO06A_DAR0009.ogg"
    "至" "「什么啊？　开玩笑的吗？」"
    "说明太麻烦了。"
    "我就按照桶子刚才说的承认自己一氧化碳中毒了。"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0010"
    $ current_voice = "voice/KYO06A_DAR0010.ogg"
    "至" "「果然还是去医院比较好吧？」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0009"
    $ current_voice = "voice/KYO06A_OKA0009.ogg"
    "伦太郎" "「听了那个就去。所以告诉我吧。借钱和素描簿有什么关系？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TABOO_AUCTIONS"])
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0011"
    $ current_voice = "voice/KYO06A_DAR0011.ogg"
    "至" "「很简单啊。那个素描簿如果交给Ｔａｂｕｏｋｕ——{color=#f00}Ｔａｂｏｏ拍卖{/color}的话，刚好价值３００万呢」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0012"
    $ current_voice = "voice/KYO06A_DAR0012.ogg"
    "至" "「中标的确实是个在出版行业工作的人，名字是……那个，虽然忘了……」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0013"
    $ current_voice = "voice/KYO06A_DAR0013.ogg"
    "至" "「总而言之那个人会在今晚８点来取那个素描簿，据说会带现金来」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0014"
    $ current_voice = "voice/KYO06A_DAR0014.ogg"
    "至" "「但是因为这场火灾已经……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")


    $ loadBG(2,"IBG026A",png=True)





    hide screen phonebtn
    "原来如此"
    "如果１个月内返还借款的话，利息是０."
    "所以想着把素描簿按『３００万円』卖了的话就应该可以还钱了。"
    "没想到……"
    window hide


    $ loadBG(0,"BG79N6")






    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0010"
    $ current_voice = "voice/KYO06A_OKA0010.ogg"
    "伦太郎" "「呐桶子，说起来，我们不还钱了怎么样？」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0011"
    $ current_voice = "voice/KYO06A_OKA0011.ogg"
    "伦太郎" "「『因为利息的设定违反了法律所以没有返还的义务』助手好像这么说过？」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0015"
    $ current_voice = "voice/KYO06A_DAR0015.ogg"
    "至" "「你觉得对方是吃这一套的人吗？　＠ｃｈａｎｎｅｌ上面写的很清楚啊。」"
    "桶子这么说着取出了手机，打开了浏览器给我看。"
    "那里写着这样的话。"
    window hide


    $ loadBG(2,"PBG19A")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0012"
    $ current_voice = "voice/KYO06A_OKA0012.ogg"
    "伦太郎" "「桶子，你确定没给我看错东西吗？　这里写着『门音信贩是很良心的』啊？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_USOUSO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_USOUSO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_USOUSO"])
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0016"
    $ current_voice = "voice/KYO06A_DAR0016.ogg"
    "至" "「『{color=#f00}如果骗子都会说自己是骗子的话就没人上当了{/color}』」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0017"
    $ current_voice = "voice/KYO06A_DAR0017.ogg"
    "至" "「冈伦，你真的不记得了吗？　这个＠ｃｈａｎｎｅｌ的留言、昨夜已经给你看过了哦。那个时候你不是马上读出来了吗」"
    "稍微考虑了一下……"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0013"
    $ current_voice = "voice/KYO06A_OKA0013.ogg"
    "伦太郎" "「不对，现在不也是很快读出来了吗？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TATEYOMI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TATEYOMI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TATEYOMI"])
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0018"
    $ current_voice = "voice/KYO06A_DAR0018.ogg"
    "至" "「那是啥好恶心啊……。这可不好笑哦，冈伦……。这种东西就是要{color=#f00}竖着读{/color}的啊常考」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0014"
    $ current_voice = "voice/KYO06A_OKA0014.ogg"
    "伦太郎" "「竖着读……？　啊啊，要竖着读的啊！」"
    "听他这么一说，我终于注意到了。"
    "我又看向了桶子的手机，将每行的第一个字连起来读。"
    "『门音信反名声超不好用保险金让你沉入东京湾』"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GACHI"])
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0015"
    $ current_voice = "voice/KYO06A_OKA0015.ogg"
    "伦太郎" "「『门音信反名声超不好用保险金让你沉入东京湾！？』」"
    window hide



    $ loadBG(2,"BG79N6")






    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0019"
    $ current_voice = "voice/KYO06A_DAR0019.ogg"
    "至" "「顺便一提发现这个的是牧濑氏哦」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0020"
    $ current_voice = "voice/KYO06A_DAR0020.ogg"
    "至" "「知道冈伦从门音信贩那里借了钱以后牧濑氏就一直抱怨个不停」"
    "是吗，红莉栖她"
    "因为是＠ｃｈａｎｎｅｌ克里斯，发现这种藏头文也是很容易的吧。"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0021"
    $ current_voice = "voice/KYO06A_DAR0021.ogg"
    "至" "「然后，发现了这个信息之后，又试着调查了一下门音信贩的其他方面」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0022"
    $ current_voice = "voice/KYO06A_DAR0022.ogg"
    "至" "「然后就得到了一些零零碎碎的消息……虽说是很奇怪的传言就是了」"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0016"
    $ current_voice = "voice/KYO06A_OKA0016.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0023"
    $ current_voice = "voice/KYO06A_DAR0023.ogg"
    "至" "「冈伦，果然很不妙吧……？　这样下去的话冈伦说不定真要被灭口了……」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "沉入东京湾……"
    "沉入东京湾……"
    "好烦……"
    "我才不想被灭口呢……"
    "才不想就这么被灭口呢！"
    "那么该怎么做才好……？"
    "Ｄｍａｉｌ……？"
    "时间跳跃……？"
    "这么想着，视线又移回了眼前的大桧山大楼……"
    window hide

























    hide screen phonebtn
    show screen phoneSD1
    "火势更甚了。"
    "也就是说……"
    "这样下去很快……就会变成很糟糕的情况……？"
    "在这个时候，我终于取回了一些冷静。"
    "素描簿的事情也好，借款也好，说不定会被沉入东京湾也好，在现在怎样都好了。"
    "比起那些，现在在我眼前的是，满是我们的回忆的，我们最宝贵的圣域，正在被熊熊大火所吞没的现实！"
    "这个现实才是更加重大深刻的危机情况。"
    "因为，在火焰的里面有着电话微波炉（暂）兼时间机器。"
    "就像是偶然的产物一样被做出来的道具——"
    "要是不小心让它们变成灰的话，就没有第二次机会了。"
    "所以到底怎么做才好……！到底该怎么办……！"
    "…………"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0017"
    $ current_voice = "voice/KYO06A_OKA0017.ogg"
    "伦太郎" "「呼……怎么做都没用了吗……」"
    window hide
    play se "SGSE182"



    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "这么说着我用力跑了起来。"
    $ stopvoc("DAR")
    play DAR "KYO06A_DAR0024"
    $ current_voice = "voice/KYO06A_DAR0024.ogg"
    "至" "「什么，喂，冈伦，你要去哪！」"
    "虽然背后传来桶子的声音，但已经没有时间回答他了。"
    "我不顾别人的讶异目光，朝着二楼冲去。"
    window hide

    $ loadBG(0,"BG02N1")
    show fire zorder 200 


    show screen phonebtn
    show screen phoneSD1
    "打开大门，再次向Ｌａｂ中——"
    "不对，这已经是第三次了……"
    "不管经历过几次都无法适应。"
    "但是好像每次火都变得更大了。"
    "灼热的火舌舔着墙壁和天花板蔓延着。"
    "无法呼吸。连眼睛都无法睁开。"
    "感觉猛烈的热浪直沁心扉，内脏有一种焦灼感。"
    "但是因为下定了决心，不去不行。"
    "我抄起在一旁的白大褂，凛然地投身于热火之中。"
    "我从火海里脱身，朝着开发室——"
    window hide



    hide fire 
    $ loadBG(0,"BG03A4")









    show screen phonebtn
    show screen phoneSD1
    "冲了进去之后，电话微波炉（暂）还安然无恙地在哪里。"
    "Ｘ６８０００，键盘，显示器，头盔都在。"
    "但是在这样的环境里，内部的精密仪器损坏了也说不定。"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0018"
    $ current_voice = "voice/KYO06A_OKA0018.ogg"
    "伦太郎" "「拜托了……动起来吧……」"
    "带着祈祷的心情按下了Ｘ６８０００的电源按钮——"
    "响起了ＣＲＴ特有的启动音，显示器也亮了起来。"
    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0019"
    $ current_voice = "voice/KYO06A_OKA0019.ogg"
    "伦太郎" "「唔哈哈哈！　这也是命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择！」"
    "应该做的事只有一件。"
    "命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)在命令着我。"
    "那样的话就跳跃吧！向着过去跳跃！"
    "这里不久肯定会被大火所吞没。"
    "那样的话，在这里的机器就全灭了。"
    "机器什么的先不管，Ｌａｂ被完全烧毁成为历史事实的话我可不能允许！"
    "（会给附近人添麻烦，而且店长肯定也会把我揍个半死吧）"
    "不管原因是什么，必须要阻止这场火灾！"
    "所以为了这点除了时间跳跃以外并无他法。"
    "头脑里没有名为Ｄｍａｉｌ的选项。"
    "要问为什么的话是因为已经发过了。在这条『第２世界线』上……"
    "而结果是，虽然的确阻止了火灾，但是——"
    hide screen phoneSD1
    window hide
    with whiteflash
    $ loadBG(0,"BG02N4",over=True)

    hide screen phonebtn
    "————"
    window hide
    with whiteflash
    $ loadBG(0,"IBG023C",over=True)

    "————"
    window hide
    with whiteflash
    $ loadBG(0,"BG01N4",over=True)

    "————"
    window hide
    with whiteflash
    hide background-over 
    $ loadBG(0,"BG03A4")


    show screen phonebtn
    show screen phoneSD1
    "总而言之没有时间了，火势很快就要蔓延到这里了。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我开始敲打键盘，进行设定。"
    "时间跳跃的目标是３小时前——也就是１８０分钟。"
    "因为还没有解决真由理被诱拐相关的事。"
    "所以将那个时间也算了进去，我完成了时间的设定。"
    "…………"
    window hide

    $ loadBG(0,"BG03A4")

    show screen phonebtn
    show screen phoneSD1
    "很快完成了准备。"
    "楼下的４２寸显像管应该好好地开着。"
    "这件事在来这里之前就已经确认好了。"
    "头罩也带好了。"
    "只剩下启动时间跳跃机器了——！"
    "我一边不停地深呼吸着，一边说道。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    $ stopvoc("OKA")
    play OKA "KYO06A_OKA0020"
    $ current_voice = "voice/KYO06A_OKA0020.ogg"
    "伦太郎" "「好了，出发！」"

    window hide

    stop bgm
    show houden 

    play se "SGSE035L" loop





    stop se

    play se "SGSE067"


    play se "SGSE053L" loop

    stop se


    play se "SGSE013"

    hide screen phoneSD1
    window hide


    hide screen phonebtn
    hide houden 
    call hide_phone
    pause 2
    hide screen phonebtn
    call timeleap (fromtime=[8,13,19,40], totime=[8,13,16,40], fromday=[5])


    return




    stop se







    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
