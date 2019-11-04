label SGFD2_KYO09A:
    window hide


    $ loadBG(0,"BG21N")







    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "等头晕过去了以后，我面前站着的是红莉栖。"
    "但是已经没有说明的时间了。"
    window hide


    $ loadBG(2,"BG21NR")



    hide screen phonebtn
    "我什么也没有告诉她，径直地走到了左下的保险柜边上，然后把手掌伸进缝隙里。"
    "指尖摸到了什么坚硬的东西。"
    "那就是用胶带铁柱的钥匙。"
    "于是剥下来一看，果然是保险柜的钥匙。"
    "上面刻着『００５』的编号。"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0000"
    $ current_voice = "voice/KYO09A_OKA0000.ogg"
    "伦太郎" "「很好！」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0000"
    $ current_voice = "voice/KYO09A_CRS0000.ogg"
    "红莉栖" "「等，等等怎么回事……？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0001"
    $ current_voice = "voice/KYO09A_OKA0001.ogg"
    "伦太郎" "「具体等会再和你说，现在先安静一下」"
    "在红莉栖困惑的目光下，我淡定地做了我应该的事。"
    "将钥匙插入『００５』号保险柜的锁，转动。"
    play se "SGSE111"

    "听到了一声好听的嗑哒声，手里的钥匙传来了打开的感觉。"
    hide screen phoneSD1
    window hide


    $ loadBG(3,"BG_BLACK")






    "我深深地呼吸了几次，闭上了眼睛。"
    "拜托了，请在里面吧……"
    "完成了祈祷之后，我缓缓地打开了……那扇门。"
    play se "SGSE329"

    "然后……"
    window hide


    $ loadBG(2,"BG21NR")
    $ loadBG(2,"IBGX090",png=True)







    play bgm "BGM13"
    hide screen phonebtn
    show screen phoneSD1
    "里面确实放着怀表。"
    "就是对于真由理来说非常重要的宝物——『怀酱』！"
    "当然『怀酱』毫发无损。"
    "也就是还是之前那份完整的样子。"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0002"
    $ current_voice = "voice/KYO09A_OKA0002.ogg"
    "伦太郎" "「唔啊哈哈哈！　看到了吗、４℃哦！　这就是魔眼的力量！」"
    "我一边用着丰满的男高音向着全宇宙宣告着，一边将从保险柜里取出的『怀酱』放到口袋里。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "顺便虽然没有必要，但是还是姑且说明一下，在『第１世界线』上『怀酱』安然无恙是因为我和红莉栖一直在保险柜之前的关系。"
    "因此４℃就没法『工作』，保险柜也就没有被破坏。"
    window hide


    $ loadBG(0,"BG21N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0003"
    $ current_voice = "voice/KYO09A_OKA0003.ogg"
    "伦太郎" "「好了，出发吧，克里斯提娜！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0001"
    $ current_voice = "voice/KYO09A_CRS0001.ogg"
    "红莉栖" "「是要去哪……？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0004"
    $ current_voice = "voice/KYO09A_OKA0004.ogg"
    "伦太郎" "「当然是我们的据点，Ｌａｂ咯！」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0002"
    $ current_voice = "voice/KYO09A_CRS0002.ogg"
    "红莉栖" "「那ｉｃｈｓ的事怎么办……？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0005"
    $ current_voice = "voice/KYO09A_OKA0005.ogg"
    "伦太郎" "「ｉｃｈｓ不是诱拐犯，只是个典当屋的ｃｏｓｐｌａｙｅｒ而已。也可以说是ｃｏｓｐｌａｙｅｒ的典当铺。」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0003"
    $ current_voice = "voice/KYO09A_CRS0003.ogg"
    "红莉栖" "「虽，虽然不太明白……那真由理在哪？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0006"
    $ current_voice = "voice/KYO09A_OKA0006.ogg"
    "伦太郎" "「真由理不用担心她。事件已经解决了。不对，不如说从最初开始就没有发送过什么事情。」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0004"
    $ current_voice = "voice/KYO09A_CRS0004.ogg"
    "红莉栖" "「……哈？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0007"
    $ current_voice = "voice/KYO09A_OKA0007.ogg"
    "伦太郎" "「总之我们出发吧，＠ｃｈａｎｎｅｌ克里斯！　回Ｌａｂ吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0005"
    $ current_voice = "voice/KYO09A_CRS0005.ogg"
    "红莉栖" "「不要那么叫我！」"
    window hide



    $ loadBG(0,"BG05N1")




    $ loadBG(2,"BG02N2")



    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0008"
    $ current_voice = "voice/KYO09A_OKA0008.ogg"
    "伦太郎" "「所以说，所有的谜题都解开了哦，各位」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB02"),"True","lh/DAR_AMB02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0006"
    $ current_voice = "voice/KYO09A_CRS0006.ogg"
    "红莉栖" "「虽然我还是完全不知道怎么回事……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWSK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWSK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KWSK"])
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0000"
    $ current_voice = "voice/KYO09A_DAR0000.ogg"
    "至" "「{color=#f00}ｋｗｓｋ{/color}」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0009"
    $ current_voice = "voice/KYO09A_OKA0009.ogg"
    "伦太郎" "「好的吧。那就都告诉你」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0010"
    $ current_voice = "voice/KYO09A_OKA0010.ogg"
    "伦太郎" "「这一切都是从『１５点１８分』收到的一封Ｄｍａｉｌ开始的」"
    $ loadBG(0,"PBG03A",over=True)
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0011"
    $ current_voice = "voice/KYO09A_OKA0011.ogg"
    "伦太郎" "「也就是说，答案隐藏在真由理手机里的这封邮件里……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0012"
    $ current_voice = "voice/KYO09A_OKA0012.ogg"
    "伦太郎" "「但是好巧不巧的，手机刚好没有电了。所以这样下去没有办法读到那封邮件」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0013"
    $ current_voice = "voice/KYO09A_OKA0013.ogg"
    "伦太郎" "「桶子，能把在那边的我的手机充电器拿过来吗？」"
    hide background-over 

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0001"
    $ current_voice = "voice/KYO09A_DAR0001.ogg"
    "至" "「但是我拒绝」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0014"
    $ current_voice = "voice/KYO09A_OKA0014.ogg"
    "伦太郎" "「这种时候不是应该拒绝的时候吧！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0002"
    $ current_voice = "voice/KYO09A_DAR0002.ogg"
    "至" "「给」"
    "桶子这么说着，将充电器投向了我这边。"
    "我一把接住之后，将充电器和真由理的手机接上，再将另一端插入了插座。"
    "我和真由理用的是同一款手机，所以充电器是可以通用的。"
    $ loadBG(0,"BG02N2")
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0015"
    $ current_voice = "voice/KYO09A_OKA0015.ogg"
    "伦太郎" "「这样就可以……」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0007"
    $ current_voice = "voice/KYO09A_CRS0007.ogg"
    "红莉栖" "「那，赶紧把邮件找出来──」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0016"
    $ current_voice = "voice/KYO09A_OKA0016.ogg"
    "伦太郎" "「等一下！　那种事不要急。万物之间都是有顺序的。山村先生也是这么说的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0008"
    $ current_voice = "voice/KYO09A_CRS0008.ogg"
    "红莉栖" "「谁呀，那是……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0017"
    $ current_voice = "voice/KYO09A_OKA0017.ogg"
    "伦太郎" "「总而言之马上就说完了。嘛听我说吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0009"
    $ current_voice = "voice/KYO09A_CRS0009.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0018"
    $ current_voice = "voice/KYO09A_OKA0018.ogg"
    "伦太郎" "「目前这个Ｄｍａｉｌ有两个谜。一个是内容，还有一个是发件人。」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0019"
    $ current_voice = "voice/KYO09A_OKA0019.ogg"
    "伦太郎" "「首先就发件人说一下吧」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0020"
    $ current_voice = "voice/KYO09A_OKA0020.ogg"
    "伦太郎" "「从结论开始说吧。发送这封Ｄｍａｉｌ的人是——克里斯提娜，你。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0010"
    $ current_voice = "voice/KYO09A_CRS0010.ogg"
    "红莉栖" "「什，什么呀，这种『犯人就是你』的说法……！」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0011"
    $ current_voice = "voice/KYO09A_CRS0011.ogg"
    "红莉栖" "「而且我也没有发过什么Ｄｍａｉｌ啊……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0021"
    $ current_voice = "voice/KYO09A_OKA0021.ogg"
    "伦太郎" "「发过的哟，在『第３世界线』上。发送人的账户名是『ｓｉｄｅｋｉｃｋ２５７』」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0012"
    $ current_voice = "voice/KYO09A_CRS0012.ogg"
    "红莉栖" "「『ｓｉｄｅｋｉｃｋ２５７』？　那确实是在真由理手机里的……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0022"
    $ current_voice = "voice/KYO09A_OKA0022.ogg"
    "伦太郎" "「不是已经说过是发到真由理的手机里的吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0013"
    $ current_voice = "voice/KYO09A_CRS0013.ogg"
    "红莉栖" "「啊啊，那就是说那个『１５点１８分』收到的邮件，那个……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0023"
    $ current_voice = "voice/KYO09A_OKA0023.ogg"
    "伦太郎" "「是的，就是那个」"
    "那封Ｄｍａｉｌ和这条世界线上的红莉栖一起确认过。"
    "所以红莉栖知道那封邮件的内容。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0003"
    $ current_voice = "voice/KYO09A_DAR0003.ogg"
    "至" "「怎么感觉只有我被蒙在鼓里啊？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0024"
    $ current_voice = "voice/KYO09A_OKA0024.ogg"
    "伦太郎" "「放心吧，桶子。克里斯提娜也完全没有注意到的样子」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0014"
    $ current_voice = "voice/KYO09A_CRS0014.ogg"
    "红莉栖" "「不知为何总觉得有点火大……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0025"
    $ current_voice = "voice/KYO09A_OKA0025.ogg"
    "伦太郎" "「好了先说回来。关于账户名的问题」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0026"
    $ current_voice = "voice/KYO09A_OKA0026.ogg"
    "伦太郎" "「克里斯提娜……『ｓｉｄｅｋｉｃｋ』是什么意思？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0015"
    $ current_voice = "voice/KYO09A_CRS0015.ogg"
    "红莉栖" "「朋友啦，挚友啦，伙伴啦，还有……助手啦之类的意思」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0027"
    $ current_voice = "voice/KYO09A_OKA0027.ogg"
    "伦太郎" "「哈。说起来克里斯提娜，对于我来说你是什么人啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB02"),"True","lh/CRS_AMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0016"
    $ current_voice = "voice/KYO09A_CRS0016.ogg"
    "红莉栖" "「毫不相关的人」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0028"
    $ current_voice = "voice/KYO09A_OKA0028.ogg"
    "伦太郎" "「是我的助手！　有些自知之明吧，第一世界线的克里斯提娜哦！　你应该有些第３世界线的克里斯提娜的感受吧？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0029"
    $ current_voice = "voice/KYO09A_OKA0029.ogg"
    "伦太郎" "「如果不是那样的话，也就不会用『ｓｉｄｅｋｉｃｋ』这样的账户名了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0017"
    $ current_voice = "voice/KYO09A_CRS0017.ogg"
    "红莉栖" "「为啥总感觉因果反了……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0030"
    $ current_voice = "voice/KYO09A_OKA0030.ogg"
    "伦太郎" "「难道说你想说『ｓｉｄｅｋｉｃｋ２５７』不是你吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0018"
    $ current_voice = "voice/KYO09A_CRS0018.ogg"
    "红莉栖" "「虽然不是想那么说……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0031"
    $ current_voice = "voice/KYO09A_OKA0031.ogg"
    "伦太郎" "「那我就问问你吧。你的生日是几月几日？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0019"
    $ current_voice = "voice/KYO09A_CRS0019.ogg"
    "红莉栖" "「７月２５日」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0032"
    $ current_voice = "voice/KYO09A_OKA0032.ogg"
    "伦太郎" "「日期和月份反过来的话？」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0004"
    $ current_voice = "voice/KYO09A_DAR0004.ogg"
    "至" "「２５７……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0020"
    $ current_voice = "voice/KYO09A_CRS0020.ogg"
    "红莉栖" "「但，但是，我又没有那种账户！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SUTEADD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SUTEADD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SUTEADD"])
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0033"
    $ current_voice = "voice/KYO09A_OKA0033.ogg"
    "伦太郎" "「确实是这样呢。因为这个账号是『第３世界线』上的助手在网吧里创建的{color=#f00}一次性账号{/color}。」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0005"
    $ current_voice = "voice/KYO09A_DAR0005.ogg"
    "至" "「网吧？　牧濑氏，难道去网吧了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0021"
    $ current_voice = "voice/KYO09A_CRS0021.ogg"
    "红莉栖" "「才，才没有去呢……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0034"
    $ current_voice = "voice/KYO09A_OKA0034.ogg"
    "伦太郎" "「为啥要否认？　去网吧又不是什么丢脸的事」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_REAJU"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SWEETS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SWEETS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SWEETS"])

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0006"
    $ current_voice = "voice/KYO09A_DAR0006.ogg"
    "至" "「是啊。普通的{color=#f00}现充{/color}呀、{color=#f00}糖果系女子{/color}呀，白脸小帅哥啊都会去的」"
    "桶子这么说了以后，红莉栖用手玩着头发有些扭捏地说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC02"),"True","lh/CRS_AMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0022"
    $ current_voice = "voice/KYO09A_CRS0022.ogg"
    "红莉栖" "「那，去过也是可能的……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0035"
    $ current_voice = "voice/KYO09A_OKA0035.ogg"
    "伦太郎" "「去了哦。确切的说是在『第３世界线』。你自己这么说的所以肯定没错」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0023"
    $ current_voice = "voice/KYO09A_CRS0023.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0036"
    $ current_voice = "voice/KYO09A_OKA0036.ogg"
    "伦太郎" "「那，话回到“一次性邮箱”上来。助手花了多久来创建这个账号呢？大概就是在让我等待的三分钟里吧。」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "在『第３世界线』上红莉栖让我等３分钟再启动电话微波炉（暂）。"
    "因为那个电话是用公共电话打的，所以大概红莉栖后来就回到了自己的基地，然后在那里创建了“一次性账号”。"
    "然后，她注册完账号，就准备好了邮件内容，然后发送给了电话微波炉（暂）。"
    window hide






    $ loadBG(0,"BG02N2")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0037"
    $ current_voice = "voice/KYO09A_OKA0037.ogg"
    "伦太郎" "「虽然常人感觉做不到这些，但是有着＠ｃｈａｎｎｅｌ的技能的话，也并非不可能」"
    "而且本来红莉栖就是年仅１７岁就在Ｓｃｉｅｎｃｅ杂志上发表论文的天才，这一点也不能忘了。"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0007"
    $ current_voice = "voice/KYO09A_DAR0007.ogg"
    "至" "「但是，为什么一定特意要用ＰＣ发送邮件？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0038"
    $ current_voice = "voice/KYO09A_OKA0038.ogg"
    "伦太郎" "「那个时候『第３世界线』的助手的手机坏掉了。好像是因为掉到网吧的厕所里了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB06"),"True","lh/DAR_AMB06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0008"
    $ current_voice = "voice/KYO09A_DAR0008.ogg"
    "至" "「哦哦……」"


    $ loadBG(2,"BG05N1")




    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0039"
    $ current_voice = "voice/KYO09A_OKA0039.ogg"
    "伦太郎" "「说起来，助手在这个时候还有一个难以理解的举动」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0040"
    $ current_voice = "voice/KYO09A_OKA0040.ogg"
    "伦太郎" "「最开始的时候Ｄｍａｉｌ的收件人是我，但是不知为何在放电现象开始后又改成了真由理的手机」"


    $ loadBG(2,"BG01N")




    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0041"
    $ current_voice = "voice/KYO09A_OKA0041.ogg"
    "伦太郎" "「这是因为将Ｄｍａｉｌ的内容加密了的关系」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0009"
    $ current_voice = "voice/KYO09A_DAR0009.ogg"
    "至" "「加密了吗？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0042"
    $ current_voice = "voice/KYO09A_OKA0042.ogg"
    "伦太郎" "「是啊。但是并不是那种数据上的加密，而只是一些文面上的——只有特定的人才能够读出来的文字」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0043"
    $ current_voice = "voice/KYO09A_OKA0043.ogg"
    "伦太郎" "「但是，那为什么要那么做呢？　是因为最开始要发给我的缘故。」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "在Ｄｍａｉｌ里面也记载着某个指示。"
    "也就是写着『做某事』的内容。"
    "如果是发送给我的手机的话，收到Ｄｍａｉｌ的我，自然就会按照所写的指示那么去做吧。"
    "但是万一在那之后，我被敌人捉住了怎么办？"
    "手机如果被夺走的话，这个指示就有可能被暴露给敌人。"
    "这就很糟糕了。发送Ｄｍａｉｌ的意义就没有了。"
    window hide






    $ loadBG(0,"BG02N2")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0044"
    $ current_voice = "voice/KYO09A_OKA0044.ogg"
    "伦太郎" "「于是『第３世界线』的助手就决定将邮件的内容加密。」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0024"
    $ current_voice = "voice/KYO09A_CRS0024.ogg"
    "红莉栖" "「也就是只有冈部能读懂的话，就算之后万一落入了敌人的手里，也不会简单地暴露这个指示吧？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0045"
    $ current_voice = "voice/KYO09A_OKA0045.ogg"
    "伦太郎" "「正是如此」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0010"
    $ current_voice = "voice/KYO09A_DAR0010.ogg"
    "至" "「那，为什么在那之后将收件人改成了真由氏呢？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0046"
    $ current_voice = "voice/KYO09A_OKA0046.ogg"
    "伦太郎" "「很简单」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0047"
    $ current_voice = "voice/KYO09A_OKA0047.ogg"
    "伦太郎" "「就算不加密这个信息，只要将收件人改成真由理的话，就可以保证这个指示不会暴露给敌人」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0048"
    $ current_voice = "voice/KYO09A_OKA0048.ogg"
    "伦太郎" "「『第３世界线』的助手在等待邮件发送的时候注意到了这一点」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0049"
    $ current_voice = "voice/KYO09A_OKA0049.ogg"
    "伦太郎" "「所以才会慌慌张张地给我打了电话，要求变更收件人为真由理。」"
    window hide


    $ loadBG(2,"IBGX072")




    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0025"
    $ current_voice = "voice/KYO09A_CRS0025.ogg"
    "红莉栖" "「那好吧……差不多是时候把答案告诉我们了吧」"
    window hide



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0050"
    $ current_voice = "voice/KYO09A_OKA0050.ogg"
    "伦太郎" "「好啊」"
    $ loadBG(0,"PBG03A")
    "我这么说了以后，将真由理的手机打开，然后打开了收件箱。"
    "然后找到了想要的秘密邮件，向着桶子递了出去（红莉栖已经看过一次了）"
    window hide
    hide screen phoneSD1
    hide screen phonebtn


    $ loadBG(2,"PBG15A")






    $ loadBG(2,"PBG15B")






    $ loadBG(2,"PBG15C")




    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0051"
    $ current_voice = "voice/KYO09A_OKA0051.ogg"
    "伦太郎" "「这是助手向我发送的密文。当然，我必须要知道怎么解读它才行」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0052"
    $ current_voice = "voice/KYO09A_OKA0052.ogg"
    "伦太郎" "「当然制作这个密文的人，也就是助手本身，也是知道它的加密方法的吧」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0053"
    $ current_voice = "voice/KYO09A_OKA0053.ogg"
    "伦太郎" "「那么解读方法到底是什么呢……？　我和助手都知道的加密方法……？」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0011"
    $ current_voice = "voice/KYO09A_DAR0011.ogg"
    "至" "「…………」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0026"
    $ current_voice = "voice/KYO09A_CRS0026.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0054"
    $ current_voice = "voice/KYO09A_OKA0054.ogg"
    "伦太郎" "「注意到的契机是，桶子在『第２世界线』告诉我的内容」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0012"
    $ current_voice = "voice/KYO09A_DAR0012.ogg"
    "至" "「我吗？我说了什么工口的东西？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0055"
    $ current_voice = "voice/KYO09A_OKA0055.ogg"
    "伦太郎" "「并没有说什么工口的东西」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG79N6",at=[Transform(yalign=1.0)])





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0013"
    $ current_voice = "voice/KYO09A_DAR0013.ogg"
    "至" "「顺便一提这个内容是牧濑氏发现的」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0014"
    $ current_voice = "voice/KYO09A_DAR0014.ogg"
    "至" "「冈伦，真的不记得了吗？这个＠ｃｈａｎｎｅｌ的文字，昨天晚上就给你看了哦。那个时候不是普通地读的吗」"
    window hide


    $ loadBG(0,"BG02N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0015"
    $ current_voice = "voice/KYO09A_DAR0015.ogg"
    "至" "「诶？　也就是说怎么回事？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0056"
    $ current_voice = "voice/KYO09A_OKA0056.ogg"
    "伦太郎" "「不明白吗？——是竖着读的啊」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0027"
    $ current_voice = "voice/KYO09A_CRS0027.ogg"
    "红莉栖" "「是啊，将三封邮件竖着放在一起读出来！」"
    "ｍｕｒｈａｒｍｓｂｌｋｕ&nａｒａｉｒｕｅａａｎａｓ&nｙｉｃｓｅ！ｉｉｌｉｋｅ"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0057"
    $ current_voice = "voice/KYO09A_OKA0057.ogg"
    "伦太郎" "「只需要从最左边开始读下来就可以了。于是就变成这样了」"
    "ｍａｙｕｒｉ　ｒａｃｈｉ　ｓａｒｅｒｕ！　ｍｅｉｓａｉ　ｂａｌｌｎｉ　ｋａｋｕｓｅ"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0016"
    $ current_voice = "voice/KYO09A_DAR0016.ogg"
    "至" "「把真由理……」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0028"
    $ current_voice = "voice/KYO09A_CRS0028.ogg"
    "红莉栖" "「藏起来……」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0017"
    $ current_voice = "voice/KYO09A_DAR0017.ogg"
    "至" "「在迷彩球里！」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0029"
    $ current_voice = "voice/KYO09A_CRS0029.ogg"
    "红莉栖" "「躲好！？」"
    "我用力地点了点头，说道。"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0058"
    $ current_voice = "voice/KYO09A_OKA0058.ogg"
    "伦太郎" "「在『１５点１８分』收到这封邮件的真由理恐怕很快──」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0059"
    $ current_voice = "voice/KYO09A_OKA0059.ogg"
    "伦太郎" "「不对，也许不会很快，但是总之收到了奇怪的邮件之后应该会让我知道」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0060"
    $ current_voice = "voice/KYO09A_OKA0060.ogg"
    "伦太郎" "「那个时候，我肯定和真由理一起在Ｌａｂ里吧」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0061"
    $ current_voice = "voice/KYO09A_OKA0061.ogg"
    "伦太郎" "「因为是那家伙所以肯定是『呐呐冈伦，有奇怪的邮件发过来了』什么的，让我看她的手机」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0062"
    $ current_voice = "voice/KYO09A_OKA0062.ogg"
    "伦太郎" "「然后，解读了这个邮件的我，按照指示里所写的让她躲了起来」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0018"
    $ current_voice = "voice/KYO09A_DAR0018.ogg"
    "至" "「也就是说……」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0030"
    $ current_voice = "voice/KYO09A_CRS0030.ogg"
    "红莉栖" "「真由理一直……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0063"
    $ current_voice = "voice/KYO09A_OKA0063.ogg"
    "伦太郎" "「是的──在这里哦」"
    $ loadBG(0,"BG01N")
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我朝着房间的一角走了过去，用脚拔掉了插座的电源线。"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0019"
    $ current_voice = "voice/KYO09A_DAR0019.ogg"
    "至" "「唔哈啪！　未来道具７号机『攻壳机动迷彩球ＤＥＭＯＮＩＺＥ　ＥＤＩＴＩＯＮ　ｖｅｒ．１．２４』降临ｋｔｋｒ──！」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0064"
    $ current_voice = "voice/KYO09A_OKA0064.ogg"
    "伦太郎" "「ＤＥＭＯＮＩＺＥ　ＥＤＩＴＩＯＮ？」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0020"
    $ current_voice = "voice/KYO09A_DAR0020.ogg"
    "至" "「魔改造过了，所以就决定这么叫了」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0031"
    $ current_voice = "voice/KYO09A_CRS0031.ogg"
    "红莉栖" "「呐，比起那种事，这里面真的有真由理吗……！？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0065"
    $ current_voice = "voice/KYO09A_OKA0065.ogg"
    "伦太郎" "「看一下不就知道了」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0066"
    $ current_voice = "voice/KYO09A_OKA0066.ogg"
    "伦太郎" "「呐桶子，这玩意怎么打开？」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0021"
    $ current_voice = "voice/KYO09A_DAR0021.ogg"
    "至" "「只要简单地举起来就行了」"

    stop bgm 
    "于是我按照他说的，举起了迷彩球。"
    "然后……"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO009A"]]["Check"]=True


    $ loadBG(2,"EV_KYO009A")



    play bgm "FD2BGM09"
    "真由理……"
    "在铺在地板的毯子上，真由理像猫一样蜷缩着睡得正香。"
    "呼吸十分平稳。"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0032"
    $ current_voice = "voice/KYO09A_CRS0032.ogg"
    "红莉栖" "「哎呀哎呀……真扫兴啊……」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0022"
    $ current_voice = "voice/KYO09A_DAR0022.ogg"
    "至" "「哈……那刚才的担心算什么呀？」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0033"
    $ current_voice = "voice/KYO09A_CRS0033.ogg"
    "红莉栖" "「但是，看起来好幸福啊」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0023"
    $ current_voice = "voice/KYO09A_DAR0023.ogg"
    "至" "「就像在捉迷藏的时候不小心睡着的孩子一样呢」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0034"
    $ current_voice = "voice/KYO09A_CRS0034.ogg"
    "红莉栖" "「总而言之……太好了呢，冈部」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0067"
    $ current_voice = "voice/KYO09A_OKA0067.ogg"
    "伦太郎" "「啊啊……」"
    "我好不容易吐出一句话。"
    "因为再说下去的话，感觉眼眶里有什么东西要流出来了……"
    "我们有好一会，只是安静地看着真由理的睡颜，沉默着。"
    "听着真由理的呼吸声，我突然想到了些不相关的事情。"
    "『第２世界线』呀『第３世界线』上，我肯定没有把真由理藏到这个迷彩球里面吧。"
    "大概在『第２世界线』和『第３世界线』上真由理也是收到了那样的邮件的。"
    "就算如此我也没有按照邮件上写着的内容去做。……这是为什么呢？"
    "从这里开始是我的推测，所以有可能有什么错的地方。"
    "但是，恐怕在『第２世界线』和『第３世界线』上，是这样的展开。"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "首先『１５点１８分』——真由理的手机收到了暗号的邮件。"
    "然后真由理就自己想了一会，试图来解开这个邮件里的内容。"
    "但是因为这样那样的原因『第２』和『第３世界线』我的手机里收到了『真由理的外出／必须全力阻止／会被诱拐的！』这样的Ｄｍａｉｌ。"
    "时间是『１５点２０分』——也就是暗号邮件发送到真由理的手机后两分钟。"
    "看到了那封邮件的我，感到了事态的紧迫性，于是在那之后一段时间没能听进真由理的话。"
    "另一方面真由理也……"
    "『听好了真由理，绝对不要外出！　呆在Ｌａｂ里！　好吗！』——被我凶神恶煞地这么要求了之后，也就没能好好地把暗号邮件但是告诉我。"
    "然后４分钟后的『１５点２４分』——『第２世界线』上接到了红莉栖打来的电话。"
    "当然是关于她收到的『尾行真由理吧／若不捉住犯人／诱拐阻止困难』的Ｄｍａｉｌ……。"
    "然后又是『第３世界线』的『１５点２２分』发来的『评议会要终止／不要使用火！／Ｌａｂ会起火』的Ｄｍａｉｌ"
    "『１５点２６分』的『绝对外出禁止／Ｌａｂ安全待机／和黑万十战斗』的Ｄｍａｉｌ被发送到了我和真由理的手机里。"
    "也就是连续不断的Ｄｍａｉｌ导致了真由理失去了说出最初的Ｄｍａｉｌ的机会。"
    "但是这样的事情只发生在了第二和第三世界线上。"
    "因为在这条世界线上Ｄｍａｉｌ并没有接踵而至，真由理才有机会问我关于这条暗号邮件的内容含义吧。"
    "『呐呐冈伦，收到了一封奇怪的邮件ー』"
    "我的话肯定是紧张起来，然后专心解读暗号，结果便是……"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO009A"]]["Check"]=True
    $ loadBG(0,"EV_KYO009A")



    show screen phonebtn
    show screen phoneSD1
    "现在这幅样子。"
    "在其他世界线上没有把真由理藏起来就是因为这个……"
    "不对，应该说是因为没有把真由理藏起来才会发生第二世界线和第三世界线那样的事情。"
    "这么想了之后……"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0000"
    $ current_voice = "voice/KYO09A_MAY0000.ogg"
    "真由理" "「恩……唔……」"
    "真由理发出困倦的声音，缓缓地睁开了眼睛。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO009B"]]["Check"]=True


    $ loadBG(2,"EV_KYO009B")



    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0001"
    $ current_voice = "voice/KYO09A_MAY0001.ogg"
    "真由理" "「咦……？　为什么……、大家……」"
    "我们三人……相互看看，脸上都露出了苦笑。"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0002"
    $ current_voice = "voice/KYO09A_MAY0002.ogg"
    "真由理" "「嘟嘟噜……♪　是真由理哦……」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0068"
    $ current_voice = "voice/KYO09A_OKA0068.ogg"
    "伦太郎" "「什么呀，那种没精打采的『嘟嘟噜』！」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0003"
    $ current_voice = "voice/KYO09A_MAY0003.ogg"
    "真由理" "「恩……因为才刚刚醒来嘛……」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0035"
    $ current_voice = "voice/KYO09A_CRS0035.ogg"
    "红莉栖" "「冈部，那是……？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0069"
    $ current_voice = "voice/KYO09A_OKA0069.ogg"
    "伦太郎" "「啊啊，是啊」"
    "我从口袋里取出惯例物品，将它放在真由理的手里。"
    "这么做了以后真由理吃了一惊……"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0004"
    $ current_voice = "voice/KYO09A_MAY0004.ogg"
    "真由理" "「诶？　诶诶诶诶？」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0005"
    $ current_voice = "voice/KYO09A_MAY0005.ogg"
    "真由理" "「这是，“怀酱”啊！　回来了啊！」"
    window hide



    $ loadBG(2,"BG01N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC01"),"True","lh/MAY_CMC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "这么说着，突然跳了起来。"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0006"
    $ current_voice = "voice/KYO09A_MAY0006.ogg"
    "真由理" "「但是，这，究竟是为什么呢？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0070"
    $ current_voice = "voice/KYO09A_OKA0070.ogg"
    "伦太郎" "「从天上掉下来的」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0007"
    $ current_voice = "voice/KYO09A_MAY0007.ogg"
    "真由理" "「诶嘿嘿，真的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0008"
    $ current_voice = "voice/KYO09A_MAY0008.ogg"
    "真由理" "「虽然不太明白，但是真由理非常高兴哦」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0009"
    $ current_voice = "voice/KYO09A_MAY0009.ogg"
    "真由理" "「谢谢你，冈伦！」"
    "真由理将“怀酱”放在耳边。"
    "一定是在听声音吧。真由理突然露出了恍惚的神情。"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0024"
    $ current_voice = "voice/KYO09A_DAR0024.ogg"
    "至" "「呐，说起来真由氏，真的一直在那个迷彩球里吗？」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0010"
    $ current_voice = "voice/KYO09A_MAY0010.ogg"
    "真由理" "「恩。为什么要问那种事啊？」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0036"
    $ current_voice = "voice/KYO09A_CRS0036.ogg"
    "红莉栖" "「因为觉得你可能不见了，所以大家都有点担心啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0011"
    $ current_voice = "voice/KYO09A_MAY0011.ogg"
    "真由理" "「不见了？　没有那种事啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB03"),"True","lh/MAY_CMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0012"
    $ current_voice = "voice/KYO09A_MAY0012.ogg"
    "真由理" "「真由喜，一直都在这里啊。所以不可能不见的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0013"
    $ current_voice = "voice/KYO09A_MAY0013.ogg"
    "真由理" "「因为真由喜啊，」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0014"
    $ current_voice = "voice/KYO09A_MAY0014.ogg"
    "真由理" "「真由喜是，」"
    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0015"
    $ current_voice = "voice/KYO09A_MAY0015.ogg"
    "真由理" "「冈伦的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0016"
    $ current_voice = "voice/KYO09A_MAY0016.ogg"
    "真由理" "「“人质”啊♪」"

    stop bgm 
    hide screen phoneSD1
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade
    $ renpy.movie_cutscene("video/fd2_ed.avi")








    $ loadBG(0,"BG01N")

    play se "SGSE022"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB01"),"True","lh/MAY_CMB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "KYO09A_MAY0017"
    $ current_voice = "voice/KYO09A_MAY0017.ogg"
    "真由理" "「小冈伦，谁好像来了啊」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0071"
    $ current_voice = "voice/KYO09A_OKA0071.ogg"
    "伦太郎" "「谁啊，在这种时候……」"


    $ loadBG(2,"BG01N")



    play se "SGSE024"
    "我走向了玄关，缓缓地打开了门。"
    "在那里出现的是……"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM08"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0072"
    $ current_voice = "voice/KYO09A_OKA0072.ogg"
    "伦太郎" "「桐──桐生──萌郁……」"
    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0000"
    $ current_voice = "voice/KYO09A_MOE0000.ogg"
    "萌郁" "「恩？难道在什么地方见过吗？」"
    "我慌忙确认了一下时间。"
    "虽然并不是完全一样，但是感觉像是Ｒｏｕｎｄｅｒ要出现的时间。"
    "难道说……不可能……"
    "感觉难以呼吸。"
    "手指感觉完全都不能动弹了。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at left0 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "然后，在这个时候走到这里的桶子……"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0025"
    $ current_voice = "voice/KYO09A_DAR0025.ogg"
    "至" "「啊，难道说是……是ｔａｂｕｏｋｕ的？」"
    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0001"
    $ current_voice = "voice/KYO09A_MOE0001.ogg"
    "萌郁" "「恩」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0026"
    $ current_voice = "voice/KYO09A_DAR0026.ogg"
    "至" "「在出版公司工作……？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HEN_PRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HEN_PRO"])
    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0002"
    $ current_voice = "voice/KYO09A_MOE0002.ogg"
    "萌郁" "「只是{color=#f00}编辑部{/color}而已。叫做『Ａｒｃ・ｒｅｗｒｉｔｅ』……」"

    stop bgm 
    "萌郁普通地说着话。"
    "不是『闪光的指压师(Ｓｈｉｎｉｎｇ　ｆｉｎｇｅｒ)』吗……？"
    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0003"
    $ current_voice = "voice/KYO09A_MOE0003.ogg"
    "萌郁" "「约定的时间，是２０点呢？是不是稍微有点早了？」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0027"
    $ current_voice = "voice/KYO09A_DAR0027.ogg"
    "至" "「不，不是，没关系……」"
    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0004"
    $ current_voice = "voice/KYO09A_MOE0004.ogg"
    "萌郁" "「那么，说好的东西，能给我吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0028"
    $ current_voice = "voice/KYO09A_DAR0028.ogg"
    "至" "「不是，那个，所以说，怎么说呢……」"
    "桶子的视线投向了房间的一角"
    "朝着视线看起，在那里的是……"
    window hide


    $ loadBG(2,"IBG023B",over=True)




    "被胡椒博士所浸染的……"
    "我不小心打翻了胡椒博士之后……"
    "价值３００万日元的……"
    "不对，曾经价值３００万日元的……"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0073"
    $ current_voice = "voice/KYO09A_OKA0073.ogg"
    "伦太郎" "「Ｓｋｅｔｃｈｂｏｏｋ……」"
    window hide
    hide background-over 




    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0005"
    $ current_voice = "voice/KYO09A_MOE0005.ogg"
    "萌郁" "「啊啊，十分抱歉呢。……。这样的话……有点…」"
    $ stopvoc("DAR")
    play DAR "KYO09A_DAR0029"
    $ current_voice = "voice/KYO09A_DAR0029.ogg"
    "至" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0074"
    $ current_voice = "voice/KYO09A_OKA0074.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "KYO09A_MOE0006"
    $ current_voice = "voice/KYO09A_MOE0006.ogg"
    "萌郁" "「打扰了，先告辞了」"
    play se "SGSE024"

    hide lh7 
    "就好像定身咒被解除了一样。"


    $ loadBG(2,"BG02A2")



    play bgm "FD2BGM11"
    "萌郁消失的同时，我立刻回过头去。"


    $ loadBG(2,"BG03A4")



    "飞快地冲入了开发室。"
    window hide


    $ loadBG(3,"BG_BLACK")






    $ loadBG(1,"BG03A4")








    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0037"
    $ current_voice = "voice/KYO09A_CRS0037.ogg"
    "红莉栖" "「等，等等冈部，打算做什么……！？」"
    "追过来的红莉栖问道。"
    "看她紧张的表情，一定是察觉到了我要干些什么了吧。"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0038"
    $ current_voice = "voice/KYO09A_CRS0038.ogg"
    "红莉栖" "「难道说……开玩笑的吧？」"
    "我站在Ｘ６８０００前说道。"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0075"
    $ current_voice = "voice/KYO09A_OKA0075.ogg"
    "伦太郎" "「还有一件尚未解决的事情」"
    window hide


    $ loadBG(2,"IBG026A",png=True)




    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0076"
    $ current_voice = "voice/KYO09A_OKA0076.ogg"
    "伦太郎" "「那就是我借着３００万日元的这件事」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0039"
    $ current_voice = "voice/KYO09A_CRS0039.ogg"
    "红莉栖" "「所以说不是说那笔钱没有必要还么──」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0077"
    $ current_voice = "voice/KYO09A_OKA0077.ogg"
    "伦太郎" "「不行，恐怕不能那样。我不知道什么时候就被沉到东京湾里去了。必须把钱还了」"
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0040"
    $ current_voice = "voice/KYO09A_CRS0040.ogg"
    "红莉栖" "「…………」"
    window hide



    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0078"
    $ current_voice = "voice/KYO09A_OKA0078.ogg"
    "伦太郎" "「返还手段想到了两个──」"
    window hide


    $ loadBG(2,"IBG024A")




    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0079"
    $ current_voice = "voice/KYO09A_OKA0079.ogg"
    "伦太郎" "「第一个就是拿下“秋叶原发明大赛”的大奖」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0080"
    $ current_voice = "voice/KYO09A_OKA0080.ogg"
    "伦太郎" "「还有一个就是──」"
    window hide





    $ loadBG(2,"IBG023B")




    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0081"
    $ current_voice = "voice/KYO09A_OKA0081.ogg"
    "伦太郎" "「回到过去，阻止胡椒博士洒到素描簿上」"
    window hide



    $ loadBG(1,"BG03A4")
    $ stopvoc("CRS")
    play CRS "KYO09A_CRS0041"
    $ current_voice = "voice/KYO09A_CRS0041.ogg"
    "红莉栖" "「那，那……你想选择哪个？」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0082"
    $ current_voice = "voice/KYO09A_OKA0082.ogg"
    "伦太郎" "「唔哈哈哈！　真是愚蠢的问题哦，克里斯提娜！」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0083"
    $ current_voice = "voice/KYO09A_OKA0083.ogg"
    "伦太郎" "「我会选择哪个？　那种问题不是早就决定好了吗！」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0084"
    $ current_voice = "voice/KYO09A_OKA0084.ogg"
    "伦太郎" "「我啊──」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0085"
    $ current_voice = "voice/KYO09A_OKA0085.ogg"
    "伦太郎" "「为了命运石之门(Ｓｔｅｉｎｓ；Ｇａｔｅ)的选择……我会奋战到底！」"
    $ stopvoc("OKA")
    play OKA "KYO09A_OKA0086"
    $ current_voice = "voice/KYO09A_OKA0086.ogg"
    "伦太郎" "「Ｅｌ・Ｐｓｙ・Ｃｏｎｇｒｏｏ」"

    hide screen phoneSD1
    window hide

    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    window hide

    show screen invisible
    $ renpy.movie_cutscene("video/imv05.avi")
    hide screen invisible
    "「三世因果的绑架·完成」"

    return
