label SGFD2_MOE06A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG20A")


    play bgm "BGM21"

    $ date="8/11"
    $ day = "WED"
    python:
        RcvMail(182)
        ReplyMail(182)
        SndMail(183)
    hide screen phonebtn
    hide screen phoneSD1

    "今天的任务不是监视Ｌａｂ，而是有别的。"
    "任务的详细内容我并不清楚。我只是被告知“回收班到了，给他们在秋叶原和那幢大楼里带个路”。"
    "好像是秋叶原里潜伏着从ＳＥＲＮ里逃出来的科学家。"
    "但是……秋叶原里潜伏着ＳＥＲＮ的科学家。这真的是偶然吗？万一，他是知道冈部君他们的存在，来给他们传递情报的话——"
    $ stopvoc("Y01")
    play KUR "MOE06A_Y010000"
    $ current_voice = "voice/MOE06A_Y010000.ogg"
    "巡行者Ａ" "「喂，你这家伙」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0000"
    $ current_voice = "voice/MOE06A_MOE0000.ogg"
    "萌郁" "「……」"
    "从科学家的藏身处中走出一个男子，站在我面前。"
    "没有多想，我后退了一步。"
    "男子与我知道的Ｒｏｕｎｄｅｒ队员有明显不同的气质。"
    "一目了然，他久经锻炼的身体和锐利的眼神……虽然操着一口流利的日语，但不论个子还是金发都说明了他是个外国人。"
    "难道说，是从ＳＥＲＮ本部来的？"
    $ stopvoc("Y01")
    play KUR "MOE06A_Y010001"
    $ current_voice = "voice/MOE06A_Y010001.ogg"
    "巡行者Ａ" "「拿着这个去大塚站的南口。就这些，不接受任何问题，不准看里面是什么东西。」"
    "男人交给我一个手提箱。当然，既然不允许我看里面是什么东西，那我也没有知道的必要。"
    $ stopvoc("Y02")
    play KUR "MOE06A_Y020000"
    $ current_voice = "voice/MOE06A_Y020000.ogg"
    "巡行者Ｂ" "「还有，之后干完了怎么办？尤其是，尸体的处理挺麻烦的啊。」"
    "尸体……"
    "刚刚，他确实这么说了。"
    "感觉他完全不把这个词当回事。"
    "现在，站在我面前的这些人，会去……杀掉科学家……"
    "我以不会被他们察觉的动作吞了口口水。"
    $ stopvoc("Y01")
    play KUR "MOE06A_Y010002"
    $ current_voice = "voice/MOE06A_Y010002.ogg"
    "巡行者Ａ" "「没关系」"
    $ stopvoc("Y01")
    play KUR "MOE06A_Y010003"
    $ current_voice = "voice/MOE06A_Y010003.ogg"
    "巡行者Ａ" "「之后的处理……就交给例行部队吧」"
    "例行部队……是什么呢？"
    "虽然，那个ＦＢ在邮件里也提到了，但是我对于“之后的处理”这个说法有些在意。"
    "ＳＥＲＮ的力量，似乎已经渗透到各个国家的中心。如果是ＳＥＲＮ的话，就算杀人这种事……也许也可以轻易地摆平。"
    "其他的可能性，因为过于害怕而不敢考虑了。"
    $ stopvoc("Y02")
    play KUR "MOE06A_Y020001"
    $ current_voice = "voice/MOE06A_Y020001.ogg"
    "巡行者Ｂ" "「目前，先各自行动。１２日８点３０在γ( Gamma )集合」"
    window hide



    $ loadBG(0,"BG40A")

    "Ｒｏｕｎｄｅｒ们的身影消失之后，我走向车站。"
    "现在，必须将回收的手提公文包交给其他的Ｒｏｕｎｄｅｒ。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0001"
    $ current_voice = "voice/MOE06A_MOE0001.ogg"
    "萌郁" "「……快点结束吧」"
    "总感觉从不知道里面装着什么的手提包中传出了血的味道。"
    window hide


    $ loadBG(0,"BG31N")

    $ targetmailid = cml.setdefault("RM_MOE_SEND_CRS02","")

    $ LR_RM_CHANCE=1

    call CHECK_RM_RECEIVE



    "我走到了大塚站的南口，将手提包交给了素未谋面但认出了我的女性。这样我的工作就算完成了。"
    "那名女性，虽然对着手里的手机说道“文件收到了”，但明显是在装样子。"
    "虽然对于像我这样的卒子来说怎么样都无所谓了。"
    "逃亡中的科学家的名字也无所谓。Ｒｏｕｎｄｅｒ们的名字也无所谓。那名女性的名字也无所谓。什么都不知道，就已经结束了。"
    "稍稍，松了口气。"
    "心情一旦变得放松下来，就想要早点回家好好睡一觉。"
    window hide
    stop se



    $ loadBG(0,"BG13N1")

    "尽管如此，回到秋叶原的时候，遇到了两个认识的人。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA02"),"True","lh/CRS_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0000"
    $ current_voice = "voice/MOE06A_MAY0000.ogg"
    "真由理" "「啊，是萌郁♪」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0000"
    $ current_voice = "voice/MOE06A_CRS0000.ogg"
    "红莉栖" "「哈啰—」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0002"
    $ current_voice = "voice/MOE06A_MOE0002.ogg"
    "萌郁" "「……」"
    "椎名和牧濑好巧不巧地和我搭话了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0001"
    $ current_voice = "voice/MOE06A_MAY0001.ogg"
    "真由理" "「嘟嘟噜♪」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0003"
    $ current_voice = "voice/MOE06A_MOE0003.ogg"
    "萌郁" "「……你好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0001"
    $ current_voice = "voice/MOE06A_CRS0001.ogg"
    "红莉栖" "「我们现在要去Ｌａｂ。萌郁也是这么打算的吧？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0004"
    $ current_voice = "voice/MOE06A_MOE0004.ogg"
    "萌郁" "「诶……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0002"
    $ current_voice = "voice/MOE06A_CRS0002.ogg"
    "红莉栖" "「真是的，冈部老是干这种事很让人头疼诶。完全不考虑别人的情况就给别人发邮件叫他们过去」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0005"
    $ current_voice = "voice/MOE06A_MOE0005.ogg"
    "萌郁" "「冈部君发的……邮件？」"
    "我急忙打开手机。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MOE06A_RECV_OKA01"]
    $ RcvMail(targetmailid)
    call read_last_mail


    "确实，冈部君有给我发过邮件。任务中关机了，所以没注意到的样子。"
    window hide
    call hide_phone


    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0002"
    $ current_voice = "voice/MOE06A_MAY0002.ogg"
    "真由理" "「呐呐，萌郁，难得的机会一起去吧♪」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0006"
    $ current_voice = "voice/MOE06A_MOE0006.ogg"
    "萌郁" "「诶……但是……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0003"
    $ current_voice = "voice/MOE06A_CRS0003.ogg"
    "红莉栖" "「啊，再不抓紧的话好像要迟到了」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0003"
    $ current_voice = "voice/MOE06A_MAY0003.ogg"
    "真由理" "「好了，走吧走吧♪」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0007"
    $ current_voice = "voice/MOE06A_MOE0007.ogg"
    "萌郁" "「诶……诶诶……」"
    "我被椎名牵着手，半拖半拉地来到了Ｌａｂ。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True
    $ loadBG(0,"EV_MOE007D")

    play bgm "BGM07"

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0000"
    $ current_voice = "voice/MOE06A_OKA0000.ogg"
    "伦太郎" "「好－嘞，全员到齐。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0004"
    $ current_voice = "voice/MOE06A_CRS0004.ogg"
    "红莉栖" "「明明是最后一个到的还要装出一副了不起的样子吗」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007C"]]["Check"]=True


    $ loadBG(2,"EV_MOE007C")



    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0001"
    $ current_voice = "voice/MOE06A_OKA0001.ogg"
    "伦太郎" "「才、才不是迟到！主角最后才登场不是惯例嘛。不如说，这一切都是预定好的——这一切都是命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择！」"
    $ stopvoc("DAR")
    play DAR "MOE06A_DAR0000"
    $ current_voice = "voice/MOE06A_DAR0000.ogg"
    "至" "「找借口乙」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0005"
    $ current_voice = "voice/MOE06A_CRS0005.ogg"
    "红莉栖" "「其他人呢？」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True


    $ loadBG(2,"EV_MOE007D")



    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0002"
    $ current_voice = "voice/MOE06A_OKA0002.ogg"
    "伦太郎" "「啊啊……打工战士说有事，菲利斯在打工，琉华子好像在神社帮忙。真是的，明明是足以左右世界命运的会议，那些家伙却这么靠不住。」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0004"
    $ current_voice = "voice/MOE06A_MAY0004.ogg"
    "真由理" "「没办法呢，毕竟是突然提出来的会议。」"
    $ stopvoc("DAR")
    play DAR "MOE06A_DAR0001"
    $ current_voice = "voice/MOE06A_DAR0001.ogg"
    "至" "「是啊是啊。大家可没有都和冈伦那样闲呢。」"
    "好像还在生气的样子……"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0003"
    $ current_voice = "voice/MOE06A_OKA0003.ogg"
    "伦太郎" "「那么，现在开始第２３５７次圆桌会议」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0006"
    $ current_voice = "voice/MOE06A_CRS0006.ogg"
    "红莉栖" "「邮件里明明写的是第１９７８次」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007C"]]["Check"]=True


    $ loadBG(2,"EV_MOE007C")



    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0004"
    $ current_voice = "voice/MOE06A_OKA0004.ogg"
    "伦太郎" "「唔……作为助手不要在意这些细节」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0007"
    $ current_voice = "voice/MOE06A_CRS0007.ogg"
    "红莉栖" "「谁是你的助手啊」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GDGD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GDGD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GDGD"])
    $ stopvoc("DAR")
    play DAR "MOE06A_DAR0002"
    $ current_voice = "voice/MOE06A_DAR0002.ogg"
    "至" "「不管怎么看又是一如既往的{color=#f00}ｇｄｇｄ{/color}啊，多谢多谢」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0005"
    $ current_voice = "voice/MOE06A_MAY0005.ogg"
    "真由理" "「今天是关于什么的话题呢？每次真由喜都觉得好难啊完全听不懂的说」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True


    $ loadBG(2,"EV_MOE007D")



    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0005"
    $ current_voice = "voice/MOE06A_OKA0005.ogg"
    "伦太郎" "「咳咳。抱歉，被助手带跑话题了。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0008"
    $ current_voice = "voice/MOE06A_CRS0008.ogg"
    "红莉栖" "「你还真敢这么说啊。」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0006"
    $ current_voice = "voice/MOE06A_OKA0006.ogg"
    "伦太郎" "「那，好。今天的话题是——」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0007"
    $ current_voice = "voice/MOE06A_OKA0007.ogg"
    "伦太郎" "「我们是否要像之前那样继续时间机器的研究。关于这一点希望和大家谈一谈」"
    window hide
    stop bgm 


    $ loadBG(2,"BG02N2")



    show screen phonebtn
    show screen phoneSD1
    "……！！"
    "求之不得的话题。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "总之先把圆桌会议开始了这件事告诉她。"
    call send_mail (id=[185,186,187,188,189,190])
    window hide








    $ targetmailid = gc["ScriptMacros"]["FM_MOE06A_SEND_TEN02"]






    $ targetmailid = gc["ScriptMacros"]["FM_MOE06A_RECV_TEN02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "给ＦＢ发了邮件后很快收到了回信。"
    window hide
    call read_last_mail


    "并不是很喜欢在这种场合发言……"
    "但是，是ＦＢ的指示。所以不能不做。"
    "不努力的话。"
    "这个话题如果好好地利用一下的话……可以阻止时间机器的研究。"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0009"
    $ current_voice = "voice/MOE06A_CRS0009.ogg"
    "红莉栖" "「我认为，我们不应该停止时间机器的研究」"
    window hide
    call hide_phone



    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0008"
    $ current_voice = "voice/MOE06A_MOE0008.ogg"
    "萌郁" "「……！」"
    window hide



    $ loadBG(2,"BG02NS2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BMB06"),"True","lh/CRS_BMB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    play bgm "FD2BGM05"
    "是哦……牧濑是为了父亲才进行时间机器的研究的。"
    "不会这么简单地就说放弃。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True


    $ loadBG(2,"EV_MOE007D")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0008"
    $ current_voice = "voice/MOE06A_OKA0008.ogg"
    "伦太郎" "「哦？这回吹的是什么风啊，Ｃｈｒｉｓｔｉｎａ。最初你不是还怀疑这项研究的么？」"
    window hide

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0010"
    $ current_voice = "voice/MOE06A_CRS0010.ogg"
    "红莉栖" "「别叫我Ｃｈｒｉｓｔｉｎａ！」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0011"
    $ current_voice = "voice/MOE06A_CRS0011.ogg"
    "红莉栖" "「嘛那种事先不管。现在呢。」"
    window hide

    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0009"
    $ current_voice = "voice/MOE06A_OKA0009.ogg"
    "伦太郎" "「所以说？你为什么想要继续研究下去呢？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0012"
    $ current_voice = "voice/MOE06A_CRS0012.ogg"
    "红莉栖" "「只是为了满足好奇心……这么说就够了。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0013"
    $ current_voice = "voice/MOE06A_CRS0013.ogg"
    "红莉栖" "「如果要说第二个理由，就是为了搞清楚至今为止的Ｄｍａｉｌ为何没有造成时间悖论——」"
    "渐渐变成了只有他们两人才能进行的对话了。"
    "但是……这里不加入对话的话就会被牧濑的意见主导了。"
    "总之，不插嘴的话。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0009"
    $ current_voice = "voice/MOE06A_MOE0009.ogg"
    "萌郁" "「那个……我能说一句吗？」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0010"
    $ current_voice = "voice/MOE06A_OKA0010.ogg"
    "伦太郎" "「但是，有这个Ｄｍａｉｌ的话过去想怎么改变都可以吧？就算有时间悖论也应该没什么好怕的。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0014"
    $ current_voice = "voice/MOE06A_CRS0014.ogg"
    "红莉栖" "「问题是。产生悖论的时候万一我们没有注意到呢？所以我才认为我们应该更谨慎地进行研究。」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0011"
    $ current_voice = "voice/MOE06A_OKA0011.ogg"
    "伦太郎" "「你自相矛盾了呢。这就好像在说我们不应该继续做下去了一样。最初是谁说应该继续做下去的？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0015"
    $ current_voice = "voice/MOE06A_CRS0015.ogg"
    "红莉栖" "「谁都没说不做实验了。我说的是，谨慎地进行下去。你们那样轻率的实验，是很容易出事的啊——」"
    "不行…… "
    "虽然很不甘心，但无法加入两人的对话。"
    "那样的话——"
    window hide









    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[192,193,194])











    $ targetmailid = gc["ScriptMacros"]["FM_MOE06A_SEND_OKA01"]






    call hide_phone


    play se "SGSE801"

    hide screen phoneSD1
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True
    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0012"
    $ current_voice = "voice/MOE06A_OKA0012.ogg"
    "伦太郎" "「那一点的话我有Ｒｅａｄｉｎｇ　Ｓｔｅｉｎｅｒ所以不用担心」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0016"
    $ current_voice = "voice/MOE06A_CRS0016.ogg"
    "红莉栖" "「就算你说不用担心……没有确切的证据还是会担心的啊」"
    "咦？"
    "明明邮件已经发过去了，还是无视了吗？"
    "不，应该是没有注意到吧。那么，再试一次好了。"
    window hide









    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[195,196,197,198])











    $ targetmailid = gc["ScriptMacros"]["FM_MOE06A_SEND_OKA02"]








    play se "SGSE801"

    hide screen phoneSD1
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE007D"]]["Check"]=True
    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0013"
    $ current_voice = "voice/MOE06A_OKA0013.ogg"
    "伦太郎" "「确实没有证据证明。但，因为这是我的主观体验所以无法证明。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0017"
    $ current_voice = "voice/MOE06A_CRS0017.ogg"
    "红莉栖" "「那样的话，想想有没有别的方法吧？比如说──」"
    "不行……果然冈部君沉醉于辩论中完全没有注意到邮件。"
    "怎么办啊，这样下去就无法完成ＦＢ给的任务了……"
    window hide



    $ loadBG(2,"BG01N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0006"
    $ current_voice = "voice/MOE06A_MAY0006.ogg"
    "真由理" "「呐呐。萌郁，没事吗？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0010"
    $ current_voice = "voice/MOE06A_MOE0010.ogg"
    "萌郁" "「……！？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0007"
    $ current_voice = "voice/MOE06A_MAY0007.ogg"
    "真由理" "「怎么说呢，你刚才好像有想对冈伦他们说的话？」"
    "是注意到我无法加入对话了吗，椎名过来和我搭话了。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0011"
    $ current_voice = "voice/MOE06A_MOE0011.ogg"
    "萌郁" "「没……没关系……」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0008"
    $ current_voice = "voice/MOE06A_MAY0008.ogg"
    "真由理" "「想说什么的话，好好地告诉他们会比较好哦」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0012"
    $ current_voice = "voice/MOE06A_MOE0012.ogg"
    "萌郁" "「但是……打扰他们两个，不太好吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "但是，椎名朝我微笑了一下，插入到已经进行到白热化的两个人的对话当中。"
    window hide


    $ loadBG(2,"BG02N2")




    stop bgm 

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC03"),"True","lh/MAY_CSC03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC04"),"True","lh/CRS_BSC04a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0009"
    $ current_voice = "voice/MOE06A_MAY0009.ogg"
    "真由理" "「呐呐，两位都稍等！」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0014"
    $ current_voice = "voice/MOE06A_OKA0014.ogg"
    "伦太郎" "「真、真由理？　怎么了突然！？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0018"
    $ current_voice = "voice/MOE06A_CRS0018.ogg"
    "红莉栖" "「发生什么了？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0010"
    $ current_voice = "voice/MOE06A_MAY0010.ogg"
    "真由理" "「萌郁好像有什么想说的，请听一下吧。」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0011"
    $ current_voice = "voice/MOE06A_MAY0011.ogg"
    "真由理" "「你们两位讨论得太投入了哟。完全没有注意到萌郁想说些什么的样子。」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0019"
    $ current_voice = "voice/MOE06A_CRS0019.ogg"
    "红莉栖" "「诶？是这样的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSA05"),"True","lh/CRS_BSA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0020"
    $ current_voice = "voice/MOE06A_CRS0020.ogg"
    "红莉栖" "「不好意思啊，萌郁。刚刚稍微太投入了些。」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0013"
    $ current_voice = "voice/MOE06A_MOE0013.ogg"
    "萌郁" "「……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0015"
    $ current_voice = "voice/MOE06A_OKA0015.ogg"
    "伦太郎" "「好啊，指压师。就好好地让我洗耳恭听你想到的将混沌带到这个世界的方法吧。来吧，说说看啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "椎名朝我微笑着。"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0012"
    $ current_voice = "voice/MOE06A_MAY0012.ogg"
    "真由理" "「太好了呢。萌郁。」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0014"
    $ current_voice = "voice/MOE06A_MOE0014.ogg"
    "萌郁" "「……谢谢、你」"
    "椎名就好像为自己感到高兴一样笑着。我向她怯生生地低下了头。"
    "再一次，藏在胸口的疼痛又袭来了。"
    "我……正在欺骗如此温柔善良的人哦？"
    "就算是任务，对我来说也——"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0015"
    $ current_voice = "voice/MOE06A_MOE0015.ogg"
    "萌郁" "「……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSC06"),"True","lh/CRS_BSC06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0021"
    $ current_voice = "voice/MOE06A_CRS0021.ogg"
    "红莉栖" "「萌郁？怎么了吗，脸色看起来很差哦？」"
    "想起了刚刚完成的任务。"
    "轻易夺走的生命。"
    "将杀人事件化为子虚乌有的事件。"
    "在这个任务之后，万一我也要将这些人和……之前的科学家一样……"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0016"
    $ current_voice = "voice/MOE06A_MOE0016.ogg"
    "萌郁" "「我想……出去透透气。」"
    $ stopvoc("OKA")
    play OKA "MOE06A_OKA0016"
    $ current_voice = "voice/MOE06A_OKA0016.ogg"
    "伦太郎" "「喂，喂。这是怎么了？刚刚不是还想说些什么的吗？」"
    play se "SGSE024"
    window hide


    $ loadBG(0,"BG_BLACK")
    hide screen phonebtn

    "我，没有和冈部君在一起讨论的资格。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG24N")



    $ targetmailid = gc["ScriptMacros"]["RM_MOE_RECV_CRS04_01"]
    $ RcvMail(targetmailid)


    $ targetmailid = gc["ScriptMacros"]["RM_MOE_RECV_MAY04_01"]
    $ RcvMail(targetmailid)



    play bgm "FD2BGM05"
    show screen phonebtn
    show screen phoneSD1
    "从Ｌａｂ里飞奔而出的我，没有目的地在秋叶原里闲逛。"
    "虽然也可以就这样回家……但想到那样就等于背叛了Ｌａｂｍ ｅ ｍ的众人，又觉得无法那么做。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_MAY04_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_MAY04_01"])

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MOE_RECV_CRS04_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MOE_RECV_CRS04_01"])

    "不……到底背叛的是哪一边呢——"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0013"
    $ current_voice = "voice/MOE06A_MAY0013.ogg"
    "？？？" "「啊——！　有了有了♪」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0017"
    $ current_voice = "voice/MOE06A_MOE0017.ogg"
    "萌郁" "「……诶？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA04"),"True","lh/MAY_ASA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0022"
    $ current_voice = "voice/MOE06A_CRS0022.ogg"
    "红莉栖" "「太好了，原来你在这里啊」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0018"
    $ current_voice = "voice/MOE06A_MOE0018.ogg"
    "萌郁" "「为什么……你们会在……？」"
    "椎名和牧濑好像追我追得上气不接下气"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0014"
    $ current_voice = "voice/MOE06A_MAY0014.ogg"
    "真由理" "「萌郁，突然就从Ｌａｂ里跑出来了呢。很担心你所以就出来找你了哦？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0023"
    $ current_voice = "voice/MOE06A_CRS0023.ogg"
    "红莉栖" "「和冈部还有桥田联系吧。就说萌郁已经找到了，就回Ｌａｂ」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0019"
    $ current_voice = "voice/MOE06A_MOE0019.ogg"
    "萌郁" "「……我很抱歉」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB01"),"True","lh/MAY_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB02"),"True","lh/CRS_ASB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0015"
    $ current_voice = "voice/MOE06A_MAY0015.ogg"
    "真由理" "「并不是需要道歉的事哦」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0024"
    $ current_voice = "voice/MOE06A_CRS0024.ogg"
    "红莉栖" "「是呢是呢。我也有这样从Ｌａｂ里飞奔而出过呢。主要是冈部的责任。」"
    "又是这样吗……又一次，Ｌａｂｍｅｍ的大家对我这么温柔。"
    "就算是这样的我，大家也毫不怀疑，温柔地与我相处。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0020"
    $ current_voice = "voice/MOE06A_MOE0020.ogg"
    "萌郁" "「……为什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA04"),"True","lh/MAY_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0025"
    $ current_voice = "voice/MOE06A_CRS0025.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0021"
    $ current_voice = "voice/MOE06A_MOE0021.ogg"
    "萌郁" "「为什么大家……对于这样的我还是那么的温柔？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0022"
    $ current_voice = "voice/MOE06A_MOE0022.ogg"
    "萌郁" "「因为……我是──」"
    "……不能说。"
    "不应该，说出来。"
    "是对于突然停下来的我感到担心吗，椎名温柔的声音传了过来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0016"
    $ current_voice = "voice/MOE06A_MAY0016.ogg"
    "真由理" "「萌郁」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0017"
    $ current_voice = "voice/MOE06A_MAY0017.ogg"
    "真由理" "「不要问为什么哦。理由什么的根本没有呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0018"
    $ current_voice = "voice/MOE06A_MAY0018.ogg"
    "真由理" "「因为，我们大家都是Ｌａｂｍｅｍ不是吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB08"),"True","lh/CRS_ASB08a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0026"
    $ current_voice = "voice/MOE06A_CRS0026.ogg"
    "红莉栖" "「是呢。Ｌａｂｍｅｍ的大家，都是伙伴呢」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0023"
    $ current_voice = "voice/MOE06A_MOE0023.ogg"
    "萌郁" "「但是……我从来就没有为Ｌａｂ做过什么事……一件也没有……」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0024"
    $ current_voice = "voice/MOE06A_MOE0024.ogg"
    "萌郁" "「这样的我……算不上是伙伴吧……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "ＦＢ出现在我的脑海里。"
    "最近的我，也没有为ＦＢ做过什么事。"
    "如果派不上用场的话，就抛弃掉。"
    "如果派不上用场的话，就不是伙伴……"

    stop bgm 
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0019"
    $ current_voice = "voice/MOE06A_MAY0019.ogg"
    "真由理" "「萌郁」"
    "椎名俯下身来，和蹲着的我视线重合了。"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0020"
    $ current_voice = "voice/MOE06A_MAY0020.ogg"
    "真由理" "「真由喜呢，认为伙伴的定义并不是那样的」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0025"
    $ current_voice = "voice/MOE06A_MOE0025.ogg"
    "萌郁" "「……诶？」"
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE003A"]]["Check"]=True
    $ loadBG(0,"EV_MOE003A")

    hide screen phonebtn
    play bgm "FD2BGM06"
    "我抬起头来。"
    "椎名和牧濑，都朝我温柔地笑着。"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0027"
    $ current_voice = "voice/MOE06A_CRS0027.ogg"
    "红莉栖" "「如果只是因为利害关系或者利用价值才聚集在一起的人就能称为伙伴的话，我早就离开这个Ｌａｂ了」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0021"
    $ current_voice = "voice/MOE06A_MAY0021.ogg"
    "真由理" "「嗯，嗯♪真由喜也从来没有在冈伦和克里斯酱的研究中发挥过作用哦？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0026"
    $ current_voice = "voice/MOE06A_MOE0026.ogg"
    "萌郁" "「但是」 "
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0027"
    $ current_voice = "voice/MOE06A_MOE0027.ogg"
    "萌郁" "「……追我出来这件事明明就是没有任何意义的……为什么？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0022"
    $ current_voice = "voice/MOE06A_MAY0022.ogg"
    "真由理" "「那个呢，就是说呢——」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0023"
    $ current_voice = "voice/MOE06A_MAY0023.ogg"
    "真由理" "「因为萌郁是我们的朋友呐」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0028"
    $ current_voice = "voice/MOE06A_MOE0028.ogg"
    "萌郁" "「朋……友………？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0028"
    $ current_voice = "voice/MOE06A_CRS0028.ogg"
    "红莉栖" "「要说Ｌａｂｍｅｍ是怎样的关系体现的话，我也觉得说是朋友最为合适。」"
    "并不是因为利害关系而聚集在一起——那就是朋友。"
    "对于和除了ＦＢ以及Ｒｏｕｎｄｅｒ之外的人类没有任何交集的我来说，这仿佛就是梦一样的话。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0029"
    $ current_voice = "voice/MOE06A_MOE0029.ogg"
    "萌郁" "「朋友……好羡慕」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0029"
    $ current_voice = "voice/MOE06A_CRS0029.ogg"
    "红莉栖" "「萌郁，不是那样的哦」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0030"
    $ current_voice = "voice/MOE06A_MOE0030.ogg"
    "萌郁" "「……诶？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0024"
    $ current_voice = "voice/MOE06A_MAY0024.ogg"
    "真由理" "「萌郁是Ｌａｂ的一员嘛，所以是真由喜的朋友哦」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0031"
    $ current_voice = "voice/MOE06A_MOE0031.ogg"
    "萌郁" "「我是你的……朋友？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0025"
    $ current_voice = "voice/MOE06A_MAY0025.ogg"
    "真由理" "「是的♪　朋友」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0030"
    $ current_voice = "voice/MOE06A_CRS0030.ogg"
    "红莉栖" "「不是那样的话，也不会这样拼命地出来找你了」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0032"
    $ current_voice = "voice/MOE06A_MOE0032.ogg"
    "萌郁" "「……」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0026"
    $ current_voice = "voice/MOE06A_MAY0026.ogg"
    "真由理" "「诶？萌郁……难道说哭了？？」"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0031"
    $ current_voice = "voice/MOE06A_CRS0031.ogg"
    "红莉栖" "「诶？等、等等为什么！？我们说错了什么了吗？」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0033"
    $ current_voice = "voice/MOE06A_MOE0033.ogg"
    "萌郁" "「不对……不对啊……」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0034"
    $ current_voice = "voice/MOE06A_MOE0034.ogg"
    "萌郁" "「……是太高兴了……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE003B"]]["Check"]=True


    $ loadBG(2,"EV_MOE003B")



    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0027"
    $ current_voice = "voice/MOE06A_MAY0027.ogg"
    "真由理" "「萌郁」"
    "椎名紧紧地握住了我的手。"
    "那双手的温暖与温柔，我从未感受过。"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0032"
    $ current_voice = "voice/MOE06A_CRS0032.ogg"
    "红莉栖" "「突然哭起来了，有点吓到我了呢」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0035"
    $ current_voice = "voice/MOE06A_MOE0035.ogg"
    "萌郁" "「不好……意思……」"
    "直到现在，我没有发现过除了被利用以外自己的存在价值。"
    "就算是ＦＢ，虽然明白自己是被她利用着……但完全不怨恨她。"
    "不如说，被利用的话就能和ＦＢ变得更亲密。这么想想就安心了。"
    "但是……就算是这样的我，也存在不是因为能够利用我而接受我的人……"
    "——十分开心。"
    "从心底里，这么想着。"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0028"
    $ current_voice = "voice/MOE06A_MAY0028.ogg"
    "真由理" "「给。这块手帕，请用♪」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0036"
    $ current_voice = "voice/MOE06A_MOE0036.ogg"
    "萌郁" "「谢谢……椎名」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0029"
    $ current_voice = "voice/MOE06A_MAY0029.ogg"
    "真由理" "「我们是朋友嘛，叫名字也可以哦」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0037"
    $ current_voice = "voice/MOE06A_MOE0037.ogg"
    "萌郁" "「名字……？」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0030"
    $ current_voice = "voice/MOE06A_MAY0030.ogg"
    "真由理" "「是呢，真由喜也想叫萌郁的名字呢」"
    "名字……"
    "我从来没有在邮件之外用如此亲昵的方式叫过别人……不知为何有些害羞。"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0038"
    $ current_voice = "voice/MOE06A_MOE0038.ogg"
    "萌郁" "「那个……」"
    $ stopvoc("MOE")
    play MOE "MOE06A_MOE0039"
    $ current_voice = "voice/MOE06A_MOE0039.ogg"
    "萌郁" "「真由理……」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0031"
    $ current_voice = "voice/MOE06A_MAY0031.ogg"
    "真由理" "「到——」"
    "将自己的手举得高高的，椎名……真由理对我开心地笑了。"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0032"
    $ current_voice = "voice/MOE06A_MAY0032.ogg"
    "真由理" "「被萌郁用名字叫了呢。好高兴啊♪」"
    "无忧无虑的笑容，将那种温暖的心情灌注到了我的胸膛里。"
    "朋友……就是如此的温暖吗。"
    $ stopvoc("CRS")
    play CRS "MOE06A_CRS0033"
    $ current_voice = "voice/MOE06A_CRS0033.ogg"
    "红莉栖" "「那，差不多该回Ｌａｂ了呢」"
    $ stopvoc("MAY")
    play MAY "MOE06A_MAY0033"
    $ current_voice = "voice/MOE06A_MAY0033.ogg"
    "真由理" "「冈伦和桶子君肯定担心地要死呢♪」"
    "这一天，我有了出生以来第一个朋友。"
    "大家，都是非常温柔的朋友。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "但是，这样的朋友即将陷入险境——而将他们带入这样的险境的人就是自己。一旦这么想……就切实地感受到现在自己正在做的事，有多么的可怕。"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
