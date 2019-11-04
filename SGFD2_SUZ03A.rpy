label SGFD2_SUZ03A:
    window hide


    $ loadBG(0,"IBGX048")

    play se "SGSE200L" loop



    $ date="8/12"
    $ day="THU"
    python:
        RcvMail(285)
        ReadMail(285)
    hide screen phonebtn
    show screen phoneSD1

    "早上醒来的时候收到了桥田至的短信。"
    "不过短信内容是β说的，总结起来就是进展得很顺利，大概在早上就能修理完成。"
    "于是我在实验室与牧濑红莉栖告别，来到了广播馆。"
    window hide

    stop se


    $ loadBG(2,"BG06A1")



    show screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0000"
    $ current_voice = "voice/SUZ03A_SUZ0000.ogg"
    "铃羽" "「早上好！」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB01"),"True","lh/SUZ_BMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0001"
    $ current_voice="voice/SUZ03A_SUZ0001.ogg"
    "铃羽β" "「抱歉，请安静点」"
    "立刻就让她生气了。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "明明自己感觉并没有那么吵啊，但是一看β所指的地方，立刻就明白理由了。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0000"
    $ current_voice = "voice/SUZ03A_DAR0000.ogg"
    "至" "「…………」"
    "父亲还在睡觉。"
    "身边到处散落着纸片。"
    "上面还写着什么东西，看来既不是垃圾，也不是用来防寒的。"
    "而且现在也不是需要防寒的季节。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0002"
    $ current_voice="voice/SUZ03A_SUZ0002.ogg"
    "铃羽β" "「父亲，早上才睡下去」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0003"
    $ current_voice = "voice/SUZ03A_SUZ0003.ogg"
    "铃羽" "「这样啊……一直都在修理吧」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0004"
    $ current_voice="voice/SUZ03A_SUZ0004.ogg"
    "铃羽β" "「这个倒不是」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0005"
    $ current_voice = "voice/SUZ03A_SUZ0005.ogg"
    "铃羽" "「诶？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0006"
    $ current_voice="voice/SUZ03A_SUZ0006.ogg"
    "铃羽β" "「修理本身所需的时间并不用那么长，不过父亲还打听了很多时间机器的事情」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0007"
    $ current_voice = "voice/SUZ03A_SUZ0007.ogg"
    "铃羽" "「一直都在进行书写交流吧」"
    "原来父亲身边散落的纸片就是这个啊。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0008"
    $ current_voice="voice/SUZ03A_SUZ0008.ogg"
    "铃羽β" "「我说，α」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0009"
    $ current_voice = "voice/SUZ03A_SUZ0009.ogg"
    "铃羽" "「什么事？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA06"),"True","lh/SUZ_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "另一个我看起来有些低落。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0010"
    $ current_voice="voice/SUZ03A_SUZ0010.ogg"
    "铃羽β" "「我有必须要向你道歉的事情」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0011"
    $ current_voice = "voice/SUZ03A_SUZ0011.ogg"
    "铃羽" "「道歉？难道你指的是时间机器没办法修好的事情吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0012"
    $ current_voice="voice/SUZ03A_SUZ0012.ogg"
    "铃羽β" "「时间机器应该已经顺利修好了。但是没有多余的能量来进行检查，因此也没办法肯定」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0013"
    $ current_voice = "voice/SUZ03A_SUZ0013.ogg"
    "铃羽" "「那你要道什么歉？」"
    play bgm "BGM20"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0014"
    $ current_voice="voice/SUZ03A_SUZ0014.ogg"
    "铃羽β" "「因为我让父亲知道了时间机器的秘密」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0015"
    $ current_voice = "voice/SUZ03A_SUZ0015.ogg"
    "铃羽" "「秘密……」"
    "从现代人的父亲眼中看来，时间机器是个很神秘的盒子。但是从β微妙的表情看来，大概父亲知道了我最不想让他知道的事情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA06"),"True","lh/SUZ_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0016"
    $ current_voice="voice/SUZ03A_SUZ0016.ogg"
    "铃羽β" "「这个时间机器只能回到过去」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0017"
    $ current_voice = "voice/SUZ03A_SUZ0017.ogg"
    "铃羽" "「……这样啊」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0018"
    $ current_voice="voice/SUZ03A_SUZ0018.ogg"
    "铃羽β" "「我向你保证过不告诉其他人」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0019"
    $ current_voice = "voice/SUZ03A_SUZ0019.ogg"
    "铃羽" "「嗯」"
    "这件事我是最不想让父亲知道的。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0020"
    $ current_voice="voice/SUZ03A_SUZ0020.ogg"
    "铃羽β" "「没什么意义了呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0021"
    $ current_voice = "voice/SUZ03A_SUZ0021.ogg"
    "铃羽" "「……嗯」"
    "但说不定比所有人都知道这件事要好。"
    "但是这不能改变，我最不想让那个人知道，可那个人已经知道了这件事的这个事实。"

    stop bgm 
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0001"
    $ current_voice = "voice/SUZ03A_DAR0001.ogg"
    "至" "「嗯，唔……」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "但是现在已经没有追究这个问题的时间了。"
    "因为父亲被我的说话声吵醒了。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0002"
    $ current_voice = "voice/SUZ03A_DAR0002.ogg"
    "至" "「铃羽，你来了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0022"
    $ current_voice = "voice/SUZ03A_SUZ0022.ogg"
    "铃羽" "「诶？刚刚，他叫我铃羽？」"
    "父亲像海狮一样挺着肚子坐了起来。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0003"
    $ current_voice = "voice/SUZ03A_DAR0003.ogg"
    "至" "「嗯。小幽灵她告诉我，这样叫说不定会让你高兴」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0023"
    $ current_voice = "voice/SUZ03A_SUZ0023.ogg"
    "铃羽" "「这个……嗯。是呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0004"
    $ current_voice = "voice/SUZ03A_DAR0004.ogg"
    "至" "「所以铃羽叫我爸爸也可以哦？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0024"
    $ current_voice = "voice/SUZ03A_SUZ0024.ogg"
    "铃羽" "「爸爸……感觉有些害羞，叫父亲可以吗？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0005"
    $ current_voice = "voice/SUZ03A_DAR0005.ogg"
    "至" "「嗯，这也不错」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0025"
    $ current_voice = "voice/SUZ03A_SUZ0025.ogg"
    "铃羽" "「那，父亲，抱歉啊，把才刚刚睡着的你吵醒。你昨晚通宵工作了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0006"
    $ current_voice = "voice/SUZ03A_DAR0006.ogg"
    "至" "「没有。修理工作本身基本都是小幽灵之一在做」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0026"
    $ current_voice = "voice/SUZ03A_SUZ0026.ogg"
    "铃羽" "「才不是呢。另一个我说父亲十分努力，因此帮了很大的忙。是吧？」"
    window hide





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") at right_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0027"
    $ current_voice="voice/SUZ03A_SUZ0027.ogg"
    "铃羽β" "「能不能帮我告诉他“是的”？」"
    window hide



    hide lh5  with dissolve
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0028"
    $ current_voice = "voice/SUZ03A_SUZ0028.ogg"
    "铃羽" "「她说是的」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0007"
    $ current_voice = "voice/SUZ03A_DAR0007.ogg"
    "至" "「真的？那我就高兴了」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0008"
    $ current_voice = "voice/SUZ03A_DAR0008.ogg"
    "至" "「但是实际上，只是在说话而已。而且所说的话有一半以上都不知道是什么意思」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0029"
    $ current_voice = "voice/SUZ03A_SUZ0029.ogg"
    "铃羽" "「这也没办法呀。虽然这个时间机器是父亲制作出来的，但是在很遥远的未来制作出来的」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0009"
    $ current_voice = "voice/SUZ03A_DAR0009.ogg"
    "至" "「话虽这么说……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0030"
    $ current_voice = "voice/SUZ03A_SUZ0030.ogg"
    "铃羽" "「你有什么在意的事情吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM19"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0010"
    $ current_voice = "voice/SUZ03A_DAR0010.ogg"
    "至" "「我觉得有点奇怪啊，这台时间机器，是从什么地方来的？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0031"
    $ current_voice = "voice/SUZ03A_SUZ0031.ogg"
    "铃羽" "「从未来来的啊。２０３６年」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0011"
    $ current_voice = "voice/SUZ03A_DAR0011.ogg"
    "至" "「不，不是这个问题。我是问制作这台时间机器的技术是从什么地方来的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0032"
    $ current_voice = "voice/SUZ03A_SUZ0032.ogg"
    "铃羽" "「诶？什么意思？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0012"
    $ current_voice = "voice/SUZ03A_DAR0012.ogg"
    "至" "「如果是因为以电话微波炉技术为蓝本，让未来的我制作成了时间机器就没问题了，但难道没可能是因为我像现在这样修理了时间机器吗？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0013"
    $ current_voice = "voice/SUZ03A_DAR0013.ogg"
    "至" "「那也就是说，并不是我在未来制作完成了时间机器，而是将这台时间机器再现而已」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0014"
    $ current_voice = "voice/SUZ03A_DAR0014.ogg"
    "至" "「但是成为一切的根本的这台时间机器，就是我在未来再现出来的时间机器啊？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0015"
    $ current_voice = "voice/SUZ03A_DAR0015.ogg"
    "至" "「这样的话，这台时间机器是谁最早完成的？ 想到这个问题我晚上都睡不着觉了，实在是个难题啊」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0016"
    $ current_voice = "voice/SUZ03A_DAR0016.ogg"
    "至" "「哎呀，虽然这不是睡到刚才的家伙应该说的话」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0033"
    $ current_voice = "voice/SUZ03A_SUZ0033.ogg"
    "铃羽" "「……的确，原因和结果成了封闭的环」"
    "如果只是使用时间机器，应该不会改变能眼前的这条世界线。"
    "也就是说父亲在这个时间点，也就是２０１０年时，原本就在修理时间机器……。"
    "但是，如果这样的话，那就跟父亲所说的一样，因为在修理时看见了时间机器，所以在２０３６年制造了出来……。"
    "不过我来这里后的所作所为，以及所出现的地方都很引人注目，所以也有可能让世界线稍微产生了变化。"
    "并且这个变化，我跟父亲都无法意识到。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0017"
    $ current_voice = "voice/SUZ03A_DAR0017.ogg"
    "至" "「还是说世界线不同没有导致矛盾？在最初没有时间机器到来的世界线中，我凭自己的力量完成时间机器的？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0034"
    $ current_voice = "voice/SUZ03A_SUZ0034.ogg"
    "铃羽" "「大概是吧。因为父亲以前没有告诉我这些事」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0018"
    $ current_voice = "voice/SUZ03A_DAR0018.ogg"
    "至" "「这样啊。铃羽没有见过我吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0035"
    $ current_voice = "voice/SUZ03A_SUZ0035.ogg"
    "铃羽" "「嗯。因为父亲向ＳＥＲＮ隐藏了自己的存在」"
    "所以我见到现在年轻时的父亲，也没认出来。"
    "多亏了那两个幽灵才认出来的。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB02"),"True","lh/DAR_AMB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0019"
    $ current_voice = "voice/SUZ03A_DAR0019.ogg"
    "至" "「抱歉，铃羽」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0036"
    $ current_voice = "voice/SUZ03A_SUZ0036.ogg"
    "铃羽" "「诶？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0020"
    $ current_voice = "voice/SUZ03A_DAR0020.ogg"
    "至" "「好像我让铃羽感到寂寞了，虽然是未来的我做的」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0021"
    $ current_voice = "voice/SUZ03A_DAR0021.ogg"
    "至" "「也许在被ＳＥＲＮ支配的未来中是无可奈何的事情，但是将女儿扔在一边不管，而埋头于研究中，不是父母该做的事情吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0037"
    $ current_voice = "voice/SUZ03A_SUZ0037.ogg"
    "铃羽" "「没有。我并没有埋怨父亲」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0038"
    $ current_voice = "voice/SUZ03A_SUZ0038.ogg"
    "铃羽" "「我反而很尊敬他。因为父亲留给了我能改变世界的唯一希望」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0039"
    $ current_voice = "voice/SUZ03A_SUZ0039.ogg"
    "铃羽" "「这点要远远比有个会对我温柔的父亲要自豪」"
    "这是真心的。"
    "并不是说不希望有个温柔的父亲。"
    "但是在我生活的未来，不允许这样的事情发生。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0040"
    $ current_voice = "voice/SUZ03A_SUZ0040.ogg"
    "铃羽" "「所以父亲不用道歉」"
    "父亲所做的是正确的。"
    "如果父亲不跟我保持距离，就会被ＳＥＲＮ发现，从而失去改变过去的机会。"
    "父亲只是做了该做的事情。"
    "做了迫不得已该做的事情。"
    "所以，我觉得父亲是一个理性并且坚强的人。"
    "是个为了改变未来而放弃自己人生的伟大人物。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0022"
    $ current_voice = "voice/SUZ03A_DAR0022.ogg"
    "至" "「……铃羽」"
    "但是眼前的父亲与自己想象中的不同，是个有着更多人情味的人。"
    "会想象出自己在未来做过的事而向我道歉。"
    "他就是个这么温柔的人。"
    "如此温柔的人被迫不顾我跟母亲，只埋头于时间机器的研究之中。"
    "我想最伤心的人是他才对吧。"
    "比起自己不能见到父亲。"
    "父亲不能见到我的话。"
    "会更加的痛心吧。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0041"
    $ current_voice = "voice/SUZ03A_SUZ0041.ogg"
    "铃羽" "「我丝毫都没有埋怨过父亲」"
    "这是真心的。"
    "所以不希望父亲露出痛苦的表情。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0023"
    $ current_voice = "voice/SUZ03A_DAR0023.ogg"
    "至" "「但是……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0042"
    $ current_voice = "voice/SUZ03A_SUZ0042.ogg"
    "铃羽" "「呐，父亲，我有事情要拜托你」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0024"
    $ current_voice = "voice/SUZ03A_DAR0024.ogg"
    "至" "「嗯？拜托？只要我能做到什么都可以」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0043"
    $ current_voice = "voice/SUZ03A_SUZ0043.ogg"
    "铃羽" "「我希望父亲带我去秋叶原逛逛」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0025"
    $ current_voice = "voice/SUZ03A_DAR0025.ogg"
    "至" "「……只是这样就可以了吗？」"
    "想要与父亲一起，走在父亲最喜欢的街道上。"
    "虽然父亲说「只是这样」，但是对我来说，已经是极大的奢侈了。"
    "但如果我说出这是极大的奢侈，父亲又会露出难过的表情。"
    "所以我也装作一副很平常的样子。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0044"
    $ current_voice = "voice/SUZ03A_SUZ0044.ogg"
    "铃羽" "「嗯。我「只是这样」就可以了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB01"),"True","lh/DAR_AMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0026"
    $ current_voice = "voice/SUZ03A_DAR0026.ogg"
    "至" "「那就这么做吧」"
    "然后父亲笑了。"
    "也许他已经发现了我没有说出口的事情。"
    "但还是笑了。"
    "父亲就是这样温柔的人。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0027"
    $ current_voice = "voice/SUZ03A_DAR0027.ogg"
    "至" "「话虽这么说，但之前一直在炎热的地方工作，如果不去洗澡更衣，会很臭吧笑」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0045"
    $ current_voice = "voice/SUZ03A_SUZ0045.ogg"
    "铃羽" "「不用现在带我去也可以。况且，父亲还没有睡觉」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0028"
    $ current_voice = "voice/SUZ03A_DAR0028.ogg"
    "至" "「睡觉还是回实验室睡比较好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0046"
    $ current_voice = "voice/SUZ03A_SUZ0046.ogg"
    "铃羽" "「那就回实验室洗澡休息吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0029"
    $ current_voice = "voice/SUZ03A_DAR0029.ogg"
    "至" "「这样的话，父，父，父亲我有一个提议」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0047"
    $ current_voice = "voice/SUZ03A_SUZ0047.ogg"
    "铃羽" "「什么？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0030"
    $ current_voice = "voice/SUZ03A_DAR0030.ogg"
    "至" "「要，要不要跟父亲一起洗澡？」"
    "父亲一副认真的表情这样问我。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0048"
    $ current_voice = "voice/SUZ03A_SUZ0048.ogg"
    "铃羽" "「跟父亲一起洗澡吗」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0031"
    $ current_voice = "voice/SUZ03A_DAR0031.ogg"
    "至" "「……不，不行吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0049"
    $ current_voice = "voice/SUZ03A_SUZ0049.ogg"
    "铃羽" "「不是。可以。我也很久没有洗澡了」"
    "因为是夏天，所以在公园的水管下冲冲就行了，但是既然可以洗淋浴，我就想去洗淋浴了。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG02A1")

    play se "SGSE047L" loop

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0032"
    $ current_voice = "voice/SUZ03A_DAR0032.ogg"
    "至" "「铃羽！快点走吧！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0050"
    $ current_voice = "voice/SUZ03A_SUZ0050.ogg"
    "铃羽" "「还是算了吧。我等父亲洗完再洗」"
    "让我担心的是实验室的浴室不够大。"
    "两个女孩子的话能够一起进去，但如果是父亲跟我的话，就有一点小了。"
    "我觉得两人勉强挤进去洗澡会很痛苦，但是父亲好像不是这么想的。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0033"
    $ current_voice = "voice/SUZ03A_DAR0033.ogg"
    "至" "「父亲我，心跳不已地全裸待机中哦。话说我是很正常地在全裸，有什么问题吗？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0034"
    $ current_voice = "voice/SUZ03A_DAR0034.ogg"
    "至" "「说到全裸，吊环广告上有全裸入浴照片对吧，我一直在想既然是入浴照片，常理来想应该是全裸的才对吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0051"
    $ current_voice = "voice/SUZ03A_SUZ0051.ogg"
    "铃羽" "「吊环广告是什么？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0035"
    $ current_voice = "voice/SUZ03A_DAR0035.ogg"
    "至" "「就是电车中吊环扶手上的广告」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0052"
    $ current_voice = "voice/SUZ03A_SUZ0052.ogg"
    "铃羽" "「电车中的广告…… ？」"
    "即使解释了我也想象不到。"
    "因为平时都是骑自行车的，所以电车里的东西，我并不是很清楚。"
    "也许非常小的时候与母亲一起坐过，但是已经不记得了。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0036"
    $ current_voice = "voice/SUZ03A_DAR0036.ogg"
    "至" "「话就说到这里了，铃羽也快点进来啊。帮我搓背，父亲我会非常高兴的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0053"
    $ current_voice = "voice/SUZ03A_SUZ0053.ogg"
    "铃羽" "「那，说不定会有些挤哦……」"
    "太跟父亲客气反而不好，所以我又同意了。"
    "正好想脱衣服时。"

    hide lh8 

    $ loadBG(0,"BG01A")
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA05"),"True","lh/CRS_ASA05a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)








    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play se "SGSE024"










    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0000"
    $ current_voice = "voice/SUZ03A_CRS0000.ogg"
    "红莉栖" "「哈喽……诶，你在干什么？」"


    "就在我脱下上衣的时候，牧濑红莉栖来到了实验室中。"
    "看见半裸的我，露出惊讶的表情。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0054"
    $ current_voice = "voice/SUZ03A_SUZ0054.ogg"
    "铃羽" "「那个……我想跟父亲一起洗澡」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0001"
    $ current_voice = "voice/SUZ03A_CRS0001.ogg"
    "红莉栖" "「啊啊，洗澡啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0055"
    $ current_voice = "voice/SUZ03A_SUZ0055.ogg"
    "铃羽" "「我不能随便使用浴室吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0002"
    $ current_voice = "voice/SUZ03A_CRS0002.ogg"
    "红莉栖" "「这倒不是。阿万音小姐也是实验员……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA03"),"True","lh/CRS_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM10"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0003"
    $ current_voice = "voice/SUZ03A_CRS0003.ogg"
    "红莉栖" "「诶，你刚刚说父亲！ ？父亲指的是桥田吧！ ？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0056"
    $ current_voice = "voice/SUZ03A_SUZ0056.ogg"
    "铃羽" "「嗯。父亲因为修理时间机器而留了很多的汗」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0004"
    $ current_voice = "voice/SUZ03A_CRS0004.ogg"
    "红莉栖" "「我问的是为什么要一起洗澡！ ？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0057"
    $ current_voice = "voice/SUZ03A_SUZ0057.ogg"
    "铃羽" "「我想要帮他擦背」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0005"
    $ current_voice = "voice/SUZ03A_CRS0005.ogg"
    "红莉栖" "「……我明白你的想法」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0006"
    $ current_voice = "voice/SUZ03A_CRS0006.ogg"
    "红莉栖" "「重点在于是谁提出这个问题的。根据提出者的不同，会决定这事是否是犯罪。谁提出来的？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0058"
    $ current_voice = "voice/SUZ03A_SUZ0058.ogg"
    "铃羽" "「父亲提出来的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0007"
    $ current_voice = "voice/SUZ03A_CRS0007.ogg"
    "红莉栖" "「这个变态……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB03"),"True","lh/CRS_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0008"
    $ current_voice = "voice/SUZ03A_CRS0008.ogg"
    "红莉栖" "「混蛋桥田，对如此天真的女儿……」"
    window hide


    $ loadBG(2,"BG02A1")



    "牧濑红莉栖一边小声地说着一边迅速地走向浴室方向。"
    "虽然不清楚是怎么回事，但她看起来似乎非常生气。"
    play se "SGSE119"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0009"
    $ current_voice = "voice/SUZ03A_CRS0009.ogg"
    "红莉栖" "「桥田！你分不清楚什么该做什么不该做吗！竟然利用阿万音小姐对现代常识的不熟悉，趁机让她跟你一起洗澡？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0010"
    $ current_voice = "voice/SUZ03A_CRS0010.ogg"
    "红莉栖" "「你这个变态！不知廉耻！我绝对不会让阿万音小姐进去的！」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0037"
    $ current_voice = "voice/SUZ03A_DAR0037.ogg"
    "至" "「牧，牧濑氏！？怎么这个时间来这里了……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0059"
    $ current_voice = "voice/SUZ03A_SUZ0059.ogg"
    "铃羽" "「牧濑红莉栖为什么生气？」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0011"
    $ current_voice = "voice/SUZ03A_CRS0011.ogg"
    "红莉栖" "「啊……。就是因为阿万音小姐不知道我为什么生气才让我如此生气」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0060"
    $ current_voice = "voice/SUZ03A_SUZ0060.ogg"
    "铃羽" "「如果是因为我不知道造成的，那不是该骂我吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0012"
    $ current_voice = "voice/SUZ03A_CRS0012.ogg"
    "红莉栖" "「正确来说，正是因为桥田利用你的无知，让你跟他一起洗澡这点，让我很生气」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0061"
    $ current_voice = "voice/SUZ03A_SUZ0061.ogg"
    "铃羽" "「一起洗澡是不好的事情吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB09"),"True","lh/CRS_AMB09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0013"
    $ current_voice = "voice/SUZ03A_CRS0013.ogg"
    "红莉栖" "「父女一起洗澡，可以倒是可以，不过最多只到小学毕业为止，常识来看的话」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0014"
    $ current_voice = "voice/SUZ03A_CRS0014.ogg"
    "红莉栖" "「你现在多少岁了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0062"
    $ current_voice = "voice/SUZ03A_SUZ0062.ogg"
    "铃羽" "「虽说已经１８岁了」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0015"
    $ current_voice = "voice/SUZ03A_CRS0015.ogg"
    "红莉栖" "「小学毕业的人是几岁？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0063"
    $ current_voice = "voice/SUZ03A_SUZ0063.ogg"
    "铃羽" "「……几岁来着」"
    "并不是我在装傻，而是一时间想不起来。"
    "因为与２０１０相关的知识里并没有学过这个。"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0016"
    $ current_voice = "voice/SUZ03A_CRS0016.ogg"
    "红莉栖" "「根据国家文化不同年龄也会不同，在这个国家是１２岁」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0064"
    $ current_voice = "voice/SUZ03A_SUZ0064.ogg"
    "铃羽" "「这样啊。我记下来」"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB03"),"True","lh/CRS_AMB03a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)








    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0017"
    $ current_voice = "voice/SUZ03A_CRS0017.ogg"
    "红莉栖" "「没错，你记着……不是啊。我要说的是１８岁是已经不能一起洗澡的年龄了」"


    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0018"
    $ current_voice = "voice/SUZ03A_CRS0018.ogg"
    "红莉栖" "「而且父亲也是未来才会成为父亲哦，现在只是个１９岁的禽兽啊？跟这种人一起洗澡简直不能想象！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0065"
    $ current_voice = "voice/SUZ03A_SUZ0065.ogg"
    "铃羽" "「禽兽……父亲吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0019"
    $ current_voice = "voice/SUZ03A_CRS0019.ogg"
    "红莉栖" "「没错。而且是个二次元与三次元都可以的超级变态！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0066"
    $ current_voice = "voice/SUZ03A_SUZ0066.ogg"
    "铃羽" "「……也就是说，在这个时代，我跟父亲一起洗澡是不好的事情」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0020"
    $ current_voice = "voice/SUZ03A_CRS0020.ogg"
    "红莉栖" "「在未来像你这么大年纪的男女一起洗澡，不也是不可以的吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0067"
    $ current_voice = "voice/SUZ03A_SUZ0067.ogg"
    "铃羽" "「因为我是战士。没有时间去顾及男女间的差异」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0021"
    $ current_voice = "voice/SUZ03A_CRS0021.ogg"
    "红莉栖" "「……这，这样啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0068"
    $ current_voice = "voice/SUZ03A_SUZ0068.ogg"
    "铃羽" "「而且小时候没有机会与父亲一起洗澡，想要尝试一次」"
    "牧濑红莉栖说这种事在成为初中生之后就不能再做了。"
    "但对我来说，别说不能再做了，我连一次都没有过。"
    "既没有与父亲一起洗过澡，而且以后大概也不会有机会了。"
    "因为父亲一直都不在身边，而且２０３６年就已经死了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0022"
    $ current_voice = "voice/SUZ03A_CRS0022.ogg"
    "红莉栖" "「这个……也许是这样的……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0069"
    $ current_voice = "voice/SUZ03A_SUZ0069.ogg"
    "铃羽" "「牧濑红莉栖。我知道与父亲一起洗澡并不是什么好事」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0070"
    $ current_voice = "voice/SUZ03A_SUZ0070.ogg"
    "铃羽" "「但是，这是绝对不能容许的事情吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0023"
    $ current_voice = "voice/SUZ03A_CRS0023.ogg"
    "红莉栖" "「绝对不能容许……也不是那样……如果双方都同意的话，应该不算是犯罪吧……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0071"
    $ current_voice = "voice/SUZ03A_SUZ0071.ogg"
    "铃羽" "「那么，现在你能不能放我们一马？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0024"
    $ current_voice = "voice/SUZ03A_CRS0024.ogg"
    "红莉栖" "「……阿万音小姐。我明白你的心情。我并不是想要阻止你想向父亲撒娇的心情」"
    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0072"
    $ current_voice = "voice/SUZ03A_SUZ0072.ogg"
    "铃羽" "「那么」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0025"
    $ current_voice = "voice/SUZ03A_CRS0025.ogg"
    "红莉栖" "「但是不行！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0073"
    $ current_voice = "voice/SUZ03A_SUZ0073.ogg"
    "铃羽" "「！？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0026"
    $ current_voice = "voice/SUZ03A_CRS0026.ogg"
    "红莉栖" "「让那个变态与18岁的女孩子一起洗澡，我的良心不能允许这种事情发生！绝对不能允许！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0074"
    $ current_voice = "voice/SUZ03A_SUZ0074.ogg"
    "铃羽" "「……无论如何都不行吗？」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0027"
    $ current_voice = "voice/SUZ03A_CRS0027.ogg"
    "红莉栖" "「无论如何都不行」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0075"
    $ current_voice = "voice/SUZ03A_SUZ0075.ogg"
    "铃羽" "「这样啊……」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0028"
    $ current_voice = "voice/SUZ03A_CRS0028.ogg"
    "红莉栖" "「做些其他的事情吧！如果不是能让桥田得逞的事的话，我也不会反对」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0029"
    $ current_voice = "voice/SUZ03A_CRS0029.ogg"
    "红莉栖" "「……我，管太多了吧。但是这个是作为朋友的忠告」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0030"
    $ current_voice = "voice/SUZ03A_CRS0030.ogg"
    "红莉栖" "「可以断言的是――」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0031"
    $ current_voice = "voice/SUZ03A_CRS0031.ogg"
    "红莉栖" "「现在１９岁的桥田，就只是个变态而已」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0076"
    $ current_voice = "voice/SUZ03A_SUZ0076.ogg"
    "铃羽" "「这，这样啊」"
    "牧濑红莉栖双眼充血说话的样子，让身为战士的我都有些害怕。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0077"
    $ current_voice = "voice/SUZ03A_SUZ0077.ogg"
    "铃羽" "「最后，我打算让父亲带我逛秋叶原，这也不行吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0032"
    $ current_voice = "voice/SUZ03A_CRS0032.ogg"
    "红莉栖" "「这个就没有问题。是呢，只是挽手这种程度的话，也不会让那家伙太得逞」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0078"
    $ current_voice = "voice/SUZ03A_SUZ0078.ogg"
    "铃羽" "「嗯。知道了。可以挽手」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0033"
    $ current_voice = "voice/SUZ03A_CRS0033.ogg"
    "红莉栖" "「再进一步就不行了！无论他说什么都要拒绝！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0079"
    $ current_voice = "voice/SUZ03A_SUZ0079.ogg"
    "铃羽" "「……嗯」"
    "我明白牧濑红莉栖是为我着想。"
    "所以我也找她商量了一下。"
    play se "SGSE046"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0038"
    $ current_voice = "voice/SUZ03A_DAR0038.ogg"
    "至" "「那个……牧濑氏现在在那里，我就这样出去的话，大概会见到地狱吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA09"),"True","lh/CRS_AMA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0034"
    $ current_voice = "voice/SUZ03A_CRS0034.ogg"
    "红莉栖" "「没，没错」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0039"
    $ current_voice = "voice/SUZ03A_DAR0039.ogg"
    "至" "「不过我刚才想象了一下那个场面，感觉也许我会抛弃一切去尝试一下」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB03"),"True","lh/CRS_AMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0035"
    $ current_voice = "voice/SUZ03A_CRS0035.ogg"
    "红莉栖" "「你再洗久点吧，你这个变态！」"
    hide screen phoneSD1
    window hide

    stop bgm 

    stop se



    $ loadBG(0,"BG13A2")

    play bgm "FDBGM02"
    show screen phonebtn
    show screen phoneSD1
    "随后，冈部伦太郎也来了实验室，父亲躺在沙发上大声打呼噜，我离开实验室，稍微去打发一下时间。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0080"
    $ current_voice = "voice/SUZ03A_SUZ0080.ogg"
    "铃羽" "「在父亲醒来之前，该做什么呢」"
    "我让父亲在醒来后联系我。"
    "现在也不想在这段时间内在秋叶原中晃来晃去，也没有什么特别想做的事情。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0081"
    $ current_voice="voice/SUZ03A_SUZ0081.ogg"
    "铃羽ω" "「难得有时间，改变一下服装如何？」"
    "到达车站的时候，ω说了奇怪的话。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0082"
    $ current_voice = "voice/SUZ03A_SUZ0082.ogg"
    "铃羽" "「改变一下是指？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0083"
    $ current_voice="voice/SUZ03A_SUZ0083.ogg"
    "铃羽ω" "「虽然对方是父亲，但是也是跟约会差不多的事情吧？感觉这种场合穿运动服不太合适」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0084"
    $ current_voice = "voice/SUZ03A_SUZ0084.ogg"
    "铃羽" "「运动服，不行吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB01"),"True","lh/SUZ_DMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0085"
    $ current_voice="voice/SUZ03A_SUZ0085.ogg"
    "铃羽ω" "「不行吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0086"
    $ current_voice = "voice/SUZ03A_SUZ0086.ogg"
    "铃羽" "「别看它这样，这可是７０年代的古董品哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA06"),"True","lh/SUZ_DMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0087"
    $ current_voice="voice/SUZ03A_SUZ0087.ogg"
    "铃羽ω" "「就是件旧衣服吧」"
    "运动服虽然是运动服但却不是普通的运动服。想让ω明白这点，但是她却完全不听。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0088"
    $ current_voice="voice/SUZ03A_SUZ0088.ogg"
    "铃羽β" "「话虽这么说，但就是个变装道具而已。为了变得像７０年代的人」"
    "这次β似乎也不是站在我这边的了。"
    hide lh6  with dissolve
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0089"
    $ current_voice = "voice/SUZ03A_SUZ0089.ogg"
    "铃羽" "「呜呜」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0090"
    $ current_voice="voice/SUZ03A_SUZ0090.ogg"
    "铃羽ω" "「你的材质也不算差，还是打扮漂亮点比较好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0091"
    $ current_voice = "voice/SUZ03A_SUZ0091.ogg"
    "铃羽" "「这是你说出来的话吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0092"
    $ current_voice="voice/SUZ03A_SUZ0092.ogg"
    "铃羽ω" "「我说很奇怪吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0093"
    $ current_voice = "voice/SUZ03A_SUZ0093.ogg"
    "铃羽" "「相当奇怪吧」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0094"
    $ current_voice="voice/SUZ03A_SUZ0094.ogg"
    "铃羽ω" "「哪里奇怪？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0095"
    $ current_voice = "voice/SUZ03A_SUZ0095.ogg"
    "铃羽" "「这就是所谓的自明」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMC01"),"True","lh/SUZ_DMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0096"
    $ current_voice="voice/SUZ03A_SUZ0096.ogg"
    "铃羽ω" "「又说这种话？」"
    "ω一脸不开心的表情。"
    "一听到有点难的词语，ω就会皱眉。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0097"
    $ current_voice="voice/SUZ03A_SUZ0097.ogg"
    "铃羽ω" "「总之我想说的是，父亲不是不明白运动服的好坏么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0098"
    $ current_voice = "voice/SUZ03A_SUZ0098.ogg"
    "铃羽" "「父亲不知道吗」"
    "这个指责真是恰如其分。"
    "父亲总是穿同样的衣服，似乎不像是懂流行的人。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0099"
    $ current_voice="voice/SUZ03A_SUZ0099.ogg"
    "铃羽ω" "「啊，但是好像喜欢紧身裤」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0100"
    $ current_voice = "voice/SUZ03A_SUZ0100.ogg"
    "铃羽" "「是吗？」"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_CRS01_01"]

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0101"
    $ current_voice="voice/SUZ03A_SUZ0101.ogg"
    "铃羽ω" "「他好几次都说过『紧身裤真好啊』这种话」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0102"
    $ current_voice = "voice/SUZ03A_SUZ0102.ogg"
    "铃羽" "「那么再多展示一下紧身裤较好？」"
    call CHECK_RM_RECEIVE
    "我试着将运动服的下摆稍微往上提了提，但是只感觉有些奇怪。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0103"
    $ current_voice="voice/SUZ03A_SUZ0103.ogg"
    "铃羽ω" "「我觉得还是穿让人明显感觉到可爱的衣服比较好」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0104"
    $ current_voice = "voice/SUZ03A_SUZ0104.ogg"
    "铃羽" "「我没有那种衣服，而且不知道穿什么才好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0105"
    $ current_voice="voice/SUZ03A_SUZ0105.ogg"
    "铃羽ω" "「让我来帮你搭配。所以去卖那种衣服的店吧」"

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0106"
    $ current_voice = "voice/SUZ03A_SUZ0106.ogg"
    "铃羽" "「服装店我也不是很清楚。原本我就没打算来２０１０年」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0107"
    $ current_voice="voice/SUZ03A_SUZ0107.ogg"
    "铃羽ω" "「如果这个时代也有『４Ｓｔｙｌｅｓ』这种店就好了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0108"
    $ current_voice = "voice/SUZ03A_SUZ0108.ogg"
    "铃羽" "「佛思戴鲁姿？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0109"
    $ current_voice="voice/SUZ03A_SUZ0109.ogg"
    "铃羽ω" "「是我喜欢的品牌。涉谷有店，不过现在时间和世界都不同呢。也许２０１０年没有这间店」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0110"
    $ current_voice = "voice/SUZ03A_SUZ0110.ogg"
    "铃羽" "「涉谷吗……对第一次尝试来说有点远呢」"
    "我现在正在确认车站路线图。"
    "涉谷在叫做山手线的环形线上，正好在秋叶原的另一面。"
    "在２３区中的西边。"
    "骑自行车去单程也只需要３０分～１小时。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0111"
    $ current_voice="voice/SUZ03A_SUZ0111.ogg"
    "铃羽ω" "「不要浪费时间，总之还是坐电车去吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0112"
    $ current_voice = "voice/SUZ03A_SUZ0112.ogg"
    "铃羽" "「坐电车去？不是自行车？」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0113"
    $ current_voice="voice/SUZ03A_SUZ0113.ogg"
    "铃羽ω" "「我们又不能骑自行车」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0114"
    $ current_voice = "voice/SUZ03A_SUZ0114.ogg"
    "铃羽" "「那样的话不要勉强自己去也行啊」"
    "原本我就对穿可爱的衣服就没有兴趣。"
    "况且根据不确定的情报而进行移动也很让人不爽。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB01"),"True","lh/SUZ_DMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0115"
    $ current_voice="voice/SUZ03A_SUZ0115.ogg"
    "铃羽ω" "「你怎么这么没有干劲，α呢？」"
    "就因为这样被ω责备了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0116"
    $ current_voice = "voice/SUZ03A_SUZ0116.ogg"
    "铃羽" "「父亲，喜欢紧身裤吧？所以保持这样子也不错……」"
    "试着辩驳了一下，但被ω给打断了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB02"),"True","lh/SUZ_DMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0117"
    $ current_voice="voice/SUZ03A_SUZ0117.ogg"
    "铃羽ω" "「α也想要父亲觉得自己可爱吧？」"
    "真是个直截了当的问题。"
    "被这么直接地问，感觉有些害羞。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0118"
    $ current_voice = "voice/SUZ03A_SUZ0118.ogg"
    "铃羽" "「……这个，倒是这样」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0119"
    $ current_voice="voice/SUZ03A_SUZ0119.ogg"
    "铃羽ω" "「所以就听我的！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0120"
    $ current_voice = "voice/SUZ03A_SUZ0120.ogg"
    "铃羽" "「嗯，嗯」"
    "那，首先从怎么坐电车开始……。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_CRS01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_CRS01_01"])

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"IBGX048")

    hide screen phonebtn
    show screen phoneSD1
    "随后就按着ω所说的去做了。"
    "按照她所说的方法搭乘电车，按照她所说的方法找店，按照她所说的方法买衣服。"
    window hide


    $ loadBG(2,"BG02A1")




    "正好买完衣服的时候，父亲打了电话来，我们回到了秋叶原。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ003A"]]["Check"]=True
    $ loadBG(0,"EV_SUZ003A")









    play bgm "BGM18"



    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0040"
    $ current_voice = "voice/SUZ03A_DAR0040.ogg"
    "至" "「喔喔！铃羽，怎么了穿这种衣服？虽然超级萌！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0121"
    $ current_voice = "voice/SUZ03A_SUZ0121.ogg"
    "铃羽" "「……幽灵说难得的机会。果然很奇怪吗？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0041"
    $ current_voice = "voice/SUZ03A_DAR0041.ogg"
    "至" "「没有没有，让铃羽穿这种衣服，小幽灵，真是明白我的喜好啊。ＧＪ！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0122"
    $ current_voice = "voice/SUZ03A_SUZ0122.ogg"
    "铃羽" "「在ω的世界线中的父亲，似乎过着普通的日子」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0123"
    $ current_voice="voice/SUZ03A_SUZ0123.ogg"
    "铃羽ω" "「不是ω是铃羽哦」"
    "因为很难说出口。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0042"
    $ current_voice = "voice/SUZ03A_DAR0042.ogg"
    "至" "「哇啊！也就是说我的性癖已经全部被掌握了，我明白了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0124"
    $ current_voice = "voice/SUZ03A_SUZ0124.ogg"
    "铃羽" "「性癖指的是爱好？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0043"
    $ current_voice = "voice/SUZ03A_DAR0043.ogg"
    "至" "「基本上是同一东西」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0125"
    $ current_voice = "voice/SUZ03A_SUZ0125.ogg"
    "铃羽" "「那就好」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0044"
    $ current_voice = "voice/SUZ03A_DAR0044.ogg"
    "至" "「话说，铃羽」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0126"
    $ current_voice = "voice/SUZ03A_SUZ0126.ogg"
    "铃羽" "「什么？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0045"
    $ current_voice = "voice/SUZ03A_DAR0045.ogg"
    "至" "「今天的你，非常的可爱哦！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0127"
    $ current_voice = "voice/SUZ03A_SUZ0127.ogg"
    "铃羽" "「……！？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0046"
    $ current_voice = "voice/SUZ03A_DAR0046.ogg"
    "至" "「……咦？难道你生气了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0128"
    $ current_voice = "voice/SUZ03A_SUZ0128.ogg"
    "铃羽" "「没有。因为我从没被这么说过，只是有些惊讶……」"
    "没错，从没有这么被说过。"
    "因为从我开始记事起，父亲就杳无音讯，所以被表扬的机会，真的一次都没有。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0129"
    $ current_voice="voice/SUZ03A_SUZ0129.ogg"
    "铃羽ω" "「果然按照我所说的没错吧？」"
    "所以我只能老实地同意ω所说的话。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0130"
    $ current_voice = "voice/SUZ03A_SUZ0130.ogg"
    "铃羽" "「嗯」"
    window hide

    stop bgm 



    $ loadBG(0,"BG16A3")

    play bgm "BGM05"
    show screen phonebtn
    show screen phoneSD1
    "接下来就真的是梦幻般的时间了。"
    "中午一起吃的牛肉饭，明明以前也跟父亲一起吃过，但是比那个时候的还要美味。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0131"
    $ current_voice = "voice/SUZ03A_SUZ0131.ogg"
    "铃羽" "「父亲，我可以牵你的手吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0047"
    $ current_voice = "voice/SUZ03A_DAR0047.ogg"
    "至" "「牵手？可以哦……话说对我来说，更进一步都ＯＫ哦」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0132"
    $ current_voice = "voice/SUZ03A_SUZ0132.ogg"
    "铃羽" "「哈哈。但是牧濑红莉栖警告过我，只能亲密到挽手」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0048"
    $ current_voice = "voice/SUZ03A_DAR0048.ogg"
    "至" "「这种事不说我怎么会知道」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0133"
    $ current_voice = "voice/SUZ03A_SUZ0133.ogg"
    "铃羽" "「这倒也是」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0049"
    $ current_voice = "voice/SUZ03A_DAR0049.ogg"
    "至" "「那么比牵手更进一步而，挽手怎样？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0134"
    $ current_voice = "voice/SUZ03A_SUZ0134.ogg"
    "铃羽" "「好啊」"
    "就这样父亲跟我挽手了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    play se "SGSE809"



    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0050"
    $ current_voice = "voice/SUZ03A_DAR0050.ogg"
    "至" "「哇啊！」"
    "父亲的手机响了。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0051"
    $ current_voice = "voice/SUZ03A_DAR0051.ogg"
    "至" "「哇，牧濑氏的短信」"
    play se "SGSE158"

    "父亲看过发来的短信后发出了惊讶的声音。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0052"
    $ current_voice = "voice/SUZ03A_DAR0052.ogg"
    "至" "「牧濑氏！你！在看着吧！」"
    "然后慌慌张张地望了望四周。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0135"
    $ current_voice = "voice/SUZ03A_SUZ0135.ogg"
    "铃羽" "「怎么了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0053"
    $ current_voice = "voice/SUZ03A_DAR0053.ogg"
    "至" "「牧濑氏发短信说『如果你认为不说出来就不会暴露的话我可会杀了你哦』」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0136"
    $ current_voice = "voice/SUZ03A_SUZ0136.ogg"
    "铃羽" "「……真是巧啊」"


    $ targetmailid = gc["ScriptMacros"]["FM_SUZ03A_RECV_CRS01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "正在这么想的时候，这次轮到我收短信了。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail






    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0137"
    $ current_voice = "voice/SUZ03A_SUZ0137.ogg"
    "铃羽" "「牧濑红莉栖，好像也想杀了我」"
    window hide
    call hide_phone

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0054"
    $ current_voice = "voice/SUZ03A_DAR0054.ogg"
    "至" "「我以前就这么觉得了，真是恐怖的女人……」"
    "透过与父亲挽在一起的手臂，得知父亲是真的在害怕。"
    "但是，我反而觉得有些放松。"
    "也许笑笑比较好。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0138"
    $ current_voice = "voice/SUZ03A_SUZ0138.ogg"
    "铃羽" "「这也是牧濑红莉栖的报复吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0055"
    $ current_voice = "voice/SUZ03A_DAR0055.ogg"
    "至" "「嗯？怎么回事？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0139"
    $ current_voice = "voice/SUZ03A_SUZ0139.ogg"
    "铃羽" "「我在未来曾企图杀掉牧濑红莉栖。她是被称为「时间机器之母」的人民公敌」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0140"
    $ current_voice = "voice/SUZ03A_SUZ0140.ogg"
    "铃羽" "「这件事昨天不是已经道歉了吗……那家伙，是很记仇的人吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0056"
    $ current_voice = "voice/SUZ03A_DAR0056.ogg"
    "至" "「而且，以前被冈伦指责同样的事情时，她反驳说「不是记仇，只是比其他人的记忆更好一点」」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0141"
    $ current_voice = "voice/SUZ03A_SUZ0141.ogg"
    "铃羽" "「哈哈哈。很像她会说的话呢」"

    stop bgm 
    "我被这件事弄笑了，父亲却没笑。"
    "突然陷入了沉默，低下了头。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0057"
    $ current_voice = "voice/SUZ03A_DAR0057.ogg"
    "至" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0142"
    $ current_voice = "voice/SUZ03A_SUZ0142.ogg"
    "铃羽" "「怎么了，父亲？我说了奇怪的话吗？」"
    "因为事情太过于突然让我无法得知理由。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0058"
    $ current_voice = "voice/SUZ03A_DAR0058.ogg"
    "至" "「没有，只是想起了一些事情……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0143"
    $ current_voice = "voice/SUZ03A_SUZ0143.ogg"
    "铃羽" "「想起了一些事情……」"
    "我搜索记忆，寻找父亲为什么会沉默的理由。"
    play bgm "FD2BGM05"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0144"
    $ current_voice = "voice/SUZ03A_SUZ0144.ogg"
    "铃羽" "「是时间机器……吧？」"
    "随后，问题立刻得到了解答。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0059"
    $ current_voice = "voice/SUZ03A_DAR0059.ogg"
    "至" "「嗯」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0145"
    $ current_voice = "voice/SUZ03A_SUZ0145.ogg"
    "铃羽" "「修理的时候是从β那里听说的吧」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0060"
    $ current_voice = "voice/SUZ03A_DAR0060.ogg"
    "至" "「嗯」"
    "他听到了什么，已经不用再次确认了。"
    "时间机器只会回到过去。"
    "也就是说我回到１９７５年的话，就不能回来的意思。"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_MAY02_01"]

    $ LR_RM_CHANCE=6

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0061"
    $ current_voice = "voice/SUZ03A_DAR0061.ogg"
    "至" "「今天，你打算跳回过去吧？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0146"
    $ current_voice = "voice/SUZ03A_SUZ0146.ogg"
    "铃羽" "「……你怎么知道的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0062"
    $ current_voice = "voice/SUZ03A_DAR0062.ogg"
    "至" "「因为，不是这样的话你不会让我带你逛秋叶原……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0147"
    $ current_voice = "voice/SUZ03A_SUZ0147.ogg"
    "铃羽" "「……真不愧是父亲」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0063"
    $ current_voice = "voice/SUZ03A_DAR0063.ogg"
    "至" "「铃羽一定要走吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0148"
    $ current_voice = "voice/SUZ03A_SUZ0148.ogg"
    "铃羽" "「……嗯。因为抵抗组织只有那一台时间机器」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0064"
    $ current_voice = "voice/SUZ03A_DAR0064.ogg"
    "至" "「那个，铃羽。能不能给我一点时间？」"


    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0149"
    $ current_voice = "voice/SUZ03A_SUZ0149.ogg"
    "铃羽" "「时间？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0065"
    $ current_voice = "voice/SUZ03A_DAR0065.ogg"
    "至" "「因为有时间机器，所以即便晚点出发也还是能到达１９７５年吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0150"
    $ current_voice = "voice/SUZ03A_SUZ0150.ogg"
    "铃羽" "「不是，并不是那么万能的东西。而且我在这里的话，说不定会引起致命的时间悖论」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0066"
    $ current_voice = "voice/SUZ03A_DAR0066.ogg"
    "至" "「不发生也说不定」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0151"
    $ current_voice = "voice/SUZ03A_SUZ0151.ogg"
    "铃羽" "「越在这里待的时间长，危险性就会越大。这点父亲也知道吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0152"
    $ current_voice = "voice/SUZ03A_SUZ0152.ogg"
    "铃羽" "「而且就算有时间又能做出什么？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0067"
    $ current_voice = "voice/SUZ03A_DAR0067.ogg"
    "至" "「我会完成时间机器！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0153"
    $ current_voice = "voice/SUZ03A_SUZ0153.ogg"
    "铃羽" "「完成？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0068"
    $ current_voice = "voice/SUZ03A_DAR0068.ogg"
    "至" "「我听说了哦。在小幽灵的世界线中存在能够去未来的时间机器。所以铃羽的时间机器也可以变得能去未来吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0154"
    $ current_voice = "voice/SUZ03A_SUZ0154.ogg"
    "铃羽" "「这个，大概办不到」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0069"
    $ current_voice = "voice/SUZ03A_DAR0069.ogg"
    "至" "「为什么？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0155"
    $ current_voice = "voice/SUZ03A_SUZ0155.ogg"
    "铃羽" "「在这条世界线上父亲没有造出能够去未来的时间机器。世界线会向着这个方向收缩」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0156"
    $ current_voice = "voice/SUZ03A_SUZ0156.ogg"
    "铃羽" "「无论这条时间线怎么变ＳＥＲＮ都会完成时间机器并独占它。唯一的例外就是父亲留下的这台时间机器」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0070"
    $ current_voice = "voice/SUZ03A_DAR0070.ogg"
    "至" "「但如果铃羽回到过去的话，就不能再见到大家了」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0071"
    $ current_voice = "voice/SUZ03A_DAR0071.ogg"
    "至" "「我，冈伦，牧濑氏，真由氏，小菲莉司，琉华氏，桐生氏……」"
    "父亲如同回忆一般一个个列举出大家的名字。"
    "我听到这些话，让我感觉更坚强了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0157"
    $ current_voice = "voice/SUZ03A_SUZ0157.ogg"
    "铃羽" "「马上就会见到了」"
    "我知道这是在骗人。"
    "回到过去的我不会再见到父亲他们。"
    "这点我已经知道了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0158"
    $ current_voice = "voice/SUZ03A_SUZ0158.ogg"
    "铃羽" "「因为是去过去哦？我回到过去，在那个时代生活。等我到了５０岁左右，就到了这个时代了吧？」"
    "但是这事情一定要说的十分肯定才行。"
    "要不然父亲会担心。"
    "如果知道不能再相见，父亲会阻止我的。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0072"
    $ current_voice = "voice/SUZ03A_DAR0072.ogg"
    "至" "「哦，嗯」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0159"
    $ current_voice = "voice/SUZ03A_SUZ0159.ogg"
    "铃羽" "「话说，说不定我们已经见过了哦？只是因为我没有说出名字，也许是父亲非常熟悉的人」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0073"
    $ current_voice = "voice/SUZ03A_DAR0073.ogg"
    "至" "「如果这个人是铃羽，为什么不说出名字？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0160"
    $ current_voice = "voice/SUZ03A_SUZ0160.ogg"
    "铃羽" "「因为见到过去的自己会产生时间悖论。如果我回去过去的话，这个时间的我就剩下一个人了。这样肯定会说出名字的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0161"
    $ current_voice = "voice/SUZ03A_SUZ0161.ogg"
    "铃羽" "「或者，因为我们现在这样在这里说话，因此在我跳回去之前就故意不出现了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0162"
    $ current_voice = "voice/SUZ03A_SUZ0162.ogg"
    "铃羽" "「阿万音铃羽就是这样的人。我都这样说了，不会有错吧，父亲？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0074"
    $ current_voice = "voice/SUZ03A_DAR0074.ogg"
    "至" "「嗯，嗯」"
    "为了要让父亲绝对的相信我的话。"
    "想要让他接受。"
    "但是连旁人都知道这是行不通的。"
    "歪理就只能是歪理。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0163"
    $ current_voice = "voice/SUZ03A_SUZ0163.ogg"
    "铃羽" "「父亲，真是温柔」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0075"
    $ current_voice = "voice/SUZ03A_DAR0075.ogg"
    "至" "「诶？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0164"
    $ current_voice = "voice/SUZ03A_SUZ0164.ogg"
    "铃羽" "「我原以为父亲是更加理性的人。可以说是理论派吧？ 能造出时间机器的人肯定很聪明，是个能直言不讳的人」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0165"
    $ current_voice = "voice/SUZ03A_SUZ0165.ogg"
    "铃羽" "「所以我觉得我是不是不像父亲。明明是反抗组织的战士，被交付狙击任务时，在关键的时候不能够扣下扳机」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0076"
    $ current_voice = "voice/SUZ03A_DAR0076.ogg"
    "至" "「你指的是牧濑氏吧？我觉得不刺杀她才是正确的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0166"
    $ current_voice = "voice/SUZ03A_SUZ0166.ogg"
    "铃羽" "「……嗯」"
    window hide


    $ loadBG(2,"IBGX048")



    "现在这样觉得了。"
    "没杀牧濑红莉栖真好。"
    "与牧濑红莉栖聊过后，明白并不是她的错。"
    "但是当时根本就不能想像这样的一天会到来。"
    hide screen phoneSD1
    window hide


    $ loadBG(3,"BG_CHI",trans=ImageDissolve(im.Scale("mask/mask01.png",1024,576),1))






    hide screen phonebtn
    "因为我的失误而导致作战失败了，让我失去了很多伙伴。"
    window hide



    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    "是我杀死了伙伴们。"
    window hide

    scene expression Solid("000000")  with fade

    $ loadBG(0,"BG_BLACK")

    "我一直是这么认为的。"
    "不能让事情就这样结束。"
    "所以我要回到过去。"
    "乘坐父亲留下的时间机器，为了得到ＩＢＮ５１００。"
    window hide


    $ loadBG(0,"BG40A")

    "可是，我却顺路来到了这个时代。"
    "将父亲抛弃了一切而留下来的时间机器，为自己而用。"
    "如果是父亲的话，肯定不会做这种多余的事情。"
    "我是这么认为的。"
    window hide


    $ loadBG(0,"BG16A3")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1

    stop bgm 
    "但是现在明白了。"
    "父亲早就知道了。"
    "知道我会来这里。"
    "所以父亲才会将时间机器交给我。"
    "父亲躲着ＳＥＲＮ而生，是为了将我送出去。"
    play bgm "FD2BGM09"
    "父亲早就知道了。"
    "我会这样与父亲见面。"
    "所以，肯定父亲他……"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0167"
    $ current_voice = "voice/SUZ03A_SUZ0167.ogg"
    "铃羽" "「但是现在我觉得我还是挺像父亲的」"
    "父亲不是生下来就是强人。"
    "是ＳＥＲＮ创造的世界让父亲变成了强人。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0077"
    $ current_voice = "voice/SUZ03A_DAR0077.ogg"
    "至" "「虽然不太明白，但是女儿像父亲不是常识么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0168"
    $ current_voice = "voice/SUZ03A_SUZ0168.ogg"
    "铃羽" "「所以，我要回到过去。就算父亲会阻止我」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0078"
    $ current_voice = "voice/SUZ03A_DAR0078.ogg"
    "至" "「嗯，嗯」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0169"
    $ current_voice = "voice/SUZ03A_SUZ0169.ogg"
    "铃羽" "「所以，今天在离别时就不要说这种伤感的话了吧」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ004A"]]["Check"]=True


    $ loadBG(2,"EV_SUZ004A")



    hide screen phonebtn
    "于是父亲就没有再谈到时间机器的事。"
    "我觉得他并不是被说服了。"
    "原本就没有能够说服他的话。"
    "但是父亲还一直保持着笑容。"
    "虽然偶然会有失败，但是一直还在保持着。"
    "果然父亲是温柔的人。"
    window hide



    $ loadBG(0,"BG05E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0170"
    $ current_voice = "voice/SUZ03A_SUZ0170.ogg"
    "铃羽" "「今天谢谢你，父亲」"
    "在逛完秋叶原回去的时候，天空被夕阳染红。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0079"
    $ current_voice = "voice/SUZ03A_DAR0079.ogg"
    "至" "「得了各种各样的好处，应该是我感谢你才对」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0171"
    $ current_voice = "voice/SUZ03A_SUZ0171.ogg"
    "铃羽" "「好处？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0080"
    $ current_voice = "voice/SUZ03A_DAR0080.ogg"
    "至" "「比如说，铃羽想不到胸挺大的，手肘透过衣服感觉到了」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0036"
    $ current_voice = "voice/SUZ03A_CRS0036.ogg"
    "红莉栖" "「稍微自重点，你这变态！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑红莉栖不知何时来了，瞪着父亲。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0037"
    $ current_voice = "voice/SUZ03A_CRS0037.ogg"
    "红莉栖" "「我还以为阿万音小姐会平安地回来呢，突然就性骚扰了，这怎么能让人容忍？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SAHSEN"])
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0081"
    $ current_voice = "voice/SUZ03A_DAR0081.ogg"
    "至" "「{color=#f00}对不起鸟{/color}」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0038"
    $ current_voice = "voice/SUZ03A_CRS0038.ogg"
    "红莉栖" "「阿万音小姐，还有没有做比挽手更深入的事情？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0172"
    $ current_voice = "voice/SUZ03A_SUZ0172.ogg"
    "铃羽" "「……嗯。大概没有做让牧濑红莉栖在意的事情」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0039"
    $ current_voice = "voice/SUZ03A_CRS0039.ogg"
    "红莉栖" "「那就是做了很多故意让我不会在意的事吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0173"
    $ current_voice = "voice/SUZ03A_SUZ0173.ogg"
    "铃羽" "「很温柔地对待我」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0040"
    $ current_voice = "voice/SUZ03A_CRS0040.ogg"
    "红莉栖" "「没有奇怪的含义？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0174"
    $ current_voice = "voice/SUZ03A_SUZ0174.ogg"
    "铃羽" "「没有奇怪的含义」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB05"),"True","lh/CRS_AMB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑红莉栖听了我的回答后，疑惑地看着父亲。"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0041"
    $ current_voice = "voice/SUZ03A_CRS0041.ogg"
    "红莉栖" "「真的没有奇怪的含义？」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0082"
    $ current_voice = "voice/SUZ03A_DAR0082.ogg"
    "至" "「我觉得没有」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0042"
    $ current_voice = "voice/SUZ03A_CRS0042.ogg"
    "红莉栖" "「那就好」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "接着牧濑红莉栖看向了我。"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0043"
    $ current_voice = "voice/SUZ03A_CRS0043.ogg"
    "红莉栖" "「…………」"
    "但是什么都没说。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0175"
    $ current_voice = "voice/SUZ03A_SUZ0175.ogg"
    "铃羽" "「什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0044"
    $ current_voice = "voice/SUZ03A_CRS0044.ogg"
    "红莉栖" "「没，没什么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0176"
    $ current_voice = "voice/SUZ03A_SUZ0176.ogg"
    "铃羽" "「你看起来想说什么」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0045"
    $ current_voice = "voice/SUZ03A_CRS0045.ogg"
    "红莉栖" "「我只是在想你有没有足够地被父亲宠爱呢，可不是因为担心你，也不是因为跟你在一起的是那个变态」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0177"
    $ current_voice = "voice/SUZ03A_SUZ0177.ogg"
    "铃羽" "「原来你在想这些啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0046"
    $ current_voice = "voice/SUZ03A_CRS0046.ogg"
    "红莉栖" "「不是啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0178"
    $ current_voice = "voice/SUZ03A_SUZ0178.ogg"
    "铃羽" "「已经得到足够宠爱了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0047"
    $ current_voice = "voice/SUZ03A_CRS0047.ogg"
    "红莉栖" "「没，没错。那样就好」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0179"
    $ current_voice = "voice/SUZ03A_SUZ0179.ogg"
    "铃羽" "「牧濑红莉栖，你真是好人」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0048"
    $ current_voice = "voice/SUZ03A_CRS0048.ogg"
    "红莉栖" "「我昨天就提醒过你了不要跟我说这种话……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0180"
    $ current_voice = "voice/SUZ03A_SUZ0180.ogg"
    "铃羽" "「我知道了这点真是太好了」"
    "但是，也许有一些迟了。"
    "如果我没有将她当成未来的她，如果能看待现在的她，就能够更早地明白。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC03"),"True","lh/CRS_AMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0049"
    $ current_voice = "voice/SUZ03A_CRS0049.ogg"
    "红莉栖" "「解开对我的误解也让我松了口气」"
    "牧濑红莉栖对着我笑了。"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0050"
    $ current_voice = "voice/SUZ03A_CRS0050.ogg"
    "红莉栖" "「今晚，就要走了吧？」"
    "突然问了个让人惊讶的问题。"
    play bgm "FD2BGM08"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0181"
    $ current_voice = "voice/SUZ03A_SUZ0181.ogg"
    "铃羽" "「……你怎么知道？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0051"
    $ current_voice = "voice/SUZ03A_CRS0051.ogg"
    "红莉栖" "「果然是这样」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0182"
    $ current_voice = "voice/SUZ03A_SUZ0182.ogg"
    "铃羽" "「瞎猜啊。不像凡事都讲道理的你会说的话呢」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0052"
    $ current_voice = "voice/SUZ03A_CRS0052.ogg"
    "红莉栖" "「面对会偷偷离开的人，没法等到证据搜集完全，这种事也是有的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0183"
    $ current_voice = "voice/SUZ03A_SUZ0183.ogg"
    "铃羽" "「是呢」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0053"
    $ current_voice = "voice/SUZ03A_CRS0053.ogg"
    "红莉栖" "「那个时间机器，只能跳回过去吧？」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "牧濑红莉栖说话时，我看向父亲。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0083"
    $ current_voice = "voice/SUZ03A_DAR0083.ogg"
    "至" "「…………」"
    "但是父亲只是无言地否定。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0054"
    $ current_voice = "voice/SUZ03A_CRS0054.ogg"
    "红莉栖" "「这也只是推论。如果回去后能够立刻回来的话，就不会跟这个桥田约会了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0184"
    $ current_voice = "voice/SUZ03A_SUZ0184.ogg"
    "铃羽" "「难道说你今天一整天，都在考虑我们的事情？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0055"
    $ current_voice = "voice/SUZ03A_CRS0055.ogg"
    "红莉栖" "「应，应该不是这样吧！我只要几秒钟就能猜到这种事情……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0185"
    $ current_voice = "voice/SUZ03A_SUZ0185.ogg"
    "铃羽" "「在想呢，一直」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0056"
    $ current_voice = "voice/SUZ03A_CRS0056.ogg"
    "红莉栖" "「也，也是，也可以这么说」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0186"
    $ current_voice = "voice/SUZ03A_SUZ0186.ogg"
    "铃羽" "「还有，你一直在看着我们吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0057"
    $ current_voice = "voice/SUZ03A_CRS0057.ogg"
    "红莉栖" "「倒是没有看着你们，要是回来得再晚一点的话，还想着要不要再发一条短信」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0058"
    $ current_voice = "voice/SUZ03A_CRS0058.ogg"
    "红莉栖" "「因为这两人是父女，如果变得亲密起来了话会很麻烦吧，一般来讲」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0187"
    $ current_voice = "voice/SUZ03A_SUZ0187.ogg"
    "铃羽" "「谢谢，牧濑红莉栖」"
    "我突然意识到我刚刚说出了没来这个时代的我绝对不会说出的话。"
    "我在感谢牧濑红莉栖。"
    "如果反抗组织的伙伴听见的话，会有怎样的表情呢。"
    "我不禁想象了这种不可能发生的事情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA09"),"True","lh/CRS_AMA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0059"
    $ current_voice = "voice/SUZ03A_CRS0059.ogg"
    "红莉栖" "「怎，怎么了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0188"
    $ current_voice = "voice/SUZ03A_SUZ0188.ogg"
    "铃羽" "「最后能见到你太好了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0060"
    $ current_voice = "voice/SUZ03A_CRS0060.ogg"
    "红莉栖" "「最后，你不去见冈部他们吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0189"
    $ current_voice = "voice/SUZ03A_SUZ0189.ogg"
    "铃羽" "「嗯，会让我有产生迟疑的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0061"
    $ current_voice = "voice/SUZ03A_CRS0061.ogg"
    "红莉栖" "「那就没办法了呢。冈部他们就由我来转达吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0190"
    $ current_voice = "voice/SUZ03A_SUZ0190.ogg"
    "铃羽" "「也许没有这个必要」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0062"
    $ current_voice = "voice/SUZ03A_CRS0062.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0191"
    $ current_voice = "voice/SUZ03A_SUZ0191.ogg"
    "铃羽" "「我只是去过去。在我离开了之后，回到过去的我就会立刻出现在大家面前的」"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0063"
    $ current_voice = "voice/SUZ03A_CRS0063.ogg"
    "红莉栖" "「这观点太过理想了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0064"
    $ current_voice = "voice/SUZ03A_CRS0064.ogg"
    "红莉栖" "「但是这种事，我并不讨厌」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0192"
    $ current_voice = "voice/SUZ03A_SUZ0192.ogg"
    "铃羽" "「短暂离别了哦，牧濑红莉栖」"
    "牧濑红莉栖说这是理想化的。"
    "但是，我知道这只是个谎言。"
    "回到过去的我已经死了。"
    "就算能够平安的再见，这条时间线也只有非常有限的时间了。如果我的任务成功了，过去和未来都会被再构成，连接至其他的世界线。"
    "不过我觉得这样也不错。"
    "就算是很短的是时间，就算是再构成时会消失的记忆。"
    "这样的相遇是确实存在过的。"
    $ stopvoc("CRS")
    play CRS "SUZ03A_CRS0065"
    $ current_voice = "voice/SUZ03A_CRS0065.ogg"
    "红莉栖" "「短暂的分别，阿万音小姐」"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA02"),"True","lh/DAR_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "听到这句话，我将视线转向父亲那边。"
    "牧濑红莉栖肯定也跟我一起看了过去。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0084"
    $ current_voice = "voice/SUZ03A_DAR0084.ogg"
    "至" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0193"
    $ current_voice = "voice/SUZ03A_SUZ0193.ogg"
    "铃羽" "「与父亲短暂的分离」"
    "再次对父亲说谎让我心痛。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0085"
    $ current_voice = "voice/SUZ03A_DAR0085.ogg"
    "至" "「嗯，嗯」"
    "也许父亲已经发现这条世界线将会消失。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0086"
    $ current_voice = "voice/SUZ03A_DAR0086.ogg"
    "至" "「铃羽，我最后说一句可以吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0194"
    $ current_voice = "voice/SUZ03A_SUZ0194.ogg"
    "铃羽" "「什么？」"
    "我已经做好他接下来的话是悲伤的话的准备了。"
    "今天我看到父亲已经很多次欲言又止了。"
    "但是。"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0087"
    $ current_voice = "voice/SUZ03A_DAR0087.ogg"
    "至" "「今天的铃羽也很可爱」"
    $ stopvoc("DAR")
    play DAR "SUZ03A_DAR0088"
    $ current_voice = "voice/SUZ03A_DAR0088.ogg"
    "至" "「但是父亲喜欢平时那样的铃羽啊啊啊啊啊！」"
    "父亲说出口的话跟我想像的完全不一样。"
    "别说伤心了，简直让我开心得不得了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0195"
    $ current_voice = "voice/SUZ03A_SUZ0195.ogg"
    "铃羽" "「没有任何烦恼真是太好了」"
    "像平时的自己最好了。"
    "在父亲最后的这番话下，我的踌躇全部消失了。"
    "不需要烦恼的并不是只有服装。"
    "我要像想像中的自己一样生活。"
    "这肯定是因为我是父亲的女儿。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG06N1")

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_OKA02_01"]

    $ LR_RM_CHANCE=0
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    show screen phonebtn
    show screen phoneSD1
    "β在进行最后的检查。"
    "弄坏的是我，修好的确是父亲与β。"
    "虽然我说过即使修不好我也不会怨恨，但是β不这么认为，她已经做好肯定会完成任务的觉悟了。"
    "确实是有军人的感觉。"
    "任何时候都会完成任务。"
    "也许不久前的我，会想要变得像她一样也说不定。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA06"),"True","lh/SUZ_DMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0196"
    $ current_voice="voice/SUZ03A_SUZ0196.ogg"
    "铃羽ω" "「这件衣服，我做了多余的事情吗？」"
    "然而另一个我却在担心完全不同的事情。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0197"
    $ current_voice = "voice/SUZ03A_SUZ0197.ogg"
    "铃羽" "「没有这回事。你帮了很大的忙」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0198"
    $ current_voice="voice/SUZ03A_SUZ0198.ogg"
    "铃羽ω" "「但是父亲说，平时那样的铃羽比较好……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0199"
    $ current_voice = "voice/SUZ03A_SUZ0199.ogg"
    "铃羽" "「如果是平时那样的我，会让我觉得害羞而无法挽手的，就是有种成为别人的感觉，才有勇气去做的」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0200"
    $ current_voice="voice/SUZ03A_SUZ0200.ogg"
    "铃羽ω" "「这样吗」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0201"
    $ current_voice = "voice/SUZ03A_SUZ0201.ogg"
    "铃羽" "「而且最后还被夸奖可爱了。所以要感谢你。我根本不知道怎么挑选可爱的衣服，说到底也不会想到去买衣服」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0202"
    $ current_voice="voice/SUZ03A_SUZ0202.ogg"
    "铃羽ω" "「那样就好」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_OKA02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_OKA02_01"])

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "在ω被我说服的时候，β来了。"
    "这或许不是偶然，她也许一直都在注意这边。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0203"
    $ current_voice="voice/SUZ03A_SUZ0203.ogg"
    "铃羽β" "「检查结束了，α」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0204"
    $ current_voice = "voice/SUZ03A_SUZ0204.ogg"
    "铃羽" "「嗯。谢谢，让你帮了我这么多」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0205"
    $ current_voice="voice/SUZ03A_SUZ0205.ogg"
    "铃羽β" "「不用。我只是做了该做的事情」"
    "随后，β一直看着我的脸。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0206"
    $ current_voice = "voice/SUZ03A_SUZ0206.ogg"
    "铃羽" "「什么？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0207"
    $ current_voice="voice/SUZ03A_SUZ0207.ogg"
    "铃羽β" "「我能提一个建议吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0208"
    $ current_voice = "voice/SUZ03A_SUZ0208.ogg"
    "铃羽" "「可以啊？」"
    "现在还会说些什么呢。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0209"
    $ current_voice="voice/SUZ03A_SUZ0209.ogg"
    "铃羽β" "「这台时间机器，我可以去坐吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0210"
    $ current_voice = "voice/SUZ03A_SUZ0210.ogg"
    "铃羽" "「你？开走？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0211"
    $ current_voice="voice/SUZ03A_SUZ0211.ogg"
    "铃羽β" "「如果是不能回来的旅行的话，还是我去比较好，我一直这样想的。α，你不在的话父亲会伤心的」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0212"
    $ current_voice="voice/SUZ03A_SUZ0212.ogg"
    "铃羽β" "「我也是阿万音铃羽。虽然是不同的世界线，但也不想让父亲伤心」"
    "β与ω相比，感觉更缺少「自我」。"
    "所以对我而言，这是她第一次说自己的事情。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0213"
    $ current_voice="voice/SUZ03A_SUZ0213.ogg"
    "铃羽β" "「在这条世界线上我就像是幽灵一样的东西，但却能修理，回到过去的话应该能得到ＩＢＮ５１００」"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_CRS02_01"]


    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0214"
    $ current_voice = "voice/SUZ03A_SUZ0214.ogg"
    "铃羽" "「谢谢你，β」"
    call CHECK_RM_RECEIVE
    "我很感谢β的关心。"
    call CHECK_RM_RECEIVE
    "无论是不想让父亲悲伤的心情，还是想让我留在这个时代的心情。"

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0215"
    $ current_voice = "voice/SUZ03A_SUZ0215.ogg"
    "铃羽" "「但是，我要去」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_CRS02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_CRS02_01"])

    play bgm "BGM10"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "但是，却不能按他所说的做。"
    "我已经决定了。"
    "不对，我最初就是这样打算的。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0216"
    $ current_voice="voice/SUZ03A_SUZ0216.ogg"
    "铃羽β" "「为什么？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0217"
    $ current_voice = "voice/SUZ03A_SUZ0217.ogg"
    "铃羽" "「首先因为不可能」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0218"
    $ current_voice = "voice/SUZ03A_SUZ0218.ogg"
    "铃羽" "「无论是你还另一个我，都是像我的鬼魂一样的东西。因为我的犹豫而出生的其他可能性情况下的我」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0219"
    $ current_voice = "voice/SUZ03A_SUZ0219.ogg"
    "铃羽" "「让你一个人回到过去完成使命，是不行的，肯定」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0220"
    $ current_voice="voice/SUZ03A_SUZ0220.ogg"
    "铃羽β" "「只有我一个人回到过去的可能性也……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0221"
    $ current_voice = "voice/SUZ03A_SUZ0221.ogg"
    "铃羽" "「父亲留下的时间机器只有一台。只靠你一个人回到过去，这样危险性太大了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0222"
    $ current_voice = "voice/SUZ03A_SUZ0222.ogg"
    "铃羽" "「而且你在你的世界线中还有使命」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA05"),"True","lh/SUZ_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0223"
    $ current_voice="voice/SUZ03A_SUZ0223.ogg"
    "铃羽β" "「……我的世界线中的使命」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0224"
    $ current_voice = "voice/SUZ03A_SUZ0224.ogg"
    "铃羽" "「因为是只靠我一个人走不下去的路。所以你们两人来了，这已经足够了。就算你能够帮忙，我也还是要回到过去」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0225"
    $ current_voice = "voice/SUZ03A_SUZ0225.ogg"
    "铃羽" "「即便这样你也想回到过去的话，我能做到的最大让步就是『那就跟我一起去吧』」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0226"
    $ current_voice = "voice/SUZ03A_SUZ0226.ogg"
    "铃羽" "「但是肯定在回到过去的途中你们就会消失。回到该回到的世界」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA05"),"True","lh/SUZ_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
        alpha 1.0
        linear 0.5alpha 0.5
        linear 0.5alpha 1.0































    "如同是在证明我的话的正确一样，β和ω的身影一瞬间消失了。"
    "虽然她们两人一直像幽灵一样，但是感觉现在的存在变得更加弱了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA06"),"True","lh/SUZ_BMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0227"
    $ current_voice="voice/SUZ03A_SUZ0227.ogg"
    "铃羽β" "「其实从刚刚开始我就听不清楚你的声音了。大概就像你说的，我要回到我的世界线去了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0228"
    $ current_voice = "voice/SUZ03A_SUZ0228.ogg"
    "铃羽" "「你是发现了这点才说自己去的吗？」"
    "我觉得她的话自相矛盾。"
    "明明感觉自己要回到自己的世界线了，为什么要提出自己一个人回到过去呢。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0229"
    $ current_voice="voice/SUZ03A_SUZ0229.ogg"
    "铃羽β" "「呐，α。你有没有想过要是我没能修好时间机器的话该怎么办？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0230"
    $ current_voice = "voice/SUZ03A_SUZ0230.ogg"
    "铃羽" "「我从没想过……」"
    "我回答她的问题后，为什么她不回答问题，而是提出了另一个问题。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0231"
    $ current_voice="voice/SUZ03A_SUZ0231.ogg"
    "铃羽β" "「如果我不能修时间机器的话，无论你怎样打算，你都只有留在这个时代了。这点，你知道吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0232"
    $ current_voice = "voice/SUZ03A_SUZ0232.ogg"
    "铃羽" "「你在担心我吧」"
    "我终于明白β所说的意思了。"
    "而且我感觉自己是个只看他人表面的人。"
    "感觉无论是牧濑红莉栖，还是父亲，或者另一个的我，我都只在看他们的表面。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0233"
    $ current_voice="voice/SUZ03A_SUZ0233.ogg"
    "铃羽β" "「我不是说过你留在这里比较好吗」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0234"
    $ current_voice = "voice/SUZ03A_SUZ0234.ogg"
    "铃羽" "「你是位称职的军人这点，就已经让我感到满足了。但是你果然也是阿万音铃羽」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA05"),"True","lh/SUZ_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0235"
    $ current_voice="voice/SUZ03A_SUZ0235.ogg"
    "铃羽β" "「我说服了自己。我只要成为未来的基石就行了。既没有迷茫也没有后悔」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0236"
    $ current_voice = "voice/SUZ03A_SUZ0236.ogg"
    "铃羽" "「那么，我希望你能明白。我也能明白的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0237"
    $ current_voice = "voice/SUZ03A_SUZ0237.ogg"
    "铃羽" "「我跟你不同，会为绕路而迷茫和后悔……现在明白了。这不是谎话。」"
    "为了证明我是真心的，而一直看着β的脸。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA05"),"True","lh/SUZ_BMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
        alpha 1.0
        linear 0.5alpha 0.5
        linear 0.5alpha 1.0































    "β的身影闪动着消失，然后又出现。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0238"
    $ current_voice = "voice/SUZ03A_SUZ0238.ogg"
    "铃羽" "「我终于明白了。父亲是以怎样的心情，将这台时间机器交付给我」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0239"
    $ current_voice = "voice/SUZ03A_SUZ0239.ogg"
    "铃羽" "「虽然只能制造不能回到未来的不完全物，但还是躲着ＳＥＲＮ在一直制作着」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0240"
    $ current_voice = "voice/SUZ03A_SUZ0240.ogg"
    "铃羽" "「父亲早就知道了。我会绕路。就算我会迷茫。父亲还是相信着我而制作时间机器」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0241"
    $ current_voice = "voice/SUZ03A_SUZ0241.ogg"
    "铃羽" "「所以我希望你明白。并不是我心不甘情不愿地去。也不是因为只有这一个办法」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0242"
    $ current_voice = "voice/SUZ03A_SUZ0242.ogg"
    "铃羽" "「不是为了不让同伴白死。也不是为了弥补过错。也不是为了让父亲伤心而去。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ03A_SUZ0243"
    $ current_voice="voice/SUZ03A_SUZ0243.ogg"
    "铃羽β" "「是为了你自己而去的吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
        alpha 1.0
        linear 0.5alpha 0.5
        linear 0.5alpha 1.0
    with Dissolve(.5)































    "β的身影一时间剧烈的闪动起来。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0244"
    $ current_voice = "voice/SUZ03A_SUZ0244.ogg"
    "铃羽" "「没错」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0245"
    $ current_voice="voice/SUZ03A_SUZ0245.ogg"
    "铃羽ω" "「……虽然我不明白，但是我该怎么做才好？」"

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA06"),"True","lh/SUZ_DMA06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "随后ω哭了。"
    "似乎是感觉听不懂我跟β的话。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0246"
    $ current_voice="voice/SUZ03A_SUZ0246.ogg"
    "铃羽ω" "「我没有使命，回去后也只是早上起来去学校……」"
    "看着哭泣的ω，我想着这姑娘果然也是「阿万音铃羽」。"
    "生在和平的世界中，过着平常日子的阿万音铃羽。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0247"
    $ current_voice = "voice/SUZ03A_SUZ0247.ogg"
    "铃羽" "「我们会以你为目标努力的」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0248"
    $ current_voice="voice/SUZ03A_SUZ0248.ogg"
    "铃羽ω" "「什么意思？一点都不明白！」"
    "我的使命完成后，世界将不再受ＳＥＲＮ的支配。"
    "但是那并不一定是和平的世界线。"
    "这点从β是军人这点就能知道。"
    "就算世界线改变，也有可能因为其他的原因而无法达到世界和平。"
    "也许我的使命只是毫无意义的东西。"
    "但是ω的存在，标示着和平的世界线在某个地方存在着。"
    "没错，她就是希望，这种东西。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0249"
    $ current_voice = "voice/SUZ03A_SUZ0249.ogg"
    "铃羽" "「你就像现在这样幸福地活下去吧」"
    "对她的愿望就只有这一个。"
    "出生在和平的世界，过着普通生活的阿万音铃羽。只要她是幸福的，其他阿万音铃羽的努力就算得到了回报。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0250"
    $ current_voice="voice/SUZ03A_SUZ0250.ogg"
    "铃羽ω" "「不用你说我也很幸福哦！因为你们说了奇怪的事情，让我都悲伤了！」"
    "但是这份心情现在无法传递给她。"
    "不，之后的也无法传递给她吧。"
    "因为她不会知道其他阿万音铃羽的努力。"
    "但是，这样就行了。"
    "因为她展示了我所希望的结果。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0251"
    $ current_voice = "voice/SUZ03A_SUZ0251.ogg"
    "铃羽" "「那就忘记我们所说的」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0252"
    $ current_voice="voice/SUZ03A_SUZ0252.ogg"
    "铃羽ω" "「……可以忘记吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0253"
    $ current_voice = "voice/SUZ03A_SUZ0253.ogg"
    "铃羽" "「如果那样会让你幸福的话」"
    "我为了我而回到过去。"
    "这件事情没有必要将她牵扯进来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0254"
    $ current_voice="voice/SUZ03A_SUZ0254.ogg"
    "铃羽ω" "「嗯」"

















































    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
        alpha 1.0
        linear 0.5alpha 0.5
        linear 0.5alpha 1.0
        repeat
    with Dissolve(.5)
    "她的身影剧烈的闪动两秒后消失了。"
    "等我注意到时她的存在已经变得稀薄了。"
    "她好像已经停止了哭泣。"
    "虽然眼泪还挂在脸颊上，大概新的眼泪已经没有涌出来了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0255"
    $ current_voice = "voice/SUZ03A_SUZ0255.ogg"
    "铃羽" "「啊，但是我能说一句吗？」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0256"
    $ current_voice="voice/SUZ03A_SUZ0256.ogg"
    "铃羽ω" "「只说一句……就没关系」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0257"
    $ current_voice = "voice/SUZ03A_SUZ0257.ogg"
    "铃羽" "「不要让父亲和母亲太头痛了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ03A_SUZ0258"
    $ current_voice="voice/SUZ03A_SUZ0258.ogg"
    "铃羽ω" "「这种事情……你不说我也知道……」"






    $ loadBG(3,"BG_WHITE")



















    $ loadBG(2,"BG06N1")



    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0259"
    $ current_voice = "voice/SUZ03A_SUZ0259.ogg"
    "铃羽" "「只有这点，是我的拜托哦。绝对，拜托你了！」"


    "没有回答。"
    "她的身影消失不见了。"
    "本该在身边的β的身影也是。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0260"
    $ current_voice = "voice/SUZ03A_SUZ0260.ogg"
    "铃羽" "「谢谢你帮我修理，β」"
    "虽然没有回答，我还是继续在说。 "
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0261"
    $ current_voice = "voice/SUZ03A_SUZ0261.ogg"
    "铃羽" "「要跟父亲母亲好好相处哦，ω」"
    "我觉得也许还能传达给她们。"
    "但是这次没有听见ω反驳的「不是ω是铃羽」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0262"
    $ current_voice = "voice/SUZ03A_SUZ0262.ogg"
    "铃羽" "「再见，另一个的我们。虽然时间很短，但是遇见你们真好」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"IBGX081")


    $ loadBG(2,"IBGX081")








    play se "SGSE147"






    hide screen phonebtn
    "我一个人坐进时间机器中，发动了系统。"
    "这个声音让我觉得非常怀念。"
    "感觉来这个时代已经是很久以前的事情了。"
    "肯定已经完全修好了。"
    "听着记忆中的声音，我这样想着。"
    "只凭声音就能带来勇气。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0263"
    $ current_voice = "voice/SUZ03A_SUZ0263.ogg"
    "铃羽" "「其实这点也是父亲的心意吧」"
    "第一次乘坐时完全没有这样的感觉。"
    "但是我记得。"
    "这个带来勇气的声音。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0264"
    $ current_voice = "voice/SUZ03A_SUZ0264.ogg"
    "铃羽" "「好，走啦！」"
    "我舒展身体后坐在了椅子上。"
    "系好安全带，深呼了一口气。"
    "随后确认操作盘和目标时间。"
    "１９７５年。这是最初就该去的时代。"
    "然后我再度踏上没有回路的过去。"
    "失败说不定会导致死亡的旅途。"
    "但是我并不害怕。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0265"
    $ current_voice = "voice/SUZ03A_SUZ0265.ogg"
    "铃羽" "「ＦＧ２０４　２ｎｄ　ＥＤＩＴＩＯＮ　Ｖｅｒ……诶，是几号来着」"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0266"
    $ current_voice = "voice/SUZ03A_SUZ0266.ogg"
    "铃羽" "「不管了，出发！」"

    hide screen phoneSD1
    window hide

    stop bgm 

    return





    return







    return







    return














    return










































    return
