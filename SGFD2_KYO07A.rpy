label SGFD2_KYO07A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG16A1")
    play se "SGSE054"



    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "噪音刺痛着鼓膜。"
    "感觉脑子里有什么东西在搅动着一样的痛苦。"
    "我紧咬牙关，忍受着那份痛苦。"
    window hide
    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "终于在痛苦退去的时候，我立刻注意到了在旁边的红莉栖。"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0000"
    $ current_voice = "voice/KYO07A_CRS0000.ogg"
    "红莉栖" "「怎么了……？　没事吧……？」"
    "右手是手机……"
    "西沉的太阳……"
    "看了一眼手表确认了时间，果然是『１６点４０分』。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0000"
    $ current_voice = "voice/KYO07A_OKA0000.ogg"
    "伦太郎" "「时间跳跃、成功了、吗……」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0001"
    $ current_voice = "voice/KYO07A_CRS0001.ogg"
    "红莉栖" "「诶？　什么？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0001"
    $ current_voice = "voice/KYO07A_OKA0001.ogg"
    "伦太郎" "「不，没什么」"
    "不管怎样和这次跳跃的事情都要向她说明吧。"
    "但是，现在应该先确认事态。"
    "我转向红莉栖，向她问道。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0002"
    $ current_voice = "voice/KYO07A_OKA0002.ogg"
    "伦太郎" "「我们现在在干什么？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0002"
    $ current_voice = "voice/KYO07A_CRS0002.ogg"
    "红莉栖" "「……哈？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0003"
    $ current_voice = "voice/KYO07A_OKA0003.ogg"
    "伦太郎" "「虽然你肯定不懂是怎么回事吧，但现在请先回答我。详情之后肯定会和你说的……拜托了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖似乎是因为怀疑一般眯起了眼睛……"
    "接下来露出了好像是想起了什么事情一样的表情，板下了脸转过头去。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0003"
    $ current_voice = "voice/KYO07A_CRS0003.ogg"
    "红莉栖" "「不行，现在不是呆站在这里的时候。赶快走吧」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0004"
    $ current_voice = "voice/KYO07A_OKA0004.ogg"
    "伦太郎" "「是要去哪里？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0004"
    $ current_voice = "voice/KYO07A_CRS0004.ogg"
    "红莉栖" "「这不是明摆着吗。去追真由理啊」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "红莉栖朝着路的前方跑了起来。"
    "在那前方，我沿着红莉栖的肩膀方向看到了逐渐远去的真由理的身影。"
    "原来如此，谜题解开了一个。"
    "好像是我和红莉栖目前正在尾随真由理。"
    "我慌慌张张地跟在红莉栖的后面。"
    window hide

    $ loadBG(0,"BG18A1")

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0005"
    $ current_voice = "voice/KYO07A_OKA0005.ogg"
    "伦太郎" "「Ｄｍａｉｌ收到了吧？『尾随真由理吧』『若不捉住犯人』『诱拐阻止困难』的Ｄｍａｉｌ……」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0005"
    $ current_voice = "voice/KYO07A_CRS0005.ogg"
    "红莉栖" "「虽说是这样……为什么现在问这个？」"
    "没有停下脚步，我们继续交谈。"
    "为了不跟丢真由理，一直向前奔跑……"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0006"
    $ current_voice = "voice/KYO07A_OKA0006.ogg"
    "伦太郎" "「Ｄｍａｉｌ是什么时候收到的？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0006"
    $ current_voice = "voice/KYO07A_CRS0006.ogg"
    "红莉栖" "「『１５点２４分』……刚好是我和桥田刚出发去买东西的时候」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0007"
    $ current_voice = "voice/KYO07A_OKA0007.ogg"
    "伦太郎" "「桶子后来怎么样了？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0007"
    $ current_voice = "voice/KYO07A_CRS0007.ogg"
    "红莉栖" "「所以就把他丢在那里了……买东西的任务交给他，我就先回了Ｌａｂ」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0008"
    $ current_voice = "voice/KYO07A_CRS0008.ogg"
    "红莉栖" "「呐，这算什么话啊？　是在耍我吗？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0008"
    $ current_voice = "voice/KYO07A_OKA0008.ogg"
    "伦太郎" "「理由之后肯定和你说。不是这么说过了吗？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0009"
    $ current_voice = "voice/KYO07A_CRS0009.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0009"
    $ current_voice = "voice/KYO07A_OKA0009.ogg"
    "伦太郎" "「那，之后呢？　把邮件给我看了吗？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0010"
    $ current_voice = "voice/KYO07A_CRS0010.ogg"
    "红莉栖" "「也给真由理看了」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0010"
    $ current_voice = "voice/KYO07A_OKA0010.ogg"
    "伦太郎" "「你，你说什么？」"
    "我下意识地停下了脚步。"
    "但是红莉栖并没有停下来。"
    "马上追了上去继续问清楚。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0011"
    $ current_voice = "voice/KYO07A_OKA0011.ogg"
    "伦太郎" "「为什么告诉了真由理？　那样的话尾行不是没有意义了吗」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0011"
    $ current_voice = "voice/KYO07A_CRS0011.ogg"
    "红莉栖" "「不是你说应该告诉她的吗？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0012"
    $ current_voice = "voice/KYO07A_OKA0012.ogg"
    "伦太郎" "「是我说的？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0012"
    $ current_voice = "voice/KYO07A_CRS0012.ogg"
    "红莉栖" "「『真由理隐藏自己的气息的能力十分惊人——普通的尾行的话有跟丢的可能性，所以还是应该告诉她』」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0013"
    $ current_voice = "voice/KYO07A_CRS0013.ogg"
    "红莉栖" "「『虽说诱拐的危机迫在眉睫，但是如果不告诉本人的话，应该不会有所警戒吧』……不是这么说了吗」"
    "虽说肯定是没有这样的记忆，但感觉自己确实会这么说。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0013"
    $ current_voice = "voice/KYO07A_OKA0013.ogg"
    "伦太郎" "「那真由理是知道我们在尾行的咯？」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0014"
    $ current_voice = "voice/KYO07A_CRS0014.ogg"
    "红莉栖" "「你觉得那个会是不知道的人做的事吗？」"
    "真由理就站在那里，好像是故意一样朝这边伸了一个懒腰。"
    "在确认了我们的位置之后，她单手撑腰，朝这边稍稍地挥了挥手，然后又再次向前走去。"
    "诶呀诶呀……"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0015"
    $ current_voice = "voice/KYO07A_CRS0015.ogg"
    "红莉栖" "「虽然之前有和她说过『和平时一样行动就行了』……」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0014"
    $ current_voice = "voice/KYO07A_OKA0014.ogg"
    "伦太郎" "「嘛，从某种程度上来说这个也算是和平时一样吧……」"
    window hide

    $ loadBG(0,"BG30A")



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0016"
    $ current_voice = "voice/KYO07A_CRS0016.ogg"
    "红莉栖" "「那，差不多该告诉我了吧？　这记忆丧失Ｐｌａｙ到底是怎么回事？」"
    "这已经是第几次说明这些内容了呢……"
    "如果把别的世界线上的次数也算进去的话，早就数不清了。"
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "因为说了很多次了，逐渐掌握了要领。"
    "我已经知道要怎么说才能快速地让红莉栖明白。"
    "但是，就算这样从最初开始说明也是非常费口舌的事。"
    "全部说完的时候，周围的天空已经被染成深红色了。"
    window hide

    $ loadBG(0,"BG23E")

    "…………"
    window hide
    $ loadBG(0,"BG24E")

    "…………"
    window hide
    $ loadBG(0,"BG14E")

    "…………"
    window hide
    $ loadBG(0,"BG22E")

    "…………"
    window hide
    $ loadBG(0,"BG13E1")

    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0015"
    $ current_voice = "voice/KYO07A_OKA0015.ogg"
    "伦太郎" "「就算这样犯人这家伙，还是从来没出现过啊……」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0017"
    $ current_voice = "voice/KYO07A_CRS0017.ogg"
    "红莉栖" "「虽然到目前为止已经尾随了一个小时以上，但是接触过真由理的只有一个发纸巾的大哥哥」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAID_CAFE"])
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0016"
    $ current_voice = "voice/KYO07A_OKA0016.ogg"
    "伦太郎" "「连{color=#f00}女仆咖啡{/color}的探子都不能回应，真是遗憾呢」"
    window hide
    $ loadBG(0,"BG24E")

    "根据红莉栖的话来看，真由理是被我们拜托了『不要决定目的地，在秋叶原的街上闲逛』。"
    window hide
    $ loadBG(0,"BG23E")

    "忠实地遵从了这个指示，真由理就在街上漫步着。"
    window hide
    $ loadBG(0,"BG16E1")

    "我和红莉栖在后面和她保持着适当的距离，一直跟在她后面。"
    window hide
    $ loadBG(0,"BG18E1")

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0018"
    $ current_voice = "voice/KYO07A_CRS0018.ogg"
    "红莉栖" "「呐，虽然只是保险起见『ｉｃｈｓ＝黑斗篷的家伙』这么想也可以吧？」"
    "在走的时候红莉栖问道。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0017"
    $ current_voice = "voice/KYO07A_OKA0017.ogg"
    "伦太郎" "「是啊。是『第３世界线』上到Ｌａｂ来的家伙呢。」"
    "我接着说了下去。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0018"
    $ current_voice = "voice/KYO07A_OKA0018.ogg"
    "伦太郎" "「但是如果他们现在在哪里打算拐走真由理的话，应该不会是那副打扮才对……」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0019"
    $ current_voice = "voice/KYO07A_OKA0019.ogg"
    "伦太郎" "「不管怎么说，那副打扮实在是太抢眼了」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0019"
    $ current_voice = "voice/KYO07A_CRS0019.ogg"
    "红莉栖" "「这种人这么多的地方，感觉有可能真由理会被拐跑哦？」"
    "就在红莉栖这么说了之后的瞬间——"
    window hide

    stop bgm 
    play se "SGSE211"


    "黑色的人影从道路的另一侧出现了。"
    "这么想着的时候，真由理的身影已经不见了。"
    "……诶？"
    "我一瞬间呆住了……"
    window hide
    play bgm "BGM12"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0020"
    $ current_voice = "voice/KYO07A_CRS0020.ogg"
    "红莉栖" "「出发了哦，冈部！」"
    "红莉栖尖锐的声音划过我的鼓膜。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0020"
    $ current_voice = "voice/KYO07A_OKA0020.ogg"
    "伦太郎" "「可恶──！」"
    play se "SGSE183L"

    "我立刻冲过了马路、"
    hide screen phoneSD1
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO004A"]]["Check"]=True
    $ loadBG(0,"EV_KYO004A")

    hide screen phonebtn
    "跑到路上的时候，我看到了前方拉着真由理的手向前走着的黑影。"
    "黑斗篷——！"
    "切……这家伙胆子还挺大的嘛。"
    "在这个太阳还没有下山的时候，众目睽睽之下，敢穿着这样的衣服明目张胆地带走真由理吗！"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0021"
    $ current_voice = "voice/KYO07A_OKA0021.ogg"
    "伦太郎" "「别开玩笑了！」"
    "我提升速度，向黑斗篷追去。"
    "距离不断缩短。"
    "我超过了红莉栖，将她甩在后面。"
    "红莉栖却——"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0021"
    $ current_voice = "voice/KYO07A_CRS0021.ogg"
    "红莉栖" "「等等我！」"
    "只是这么一声，当然无法让黑斗篷停下脚步。"
    "他连头都没有回。"
    "只是牵着真由理的手，朝着路的另一侧狂奔着。"
    "不一会儿——"
    window hide


    $ loadBG(2,"BG_BLACK")





    hide screen phonebtn
    show screen phoneSD1
    "黑斗篷和真由理的身影消失了。"
    "在跑到路的尽头的时候，他们朝着右边转了。"
    "于是我也跟着在那个角落右转了——"
    window hide


    $ loadBG(2,"BG16E1")






    stop se
    show screen phonebtn
    "然后来到了中央通路——路边满是行人——"
    "试着确认了一下该向哪里走，于是在人群的缝隙中看到了奔跑着的黑斗篷和真由理的身影。"
    "我努力地在人海中游弋着。"
    "不知道和几个人撞了肩膀，但那又何妨！"
    "这样下去真由理就会被带走了。"
    "作战失败——最坏的结果——"
    "被不安的预感所驱动着，我全力追在黑斗篷后面。"
    "最终黑斗篷改变了方向。"
    "横穿过了中央路口，向着另一侧——"
    "在没有人行横道也没有信号灯的路上，他们在车流之间穿梭着。"
    "我也连忙飞奔入车道。"
    "幸好车流似乎停了下来。"
    "就这样朝着马路对面的人行道——"
    "迈出脚步的时候——"
    window hide


    $ loadBG(2,"BG_BLACK")



    play se "SGSE324L" loop


    stop bgm 
    hide screen phonebtn
    "背后传来爆音——"
    "汽车的引擎声轰鸣着。"
    "刷地转过头去。"
    window hide

    $ loadBG(0,"BG16E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "看到的是在马路中央的红莉栖的身影。"
    "正朝着这里跑来。"
    "从旁边袭来的一辆车——"
    "白色的货车——"
    play se "SGSE063"
    "突然间——"
    play se "SGSE063"
    "提高了速度——"
    play se "SGSE063"
    "现在——"
    play se "SGSE063"
    "朝着红莉栖的——"
    play se "SGSE063"
    "前方——"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0022"
    $ current_voice = "voice/KYO07A_OKA0022.ogg"
    "伦太郎" "「红莉栖──！！！」"
    hide screen phoneSD1
    window hide














    play se "SGSE372"


    stop se



























    play se "SGSE373"








    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO005A"]]["Check"]=True
    $ loadBG(0,"EV_KYO005A")

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0022"
    $ current_voice = "voice/KYO07A_CRS0022.ogg"
    "红莉栖" "「痛痛痛痛……」"
    "注意到的时候，我整个人已经趴在红莉栖身上了。"
    play bgm "FDBGM04"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0023"
    $ current_voice = "voice/KYO07A_OKA0023.ogg"
    "伦太郎" "「啊、啊啊……抱歉」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0023"
    $ current_voice = "voice/KYO07A_CRS0023.ogg"
    "红莉栖" "「为什么要道歉啊！　你不是救了我吗！」"
    "好像是那么回事。"
    "在车冲过来的那一刻，我千钧一发之际扑倒了红莉栖，防止了事故的发生。"
    "是因为是下意识的动作吧，到现在也没有救了她的实感。"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0024"
    $ current_voice = "voice/KYO07A_CRS0024.ogg"
    "红莉栖" "「笨蛋，要是出了点问题的话，你就要被车压成肉酱了啊」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0024"
    $ current_voice = "voice/KYO07A_OKA0024.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0025"
    $ current_voice = "voice/KYO07A_CRS0025.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0025"
    $ current_voice = "voice/KYO07A_OKA0025.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0026"
    $ current_voice = "voice/KYO07A_CRS0026.ogg"
    "红莉栖" "「谢谢你……」"
    "红莉栖噙着泪水说道。"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0027"
    $ current_voice = "voice/KYO07A_CRS0027.ogg"
    "红莉栖" "「真的，非常感谢……」"
    "再次说出的道谢的话语因为恐惧而颤抖着。"
    "红莉栖咬着嘴唇，拭了拭眼角。"
    "我有些不好意思，移开了视线，站起身来。"
    window hide

    stop bgm 


    $ loadBG(2,"BG16E1")



    show screen phonebtn
    show screen phoneSD1
    "朝着黑斗篷的方向投去了目光。"
    "但是并没有看到他们的身影。"
    "糟糕了。糟糕了啊……"
    "总之先朝着黑斗篷的方向走走看吧。"
    "这么想着的时候，我看到了无法置之不理的东西。"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    "刚才白色的卡车，好像撞进了一家店的样子。"
    "似乎是因为为了避让我们而进行了紧急刹车，一头撞进了店里。"
    "追黑斗篷这件事刻不容缓。"
    "我自然是再清楚不过了。"
    "但是说不定也会有受伤的人，所以也不能这么置之不顾。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0026"
    $ current_voice = "voice/KYO07A_OKA0026.ogg"
    "伦太郎" "「啊啊、可恶！」"
    "我发出一声哀嚎，和红莉栖一起向现场走去。"
    window hide


    $ loadBG(2,"BG77A")



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0028"
    $ current_voice = "voice/KYO07A_CRS0028.ogg"
    "红莉栖" "「没事吧！　有人受伤了吗！？」"
    "红莉栖朝店里喊一声。"
    "立刻就有应该是店员的声音传了过来。"
    $ stopvoc("Y18")
    play KUR "KYO07A_Y180000"
    $ current_voice = "voice/KYO07A_Y180000.ogg"
    "店員" "「店没有问题！　大家都在厨房里所以没事！　车那边怎么样！？」"
    "是啊，车……"
    "司机和乘客都没事吗？"
    "这么想着，朝那边看了一眼——"
    "从破掉的车窗里爬出一个男子。"
    "感觉这非主流的派头好像见过……"
    "比盖亚的光辉还要更加耀眼的男性——！"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM02"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0027"
    $ current_voice = "voice/KYO07A_OKA0027.ogg"
    "伦太郎" "「４℃ー！」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0000"
    $ current_voice = "voice/KYO07A_SDO0000.ogg"
    "４℃" "「是四度！　说起来，你这家伙是怎么知道我名字的啊……」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0029"
    $ current_voice = "voice/KYO07A_CRS0029.ogg"
    "红莉栖" "「开车的是你吗？」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0001"
    $ current_voice = "voice/KYO07A_SDO0001.ogg"
    "４℃" "「这不明摆着么！」"
    "感觉并不是那么显然就是了……"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0028"
    $ current_voice = "voice/KYO07A_OKA0028.ogg"
    "伦太郎" "「别的乘客呢？」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0002"
    $ current_voice = "voice/KYO07A_SDO0002.ogg"
    "４℃" "「才没有咧！」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0030"
    $ current_voice = "voice/KYO07A_CRS0030.ogg"
    "红莉栖" "「也就是说只有你一个人在车上咯？」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0003"
    $ current_voice = "voice/KYO07A_SDO0003.ogg"
    "４℃" "「所以不是已经这么说过了嘛！」"
    "稍微放心了些。没有人受伤。"
    "４℃也还能流畅地说话所以应该没事。"
    "我看到４℃身后的车里弹出的安全气囊就知道确实如此了。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0029"
    $ current_voice = "voice/KYO07A_OKA0029.ogg"
    "伦太郎" "「４℃、虽然不是很在意你的情况，但是还是再确认一下。没事吧？」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0004"
    $ current_voice = "voice/KYO07A_SDO0004.ogg"
    "４℃" "「你这家伙……是找打吗？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0030"
    $ current_voice = "voice/KYO07A_OKA0030.ogg"
    "伦太郎" "「给我３００万我就给你找」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0005"
    $ current_voice = "voice/KYO07A_SDO0005.ogg"
    "４℃" "「切，这么屌啊，你这混蛋！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DMA02"),"True","lh/SDO_DMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "随着他的怒吼，他举起了他的右手，手里好像握着棒子一样的东西。"
    "棒子一样的东西……"
    "也就是铁棒……"
    "铁棒→被打→领便当。"
    "我一瞬间完成了这个联想，摆出了『少侠，请三思』的Ｐｏｓｅ。"
    "然后也这么说了。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0031"
    $ current_voice = "voice/KYO07A_OKA0031.ogg"
    "伦太郎" "「少侠，请三思！」"
    "４℃并没有冲动。"
    "不如说连冲动的机会都没有。"
    "在他出手之前他就已经被一个疾风般的人物给缚住了。"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190000"
    $ current_voice = "voice/KYO07A_Y190000.ogg"
    "警官？" "「确保哦哦哦────！」"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0006"
    $ current_voice = "voice/KYO07A_SDO0006.ogg"
    "４℃" "「糟了！」"
    window hide
    play se "SGSE015"




    $ loadBG(2,"BG_BLACK")





    hide screen phonebtn
    "吃了重重一击，４℃向后倒去。"
    "骑在他身上的是穿着制服的警官。"
    "……诶？"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0007"
    $ current_voice = "voice/KYO07A_SDO0007.ogg"
    "４℃" "「住手！　放开我！　放开我！　说了放开我啊啊啊啊！」"
    "就算如此４℃也没有停止抵抗。"
    "就算被警官制服在地上，仍然不停地闹腾着。"
    "在这段时间里，其他警官又一个个出现了。"
    "警官们一个个压在了４℃的身上，于是他完全没有挪动的空间了。"
    $ stopvoc("SDO")
    play SDO "KYO07A_SDO0008"
    $ current_voice = "voice/KYO07A_SDO0008.ogg"
    "４℃" "「可恶！　给我记好了！　不会就这样放过你们的！」"

    stop bgm 
    "被警官制住，拖到一边的４℃……"
    window hide


    $ loadBG(2,"BG16E1")



    show screen phonebtn
    show screen phoneSD1
    "最终被塞进了停在路边的巡逻警车里。"
    window hide

    play se "SGSE140"

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0031"
    $ current_voice = "voice/KYO07A_CRS0031.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0032"
    $ current_voice = "voice/KYO07A_OKA0032.ogg"
    "伦太郎" "「…………」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我和红莉栖面面相觑。"
    "正在我们不知所措时，从那边来了一个警察。"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190001"
    $ current_voice = "voice/KYO07A_Y190001.ogg"
    "警官" "「多亏了你们呢」"
    "是最初扑倒４℃的警官。"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0032"
    $ current_voice = "voice/KYO07A_CRS0032.ogg"
    "红莉栖" "「刚才那人，为什么会被带到警车里？」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190002"
    $ current_voice = "voice/KYO07A_Y190002.ogg"
    "警官" "「那家伙是有名的投币保险柜扒手哦。是个惯犯」"
    "真意外啊……没想到会是这样。"
    "不过那家伙的话看起来也确实会做这种事。"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190003"
    $ current_voice = "voice/KYO07A_Y190003.ogg"
    "警官" "「在大楼前面的那个投币式保险柜，应该知道吧？　刚刚那家伙还在那里作案了」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190004"
    $ current_voice = "voice/KYO07A_Y190004.ogg"
    "警官" "「然后被巡逻中的我们发现了……。也就是所谓的抓了个现行」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190005"
    $ current_voice = "voice/KYO07A_Y190005.ogg"
    "警官" "「所以当然立即决定逮捕他，但没想到他居然就跳进了停在边上的车开始了逃亡」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0033"
    $ current_voice = "voice/KYO07A_CRS0033.ogg"
    "红莉栖" "「所以才会是那样的速度……」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190006"
    $ current_voice = "voice/KYO07A_Y190006.ogg"
    "警官" "「恩恩。所以结果就是……你们看到的那样」"
    window hide


    $ loadBG(2,"BG77A")



    show screen phonebtn
    "警官这么说着，指向了背后的那辆白色货车。"
    "在那个时候，我注意到警察的手里好像握着什么。"
    "是白色的手帕包着的东西……"
    "我装作不在意的样子问了一下。"
    "警官立刻就告诉我了……"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190007"
    $ current_voice = "voice/KYO07A_Y190007.ogg"
    "警官" "「啊啊，这个吗？　这个是那家伙刚从保险柜里偷出来的东西。用铁棍撬开的门」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0034"
    $ current_voice = "voice/KYO07A_CRS0034.ogg"
    "红莉栖" "「能给我们看看吗？」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190008"
    $ current_voice = "voice/KYO07A_Y190008.ogg"
    "警官" "「恩恩，没问题啊」"
    "这么说着，警官摊开了他的手。"
    "向里看去，在白手帕里的东西是——"
    window hide


    $ loadBG(2,"IBG012A",png=True)



    play bgm "FD2BGM05"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0035"
    $ current_voice = "voice/KYO07A_CRS0035.ogg"
    "红莉栖" "「怀表……？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0033"
    $ current_voice = "voice/KYO07A_OKA0033.ogg"
    "伦太郎" "「不对，这不仅仅是怀表……。是『怀酱』……啊……」"
    "是的，这无疑就是『怀酱』。"
    "真由理最重要的宝物——"
    "我是不会看错的。"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190009"
    $ current_voice = "voice/KYO07A_Y190009.ogg"
    "警官" "「咦？　是你知道的东西吗？"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0034"
    $ current_voice = "voice/KYO07A_OKA0034.ogg"
    "伦太郎" "「诶诶……。是朋友的东西」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190010"
    $ current_voice = "voice/KYO07A_Y190010.ogg"
    "警官" "「那家伙真是弱啊……。虽然帮助我们逮捕了他，我们十分想要表示谢意……」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190011"
    $ current_voice = "voice/KYO07A_Y190011.ogg"
    "警官" "「但是这也算是证据之一，还是要带回警局保管。承蒙理解了啊？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0035"
    $ current_voice = "voice/KYO07A_OKA0035.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0036"
    $ current_voice = "voice/KYO07A_CRS0036.ogg"
    "红莉栖" "「说起来，这个好像坏掉了吧？　你看玻璃的部分都碎了」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190012"
    $ current_voice = "voice/KYO07A_Y190012.ogg"
    "警官" "「会不会原来就是这样了呢？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0036"
    $ current_voice = "voice/KYO07A_OKA0036.ogg"
    "伦太郎" "「不会的！真由理一直把它当做最重要的宝物！不管什么时候都在手里玩弄着……！」"
    $ stopvoc("Y19")
    play KUR "KYO07A_Y190013"
    $ current_voice = "voice/KYO07A_Y190013.ogg"
    "警官" "「是吗……。那看来是因为刚才的事故的冲击坏掉了吧」"
    "感觉身体中有一座火山喷发了。"
    "脑袋后方感觉轻飘飘的，眼前因为愤怒而变得一片空白。"
    window hide



    $ loadBG(3,"BG16E1")



    "抬起头，开始寻找４℃所在的警车。"
    "但是刚刚还停在那里的警车已经消失了。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0037"
    $ current_voice = "voice/KYO07A_OKA0037.ogg"
    "伦太郎" "「可恶！　４℃这混蛋！」"
    "我忿忿地吐出一些咒骂的话，踢了一脚边上的白色货车。"
    window hide
    play se "SGSE325"



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0037"
    $ current_voice = "voice/KYO07A_CRS0037.ogg"
    "红莉栖" "「等等，冈部，冷静下来！」"
    "就算红莉栖像是安抚我一样的按住了我的肩膀，但是我心中的郁愤仍没有平息、"
    "那家伙弄坏了真由理最重要的宝物！"
    "将相信这Ｌａｂｍｅｍ，为了Ｌａｂ的光明未来，舍身成仁的怀表——"
    "…………"
    "诶……？等等……"
    "为什么那个怀表……会在投币式保险柜里？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0038"
    $ current_voice = "voice/KYO07A_CRS0038.ogg"
    "红莉栖" "「总而言之，４℃那家伙的事情怎样都好了。比起那个现在──」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0038"
    $ current_voice = "voice/KYO07A_OKA0038.ogg"
    "伦太郎" "「明白了。去找吧。黑斗篷和真由理的位置……」"
    "我这么回答着，又一次看向了事故现场。"
    window hide


    $ loadBG(2,"BG77A")



    show screen phonebtn
    "白色货车冲入的是一家披萨店。"
    "碎成好多片的塑料看板上是大大的“逼胜客”。应该是店名。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG13E1")

    show screen phonebtn
    show screen phoneSD1
    "黑斗篷和真由理离开的方向，是秋叶原的车站。"
    "于是我和红莉栖一路找到了那里……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0039"
    $ current_voice = "voice/KYO07A_CRS0039.ogg"
    "红莉栖" "「没有呢……」"
    "也并不是不能理解。"
    "从失去两人行踪到现在已经过了１０分钟以上了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0040"
    $ current_voice = "voice/KYO07A_CRS0040.ogg"
    "红莉栖" "「我们分头去找吧」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0039"
    $ current_voice = "voice/KYO07A_OKA0039.ogg"
    "伦太郎" "「抱歉啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0041"
    $ current_voice = "voice/KYO07A_CRS0041.ogg"
    "红莉栖" "「为什么道歉啊？」"
    "我看着来往的行人说道。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0040"
    $ current_voice = "voice/KYO07A_OKA0040.ogg"
    "伦太郎" "「因为把你卷进来了啊，克里斯提娜」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这么说着，红莉栖用手叉腰……"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0042"
    $ current_voice = "voice/KYO07A_CRS0042.ogg"
    "红莉栖" "「并不是卷进来了啊。是我自己想要帮忙的」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0043"
    $ current_voice = "voice/KYO07A_CRS0043.ogg"
    "红莉栖" "「刚才你说的『第１世界线』的我好像也是自愿加入的，而不是受你之托」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0044"
    $ current_voice = "voice/KYO07A_CRS0044.ogg"
    "红莉栖" "「所以我才会从自己的手机给自己发送『尾行真由理吧』的Ｄｍａｉｌ……吧？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0041"
    $ current_voice = "voice/KYO07A_OKA0041.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0045"
    $ current_voice = "voice/KYO07A_CRS0045.ogg"
    "红莉栖" "「请不要认为你只有你自己一个人。那只是自欺欺人罢了。」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0046"
    $ current_voice = "voice/KYO07A_CRS0046.ogg"
    "红莉栖" "「世界上的万物，之间必定有着复杂的因果。」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0042"
    $ current_voice = "voice/KYO07A_OKA0042.ogg"
    "伦太郎" "「请用日语说。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0047"
    $ current_voice = "voice/KYO07A_CRS0047.ogg"
    "红莉栖" "「就是用日语说的」"
    "红莉栖叹了口气继续说下去。"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0048"
    $ current_voice = "voice/KYO07A_CRS0048.ogg"
    "红莉栖" "「总之如果是真由理的事的话请随意差遣我。」"
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0049"
    $ current_voice = "voice/KYO07A_CRS0049.ogg"
    "红莉栖" "「因为我也是Ｌａｂ的一份子，也是你的……ｓｉｄｅｋｉｃｋ啊。」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0043"
    $ current_voice = "voice/KYO07A_OKA0043.ogg"
    "伦太郎" "「ｓｉｄｅ……ｋｉｃｋ？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GGRKS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GGRKS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GGRKS"])
    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0050"
    $ current_voice = "voice/KYO07A_CRS0050.ogg"
    "红莉栖" "「{color=#f00}请自行谷歌{/color}」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC01"),"True","lh/CRS_ASC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO07A_CRS0051"
    $ current_voice = "voice/KYO07A_CRS0051.ogg"
    "红莉栖" "「那么就这样，如果找到真由理的话就和对方联系吧。那边就拜托你了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "这么说着红莉栖消失在了人群里。"
    "『ｓｉｄｅｋｉｃｋ』……。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我又一次在脑海里取出了这个关键词。"
    "试着Ｇｏｏｇｌｅ了一下，发现有挺多的意思，于是选了一个看了一下。"
    "上面写着这样的定义。"
    window hide
    hide screen phoneSD1


    $ loadBG(2,"PBG20A")




    call hide_phone

    hide screen phonebtn
    "ｓｉｄｅｋｉｃｋ"
    "（名）挚友，伙伴，助手"
    "感觉好像联系起来了……"
    "我是这么觉得的。"
    window hide



    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    hide screen phoneSD1
    "在那之后，我也展开了对黑斗篷和真由理的搜索"
    "找遍了秋叶原的角角落落……"
    window hide
    $ loadBG(0,"BG14E")

    "…………"
    window hide
    $ loadBG(0,"BG22E")

    "…………"
    window hide
    $ loadBG(0,"BG17A")

    "…………"
    window hide
    $ loadBG(0,"BG20E")

    "…………"
    window hide
    $ loadBG(0,"BG18E1")

    "…………"
    window hide
    $ loadBG(0,"BG24E")

    "结果仍然没有看到两个人的身影……"
    window hide
    $ loadBG(0,"BG23E")

    "注意到的时候已经来到了ＵＰＸ前面。"
    "当然已经试着给真由理打过很多次电话了。"
    "但是只得到了『现在暂时无法接听』的机械音。"
    "开始自责起来。作战失败——情况变得不妙了。"
    "不应该按照第一世界线的红莉栖所说的那样等待犯人的出现……"
    "放任真由理，等待犯人出现的做法，现在看来十分无谋。"
    "并不是红莉栖的错……"
    "错的是我。全部是因为我。"
    "我抱着头蹲在地上。"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    "这时，在那里……"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0000"
    $ current_voice = "voice/KYO07A_FEI0000.ogg"
    "菲利斯" "「凶真、事情的经过我已经全部听说了！」"
    "声音传了过来。"
    "抬头一看，是菲利斯正在用手指着这边。"
    "不知道是什么意思。"
    "我茫然地牵着菲利斯的手站了起来。"

    window hide



    $ loadBG(2,"BG23E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC01"),"True","lh/FEI_BMC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0001"
    $ current_voice = "voice/KYO07A_FEI0001.ogg"
    "菲利斯" "「刚刚和克喵见面了喵」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0044"
    $ current_voice = "voice/KYO07A_OKA0044.ogg"
    "伦太郎" "「克喵？　那是谁啊」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0002"
    $ current_voice = "voice/KYO07A_FEI0002.ogg"
    "菲利斯" "「牧濑喵」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0045"
    $ current_voice = "voice/KYO07A_OKA0045.ogg"
    "伦太郎" "「请用日语」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMB01"),"True","lh/FEI_BMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0003"
    $ current_voice = "voice/KYO07A_FEI0003.ogg"
    "菲利斯" "「那……克里斯提喵」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0046"
    $ current_voice = "voice/KYO07A_OKA0046.ogg"
    "伦太郎" "「啊啊，助手啊」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0047"
    $ current_voice = "voice/KYO07A_OKA0047.ogg"
    "伦太郎" "「也就是说你知道那家伙咯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA01"),"True","lh/FEI_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0004"
    $ current_voice = "voice/KYO07A_FEI0004.ogg"
    "菲利斯" "「当然了喵。克喵可是『ＭａｙＱｕｅｅｎ＋Ｎｙａ²』的常客喵。最开始是真由喜带来的喵」"
    "呜哇，是这样的世界线啊……"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0005"
    $ current_voice = "voice/KYO07A_FEI0005.ogg"
    "菲利斯" "「然后，从克喵那里已经全部听说了」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0048"
    $ current_voice = "voice/KYO07A_OKA0048.ogg"
    "伦太郎" "「全部……？」"
    "虽然我提问了，但是菲利斯没有回答我，继续说了下去。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0006"
    $ current_voice = "voice/KYO07A_FEI0006.ogg"
    "菲利斯" "「凶真、这可是“机关”的阴谋喵！　不十万火急地发送“时空邮件”的话就不得了了喵！」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0049"
    $ current_voice = "voice/KYO07A_OKA0049.ogg"
    "伦太郎" "「时空邮件是什么……？」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0007"
    $ current_voice = "voice/KYO07A_FEI0007.ogg"
    "菲利斯" "「时空邮件就是时空邮件喵！」"
    "想了一下，大概是指Ｄｍａｉｌ吧……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA01"),"True","lh/FEI_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0008"
    $ current_voice = "voice/KYO07A_FEI0008.ogg"
    "菲利斯" "「也就是说，赶紧和桶子联系，进行电话微波炉的设定吧喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0009"
    $ current_voice = "voice/KYO07A_FEI0009.ogg"
    "菲利斯" "「时空邮件的内容已经在菲利斯的手机上准备好了喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0010"
    $ current_voice = "voice/KYO07A_FEI0010.ogg"
    "菲利斯" "「只剩下凶真和桶子联系然后说ＧＯ了喵！」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0050"
    $ current_voice = "voice/KYO07A_OKA0050.ogg"
    "伦太郎" "「等等等等，你到底在说什么啊！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0011"
    $ current_voice = "voice/KYO07A_FEI0011.ogg"
    "菲利斯" "「好了赶紧按照菲利斯说的做吧喵！」"
    "菲利斯摆出了猫娘的ｐｏｓｅ，露出了虎牙。"
    "虽然不太可怕，但是因为里面的别的含义还是让步了。"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0012"
    $ current_voice = "voice/KYO07A_FEI0012.ogg"
    "菲利斯" "「请告诉桶子喵希望时空邮件能发送到『１５点２３分』喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0013"
    $ current_voice = "voice/KYO07A_FEI0013.ogg"
    "菲利斯" "「这是为了能让凶真的手机收到之前应该收到的两封邮件喵」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0051"
    $ current_voice = "voice/KYO07A_OKA0051.ogg"
    "伦太郎" "「是指『真由理的外出／必须全力阻止』和『评议会要终止／不要使用火！』的Ｄｍａｉｌ──时空邮件是吧？」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0014"
    $ current_voice = "voice/KYO07A_FEI0014.ogg"
    "菲利斯" "「就是这样喵。在那个时间点之前如果能收到别的时空邮件的话，就有让那两封邮件消失的可能性喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0015"
    $ current_voice = "voice/KYO07A_FEI0015.ogg"
    "菲利斯" "「特别是那封『不要使用火！』的邮件，明显是为了阻止Ｌａｂ发生火灾才发过来的喵」"
    "虽然不太明白到底是怎么回事，但好像菲利斯已经完全掌握了情况的样子。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC01"),"True","lh/FEI_BMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0016"
    $ current_voice = "voice/KYO07A_FEI0016.ogg"
    "菲利斯" "「还有就是之前的那封喵。这次感觉应该发给真由喜喵」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0052"
    $ current_voice = "voice/KYO07A_OKA0052.ogg"
    "伦太郎" "「发给真由喜？　为什么？」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0017"
    $ current_voice = "voice/KYO07A_FEI0017.ogg"
    "菲利斯" "「让真由喜也有些危机感喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0018"
    $ current_voice = "voice/KYO07A_FEI0018.ogg"
    "菲利斯" "「虽然这条世界线上凶真和克喵都很努力了，但是还是没能做得很好喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0019"
    $ current_voice = "voice/KYO07A_FEI0019.ogg"
    "菲利斯" "「所以下一次就让真由理也有这个意思，让她保护好自己喵」"
    "不对，这件事本来在这条世界线上就该发生的……"
    "嘛好吧，总之先听下去吧。"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0020"
    $ current_voice = "voice/KYO07A_FEI0020.ogg"
    "菲利斯" "「最后是关于时空邮件的内容喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0021"
    $ current_voice = "voice/KYO07A_FEI0021.ogg"
    "菲利斯" "「果然还是要让真由理不能外出喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0022"
    $ current_voice = "voice/KYO07A_FEI0022.ogg"
    "菲利斯" "「所以打算发送『在Ｌａｂ待机』过去」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0053"
    $ current_voice = "voice/KYO07A_OKA0053.ogg"
    "伦太郎" "「不可以，那么做并没有意义。最后如果一直呆在Ｌａｂ的话，黑斗篷的那群家伙还是会来的。」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0023"
    $ current_voice = "voice/KYO07A_FEI0023.ogg"
    "菲利斯" "「我知道喵」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0024"
    $ current_voice = "voice/KYO07A_FEI0024.ogg"
    "菲利斯" "「虽然知道，但那不是你一直想要的事情喵？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0054"
    $ current_voice = "voice/KYO07A_OKA0054.ogg"
    "伦太郎" "「……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMB01"),"True","lh/FEI_BMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0025"
    $ current_voice = "voice/KYO07A_FEI0025.ogg"
    "菲利斯" "「因为凶真和克喵现在不是拼了命地想找到黑斗篷吗？」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0026"
    $ current_voice = "voice/KYO07A_FEI0026.ogg"
    "菲利斯" "「有那样的机会不去利用，反而现在在这里做着这样徒劳的搜索，可不是什么有意思的事情哦」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0055"
    $ current_voice = "voice/KYO07A_OKA0055.ogg"
    "伦太郎" "「但是……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0027"
    $ current_voice = "voice/KYO07A_FEI0027.ogg"
    "菲利斯" "「战斗吧喵，凶真！　当缩头乌龟是不行的！」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0028"
    $ current_voice = "voice/KYO07A_FEI0028.ogg"
    "菲利斯" "「只是这样固步自封，追在真由喜后面的话，是肯定救不了真由喜的啊喵！」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0029"
    $ current_voice = "voice/KYO07A_FEI0029.ogg"
    "菲利斯" "「就因为这种心态，就算在这条世界线上，你也不打算和黑斗篷正面战斗吧？」"
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0030"
    $ current_voice = "voice/KYO07A_FEI0030.ogg"
    "菲利斯" "「所以才会采取尾行这种危险的手法……」"

    stop bgm 
    "确实……如同菲利斯所说。"
    "不知为何感觉思路被打开了。"
    "是啊，来试着和他战斗吧。"
    "不对，是只能和他战斗了。"
    "不管发生什么，如果都会收束到真由理被拐走，或是Ｌａｂ发生火灾的世界线的话，除了和黑斗篷们决一死战以外就别无他法了！"
    play bgm "FD2BGM11"
    "这么想着，身体里渐渐地充满了活力。"
    "我大笑一阵，高声说道。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHESHIRE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHESHIRE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHESHIRE"])
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0056"
    $ current_voice = "voice/KYO07A_OKA0056.ogg"
    "伦太郎" "「唔哈哈哈哈哈！　就是那样，就是那样啊，菲利斯哦！　不愧是会用{color=#f00}柴郡猫的微笑(Ｃｈｅｓｈｉｒｅ　ｂｒａｋｅ){/color}的人！」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0057"
    $ current_voice = "voice/KYO07A_OKA0057.ogg"
    "伦太郎" "「刚才都是为了考验你……。所以那些失落也好烦恼也好都是装出来的哦？」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0058"
    $ current_voice = "voice/KYO07A_OKA0058.ogg"
    "伦太郎" "「很好！岂有不好之理！！虽说什么岂有不好之理不太懂是什么意思，总之去战斗吧」"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0059"
    $ current_voice = "voice/KYO07A_OKA0059.ogg"
    "伦太郎" "「嘿，嘿，嘿……解除右腕的封印的时刻终于到来了吗──」"
    "就在我说着这些的时候……"
    hide screen phonebtn
    hide screen phoneSD1

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA02"),"True","lh/FEI_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0031"
    $ current_voice = "voice/KYO07A_FEI0031.ogg"
    "菲利斯" "「啊，喂喂，是桶喵吗？」"
    "注意到的时候，菲利斯趁我不注意已经从我的口袋里取出了我的手机，开始打起了电话。"
    $ stopvoc("OKA")
    play OKA "KYO07A_OKA0060"
    $ current_voice = "voice/KYO07A_OKA0060.ogg"
    "伦太郎" "「喂，菲利斯！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0032"
    $ current_voice = "voice/KYO07A_FEI0032.ogg"
    "菲利斯" "「好了你先安静下喵！」"
    $ stopvoc("DAR")
    play DAR "KYO07A_DAR0000"
    $ current_voice = "voice/KYO07A_DAR0000.ogg"
    "至" "「菲，菲利斯碳、这边已经准备好了哦！」"
    "就好像要让手机跳起来了一样，桶子饥渴的声音透过听筒从菲利斯手里的手机中传了出来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA01"),"True","lh/FEI_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0033"
    $ current_voice = "voice/KYO07A_FEI0033.ogg"
    "菲利斯" "「那就赶紧，启动电话微波炉吧！」"
    $ stopvoc("DAR")
    play DAR "KYO07A_DAR0001"
    $ current_voice = "voice/KYO07A_DAR0001.ogg"
    "至" "「ＯＫ！　约好的蛋包饭，可就拜托了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA02"),"True","lh/FEI_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0034"
    $ current_voice = "voice/KYO07A_FEI0034.ogg"
    "菲利斯" "「明白了喵。会给你做１００份的喵。」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MUNEATSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MUNEATSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MUNEATSU"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZENORE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ZENORE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ZENORE"])

    $ stopvoc("DAR")
    play DAR "KYO07A_DAR0002"
    $ current_voice = "voice/KYO07A_DAR0002.ogg"
    "至" "「哦哦，这是何等的{color=#f00}令人血脉喷张{/color}啊！　{color=#f00}我整个人都哭了{/color}哦！　说着这个时候放电现象出现了！」"
    "心里还没有做好准备。"
    "听到了这句话，菲利斯说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC01"),"True","lh/FEI_BMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0035"
    $ current_voice = "voice/KYO07A_FEI0035.ogg"
    "菲利斯" "「那就出发了喵，凶真！」"
    "菲利斯用拇指按下了自己手机的发送键。"
    "在那一瞬间，我看到了画面上的邮件内容。"
    "上面是这么写的。"
    window hide


    $ loadBG(0,"BG_BLACK")

    window hide

    "绝对外出禁止"
    "Ｌａｂ安全待机"
    "和黑万十战斗"
    window hide


    $ loadBG(0,"BG23E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA01"),"True","lh/FEI_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    hide screen phoneSD1
    $ stopvoc("FEI")
    play FEI "KYO07A_FEI0036"
    $ current_voice = "voice/KYO07A_FEI0036.ogg"
    "菲利斯" "「一，二……发射喵！」"


    stop bgm 
    hide screen phoneSD1
    $ loadBG(2,"BG_BLACK")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_05A.avi")
    hide screen invisible




    $ loadBG(2,"BG03A4")





    return
