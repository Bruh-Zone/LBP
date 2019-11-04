label SGFD2_KYO08B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX072")


    $ date="8/13"
    hide screen phonebtn
    show screen phoneSD1

    play bgm "BGM19"
    "吹雪的哥哥『长濑新一』是在典当屋工作的Ｃｏｓｐｌａｙｅｒ。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    "吹雪好像是因为之前真由理因为有Ｃｏｓｐｌａｙ作为共同爱好而认识的好友。"
    "去拜访这位新一君好像是一个月之前的事。"
    "目的是筹钱——"
    "为了能够让『未来道具魔改造计划』顺利进行，想要向他们借３００万日元，真由理是这么拜托的。"
    "当然当铺不是银行，不可能随意地借钱给给别人。"
    window hide


    $ loadBG(2,"IBGX090",png=True)



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHICHIGUSA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHICHIGUSA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHICHIGUSA"])
    "&c$W(LR_TIPS1);&rs于是向真由理收取了抵押品——也就是『怀酱』。"
    window hide





    "但是这个怀表就算再怎么古老，也不会值３００万日元。"
    "于是新一就撒了一个谎。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    "『这确实是个非常厉害的怀表呢。确实价值３００万元左右吧。但是因为比较贵所以请你等一下』"
    "这么说着，新一去了银行，设法借到了３００万日元。"
    "也就是打落牙齿往肚子里吞嘛……"
    "顺便一提这些事情真由理到现在也不知道。"
    "还以为３００万日元是从典当屋里借的。"
    "我从新一那里听说这些的时候，真由理并不在场。"
    "因为是男人之间的谈话，所以就让真由理先回去了。"
    window hide

    $ loadBG(0,"IBGX072")

    show screen phoneSD1
    "那么，话说回来。"
    "从那天起过了一个月，也就是到了昨天『８月１２日』。"
    "『那３００万元并不是真由理中了彩票得到的，而是用自己的怀表作为抵押换来的钱』"
    "得到了这个情报的我带着从门音信贩那里借来的３００万日元，来到了新一工作的典当屋……的样子。"
    "在那里我将钱交给新一，想让他将『怀酱』还回来。"
    "但是怀表并不在典当屋，而是在新一自己家里。"
    "新一因为自己的谎话被发现了，就惊恐地收下了钱，然后告诉我『怀表一定会亲自还给真由理的，所以就请先回吧』。"
    "当然那个时候我对于这样的说法无法接受。"
    "在那个地方耗了２，３个小时……"
    "最后结果却是在听了新一说的某些话以后，两手空空的回来了。"
    window hide


    $ loadBG(2,"IBG044A")



    "然后就到了今天『８月１３日』——"
    "新一好像是为了将怀表还给真由理，和她约定了碰头的时间。"
    "约好的时间是『１６点３０分』……"
    "但是等了一会以后发现，真由理并没有出现在约好的地方。"
    "当然了啊。读了那两封Ｄｍａｉｌ的我，阻止了真由理的外出。"
    "电话也打不通，邮件发了也没有回复。"
    "那是因为真由理的手机没有电了，所以才联系不上的啊。"
    "这里正常的想法应该是『那明天或者后天还给她就行了』，但新一却没有这么想。"
    "因为昨天我说过『这个怀表对于真由理来说，是非常重要的东西』这样恳切的话语。"
    "所以新一认为无论如何今天一定要把怀表还给真由理。"
    "所以因此来到了Ｌａｂ——"
    "说是以前从真由理那里听说过她常常泡在这个Ｌａｂ里。"
    window hide



    $ loadBG(2,"BG05N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"SHI_BMA01"),"True","lh/SHI_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0000"
    $ current_voice = "voice/KYO08B_OKA0000.ogg"
    "伦太郎" "「原来如此，这样就说得通了」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0001"
    $ current_voice = "voice/KYO08B_OKA0001.ogg"
    "伦太郎" "「也就是说你是为了将怀表还给真由理才到这个Ｌａｂ来的？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150000"
    $ current_voice = "voice/KYO08B_Y150000.ogg"
    "新一" "「不对，正确地来说是因为要将怀表还给她这件事才来的。」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0002"
    $ current_voice = "voice/KYO08B_OKA0002.ogg"
    "伦太郎" "「有什么不对的？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150001"
    $ current_voice = "voice/KYO08B_Y150001.ogg"
    "新一" "「稍微不太一样」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0003"
    $ current_voice = "voice/KYO08B_OKA0003.ogg"
    "伦太郎" "「唔……嘛算了」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0004"
    $ current_voice = "voice/KYO08B_OKA0004.ogg"
    "伦太郎" "「说起来那些家伙都是谁？穿着黑斗篷的那些……虽然你也是这幅派头，但为什么会穿成那样啊？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150002"
    $ current_voice = "voice/KYO08B_Y150002.ogg"
    "新一" "「那些人都是我的Ｃｏｓ伙伴。虽然不是和我妹一个圈子的就是了」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150003"
    $ current_voice = "voice/KYO08B_Y150003.ogg"
    "新一" "「然后，因为那个Ｃｏｓ服是为了明后天的夏Ｃｏｍｉ准备的，椎名做出来的衣服……」"
    "果然是这样啊……"
    "那样的话好像做了很对不起真由理的事情呢。"
    "我有些后悔让那些衣服上面沾满血迹了。"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0005"
    $ current_voice = "voice/KYO08B_OKA0005.ogg"
    "伦太郎" "「但是，在街上没必要穿成那样吧，难道那些是你们平时穿的衣服？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150004"
    $ current_voice = "voice/KYO08B_Y150004.ogg"
    "新一" "「当然不是这样」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0006"
    $ current_voice = "voice/KYO08B_OKA0006.ogg"
    "伦太郎" "「那为什么……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150005"
    $ current_voice = "voice/KYO08B_Y150005.ogg"
    "新一" "「我们到这里来是找椎名的。我告诉大家“我想要找到椎名”……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150006"
    $ current_voice = "voice/KYO08B_Y150006.ogg"
    "新一" "「于是大家就分头去找了。但是秋叶原这么大，不可能轻易地找到吧？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150007"
    $ current_voice = "voice/KYO08B_Y150007.ogg"
    "新一" "「于是我就说『那我们试着换个方式来找吧』，结果就变这样了……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0007"
    $ current_voice = "voice/KYO08B_OKA0007.ogg"
    "伦太郎" "「所以才会穿着这么显眼的衣服……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150008"
    $ current_voice = "voice/KYO08B_Y150008.ogg"
    "新一" "「穿着这样的衣服，以为能被人认出来是椎名做的，就能找到她了……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150009"
    $ current_voice = "voice/KYO08B_Y150009.ogg"
    "新一" "「但结果没找到，最后来到了这个Ｌａｂ……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0008"
    $ current_voice = "voice/KYO08B_OKA0008.ogg"
    "伦太郎" "「那那辆车呢……？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150010"
    $ current_voice = "voice/KYO08B_Y150010.ogg"
    "新一" "「刚才不是有个拿着长剑的家伙吗？就是他的车」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150011"
    $ current_voice = "voice/KYO08B_Y150011.ogg"
    "新一" "「那家伙，一激动起来就是控制不住自己的那种人。……想必你也很清楚了吧。」"
    window hide


    $ loadBG(2,"IBG044A")



    hide screen phonebtn
    "不知何时头上早已繁星点点。"
    "是我的错觉吗，感觉现在看到的天空比别的世界线更加的澄澈。"
    window hide



    $ loadBG(2,"BG05N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"SHI_BMA01"),"True","lh/SHI_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0009"
    $ current_voice = "voice/KYO08B_OKA0009.ogg"
    "伦太郎" "「那么……差不多该把“惯例物品”还给我了吧」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150012"
    $ current_voice = "voice/KYO08B_Y150012.ogg"
    "新一" "「惯例物品……？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0010"
    $ current_voice = "voice/KYO08B_OKA0010.ogg"
    "伦太郎" "「不是明摆着吗？　怀表啊」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150013"
    $ current_voice = "voice/KYO08B_Y150013.ogg"
    "新一" "「那个……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150014"
    $ current_voice = "voice/KYO08B_Y150014.ogg"
    "新一" "「其实不在这里」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0011"
    $ current_voice = "voice/KYO08B_OKA0011.ogg"
    "伦太郎" "「什么……！」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150015"
    $ current_voice = "voice/KYO08B_Y150015.ogg"
    "新一" "「今晚，无论如何必须要参加一个认识的人的守夜……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0012"
    $ current_voice = "voice/KYO08B_OKA0012.ogg"
    "伦太郎" "「虽然那真是非常的遗憾啊，但是这件事和还不了怀表有什么关系啊！」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150016"
    $ current_voice = "voice/KYO08B_Y150016.ogg"
    "新一" "「刚才觉得今天见不到真由理了。在约好的地点看不到，也联系不上她……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150017"
    $ current_voice = "voice/KYO08B_Y150017.ogg"
    "新一" "「但是，无论如何今天一定要把怀表还给她……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150018"
    $ current_voice = "voice/KYO08B_Y150018.ogg"
    "新一" "「所以……就放到保险柜里去了」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150019"
    $ current_voice = "voice/KYO08B_Y150019.ogg"
    "新一" "「大楼前面的……投币式保险柜里……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0013"
    $ current_voice = "voice/KYO08B_OKA0013.ogg"
    "伦太郎" "「你说——什么！　为什么要那么做啊！」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150020"
    $ current_voice = "voice/KYO08B_Y150020.ogg"
    "新一" "「不是已经说了么。我以为今天见不到她了。」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150021"
    $ current_voice = "voice/KYO08B_Y150021.ogg"
    "新一" "「虽然见不到，但是还是绝对想要在今天还给她的……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150022"
    $ current_voice = "voice/KYO08B_Y150022.ogg"
    "新一" "「那个时候，就在想该怎么办呢……？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0014"
    $ current_voice = "voice/KYO08B_OKA0014.ogg"
    "伦太郎" "「……？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150023"
    $ current_voice = "voice/KYO08B_Y150023.ogg"
    "新一" "「看这里」"
    "新一这么说着从口袋里取出手机。"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150024"
    $ current_voice = "voice/KYO08B_Y150024.ogg"
    "新一" "「万一就算找了很久还是没有找到她的话，就打算发送这封邮件」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150025"
    $ current_voice = "voice/KYO08B_Y150025.ogg"
    "新一" "「当然还没有发送，但是内容是这样的」"
    "我看向了他的手机画面。"
    "上面这么写着。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG21A",over=True)



    hide screen phonebtn
    "『椎名存放在我这里的惯例物品，放在了大楼前的Ｌｏｃｋｅｒ里了。Ｌｏｃｋｅｒ的编号是００５。钥匙我用胶带贴在下面了。』"
    "感觉见过的文章……"
    "不可能忘记。"
    "这是……"
    "…………"
    window hide
    hide background-over 





    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0015"
    $ current_voice = "voice/KYO08B_OKA0015.ogg"
    "伦太郎" "「呐，有一件事想问一下……。你的手机邮箱地址的账户名是什么……？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150026"
    $ current_voice = "voice/KYO08B_Y150026.ogg"
    "新一" "「为什么要问那种事……？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0016"
    $ current_voice = "voice/KYO08B_OKA0016.ogg"
    "伦太郎" "「所以说拜托了，请告诉我吧」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150027"
    $ current_voice = "voice/KYO08B_Y150027.ogg"
    "新一" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0017"
    $ current_voice = "voice/KYO08B_OKA0017.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150028"
    $ current_voice = "voice/KYO08B_Y150028.ogg"
    "新一" "「是『ｉ_ｃｈａｉｎ_ｈｉｓ_ｓｎａｋｅ』……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0018"
    $ current_voice = "voice/KYO08B_OKA0018.ogg"
    "伦太郎" "「意思是……？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150029"
    $ current_voice = "voice/KYO08B_Y150029.ogg"
    "新一" "「诶？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0019"
    $ current_voice = "voice/KYO08B_OKA0019.ogg"
    "伦太郎" "「我在问你那个账户名的意思！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ANAGRAM"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ANAGRAM"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ANAGRAM"])
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150030"
    $ current_voice = "voice/KYO08B_Y150030.ogg"
    "新一" "「意思，什么的，并没有啊……。只是单纯的{color=#f00}字母重排{/color}而已」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150031"
    $ current_voice = "voice/KYO08B_Y150031.ogg"
    "新一" "「我的名字是ＮＡＫＡＳＥ　ＳＨＩＮＩＣＨＩ」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150032"
    $ current_voice = "voice/KYO08B_Y150032.ogg"
    "新一" "「重新排列一下就变成『Ｉ　ＣＨＡＩＮ　ＨＩＳ　ＳＮＡＫＥ』了」"
    "ＮＡＫＡＳＥＳＨＩＮＩＣＨＩ\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓\nＩＣＨＡＩＮＨＩＳＳＮＡＫＥ"
    "我大惊失色。"
    "感觉整个人都不好了"
    "同时又感觉——豁然开朗。"
    "无数的碎片在我心中闪闪发光。"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0020"
    $ current_voice = "voice/KYO08B_OKA0020.ogg"
    "伦太郎" "「是吗……。是这么一回事么……」"
    window hide

    stop bgm 


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "那一瞬间，我顿悟了。"
    "最近发生的一切事情的全貌，我一瞬间都全部掌握了。"
    "这个时候，红莉栖来了……"
    window hide



    $ loadBG(2,"BG05N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "红莉栖露出吃惊的表情说道。"
    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0000"
    $ current_voice = "voice/KYO08B_CRS0000.ogg"
    "红莉栖" "「这个人……是谁？」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG21N2")

    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM26"
    "我和新一来到了大楼前面的投币式保险柜。"
    "还有一件事想要确认一下。"
    "让红莉栖先回Ｌａｂ待机了。"
    "如果我的想法是正确的话，接下来是不得不发送Ｄｍａｉｌ才行了。"
    "如果那时Ｌａｂ里没有人的话，电话微波炉（暂）就无法启动。"
    "于是就拜托了红莉栖去做启动的工作。"
    "虽说红莉栖开始稍有不满，但在我说“把你在网吧的事说出去哦”之后就乖乖从命了。"
    "于是到了现在。"
    "那么，说到要确认的事，当我看到保险柜的门的时候，心里就已经有数了。"
    window hide


    $ loadBG(2,"BG21N2R")



    "左下——『００５』的保险柜的门不自然地歪曲着。"
    "于是就没有必要再看了。"
    "但是我还是不死心，朝里面看了一眼。"
    window hide


    $ loadBG(2,"IBG025A",png=True)



    "空空如也……"
    "里面什么也没有。"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150033"
    $ current_voice = "voice/KYO08B_Y150033.ogg"
    "新一" "「怎么会……！」"
    "虽然新一十分地激动，但是我并不意外。"
    "当然这个结果确实十分令人遗憾。"
    "但是因为事先就有这个心理准备，所以也就没那么大动摇。"
    window hide



    $ loadBG(3,"BG21N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"SHI_BMA02"),"True","lh/SHI_BMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0021"
    $ current_voice = "voice/KYO08B_OKA0021.ogg"
    "伦太郎" "「想要知道发生了什么吗？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150034"
    $ current_voice = "voice/KYO08B_Y150034.ogg"
    "新一" "「你知道吗？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0022"
    $ current_voice = "voice/KYO08B_OKA0022.ogg"
    "伦太郎" "「恩恩。有个叫做４℃的家伙用铁棒撬开了门……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0023"
    $ current_voice = "voice/KYO08B_OKA0023.ogg"
    "伦太郎" "「然后将里面的怀表偷走了。那家伙是个有名的保险柜拾荒者的样子……」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150035"
    $ current_voice = "voice/KYO08B_Y150035.ogg"
    "新一" "「可恶！不能原谅！不能原谅！为什么警察没有将那家伙抓起来啊？」"
    "虽说『第２世界线』上是抓住了……"
    "但是『第３世界线』是不可能的。"
    "怀表也肯定已经被转手卖到不知道什么地方去了。"
    "虽然这么说很令人不快，但是在这条『第３世界线』上怀酱回到真由理的手里的可能性是非常低的。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG77A")

    hide screen phonebtn
    "在『第２世界线』上也是。"
    "虽说作为证据品被警察收走的怀酱，总会回到真由理的手里吧。"
    "但那已经不是以前的怀酱了。"
    "怀酱因为事故的冲击而坏掉了……"
    window hide


    $ loadBG(0,"BG21N2")

    show screen phonebtn
    show screen phoneSD1
    "那么有没有让怀酱安然无恙地回到真由理的手里的方法呢……？"
    "有的。只有一个——"
    "回到第１世界线就好了。"
    "『怎么办呢……？』"
    "当然是发送Ｄｍａｉｌ了……。"
    "『从谁的手机发……？』"
    "ｉｃｈｓ的……新一的手机……"
    "『收件人是……？』"
    "我的手机。"
    "『发送到的时间是……？』"
    "１６点０３分……"
    "『内容是……？』"
    "刚才给我看的手机上的那份邮件，就那么发过去吧。"
    "因为Ｄｍａｉｌ会将超过１８个的全角文字的后面截断。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    window hide

    "椎名在我这里的惯例物品，放在了大楼前的Ｌｏｃｋｅｒ里了。Ｌｏｃｋｅｒ的编号是００５。钥匙我用胶带贴在下面了。』"
    "椎名在我这里的惯例物品，放在了大楼前的Ｌｏｃｋｅｒ里了。Ｌｏｃｋｅｒ的编号是００５。钥匙我用胶带贴在下面了。"
    "椎名在我这里的惯例物品，放在了大楼前的Ｌｏｃｋｅｒ里"
    window hide


    $ loadBG(0,"BG21N2")

    show screen phonebtn
    show screen phoneSD1
    "但是还有一个值得注意的地方：如果回到第一世界线的话，真由理不是又要变成行踪不明的状态了么。"
    "但是，没有必要担心这个。"
    "因为ｉｃｈｓ并不是诱拐犯。"
    "这一切都记载在了“ｓｉｄｅｋｉｃｋ”发送的Ｄｍａｉｌ里。"
    "在那无法理解的字符串里……"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG21B")



    hide screen phonebtn
    "我借了新一的手机，找到刚才没发送的邮件，将收件人设定为了『电话微波炉（暂）』。"
    "关于收件人和时间点，都已经事先告诉了红莉栖。"
    "只需要给红莉栖打个电话……"

    window hide


    $ loadBG(2,"BG21N2")



    show screen phonebtn
    show screen phoneSD1
    "但是，那家伙的手机在网吧里掉坑里了，所以现在处于故障状态。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "所以我就决定显像管工房打电话。"
    "但是我手机里并没有店里的电话。"
    "所以最后打了１０４问了号码，直接打了过去。"
    window hide






    $ stopvoc("TEN")
    play TEN "KYO08B_TEN0000"
    $ current_voice = "voice/KYO08B_TEN0000.ogg"
    "天王寺" "「你好，这里是显像管工房」"

    "于是我说『如此如此这般这般总之有非常紧急的事情想和红莉栖取得联系，不好意思能去２楼叫她来听电话吗』。"
    "这么说了以后店长说……"

    $ stopvoc("TEN")
    play TEN "KYO08B_TEN0001"
    $ current_voice = "voice/KYO08B_TEN0001.ogg"
    "天王寺" "「没那么麻烦。这个电话是通２楼的所以就直接帮你转一下好了。你等等」"

    play se "SGSE379L" loop

    "这么说着，我听到了致爱丽丝的电话铃声。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"SHI_BMA01"),"True","lh/SHI_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "在等待的时候，我朝着新一又问道。"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0024"
    $ current_voice = "voice/KYO08B_OKA0024.ogg"
    "伦太郎" "「呐新一，有两件想问你的事情，可以吗？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150036"
    $ current_voice = "voice/KYO08B_Y150036.ogg"
    "新一" "「是什么啊？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0025"
    $ current_voice = "voice/KYO08B_OKA0025.ogg"
    "伦太郎" "「如果说，如果说的话」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0026"
    $ current_voice = "voice/KYO08B_OKA0026.ogg"
    "伦太郎" "「刚才在找真由理的时候，如果你的同伴中的一个……比如说那个拿着长剑的家伙吧，找到了真由理的话，你觉得他会怎么做？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150037"
    $ current_voice = "voice/KYO08B_Y150037.ogg"
    "新一" "「唔……如果是那家伙的话，估计会强行将真由理带到我们这里吧」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0027"
    $ current_voice = "voice/KYO08B_OKA0027.ogg"
    "伦太郎" "「然后呢？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150038"
    $ current_voice = "voice/KYO08B_Y150038.ogg"
    "新一" "「在我见到真由理之后，当然是将怀表还给他」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0028"
    $ current_voice = "voice/KYO08B_OKA0028.ogg"
    "伦太郎" "「如果已经放到这个保险柜里了呢？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150039"
    $ current_voice = "voice/KYO08B_Y150039.ogg"
    "新一" "「那样的话，就会带她到这个保险柜边……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0029"
    $ current_voice = "voice/KYO08B_OKA0029.ogg"
    "伦太郎" "「那如果已经是现在这幅样子了呢」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150040"
    $ current_voice = "voice/KYO08B_Y150040.ogg"
    "新一" "「那果然……会很麻烦吧。估计会一边哭着一边道歉，然后……会怎么做呢？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150041"
    $ current_voice = "voice/KYO08B_Y150041.ogg"
    "新一" "「最后应该会把她送到那个研究所，是叫Ｌａｂ的吧？」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150042"
    $ current_voice = "voice/KYO08B_Y150042.ogg"
    "新一" "「虽说我现在已经想哭了就是了……」"
    "新一这么说着，用手揉了揉眼角。"
    "『致爱丽丝』还在想着。"
    "我没将手机移开耳边，继续问道。"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0030"
    $ current_voice = "voice/KYO08B_OKA0030.ogg"
    "伦太郎" "「第二个问题，我昨天去了典当屋，但是你最后说了什么话才让我回去了？」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0031"
    $ current_voice = "voice/KYO08B_OKA0031.ogg"
    "伦太郎" "「到底是什么话？」"
    "我这么问着，新一抬头看向了夜空，伸出一只手，仿佛要从天上摘下星星一般握住了他的手。"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150043"
    $ current_voice = "voice/KYO08B_Y150043.ogg"
    "新一" "「『我喜欢椎名』……我这么说了」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150044"
    $ current_voice = "voice/KYO08B_Y150044.ogg"
    "新一" "「所以那个怀表，不管怎样都想自己还给她……」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0032"
    $ current_voice = "voice/KYO08B_OKA0032.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("Y15")
    play KUR "KYO08B_Y150045"
    $ current_voice = "voice/KYO08B_Y150045.ogg"
    "新一" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0033"
    $ current_voice = "voice/KYO08B_OKA0033.ogg"
    "伦太郎" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop se

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0001"
    $ current_voice = "voice/KYO08B_CRS0001.ogg"
    "红莉栖" "「啊，喂喂，冈部？　是我了哦？」"

    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0034"
    $ current_voice = "voice/KYO08B_OKA0034.ogg"
    "伦太郎" "「…………」"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0002"
    $ current_voice = "voice/KYO08B_CRS0002.ogg"
    "红莉栖" "「恩？　喂喂，能听到吗！」"

    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0035"
    $ current_voice = "voice/KYO08B_OKA0035.ogg"
    "伦太郎" "「能听到哦」"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0003"
    $ current_voice = "voice/KYO08B_CRS0003.ogg"
    "红莉栖" "「那样的话就回一句嘛，真是的……」"
    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0004"
    $ current_voice = "voice/KYO08B_CRS0004.ogg"
    "红莉栖" "「店长，正勃然大怒中哦？　Ｌａｂ的惨样被看到了啦。」"
    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0005"
    $ current_voice = "voice/KYO08B_CRS0005.ogg"
    "红莉栖" "「虽说『荧光剑·Ｓａｂｅｒ』的残骸暂时收拾好了，但是颜料的血迹收拾起来好像要花很久于是就暂时没管」"
    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0006"
    $ current_voice = "voice/KYO08B_CRS0006.ogg"
    "红莉栖" "「如果要启动电话微波炉的话，之后下去还这个无绳电话的时候估计又要被店长骂了吧，真是够了……」"

    "我随意地看了一眼自己的下身。"
    "估计是扑倒新一身上的时候沾上的吧，衣服上也好手上也好都满是红色的“血”。"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0007"
    $ current_voice = "voice/KYO08B_CRS0007.ogg"
    "红莉栖" "「啊，对了对了，电话微波炉已经设置好了。所以只需要启动就行」"

    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0036"
    $ current_voice = "voice/KYO08B_OKA0036.ogg"
    "伦太郎" "「…………」"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0008"
    $ current_voice = "voice/KYO08B_CRS0008.ogg"
    "红莉栖" "「呐，这到底是为了什么？发生了什么吗」"

    $ stopvoc("OKA")
    play OKA "KYO08B_OKA0037"
    $ current_voice = "voice/KYO08B_OKA0037.ogg"
    "伦太郎" "「不，没什么。——那就开始吧！　电话微波炉，启动！」"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0009"
    $ current_voice = "voice/KYO08B_CRS0009.ogg"
    "红莉栖" "「了解」"

    "立刻，手机的另一边响起了噼噼啪啪的火花声。"

    $ stopvoc("CRS")
    play CRS "KYO08B_CRS0010"
    $ current_voice = "voice/KYO08B_CRS0010.ogg"
    "红莉栖" "「放电现象，确认发生！」"
    call hide_phone

    hide screen phoneSD1


    stop bgm 


    $ loadBG(2,"PBG21C")




    stop bgm 
    stop se
    stop se


    $ loadBG(2,"PBG21D")
    play se "SGSE164"





    hide screen phonebtn
    "我听到这句话的同时，按下了新一的手机的发送键。"





    $ loadBG(2,"BG21N")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_06A.avi")
    hide screen invisible




    return
