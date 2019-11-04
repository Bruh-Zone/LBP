label SGFD2_KYO01B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG21E")

    play bgm "BGM23"

    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "从开始潜伏到现在，大概过了一小时左右。"
    "虽然躲在阴影里确认着来往的人群，但是完全没有感觉ｉｃｈｓ出现过。"
    "接到了红莉栖的联系。"
    "琉华子好像在柳林神社里。"
    "没能接电话好像是因为去厕所了……"
    "嘛，那种事怎么都行。"
    "问题是之后说的话。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0000"
    $ current_voice = "voice/KYO01B_CRS0000.ogg"
    "红莉栖" "「说真由理没有来过……」"
    "我吞了一口口水。"
    "虽然十分不想这么想，但是也就是说那封恐吓信的可信度变高了。"
    "真由理不会是在去柳林神社的路上被ｉｃｈｓ绑架了吧？"
    "红莉栖说她去真由理可能去的地方找找看以后就挂了电话。"
    "心脏跳的很快。胃里隐隐作痛。"
    "在那之后不久，我又接到了琉华子的电话。"
    "『已经听牧濑说了。留言也听到了。在下也要去找真由理酱。』"
    "琉华子用颤抖的声音说道。"
    "那声音让我感到更加烦躁了。"
    "在和琉华子的通话结束后，手机又响了。"
    "但是那并不是我的手机。"
    window hide


    $ loadBG(2,"PBG03A")



    hide screen phonebtn
    show screen phoneSD1
    "而是真由理的。"
    "刚刚在Ｌａｂ里发现，下意识地放进了自己的口袋。"
    "发信人显示的是是“琉华君”。"
    "大概是红莉栖忘记告诉琉华子真由理忘记带手机这件事了吧。"
    "所以琉华子就给真由理打了电话……"
    "我没有按下通话键。"
    "电池剩下的不多了，所以想省着点。"
    "说不定会有其他重要人物通过手机联系真由理。"
    "为了那种时候，要保存电池。"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "在那之后，我联系了菲利斯。"
    "菲利斯也并不知道真由理的位置。"
    "『ＭａｙＱｕｅｅｎ＋Ｎｙａ²』里问了一遍也没有结果。"
    "给真由理家里打了电话，是她母亲接的。"
    "说她还没有回来。"
    "为了不让她操心，我并没有告诉她关于被诱拐的事情就挂了电话。"
    window hide




    show screen phonebtn
    show screen phoneSD1
    "这是……这一小时内发生的事。"
    "为了排解胃痛，我一手拿着豆沙面包，另一手拿着牛奶往嘴里灌。"
    window hide



    $ loadBG(0,"BG21E")

    "又过了５分钟——"
    "疑似犯人的身影依然没有见到。"
    "我将最后一点面包塞入口中，一口气喝完了剩下的牛奶。"
    "在手上剩下的是，面包的包装纸，和牛奶的盒子。"
    "也就是垃圾。"
    "虽然找了一下，但是并没有发现任何像垃圾桶的地方。"
    "无可奈何之下，我将包装纸和牛奶盒子捏成了棒状塞进了白大褂的口袋里。"
    "手伸进口袋的时候，指尖摸到了什么微妙的东西。"
    "是纸。口袋里有一张纸。"
    "我将它缓缓地抽了出来。"
    "似乎是传单一样的东西。"
    "对折了两次。"
    "用更加现代的说法就是Ｆｌｙｅｒ。"
    "打开了看一下，上面写着的内容是："
    window hide
    play se "SGSE221"



    $ loadBG(2,"IBG024A")



    hide screen phonebtn

    "『第８回秋叶原发明大赛』"
    "『大奖奖金：神神神神神马３００万！！！』"
    "『作品募集时间：２０１０年８月１日～８月３１日』"
    "『创在属于你的１％(光明)的未来！』"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0000"
    $ current_voice = "voice/KYO01B_OKA0000.ogg"
    "伦太郎" "「大奖奖金──３００万！？」"
    "在那个时候……"
    play se "SGSE315"

    "突然有谁从我身后拍了一下我的肩膀。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "我一个激灵向前一跃，同时转过身来，发现站在那里的是……"
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0001"
    $ current_voice = "voice/KYO01B_OKA0001.ogg"
    "伦太郎" "「克里斯提娜……」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0001"
    $ current_voice = "voice/KYO01B_CRS0001.ogg"
    "红莉栖" "「反应过度了吧」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0002"
    $ current_voice = "voice/KYO01B_OKA0002.ogg"
    "伦太郎" "「才不是吓了一跳呢。那是反击的架势」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0003"
    $ current_voice = "voice/KYO01B_OKA0003.ogg"
    "伦太郎" "「虽然你可能没注意到，但我刚才已经朝你挥出三下拳头了哦，次次都是在你鼻梁前停住的。捡了一条命啊你」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0002"
    $ current_voice = "voice/KYO01B_CRS0002.ogg"
    "红莉栖" "「那，ｉｃｈｓ呢？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0004"
    $ current_voice = "voice/KYO01B_OKA0004.ogg"
    "伦太郎" "「有在听我说话么……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB07"),"True","lh/CRS_AMB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0003"
    $ current_voice = "voice/KYO01B_CRS0003.ogg"
    "红莉栖" "「看你那副样子，看来是谁都没有出现啊」"
    "我咬着嘴里的肉，点了点头。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0005"
    $ current_voice = "voice/KYO01B_OKA0005.ogg"
    "伦太郎" "「差不多了吧，这样继续监视下去没有什么意义啊？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0004"
    $ current_voice = "voice/KYO01B_CRS0004.ogg"
    "红莉栖" "「为什么？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0006"
    $ current_voice = "voice/KYO01B_OKA0006.ogg"
    "伦太郎" "「ｉｃｈｓ肯定是在等待着我们的联络来行动的」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0007"
    $ current_voice = "voice/KYO01B_OKA0007.ogg"
    "伦太郎" "「『“惯例物品已经放入保险柜了。编号是多少多少』……没有那样的情报的话，来这里不是就变成白费力气了吗。」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0008"
    $ current_voice = "voice/KYO01B_OKA0008.ogg"
    "伦太郎" "「首先钥匙要怎么处理？如果保险柜锁着的话是没办法取出来的吧」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0009"
    $ current_voice = "voice/KYO01B_OKA0009.ogg"
    "伦太郎" "「恐怕ｉｃｈｓ会以某种形式告诉我们钥匙的转移方法……那家伙估计在那之后才会开始行动」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0005"
    $ current_voice = "voice/KYO01B_CRS0005.ogg"
    "红莉栖" "「那，我们试试吧？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0010"
    $ current_voice = "voice/KYO01B_OKA0010.ogg"
    "伦太郎" "「……诶？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0006"
    $ current_voice = "voice/KYO01B_CRS0006.ogg"
    "红莉栖" "「我是说再……试着联络一次。再给ｉｃｈｓ发一次邮件吧」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0007"
    $ current_voice = "voice/KYO01B_CRS0007.ogg"
    "红莉栖" "「『“惯例物品已经放入保险柜了。编号是……』邮件这么写的话……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0011"
    $ current_voice = "voice/KYO01B_OKA0011.ogg"
    "伦太郎" "「骗他吗……？」"
    "红莉栖利落地点了点头。"
    play se "SGSE803"

    "在那之后，手机响了。"
    "不是我的，而是真由理的。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG03A")



    hide screen phonebtn
    "打开之后发现有一封邮件。"
    "发件人是琉华子……"
    "打开看看。"
    "确认了一下内容。"
    window hide


    $ loadBG(2,"PBG13A")



    "是担心真由理的安全的邮件。"
    "恐怕是因为电话怎么都打不通，才会这么发邮件的吧。"
    "实在是令人佩服的行为。"
    "但（虽然对于琉华子来说很抱歉）这些邮件对于解决这个事件无济于事。"
    "在一旁看着手机屏幕的红莉栖也露出了丧气的表情。"
    window hide


    $ loadBG(2,"PBG03A")



    "我叹了口气，关掉了琉华子发来的邮件。"
    "然后将真由理的手机——"
    window hide

    stop bgm 



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0008"
    $ current_voice = "voice/KYO01B_CRS0008.ogg"
    "红莉栖" "「等等！」"
    "在那个时候，红莉栖突然叫了出来。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0009"
    $ current_voice = "voice/KYO01B_CRS0009.ogg"
    "红莉栖" "「刚才的邮件，能再给我看看吗？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0010"
    $ current_voice = "voice/KYO01B_CRS0010.ogg"
    "红莉栖" "「啊啊，不是邮件，而是要看看邮箱。想看收件箱。」"
    "我按照她的要求，打开了收件箱。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG14A")



    "那里有４封邮件。"
    "最上面的便是刚刚收到的琉华子发来的邮件。"
    "但，在那下面的是……？"
    "排成一串的三封邮件……"
    window hide


    $ loadBG(2,"PBG15A")






    $ loadBG(2,"PBG15B")






    $ loadBG(2,"PBG15C")




    play bgm "BGM25"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0012"
    $ current_voice = "voice/KYO01B_OKA0012.ogg"
    "伦太郎" "「Ｄ，Ｄｍａｉｌ……」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0011"
    $ current_voice = "voice/KYO01B_CRS0011.ogg"
    "红莉栖" "「果然……」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0012"
    $ current_voice = "voice/KYO01B_CRS0012.ogg"
    "红莉栖" "「因为有三封不在联系人的地址发来的邮件，所以就在想难道说……」"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0013"
    $ current_voice = "voice/KYO01B_OKA0013.ogg"
    "伦太郎" "「什么意思！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0013"
    $ current_voice = "voice/KYO01B_CRS0013.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0014"
    $ current_voice = "voice/KYO01B_OKA0014.ogg"
    "伦太郎" "「这３封邮件里的内容是什么意思！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0014"
    $ current_voice = "voice/KYO01B_CRS0014.ogg"
    "红莉栖" "「那种事，不可能知道吧。不管怎么看都是没有意义的字符串啊」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0015"
    $ current_voice = "voice/KYO01B_OKA0015.ogg"
    "伦太郎" "「把它们化为文字的话？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0015"
    $ current_voice = "voice/KYO01B_CRS0015.ogg"
    "红莉栖" "「或者试着找出里面的暗号？……」"
    "暗号……"
    "舌头的顶部有一种令人不快的感觉。"
    "是刚才喝下去的牛奶有一些残留在口中了。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0016"
    $ current_voice = "voice/KYO01B_CRS0016.ogg"
    "红莉栖" "「发送者是谁？ｉｃｈｓ还有其他人嘛？」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG15A")



    hide screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOMAIN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOMAIN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOMAIN"])
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0016"
    $ current_voice = "voice/KYO01B_OKA0016.ogg"
    "伦太郎" "「地址不一样啊。不管是账户名还是{color=#f00}域名{/color}。这个是『ｔａｂｏｏ．ｃｏ．ｊｐ』──」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0017"
    $ current_voice = "voice/KYO01B_CRS0017.ogg"
    "红莉栖" "「也就是用ＰＣ发送的邮件啊」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0017"
    $ current_voice = "voice/KYO01B_OKA0017.ogg"
    "伦太郎" "「我也觉得」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0018"
    $ current_voice = "voice/KYO01B_CRS0018.ogg"
    "红莉栖" "「『ｓｉｄｅｋｉｃｋ』这名字有线索吗？」"
    "我沉默着摇了摇头。"
    "那么问的话，也就意味着红莉栖也没有任何头绪咯。"
    "就算如此……"
    "就算如此……"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0018"
    $ current_voice = "voice/KYO01B_OKA0018.ogg"
    "伦太郎" "「到底在说什么会怎么样啊！　为什么一个连Ｌａｂｍｅｎ都不是的人会连续发送两封Ｄｍａｉｌ──！」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0019"
    $ current_voice = "voice/KYO01B_CRS0019.ogg"
    "红莉栖" "「发送的顺序，好像是反过来的呢」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0020"
    $ current_voice = "voice/KYO01B_CRS0020.ogg"
    "红莉栖" "「这里的Ｄｍａｉｌ的接受时间是１５点１８分吧？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0021"
    $ current_voice = "voice/KYO01B_CRS0021.ogg"
    "红莉栖" "「另一方面，ｉｃｈｓ发来的邮件的时间是──」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0019"
    $ current_voice = "voice/KYO01B_OKA0019.ogg"
    "伦太郎" "「１６点３分，发过来的……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0020"
    $ current_voice = "voice/KYO01B_OKA0020.ogg"
    "伦太郎" "「也就是两封邮件，其实是ｓｉｄｅｋｉｃｋ的先发，然后ｉｃｈｓ再发的」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0000"
    $ current_voice = "voice/KYO01B_SDO0000.ogg"
    "４℃？" "「呐」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0021"
    $ current_voice = "voice/KYO01B_OKA0021.ogg"
    "伦太郎" "「吵死了！　给我安静点！　在讨论大事呢！」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0001"
    $ current_voice = "voice/KYO01B_SDO0001.ogg"
    "４℃？" "「你，你这家伙……想死吗！？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0022"
    $ current_voice = "voice/KYO01B_OKA0022.ogg"
    "伦太郎" "「什么？」"

    stop bgm 
    "放下真由理的手机，我回过头去。"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    show screen phonebtn
    "在那里站着的是，比盖亚女神还要熠熠生辉的男子。"
    "恩？等等……"
    "这个男的，好像在哪里见过……"
    "开始在记忆里搜寻。"
    "眯上眼睛仔细打量了一会他之后，脑海中突然闪过一道亮光。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0023"
    $ current_voice = "voice/KYO01B_OKA0023.ogg"
    "伦太郎" "「４℃ー！　你这家伙就是，ｉｃｈｓ吗！」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0002"
    $ current_voice = "voice/KYO01B_SDO0002.ogg"
    "４℃" "「哈～？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DLA01"),"True","lh/SDO_DLA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    play bgm "FD2BGM02"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0024"
    $ current_voice = "voice/KYO01B_OKA0024.ogg"
    "伦太郎" "「真由理在哪里！　在哪里啊！」"
    "我抓住４℃的肩膀，前后左右激烈地摇晃着他。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DLA02"),"True","lh/SDO_DLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0003"
    $ current_voice = "voice/KYO01B_SDO0003.ogg"
    "４℃" "「喂，等等，你这……放开我，放开我啊……！」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0022"
    $ current_voice = "voice/KYO01B_CRS0022.ogg"
    "红莉栖" "「等，等等，怎么一回事啊，冈部！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0025"
    $ current_voice = "voice/KYO01B_OKA0025.ogg"
    "伦太郎" "「烦死了！　你安静点！」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0004"
    $ current_voice = "voice/KYO01B_SDO0004.ogg"
    "４℃" "「真由理什么的，我不知道啊！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0026"
    $ current_voice = "voice/KYO01B_OKA0026.ogg"
    "伦太郎" "「打算装傻吗，４℃ー！　不对，ｉｃｈｓ！」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0005"
    $ current_voice = "voice/KYO01B_SDO0005.ogg"
    "４℃" "「ｉｃｈｓ是什么鬼啊！　还有我也不叫什么４℃！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0027"
    $ current_voice = "voice/KYO01B_OKA0027.ogg"
    "伦太郎" "「『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』是你的账户！　肯定是这样吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DLA01"),"True","lh/SDO_DLA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0006"
    $ current_voice = "voice/KYO01B_SDO0006.ogg"
    "４℃" "「有没有人啊，有没有人过来下啊，这个人好奇怪～」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0028"
    $ current_voice = "voice/KYO01B_OKA0028.ogg"
    "伦太郎" "「真的吗！？　你是说你真的不知道！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DLA02"),"True","lh/SDO_DLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)






    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0007"
    $ current_voice = "voice/KYO01B_SDO0007.ogg"
    "４℃" "「所以说刚才不就说不知道了——吗！」"


    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    "当他说出最后一个字的时候，４℃把我的手强行甩开了。"
    "稍稍离开了些距离。"
    "视线向下移动的时候，我发现他的右手里握着一个危险的东西。"
    "看起来是棍子一样的东西……"
    "说起来棍状物的话……"
    "棍子→被打→领便当"
    "瞬间完成了这一联想的我摆出了“少侠，请三思！”的姿势。"
    "于是这么说了。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0029"
    $ current_voice = "voice/KYO01B_OKA0029.ogg"
    "伦太郎" "「少侠，请三思！」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0008"
    $ current_voice = "voice/KYO01B_SDO0008.ogg"
    "４℃" "「你说啥～？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0030"
    $ current_voice = "voice/KYO01B_OKA0030.ogg"
    "伦太郎" "「你是真的不知道邮件的事情吧？」"
    window hide





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC01"),"True","lh/CRS_ALC01a~ipad.png") at left_l as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0023"
    $ current_voice = "voice/KYO01B_CRS0023.ogg"
    "红莉栖" "「冈部……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0031"
    $ current_voice = "voice/KYO01B_OKA0031.ogg"
    "伦太郎" "「怎么了？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0024"
    $ current_voice = "voice/KYO01B_CRS0024.ogg"
    "红莉栖" "「ｉｃｈｓ发送的是Ｄｍａｉｌ」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0025"
    $ current_voice = "voice/KYO01B_CRS0025.ogg"
    "红莉栖" "「不管这个人是不是真的犯人，关于未来发送的邮件内容肯定是不知道的吧」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0009"
    $ current_voice = "voice/KYO01B_SDO0009.ogg"
    "４℃" "「喂，嘀嘀咕咕说些什么呢」"
    window hide



    hide lh5  with dissolve
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0032"
    $ current_voice = "voice/KYO01B_OKA0032.ogg"
    "伦太郎" "「明白了。那样的话就只有一件事想问一下，不对，想让你给我看一下，你的手机……」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0010"
    $ current_voice = "voice/KYO01B_SDO0010.ogg"
    "４℃" "「为什么啊？」"
    "我考虑了２秒钟后说道。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0033"
    $ current_voice = "voice/KYO01B_OKA0033.ogg"
    "伦太郎" "「你不是一直是杀马特时尚界的领军人物吗，所以想知道你超酷的非主流系手机是什么样的」"
    "当然是随便编的。"
    "但是好像４℃接受了这个说法，歪了歪嘴把手机给我看了。"
    "看起来不像是ｉｃｈｓ那种人会使用的手机机型。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0026"
    $ current_voice = "voice/KYO01B_CRS0026.ogg"
    "红莉栖" "「相信他不就好了嘛」"
    "我坦率地道了歉。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0034"
    $ current_voice = "voice/KYO01B_OKA0034.ogg"
    "伦太郎" "「不好意思，似乎搞错人了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0011"
    $ current_voice = "voice/KYO01B_SDO0011.ogg"
    "４℃" "「搞了半天是搞错人了吗，呆子！」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0027"
    $ current_voice = "voice/KYO01B_CRS0027.ogg"
    "红莉栖" "「嘛嘛，消消火消消火……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0035"
    $ current_voice = "voice/KYO01B_OKA0035.ogg"
    "伦太郎" "「我说４℃啊」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0012"
    $ current_voice = "voice/KYO01B_SDO0012.ogg"
    "４℃" "「是四度！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0036"
    $ current_voice = "voice/KYO01B_OKA0036.ogg"
    "伦太郎" "「啊啊，是哦。数字的四，温度的度，所以是四度啊。」（注：冈伦之前一直按照训读来发音，属于叫错别人名字）"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0013"
    $ current_voice = "voice/KYO01B_SDO0013.ogg"
    "４℃" "「为，为什么，你会知道……？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0037"
    $ current_voice = "voice/KYO01B_OKA0037.ogg"
    "伦太郎" "「知道就是知道啦，我也不知道为什么我会知道」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0038"
    $ current_voice = "voice/KYO01B_OKA0038.ogg"
    "伦太郎" "「比起那个四度，你在这种地方干什么？」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0014"
    $ current_voice = "voice/KYO01B_SDO0014.ogg"
    "４℃" "「那是我的台词啊。你为什么在这里逗留了１个小时以上了？」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0015"
    $ current_voice = "voice/KYO01B_SDO0015.ogg"
    "４℃" "「很麻烦诶，打扰我工作，快点消失吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0016"
    $ current_voice = "voice/KYO01B_SDO0016.ogg"
    "４℃" "「否则的话，就要卷入我超不妙的黑色光环咯？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0039"
    $ current_voice = "voice/KYO01B_OKA0039.ogg"
    "伦太郎" "「什么工作？　难道你这家伙受雇于ｉｃｈｓ──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA01"),"True","lh/SDO_DSA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0017"
    $ current_voice = "voice/KYO01B_SDO0017.ogg"
    "４℃" "「才不是呢，雇主什么的我才没有呢」"
    $ stopvoc("SDO")
    play SDO "KYO01B_SDO0018"
    $ current_voice = "voice/KYO01B_SDO0018.ogg"
    "４℃" "「作为非主流不良界顶点的本大爷，被谁给支配什么的——糟糕！」"
    window hide
    play se "SGSE182"

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "一瞬间的事。"
    "４℃看到我身后的什么东西，转过身去拔腿就跑。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "回头看去是一辆警车。"
    "警车徐徐地开着，什么事也没有的样子经过了这里。"
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0028"
    $ current_voice = "voice/KYO01B_CRS0028.ogg"
    "红莉栖" "「那家伙，是谁……？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0040"
    $ current_voice = "voice/KYO01B_OKA0040.ogg"
    "伦太郎" "「大概是在别的世界线见过吧。」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0029"
    $ current_voice = "voice/KYO01B_CRS0029.ogg"
    "红莉栖" "「此话怎讲？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0041"
    $ current_voice = "voice/KYO01B_OKA0041.ogg"
    "伦太郎" "「抱歉……没法好好说嘛。记忆到现在也很混乱」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0042"
    $ current_voice = "voice/KYO01B_OKA0042.ogg"
    "伦太郎" "「我既记不清到现在为止已经经历过的世界线，也不清楚这条世界线是怎样的世界线」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0043"
    $ current_voice = "voice/KYO01B_OKA0043.ogg"
    "伦太郎" "「不如说我想问问你，这里到底是怎样的世界线？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0030"
    $ current_voice = "voice/KYO01B_CRS0030.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0044"
    $ current_voice = "voice/KYO01B_OKA0044.ogg"
    "伦太郎" "「你知道铃羽吗？　阿万音铃羽」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0031"
    $ current_voice = "voice/KYO01B_CRS0031.ogg"
    "红莉栖" "「当然了。在{color=#f00}显像管工房{/color}打过工的孩子不是吗？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0045"
    $ current_voice = "voice/KYO01B_OKA0045.ogg"
    "伦太郎" "「『打过工』……是过去式啊」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0032"
    $ current_voice = "voice/KYO01B_CRS0032.ogg"
    "红莉栖" "「因为不久之前不是辞掉了吗」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0046"
    $ current_voice = "voice/KYO01B_OKA0046.ogg"
    "伦太郎" "「{color=#f00}广播馆{/color}的时——人工卫星呢？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0033"
    $ current_voice = "voice/KYO01B_CRS0033.ogg"
    "红莉栖" "「虽然不知道有什么联系，但是突然那个消失了」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0047"
    $ current_voice = "voice/KYO01B_OKA0047.ogg"
    "伦太郎" "「是吗……。是这样啊……」"
    "胸膛变得愈发沉重。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"IBGX075")

    hide screen phonebtn
    "在Ｌａｂ的开发室里有ＩＢＮ５１００。"
    "也就是说……是那么回事……"
    "虽然已经隐约察觉到了事实，但是这血淋淋的显示摆在眼前还是让我有些胸痛。"
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA04"),"True","lh/CRS_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0048"
    $ current_voice = "voice/KYO01B_OKA0048.ogg"
    "伦太郎" "「秋叶原还是御宅圣地吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0034"
    $ current_voice = "voice/KYO01B_CRS0034.ogg"
    "红莉栖" "「哈……？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0049"
    $ current_voice = "voice/KYO01B_OKA0049.ogg"
    "伦太郎" "「不，不用回答了。到这里来的时候已经看到了」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0050"
    $ current_voice = "voice/KYO01B_OKA0050.ogg"
    "伦太郎" "「街上满是萌系商店。」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0051"
    $ current_voice = "voice/KYO01B_OKA0051.ogg"
    "伦太郎" "「Ａｎｉｍａｔｅ，虎之穴，Ｍａｎｄａｒａｋｅ，Ｇａｍｅｒｓ，ＬＡＭＭＴＡＲＲＡ，Ｍｅｌｏｎｂｏｏｋｓ，ａｓｏｂｉｃｉｔｙ都好好的在那里啊」（注：都是秋叶原有名的同人店）"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0035"
    $ current_voice = "voice/KYO01B_CRS0035.ogg"
    "红莉栖" "「所以……怎么了？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0052"
    $ current_voice = "voice/KYO01B_OKA0052.ogg"
    "伦太郎" "「琉华子是男的吗？」"
    "没有回答她的问题，我继续问了下去。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0036"
    $ current_voice = "voice/KYO01B_CRS0036.ogg"
    "红莉栖" "「虽然是那么听说的，但果然不是吗？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0053"
    $ current_voice = "voice/KYO01B_OKA0053.ogg"
    "伦太郎" "「不对，是男的。本就应该是男的……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0054"
    $ current_voice = "voice/KYO01B_OKA0054.ogg"
    "伦太郎" "「如果不是那样的话，真由理的手机的地址簿里就不会登陆『琉华君』这样的名字了。」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0055"
    $ current_voice = "voice/KYO01B_OKA0055.ogg"
    "伦太郎" "「如果是女生的话，登录名不是『琉华酱』就很奇怪了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0037"
    $ current_voice = "voice/KYO01B_CRS0037.ogg"
    "红莉栖" "「明白了，明白了」"
    "红莉栖有些无奈地说。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0038"
    $ current_voice = "voice/KYO01B_CRS0038.ogg"
    "红莉栖" "「你刚刚说的话里，有９９％我无法理解，但剩下的１％算是理解了」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0039"
    $ current_voice = "voice/KYO01B_CRS0039.ogg"
    "红莉栖" "「比如说你常说的“Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ”发动了吧？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0040"
    $ current_voice = "voice/KYO01B_CRS0040.ogg"
    "红莉栖" "「你是因为在别的世界线发送了Ｄｍａｉｌ，然后移动到了这条世界线上……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0056"
    $ current_voice = "voice/KYO01B_OKA0056.ogg"
    "伦太郎" "「不对，不对啊，克里斯提娜。事情并非那么简单」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0057"
    $ current_voice = "voice/KYO01B_OKA0057.ogg"
    "伦太郎" "「话说回来，虽然很在意刚才的事……」"
    "我用手指推了推并不存在的眼镜继续说下去。"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0058"
    $ current_voice = "voice/KYO01B_OKA0058.ogg"
    "伦太郎" "「听好了，助手哟！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0059"
    $ current_voice = "voice/KYO01B_OKA0059.ogg"
    "伦太郎" "「恐怕我——进行了时间跳跃！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "瞬间冷场……"
    "红莉栖就像个中了石化咒语的村民Ａ一样呆在那里，最终静静地吐了一口气说道。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0041"
    $ current_voice = "voice/KYO01B_CRS0041.ogg"
    "红莉栖" "「骗人……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0060"
    $ current_voice = "voice/KYO01B_OKA0060.ogg"
    "伦太郎" "「并不是骗人」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0042"
    $ current_voice = "voice/KYO01B_CRS0042.ogg"
    "红莉栖" "「开玩笑的……？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0061"
    $ current_voice = "voice/KYO01B_OKA0061.ogg"
    "伦太郎" "「并不是开玩笑，我是从这条世界线上的未来１６点左右的时间跳跃过来的。」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0043"
    $ current_voice = "voice/KYO01B_CRS0043.ogg"
    "红莉栖" "「也就是说使用了时间机器！？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0062"
    $ current_voice = "voice/KYO01B_OKA0062.ogg"
    "伦太郎" "「是的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0044"
    $ current_voice = "voice/KYO01B_CRS0044.ogg"
    "红莉栖" "「为什么！？　不是说不进行实验吗！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0063"
    $ current_voice = "voice/KYO01B_OKA0063.ogg"
    "伦太郎" "「理由并不清楚，看起来记不得了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0045"
    $ current_voice = "voice/KYO01B_CRS0045.ogg"
    "红莉栖" "「和刚刚说的不同，不是感觉记得很清楚么？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0046"
    $ current_voice = "voice/KYO01B_CRS0046.ogg"
    "红莉栖" "「就好像记得别的世界线的事情一样」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0064"
    $ current_voice = "voice/KYO01B_OKA0064.ogg"
    "伦太郎" "「啊啊，确实呢。但这个世界线的事情我真的不清楚！」"
    "我从口袋里取出传单，摆到红莉栖的眼前。"
    window hide


    $ loadBG(2,"IBG024A")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0065"
    $ current_voice = "voice/KYO01B_OKA0065.ogg"
    "伦太郎" "「这个传单是什么啊！秋叶原发明大赛！？我可没记得往口袋里放过这种东西！」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"IBG023A")

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0066"
    $ current_voice = "voice/KYO01B_OKA0066.ogg"
    "伦太郎" "「那个素描簿也是！我可不记得我们神圣的未来道具研究所里有那样的东西存在」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0067"
    $ current_voice = "voice/KYO01B_OKA0067.ogg"
    "伦太郎" "「还有真由理的事也是──！　真由理被诱拐什么的历史我可没有听说过……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0068"
    $ current_voice = "voice/KYO01B_OKA0068.ogg"
    "伦太郎" "「我什么也……不知道啊……」"
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0047"
    $ current_voice = "voice/KYO01B_CRS0047.ogg"
    "红莉栖" "「…………」"
    "在我这么自暴自弃地说完之后，红莉栖难过地皱着眉头，移开了视线。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NET_CAFE"])
    "{color=#f00}ＮｅｔＣａｆｅ{/color}的痛车奏着喧嚣的音乐开了过去。"
    "就算它离开了，周围并没有安静下来。"
    "街道的喧嚣放佛要来添乱似的，在大楼的片隅之间穿梭着。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0048"
    $ current_voice = "voice/KYO01B_CRS0048.ogg"
    "红莉栖" "「失败了啊……」"
    "失败……？"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0049"
    $ current_voice = "voice/KYO01B_CRS0049.ogg"
    "红莉栖" "「记忆数据的传送失败。复制和粘贴出了问题」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0050"
    $ current_voice = "voice/KYO01B_CRS0050.ogg"
    "红莉栖" "「说不定冈部的假说是对的呢」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0051"
    $ current_voice = "voice/KYO01B_CRS0051.ogg"
    "红莉栖" "「『向过去发送的数据，有会因为某些误差而导致分形构造化的可能性』……这么说过吧？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0069"
    $ current_voice = "voice/KYO01B_OKA0069.ogg"
    "伦太郎" "「所以因此我才……失去了记忆？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0052"
    $ current_voice = "voice/KYO01B_CRS0052.ogg"
    "红莉栖" "「不知道……。虽然不知道，但是也可能是这样的呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0053"
    $ current_voice = "voice/KYO01B_CRS0053.ogg"
    "红莉栖" "「总而言之，有一件事是肯定的。时间跳跃机器是残次品这一点」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0070"
    $ current_voice = "voice/KYO01B_OKA0070.ogg"
    "伦太郎" "「不对，不应该是这样，别的世界上的机能是正常的。」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0054"
    $ current_voice = "voice/KYO01B_CRS0054.ogg"
    "红莉栖" "「那，看来是这条世界线上我犯了什么错误吧。估计是有什么巨大的ＢＵＧ吧」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0071"
    $ current_voice = "voice/KYO01B_OKA0071.ogg"
    "伦太郎" "「…………」"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    "抬头看去，天空一片血红……"
    "夜色缓缓地从东边迫近了。"
    window hide



    $ loadBG(2,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0055"
    $ current_voice = "voice/KYO01B_CRS0055.ogg"
    "红莉栖" "「呐冈部，再问一次啊，真的不记得时间跳跃之前的事情了？」"
    "我点了点头。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0056"
    $ current_voice = "voice/KYO01B_CRS0056.ogg"
    "红莉栖" "「那样的话，怎么说呢，有点……糟糕吧？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0072"
    $ current_voice = "voice/KYO01B_OKA0072.ogg"
    "伦太郎" "「怎么说？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0057"
    $ current_voice = "voice/KYO01B_CRS0057.ogg"
    "红莉栖" "「刚才说过了，冈部你自己说过不进行时间机器的实验吧？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0058"
    $ current_voice = "voice/KYO01B_CRS0058.ogg"
    "红莉栖" "「就算这样，你还是使用了时间机器从１６点跳到了现在」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0059"
    $ current_voice = "voice/KYO01B_CRS0059.ogg"
    "红莉栖" "「也就是说，在使用时间机器之前，肯定发生了什么特别严重的事情吧」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0060"
    $ current_voice = "voice/KYO01B_CRS0060.ogg"
    "红莉栖" "「肯定是因为那个，才陷入了不得不使用时间机器的境地吧」"
    "感觉自己起了鸡皮疙瘩。"
    "我感到自己的皮肤上的汗腺正在一个个打开。"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0061"
    $ current_voice = "voice/KYO01B_CRS0061.ogg"
    "红莉栖" "「虽然说过问了好几次了，但能不能再试着想想发生了什么？」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0062"
    $ current_voice = "voice/KYO01B_CRS0062.ogg"
    "红莉栖" "「时间跳跃前发生了什么吗……也就是现在开始会发生什么……」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0063"
    $ current_voice = "voice/KYO01B_CRS0063.ogg"
    "红莉栖" "「如果不行的话，那就试着从现在会发生什么开始想想吧，能以此作为头绪也说不定。」"
    "看了看手表，１８点１３分。"
    "这个时候，我在干什么？"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0073"
    $ current_voice = "voice/KYO01B_OKA0073.ogg"
    "伦太郎" "「哦对了，克里斯提娜，这个时候我和你正在买东西啊」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0064"
    $ current_voice = "voice/KYO01B_CRS0064.ogg"
    "红莉栖" "「买什么东西？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0074"
    $ current_voice = "voice/KYO01B_OKA0074.ogg"
    "伦太郎" "「开发评议会用的。」"
    "决定不使用时间机器。"
    "但是还是，要庆祝一下完成，所以就打算举行名为开发评议会……的宴会。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0065"
    $ current_voice = "voice/KYO01B_CRS0065.ogg"
    "红莉栖" "「好奇怪啊。和我去买东西的，不是桥田吗……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0075"
    $ current_voice = "voice/KYO01B_OKA0075.ogg"
    "伦太郎" "「啊啊，是啊，这条世界线变成了这样。」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0076"
    $ current_voice = "voice/KYO01B_OKA0076.ogg"
    "伦太郎" "「但是我所知道的那条世界线上，去买东西的可是我和你。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0066"
    $ current_voice = "voice/KYO01B_CRS0066.ogg"
    "红莉栖" "「唔……。那么那条世界线上后来发生了什么……？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0077"
    $ current_voice = "voice/KYO01B_OKA0077.ogg"
    "伦太郎" "「买完了以后我们回了Ｌａｂ，桌子上放着３片ＰＩＺＺＡ外卖。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0067"
    $ current_voice = "voice/KYO01B_CRS0067.ogg"
    "红莉栖" "「有３片？谁吃啊？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0078"
    $ current_voice = "voice/KYO01B_OKA0078.ogg"
    "伦太郎" "「这个问题太弱智了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0068"
    $ current_voice = "voice/KYO01B_CRS0068.ogg"
    "红莉栖" "「桥田吃了大部分吧？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0079"
    $ current_voice = "voice/KYO01B_OKA0079.ogg"
    "伦太郎" "「正是如此，拜托买披萨的就是他。在我们出去买东西的时候下的订单」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0069"
    $ current_voice = "voice/KYO01B_CRS0069.ogg"
    "红莉栖" "「在那之后呢？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0080"
    $ current_voice = "voice/KYO01B_OKA0080.ogg"
    "伦太郎" "「在那之后……在那之后呢……那个……」"
    hide screen phoneSD1
    window hide

    stop bgm 


    $ loadBG(0,"BG01N")

    hide screen phonebtn
    "宴会的中途……"
    "从没有关掉的电视里……"
    "传出了紧急报告的……声音……"
    window hide


    $ loadBG(0,"IBGX099")
    play se "SGSE052"


    "——————。"
    window hide
    window hide


    $ loadBG(0,"BG21E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM09"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0081"
    $ current_voice = "voice/KYO01B_OKA0081.ogg"
    "伦太郎" "「糟了……」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0070"
    $ current_voice = "voice/KYO01B_CRS0070.ogg"
    "红莉栖" "「……诶？」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0082"
    $ current_voice = "voice/KYO01B_OKA0082.ogg"
    "伦太郎" "「糟糕了……糟糕了啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0071"
    $ current_voice = "voice/KYO01B_CRS0071.ogg"
    "红莉栖" "「什，什么啊……。也就是说发生了什么？」"
    "埋藏在脑海深处的记忆……"
    "以为早已愈合的伤痕……"
    "复苏了……"
    "是那样的鲜明……"
    "就好像被洗刷过无数次般……"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"EVX_M05A",over=True)







    hide screen phonebtn
    "不对，等等！不要慌，冷静下来！那是别的世界线的事情吧！？"
    "并不是这个在Ｌａｂ里有素描簿，还拿着发明比赛的传单的世界线的事情！"
    "虽然脑袋里明白了，胸口的躁动还是无法抑制。"
    "心脏砰砰直跳。"
    "被切开的身体里的汗腺不断地喷涌着粘性的液体。"
    "怎么办才好……。该怎么办……"
    "总之先要确认真由理的人身安全……"
    "那样的话要做的事只有一件。"
    "——用Ｄｍａｉｌ！"
    window hide
    hide background-over 
    with dissolve




    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我飞快地取出手机，给桶子挂了电话。"
    window hide





    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0083"
    $ current_voice = "voice/KYO01B_OKA0083.ogg"
    "伦太郎" "「桶子！　是我啊！」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0000"
    $ current_voice = "voice/KYO01B_DAR0000.ogg"
    "至" "「小冈伦！　真由氏怎样了！？」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0084"
    $ current_voice = "voice/KYO01B_OKA0084.ogg"
    "伦太郎" "「还没有找啊哦。但是找她的方法只有一个」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0001"
    $ current_voice = "voice/KYO01B_DAR0001.ogg"
    "至" "「是什么……？」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0085"
    $ current_voice = "voice/KYO01B_OKA0085.ogg"
    "伦太郎" "「是Ｄｍａｉｌ。用Ｄｍａｉｌ吧」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0072"
    $ current_voice = "voice/KYO01B_CRS0072.ogg"
    "红莉栖" "「等，等等冈部！」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0086"
    $ current_voice = "voice/KYO01B_OKA0086.ogg"
    "伦太郎" "「吵死了，你先安静点！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0087"
    $ current_voice = "voice/KYO01B_OKA0087.ogg"
    "伦太郎" "「桶子，以最快速度做好{color=#f00}电话微波炉（暂）{/color}的准备！」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0002"
    $ current_voice = "voice/KYO01B_DAR0002.ogg"
    "至" "「Ｏ、ＯＫ！　发送对象和时间为？」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0088"
    $ current_voice = "voice/KYO01B_OKA0088.ogg"
    "伦太郎" "「发送对象是我的手机。时间……那个……确定真由理还在Ｌａｂ的时间是？」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0003"
    $ current_voice = "voice/KYO01B_DAR0003.ogg"
    "至" "「１５点１６分。从刚才手机里的通话来看肯定没问题」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0089"
    $ current_voice = "voice/KYO01B_OKA0089.ogg"
    "伦太郎" "「什么意思……？」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0004"
    $ current_voice = "voice/KYO01B_DAR0004.ogg"
    "至" "「刚想起来，和牧濑氏一起买东西的时候，接到过真由理的电话」"
    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0005"
    $ current_voice = "voice/KYO01B_DAR0005.ogg"
    "至" "「要买什么零食，在这点上我和牧濑氏起了分歧，最后就交给真由氏决定了……」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0090"
    $ current_voice = "voice/KYO01B_OKA0090.ogg"
    "伦太郎" "「那个时候她确实在Ｌａｂ吗？」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0006"
    $ current_voice = "voice/KYO01B_DAR0006.ogg"
    "至" "「恩。『还没去琉华氏那里吗？』这么问了，回答说『就要出发了呢』"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0091"
    $ current_voice = "voice/KYO01B_OKA0091.ogg"
    "伦太郎" "「明白了，那么就发送到那个时间点吧。计算就……交给你了」"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0007"
    $ current_voice = "voice/KYO01B_DAR0007.ogg"
    "至" "「了解！　叫做魔改造太好了」"

    "恩？魔改造？什么东西？"
    "虽然那么问了，但是并没有得到答复。"
    "大概是桶子已经放下了手机，开始做准备了吧。"
    "嘛也好。我们这边也有必须要做的事情。"
    "输入Ｄｍａｉｌ的文章。"
    "我的手机要和桶子保持通话，所以用了真由理的手机。"
    hide screen phoneSD1
    window hide


    call hide_phone
    $ loadBG(2,"PBG16A")



    hide screen phonebtn
    "发送目标自然是电话微波炉（暂）。"
    "内容如下。"
    window hide







    stop se


    $ loadBG(2,"PBG16B")
    pause










    stop se


    $ loadBG(2,"PBG16C")
    pause










    stop se


    $ loadBG(2,"PBG16D")
    pause








    $ loadBG(2,"BG21E")
    pause

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0073"
    $ current_voice = "voice/KYO01B_CRS0073.ogg"
    "红莉栖" "「呐，果然还是冷静些好好考虑……」"
    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0092"
    $ current_voice = "voice/KYO01B_OKA0092.ogg"
    "伦太郎" "「我很冷静」"
    $ stopvoc("CRS")
    play CRS "KYO01B_CRS0074"
    $ current_voice = "voice/KYO01B_CRS0074.ogg"
    "红莉栖" "「并看不出来……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "眼下最优先事项是确保真由理的人身安全。"
    "虽然还没能确定被诱拐了，但事实是怎样都好了。"
    "发送了这封Ｄｍａｉｌ的话，真由理就——"
    window hide





    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0008"
    $ current_voice = "voice/KYO01B_DAR0008.ogg"
    "至" "「冈伦，准备好了！」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0093"
    $ current_voice = "voice/KYO01B_OKA0093.ogg"
    "伦太郎" "「好！　电话微波炉（暂）、启动！」"
    "我从手机里听到了啪啦啪啦的火花声。"

    $ stopvoc("DAR")
    play DAR "KYO01B_DAR0009"
    $ current_voice = "voice/KYO01B_DAR0009.ogg"
    "至" "「放电现象来了——！」"

    $ stopvoc("OKA")
    play OKA "KYO01B_OKA0094"
    $ current_voice = "voice/KYO01B_OKA0094.ogg"
    "伦太郎" "「了解！」"
    hide screen phoneSD1
    window hide

    stop bgm 


    $ loadBG(2,"PBG16D")



    hide screen phonebtn
    "我如此宣言道，按下了——真由理手机的发送按钮。"

    window hide


    $ loadBG(2,"PBG16E")




    stop bgm 
    stop se
    stop se


    $ loadBG(2,"PBG16F")
    play se "SGSE164"





    hide screen phoneSD1



    $ loadBG(2,"BG23E")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_01A.avi")
    hide screen invisible




    return






    return




    $ loadBG(0,"BG23E")

    return
