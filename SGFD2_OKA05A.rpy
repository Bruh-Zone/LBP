label SGFD2_OKA05A:



    window hide


    $ loadBG(0,"BG05A1")
    play se "SGSE200L" loop



    $ date="8/11"
    python:
        cml = {}
        while len(rml)>0 and rml[0]["MetaData"]["Time"] > 740 and rml[0]["MetaData"]["Date"] == 811:
            UnreadMail(rml[0]["MailNumber"])
            notLate(rml[0]["MailNumber"])
            del rml[0]
        while len(sml)>0 and sml[0]["MetaData"]["Time"] > 740 and sml[0]["MetaData"]["Date"] == 811:
            del sml[0]
        while len(lml)>0 and gc["MailData"][lml[0]]["MetaData"]["Time"] > 740 and gc["MailData"][lml[0]]["MetaData"]["Date"] == 811:
            notLate(lml[0])
            del lml[0]
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0000"
    $ current_voice = "voice/OKA05A_OKA0000.ogg"
    "伦太郎" "「…………」"
    "夏日的阳光也尚未将天气变得太热。"
    "一早就叽叽喳喳的麻雀声，听起来很悦耳。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0000"
    $ current_voice = "voice/OKA05A_NAE0000.ogg"
    "绹" "「啊……冈伦叔叔，早上好……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0001"
    $ current_voice = "voice/OKA05A_NAE0001.ogg"
    "绹" "「真是早呢……」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0001"
    $ current_voice = "voice/OKA05A_OKA0001.ogg"
    "伦太郎" "「好！快点走吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0002"
    $ current_voice = "voice/OKA05A_NAE0002.ogg"
    "绹" "「啊，好的」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA05A_TEN0000"
    $ current_voice = "voice/OKA05A_TEN0000.ogg"
    "天王寺" "「冈部，你听好了。你要是把绹弄哭的话，我绝不会轻饶你的。从头到尾，都要给我好好照顾啊」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0002"
    $ current_voice = "voice/OKA05A_OKA0002.ogg"
    "伦太郎" "「我保证」"
    "不想看见绹哭泣的样子——这也是进行时间跳跃的原因。"
    hide screen phoneSD1
    window hide

    stop se




    $ loadBG(0,"BG22B0")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "FD2BGM05"

    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0003"
    $ current_voice = "voice/OKA05A_NAE0003.ogg"
    "绹" "「啊……」"
    "淀桥相机前已经排起了长队。"
    "仔细一看，果然大多数是转卖屋雇佣的打工者。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0003"
    $ current_voice = "voice/OKA05A_OKA0003.ogg"
    "伦太郎" "「队尾在那里。走吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0004"
    $ current_voice = "voice/OKA05A_NAE0004.ogg"
    "绹" "「嗯、嗯」"
    window hide



    $ loadBG(0,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0005"
    $ current_voice = "voice/OKA05A_NAE0005.ogg"
    "绹" "「真的，能买到吗？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0004"
    $ current_voice = "voice/OKA05A_OKA0004.ogg"
    "伦太郎" "「我们能买到的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0006"
    $ current_voice = "voice/OKA05A_NAE0006.ogg"
    "绹" "「诶，是吗……？」"
    call CHECK_RM_RECEIVE
    "但是，能买到游戏的只有我们。"
    call CHECK_RM_RECEIVE
    "大量排在后面的孩子们都会买不到游戏。"
    call CHECK_RM_RECEIVE
    "这种结局，绝不能允许。"


    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0005"
    $ current_voice = "voice/OKA05A_OKA0005.ogg"
    "伦太郎" "「绹，我去一下厕所」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0007"
    $ current_voice = "voice/OKA05A_NAE0007.ogg"
    "绹" "「啊……嗯」"
    "我让绹留在队伍中，而我则迅速向车站方向走去。"

    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"])
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]]["late"]=True

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG_BLACK")



    $ loadBG(0,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "FD2BGM07"


    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0006"
    $ current_voice = "voice/OKA05A_OKA0006.ogg"
    "伦太郎" "「拜托了，超级嗨客！请帮我查一下转卖屋的信息！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0000"
    $ current_voice = "voice/OKA05A_DAR0000.ogg"
    "至" "「都说了是超级黑客了。说起来为什么我要做这种事——」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0007"
    $ current_voice = "voice/OKA05A_OKA0007.ogg"
    "伦太郎" "「报酬是琉华子用过的足袋」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB02"),"True","lh/DAR_AMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0001"
    $ current_voice = "voice/OKA05A_DAR0001.ogg"
    "至" "「请务必让我来查！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0008"
    $ current_voice = "voice/OKA05A_OKA0008.ogg"
    "伦太郎" "「这才算是变态应有的样子嘛」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0002"
    $ current_voice = "voice/OKA05A_DAR0002.ogg"
    "至" "「不是哦！是名为变态的绅士！」"
    "在时间跳跃前，我拜托桶子查了查转卖屋的地址。"
    "我要惩罚的真正罪恶是转卖屋的头目——"
    "只要破坏了他们的组织，就不会发生孩子们拿不到游戏这种事了。"
    "为了这些，必须要获得邪恶的转卖屋组织的情报。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0009"
    $ current_voice = "voice/OKA05A_OKA0009.ogg"
    "伦太郎" "「但是，能这么简单的就查到吗？」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0003"
    $ current_voice = "voice/OKA05A_DAR0003.ogg"
    "至" "「总之先在Ｙａｈｏｏ上随便问了一下……哦，答案来啦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IP"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IP"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IP"])
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0004"
    $ current_voice = "voice/OKA05A_DAR0004.ogg"
    "至" "「不愧是定型文，回答得真快。看看开头……哦，陌生{color=#f00}ＩＰ{/color}回答的！已经闻到足袋的气味了！嗅嗅嗅嗅！」"
    "开始黑客活动后桶子的ＣＰＵ频率马上就上升了。"
    "虽然不知道他会怎么使用琉华子用过的足袋，但是只要我进行时间跳跃的话，这个机会就永远不会来到。"
    "可悲的超级嗨客。"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0005"
    $ current_voice = "voice/OKA05A_DAR0005.ogg"
    "至" "「真是太好了！能顺利的话我就在家里给你个吻。就这样就这样……成了！！」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0006"
    $ current_voice = "voice/OKA05A_DAR0006.ogg"
    "至" "「地址查明ｋｔｋｒ(ｋｔｋｒ)！！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0010"
    $ current_voice = "voice/OKA05A_OKA0010.ogg"
    "伦太郎" "「好、好快」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0007"
    $ current_voice = "voice/OKA05A_DAR0007.ogg"
    "至" "「呵呵呵……小看巫师级的黑客可不行哦！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0011"
    $ current_voice = "voice/OKA05A_OKA0011.ogg"
    "伦太郎" "「真不愧是三十岁的处男，竟然能用魔法！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA06"),"True","lh/DAR_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0008"
    $ current_voice = "voice/OKA05A_DAR0008.ogg"
    "至" "「不是啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0009"
    $ current_voice = "voice/OKA05A_DAR0009.ogg"
    "至" "「嘛，毕竟有货物需要处理，这么隐秘也是没办法的事」"
    "的确，不可能用真实的地址来进行物品交易。"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0010"
    $ current_voice = "voice/OKA05A_DAR0010.ogg"
    "至" "「那，怎么办？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0012"
    $ current_voice = "voice/OKA05A_OKA0012.ogg"
    "伦太郎" "「什么怎么办？」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0011"
    $ current_voice = "voice/OKA05A_DAR0011.ogg"
    "至" "「这种组织，街上到处都是」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0012"
    $ current_voice = "voice/OKA05A_DAR0012.ogg"
    "至" "「安全性很差，只靠一个邮箱地址就能全部看到了」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0013"
    $ current_voice = "voice/OKA05A_DAR0013.ogg"
    "至" "「我觉得随便找一下就能找出要命的信息来」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0013"
    $ current_voice = "voice/OKA05A_OKA0013.ogg"
    "伦太郎" "「呵——呵呵呵呵呵——」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0014"
    $ current_voice = "voice/OKA05A_OKA0014.ogg"
    "伦太郎" "「哇哈哈哈！桶子随你发挥！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0015"
    $ current_voice = "voice/OKA05A_OKA0015.ogg"
    "伦太郎" "「盘踞在秋叶原的罪恶组织，不能再让你们得逞下去了！」"
    window hide

    stop bgm 


    $ loadBG(0,"BG13A2")

    show screen phonebtn
    show screen phoneSD1

    play se "SGSE007L" loop

    "我知道自己的行为不值得赞扬。"
    "非法入侵，黑客活动。"
    "但是，这是为了正义，所以我已决定就算弄脏自己的手也不会在意。"
    window hide
    show expression "bg/BG10A3~ipad.jpg" as background :
        yalign 1.0
        linear 1.5yalign 0.2
    with dissolve


















    hide screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    "我仰望耸立在自己面前的{color=#f00}Ｒａｄｉｏ会馆{/color}"
    "转卖屋的仓库就在这里。"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM03"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0016"
    $ current_voice = "voice/OKA05A_OKA0016.ogg"
    "伦太郎" "「天在呼唤！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0017"
    $ current_voice = "voice/OKA05A_OKA0017.ogg"
    "伦太郎" "「地在呼唤！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0018"
    $ current_voice = "voice/OKA05A_OKA0018.ogg"
    "伦太郎" "「安第斯在呼唤！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0019"
    $ current_voice = "voice/OKA05A_OKA0019.ogg"
    "伦太郎" "「秋叶原中诞生的神秘英雄！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0020"
    $ current_voice = "voice/OKA05A_OKA0020.ogg"
    "伦太郎" "「羊驼人，登场！」"
    window hide

    $ loadBG(0,"IBG019A",png=True,hold=True)
    $ loadBG(0,"BG07A6")


    hide screen phonebtn
    hide screen phoneSD1
    stop bgm 
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0021"
    $ current_voice = "voice/OKA05A_OKA0021.ogg"
    "伦太郎" "「……呼」"
    window hide

    hide background-png 
    show screen phonebtn
    show screen phoneSD1
    with dissolve
    "戴上羊驼面具，报上名之后，我溜进了那幢楼里。"
    "距离天上掉下人工卫星已经过了一年了。"
    "虽然人工卫星已经被搬离，但建筑物中的租户仍然处于休业中。"

    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ01","")

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    "但是，部分事务所和仓库还在继续使用。"
    call CHECK_RM_RECEIVE
    "转卖屋肯定也是看中这点。"
    call CHECK_RM_RECEIVE
    "似乎从去年冬天开始就在这里租借仓库。"


    window hide
    play se "SGSE153"




    $ loadBG(0,"BG09A")

    "我终于找到了目标仓库。"
    "电子密码锁。"
    "但是桶子早就已经黑到了密码。"
    play se "SGSE353"

    "解除电子密码锁。"
    "打开门——"
    window hide
    play se "SGSE084"



    $ loadBG(2,"BG67A")



    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0022"
    $ current_voice = "voice/OKA05A_OKA0022.ogg"
    "伦太郎" "「果然……如此」"
    "仓库中等待交易的同人志堆积如山。"
    "还有一看就知道是盗版ＤＶＤ。"
    "据桶子黑入的邮件内容就能推测得知，转卖屋应该在暗地里进行非法软件销售。"
    "只要暴露这间仓库的存在，销售就无法继续进行……"
    "我迅速地拿出早就准备好的东西。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0023"
    $ current_voice = "voice/OKA05A_OKA0023.ogg"
    "伦太郎" "「羊驼七道具(Ｓｅｖｅｎ　Ｇｅａｒ)，——『Ｓａｌｓａ・Ｓｎａｋｅ』！！"
    "这是未来道具４号机「Ｍｕｄ・Ｓｎａｋｅ」的改良版。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0024"
    $ current_voice = "voice/OKA05A_OKA0024.ogg"
    "伦太郎" "「————」"
    "我深深地吸了一口气，让自己冷静下来，然后按下了Ｓａｌｓａ・Ｓｎａｋｅ的开关。"
    window hide

    play se "SGSE354L" loop
    show smoke 
    show sprinkler 


    "探测到飘出来的烟之后，Ｒａｄｉｏ会馆的烟雾警报器响了起来。"
    "喷水器从天花板上往下洒水，将仓库中的物品全部淋湿了。"
    "误以为是火灾的警察和消防队应该会迅速赶来。"
    "这样的应该就能发现这些盗版ＤＶＤ了。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0025"
    $ current_voice = "voice/OKA05A_OKA0025.ogg"
    "伦太郎" "「好。剩下的就是逃出——」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0000"
    $ current_voice = "voice/OKA05A_MAY0000.ogg"
    "真由理" "「羊驼人！救命！」"
    play bgm "BGM08"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0026"
    $ current_voice = "voice/OKA05A_OKA0026.ogg"
    "伦太郎" "「真由理！？」"
    $ stopvoc("Y10")
    play voc "OKA05A_Y100000"
    $ current_voice = "voice/OKA05A_Y100000.ogg"
    "？？？" "「喂、喂！你是什么人！！」"
    window hide


    $ loadBG(2,"BG_BLACK")









    hide smoke 
    hide sprinkler 

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC04"),"True","lh/MAY_ASC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(0,"BG09A",trans=ImageDissolve(im.Scale("mask/mask18.png",1024,576),0.5),hide=False)














    "就像是在追真由理一样，走廊那头出现了一个人影。"
    "果然这次真由理也被当成了人质吗？"
    "仔细一看，那人是在淀桥的队伍前发放购物款的人——"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0027"
    $ current_voice = "voice/OKA05A_OKA0027.ogg"
    "伦太郎" "「可恶！」"
    "原本的话，我会使用羊驼之力与他战斗，但是这次并不知道未来会怎样。"
    "而且，只要真由理有可能会变成人质，就不能认真地与他战斗。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0028"
    $ current_voice = "voice/OKA05A_OKA0028.ogg"
    "伦太郎" "「真由理，快点！ 」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0001"
    $ current_voice = "voice/OKA05A_MAY0001.ogg"
    "真由理" "「嗯……嗯！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE183L,false"


    stop se
    "我拉着真由理的手，拼命在走廊中奔跑。"
    "转卖屋的人也紧跟在身后——"






    show smoke 
    $ stopvoc("Y10")
    play voc "OKA05A_Y100001"
    $ current_voice = "voice/OKA05A_Y100001.ogg"
    "转卖屋" "「混蛋，站住！你怎么能对我的商品做这种事——喂！！」"


    $ stopvoc("Y10")
    play voc "OKA05A_Y100002"
    $ current_voice = "voice/OKA05A_Y100002.ogg"
    "转卖屋" "「唔，可恶！如果不把火扑灭，商品就会湿透，呜呜！咳咳！」"
    "男人被Ｓａｌｓａ·Ｓｎａｋｅ的的烟雾包围，身体无法动弹。"
    "这些烟雾中含有莎莎酱的刺激成分。"
    "只要被烟雾包围住，就无法控制自己的行动了。"
    "与Ｍｕｄ·Ｓｎａｋｅ不同的是，很难消灭烟雾的源头。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0029"
    $ current_voice = "voice/OKA05A_OKA0029.ogg"
    "伦太郎" "「——计划顺利」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA01"),"True","lh/MAY_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0030"
    $ current_voice = "voice/OKA05A_OKA0030.ogg"
    "伦太郎" "「走啦！真由理！」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0002"
    $ current_voice = "voice/OKA05A_MAY0002.ogg"
    "真由理" "「——嗯！」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"])

    window hide

    stop se

    stop se




    hide smoke 
    $ loadBG(0,"BG07A5")


    play se "SGSE183L" loop
    hide screen phonebtn
    "我一口气冲下楼梯——"
    "握住人质真由理的手——"
    "逃离罪恶组织，就算要逃到天涯海角——"
    "一直、一直逃到天荒地老——"
    "无论何时何地都要逃下去——！"
    hide screen phoneSD1
    window hide

    stop se

    stop se

    stop bgm 




    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ02","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call CHECK_RM_RECEIVE



    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ03_01"])

    $ loadBG(0,"BG08A2")

    show screen phonebtn
    show screen phoneSD1
    play se "SGSE355L" loop

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0031"
    $ current_voice = "voice/OKA05A_OKA0031.ogg"
    "伦太郎" "「哈哈哈！任务完成！」"
    "我一个人走在塞满了消防车和看热闹的人的车站前。"
    "顺利地救出了真由理，任务完成！"
    "剩下的就是等待消防员和警察惩罚转卖屋。"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG14A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA04"),"True","lh/NAE_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play se "SGSE007L" loop


    show screen phoneSD1

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0008"
    $ current_voice = "voice/OKA05A_NAE0008.ogg"
    "绹" "「啊！冈伦叔叔，来太晚了！」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0009"
    $ current_voice = "voice/OKA05A_NAE0009.ogg"
    "绹" "「你一直不回来，我好寂寞啊！」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0032"
    $ current_voice = "voice/OKA05A_OKA0032.ogg"
    "伦太郎" "「啊啊，抱歉抱歉」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0010"
    $ current_voice = "voice/OKA05A_NAE0010.ogg"
    "绹" "「…………哼」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0011"
    $ current_voice = "voice/OKA05A_NAE0011.ogg"
    "绹" "「满脸笑容，根本就没在反省」"
    "我作为羊驼人，完成了自己该完成的任务，自然会满面笑容——"
    stop se
    $ stopvoc("SDO")
    play SDO "OKA05A_SDO0000"
    $ current_voice = "voice/OKA05A_SDO0000.ogg"
    "４℃？" "「所以，究竟是怎么回事！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ALA03"),"True","lh/NAE_ALA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0012"
    $ current_voice = "voice/OKA05A_NAE0012.ogg"
    "绹" "「吓！」"
    "被身后传来的声音吓到，绹顿时绷直了身体。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play bgm "FD2BGM02"

    $ stopvoc("Y10")
    play voc "OKA05A_Y100003"
    $ current_voice = "voice/OKA05A_Y100003.ogg"
    "转卖屋" "「都说仓库被破坏，现在资金有危机，今天的工作终止。就此解散——」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SDO')",DynamicDisplayable(mouthanime,"SDO_DSA02"),"True","lh/SDO_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SDO")
    play SDO "OKA05A_SDO0001"
    $ current_voice = "voice/OKA05A_SDO0001.ogg"
    "４℃" "「你说中止就中止！我们可是从早上就开始排队了！」"
    $ stopvoc("Y06")
    play voc "OKA05A_Y060000"
    $ current_voice = "voice/OKA05A_Y060000.ogg"
    "５℃" "「没错没错！」"
    $ stopvoc("Y07")
    play voc "OKA05A_Y070000"
    $ current_voice = "voice/OKA05A_Y070000.ogg"
    "６℃" "「至少要给打工工资！」"
    "从火灾现场赶回来的转卖屋的人，开始中止购买的安排。"
    $ stopvoc("Y10")
    play voc "OKA05A_Y100004"
    $ current_voice = "voice/OKA05A_Y100004.ogg"
    "转卖屋" "「都说了，就算你们排在这里也不会有钱——」"
    $ stopvoc("SDO")
    play SDO "OKA05A_SDO0002"
    $ current_voice = "voice/OKA05A_SDO0002.ogg"
    "４℃" "「你们的事情Ｎｏ　Ｐｒｏｂｌｅｍ！是吧，各位！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "在４℃的召唤下，队伍中稀稀落落响起赞同的声音。"
    "转卖屋主瞬间就被包围了。"
    "被这么多人包围，肯定打不过。"
    "在争论了一会儿后，在付给了应付的工资后，队伍解散了。"
    $ stopvoc("Y10")
    play voc "OKA05A_Y100005"
    $ current_voice = "voice/OKA05A_Y100005.ogg"
    "转卖屋" "「可恶！赤字过头了。这件事该怎么解释才好？」"
    $ stopvoc("Y10")
    play voc "OKA05A_Y100006"
    $ current_voice = "voice/OKA05A_Y100006.ogg"
    "转卖屋" "「今天就是截止日期了……这下，头儿就……」"
    "擦身而过的转卖屋主说出这样的话。"
    "虽然有点可怜，但全是自作自受。"

    stop bgm fadeout 5
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0013"
    $ current_voice = "voice/OKA05A_NAE0013.ogg"
    "绹" "「冈伦叔叔，那个人——」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0033"
    $ current_voice = "voice/OKA05A_OKA0033.ogg"
    "伦太郎" "「啊，那人是坏人。应该要受到天罚」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0014"
    $ current_voice = "voice/OKA05A_NAE0014.ogg"
    "绹" "「不是，我不是问这个」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0015"
    $ current_voice = "voice/OKA05A_NAE0015.ogg"
    "绹" "「我觉得好像在什么地方见过那个人」"
    "绹自言自语的话中，明显夹杂着不安感在其中。"
    hide screen phoneSD1
    window hide




    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE



    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_FEI03_01"])

    $ loadBG(0,"BG05A2",trans=fade)


    play se "SGSE004L" loop
    show screen phoneSD1
    "我们顺利地买到雷ＮｅｔＡＢ３Ｄ，向显像管工房返回。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0016"
    $ current_voice = "voice/OKA05A_NAE0016.ogg"
    "绹" "「我回来了！」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0017"
    $ current_voice = "voice/OKA05A_NAE0017.ogg"
    "绹" "「爸爸，我回来了哦！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0018"
    $ current_voice = "voice/OKA05A_NAE0018.ogg"
    "绹" "「啊，咦？没人在？」"
    "嗯……好奇怪。"
    "在时间跳跃之前，的确店长有因为心情很好而给了我奖金。"
    "是因为时间错过了一点吗？"
    "还是说——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0019"
    $ current_voice = "voice/OKA05A_NAE0019.ogg"
    "绹" "「爸爸……扔下我，去哪了？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0034"
    $ current_voice = "voice/OKA05A_OKA0034.ogg"
    "伦太郎" "「没事的。肯定是出去买东西了吧」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0020"
    $ current_voice = "voice/OKA05A_NAE0020.ogg"
    "绹" "「真的吗？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0035"
    $ current_voice = "voice/OKA05A_OKA0035.ogg"
    "伦太郎" "「啊，肯定……是」"
    "我只能含混不清地糊弄过去。"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    "就这样，时间过去了。"
    hide screen phoneSD1
    window hide

    stop se




    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE



    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_RUK03_01"])

    $ loadBG(0,"BG05N3",trans=fade)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM23"

    $ stopvoc("SUZ")
    play SUZ "OKA05A_SUZ0000"
    $ current_voice = "voice/OKA05A_SUZ0000.ogg"
    "铃羽" "「呐，冈部伦太郎，还是把她送回家比较好吧？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0036"
    $ current_voice = "voice/OKA05A_OKA0036.ogg"
    "伦太郎" "「……是呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve




    $ loadBG(2,"BG39N1S1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA03"),"True","lh/NAE_AMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0021"
    $ current_voice = "voice/OKA05A_NAE0021.ogg"
    "绹" "「…………」"
    "绹安静地玩着游戏。"
    "明明拿到了期待已久的游戏，脸上的表情却不开心。"
    "但是，Ｍｒ．布朗却没有回家……"
    $ stopvoc("MOE")
    play MOE "OKA05A_MOE0000"
    $ current_voice = "voice/OKA05A_MOE0000.ogg"
    "？？？" "「………」"
    "这不是可爱到只要离开视线就会心痛的女儿吗？"
    "那个笨蛋父亲难道只溺爱到这种程度吗？"
    "还是说，难道——"
    $ stopvoc("MOE")
    play MOE "OKA05A_MOE0001"
    $ current_voice = "voice/OKA05A_MOE0001.ogg"
    "？？？" "「…………唔」"
    "如果我再像之前一样行动，世界就会像以前一样。"
    "时间跳跃前，Ｍｒ．布朗肯定是在家的。"
    "既然他没回来，肯定是因为我的行动——"
    stop bgm 
    $ stopvoc("MOE")
    play MOE "OKA05A_MOE0002"
    $ current_voice = "voice/OKA05A_MOE0002.ogg"
    "？？？" "「…………冈部君」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0037"
    $ current_voice = "voice/OKA05A_OKA0037.ogg"
    "伦太郎" "「嗯！」"
    window hide




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(2,"BG05N3",hide=False)



    "背后突然传来声音，我的思路一下子就断了。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0038"
    $ current_voice = "voice/OKA05A_OKA0038.ogg"
    "伦太郎" "「闪光的指压师(Ｓｈｉｎｉｎｇ　Ｆｉｎｇｅｒ)！什，什么时候！」"
    $ stopvoc("MOE")
    play MOE "OKA05A_MOE0003"
    $ current_voice = "voice/OKA05A_MOE0003.ogg"
    "萌郁" "「刚刚就在」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0039"
    $ current_voice = "voice/OKA05A_OKA0039.ogg"
    "伦太郎" "「什么！你这身手久经训练吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "OKA05A_MOE0004"
    $ current_voice = "voice/OKA05A_MOE0004.ogg"
    "萌郁" "「————」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB05"),"True","lh/MOE_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "指压师无视我的话，无言地敲着手机。"
    hide screen phonebtn


    $ targetmailid = gc["ScriptMacros"]["FM_OKA05A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "短信立刻传来。"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0040"
    $ current_voice = "voice/OKA05A_OKA0040.ogg"
    "伦太郎" "「……完全不明白」"

    "话说，之前是只发了短信吧。"

    "反正都只能用短信传达，活人特意过来也没意义。"

    "——就在这么想的时候。"

    "我发现萌郁的表情比平时的更青。"

    window hide


    call read_last_mail






    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0041"
    $ current_voice = "voice/OKA05A_OKA0041.ogg"
    "伦太郎" "「————」"
    play bgm "FD2BGM05"
    "怎么？"
    "这……到底……"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0022"
    $ current_voice = "voice/OKA05A_NAE0022.ogg"
    "绹" "「爸爸……？」"
    window hide
    call hide_phone

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "绹小声叫着，我赶紧跑进工房里面。"
    window hide
    play se "SGSE017"



    $ loadBG(2,"BG04A2")



    "首都圈Ｎｅｗｓ的新闻。"
    "字幕显示着「男子秋叶原站前跳楼自杀」的文字。"
    window hide


    $ loadBG(2,"IBG016D")



    hide screen phonebtn
    $ stopvoc("X01")
    play voc "OKA05A_X010000"
    $ current_voice = "voice/OKA05A_X010000.ogg"
    "新闻主播" "「确认死亡的是３０～４０岁左右的男性，警察现在正在加紧确认身份中」"
    "伴随着「现场提供」的字幕出现的照片中，记忆中的那个围裙倒在车站前——"
    "肯定是Ｍｒ．布朗不会错。"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0023"
    $ current_voice = "voice/OKA05A_NAE0023.ogg"
    "绹" "「呜呜——!」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0042"
    $ current_voice = "voice/OKA05A_OKA0042.ogg"
    "伦太郎" "「绹！」"
    window hide



    $ loadBG(2,"BG04A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ALA03"),"True","lh/NAE_ALA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    "似乎想要遮住从四面八方的Ｍｒ．布朗传来的视线，绹将身体缩成一团。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0043"
    $ current_voice = "voice/OKA05A_OKA0043.ogg"
    "伦太郎" "「没事的，没事」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ALA07"),"True","lh/NAE_ALA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0024"
    $ current_voice = "voice/OKA05A_NAE0024.ogg"
    "绹" "「呜、呜呜、呜……」"
    $ stopvoc("NAE")
    play NAE "OKA05A_NAE0025"
    $ current_voice = "voice/OKA05A_NAE0025.ogg"
    "绹" "「哇啊啊啊啊啊啊……！」"
    "小小的身体中，爆发出响亮的哭声。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "眼泪一直都没停下来。"
    "啊啊……我又没能守住约定。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG37N",trans=fade)


    show screen phonebtn
    show screen phoneSD1
    "Ｍｒ．布朗没有亲人。"
    "将葬礼等细节的事情，交给了跟他熟悉的工商会的人。"
    "绹被孤儿院带走了。但是在工作人员来领之前，不能让绹一个人呆着。"
    "讨论的结果是，打工战士与绹一起住一晚。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0044"
    $ current_voice = "voice/OKA05A_OKA0044.ogg"
    "伦太郎" "「拜托了」"
    $ stopvoc("SUZ")
    play SUZ "OKA05A_SUZ0001"
    $ current_voice = "voice/OKA05A_SUZ0001.ogg"
    "铃羽" "「交给我吧。这种事情，我很熟悉的」"
    "熟悉——啊。"
    "我有一天也会熟悉充满这种事的生活吧……"
    $ stopvoc("SUZ")
    play SUZ "OKA05A_SUZ0002"
    $ current_voice = "voice/OKA05A_SUZ0002.ogg"
    "铃羽" "「打起精神来，冈部伦太郎」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0045"
    $ current_voice = "voice/OKA05A_OKA0045.ogg"
    "伦太郎" "「嗯嗯，谢谢」"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn

    stop bgm 
    "道谢之后，走上回家路。"
    window hide
