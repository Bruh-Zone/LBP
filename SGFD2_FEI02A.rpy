label SGFD2_FEI02A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide



    $ loadBG(0,"BG16A1")


    play se "SGSE007L" loop


    $ date="8/8"
    $ day = "SUN"
    show screen phonebtn
    show screen phoneSD1

    "第二天是星期天，秋叶原人山人海。"
    "在这样的日子里蜥蜴人出现的话也一点都不奇怪。"
    "因为据说蜥蜴人喜欢在人多的地方出现。从目击情报的发生点可以看出来，"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BUILDE"])

    "{color=#f00}ＵＰＸ{/color}啦、{color=#f00}大楼{/color}啦，广播馆，秋叶原站，还有漆原家的柳林神社……也就是说他就是个喜欢吸引别人眼球的家伙。"
    "这种程度的话就算不推理也能明白。就算如此，在我心中，面对这样的Ｍｙｓｔｅｒｙ的斗志却越烧越旺。"
    "一直以来只有在小说呀漫画里体验到的紧张与刺激，现在正在我的眼前等着我。"
    "将会怎样去攻略这个谜题呢，到底会是怎样的真相呢，只是想想这些就已经心潮澎湃了。"
    window hide

    stop se



    $ loadBG(0,"BG03A4")


    $ targetmailid = gc["ScriptMacros"]["RM_FEI_RECV_TEN01_01"]

    $ LR_RM_CHANCE=23
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0000"
    $ current_voice = "voice/FEI02A_DAR0000.ogg"
    "至" "「还没好吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0000"
    $ current_voice = "voice/FEI02A_MAY0000.ogg"
    "真由理" "「不行的哦，桶子君。偷看更衣可是违反规则的。禁止进入窗帘的另一侧！」"
    call CHECK_RM_RECEIVE
    "阿万音和我从早上开始就干劲十足地来到Ｌａｂ，从真由喜那里拿到了Ｃｏｓ服之后，就赶紧开始换起了衣服。"
    call CHECK_RM_RECEIVE
    "在窗帘的另一边，桶子君一定是双目充血，等待着我们的更衣结束。"
    call CHECK_RM_RECEIVE
    "虽然有些害羞，但是我对于被这样注视并不感到厌恶。想起了ＭａｙＱｕｅｅｎ＋Ｎｙａ²刚开业时我穿着女仆装的感受，我露出了微笑。"
    call CHECK_RM_RECEIVE
    "阿万音并不知道我在想着这样的事情，整理着打底裤的皱纹，朝着我这边笑了一个。"
    call CHECK_RM_RECEIVE
    "她的笑脸，是对于即将扮演的超级英雄的期待的证据。之后应该会笑的更多吧。这样的心情，就算不读她的心，我也能清楚地把握到。"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0001"
    $ current_voice = "voice/FEI02A_DAR0001.ogg"
    "至" "「喂，差不多该好了吧？」"
    call CHECK_RM_RECEIVE
    "桶子又催促了一回。"
    call CHECK_RM_RECEIVE
    "真由理酱重申了一次。"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0001"
    $ current_voice = "voice/FEI02A_MAY0001.ogg"
    "真由理" "「不能这么心急哦，桶子君。女孩子的换衣服可是非常繁琐的」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0002"
    $ current_voice = "voice/FEI02A_DAR0002.ogg"
    "至" "「不是，就是等不及看真由氏做的Ｃｏｓ服穿在菲利斯碳身上的样子了」"
    call CHECK_RM_RECEIVE
    "就好好期待一下吧，桶子。"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0000"
    $ current_voice = "voice/FEI02A_SUZ0000.ogg"
    "铃羽" "「我好歹也在换衣服呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0003"
    $ current_voice = "voice/FEI02A_DAR0003.ogg"
    "至" "「我也很期待运动短裤哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0004"
    $ current_voice = "voice/FEI02A_DAR0004.ogg"
    "至" "「阿万音氏的本体是运动短裤。不接受异议！」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0001"
    $ current_voice = "voice/FEI02A_SUZ0001.ogg"
    "铃羽" "「作为夸奖我收下了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0005"
    $ current_voice = "voice/FEI02A_DAR0005.ogg"
    "至" "「比起那个，真由氏超厉害吧？　一晚上就做好了诶。而且是两人份的」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0002"
    $ current_voice = "voice/FEI02A_MAY0002.ogg"
    "真由理" "「诶嘿嘿，是这样呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0003"
    $ current_voice = "voice/FEI02A_MAY0003.ogg"
    "真由理" "「但是呢，只是把现成的衣服组合起来而已，其实并没有花那么多时间」"
    call CHECK_RM_RECEIVE
    "她虽然表现得很谦虚，但真的很厉害。仔细看看的话，会发现她在衣服上加了很多让穿起来变得更加容易的改动。"
    call CHECK_RM_RECEIVE
    "并不是临时拼凑出来的衣服，这一点穿上以后就明白了。"
    call CHECK_RM_RECEIVE
    "完成度相当有保证。就算如此真由理好像还是没有满足似的，在把Ｃｏｓ服交给我们的时候还说下次想做出更厉害的衣服来。"

    call CHECK_RM_RECEIVE
    "于是在阿万音结束了更衣的时候，我也整理好了身上的装束。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_TEN01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_TEN01_01"])

    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0006"
    $ current_voice = "voice/FEI02A_DAR0006.ogg"
    "至" "「差不多了吧？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0000"
    $ current_voice = "voice/FEI02A_FEI0000.ogg"
    "菲利斯" "「Ｏ－Ｋ－♪」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0002"
    $ current_voice = "voice/FEI02A_SUZ0002.ogg"
    "铃羽" "「准备就绪！」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0004"
    $ current_voice = "voice/FEI02A_MAY0004.ogg"
    "真由理" "「那么，现在就拉开窗帘咯」"
    hide screen phoneSD1
    window hide
    play se "SGSE352"



    $ loadBG(3,"BG_WHITE")






    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI001A"]]["Check"]=True
    $ loadBG(1,"EV_FEI001A")




    play bgm "BGM05"
    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0005"
    $ current_voice = "voice/FEI02A_MAY0005.ogg"
    "真由理" "「哇！」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0007"
    $ current_voice = "voice/FEI02A_DAR0007.ogg"
    "至" "「我靠！　这是何等的Ｓｅｘｙ！　这是何等的菲利斯碳！」"
    "看着桶子和真由理酱眼睛闪闪发光望着我的样子，我稍微有些脸红。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI001B"]]["Check"]=True


    $ loadBG(2,"EV_FEI001B")







    "一半是高兴，另一半是害羞。"
    "将视线稍稍朝下来隐藏自己的害羞。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0001"
    $ current_voice = "voice/FEI02A_FEI0001.ogg"
    "菲利斯" "「但是稍微感觉胸口附近有点紧啊」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0006"
    $ current_voice = "voice/FEI02A_MAY0006.ogg"
    "真由理" "「恩，但我是按照合身的尺寸做的啊……啊，难道说，又变大了吗？」"
    window hide


























    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOKO"])

    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0008"
    $ current_voice = "voice/FEI02A_DAR0008.ogg"
    "至" "「又，又，又，又，又，又变大了？！这可是大事件！目前是富士山级别珠穆朗玛峰级别还是Ｅｖｅｒｅｓｔ级别{color=#f00}常考{/color}！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI001C"]]["Check"]=True


    $ loadBG(3,"EV_FEI001C")






    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0002"
    $ current_voice = "voice/FEI02A_FEI0002.ogg"
    "菲利斯" "「桶喵你兴奋过头了啦，菲利斯还只是北阿尔卑斯级别的」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0009"
    $ current_voice = "voice/FEI02A_DAR0009.ogg"
    "至" "「北阿尔卑斯……咕噜」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0003"
    $ current_voice = "voice/FEI02A_SUZ0003.ogg"
    "铃羽" "「就算那样还是很适合啊。Ｓｅｘｙ路线也很行嘛，Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0003"
    $ current_voice = "voice/FEI02A_FEI0003.ogg"
    "菲利斯" "「当然了喵！　菲利斯可是降临于这片土地之上最后的女神喵！」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0007"
    $ current_voice = "voice/FEI02A_MAY0007.ogg"
    "真由理" "「原来以为对于菲利斯酱来说可能会有点土，但是现在看这么合适真是太好了♪」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0004"
    $ current_voice = "voice/FEI02A_SUZ0004.ogg"
    "铃羽" "「但是看这个素材，在这个季节的话是不是有点太闷了」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0010"
    $ current_voice = "voice/FEI02A_DAR0010.ogg"
    "至" "「太热的话就把拉链拉下来一些吧，菲利斯碳！」"
    "……哦，唔。"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0011"
    $ current_voice = "voice/FEI02A_DAR0011.ogg"
    "至" "「来吧不要忍耐了，解放自己内心的欲望吧！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI001B"]]["Check"]=True




    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0004"
    $ current_voice = "voice/FEI02A_FEI0004.ogg"
    "菲利斯" "「那是做不到的喵，桶喵。如果把这个拉链拉下来的话，封印于此胸口的潘多拉之匣就会被解开，世界将被黑暗所支配……」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0012"
    $ current_voice = "voice/FEI02A_DAR0012.ogg"
    "至" "「也就是说……这是怎么一回事哦」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI001D"]]["Check"]=True


    $ loadBG(2,"EV_FEI001D")



    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0005"
    $ current_voice = "voice/FEI02A_FEI0005.ogg"
    "菲利斯" "「绝对ＮＯ！！！　喵」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0008"
    $ current_voice = "voice/FEI02A_MAY0008.ogg"
    "真由理" "「铃羽感觉穿着怎么样？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_M4CARBINE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_M4CARBINE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_M4CARBINE"])
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0005"
    $ current_voice = "voice/FEI02A_SUZ0005.ogg"
    "铃羽" "「完全没有问题！　诶呀，穿着这种衣服感觉稍微有些怀念啊。如果还有{color=#f00}柯尔特Ｍ４卡宾枪{/color}的话就完美了」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0006"
    $ current_voice = "voice/FEI02A_FEI0006.ogg"
    "菲利斯" "「穿起来的手法看起来很熟练呢。铃羽喵也有Ｃｏｓｐｌａｙ的经验吗？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0006"
    $ current_voice = "voice/FEI02A_SUZ0006.ogg"
    "铃羽" "「就好像是过去的工作服一样的感觉……但其实不是特别的工作的话是不会穿成这样的呢♪」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0009"
    $ current_voice = "voice/FEI02A_MAY0009.ogg"
    "真由理" "「喜欢的话真是太好了呢。那，回去之后就帮菲利斯酱改一下衣服吧」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA01"),"True","lh/SUZ_FSA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    show screen phonebtn
    "就算如此但还是有些遗憾，因为今天冈部不在。这么想着的时候，不经意间说出了一些软弱的话语。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0007"
    $ current_voice = "voice/FEI02A_FEI0007.ogg"
    "菲利斯" "「……也想给凶真看看啊喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0007"
    $ current_voice = "voice/FEI02A_SUZ0007.ogg"
    "铃羽" "「冈部伦太郎今天也打工吗？」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0013"
    $ current_voice = "voice/FEI02A_DAR0013.ogg"
    "至" "「恩。和牧濑氏一起今天一早就出去了。今天大概是和桐生氏在一起吧？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0008"
    $ current_voice = "voice/FEI02A_FEI0008.ogg"
    "菲利斯" "「本人稍微要抗议一下喵」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[274,275,276])






    call hide_phone

    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0009"
    $ current_voice = "voice/FEI02A_FEI0009.ogg"
    "菲利斯" "「哼，难得想给凶真展示一下暗之女神(雅典娜)所赐予的漆黑之铠的说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA03"),"True","lh/SUZ_FSA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0008"
    $ current_voice = "voice/FEI02A_SUZ0008.ogg"
    "铃羽" "「…………」"
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0010"
    $ current_voice = "voice/FEI02A_MAY0010.ogg"
    "真由理" "「…………」"
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0014"
    $ current_voice = "voice/FEI02A_DAR0014.ogg"
    "至" "「…………」"
    "是哦，这大概只有冈部会懂我在说些什么……"
    "到刚才为止都还挺正常的，就一不小心入戏了。"

    $ targetmailid = 440

    $ LR_RM_CHANCE=28

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0015"
    $ current_voice = "voice/FEI02A_DAR0015.ogg"
    "至" "「比，比起那个这个。我把秋叶原怪奇地图打印好了哦。要调查的话这个是必须的吧」"
    call CHECK_RM_RECEIVE
    "那是将之前的目击情报整合起来打印在地图上的产物。"
    call CHECK_RM_RECEIVE
    "不愧是桶子，Ｎｉｃｅ　Ｆｅｌｌｏｗ。"
    call CHECK_RM_RECEIVE
    "托他的福刚才有些尴尬的气氛稍微减弱了些。"
    call CHECK_RM_RECEIVE
    "桶子虽然平时看起来大大咧咧的，其实还是很会注意气氛的嘛。"
    call CHECK_RM_RECEIVE
    "他就是这种小地方招女生喜欢啊。"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0010"
    $ current_voice = "voice/FEI02A_FEI0010.ogg"
    "菲利斯" "「谢谢了，桶喵♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0016"
    $ current_voice = "voice/FEI02A_DAR0016.ogg"
    "至" "「再多夸我几句也没关系的，菲利斯碳！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0011"
    $ current_voice = "voice/FEI02A_MAY0011.ogg"
    "真由理" "「对了，在皮带上我特意做了个小口袋，在里面可以放些小东西啦钱包之类的♪」"
    call CHECK_RM_RECEIVE
    "听了真由理酱的话，我确认了一下皮带。"
    call CHECK_RM_RECEIVE
    "确实那里有个口袋。"
    call CHECK_RM_RECEIVE
    "我就将钱包和桶子递过来的地图放了进去，然后把传单夹在了皮带上。这样就准备完了♪"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0011"
    $ current_voice = "voice/FEI02A_FEI0011.ogg"
    "菲利斯" "「那么各位，英姿飒爽的黑猫就出动了喵！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0012"
    $ current_voice = "voice/FEI02A_MAY0012.ogg"
    "真由理" "「呐呐，铃羽没有新的名字吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA01"),"True","lh/SUZ_FSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0009"
    $ current_voice = "voice/FEI02A_SUZ0009.ogg"
    "铃羽" "「我倒是无所谓」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0012"
    $ current_voice = "voice/FEI02A_FEI0012.ogg"
    "菲利斯" "「恩，说起来的话确实是这样喵。难得有机会当一次英雄，果然还是想帮你起一个喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA02"),"True","lh/SUZ_FSA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0010"
    $ current_voice = "voice/FEI02A_SUZ0010.ogg"
    "铃羽" "「那样的话……Ａｌｐｈａ或者Ｂｒａｖｏ之类的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "FEI02A_DAR0017"
    $ current_voice = "voice/FEI02A_DAR0017.ogg"
    "至" "「北约音标字母吗。在无线电通信或者外国电影里军队经常使用的样子」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA01"),"True","lh/SUZ_FSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0011"
    $ current_voice = "voice/FEI02A_SUZ0011.ogg"
    "铃羽" "「Ａ是Ａｌｐｈａ，Ｂ是Ｂｒａｖｏ、一直到Ｚ都有哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0013"
    $ current_voice = "voice/FEI02A_FEI0013.ogg"
    "菲利斯" "「铃羽（Ｓｕｚｕ）的Ｓ是？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0012"
    $ current_voice = "voice/FEI02A_SUZ0012.ogg"
    "铃羽" "「希尔拉，Ｓｉｅｒｒａ。在西班牙语里是山的意思。也有读成希艾拉的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "FEI02A_MAY0013"
    $ current_voice = "voice/FEI02A_MAY0013.ogg"
    "真由理" "「希艾拉不是挺不错的嘛」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0014"
    $ current_voice = "voice/FEI02A_FEI0014.ogg"
    "菲利斯" "「确实不错喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA04"),"True","lh/SUZ_FSA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0013"
    $ current_voice = "voice/FEI02A_SUZ0013.ogg"
    "铃羽" "「Ｂｏｓｓ觉得好的话，那就那样吧」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0015"
    $ current_voice = "voice/FEI02A_FEI0015.ogg"
    "菲利斯" "「那就重新说一遍……准备好了吗，希艾拉？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA02"),"True","lh/SUZ_FSA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0014"
    $ current_voice = "voice/FEI02A_SUZ0014.ogg"
    "铃羽" "「Ｏｋａｙ－ｄｏｋｅｙ、Ｂｏｓｓ！」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0016"
    $ current_voice = "voice/FEI02A_FEI0016.ogg"
    "菲利斯" "「今天就好好地享受一下吧喵♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA03"),"True","lh/SUZ_FSA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0015"
    $ current_voice = "voice/FEI02A_SUZ0015.ogg"
    "铃羽" "「啊……恩，好啊……」"

    call CHECK_RM_RECEIVE
    window hide

    stop bgm 


    $ loadBG(2,"IBGX048")
    play se "SGSE024"




    "于是就这样，我们英姿飒爽地打开了研究所的大门。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_OKA01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_OKA01_01"])

    window hide



    $ loadBG(0,"BG16A1")

    play bgm "BGM18"
    "刚走到外面，就发现今天街上人山人海。"
    window hide


    $ loadBG(2,"BG20A")


    play se "SGSE007L" loop



    "今天可是暑假里的周日。随便一看就发现从其他地方来的家族和外国观光客比平时要多很多。"
    window hide



    $ loadBG(2,"BG24A")




    "这些人要是还是认为秋叶原是奇怪的街区而不是二次元的街区的话，如果是那些认为萌系的街区不好的大人，一定会觉得这条街的文化就突然变了样吧。"
    "看着车水马龙的街道上的人们，我不由自主地叹了口气。"

    $ targetmailid = cml.setdefault("RM_FEI_SEND_OKA01","")

    $ LR_RM_CHANCE=9

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0016"
    $ current_voice = "voice/FEI02A_SUZ0016.ogg"
    "铃羽" "「果然人好多啊。和往常一样被吓了一跳呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0017"
    $ current_voice = "voice/FEI02A_FEI0017.ogg"
    "菲利斯" "「希艾拉的家乡难道不是这样的感觉吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB03"),"True","lh/SUZ_FMB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0017"
    $ current_voice = "voice/FEI02A_SUZ0017.ogg"
    "铃羽" "「不应该啊」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0018"
    $ current_voice = "voice/FEI02A_SUZ0018.ogg"
    "铃羽" "「……」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0019"
    $ current_voice = "voice/FEI02A_SUZ0019.ogg"
    "铃羽" "「Ｂｏｓｓ，是不是角色有点奇怪？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0018"
    $ current_voice = "voice/FEI02A_FEI0018.ogg"
    "菲利斯" "「现在我是黑猫哦。带上护目镜把脸遮住以后就是别人了」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0020"
    $ current_voice = "voice/FEI02A_SUZ0020.ogg"
    "铃羽" "「啊啊……是这样啊」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0019"
    $ current_voice = "voice/FEI02A_FEI0019.ogg"
    "菲利斯" "「正是如此」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0020"
    $ current_voice = "voice/FEI02A_FEI0020.ogg"
    "菲利斯" "「恩……」"

    call CHECK_RM_RECEIVE
    window hide


    $ loadBG(2,"IBGX048")



    "将双手举过头顶，我伸了个懒腰。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_OKA02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_OKA02_01"])

    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0021"
    $ current_voice = "voice/FEI02A_FEI0021.ogg"
    "菲利斯" "「呐，希艾拉没有感受到吗？　那种从一直束缚着自己的东西里解放的清爽感觉」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0021"
    $ current_voice = "voice/FEI02A_SUZ0021.ogg"
    "铃羽" "「被解放的感觉？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0022"
    $ current_voice = "voice/FEI02A_FEI0022.ogg"
    "菲利斯" "「比如说……匿名在网上发表各种各样的东西的感觉。从现实中脱离，写一些自己想写的东西……」"
    "对我来说那种感觉属于意料之外的收获。"
    window hide




    $ loadBG(3,"EV_FEI001A")



























    "『菲利斯』的时候没法做到的事，感觉在这个新的『角色』下就可以不经意地完成。"
    "那是因为用护目镜遮住了眼睛。"
    "现在的我不是菲利斯。"
    "所以就算穿着这么凸显身体曲线的紧身衣也毫不害羞。"
    "因为我现在不是菲利斯而是黑猫。"
    window hide






























    $ loadBG(2,"BG24A")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA04"),"True","lh/SUZ_FMA04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0022"
    $ current_voice = "voice/FEI02A_SUZ0022.ogg"
    "铃羽" "「……恩。我感觉我好像明白了」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0023"
    $ current_voice = "voice/FEI02A_FEI0023.ogg"
    "菲利斯" "「这就是伙伴啊」"
    "我看着阿万音的眼睛微笑着。"

    $ targetmailid = gc["ScriptMacros"]["RM_FEI_RECV_MAY01_01"]

    $ LR_RM_CHANCE=15

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0023"
    $ current_voice = "voice/FEI02A_SUZ0023.ogg"
    "铃羽" "「好，那接下来是来自可靠的伙伴的提案。刚才已经看了一下了，这里附近没有蜥蜴人的样子，接下来去哪里？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0024"
    $ current_voice = "voice/FEI02A_FEI0024.ogg"
    "菲利斯" "「恩。但是在那之前……」"
    window hide
    hide lh7 
    call CHECK_RM_RECEIVE
    "因为服装的关系，人们与我们擦肩而过的时候有着各种各样的反应。"
    call CHECK_RM_RECEIVE
    "有些人觉得这在秋叶原里是很理所当然的，所以毫无反应。也有些人投来奇异的眼神，还有的女学生笑着说“好可爱啊”。也有用手机拍照的人。"
    call CHECK_RM_RECEIVE
    "——可不能放过这个机会啊。"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0025"
    $ current_voice = "voice/FEI02A_FEI0025.ogg"
    "菲利斯" "「哼哼，黑猫的初次任务哦，希艾拉」"
    call CHECK_RM_RECEIVE
    "一边这么说着，我从皮带上面取出传单，毫不害羞地大声说道。"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0026"
    $ current_voice = "voice/FEI02A_FEI0026.ogg"
    "菲利斯" "「正义的伙伴，黑猫参上！黑猫必将守护秋叶原的形象！」"

    play se "SGSE096L"

    stop se
    call CHECK_RM_RECEIVE
    "然后将传单撒在联络通路上。"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0027"
    $ current_voice = "voice/FEI02A_FEI0027.ogg"
    "菲利斯" "「黑猫说不定会出现的女仆咖啡，ＭａｙＱｕｅｅｎ＋Ｎｙａ²现在营业中！　等待着各位主人的关顾哦♥」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0024"
    $ current_voice = "voice/FEI02A_SUZ0024.ogg"
    "铃羽" "「等，等等Ｂｏｓｓ！　在做什么呀！」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0028"
    $ current_voice = "voice/FEI02A_FEI0028.ogg"
    "菲利斯" "「做什么……只是用了一下黑猫的秘密道具？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0025"
    $ current_voice = "voice/FEI02A_SUZ0025.ogg"
    "铃羽" "「秘密道具？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0029"
    $ current_voice = "voice/FEI02A_FEI0029.ogg"
    "菲利斯" "「是的，还有用来放零钱的『猫咪钱包』，用来爬到高处的『猫咪梯子』，还有用来赶走鲨鱼的『猫咪喷雾剂』哟♪」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0026"
    $ current_voice = "voice/FEI02A_SUZ0026.ogg"
    "铃羽" "「真是的，就算变成了黑猫，果然菲利斯还是菲利斯啊！总之在被围住之前出发吧」"

    call CHECK_RM_RECEIVE
    window hide
    hide lh7 
    "这么说着，阿万音拉着我的手，在大家的注目之下，将逐渐聚集起来的人群甩在了身后。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_MAY01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_MAY01_01"])

    window hide
    play se "SGSE183L"


    stop se


    $ loadBG(3,"BG_BLACK")








    $ loadBG(0,"BG16A1")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play se "SGSE007L" loop






    stop se
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0027"
    $ current_voice = "voice/FEI02A_SUZ0027.ogg"
    "铃羽" "「……哈，哈。引起那样的骚动的话，难道不会让蜥蜴人逃走吗」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0030"
    $ current_voice = "voice/FEI02A_FEI0030.ogg"
    "菲利斯" "「……哈，哈。不是那回事哦。如果人聚集起来的话，肯定会表露出兴趣过来看一下的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0028"
    $ current_voice = "voice/FEI02A_SUZ0028.ogg"
    "铃羽" "「为什么你会知道那种事情啊」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0031"
    $ current_voice = "voice/FEI02A_FEI0031.ogg"
    "菲利斯" "「蜥蜴人可是很喜欢引人注目的哦？不然的话，就不会在人多的地方出现了」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0029"
    $ current_voice = "voice/FEI02A_SUZ0029.ogg"
    "铃羽" "「但就算这样，我们也没法去追啊。作战要慎重，行动要大胆啊Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0032"
    $ current_voice = "voice/FEI02A_FEI0032.ogg"
    "菲利斯" "「了解♪　确实如希艾拉所说的，稍微有点轻率了啊。抱歉♥」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我没有多想就抱住了阿万音。"
    "透过服装，我们互相感受到了对方的体温与柔软的身体。"
    window hide


    $ loadBG(2,"BG_BLACK",over=True)



    "说起来这种感觉……很像那个时候呢。"
    "小时候经常让爸爸妈妈感到很困扰……"
    window hide
    hide background-over 



    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0030"
    $ current_voice = "voice/FEI02A_SUZ0030.ogg"
    "铃羽" "「等，等等……你在干什么呀，Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0033"
    $ current_voice = "voice/FEI02A_FEI0033.ogg"
    "菲利斯" "「嗯，我也不明白啊。让希艾拉担心了，突然就觉得你变可爱了」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0031"
    $ current_voice = "voice/FEI02A_SUZ0031.ogg"
    "铃羽" "「在这种地方，要是被谁看到的话会误解的吧」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0034"
    $ current_voice = "voice/FEI02A_FEI0034.ogg"
    "菲利斯" "「现在的我是黑猫，所以没关系啦」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0032"
    $ current_voice = "voice/FEI02A_SUZ0032.ogg"
    "铃羽" "「难道说喝醉了吗？　……也没有啊。果然是被那套衣服给热坏了么？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0035"
    $ current_voice = "voice/FEI02A_FEI0035.ogg"
    "菲利斯" "「确实可能有点热啊。气温变高了吗」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我一边有些遗憾地感受着阿万音的触感，一边缓缓地放开了她的身体。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0033"
    $ current_voice = "voice/FEI02A_SUZ0033.ogg"
    "铃羽" "「那么热的话，不如把拉链往下拉一些？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0036"
    $ current_voice = "voice/FEI02A_FEI0036.ogg"
    "菲利斯" "「那可不行。我的肌肤只能露给与魔王达克提亚对抗的王子大人看」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0034"
    $ current_voice = "voice/FEI02A_SUZ0034.ogg"
    "铃羽" "「……你高兴就好」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0037"
    $ current_voice = "voice/FEI02A_FEI0037.ogg"
    "菲利斯" "「明白就好。那么接下来、朝着车站ＧＯ！吧」"
    window hide

    stop se

    stop bgm 




    $ loadBG(0,"BG13A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)













    play se "SGSE007L" loop


    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA06"),"True","lh/SUZ_FMA06a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)








    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0035"
    $ current_voice = "voice/FEI02A_SUZ0035.ogg"
    "铃羽" "「这里也是相对来说蜥蜴人的目击情报较多的地方呢。……还有，有人说那里的广播馆上面还有ＵＦＯ什么的」"





    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0036"
    $ current_voice = "voice/FEI02A_SUZ0036.ogg"
    "铃羽" "「ＵＦＯ之后再说吧，ＢＯＳＳ」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0037"
    $ current_voice = "voice/FEI02A_SUZ0037.ogg"
    "铃羽" "「……咦、ＢＯＳＳ？」"
    "脑袋有些朦胧。"
    window hide


    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0038"
    $ current_voice = "voice/FEI02A_SUZ0038.ogg"
    "铃羽" "「等等，这是要去哪儿」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0038"
    $ current_voice = "voice/FEI02A_FEI0038.ogg"
    "菲利斯" "「咦……是{color=#f00}显像管工房{/color}的店长呢」"
    window hide














    "出现在我模糊的视线中的是，３０米前方的一个身影。"



    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at left_q1 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "秋叶原的车站前提着购物的袋子的光头男子出现在那里。"
    "虽然一下子没有反应过来，但是看那威风堂堂的样子不就是天王寺先生吗。"
    window hide













    hide lh6 
    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


















    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0039"
    $ current_voice = "voice/FEI02A_SUZ0039.ogg"
    "铃羽" "「还真是，买东西回来吗」"
    "根据阿万音的反应确认了自己的推测。……那样的话。"
    window hide

















    hide lh6 
    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at left_q1 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


















    play bgm "BGM25"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0039"
    $ current_voice = "voice/FEI02A_FEI0039.ogg"
    "菲利斯" "「我对那个人从很久之前开始就有想说的话了」"
    "我带着晕乎乎的脑袋朝店长走去。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0040"
    $ current_voice = "voice/FEI02A_SUZ0040.ogg"
    "铃羽" "「有想说的事情……难道说Ｂｏｓｓ？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0040"
    $ current_voice = "voice/FEI02A_FEI0040.ogg"
    "菲利斯" "「开会的时候还很牛逼地摆架子，完全把我当小孩子看了嘛」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0041"
    $ current_voice = "voice/FEI02A_FEI0041.ogg"
    "菲利斯" "「而且昨天还临时取消了计划……肯定是还在耍什么把戏吧」"
    "阿万音从我的背后拉住了我，阻止我追到店长身边去。"
    window hide













    hide lh6 
    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


















    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0041"
    $ current_voice = "voice/FEI02A_SUZ0041.ogg"
    "铃羽" "「难道说真要去和店长吵架？　还是算了吧」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0042"
    $ current_voice = "voice/FEI02A_FEI0042.ogg"
    "菲利斯" "「没关系，有带着护目镜，不会被发现就是我们的」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0042"
    $ current_voice = "voice/FEI02A_SUZ0042.ogg"
    "铃羽" "「不是说这个问题啦」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0043"
    $ current_voice = "voice/FEI02A_FEI0043.ogg"
    "菲利斯" "「虽然我平时总是对大人的行为沉默，但今天可不打算那么做。我可是英雄，不行使正义的话……」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0043"
    $ current_voice = "voice/FEI02A_SUZ0043.ogg"
    "铃羽" "「等……ＢＯＳＳ！」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0044"
    $ current_voice = "voice/FEI02A_FEI0044.ogg"
    "菲利斯" "「给我等等，天王寺先生！」"
    window hide
















    hide lh6 
    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI02A_TEN0000"
    $ current_voice = "voice/FEI02A_TEN0000.ogg"
    "天王寺" "「……恩？」"
    "在天王寺先生转过身来的前一刻，我发现我被阿万音拖到了看板的阴影里。"
    "不光身体被阿万音给制住了，就连嘴巴都被她堵得严严实实，连声音都发不出来。"
    "于是天王寺先生回过头来就谁也没看到，不可思议地歪了歪脑袋。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI02A_TEN0001"
    $ current_voice = "voice/FEI02A_TEN0001.ogg"
    "天王寺" "「是我的错觉吗……。感觉有人在叫我的样子」"








    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0045"
    $ current_voice = "voice/FEI02A_FEI0045.ogg"
    "菲利斯" "「唔！　唔！」"


    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0044"
    $ current_voice = "voice/FEI02A_SUZ0044.ogg"
    "铃羽" "「ＢＯＳＳ、嘘！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "就这样稍微过了一会，在铃羽确认了天王寺先生已经离开之后，她终于放开了我。"
    window hide


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0045"
    $ current_voice = "voice/FEI02A_SUZ0045.ogg"
    "铃羽" "「呼，还以为会变成什么样子呢。但是好像安全回避了的样子呢」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0046"
    $ current_voice = "voice/FEI02A_FEI0046.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA06"),"True","lh/SUZ_FMA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0046"
    $ current_voice = "voice/FEI02A_SUZ0046.ogg"
    "铃羽" "「……果然生气了吗，Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0047"
    $ current_voice = "voice/FEI02A_FEI0047.ogg"
    "菲利斯" "「啊啊、不是哦希艾拉。我，为什么会做出那种事情来呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0047"
    $ current_voice = "voice/FEI02A_SUZ0047.ogg"
    "铃羽" "「果然是热昏了头吧」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0048"
    $ current_voice = "voice/FEI02A_FEI0048.ogg"
    "菲利斯" "「是……这样吗」"
    "虽然在天王寺先生消失之前我就已经取回了冷静，但是要是刚才没有铃羽的话我会做出些什么事啊……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0048"
    $ current_voice = "voice/FEI02A_SUZ0048.ogg"
    "铃羽" "「总之先去个凉快点的地方吧，比如有空调之类的店」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0049"
    $ current_voice = "voice/FEI02A_FEI0049.ogg"
    "菲利斯" "「恩……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB03"),"True","lh/SUZ_FMB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0049"
    $ current_voice = "voice/FEI02A_SUZ0049.ogg"
    "铃羽" "「但是好奇怪啊，明明这个服装没有那么热的才对……」"
    window hide

    stop se



    $ loadBG(0,"BG22A")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0050"
    $ current_voice = "voice/FEI02A_SUZ0050.ogg"
    "铃羽" "「唔，这里的话空调就很足了……。诶，Ｂｏｓｓ？　Ｂｏｓｓ！？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0050"
    $ current_voice = "voice/FEI02A_FEI0050.ogg"
    "菲利斯" "「唔喵♥」"
    play bgm "FD2BGM10"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0051"
    $ current_voice = "voice/FEI02A_SUZ0051.ogg"
    "铃羽" "「等等等等等等！　在做什么呀，Ｂｏｓｓ！」"
    "我的眼里已经容不下除了呜帕人偶之外的东西了。"
    "应该是『雷ＮＥＴ翔』促销用的用来实现孩子们的梦想的人偶吧。但是我也混在孩子堆里，尽情享受着那人偶。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0051"
    $ current_voice = "voice/FEI02A_FEI0051.ogg"
    "菲利斯" "「好可爱喵♥　好可爱喵♥　好想再毛茸茸一些啊喵～♥」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB01"),"True","lh/SUZ_FMB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0052"
    $ current_voice = "voice/FEI02A_SUZ0052.ogg"
    "铃羽" "「快停停，呜帕也很困扰啊，还有不要一个人把他给抢走啊！」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0052"
    $ current_voice = "voice/FEI02A_FEI0052.ogg"
    "菲利斯" "「呜帕！　呜帕！　我的呜帕！」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0053"
    $ current_voice = "voice/FEI02A_SUZ0053.ogg"
    "铃羽" "「啊啊，已经不知道她是菲利斯还是黑猫了」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0053"
    $ current_voice = "voice/FEI02A_FEI0053.ogg"
    "菲利斯" "「菲利斯不是菲利斯了喵♥　是呜帕的宠物喵♥」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0054"
    $ current_voice = "voice/FEI02A_SUZ0054.ogg"
    "铃羽" "「不好意思，这孩子有点太热了！　走了哦Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0054"
    $ current_voice = "voice/FEI02A_FEI0054.ogg"
    "菲利斯" "「啊啊，好想要呜帕，好想要！」"
    window hide

    stop bgm 


    $ loadBG(2,"BG_BLACK")




    "…………。"
    window hide


    $ loadBG(2,"BG14A")



    play bgm "BGM22"
    "……受不了了。"
    "好像我刚才和小孩子一样发脾气了。"
    "但是我记不得刚才的事情了。"
    "阿万音觉得我是被热昏了头，但是我不那么认为。"
    "突然抱住阿万音什么的，向天王寺先生提出抗议什么的，变得像小孩子一样一个人独占呜帕什么的……但是同时，我也被至今为止都未曾感受过的解放感所包围着。"
    "这种不受理性拘束，随心所欲地行动的感觉真是太棒了。"
    "果然带着护目镜行动就会变得大胆起来吗。就算如此……"
    "总而言之给阿万音添麻烦了是事实，所以我朝她低下了头。"
    "这个时候……"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0055"
    $ current_voice = "voice/FEI02A_FEI0055.ogg"
    "菲利斯" "「喂，希艾拉你在干什么呀」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0055"
    $ current_voice = "voice/FEI02A_SUZ0055.ogg"
    "铃羽" "「诶？　干什么……在给Ｂｏｓｓ的脖子挠痒痒啊」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0056"
    $ current_voice = "voice/FEI02A_FEI0056.ogg"
    "菲利斯" "「我又不是猫喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA02"),"True","lh/SUZ_FMA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0056"
    $ current_voice = "voice/FEI02A_SUZ0056.ogg"
    "铃羽" "「喵？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0057"
    $ current_voice = "voice/FEI02A_FEI0057.ogg"
    "菲利斯" "「我又不是猫」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0057"
    $ current_voice = "voice/FEI02A_SUZ0057.ogg"
    "铃羽" "「明明好像很舒服的样子？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0058"
    $ current_voice = "voice/FEI02A_FEI0058.ogg"
    "菲利斯" "「我又不是猫」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0058"
    $ current_voice = "voice/FEI02A_SUZ0058.ogg"
    "铃羽" "「终于变得稳重起来了。不会再发疯了吧？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0059"
    $ current_voice = "voice/FEI02A_FEI0059.ogg"
    "菲利斯" "「总之先去漆原的地方吧，可以吗？」"
    window hide

    stop bgm 



    $ loadBG(0,"BG15A")


    play se "SGSE004L" loop

    play bgm "BGM14"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA01"),"True","lh/RUK_BSA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "走进神社，我们立刻就看到了漆原的身影。"
    "就好像平时那样，拿着扫帚在那里沙沙地扫着地。"
    "但是「和平时那样」也就到此为止了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSB04"),"True","lh/RUK_BSB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "他注意到我和阿万音之后，慌慌张张躲进了神社内部。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0060"
    $ current_voice = "voice/FEI02A_FEI0060.ogg"
    "菲利斯" "「漆原！」"
    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0000"
    $ current_voice = "voice/FEI02A_RUK0000.ogg"
    "琉华" "「漆原……？」"
    "好像变成了黑猫之后起了意外的效果。他也没有打算装作没听见我们的叫声，犹豫了一会之后，仿佛下了什么似的转过头来。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSB01"),"True","lh/RUK_BSB01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0001"
    $ current_voice = "voice/FEI02A_RUK0001.ogg"
    "琉华" "「真稀奇啊，你们两个人在一起」"
    "虽然嘴角在笑但是眼睛里完全没有笑意。"
    "……完全不行呢。就算是那些大人也不会有如此拙劣的演技。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BMB01"),"True","lh/RUK_BMB01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0059"
    $ current_voice = "voice/FEI02A_SUZ0059.ogg"
    "菲利斯" "「想和你打听一些都市传说方面的事情，可以吗」"
    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0002"
    $ current_voice = "voice/FEI02A_RUK0002.ogg"
    "琉华" "「比起那个……你怎么了嘛，菲利斯。平时一直都是用『琉华喵』来叫我的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA02"),"True","lh/SUZ_FMA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0060"
    $ current_voice = "voice/FEI02A_SUZ0060.ogg"
    "铃羽" "「嘛，称呼什么的怎样都好了。还是先告诉我们关于都市传说的事情吧」"
    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0003"
    $ current_voice = "voice/FEI02A_RUK0003.ogg"
    "琉华" "「但是……我现在就要出去了」"
    "看着好像在搪塞我们的漆原，感觉身体里又起了那种感觉。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0061"
    $ current_voice = "voice/FEI02A_SUZ0061.ogg"
    "铃羽" "「关于蜥蜴人的目击情报，稍微一点点就行」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BMA03"),"True","lh/RUK_BMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0004"
    $ current_voice = "voice/FEI02A_RUK0004.ogg"
    "琉华" "「在下真的不知道……」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0062"
    $ current_voice = "voice/FEI02A_SUZ0062.ogg"
    "铃羽" "「…………」"
    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0005"
    $ current_voice = "voice/FEI02A_RUK0005.ogg"
    "琉华" "「那么，父亲还在等着我……」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0063"
    $ current_voice = "voice/FEI02A_SUZ0063.ogg"
    "铃羽" "「是吗」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA05"),"True","lh/SUZ_FMA05a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0064"
    $ current_voice = "voice/FEI02A_SUZ0064.ogg"
    "铃羽" "「……说起来，为什么看到我们穿成这样但一点都不惊讶？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BMB02"),"True","lh/RUK_BMB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0006"
    $ current_voice = "voice/FEI02A_RUK0006.ogg"
    "琉华" "「……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM25"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0065"
    $ current_voice = "voice/FEI02A_SUZ0065.ogg"
    "铃羽" "「……果然，不知道什么的都是在撒谎吧」"
    "撒谎……"
    window hide
    play se "SGSE063"



    $ loadBG(2,"BG_BLACK",trans=ImageDissolve(im.Scale("mask/mask00.png",1024,576),1),at=[Transform(alpha=0.5)],over=True)









    "和那个时候一样呢。"
    "昨天晚上的黑木。还有出席的大人们。"
    "谎言会使人受伤。"
    "将其称为无法挽回的灾厄。"
    "绝对无法原谅。谎言，谎言，谎言……"
    window hide


    $ loadBG(3,"BG_CHI",trans=ImageDissolve(im.Scale("mask/mask01.png",1024,576),1),at=[Transform(alpha=0.5)],over=True)





















    "这么想着，我心中的炽热的感情又涌上来了。"
    "是啊，我现在是黑猫。"
    "为了伸张正义，是决不允许谎言的……"
    window hide
    hide background-over 
    with dissolve
























    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA02"),"True","lh/RUK_BLA02a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我被这股热血所驱动，蹿到了漆原的背后，靠着他的耳朵用细微的声音说道。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0061"
    $ current_voice = "voice/FEI02A_FEI0061.ogg"
    "菲利斯" "「说谎是不行的……。看着你的眼睛我就明白了哦。」"
    "然后轻轻地用舌头在他的脸颊上舔了一下，也就是表示出“接下来你就是我的盘中餐了”的意思。"
    "——就好像野兽一样"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA04"),"True","lh/RUK_BLA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "FEI02A_RUK0007"
    $ current_voice = "voice/FEI02A_RUK0007.ogg"
    "琉华" "「非，非常抱歉～～～！」"
    window hide


    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "但是好像起到了反作用。因为事发突然，他的脸蛋瞬间变得通红，然后把我一把推开，扔下扫帚躲到房间离去了。"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0066"
    $ current_voice = "voice/FEI02A_SUZ0066.ogg"
    "铃羽" "「诶呀」"
    "然后我取回了冷静。"
    "最后还是这么做了啊，我一边反省着，一边感受到了让我焦躁不安的元凶消失后的安全感。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0062"
    $ current_voice = "voice/FEI02A_FEI0062.ogg"
    "菲利斯" "「抱歉啊希艾拉，不小心就那么做了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0067"
    $ current_voice = "voice/FEI02A_SUZ0067.ogg"
    "铃羽" "「没事哦，比起那个问题在于……」"
    "阿万音若无其事地在我耳边低声说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0068"
    $ current_voice = "voice/FEI02A_SUZ0068.ogg"
    "铃羽" "「好像有谁在看我们」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0063"
    $ current_voice = "voice/FEI02A_FEI0063.ogg"
    "菲利斯" "「……！」"
    play bgm "BGM23"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0069"
    $ current_voice = "voice/FEI02A_SUZ0069.ogg"
    "铃羽" "「……就是这样」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0064"
    $ current_voice = "voice/FEI02A_FEI0064.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0070"
    $ current_voice = "voice/FEI02A_SUZ0070.ogg"
    "铃羽" "「好像从中央通路开始就跟着我们了。……没关系，没有打算袭击我们的意思」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0065"
    $ current_voice = "voice/FEI02A_FEI0065.ogg"
    "菲利斯" "「真的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0071"
    $ current_voice = "voice/FEI02A_SUZ0071.ogg"
    "铃羽" "「恩没问题，我可以保证哦」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0066"
    $ current_voice = "voice/FEI02A_FEI0066.ogg"
    "菲利斯" "「说起来，黑木的样子也很奇怪啊」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0072"
    $ current_voice = "voice/FEI02A_SUZ0072.ogg"
    "铃羽" "「朋友吗？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0067"
    $ current_voice = "voice/FEI02A_FEI0067.ogg"
    "菲利斯" "「家人……吧」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0073"
    $ current_voice = "voice/FEI02A_SUZ0073.ogg"
    "铃羽" "「……这样吗。就算这样漆原琉华的态度也好被监视也好，总感觉有股阴谋的味道……」"
    window hide

    stop se


    $ loadBG(0,"BG23A")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play se "SGSE007L" loop

    "离开柳林神社后我们在咖啡厅里暂时落脚。"
    "感觉一直在观察着我们的人物并没有什么问题。"
    "虽然阿万音感觉到了餐厅的介绍台前面的女性，在桌子上聊天的二人组，咖啡的店员也投来颇有深意的视线，但是并没有采取什么特别的行动。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0074"
    $ current_voice = "voice/FEI02A_SUZ0074.ogg"
    "铃羽" "「在柜台的店长也是一伙的啊。露出那种视线」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0068"
    $ current_voice = "voice/FEI02A_FEI0068.ogg"
    "菲利斯" "「但是还送了我小礼物呢」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0075"
    $ current_voice = "voice/FEI02A_SUZ0075.ogg"
    "铃羽" "「那是因为是Ｂｏｓｓ的熟人的关系吧。难道不是委员会的人吗？」"
    "我抿了一口冰可可，在舌尖上感受着特有的甜味。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0069"
    $ current_voice = "voice/FEI02A_FEI0069.ogg"
    "菲利斯" "「果然从人造卫星里逃出来的宇宙生物已经寄生在大家身上了啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0076"
    $ current_voice = "voice/FEI02A_SUZ0076.ogg"
    "铃羽" "「并，并不是那回事吧。所以说，果然ＵＦＯ说还是有点……是吧」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0070"
    $ current_voice = "voice/FEI02A_FEI0070.ogg"
    "菲利斯" "「不调查一下的话是不会知道哦」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0077"
    $ current_voice = "voice/FEI02A_SUZ0077.ogg"
    "铃羽" "「果然，还是变成这样了呢」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0071"
    $ current_voice = "voice/FEI02A_FEI0071.ogg"
    "菲利斯" "「那，休息之后就决定去广播馆咯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA06"),"True","lh/SUZ_FMA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0078"
    $ current_voice = "voice/FEI02A_SUZ0078.ogg"
    "铃羽" "「关于那件事呢有点，Ｂｏｓｓ……」"
    "阿万音的视线垂了下去，突然空气变得沉重起来"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0079"
    $ current_voice = "voice/FEI02A_SUZ0079.ogg"
    "铃羽" "「其实和别人有说好的事情，大概５分钟之后就必须出发了」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0072"
    $ current_voice = "voice/FEI02A_FEI0072.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA03"),"True","lh/SUZ_FMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0080"
    $ current_voice = "voice/FEI02A_SUZ0080.ogg"
    "铃羽" "「那么，今天的调查就到这里……」"

    stop bgm 
    "……谎言。"
    window hide
    play se "SGSE063"



    $ loadBG(2,"BG_BLACK",trans=ImageDissolve(im.Scale("mask/mask00.png",1024,576),1),at=[Transform(alpha=0.5)],over=True)









    "我不经意间又被在柳林神社感受到的那股热血所淹没。"
    "与此同时，在我的内心深处，黑色的情感急速地翻涌上来。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0081"
    $ current_voice = "voice/FEI02A_SUZ0081.ogg"
    "铃羽" "「……抱歉啊，Ｂｏｓｓ」"
    "骗子……"
    "今天不是一直和我在一起调查吗？"
    "难道还是说我搞错了？"
    "如果有事情的话，为什么不更早一些和我说？"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0073"
    $ current_voice = "voice/FEI02A_FEI0073.ogg"
    "菲利斯" "「……讨厌」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0082"
    $ current_voice = "voice/FEI02A_SUZ0082.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0074"
    $ current_voice = "voice/FEI02A_FEI0074.ogg"
    "菲利斯" "「真的是不去不行吗？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0083"
    $ current_voice = "voice/FEI02A_SUZ0083.ogg"
    "铃羽" "「……恩」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0075"
    $ current_voice = "voice/FEI02A_FEI0075.ogg"
    "菲利斯" "「不管怎样都不能不去？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0084"
    $ current_voice = "voice/FEI02A_SUZ0084.ogg"
    "铃羽" "「……恩」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0076"
    $ current_voice = "voice/FEI02A_FEI0076.ogg"
    "菲利斯" "「绝对！？」"
    "好奇怪啊……平时的话很简单地就能自然应对的，但是今天就是做不到。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0085"
    $ current_voice = "voice/FEI02A_SUZ0085.ogg"
    "铃羽" "「抱歉啊，真的不行。……虽然很遗憾」"
    "我混乱了。"
    "理性与欲望的冲撞，让我觉得脑袋快要炸了。"
    "这样不就要和阿万音不欢而散了吗。那可不行……"
    "肯定有什么好办法……有什么……"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0086"
    $ current_voice = "voice/FEI02A_SUZ0086.ogg"
    "铃羽" "「那样的话……在我事情办完之后，可以顺路去一下Ｂｏｓｓ的家里」"
    "我的，家里……？"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0087"
    $ current_voice = "voice/FEI02A_SUZ0087.ogg"
    "铃羽" "「如果困扰的话还是算了……」"
    window hide
    hide background-over 
    with ImageDissolve(im.Scale("mask/mask10.png",1024,576),1)







    "在那瞬间，吞噬了我的黑色情感烟消云散。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0077"
    $ current_voice = "voice/FEI02A_FEI0077.ogg"
    "菲利斯" "「没事哦，热烈欢迎！　来我家住一晚吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA02"),"True","lh/SUZ_FMA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0088"
    $ current_voice = "voice/FEI02A_SUZ0088.ogg"
    "铃羽" "「可以吗！？　那肯定去！　啊，但是如果要请我吃饭的话我要准备下食材吧。不好意思哈，刚好没有剩下能用的」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0078"
    $ current_voice = "voice/FEI02A_FEI0078.ogg"
    "菲利斯" "「食材？　那个黑木会准备好的，但是……那是哪国的风俗啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA04"),"True","lh/SUZ_FMA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0089"
    $ current_voice = "voice/FEI02A_SUZ0089.ogg"
    "铃羽" "「啊……。是吗，不用这么搞啊，啊哈哈哈哈……。那，总之我大概傍晚之前就能办完事情，那时候再联系吧」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0079"
    $ current_voice = "voice/FEI02A_FEI0079.ogg"
    "菲利斯" "「恩，我等着你哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMA01"),"True","lh/SUZ_FMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0090"
    $ current_voice = "voice/FEI02A_SUZ0090.ogg"
    "铃羽" "「那么，差不多该走了」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0080"
    $ current_voice = "voice/FEI02A_FEI0080.ogg"
    "菲利斯" "「恩♪」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0091"
    $ current_voice = "voice/FEI02A_SUZ0091.ogg"
    "铃羽" "「我一定会去的，那再见了！」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0081"
    $ current_voice = "voice/FEI02A_FEI0081.ogg"
    "菲利斯" "「……恩」"
    "之前我还感受着因为阿万音的相助得到的安心感，但现在我感觉自己因为变成孤身一人，只能感受到那种孤独感。"
    "我到底都做了些什么啊……"
    "这样下去，不知道什么时候就会变成无法挽回的局面了……"
    "手上的可可里冰慢慢融化了，变得有些淡了起来——"
    window hide

    stop se


    $ loadBG(0,"BG11A1")

    play se "SGSE366L" loop

    $ targetmailid = cml.setdefault("RM_FEI_SEND_MAY01","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_MAY02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_MAY02_01"])



    $ targetmailid = gc["ScriptMacros"]["RM_FEI_RECV_KUR03_01"]

    $ LR_RM_CHANCE=22
    call CHECK_RM_RECEIVE
    "因为广播馆屋顶变成了禁止进入的状态，所以人也没有，一副寂寥的样子。"
    call CHECK_RM_RECEIVE
    "在那里表示此处危险的标志，只有贴在出入口的门上的一张“禁止入内的纸条”。也许有警卫吧，但是并没有什么封锁线。"
    call CHECK_RM_RECEIVE
    "这里危机感如此淡薄的原因，恐怕还是负责警卫的人员被外星生命体所控制了吧……"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0082"
    $ current_voice = "voice/FEI02A_FEI0082.ogg"
    "菲利斯" "「打扰了……」"
    call CHECK_RM_RECEIVE
    "我又确认了一次周围没有人之后，走近了人造卫星。"
    call CHECK_RM_RECEIVE
    "引起问题的人造卫星卡在８楼和屋顶之间的墙壁里，只有头部露了出来。"
    call CHECK_RM_RECEIVE
    "从那里开始到我所在的地方，有像蜘蛛巢穴一样的裂缝，不会就突然倒了吧……总觉得有点不安。"
    call CHECK_RM_RECEIVE
    "所以最开始我就很小心地前进着，一边确认着安全一边接近了目标。"
    call CHECK_RM_RECEIVE
    "果然人造卫星是都市传说中说的那样的ＵＦＯ吗？"
    call CHECK_RM_RECEIVE
    "——答案很简单，肯定是地球制造的。"
    call CHECK_RM_RECEIVE
    "因为材料一看就是地球上的东西。"
    call CHECK_RM_RECEIVE
    "说白了就简单了……"
    call CHECK_RM_RECEIVE
    "想着至少找找宇宙生物的痕迹吧，稍微调查了一下，结果也是徒劳无功。周围虽然有鞋子一样的足迹，但是期待中的滑溜溜的液体痕迹却完全没有看到。"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0083"
    $ current_voice = "voice/FEI02A_FEI0083.ogg"
    "菲利斯" "「……失望」"
    call CHECK_RM_RECEIVE
    "我到这里来原来期望着的是科幻电影中那样的场景。"
    call CHECK_RM_RECEIVE
    "那种街道上的居民被宇宙生物控制，变成侵略者的人们追赶着主人公的电影战争画面。"
    call CHECK_RM_RECEIVE
    "但是明白了是人造卫星之后那种期待就荡然无存了。"
    call CHECK_RM_RECEIVE
    "我再一次深深地叹了一口气。"
    call CHECK_RM_RECEIVE
    "如果阿万音在这里的话，她到底会是怎样的反应呢。"
    call CHECK_RM_RECEIVE
    "“不能大意啊Ｂｏｓｓ，有人在监视我们这一点是事实”……应该会说些这样的吧。也就是说还要继续调查吗？"
    call CHECK_RM_RECEIVE
    "但是一个人感觉好没劲啊。"

    call CHECK_RM_RECEIVE
    "我放弃了进一步的调查，回家了。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_KUR02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_KUR02_01"])

    window hide

    stop se



    $ loadBG(0,"BG68N")


    $ targetmailid = cml.setdefault("RM_FEI_SEND_KUR03","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_KUR03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_KUR03_01"])



    $ targetmailid = gc["ScriptMacros"]["RM_FEI_RECV_MAY03_01"]

    $ LR_RM_CHANCE=11
    call CHECK_RM_RECEIVE
    "如果阿万音过来的话，我在想着和她先整理一下今天的调查结果。"
    call CHECK_RM_RECEIVE
    "虽然没有能算得上收获的结论，但是如果把发现的事情和注意到的事情写下来的话，应该能得到些什么。"
    call CHECK_RM_RECEIVE
    "那样的话也许就会注意到平时无法察觉的细节。"
    call CHECK_RM_RECEIVE
    "当然我们身后有监视者啦，漆原和黑木似乎在向我隐瞒着什么之类的变化也必须加以考虑。"
    call CHECK_RM_RECEIVE
    "但是真正的重要的是，掺杂在那些大变化中的细小改变。如果忽视了那些，那么真相也将迷雾重重。"
    call CHECK_RM_RECEIVE
    "不对，并不仅仅如此。"
    call CHECK_RM_RECEIVE
    "误入歧途的可能性也很高。"
    call CHECK_RM_RECEIVE
    "总之就是打算和她一件事一件事慢慢探讨。"
    call CHECK_RM_RECEIVE
    "这样的事情也许一生也只有一次。"
    call CHECK_RM_RECEIVE
    "我雀跃不已。"
    call CHECK_RM_RECEIVE
    "但是与我心中雀跃的心情相反的是，到来的阿万音脸上的难受的感情。"

    call CHECK_RM_RECEIVE
    "她来的时候，已经快到日落的时候了。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_MAY02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_MAY02_01"])

    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG26E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0092"
    $ current_voice = "voice/FEI02A_SUZ0092.ogg"
    "铃羽" "「稍微有点迟到了，不好意思啊……」"
    "虽然嘴角露出了笑容，但是并没有打算隐藏自己疲劳的表情，感觉相当灰心的样子。"
    window hide


    $ loadBG(0,"BG68N")

    show screen phonebtn
    show screen phoneSD1

    $ targetmailid = cml.setdefault("RM_FEI_SEND_MAY03","")

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    "她说过和谁有过约定。"
    call CHECK_RM_RECEIVE
    "和那时候的表情相比，阿万音显然是没有得到想要的结果。"
    call CHECK_RM_RECEIVE
    "总之我先把调查的整理工作放在一边，首先为了填饱肚子，和她一起开始准备起了晚餐。"
    call CHECK_RM_RECEIVE
    "这样的话如果能让她心情变好一些就好了……"

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_FEI_RECV_MAY02_02"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_FEI_RECV_MAY02_02"])

    window hide



    $ loadBG(2,"BG68N")





    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA06"),"True","lh/SUZ_AMA06a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    play se "SGSE044" loop




    play se "SGSE222"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0084"
    $ current_voice = "voice/FEI02A_FEI0084.ogg"
    "菲利斯" "「……说起来，试着调查了一下果然不是ＵＦＯ啊喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0093"
    $ current_voice = "voice/FEI02A_SUZ0093.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0085"
    $ current_voice = "voice/FEI02A_FEI0085.ogg"
    "菲利斯" "「虽然不知道是不是人造卫星喵，但是很明显是地球上造出来的东西喵」"
    "但是阿万音只是带着阴沉的表情切着葱。菜刀的声音也很重，她像是被别的什么事情给夺走了魂魄。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0086"
    $ current_voice = "voice/FEI02A_FEI0086.ogg"
    "菲利斯" "「铃羽喵平时会做料理吗？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0094"
    $ current_voice = "voice/FEI02A_SUZ0094.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0087"
    $ current_voice = "voice/FEI02A_FEI0087.ogg"
    "菲利斯" "「铃羽喵？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0095"
    $ current_voice = "voice/FEI02A_SUZ0095.ogg"
    "铃羽" "「恩？　那个……料理、是吗？」"
    stop se
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0096"
    $ current_voice = "voice/FEI02A_SUZ0096.ogg"
    "铃羽" "「当然了哦。但是，像这么认真做的还是第一次。」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0088"
    $ current_voice = "voice/FEI02A_FEI0088.ogg"
    "菲利斯" "「认真做的？　这只是个鸡肉鸡蛋盖饭而已啊」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0097"
    $ current_voice = "voice/FEI02A_SUZ0097.ogg"
    "铃羽" "「我只是煮点野草，还有有时候烤点捕上来的鱼……嘛只是些切好以后烤一下的简单操作而已。调味什么的并不是很在意」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0089"
    $ current_voice = "voice/FEI02A_FEI0089.ogg"
    "菲利斯" "「感觉好有野外求生的感觉啊喵。难道说是露营那样喵？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0098"
    $ current_voice = "voice/FEI02A_SUZ0098.ogg"
    "铃羽" "「也说不定是那样吧。Ｂｏｓｓ是经常做料理吗？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0090"
    $ current_voice = "voice/FEI02A_FEI0090.ogg"
    "菲利斯" "「那种叫法仅限我是黑猫的时候就好」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0099"
    $ current_voice = "voice/FEI02A_SUZ0099.ogg"
    "铃羽" "「是我这么叫习惯了啊。叫你Ｂｏｓｓ也没关系啊？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0091"
    $ current_voice = "voice/FEI02A_FEI0091.ogg"
    "菲利斯" "「如果铃羽希望的话也没关系喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0100"
    $ current_voice = "voice/FEI02A_SUZ0100.ogg"
    "铃羽" "「那，到底怎样？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0092"
    $ current_voice = "voice/FEI02A_FEI0092.ogg"
    "菲利斯" "「料理一直是交给黑木的喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0101"
    $ current_voice = "voice/FEI02A_SUZ0101.ogg"
    "铃羽" "「但是感觉还是很熟练呢，顺序什么的」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0093"
    $ current_voice = "voice/FEI02A_FEI0093.ogg"
    "菲利斯" "「是妈妈教我的呢」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0102"
    $ current_voice = "voice/FEI02A_SUZ0102.ogg"
    "铃羽" "「说起来，今天你妈妈……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "阿万音一瞬间，沉默了下去。好像想到了什么不是很敢问出口的问题。但是我却露出笑脸回答了她。"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0094"
    $ current_voice = "voice/FEI02A_FEI0094.ogg"
    "菲利斯" "「妈妈的话，一直因为工作不在家里喵。一直出差，我想着她能偶尔回来一下的时候又要出差了……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0095"
    $ current_voice = "voice/FEI02A_FEI0095.ogg"
    "菲利斯" "「虽然回来的话，会一直陪着菲利斯……但是一旦离开了家就音信全无」"
    "是的……"
    "所以我才会为了守护爸爸的秋叶原，和大人们战斗着。"
    "这样的事情，已经持续了１０年。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0103"
    $ current_voice = "voice/FEI02A_SUZ0103.ogg"
    "铃羽" "「爸爸呢？」"
    "我沉默着摇了摇头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA06"),"True","lh/SUZ_AMA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0104"
    $ current_voice = "voice/FEI02A_SUZ0104.ogg"
    "铃羽" "「……这样啊」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0096"
    $ current_voice = "voice/FEI02A_FEI0096.ogg"
    "菲利斯" "「要和真由喜保密喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0105"
    $ current_voice = "voice/FEI02A_SUZ0105.ogg"
    "铃羽" "「没告诉她吗？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0097"
    $ current_voice = "voice/FEI02A_FEI0097.ogg"
    "菲利斯" "「不想让她担心喵」"
    "而且，她看着我的目光发生变化的话，太可怕了。"
    "我就是我。我希望她能一直看到现在的我。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0106"
    $ current_voice = "voice/FEI02A_SUZ0106.ogg"
    "铃羽" "「但是，如果邀请她来家里玩的话不就明白了吗」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0098"
    $ current_voice = "voice/FEI02A_FEI0098.ogg"
    "菲利斯" "「所以谁也没有叫来过喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0107"
    $ current_voice = "voice/FEI02A_SUZ0107.ogg"
    "铃羽" "「……？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0099"
    $ current_voice = "voice/FEI02A_FEI0099.ogg"
    "菲利斯" "「邀请过的人，铃羽喵你是第一个。真由喜她们，还没……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0100"
    $ current_voice = "voice/FEI02A_FEI0100.ogg"
    "菲利斯" "「今天的菲利斯，稍微有些奇怪啊。变得像猫一样，突然生气什么的。虽然没有和别人说过自己的事情……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0101"
    $ current_voice = "voice/FEI02A_FEI0101.ogg"
    "菲利斯" "「果然，是因为变成黑猫以后勇气变大了啊……」"
    "阿万音有些迷惑。像是要说些什么的样子张开了嘴，搜寻了一下要说的话，却又不知道该不该说，最终闭上了嘴。"
    "我等待着她的发言。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "像是下了主意，她打破了沉默。"
    play bgm "BGM13"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0108"
    $ current_voice = "voice/FEI02A_SUZ0108.ogg"
    "铃羽" "「今天，我是说要和人见面是吧。」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0102"
    $ current_voice = "voice/FEI02A_FEI0102.ogg"
    "菲利斯" "「……恩」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0109"
    $ current_voice = "voice/FEI02A_SUZ0109.ogg"
    "铃羽" "「那个……要见的人其实是我爸爸哦。」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0103"
    $ current_voice = "voice/FEI02A_FEI0103.ogg"
    "菲利斯" "「……爸爸？」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0110"
    $ current_voice = "voice/FEI02A_SUZ0110.ogg"
    "铃羽" "「我呢，不知道爸爸是怎样的人。但是我知道他就在这条街道上，所以一直在找他……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0104"
    $ current_voice = "voice/FEI02A_FEI0104.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0111"
    $ current_voice = "voice/FEI02A_SUZ0111.ogg"
    "铃羽" "「讨厌啊，Ｂｏｓｓ。不要露出那种表情」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0112"
    $ current_voice = "voice/FEI02A_SUZ0112.ogg"
    "铃羽" "「说起来，今天我也没见到他，很失望啊……」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0113"
    $ current_voice = "voice/FEI02A_SUZ0113.ogg"
    "铃羽" "「但是，我相信我明天一定能遇到他的。因为我知道这里是爸爸的活动区域啊。如果在这里的话我一定能遇到他的」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0105"
    $ current_voice = "voice/FEI02A_FEI0105.ogg"
    "菲利斯" "「这样啊、……太好了」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0114"
    $ current_voice = "voice/FEI02A_SUZ0114.ogg"
    "铃羽" "「都说到这个份上了也没关系啦吧。其实呢，Ｂｏｓｓ。我是……从未来来的。」"
    "……喵？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB04"),"True","lh/SUZ_AMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0115"
    $ current_voice = "voice/FEI02A_SUZ0115.ogg"
    "铃羽" "「广播馆的人工卫星，其实是我乘着过来的时间机器哦」"
    "……阿万音。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0116"
    $ current_voice = "voice/FEI02A_SUZ0116.ogg"
    "铃羽" "「本来的任务是要去１９７５年的，但是因为是单程车票，所以上级允许了我顺路看一下爸爸」"
    "我大吃一惊。"
    "是吗，原来如此……"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RESISTANCE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RESISTANCE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RESISTANCE"])
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0106"
    $ current_voice = "voice/FEI02A_FEI0106.ogg"
    "菲利斯" "「……这样就明白了。铃羽是未来世界的{color=#f00}抵抗者{/color}喵。和机关的那帮人一直战斗着喵！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0117"
    $ current_voice = "voice/FEI02A_SUZ0117.ogg"
    "铃羽" "「Ｂｏｓｓ，为什么你会知道那种事情……？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0107"
    $ current_voice = "voice/FEI02A_FEI0107.ogg"
    "菲利斯" "「菲利斯是机关改造出来的变异人喵。被经过基因改造的猫咬了一口之后，就变得和猫一样任性和喜怒无常了喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB04"),"True","lh/SUZ_AMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0118"
    $ current_voice = "voice/FEI02A_SUZ0118.ogg"
    "铃羽" "「基因改造？是吗……我也听说了哦。３００人委员会的研究机构也在进行基因改造的研究。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB03"),"True","lh/SUZ_AMB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0119"
    $ current_voice = "voice/FEI02A_SUZ0119.ogg"
    "铃羽" "「……但是，任性和喜怒无常？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHESHIRE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHESHIRE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHESHIRE"])
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0108"
    $ current_voice = "voice/FEI02A_FEI0108.ogg"
    "菲利斯" "「不仅如此喵。菲利斯还有看着对方眼睛就能知道他心里在想什么的，名为、{color=#f00}柴郡猫的微笑(Ｃｈｅｓｈｉｒｅ・Ｂｒａｋｅ){/color}的能力喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0120"
    $ current_voice = "voice/FEI02A_SUZ0120.ogg"
    "铃羽" "「啊啊，原来如此。读心术啊！」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0121"
    $ current_voice = "voice/FEI02A_SUZ0121.ogg"
    "铃羽" "「白天的时候，Ｂｏｓｓ看着漆原琉华的眼睛就说他在撒谎。原来是这么一回事啊……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0109"
    $ current_voice = "voice/FEI02A_FEI0109.ogg"
    "菲利斯" "「这么下去未来就会被机关所支配，人类就要灭亡了。所以菲利斯才从研究所里逃出来，秘密地收集情报，寻找着对抗的手段喵！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    "说起来，真的很令人意外。冈部称为『Ｄｕｂｂｉｎｇ１０』的{color=#f00}中二病{/color}妄想游戏，居然还有除了他以外的人会玩。"
    "那样的话，我白天发作的时候配合一下不是挺好的吗。"
    "她和一直以来觉得玩起来很麻烦的冈部不一样，眼睛里透着认真的目光，很有称为演员的潜力啊。"
    "这么想着，我感受到了和变成黑猫暴走的时候一样的快乐。"
    "好像阿万音也在想着一样的事情，是因为电波对上了吗，感觉这种寻找同伴的方法很不寻常啊。"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0122"
    $ current_voice = "voice/FEI02A_SUZ0122.ogg"
    "铃羽" "「好意外啊，没想到居然世界上还有能够理解我的人」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0110"
    $ current_voice = "voice/FEI02A_FEI0110.ogg"
    "菲利斯" "「菲利斯也很高兴喵♪　刚才那些还以为只能和凶真说说的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA03"),"True","lh/SUZ_AMA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0123"
    $ current_voice = "voice/FEI02A_SUZ0123.ogg"
    "铃羽" "「凶真？　啊啊，是说冈部伦太郎吧。虽然我也希望他能帮忙，但是不知道他会不会信我……」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0111"
    $ current_voice = "voice/FEI02A_FEI0111.ogg"
    "菲利斯" "「能够理解你是因为，菲利斯和铃羽喵是挚友啊喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0124"
    $ current_voice = "voice/FEI02A_SUZ0124.ogg"
    "铃羽" "「挚友……？」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0112"
    $ current_voice = "voice/FEI02A_FEI0112.ogg"
    "菲利斯" "「是啊喵。从出生开始就被无形的命运之绳相连，是命中注定的一对喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0125"
    $ current_voice = "voice/FEI02A_SUZ0125.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0113"
    $ current_voice = "voice/FEI02A_FEI0113.ogg"
    "菲利斯" "「……铃羽喵？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0126"
    $ current_voice = "voice/FEI02A_SUZ0126.ogg"
    "铃羽" "「挚友，吗……。让我想起了未来的那些已经忘记的事情……」"
    "不经意间阿万音握住了我的手"
    "那双手十分温暖，但是却又很粗糙。像是男性的皮肤那样，然而透过肌肤传来的纤细感，却毫无疑问是女性的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI02A_SUZ0127"
    $ current_voice = "voice/FEI02A_SUZ0127.ogg"
    "铃羽" "「能遇到你真是太好了呢，Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI02A_FEI0114"
    $ current_voice = "voice/FEI02A_FEI0114.ogg"
    "菲利斯" "「菲利斯也很高兴喵。谢谢你，铃羽喵」"
    window hide


    $ loadBG(2,"BG68N")



    "然后我们就一起做了亲子丼。"
    "一边摆弄着锅碗瓢盆，一边尝着咸淡交换着眼神。"
    "厨房里奏鸣着的菜刀的声音一扫之前的忧郁，不知何时变得抑扬顿挫起来。"


    hide screen phoneSD1
    window hide

    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return











    return





















    return
