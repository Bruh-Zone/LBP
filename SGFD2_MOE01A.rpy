label SGFD2_MOE01A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade
    with fade
    $ loadBG(0,"TIT008")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade



    $ date="8/15"
    $ day = "SAT"








    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MOE002A"]]["Check"]=True
    $ loadBG(0,"EV_MOE002A")

    play bgm "BGM25"
    hide screen phonebtn
    hide screen phoneSD1

    "今生第一次握住手枪。"
    "指尖慢慢搭上冰冷的扳机。"
    "只需轻轻一扣，我便能夺去她的性命。"
    "枪口的前方，是两位少女。"
    "啊啊……请不要用那样柔弱的眼光看着我啊。"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0000"
    $ current_voice = "voice/MOE01A_MOE0000.ogg"
    "萌郁" "「我是Ｍ４(エムフォー)……」"
    "像是说给自己听一样，我嚅嗫道。"
    "嗯，我就是Ｍ４。我不是桐生萌郁。"
    "从最开始我就是，欺骗着他们，混在他们之间的间谍。"
    "如果是为了ＦＢ的话……就算杀人也不是那样的令人讨厌。"
    "如果是为了ＦＢ的话……就算是再重要的人们也可以去杀。"
    "──４年前的那一天。"
    "在那时已经变得既无所求，亦无所牵挂的我。"
    "觉得应该了结余生，从大楼的顶上打算一跃而下的我。"
    "被ＦＢ的一条短信拯救了。"
    "是玩笑也好，是真心话也好。"
    "我只是对于自己被他人所理解感到高兴。"
    "我现在在这里站着。"
    "活下来真是太好了。"
    "震动的枪口，依然指向她们。"
    "想起来吧……想起来吧Ｍ４。"
    "想起你被ＦＢ拯救的那一天。"
    "那个人理解了我的所有。"
    "陪我进行了一整夜无聊的人生咨询。"
    "那时候真是开心啊。"
    "想与ＦＢ变得更加亲密。"
    "想要让自己对他变得更加重要。"
    "如果是那样的话，应该开火。应该开火啊Ｍ４。"
    "就算对方是……无可替代的人也……！"
    play se "SGSE060"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0001"
    $ current_voice = "voice/MOE01A_MOE0001.ogg"
    "萌郁" "「不准动」"
    "已经无法回头了。"
    "不，并没有回头的必要。"
    "红莉栖也好，真由理也好……就算被我用手枪指着，仍然用担心的眼神注视着我。"
    "就好像还把我当做Ｌａｂｍｅｍ……当做伙伴……当做朋友那样信任着我。"
    $ stopvoc("DAR")
    play DAR "MOE01A_DAR0000"
    $ current_voice = "voice/MOE01A_DAR0000.ogg"
    "至" "「桐生氏……？」"
    $ stopvoc("OKA")
    play OKA "MOE01A_OKA0000"
    $ current_voice = "voice/MOE01A_OKA0000.ogg"
    "伦太郎" "「萌郁！　你在干什么！」"
    "冈部君。"
    "桥田君。"
    "两位都在杀害对象中。"
    "从ＦＢ那里得到的命令是——"
    "『和时间机器有关的全员，全部抹杀掉吧』"
    "我必须将Ｌａｂｍ ｅ ｍ全部杀死。"
    "现在是最后的机会。"
    "我拼命调整混乱的呼吸。"
    "上吧，Ｍ４。"
    "我，不是桐生萌郁。"
    "我从最开始就不是他们的伙伴啊……"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0002"
    $ current_voice = "voice/MOE01A_MOE0002.ogg"
    "萌郁" "「我是、Ｍ４。ＳＥＲＮ的、Ｒｏｕｎｄｅｒ」"
    "不要慌张。冷静下来。"
    $ stopvoc("SUZ")
    play SUZ "MOE01A_SUZ0000"
    $ current_voice = "voice/MOE01A_SUZ0000.ogg"
    "铃羽" "「桐生萌郁！　为什么！　……咕啊！？」"
    $ stopvoc("OKA")
    play OKA "MOE01A_OKA0001"
    $ current_voice = "voice/MOE01A_OKA0001.ogg"
    "伦太郎" "「铃羽！」"
    "被我的行为所动摇的阿万音，被Ｒｏｕｎｄｅｒ制服了。"
    "押着阿万音的Ｒｏｕｎｄｅｒ朝这边看来。"
    $ stopvoc("Y01")
    play KUR "MOE01A_Y010000"
    $ current_voice = "voice/MOE01A_Y010000.ogg"
    "巡行者Ａ" "「你知道该怎么做的吧」"
    "要做什么，我当然心知肚明。"
    "明明是知道的……然而……"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0003"
    $ current_voice = "voice/MOE01A_MOE0003.ogg"
    "萌郁" "「我是、Ｍ４……！」"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0004"
    $ current_voice = "voice/MOE01A_MOE0004.ogg"
    "萌郁" "「我是……！」"
    "明明必须开枪。"
    "明明如果不那样做的话，我就会被ＦＢ抛弃。"
    "明明知道的……但指尖无法用力。"
    "为什么扣不下扳机呢。"
    "逃避着红莉栖和真由理的视线 "
    "拜托了，请不要那样看着我。"
    "就好像，真的在担心着我一样。"
    "再瞧不起我一些吧。"
    "再厌恶我一些吧。"
    "那样的话……我就能向你们开枪了。"
    "明明应该开枪的……"
    $ stopvoc("CRS")
    play CRS "MOE01A_CRS0000"
    $ current_voice = "voice/MOE01A_CRS0000.ogg"
    "红莉栖" "「萌郁」"
    "红莉栖朝着因为晃动而无法瞄准的我走了过来。"
    "为什么？就不怕吃枪子吗？"
    $ stopvoc("MAY")
    play MAY "MOE01A_MAY0000"
    $ current_voice = "voice/MOE01A_MAY0000.ogg"
    "真由理" "「萌郁」"
    "真由理也朝我走出了一步。"
    $ stopvoc("MOE")
    play MOE "MOE01A_MOE0005"
    $ current_voice = "voice/MOE01A_MOE0005.ogg"
    "萌郁" "「别过来！」"
    "我挥舞着手枪，然而两人并没有却步。"
    "停下来吧。"
    "请不要过来啊。"
    "不要再用那样温柔的眼光看着我了啊。"
    "我并不是你们能够施舍温柔的人类。"
    "请不要再那样温柔地对待我了！"
    "否则的话……否则我就要，无法成为Ｍ４了。"
    "变回那个，桐生萌郁了。"
    "所以拜托了，请不要那么温柔。"
    "为什么……为什么，会变成这样呢。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我为了忍住眼泪而闭上了眼，却想起了与Ｌａｂ众人度过的日子。"
    "面对装模作样的冈部君，沉着应对的红莉栖。"
    "乱入那个话题的桥田君，将整个对话慢慢地带偏。"
    "真由理一边看着这样的光景一边微笑着。"
    "已经是……遥远而宝贵的旧日时光了。"
    "胸口因为伤感而阵阵作痛。"
    "应该早就埋藏于心底的悲伤迸涌而出，那些回不去的日子在眼前鲜明地划过。"

    stop bgm 

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