label L_RING_00:
    play se phonering






    $ loadBG(2,"BG16N3")



    "打电话过来的是桶子。"

    "就算通过时间跳跃来改变了过去，还是需要理解事件的因果关系。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

label L_RING_RECEIVE_00:




    stop se
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0046"
    $ current_voice = "voice/OKA05A_OKA0046.ogg"
    "伦太郎" "「喂，事情怎样了？」"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0014"
    $ current_voice = "voice/OKA05A_DAR0014.ogg"
    "至" "「感觉掌握大概了」"

    play bgm "BGM19"
    "先我一步回家的桶子，告诉了他实情内容后，迅速开始调查事件真相。"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0015"
    $ current_voice = "voice/OKA05A_DAR0015.ogg"
    "至" "「正如冈伦你预想的一样。从转卖屋的电脑邮箱中检索，『天王寺裕吾』的关键词找到了」"

    "使用时间跳跃的我改变了过去，但目的主要是与转卖屋相关的事情。"
    "如果这个改变了命运的话，也就是说——"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0016"
    $ current_voice = "voice/OKA05A_DAR0016.ogg"
    "至" "「看来显像管店长似乎是转卖屋的头目」"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0047"
    $ current_voice = "voice/OKA05A_OKA0047.ogg"
    "伦太郎" "「……这样啊」"
    "我一直都有疑问，为什么Ｍｒ．布朗，能够持续经营那种不赚钱的显像管工房。"
    "但如果像桶子说的一样，他要是有另一个身份的话就能说的通了。"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0017"
    $ current_voice = "voice/OKA05A_DAR0017.ogg"
    "至" "「从邮件中得到的还不止这些信息，似乎一定要向名叫Ｒｏｕｎｄｅｒ的组织交钱才行」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0018"
    $ current_voice = "voice/OKA05A_DAR0018.ogg"
    "至" "「看来转卖屋是Ｒｏｕｎｄｅｒ的资金源。似乎今天黄昏就是期限」"
    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0019"
    $ current_voice = "voice/OKA05A_DAR0019.ogg"
    "至" "「所以如果凑不够钱，无论发生什么都是可能的」"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0048"
    $ current_voice = "voice/OKA05A_OKA0048.ogg"
    "伦太郎" "「果然不是自杀啊」"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0020"
    $ current_voice = "voice/OKA05A_DAR0020.ogg"
    "至" "「不可能扔下小绹不管吧」"

    "全部都联系在一起了。"
    hide screen phoneSD1
    window hide

    hide screen phonemenu
    call hide_phone

    $ loadBG(0,"BG05A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "Ｍｒ．布朗不停地问绹最想要的物品的理由。"
    window hide


    $ loadBG(0,"IBG016C")

    "为什么会用同情的眼光看犯了罪的４℃。"
    window hide


    $ loadBG(0,"BG_BLACK")

    "最后，抛下最爱的绹，从屋顶上跳下的理由。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "Ｍｒ．布朗其实不是在淀桥发钱的最下端，而是组织这些的人吧。"
    "如果在现场的话，大概就能知道转卖屋能把雷ＮｅｔＡＢ３Ｄ搞到手吧。"
    window hide


    $ loadBG(0,"BG16N3")
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)


    show screen phoneSD1

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0021"
    $ current_voice = "voice/OKA05A_DAR0021.ogg"
    "至" "「但是完全没有被称为Ｒｏｕｎｄｅｒ的组织的头绪。看起来，像是某种秘密社团的样子」"




    "Ｒｏｕｎｄｅｒ……？"




    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0022"
    $ current_voice = "voice/OKA05A_DAR0022.ogg"
    "至" "「果然最终还是恶之秘密组织的阴谋……应该不是吧常考。冈伦，你知道Ｒｏｕｎｄｅｒ吗？」"




    "总觉得……在哪儿听过……"
    "这个……究竟，在哪儿……？"




    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0023"
    $ current_voice = "voice/OKA05A_DAR0023.ogg"
    "至" "「冈伦？咦？能听见吗？冈伦！」"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0049"
    $ current_voice = "voice/OKA05A_OKA0049.ogg"
    "伦太郎" "「啊，啊啊。没事」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0050"
    $ current_voice = "voice/OKA05A_OKA0050.ogg"
    "伦太郎" "「你都回去了，抱歉，还让你特意打电话过来」"

    $ stopvoc("DAR")
    play DAR "OKA05A_DAR0024"
    $ current_voice = "voice/OKA05A_DAR0024.ogg"
    "至" "「抱歉，我现在能做的只有这些了。那，明天见」"

    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0051"
    $ current_voice = "voice/OKA05A_OKA0051.ogg"
    "伦太郎" "「嗯嗯，明天见」"
    window hide
    hide screen phonemenu
    call hide_phone

    stop bgm 
    "总算回过点神来，挂断了电话。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    play bgm "FD2BGM06"
    "抬头看着天空，缓缓地走着。"
    "最初只是不想让绹哭泣而已。"
    "所以，要惩罚——让她哭泣的坏人４℃。"
    "但是４℃也是社会的受害者。"
    "他也不是喜欢吃白食，想要去转卖屋帮忙。"
    "这样的话，只有击溃真正的恶人——转卖屋。"
    "这个结果导致Ｍｒ．布朗死了。"
    "又让绹哭了。"
    "避免方法也有吧。"
    "打倒转卖屋那头的罪恶组织——「Ｒｏｕｎｄｅｒ」就行了。"
    "也许不管其他孩子有没有买到游戏，只要我们早点来排队就好了。"
    "但是——这样真的好吗？"
    "谁能说做这个选择，不会给别的人带来不幸？"
    "我们买到了一个游戏，就说明有一个人没有买到游戏吧。"
    "改变未来这种事——"
    "既是在救人，同时也是在选择不救人。"
    "只是在选择谁变得不幸。"

    stop bgm 
    "我们有这个权利吗？"
    hide screen phoneSD1
    window hide




    $ loadBG(0,"IBGX007",trans=fade)

    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("Y05")
    play voc "OKA05A_Y050000"
    $ current_voice = "voice/OKA05A_Y050000.ogg"
    "羊驼司令" "「不要想的太多了」"
    $ stopvoc("Y05")
    play voc "OKA05A_Y050001"
    $ current_voice = "voice/OKA05A_Y050001.ogg"
    "羊驼司令" "「只是个游戏吧」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0052"
    $ current_voice = "voice/OKA05A_OKA0052.ogg"
    "伦太郎" "「你怎么能明白我！」"
    window hide


    $ loadBG(2,"BG02N2",trans=fade)
    play se "SGSE356"






    play bgm "FD2BGM08"

    show screen phonebtn
    "愤怒的甩开手柄，游戏被重启了。"
    "画面中的羊驼司令消失了。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0053"
    $ current_voice = "voice/OKA05A_OKA0053.ogg"
    "伦太郎" "「你能明白我的什么……什么……！」"
    "不明白。"
    "不可能会明白。"
    "连我都不知道该怎么办。"
    "我接下来该做什么……"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0003"
    $ current_voice = "voice/OKA05A_MAY0003.ogg"
    "真由理" "「很难受吗？」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0054"
    $ current_voice = "voice/OKA05A_OKA0054.ogg"
    "伦太郎" "「诶……?」"
    "想也没有想就说道。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0055"
    $ current_voice = "voice/OKA05A_OKA0055.ogg"
    "伦太郎" "「你在说什么啊。怎么会难——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0004"
    $ current_voice = "voice/OKA05A_MAY0004.ogg"
    "真由理" "「请你，听好了」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0005"
    $ current_voice = "voice/OKA05A_MAY0005.ogg"
    "真由理" "「冈伦救了很多、很多次被当成人质的真由喜」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0006"
    $ current_voice = "voice/OKA05A_MAY0006.ogg"
    "真由理" "「这点是绝不会错的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0007"
    $ current_voice = "voice/OKA05A_MAY0007.ogg"
    "真由理" "「所以，冈伦是正义的伙伴」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0008"
    $ current_voice = "voice/OKA05A_MAY0008.ogg"
    "真由理" "「真由喜来保证」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0009"
    $ current_voice = "voice/OKA05A_MAY0009.ogg"
    "真由理" "「所以……没有必要难受」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0056"
    $ current_voice = "voice/OKA05A_OKA0056.ogg"
    "伦太郎" "「啊啊，这样啊」"
    "我不是想当正义的伙伴吗。"
    "平时很迟钝的真由理。"
    "不知为何成了坏人人质的真由理。"
    "只是想要救她而已。"
    "因为真由理是重要的Ｌａｂｍｅｍ。"
    "帮助伙伴是绝对的正义。"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0057"
    $ current_voice = "voice/OKA05A_OKA0057.ogg"
    "伦太郎" "「谢谢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0010"
    $ current_voice = "voice/OKA05A_MAY0010.ogg"
    "真由理" "「怎么了？」"
    "深深地向真由理鞠了一个躬。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0011"
    $ current_voice = "voice/OKA05A_MAY0011.ogg"
    "真由理" "「呐，冈伦？我能拜托你一件事吗」"
    $ stopvoc("MAY")
    play MAY "OKA05A_MAY0012"
    $ current_voice = "voice/OKA05A_MAY0012.ogg"
    "真由理" "「真由喜希望你能去帮助绹酱」"
    $ stopvoc("OKA")
    play OKA "OKA05A_OKA0058"
    $ current_voice = "voice/OKA05A_OKA0058.ogg"
    "伦太郎" "「啊，我知道」"
    "我的正义就在此处。"
    "真由理的愿望就是我的愿望。"
    "所以——"
    window hide



    $ loadBG(0,"BG03A4",trans=fade)


    stop bgm 
    "我脱下面具，戴上头盔。"
    window hide
    show houden 

    play se "SGSE035L" loop

    "作为正义的伙伴，朝着过去出发。"

    hide houden 
    hide screen phoneSD1
    hide screen phonebtn
    window hide
    stop se
    stop se
    stop bgm
    call timeleap (fromtime=[8,11,22,40], totime=[8,11,7,40], fromday=[4])

    return








    return
label IMTHD_XMA_01:





    return
