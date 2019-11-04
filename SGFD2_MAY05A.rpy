label SGFD2_MAY05A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG_BLACK")



    $ date="8/16"
    $ day = "MON"
    python:
        cml = {}
        while len(rml)>0 and rml[0]["MetaData"]["Time"] > 1531 and rml[0]["MetaData"]["Date"] >= 816:
            UnreadMail(rml[0]["MailNumber"])
            notLate(rml[0]["MailNumber"])
            del rml[0]
        while len(sml)>0 and sml[0]["MetaData"]["Time"] > 1531 and sml[0]["MetaData"]["Date"] >= 816:
            del sml[0]
        while len(lml)>0 and gc["MailData"][lml[0]]["MetaData"]["Time"] > 1531 and gc["MailData"][lml[0]]["MetaData"]["Date"] >= 816:
            notLate(lml[0])
            del lml[0]
    hide screen phonebtn
    hide screen phoneSD1

    "脑袋里乱哄哄的。"
    "不，不光是脑袋里面……眼前的东西也是乱糟糟的。"
    "──好难受。"
    "感受到前额剧烈的头痛和耳鸣"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0000"
    $ current_voice = "voice/MAY05A_MAY0000.ogg"
    "真由理" "「……呜呜……呜呜……啊啊……」"
    "捂着嘴，抱着头，蹲了下去。"
    "脑袋好像被叉子刺穿了一样。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0001"
    $ current_voice = "voice/MAY05A_MAY0001.ogg"
    "真由理" "「呜……呜……啊啊………」"
    "明明对于这种痛苦应该只想避之不及的。"
    "在疼痛中，稍微混杂着一些快感，是因为这个么，想要追寻那股快感。"
    "渐渐的，疼痛消散了。"


    "某个地方，电话响了起来。"
    "在哪儿？　是谁的？"
    window hide


    $ loadBG(0,"BG62A")






    "惊恐地睁开了眼睛──熟悉的真由喜的房间映入了眼帘。"
    "好奇怪啊……明明是在Ｌａｂ的，为什么？"
    "手机掉在了地上。"
    "慢慢地捡起了手机，接听了电话。"
    show screen phoneSD1
    window hide
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)





    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0002"
    $ current_voice = "voice/MAY05A_MAY0002.ogg"
    "真由理" "「喂喂……」"

    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0000"
    $ current_voice = "voice/MAY05A_FEI0000.ogg"
    "菲利斯" "「是因为信号差喵？　电话断掉了喵」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0003"
    $ current_voice = "voice/MAY05A_MAY0003.ogg"
    "真由理" "「那个……菲利斯？　怎么了……刚才干什么来着……」"

    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0001"
    $ current_voice = "voice/MAY05A_FEI0001.ogg"
    "菲利斯" "「真由喜，怎么了喵？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0004"
    $ current_voice = "voice/MAY05A_MAY0004.ogg"
    "真由理" "「那个……真由喜也不知道……真由喜……是在跟菲利斯打电话来着吗？」"



    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0002"
    $ current_voice = "voice/MAY05A_FEI0002.ogg"
    "菲利斯" "「是的喵！　在谈关于红喵的事喵」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0005"
    $ current_voice = "voice/MAY05A_MAY0005.ogg"
    "真由理" "「红喵……」"

    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0003"
    $ current_voice = "voice/MAY05A_FEI0003.ogg"
    "菲利斯" "「不过在通话的过程中有别的电话打来了，真由喜就保留了菲利斯的电话，去接那个电话了喵」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0006"
    $ current_voice = "voice/MAY05A_MAY0006.ogg"
    "真由理" "「这样啊」"
    "记忆很模糊。"



    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0004"
    $ current_voice = "voice/MAY05A_FEI0004.ogg"
    "菲利斯" "「菲利斯把红喵惹生气了……这件事喵」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0007"
    $ current_voice = "voice/MAY05A_MAY0007.ogg"
    "真由理" "「不……并不是这样的……红莉栖发来了让真由喜去帮她给菲利斯道歉的短信」"
    play bgm "BGM25"
    "不可思议的感觉，好像同样的话已经重复说了好几遍了。"
    "怎么回事呢？"
    "明明没有什么奇怪的事，却感觉好奇怪。"

    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0005"
    $ current_voice = "voice/MAY05A_FEI0005.ogg"
    "菲利斯" "「但是……」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0008"
    $ current_voice = "voice/MAY05A_MAY0008.ogg"
    "真由理" "「现在……虽然联系不上……会想办法联系……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0009"
    $ current_voice = "voice/MAY05A_MAY0009.ogg"
    "真由理" "「……她的……」"
    "联系不上？"
    "好奇怪啊……明明已经联系上了。"
    hide screen phoneSD1
    window hide



















    show screen phoneSD1
    "不，不对。"
    "虽然试着联系了，但是红莉栖酱不接电话。"
    "担心红莉栖酱。"
    hide screen phoneSD1
    window hide








    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003A"]]["Check"]=True











    show screen phoneSD1
    "不，红莉栖酱没事。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0010"
    $ current_voice = "voice/MAY05A_MAY0010.ogg"
    "真由理" "「……呜呜，到底是……哪边？」"
    "脑袋里一阵一阵的疼痛，痛得让人感觉有些恶心。"



    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0006"
    $ current_voice = "voice/MAY05A_FEI0006.ogg"
    "菲利斯" "「真由喜怎么了喵？　没事吧喵？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0011"
    $ current_voice = "voice/MAY05A_MAY0011.ogg"
    "真由理" "「……不……没什么。头有点疼，抱歉了」"

    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0007"
    $ current_voice = "voice/MAY05A_FEI0007.ogg"
    "菲利斯" "「不要太勉强喵。是因为夏Ｃｏｍｉ累到了喵？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0012"
    $ current_voice = "voice/MAY05A_MAY0012.ogg"
    "真由理" "「嗯……是吧」"



    $ stopvoc("FEI")
    play FEI "MAY05A_FEI0008"
    $ current_voice = "voice/MAY05A_FEI0008.ogg"
    "菲利斯" "「总之，菲利斯也想想看为了红喵自己能做些什么吧喵」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0013"
    $ current_voice = "voice/MAY05A_MAY0013.ogg"
    "真由理" "「谢谢……那么，再见了……」"
    window hide


    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0014"
    $ current_voice = "voice/MAY05A_MAY0014.ogg"
    "真由理" "「……奇怪的真由喜」"
    "挂了电话，呆呆地望向空中。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG16A5")

    hide screen phonebtn
    "联系不上红莉栖酱。"
    window hide


    $ loadBG(0,"BG24N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "在秋叶原里寻找她……在天桥上发现了她。"
    window hide


    $ loadBG(0,"BG62A")

    show screen phonebtn
    show screen phoneSD1
    "果然──哪里有点奇怪。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0015"
    $ current_voice = "voice/MAY05A_MAY0015.ogg"
    "真由理" "「……明明是接下来才要去找红莉栖酱的……为什么感觉真由喜已经找到红莉栖酱了呢？」"
    "这就是所谓的既视感吗？"
    "还是像预知一样的东西？"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0016"
    $ current_voice = "voice/MAY05A_MAY0016.ogg"
    "真由理" "「有点奇怪了……这到底是怎么了呢……」"
    "在不明所以的下个瞬间──"
    window hide



    hide screen phonebtn
    play se "SGSE053L" loop
    "脑袋里闪过了一道白光。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0017"
    $ current_voice = "voice/MAY05A_MAY0017.ogg"
    "真由理" "「呜……啊啊啊啊啊啊啊啊！？」"
    "疼痛暂时收住了，不，比刚才还要疼了。"
    "脑袋里乱糟糟的像是被搅来搅去一样恶心的感觉，同时本来还没有发生的事情犹如洪水一般流入了脑中。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0018"
    $ current_voice = "voice/MAY05A_MAY0018.ogg"
    "真由理" "「……啊、啊、啊啊啊！」"
    "头脑里充满了各种记忆与感情，像是要炸开了一样。"
    "真由喜成为了红莉栖酱和冈伦的重担的理由。"
    "红莉栖酱讲述的痛苦的未来。"
    "为了改变那样的未来而进行了时间跳跃回到了过去。"
    "全部回忆起来了。"
    show screen phonebtn
    play bgm "FD2BGM11"
    stop se

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0019"
    $ current_voice = "voice/MAY05A_MAY0019.ogg"
    "真由理" "「……这就是……时间跳跃……」"
    "头痛终于停下来了，深深地叹了口气。"
    "之前还不知道时间跳跃居然这么的痛苦。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0020"
    $ current_voice = "voice/MAY05A_MAY0020.ogg"
    "真由理" "「冈伦为了真由喜……尝到了那么多次这样的痛苦……」"
    "一想到冈伦有多么的痛苦，就想要哭出来了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0021"
    $ current_voice = "voice/MAY05A_MAY0021.ogg"
    "真由理" "「果然，这种事……绝对要结束它……」"
    "擦干眼泪，抬起了头。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0022"
    $ current_voice = "voice/MAY05A_MAY0022.ogg"
    "真由理" "「已经只有那一种办法了。不过关键的是，不知道它管不管用──」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0023"
    $ current_voice = "voice/MAY05A_MAY0023.ogg"
    "真由理" "「真由喜……必须要做……」"
    "拿起桌子上的日记本和蓝色呜啪，把它们放到了包里，点了点头。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0024"
    $ current_voice = "voice/MAY05A_MAY0024.ogg"
    "真由理" "「必须得求桶子君帮忙」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)







    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0000"
    $ current_voice = "voice/MAY05A_DAR0000.ogg"
    "至" "「喂喂～？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0025"
    $ current_voice = "voice/MAY05A_MAY0025.ogg"
    "真由理" "「喂喂，桶子君。是真由喜哦。现在在干什么？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0001"
    $ current_voice = "voice/MAY05A_DAR0001.ogg"
    "至" "「在Ｌａｂ闲着呢。　我接下来是去Ｎｅｔ　ｃａｆｅ呢，还是去见菲利斯呢，超级地迷茫」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0026"
    $ current_voice = "voice/MAY05A_MAY0026.ogg"
    "真由理" "「两边都去不就好了么？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0002"
    $ current_voice = "voice/MAY05A_DAR0002.ogg"
    "至" "「哦哦，我也正好是这么想的！　好，事不宜迟！　现在就出发，就这么做！」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0027"
    $ current_voice = "voice/MAY05A_MAY0027.ogg"
    "真由理" "「现在！？　今天的桶子君，有点兴奋呢」"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAYATE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAYATE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAYATE"])

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0003"
    $ current_voice = "voice/MAY05A_DAR0003.ogg"
    "至" "「当然了！　其实我在夏Ｃｏｍｉ上，得到了{color=f00}旋风馆家{/color}的同人志，那简直就是神级的质量，简直让人爽翻天了」"
    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0003a"
    $ current_voice = "voice/MAY05A_DAR0003a.ogg"
    "至" "「今晚想久违地在Ｎｅｔ　ｃａｆｅ读完全部的原作啊」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0028"
    $ current_voice = "voice/MAY05A_MAY0028.ogg"
    "真由理" "「那个，就是说，桶子君今晚会一直在秋叶原吗？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0004"
    $ current_voice = "voice/MAY05A_DAR0004.ogg"
    "至" "「当然！」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0029"
    $ current_voice = "voice/MAY05A_MAY0029.ogg"
    "真由理" "「那么，有一个小请求，可以吗？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0005"
    $ current_voice = "voice/MAY05A_DAR0005.ogg"
    "至" "「嗯，是之前真由氏说过的那个吧？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0030"
    $ current_voice = "voice/MAY05A_MAY0030.ogg"
    "真由理" "「嗯，是的。今晚的……那个晚上九点的时候，能不能让Ｄｍａｉｌ处于可以使用的状态？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0006"
    $ current_voice = "voice/MAY05A_DAR0006.ogg"
    "至" "「……Ｄｍａｉｌ？　为什么又提到那个？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0031"
    $ current_voice = "voice/MAY05A_MAY0031.ogg"
    "真由理" "「有个特别想要发的重要的Ｄｍａｉｌ……」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0007"
    $ current_voice = "voice/MAY05A_DAR0007.ogg"
    "至" "「嗯，我记得你说过要对冈伦保密是吧？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0032"
    $ current_voice = "voice/MAY05A_MAY0032.ogg"
    "真由理" "「……嗯，不行……吗？」"
    "自己说出来以后，感觉这真是个奇怪的请求。"
    "被质疑了也不奇怪。"
    "要是被问到具体的细节该怎么办啊。"
    "本来就不擅长说谎，所以没有能够瞒过去的自信。"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0008"
    $ current_voice = "voice/MAY05A_DAR0008.ogg"
    "至" "「──知道了，我给你准备」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0033"
    $ current_voice = "voice/MAY05A_MAY0033.ogg"
    "真由理" "「诶，诶诶！？」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0009"
    $ current_voice = "voice/MAY05A_DAR0009.ogg"
    "至" "「嗯？　为什么那么惊讶？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0034"
    $ current_voice = "voice/MAY05A_MAY0034.ogg"
    "真由理" "「可、可是……那个……还在想桶子君会不会问发短信的理由啊，短信的内容啊什么的。有点小惊讶……」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0010"
    $ current_voice = "voice/MAY05A_DAR0010.ogg"
    "至" "「想让我问的话我也可以问的哦？」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0035"
    $ current_voice = "voice/MAY05A_MAY0035.ogg"
    "真由理" "「……不」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0011"
    $ current_voice = "voice/MAY05A_DAR0011.ogg"
    "至" "「那么，就不问了」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0036"
    $ current_voice = "voice/MAY05A_MAY0036.ogg"
    "真由理" "「……是吗，桶子君……谢谢」"

    $ stopvoc("DAR")
    play DAR "MAY05A_DAR0012"
    $ current_voice = "voice/MAY05A_DAR0012.ogg"
    "至" "「ＯＫ，那么，差十分钟九点的时候给你预备好」"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0037"
    $ current_voice = "voice/MAY05A_MAY0037.ogg"
    "真由理" "「嗯，拜托了。那么……再见了……」"
    "有相信自己的伙伴，真的是很难得。"
    "一边感动着，一边挂断了电话。"
    window hide
    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0038"
    $ current_voice = "voice/MAY05A_MAY0038.ogg"
    "真由理" "「──之后，只需要真由喜进行准备了」"
    "双手拍了拍脸，给自己鼓劲。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG03A4")


    play se "SGSE032L" loop


    hide screen phonebtn
    show screen phoneSD1
    "跟妈妈说完「今天要在Ｌａｂ召开红莉栖酱的送别会，可能会晚点回去，不用担心」之后，便来到了Ｌａｂ。"
    "红莉栖酱的送别会什么的是在说谎。"
    "每当撒谎的时候，就会有一种十分抱歉的心情，所以其实是不想撒谎的……。"
    "但有的时候是不得不撒谎的。"
    "现在就是那种时候，这样安慰着自己，掩盖了抱歉的心情。"
    "是因为Ｌａｂ里一个人都没有的缘故吗，钟表走动的声音，显得格外地响。"
    "真由喜手里的是未来道具１号机比特什么玩意炮。"
    "冈伦起的名字稍微有些复杂，不管听几遍也记不住。"
    "为什么冈伦要故意起这么复杂的名字呢？"
    "虽然感觉很帅也是可以理解的，但是记不住的话会让人很困惑的吧。干脆就叫它小比特吧？"
    "在门口举着小比特，准备埋伏冈伦。"
    play se "SGSE042"


    stop se
    "听到了有些拖拖拉拉的脚步声。"
    "立刻就明白了那是冈伦的脚步声。"
    "心跳得非常厉害，握着小比特的手渗出了汗。"
    play se "SGSE024"
    "在门开的同时，把小比特指向了冈伦，说出了已练习多次的台词。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY004A"]]["Check"]=True


    $ loadBG(2,"EV_MAY004A")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0039"
    $ current_voice = "voice/MAY05A_MAY0039.ogg"
    "真由理" "「……冈伦，举、举、举、举起手来！」"
    "尽可能说得比较像样，但是因为紧张的缘故，口吃得很厉害。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0000"
    $ current_voice = "voice/MAY05A_OKA0000.ogg"
    "伦太郎" "「……真由理？」"
    "冈伦吊起了半边的眉毛，用好像在说「你在干什么呢？」的眼神望着真由喜。"
    "非常的害羞，想要退缩，但是真由喜绝不能因为这点小事就退缩。"
    "重新拿好小比特，瞪着冈伦，再次说出了那句话。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0040"
    $ current_voice = "voice/MAY05A_MAY0040.ogg"
    "真由理" "「冈伦，把手举起来！」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0001"
    $ current_voice = "voice/MAY05A_OKA0001.ogg"
    "伦太郎" "「……手？　干什么？」"
    "冈伦看着自己的手心，慢悠悠地歪了歪脑袋。"
    "完全感觉不到紧张感。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0041"
    $ current_voice = "voice/MAY05A_MAY0041.ogg"
    "真由理" "「别问那么多，冈伦，举起手来。就像喊万岁那样，来，万岁！」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0002"
    $ current_voice = "voice/MAY05A_OKA0002.ogg"
    "伦太郎" "「这样吗？　万岁……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY004B"]]["Check"]=True


    $ loadBG(2,"EV_MAY004B")



    "冈伦极不情愿地举起了双手。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0042"
    $ current_voice = "voice/MAY05A_MAY0042.ogg"
    "真由理" "「…………」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0003"
    $ current_voice = "voice/MAY05A_OKA0003.ogg"
    "伦太郎" "「…………」"
    "一段时间里，互相看着对方的眼睛，一动也不动。"
    "依然感觉不到一丝的紧张感。"
    play bgm "BGM06"
    "本应是更加紧张的场面啊，好奇怪呢。"
    "哪里出问题了呢。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0043"
    $ current_voice = "voice/MAY05A_MAY0043.ogg"
    "真由理" "「不对，感觉跟万岁有点不同……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0004"
    $ current_voice = "voice/MAY05A_OKA0004.ogg"
    "伦太郎" "「……哎呀，这种事你到现在才意识过来啊。那么，万岁之后呢，要做什么才好？　不过我现在没有玩的时间」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0044"
    $ current_voice = "voice/MAY05A_MAY0044.ogg"
    "真由理" "「抱歉，冈伦，现在你要做真由喜的人质」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY004C"]]["Check"]=True


    $ loadBG(2,"EV_MAY004C")



    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0005"
    $ current_voice = "voice/MAY05A_OKA0005.ogg"
    "伦太郎" "「什么……我要做你的人质？　人质的人质……这是什么啊！？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0045"
    $ current_voice = "voice/MAY05A_MAY0045.ogg"
    "真由理" "「真由喜不甘心一直做冈伦的人质！」"
    "就像往常的冈伦那样，使用了故弄玄虚的说话方式。"
    "要是使用像开玩笑一样的说话方式，平常说不出来的话也能很自然地说出来了。"
    "这件事吹雪酱也说过来着吧。"
    "穿上ＣＯＳ服装，就能变成跟往常不一样的自己。"
    "平常办不到的事也能不可思议地办到了。"
    "这个跟那个或许是一样的。"
    "冈伦也肯定是一样的吧。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0006"
    $ current_voice = "voice/MAY05A_OKA0006.ogg"
    "伦太郎" "「……真由理？　怎么了？　这可不像你啊？　为什么突然之间做这种事？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0046"
    $ current_voice = "voice/MAY05A_MAY0046.ogg"
    "真由理" "「那个，并不是突然之间，我已经想了很久了……」"
    "但是一直在犹豫。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0047"
    $ current_voice = "voice/MAY05A_MAY0047.ogg"
    "真由理" "「总之，稍微一会就可以了，什么都不要问，做真由喜的人质，拜托了，冈伦」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0007"
    $ current_voice = "voice/MAY05A_OKA0007.ogg"
    "伦太郎" "「…………」"
    "冈伦边揉着下巴，边用质疑的眼光瞅着真由喜。"
    "但突然之间表情缓和了下来，有些寂寞地笑着说道。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0008"
    $ current_voice = "voice/MAY05A_OKA0008.ogg"
    "伦太郎" "「真由理啊，要是不说得再狂妄一点可没有那种样子哦？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0048"
    $ current_voice = "voice/MAY05A_MAY0048.ogg"
    "真由理" "「嗯、嗯……确实，是这样的呢」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0049"
    $ current_voice = "voice/MAY05A_MAY0049.ogg"
    "真由理" "「那么，试着再说一次……」"
    "深呼吸，肚子用力，尽可能装模作样地试着说了出来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0050"
    $ current_voice = "voice/MAY05A_MAY0050.ogg"
    "真由理" "「冈伦！　做真由喜的人质！」"
    "……还是感觉有些不太对。"
    "但是冈伦却肯配合这样的真由喜。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0009"
    $ current_voice = "voice/MAY05A_OKA0009.ogg"
    "伦太郎" "「哼……人质的反抗么。真是个无法无天的挑战啊……知道了，我……不，凤凰院凶真，接受挑战」"
    "因为有些痛苦而抽搐的笑脸。"
    "大概是在勉强自己而配合真由喜吧。"
    "但是，要是不这么做的话……那就太痛苦了。"

    stop bgm 
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0051"
    $ current_voice = "voice/MAY05A_MAY0051.ogg"
    "真由理" "「……冈伦，谢谢。抱歉了」"
    "低下了头，冈伦像是放弃了一样叹了口气，抚摸着真由喜的头。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0010"
    $ current_voice = "voice/MAY05A_OKA0010.ogg"
    "伦太郎" "「真是的……哪个坏蛋会对人质说谢谢的？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0052"
    $ current_voice = "voice/MAY05A_MAY0052.ogg"
    "真由理" "「……真由喜……可不是坏蛋哦？」"
    "真由喜怯怯地向冈伦抗议。"
    window hide
    play se "SGSE031"

    "不过在这时，肚子叫了。"
    window hide



    $ loadBG(2,"BG01E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA05"),"True","lh/OKA_ALA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0053"
    $ current_voice = "voice/MAY05A_MAY0053.ogg"
    "真由理" "「呜呜呜……为什么在这种时候……」"
    "时机太不巧妙，脸红得好像要冒火了一样。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0011"
    $ current_voice = "voice/MAY05A_OKA0011.ogg"
    "伦太郎" "「哎呀哎呀……真是个笨拙的反抗者啊……」"
    "冈伦再一次摸了摸真由喜的头。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0054"
    $ current_voice = "voice/MAY05A_MAY0054.ogg"
    "真由理" "「呜呜……」"
    "从以前开始就很喜欢被冈伦摸头。"
    "但是，现在必须要结束了──"
    "只是稍微想想，鼻子里就感觉到一阵酸痛。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0055"
    $ current_voice = "voice/MAY05A_MAY0055.ogg"
    "真由理" "「因为……没有办法啊。真由喜……一直在做冈伦的人质。反抗什么的……这种事还不习惯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA02"),"True","lh/OKA_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0012"
    $ current_voice = "voice/MAY05A_OKA0012.ogg"
    "伦太郎" "「怎么了？　肚子已经饿到让你哭鼻子了吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0056"
    $ current_voice = "voice/MAY05A_MAY0056.ogg"
    "真由理" "「不、不是的……」"
    "是觉得犯难了呢还是觉得吃惊了呢，即使这样还保持着温柔的微笑的冈伦，没有办法去直视他。"
    "拼命地望着天花板，为了不让眼泪流下来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA05"),"True","lh/OKA_ALA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0013"
    $ current_voice = "voice/MAY05A_OKA0013.ogg"
    "伦太郎" "「──但是，真是巧啊。我也还没吃晚饭呢」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0057"
    $ current_voice = "voice/MAY05A_MAY0057.ogg"
    "真由理" "「诶？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0014"
    $ current_voice = "voice/MAY05A_OKA0014.ogg"
    "伦太郎" "「久违地一起去吃个饭吧？」"
    "冈伦依然很温柔。"
    "是照顾到了举止可疑的真由喜吧。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0058"
    $ current_voice = "voice/MAY05A_MAY0058.ogg"
    "真由理" "「……嗯」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0015"
    $ current_voice = "voice/MAY05A_OKA0015.ogg"
    "伦太郎" "「──那么，命令一下怎么样？　像个反抗者一样」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0059"
    $ current_voice = "voice/MAY05A_MAY0059.ogg"
    "真由理" "「嗯……嗯……知道了」"
    "点了下头，整理整理心情，命令冈伦道。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0060"
    $ current_voice = "voice/MAY05A_MAY0060.ogg"
    "真由理" "「那么……冈伦，带真由喜到厨房次郎去」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0016"
    $ current_voice = "voice/MAY05A_OKA0016.ogg"
    "伦太郎" "「好好，那么我们出发吧」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0061"
    $ current_voice = "voice/MAY05A_MAY0061.ogg"
    "真由理" "「嗯」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    show screen phonebtn
    "冈伦把手插在了白大褂的兜里，走到了门外去。"
    "慌忙地跟在了他的背后。"
    "虽然跟计划有些偏差，不过还有时间。"
    "稍微干点别的事……也没问题吧？"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG63A")
    python:
        SndMail(67)
        RcvMail(68)
        ReadMail(68)


    play bgm "FD2BGM09"
    show screen phoneSD1
    "厨房次郎正处于晚饭的饭点，里面人很多。"
    "排队等了一段时间，之后终于有座位了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "在落座的同时，看都不看菜谱就点了菜。"
    "真由喜点了炸肉饼盖饭。"
    "冈伦点了咖喱饭并加了两张炸肉饼，冈伦把它起名为疯狂肉饼咖喱饭。"
    "与往常没有变化的最爱菜谱，不知怎的让人十分开心。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0017"
    $ current_voice = "voice/MAY05A_OKA0017.ogg"
    "伦太郎" "「真由理，你笑得很开心啊……怎么了？　今天你好像很奇怪啊？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0062"
    $ current_voice = "voice/MAY05A_MAY0062.ogg"
    "真由理" "「嗯～，感觉像这样，跟冈伦一起等餐，好幸福啊。深刻地感觉到了这一点～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA02"),"True","lh/OKA_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0018"
    $ current_voice = "voice/MAY05A_OKA0018.ogg"
    "伦太郎" "「付一千块都还有找零的幸福么，真由理还真喜欢简单的东西呢」"


    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0063"
    $ current_voice = "voice/MAY05A_MAY0063.ogg"
    "真由理" "「诶嘿嘿～。多汁炸鸡Ｎｏ．１啦，香蕉啦，炸鸡炸鸡君啦，就已经足够幸福了～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0019"
    $ current_voice = "voice/MAY05A_OKA0019.ogg"
    "伦太郎" "「……越来越廉价了啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0064"
    $ current_voice = "voice/MAY05A_MAY0064.ogg"
    "真由理" "「嗯♪」"
    "在来到厨房次郎以前，冈伦和真由喜之间还很尴尬──"
    "在往常的店里，往常的菜单，跟往常一样没有任何变化的对话，已经十分熟悉了。"
    "像这样处身于往常的日常中，感觉坏事全都是梦一般，不管是明天还是后天，这样没有变化的日子会一直持续下去。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0065"
    $ current_voice = "voice/MAY05A_MAY0065.ogg"
    "真由理" "「……要是这样就好了啊～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0020"
    $ current_voice = "voice/MAY05A_OKA0020.ogg"
    "伦太郎" "「什么？　你在说啥？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0066"
    $ current_voice = "voice/MAY05A_MAY0066.ogg"
    "真由理" "「不，没什么～」"
    "稍微等了一会，装着菜盘子的托盘被送了过来。"
    "真由喜的托盘上放着比真由喜的手掌还要大的炸肉饼，还撒着好多的色拉。"
    "还带有米饭和猪肉汁，量也很足。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0067"
    $ current_voice = "voice/MAY05A_MAY0067.ogg"
    "真由理" "「呜哇～，看起来好好吃的样子～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA02"),"True","lh/OKA_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0021"
    $ current_voice = "voice/MAY05A_OKA0021.ogg"
    "伦太郎" "「那当然好吃了吧？」"
    "冈伦就好像是自己做的一样得意地说着。"
    "感觉平时的冈伦又回来了，真由喜高兴了起来。"
    "果然，冈伦就是得这样。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0068"
    $ current_voice = "voice/MAY05A_MAY0068.ogg"
    "真由理" "「我开动了！」"
    "双手合十之后，首先对那个跟往常一样特大的炸肉饼动嘴。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0069"
    $ current_voice = "voice/MAY05A_MAY0069.ogg"
    "真由理" "「啊呜呜……好烫！」"
    "从炸得酥脆的肉饼中，蹦出了大量的肉汁。"
    "嘴里充满了肉的香味与圆葱的甜味。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0070"
    $ current_voice = "voice/MAY05A_MAY0070.ogg"
    "真由理" "「嗯嗯～，好好吃～！」"
    "吃好吃的东西的时候就会露出笑脸。"
    "这个笑脸，也会让人充满精神的吧。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0071"
    $ current_voice = "voice/MAY05A_MAY0071.ogg"
    "真由理" "「厨房次郎的炸肉饼真是太神了。在真由喜心中，肉王的宝座非他莫属～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0022"
    $ current_voice = "voice/MAY05A_OKA0022.ogg"
    "伦太郎" "「嗯，真由理啊，我毫无保留地同意你的意见啊，这是世界的真理」"
    "冈伦像往常一样向炸肉饼上滴了三滴的酱油，发出了一阵邪笑。"
    window hide


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA05"),"True","lh/OKA_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0023"
    $ current_voice = "voice/MAY05A_OKA0023.ogg"
    "伦太郎" "「接招吧！　美食破坏！」"
    window hide
    $ loadBG(0,"IBG056A",png=True)

    "下一个瞬间，冈伦的勺子噗哧地扎在猪肉饼上，跟咖喱搅和在了一起。"



    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0072"
    $ current_voice = "voice/MAY05A_MAY0072.ogg"
    "真由理" "「啊啊～，冈伦，又弄得乱糟糟的了，好浪费啊～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0024"
    $ current_voice = "voice/MAY05A_OKA0024.ogg"
    "伦太郎" "「这才是疯狂肉饼咖喱的疯狂所在。身为疯狂科学家，必须得用这种吃法来吃。跟凡人不同。跟凡人──呜哈哈哈哈哈哈！」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0073"
    $ current_voice = "voice/MAY05A_MAY0073.ogg"
    "真由理" "「只感觉这是对炸肉饼的亵渎啊～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0025"
    $ current_voice = "voice/MAY05A_OKA0025.ogg"
    "伦太郎" "「说什么呢。这才是至高的使用方法。真由理，你有一天也会明白的。在那之前你就满足于那无可厚非的俗套菜谱吧」"


    window hide
    hide background-png  with dissolve
    "说完，冈伦张开大嘴，吃下了炸肉饼咖喱混合米饭。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0026"
    $ current_voice = "voice/MAY05A_OKA0026.ogg"
    "伦太郎" "「……嗯，果然很好吃！」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0074"
    $ current_voice = "voice/MAY05A_MAY0074.ogg"
    "真由理" "「冈伦从以前起就是这样混着吃咖喱的人呢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0027"
    $ current_voice = "voice/MAY05A_OKA0027.ogg"
    "伦太郎" "「因为从小时候起就很Ｍａｄ」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0075"
    $ current_voice = "voice/MAY05A_MAY0075.ogg"
    "真由理" "「诶─，是这样的吗？」"
    "真由喜记得冈伦成为疯狂科学家的瞬间。"
    hide screen phoneSD1
    window hide

    stop bgm 


    $ loadBG(0,"EVX_M06A")

    hide screen phonebtn
    "那是下着小雨的某一天。"
    "在奶奶死后，心里像是被掏空一样的真由喜成为了冈伦的人质。"
    "那样下去的话，真由喜似乎就要走远了。"
    "因为是人质，所以哪儿都不能去──"
    window hide


    $ loadBG(0,"BG63A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMB05"),"True","lh/OKA_AMB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    show screen phoneSD1





    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0028"
    $ current_voice = "voice/MAY05A_OKA0028.ogg"
    "伦太郎" "「──真由理，你在发什么呆！　有破绽！」"


    play bgm "BGM22"
    "嘴被炸肉饼填满的冈伦，突然之间把勺子插在了真由喜的炸肉饼上。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0076"
    $ current_voice = "voice/MAY05A_MAY0076.ogg"
    "真由理" "「啊！　那是真由喜的……」"
    "炸肉饼被抢走了一口的份。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA02"),"True","lh/OKA_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0029"
    $ current_voice = "voice/MAY05A_OKA0029.ogg"
    "伦太郎" "「哼，粗心要人命啊。居然让人质抓到了破绽──」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0077"
    $ current_voice = "voice/MAY05A_MAY0077.ogg"
    "真由理" "「冈伦总是这样。冈伦这个肉饼贼～。都已经点了两份了，为什么还要抢真由喜的呢～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0030"
    $ current_voice = "voice/MAY05A_OKA0030.ogg"
    "伦太郎" "「虽然沾满了咖喱的炸肉饼很不错，但是我也想尝尝炸肉饼本身质朴的味道是吧？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0078"
    $ current_voice = "voice/MAY05A_MAY0078.ogg"
    "真由理" "「呜～，那么，真由喜也要拿走冈伦的一口哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0031"
    $ current_voice = "voice/MAY05A_OKA0031.ogg"
    "伦太郎" "「刚才还在嫌弃别人的吃法现在又想吃了吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0079"
    $ current_voice = "voice/MAY05A_MAY0079.ogg"
    "真由理" "「嗯，虽然看起来不怎么样，说不定还挺好吃的呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA05"),"True","lh/OKA_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0032"
    $ current_voice = "voice/MAY05A_OKA0032.ogg"
    "伦太郎" "「当然好吃啦，既然说到这份上你就吃吃看吧！」"
    "冈伦用勺子盛了一勺的疯狂炸肉饼咖喱，递到了真由喜嘴边。"
    "好像恋人之间做的事，不由得害羞了起来。"
    "在ＭａｙＱｕｅｅｎ＋Ｎｙａ²里，真由喜给主人们做这种事的时候，明明什么都不想的。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0080"
    $ current_voice = "voice/MAY05A_MAY0080.ogg"
    "真由理" "「嗯、怎么……好好吃」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0033"
    $ current_voice = "voice/MAY05A_OKA0033.ogg"
    "伦太郎" "「所以跟你说过好多次好吃了吧，不要被外观的惊悚所迷惑──」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0081"
    $ current_voice = "voice/MAY05A_MAY0081.ogg"
    "真由理" "「本来以为混合了咖喱的炸肉饼就没有脆生生的感觉了，不过并不是这样呢，依然很脆，还很好吃」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0034"
    $ current_voice = "voice/MAY05A_OKA0034.ogg"
    "伦太郎" "「嗯，能够一口气摄取全部喜欢的东西，效率上也不错。说成是呕心沥血策划的究极平衡食品也不为过。知道这是很适合疯狂科学家的晚餐了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "果然又在装模作样地说话，之后冈伦一声不吭地动起勺子，开始吃咖喱。"
    "虽然一点也不浪漫，但对于这个超出预想的间接接吻，心里变得热乎了起来。"
    "过去，小孩子的时候，跟冈伦开玩笑地亲过嘴吧。"
    "清楚地想起了那时的感觉。"
    "为什么到现在都没忘呢。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0082"
    $ current_voice = "voice/MAY05A_MAY0082.ogg"
    "真由理" "「觉得有点那个呢。过去的事，没想到还没有忘记呢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0035"
    $ current_voice = "voice/MAY05A_OKA0035.ogg"
    "伦太郎" "「嗯？　突然之间在说什么？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0083"
    $ current_voice = "voice/MAY05A_MAY0083.ogg"
    "真由理" "「那个，平常以为已经忘了呢，不过现在令人惊讶地居然想起来了，稍微有些安心了呢～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0036"
    $ current_voice = "voice/MAY05A_OKA0036.ogg"
    "伦太郎" "「你到底想起什么了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0084"
    $ current_voice = "voice/MAY05A_MAY0084.ogg"
    "真由理" "「嘿嘿～，秘密～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0037"
    $ current_voice = "voice/MAY05A_OKA0037.ogg"
    "伦太郎" "「什么啊，别卖关子了」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0085"
    $ current_voice = "voice/MAY05A_MAY0085.ogg"
    "真由理" "「……冈伦也还记得吗？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0038"
    $ current_voice = "voice/MAY05A_OKA0038.ogg"
    "伦太郎" "「所以说是啥啊？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0086"
    $ current_voice = "voice/MAY05A_MAY0086.ogg"
    "真由理" "「……是吧，小的时候，开玩笑亲嘴的事，还记得吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0039"
    $ current_voice = "voice/MAY05A_OKA0039.ogg"
    "伦太郎" "「嗯！？　咳咳咳咳咳咳！」"


    "冈伦呛得很厉害。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0087"
    $ current_voice = "voice/MAY05A_MAY0087.ogg"
    "真由理" "「抱歉，冈伦。没、没事吧？」"
    "拍着他的后背，给他递去了纸巾和水。"
    "冈伦用纸巾擤了擤鼻子，一口气喝干了水。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA03"),"True","lh/OKA_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0040"
    $ current_voice = "voice/MAY05A_OKA0040.ogg"
    "伦太郎" "「我还以为你突然之间要说什么呢……那么久远的事我早忘了！」"
    "对着依然不擅长撒谎的冈伦不由得笑了起来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0088"
    $ current_voice = "voice/MAY05A_MAY0088.ogg"
    "真由理" "「是吗，已经忘了啊～？　真遗憾啊～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0041"
    $ current_voice = "voice/MAY05A_OKA0041.ogg"
    "伦太郎" "「……不想再被抢走炸肉饼的话，就赶紧安静地吃饭」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0089"
    $ current_voice = "voice/MAY05A_MAY0089.ogg"
    "真由理" "「是──」"
    "听冈伦这么一说，赶紧把炸肉饼塞在了嘴里。"
    "斜眼看到了冈伦板着脸一声不吭地吃着咖喱的样子，不由得祈祷了起来。"
    "希望这种平淡无奇的幸福的时光能够持续下去──"
    "重复时间跳跃的话，或许能够永远重复这种幸福的时光。"
    "强大的诱惑动摇了自己的内心。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0042"
    $ current_voice = "voice/MAY05A_OKA0042.ogg"
    "伦太郎" "「喂、真由理，手停下来了哦？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0090"
    $ current_voice = "voice/MAY05A_MAY0090.ogg"
    "真由理" "「啊……抱歉抱歉」"

    stop bgm 
    "但这样还是不行的。"
    "即使永远重复同一段时间，那也只是逃避，红莉栖也这样说过。"
    "真由喜也是这么想的。"
    "不管有多痛苦，也必须要向前进。"
    "虽然对于变化感到害怕……但必须要改变。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0043"
    $ current_voice = "voice/MAY05A_OKA0043.ogg"
    "伦太郎" "「对了，真由理，我要当人质当到什么时候啊？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0091"
    $ current_voice = "voice/MAY05A_MAY0091.ogg"
    "真由理" "「嗯～，直到今天结束吧？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0044"
    $ current_voice = "voice/MAY05A_OKA0044.ogg"
    "伦太郎" "「有没有想让我陪你去的地方？　Ｎｅｔ　ｃａｆｅ什么的？　还是在卡拉ＯＫ唱动漫歌曲唱到爽为止之类的？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0092"
    $ current_voice = "voice/MAY05A_MAY0092.ogg"
    "真由理" "「不，今天没有那个心情吧～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0045"
    $ current_voice = "voice/MAY05A_OKA0045.ogg"
    "伦太郎" "「那么，为什么要我做人质啊？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0093"
    $ current_voice = "voice/MAY05A_MAY0093.ogg"
    "真由理" "「这是……那个……」"
    play bgm "FD2BGM05"
    "突然被冈伦以认真地表情追问，不知道该说什么好了。"
    "不过，在匆忙之间试着故意用冈伦装模作样的说话方式说道。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0094"
    $ current_voice = "voice/MAY05A_MAY0094.ogg"
    "真由理" "「呼哈哈哈哈。为了让你协助真由喜的阴谋！」"
    "会不会让他觉得奇怪呢？"
    "真由喜看向冈伦，冈伦竖起了食指，摇了摇头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA05"),"True","lh/OKA_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0046"
    $ current_voice = "voice/MAY05A_OKA0046.ogg"
    "伦太郎" "「……呼呼呼，真是的，连笑都不会笑啊。这么不可靠的恶人之笑，我连听都没听过！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMB01"),"True","lh/OKA_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0047"
    $ current_voice = "voice/MAY05A_OKA0047.ogg"
    "伦太郎" "「真由理啊，真正的恶人是像这样子笑啊！　呜哈哈哈哈！」"


    "其他的客人被突然笑起来的冈伦吓了一跳。"
    "但是冈伦却不在乎周围的人，继续地笑着。"
    "看上去跟往常一样没有变化的冈伦。"
    "但是，这是故作精神，能看出来他是在勉强自己。"
    "冈伦总是戴着疯狂科学家的面具来隐藏自己的真心话。"
    "对不起冈伦。"
    "但是，再稍微……忍耐一会。"

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG40N")

    show screen phoneSD1
    "在厨房次郎吃饱之后，像往常那样，稍微到秋叶原闲逛散步。"
    window hide



    $ loadBG(0,"BG31N")


    play se "SGSE091L" loop


    "接下来乘坐山手线的电车。"
    "目的地是池袋──"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA02"),"True","lh/OKA_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0095"
    $ current_voice = "voice/MAY05A_MAY0095.ogg"
    "真由理" "「哈～真好吃啊。久违的炸肉饼盖饭真是绝品啊～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0048"
    $ current_voice = "voice/MAY05A_OKA0048.ogg"
    "伦太郎" "「嗯，真挺好吃的」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0096"
    $ current_voice = "voice/MAY05A_MAY0096.ogg"
    "真由理" "「吃了好吃的东西，就感觉有精神了呢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0049"
    $ current_voice = "voice/MAY05A_OKA0049.ogg"
    "伦太郎" "「是啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0097"
    $ current_voice = "voice/MAY05A_MAY0097.ogg"
    "真由理" "「不过，冈伦，让你请客真的好吗？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0050"
    $ current_voice = "voice/MAY05A_OKA0050.ogg"
    "伦太郎" "「偶尔吧，而且现在我是真由理的人质，真由理不也经常送香蕉给Ｌａｂ吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0098"
    $ current_voice = "voice/MAY05A_MAY0098.ogg"
    "真由理" "「也并不是送啊，是真由喜想吃所以才买的而已，然而却被冈伦拿去做实验了」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0051"
    $ current_voice = "voice/MAY05A_OKA0051.ogg"
    "伦太郎" "「区区香蕉，不要那么抠门」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0099"
    $ current_voice = "voice/MAY05A_MAY0099.ogg"
    "真由理" "「……可是，凝胶香蕉什么的，软绵绵的不好吃。这是对香蕉的亵渎啊～？　要是不珍惜食物，香蕉会不高兴的哦～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0052"
    $ current_voice = "voice/MAY05A_OKA0052.ogg"
    "伦太郎" "「牺牲在实验中是必须的。因为它的牺牲，诞生了伟大的发明品，反而应该感觉到骄傲」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0100"
    $ current_voice = "voice/MAY05A_MAY0100.ogg"
    "真由理" "「真由喜认为香蕉应该津津有味地吃掉更好啊─」"
    "本来是想一直聊一些像往常一样毫无内涵的东西的。"
    "但是，真由喜的话让冈伦脸上蒙上了一层雾。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0053"
    $ current_voice = "voice/MAY05A_OKA0053.ogg"
    "伦太郎" "「嘛──或许是这样的……」"
    "之前像开玩笑一样的气氛，突然一转，变得严肃了起来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0101"
    $ current_voice = "voice/MAY05A_MAY0101.ogg"
    "真由理" "「冈伦？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0054"
    $ current_voice = "voice/MAY05A_OKA0054.ogg"
    "伦太郎" "「过度的好奇心会引来杀身之祸这种说法也是有的」"
    "冈伦带有讽刺意味地笑了笑，然后痛苦地望向了真由喜。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0055"
    $ current_voice = "voice/MAY05A_OKA0055.ogg"
    "伦太郎" "「既然要杀身的话，杀死本人就好了，这是自作自受也是能够接受的。但是把没有罪的人卷进来还杀死了他，这是错的」"
    "钻牛角尖的眼神。"
    "在红莉栖酱告诉真由喜之前，真由喜还不知道冈伦为什么用这种眼神看着真由喜。"
    "但是，现在能明白了。"
    "冈伦在责备自己。"
    "因为自己改变了世界线，真由喜将要死亡。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0102"
    $ current_voice = "voice/MAY05A_MAY0102.ogg"
    "真由理" "「但是，冈伦。真由喜非常喜欢看着沉醉于开发电话微波炉的冈伦哦～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0056"
    $ current_voice = "voice/MAY05A_OKA0056.ogg"
    "伦太郎" "「……是吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0103"
    $ current_voice = "voice/MAY05A_MAY0103.ogg"
    "真由理" "「嗯，冈伦，专注到了废寝忘食的地步了吧？　真由喜只是看着就能感受到那种激动人心的情感」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0104"
    $ current_voice = "voice/MAY05A_MAY0104.ogg"
    "真由理" "「真由喜复杂的事虽然不懂，但是在沉浸与开发中的冈伦身边，一边做着ＣＯＳ服装，一边就能感受到跟冈伦在一起进行着大发明的感觉」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0105"
    $ current_voice = "voice/MAY05A_MAY0105.ogg"
    "真由理" "「冈伦那超越了度的好奇心，真由喜觉得那是宝物哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0057"
    $ current_voice = "voice/MAY05A_OKA0057.ogg"
    "伦太郎" "「真由理……」"

    stop se
    "冈伦那痛苦的表情稍微缓和了。"
    "正好在那个时候。"
    window hide
    play se "SGSE007L" loop

    "电车到达了上野站，在开门的同时，大批的人涌入了电车之中。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0106"
    $ current_voice = "voice/MAY05A_MAY0106.ogg"
    "真由理" "「啊！？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    "被一个大背包挤着后背，真由喜跌入了在前面的冈伦的怀里。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0058"
    $ current_voice = "voice/MAY05A_OKA0058.ogg"
    "伦太郎" "「真由理，没事吧？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0107"
    $ current_voice = "voice/MAY05A_MAY0107.ogg"
    "真由理" "「嗯……没事……呜……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0059"
    $ current_voice = "voice/MAY05A_OKA0059.ogg"
    "伦太郎" "「好像不是没事啊……长得小在这种时候就会很麻烦啊，能呼吸吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0108"
    $ current_voice = "voice/MAY05A_MAY0108.ogg"
    "真由理" "「呜呜……还、还行……」"
    "直接贴在了冈伦胸口那里，难以呼吸。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0060"
    $ current_voice = "voice/MAY05A_OKA0060.ogg"
    "伦太郎" "「稍微忍一会」"

    stop se
    "冈伦自然地保护着真由喜远离周围的人。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0109"
    $ current_voice = "voice/MAY05A_MAY0109.ogg"
    "真由理" "「嗯、嗯……」"
    "好像在被抱着一样。"
    "跟冈伦身体贴在一起，脸变得烫起来了。"

    play se "SGSE091L" loop
    "过了一会，电车缓缓地发动了。"
    "每当电车摇晃的时候，脸就会贴到冈伦的胸口。"
    "冈伦的味道，既让人舒心，也让人心跳加速。"
    "这样紧贴着的状态，想到自己的心在跳说不定冈伦也能感觉得到，稍微有些焦虑起来了。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0061"
    $ current_voice = "voice/MAY05A_OKA0061.ogg"
    "伦太郎" "「真由理，要是有奇怪的人的话，要说出来哦？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0110"
    $ current_voice = "voice/MAY05A_MAY0110.ogg"
    "真由理" "「奇、奇怪的人？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0062"
    $ current_voice = "voice/MAY05A_OKA0062.ogg"
    "伦太郎" "「嗯，因为真由理很天然，非常容易成为痴汉的目标」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0111"
    $ current_voice = "voice/MAY05A_MAY0111.ogg"
    "真由理" "「哎呀，真由喜虽然看起来很天然……但实际上一点也不天然哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA02"),"True","lh/OKA_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0063"
    $ current_voice = "voice/MAY05A_OKA0063.ogg"
    "伦太郎" "「是吗，到底是不是这样呢？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0112"
    $ current_voice = "voice/MAY05A_MAY0112.ogg"
    "真由理" "「……真是的，冈伦真是坏心眼」"
    "嘟起了脸蛋，把头靠在了冈伦的胸口。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0064"
    $ current_voice = "voice/MAY05A_OKA0064.ogg"
    "伦太郎" "「嗯，怎么了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0113"
    $ current_voice = "voice/MAY05A_MAY0113.ogg"
    "真由理" "「……没什么」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0065"
    $ current_voice = "voice/MAY05A_OKA0065.ogg"
    "伦太郎" "「这样啊……我还以为你是吃饱了就困了呢」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0114"
    $ current_voice = "voice/MAY05A_MAY0114.ogg"
    "真由理" "「唉呀，不是的」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0066"
    $ current_voice = "voice/MAY05A_OKA0066.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0115"
    $ current_voice = "voice/MAY05A_MAY0115.ogg"
    "真由理" "「…………」"
    "明明非常的平静，心脏却跳得快要蹦出来了一样。"
    "想要对这满员电车说声谢谢。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0116"
    $ current_voice = "voice/MAY05A_MAY0116.ogg"
    "真由理" "「……冈伦，谢谢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0067"
    $ current_voice = "voice/MAY05A_OKA0067.ogg"
    "伦太郎" "「嗯？　怎么了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0117"
    $ current_voice = "voice/MAY05A_MAY0117.ogg"
    "真由理" "「嗯～，有很多事，不知不觉地就说了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA02"),"True","lh/OKA_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0068"
    $ current_voice = "voice/MAY05A_OKA0068.ogg"
    "伦太郎" "「奇怪的家伙」"
    "虽然话中带刺，但冈伦还是温柔地抚摸着真由喜的头。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0118"
    $ current_voice = "voice/MAY05A_MAY0118.ogg"
    "真由理" "「……嘿嘿」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0069"
    $ current_voice = "voice/MAY05A_OKA0069.ogg"
    "伦太郎" "「怎么了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0119"
    $ current_voice = "voice/MAY05A_MAY0119.ogg"
    "真由理" "「不，没什么」"
    "摸真由喜的头，对冈伦来说，或许只是个习惯，或许没有什么特别的含义。"
    "但是对真由喜来说依然是特别的……"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0120"
    $ current_voice = "voice/MAY05A_MAY0120.ogg"
    "真由理" "「……不想忘记哦，冈伦」"
    "紧紧地握着冈伦的白大褂。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0070"
    $ current_voice = "voice/MAY05A_OKA0070.ogg"
    "伦太郎" "「…………」"
    "不知道是听到了还是没听到──冈伦依然沉默着，紧紧地抱着真由喜的身体。"
    "仅此而已，我的不安便魔术般地消失了。"
    "距离池袋还有十多分钟。"
    "时间限制正在一点一点地接近。"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG64N")

    play bgm "FD2BGM04"
    show screen phoneSD1
    "到达池袋以后，前往奶奶的墓地。"
    "想了很多地方以后，还是只能想到这里。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0071"
    $ current_voice = "voice/MAY05A_OKA0071.ogg"
    "伦太郎" "「前几天不是才刚扫过墓吗？　难道是想来练胆的吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0121"
    $ current_voice = "voice/MAY05A_MAY0121.ogg"
    "真由理" "「不，不是来练胆的。因为真由喜并不怕幽灵」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0072"
    $ current_voice = "voice/MAY05A_OKA0072.ogg"
    "伦太郎" "「人不可貌相。还挺勇敢的呢，真由理」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0122"
    $ current_voice = "voice/MAY05A_MAY0122.ogg"
    "真由理" "「诶嘿嘿，坏心眼的幽灵有点害怕，如果是奶奶的幽灵，反而热烈欢迎呢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0073"
    $ current_voice = "voice/MAY05A_OKA0073.ogg"
    "伦太郎" "「是么。嘛，说的也是啊──」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0123"
    $ current_voice = "voice/MAY05A_MAY0123.ogg"
    "真由理" "「这里对真由喜来说是个特别的地方，偶尔也会像这样来这里散步。很安静，能够清楚地看见星星。能让人平静下来」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SANCTUARY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SANCTUARY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SANCTUARY"])
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0074"
    $ current_voice = "voice/MAY05A_OKA0074.ogg"
    "伦太郎" "「原来如此。可以说这里是真由理的{color=#f00}圣域{/color}吧」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0124"
    $ current_voice = "voice/MAY05A_MAY0124.ogg"
    "真由理" "「嗯～三……嗯、嘛，差不多是这样吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0075"
    $ current_voice = "voice/MAY05A_OKA0075.ogg"
    "伦太郎" "「不要随便地应和。你其实并没有听懂吧？　苏子是卷肉的蔬菜」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0125"
    $ current_voice = "voice/MAY05A_MAY0125.ogg"
    "真由理" "「嘿嘿，暴露了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0076"
    $ current_voice = "voice/MAY05A_OKA0076.ogg"
    "伦太郎" "「嘛，算了，常有的事。那么，人质应该做什么？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0126"
    $ current_voice = "voice/MAY05A_MAY0126.ogg"
    "真由理" "「这里，是真由喜的专座，冈伦也坐这儿」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "坐在奶奶坟墓旁边圆圆的石头上，然后屁股挪到边上，给冈伦留出了坐下的位置。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈伦坐在了真由喜的身边。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "仰望夜空，天上繁星点点。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0127"
    $ current_voice = "voice/MAY05A_MAY0127.ogg"
    "真由理" "「喂，冈伦。快看，星星好棒啊。很漂亮是吧─？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0077"
    $ current_voice = "voice/MAY05A_OKA0077.ogg"
    "伦太郎" "「嗯」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0128"
    $ current_voice = "voice/MAY05A_MAY0128.ogg"
    "真由理" "「果然在这里看到的星星是最漂亮的啊─」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0078"
    $ current_voice = "voice/MAY05A_OKA0078.ogg"
    "伦太郎" "「因为在暗处容易看到星星」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0129"
    $ current_voice = "voice/MAY05A_MAY0129.ogg"
    "真由理" "「嗯，不光是这个缘故，还因为这里是真由喜的圣域。因此感觉看得更清楚也说不定？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0079"
    $ current_voice = "voice/MAY05A_OKA0079.ogg"
    "伦太郎" "「圣域啊。这就是所谓的脑内补正啊，真由理很擅长这个啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0130"
    $ current_voice = "voice/MAY05A_MAY0130.ogg"
    "真由理" "「嗯！」"
    "两个人坐在一起，沉默不语地仰望着夜空。"
    "沉默不语地仰望着星空，就感觉像要被吸进去了似的。"
    "附近特别安静，时间缓缓地流淌着。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0131"
    $ current_voice = "voice/MAY05A_MAY0131.ogg"
    "真由理" "「真由喜总是坐在这里，仰望天空，思考各种各样的事情」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0080"
    $ current_voice = "voice/MAY05A_OKA0080.ogg"
    "伦太郎" "「有时候每天都来呢」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0132"
    $ current_voice = "voice/MAY05A_MAY0132.ogg"
    "真由理" "「冈伦也一起来了呢」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0081"
    $ current_voice = "voice/MAY05A_OKA0081.ogg"
    "伦太郎" "「因为真由理是我的人质啊，我有义务监视着你」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0133"
    $ current_voice = "voice/MAY05A_MAY0133.ogg"
    "真由理" "「嘿嘿嘿，那个时候还真是给你添麻烦了─」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0134"
    $ current_voice = "voice/MAY05A_MAY0134.ogg"
    "真由理" "「……不，不光是那个时候……一直以来都在给冈伦添麻烦……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0135"
    $ current_voice = "voice/MAY05A_MAY0135.ogg"
    "真由理" "「对不起……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0082"
    $ current_voice = "voice/MAY05A_OKA0082.ogg"
    "伦太郎" "「为什么道歉？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0136"
    $ current_voice = "voice/MAY05A_MAY0136.ogg"
    "真由理" "「因为……给你添麻烦了」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0083"
    $ current_voice = "voice/MAY05A_OKA0083.ogg"
    "伦太郎" "「区区照顾你一个人，根本不在话下」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0137"
    $ current_voice = "voice/MAY05A_MAY0137.ogg"
    "真由理" "「冈伦……一直都在这么说。真由喜就在对冈伦撒娇。但是，总是这样或许是不行的」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0138"
    $ current_voice = "voice/MAY05A_MAY0138.ogg"
    "真由理" "「……………………」"
    window hide



    $ loadBG(2,"BG64N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0084"
    $ current_voice = "voice/MAY05A_OKA0084.ogg"
    "伦太郎" "「……真由理，怎么了？　你今天有点奇怪啊？　发生什么事了吗？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0139"
    $ current_voice = "voice/MAY05A_MAY0139.ogg"
    "真由理" "「什么事都……没有」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0085"
    $ current_voice = "voice/MAY05A_OKA0085.ogg"
    "伦太郎" "「真由理，不擅长说谎啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0140"
    $ current_voice = "voice/MAY05A_MAY0140.ogg"
    "真由理" "「诶诶～？　不过感觉没有冈伦那么差劲啊～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0086"
    $ current_voice = "voice/MAY05A_OKA0086.ogg"
    "伦太郎" "「我不擅长说谎？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0141"
    $ current_voice = "voice/MAY05A_MAY0141.ogg"
    "真由理" "「嗯，冈伦总是对真由喜撒善意的谎言是吧？　真由喜是知道的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA03"),"True","lh/OKA_ALA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0087"
    $ current_voice = "voice/MAY05A_OKA0087.ogg"
    "伦太郎" "「……啥，你在说什么？　完全不知道你指的是什么。是真由理的错觉吧？　因为真由理很擅长脑内补正」"
    "面对板着脸故意装傻的冈伦，不由得笑了出来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0142"
    $ current_voice = "voice/MAY05A_MAY0142.ogg"
    "真由理" "「呼呼。真是的，冈伦，从过去起就喜欢说反话。现在还没有变」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0088"
    $ current_voice = "voice/MAY05A_OKA0088.ogg"
    "伦太郎" "「真抱歉啊，我这个星座的人就这个性格，没有办法的吧？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0143"
    $ current_voice = "voice/MAY05A_MAY0143.ogg"
    "真由理" "「可不能把错推到星座身上啊～？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0089"
    $ current_voice = "voice/MAY05A_OKA0089.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0144"
    $ current_voice = "voice/MAY05A_MAY0144.ogg"
    "真由理" "「…………」"

    stop bgm 
    "对话中止了，周围恢复了寂静。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "再一次抬头仰望天空，像往常一样搜寻那颗星星。"
    "在柔和地闪烁着的星星当中，立刻就找到了比其他星星都亮的北极星。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0145"
    $ current_voice = "voice/MAY05A_MAY0145.ogg"
    "真由理" "「……找到了」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0090"
    $ current_voice = "voice/MAY05A_OKA0090.ogg"
    "伦太郎" "「找到什么了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0146"
    $ current_voice = "voice/MAY05A_MAY0146.ogg"
    "真由理" "「奶奶说的那颗星星」"
    "奶奶曾经告诉过真由喜星星的事。"
    "奶奶把图鉴拿在手里，教给了真由喜很多就连那时还是孩子的真由喜也能轻松找到的星星。"
    "北极星是真由喜最先能够找到的星星。"
    "像是被那颗星星吸引着一样站了起来。"
    "踮起了脚，不由得把手伸向了北极星。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0147"
    $ current_voice = "voice/MAY05A_MAY0147.ogg"
    "真由理" "「…………」"
    "很羡慕那颗一直不变地在同一个地方发光的星星。"
    "要是奶奶能一直在真由喜的身边就好了。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0091"
    $ current_voice = "voice/MAY05A_OKA0091.ogg"
    "伦太郎" "「星屑的握手么，真由理的那个习惯还没有变啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0148"
    $ current_voice = "voice/MAY05A_MAY0148.ogg"
    "真由理" "「……嗯，希望能够……抓住那颗星。感觉真由喜也能一直不变地保持下去……」"
    "保持着把手伸向北极星的姿势，说出了至今为止没有告诉任何人的秘密。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0092"
    $ current_voice = "voice/MAY05A_OKA0092.ogg"
    "伦太郎" "「那颗星？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0149"
    $ current_voice = "voice/MAY05A_MAY0149.ogg"
    "真由理" "「北极星。一直不变地在同一个地方发光的星星」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0093"
    $ current_voice = "voice/MAY05A_OKA0093.ogg"
    "伦太郎" "「一直不变……么」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0150"
    $ current_voice = "voice/MAY05A_MAY0150.ogg"
    "真由理" "「嗯，变化……是非常可怕的……在奶奶死后，真由喜的世界……一切都变了……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0151"
    $ current_voice = "voice/MAY05A_MAY0151.ogg"
    "真由理" "「全部都是灰色的，什么都感觉不到……就好像在看不见出口的巨大迷宫里迷路了一样……」"
    "光是回过头去回忆那时的事，身体就发抖了起来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0152"
    $ current_voice = "voice/MAY05A_MAY0152.ogg"
    "真由理" "「寂寞……害怕……」"
    "后面怎么也说不出口。"
    "好像全身都在拒绝说，不想再继续说下去了。"
    "但是，双臂互抱，抑制住颤抖，终于可以继续把话说出来了。"
    "因为想对冈伦，把话好好说清楚。"

    window hide



    $ loadBG(2,"BG64N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM06"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0153"
    $ current_voice = "voice/MAY05A_MAY0153.ogg"
    "真由理" "「其实，奶奶死的那天，跟真由喜说好了，要一起做团子，然后一起吃……说要教真由喜制作团子的方法……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0154"
    $ current_voice = "voice/MAY05A_MAY0154.ogg"
    "真由理" "「但是，正好那一天，真由喜被朋友约出去参加庙会……没能遵守和奶奶的约定……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0155"
    $ current_voice = "voice/MAY05A_MAY0155.ogg"
    "真由理" "「因为想着奶奶什么时候都能见，明天再说也是可以的……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0156"
    $ current_voice = "voice/MAY05A_MAY0156.ogg"
    "真由理" "「但是那样的明天却没有到来……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0094"
    $ current_voice = "voice/MAY05A_OKA0094.ogg"
    "伦太郎" "「这样……的啊……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0157"
    $ current_voice = "voice/MAY05A_MAY0157.ogg"
    "真由理" "「嗯，奶奶……身体状况突然变糟了。但是因为她是一个人住……谁都没有注意到她倒下了……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0158"
    $ current_voice = "voice/MAY05A_MAY0158.ogg"
    "真由理" "「要是那个时候，真由喜遵守了约定，或许奶奶就不用死了……非常的后悔」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0159"
    $ current_voice = "voice/MAY05A_MAY0159.ogg"
    "真由理" "「但是这种事，没有跟任何人说」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0160"
    $ current_voice = "voice/MAY05A_MAY0160.ogg"
    "真由理" "「……因为怕别人说是真由喜杀死了奶奶」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA04"),"True","lh/OKA_ALA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0095"
    $ current_voice = "voice/MAY05A_OKA0095.ogg"
    "伦太郎" "「那是不可能的吧……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0161"
    $ current_voice = "voice/MAY05A_MAY0161.ogg"
    "真由理" "「但是……可能永远都不会跟任何人说，不会跟任何人说……这种事一直在脑袋里盘旋，停不下来……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0162"
    $ current_voice = "voice/MAY05A_MAY0162.ogg"
    "真由理" "「回过神来，真由喜周围的世界，已经变成灰色的了……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0096"
    $ current_voice = "voice/MAY05A_OKA0096.ogg"
    "伦太郎" "「……这就是类似于防卫本能之类的东西吧」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0163"
    $ current_voice = "voice/MAY05A_MAY0163.ogg"
    "真由理" "「嗯……但是。从那个迷宫里救出真由喜的人，是冈伦。告诉了真由喜，出口在这里」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0097"
    $ current_voice = "voice/MAY05A_OKA0097.ogg"
    "伦太郎" "「那时的真由理，像是要走远了一样，目光没有办法移开啊」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0164"
    $ current_voice = "voice/MAY05A_MAY0164.ogg"
    "真由理" "「在成为了冈伦的人质以后，灰色的世界渐渐地恢复了颜色」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0165"
    $ current_voice = "voice/MAY05A_MAY0165.ogg"
    "真由理" "「冈伦，谢谢你让真由喜成为人质」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0166"
    $ current_voice = "voice/MAY05A_MAY0166.ogg"
    "真由理" "「但是，真由喜已经不需要你再照顾了──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA03"),"True","lh/OKA_ALA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0098"
    $ current_voice = "voice/MAY05A_OKA0098.ogg"
    "伦太郎" "「这是什么意思？」"
    "被冈伦尖锐的目光盯着，让真由喜犹豫要不要再继续说下去。"
    "但是，真由喜拿出了勇气，拼命地继续说了下去。"

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0168"
    $ current_voice = "voice/MAY05A_MAY0168.ogg"
    "真由理" "「不能再对冈伦温柔的谎言撒娇了，必须得开始改变了，所以……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0099"
    $ current_voice = "voice/MAY05A_OKA0099.ogg"
    "伦太郎" "「真由理，你在……说什么？」"
    "大大地深吸了一口气，让内心平静下来。"
    "要是可以的话，不想说出这句话。"
    "但是必须要说──"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0169"
    $ current_voice = "voice/MAY05A_MAY0169.ogg"
    "真由理" "「从今天开始，真由喜不想再做冈伦的人质了」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0100"
    $ current_voice = "voice/MAY05A_OKA0100.ogg"
    "伦太郎" "「……！？　你……说什么？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0101"
    $ current_voice = "voice/MAY05A_OKA0101.ogg"
    "伦太郎" "「这种事我不同意！　不准随便做决定！」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0170"
    $ current_voice = "voice/MAY05A_MAY0170.ogg"
    "真由理" "「冈伦因为真由喜的缘故已经受了很多苦了，真由喜是知道的……但是真由喜，不想再看到……冈伦受苦了……」"
    hide screen phonebtn
    "从背在身后的包里掏出了日记本与蓝色呜啪，递给了冈伦。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0171"
    $ current_voice = "voice/MAY05A_MAY0171.ogg"
    "真由理" "「这个，想让冈伦替真由喜拿着」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0102"
    $ current_voice = "voice/MAY05A_OKA0102.ogg"
    "伦太郎" "「……呜啪和……日记本？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0172"
    $ current_voice = "voice/MAY05A_MAY0172.ogg"
    "真由理" "「蓝色呜帕是真由喜的呜啪收藏品中最喜欢的一个，是真由喜的宝物～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0103"
    $ current_voice = "voice/MAY05A_OKA0103.ogg"
    "伦太郎" "「既然是宝物的话，自己拿着不就好了？」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0173"
    $ current_voice = "voice/MAY05A_MAY0173.ogg"
    "真由理" "「一直都是受到了冈伦的帮助，所以请拿着这个重要的东西」 "
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0174"
    $ current_voice = "voice/MAY05A_MAY0174.ogg"
    "真由理" "「希望冈伦每当看到蓝色呜帕的时候，就能回忆起真由喜啊～」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0104"
    $ current_voice = "voice/MAY05A_OKA0104.ogg"
    "伦太郎" "「……不要说奇怪的话。我是不可能忘记你的吧！　没必要借助蓝色呜啪什么的！」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0175"
    $ current_voice = "voice/MAY05A_MAY0175.ogg"
    "真由理" "「不要这么说。呐、冈伦，真由喜的日记本和蓝色呜啪，就作为真由喜的替身，成为人质」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "面对想要把日记本和蓝色呜啪塞回来的冈伦，后退了一步。"
    "这下──留有遗憾的事情就没有了。"
    "剩下的，就是按下发送事先已经显示出来的短信的按钮。"
    "藏在身后准备按下手机发送按钮的大拇指不由得颤抖了起来。"
    "这封Ｄｍａｉｌ，是通往真由喜没有成为冈伦人质的过去的大门。"
    "为了遵守那天没能遵守的与奶奶的约定的短信。"
    "发给妈妈过去的手机的短信。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0105"
    $ current_voice = "voice/MAY05A_OKA0105.ogg"
    "伦太郎" "「真由……理？　你想做什么！？　难道说──」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0176"
    $ current_voice = "voice/MAY05A_MAY0176.ogg"
    "真由理" "「冈伦、有机会再见了……肯定能再见的吧？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA06"),"True","lh/OKA_ALA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈伦意识到了藏在真由喜身后的手机，想要过来抓。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0106"
    $ current_voice = "voice/MAY05A_OKA0106.ogg"
    "伦太郎" "「Ｄｍａｉｌ！？　真由理！　住手！　快住手！」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0177"
    $ current_voice = "voice/MAY05A_MAY0177.ogg"
    "真由理" "「呜！？」"
    "好大的劲。"
    "手腕被抓住了，手机就要被夺走了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0178"
    $ current_voice = "voice/MAY05A_MAY0178.ogg"
    "真由理" "「……冈伦……会再见的，好吗？」"
    "拼命地露出了笑脸。"
    "但是，不管怎么努力，也只能边哭边笑，有些不甘心。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0179"
    $ current_voice = "voice/MAY05A_MAY0179.ogg"
    "真由理" "「……真由喜……其实想、一直……做冈伦的……啊」"
    "在手机要被抢走的一瞬间，按下了短信的发送按钮。"

    "下一个瞬间──周围的声音突然就听不见了。"
    "安静得让耳朵发痛。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0107"
    $ current_voice = "voice/MAY05A_OKA0107.ogg"
    "伦太郎" "「……！？」"
    "冈伦在说着什么。"
    "但是已经什么都听不到了。"
    "不知道在说些什么。"
    "跟奶奶去世的时候一样。"
    "世界在一瞬间被涂上了一层灰色。"

    hide screen phoneSD1
    window hide



    play se "SGSE054"



    hide screen phonebtn
    scene expression Solid("000000")  with fade

    return









    return






    return







    return











    return







    return
