label SGFD2_RUK04A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")

    play bgm "FD2BGM05"

    $ date="8/20"
    $ day="FRI"
    hide screen phonebtn
    hide screen phoneSD1


    "在那之后的慌乱和之前经历过的一样。"
    "不对，因为已经经历过了一次，说不定已经有些习惯了。"
    "当然真由理的死很令人伤心。"
    "但是最令人伤心的事，还是“习惯了”这一点。"
    "以前我只是从别人那里听说了真由理的死讯，但是并没有看到那个瞬间。"
    "所以，亲眼看到的时候，还是有些被震撼到了。"
    "闭上眼睛的话，就算现在我依然能够鲜明地回忆起真由理酱那惊讶的表情和仿佛要握住宇宙似的而伸出的手。"
    "就算如此在那之后——在到葬礼之前的这段时间里，我的动摇要比第一次的要小得多。"
    "人类就是这种反复经历后就会逐渐习惯的生物。"
    "就算是令人高兴的事情也是这样。"
    "第一次经历的时候感受到的喜悦，重复两次，三次以后，就会慢慢变淡。"
    "更别说那些悲伤的，难过的事情了。"
    "不如说，这样负能量的事情早点习惯会更好些。"
    "大概那也是没有办法的事情吧。"
    "那么做的话，人才能维持精神上的稳定吧。"
    "我明白这一点。"
    "虽然明白这一点，但是我认为那是“无可奈何的事”而不是什么好事。"
    "冈部师傅也一定害怕着这一点。"
    "不断重复着真由理的死亡的话，只会让精神不断消耗。"
    "而那结果便是，对于“死亡”这一点，变得无动于衷。"
    "心——已经死了。"
    "冈部师傅并不是不能忍受这样的事情吧。"
    "其实那个时候——真由理酱死去的瞬间，冈部师傅的眉毛都没有动一动。"
    "只是淡淡地看着眼前发生的一切。"
    "只是客观地观测着发生的事情。"
    "虽然，心中还是十分悲伤的吧。"
    "能够感到那份痛苦的吧。"
    "现在的话，冈部师傅应该在研究所里失神。"
    "但是那并不是因为真由理的“死亡”而带来的冲击，而是因为自己意识到对于真由理已经可以见死不救的“罪恶感”的逐渐扩大所造成的。"
    "内心已经被磨平了。"

    window hide


    $ loadBG(0,"BG_BLACK")


    "是什么时候的事情呢，我想起了爸爸说过的话。"

    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG15E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_AMA01"),"True","lh/URP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0000"
    $ current_voice = "voice/RUK04A_UPP0000.ogg"
    "漆原父" "「活着这件事呢，琉华。一直是包含着死亡的哦」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0000"
    $ current_voice = "voice/RUK04A_RUK0000.ogg"
    "琉华" "「包含着……死亡？这是什么意思？」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0001"
    $ current_voice = "voice/RUK04A_UPP0001.ogg"
    "漆原父" "「在死亡面前，人人平等」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0002"
    $ current_voice = "voice/RUK04A_UPP0002.ogg"
    "漆原父" "「所以任何活着的东西，在这个世界上诞生的时候就无法逃避死亡的命运哦」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0001"
    $ current_voice = "voice/RUK04A_RUK0001.ogg"
    "琉华" "「命运……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0003"
    $ current_voice = "voice/RUK04A_UPP0003.ogg"
    "漆原父" "「是的。活着这件事，其实就是朝着死亡迈进的过程，而时间其实就是这路上的路标」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0004"
    $ current_voice = "voice/RUK04A_UPP0004.ogg"
    "漆原父" "「世间万物，其实是因为死亡的存在才算真正的活着哦。」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG15A")

    hide screen phonebtn
    hide screen phoneSD1

    "那确实是，小猫死去的时候。"
    "我小时候，神社的屋檐下曾经住过一只小猫。"
    "妈妈说这么随便收养会养成不好的习惯的，但是我还是经常偷偷地给它喂些牛奶啦鱼之类的。"
    "某一天，那只猫死去了。"
    "有段时间没有看到它了。大概是和其他的猫啦狗啦打架了的关系，受了很严重的伤，在我家屋檐下断了气。"
    "在那个时候，爸爸告诉了我。"
    "爸爸当时所说的话对于那个时候的我来说，太难以理解了。"
    "但是，如今我自然是领会到了他的意思。"
    "在死亡面前，人人平等。"
    "正因如此，人们才应该珍惜眼前的时光。"
    "但是呢，如果死亡的时间是最开始就决定好的东西的话，我们又该怎么办呢。"

    window hide


    $ loadBG(2,"BG_BLACK")




    "冈部师傅说过。"
    "不管试几次，都没法救到真由理。"
    "在某个时候会被袭击。"
    "在某个时候会被车撞。"
    "在某个时候会被电车碾死。"
    "在某个时候会突然心脏病发作。"
    "他说过真由理的死亡必然会在某时降临。"
    "但是，如果命运已经被写好了，我们又能做……"

    window hide
    play se "SGSE359"

    stop bgm 


    $ loadBG(0,"BG15A")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0002"
    $ current_voice = "voice/RUK04A_RUK0002.ogg"
    "琉华" "「……？」"
    "我听到了轻轻的脚步声，于是抬起了头。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0005"
    $ current_voice = "voice/RUK04A_UPP0005.ogg"
    "漆原父" "「琉华……」"
    "爸爸静静地俯视着我。"
    play bgm "FD2BGM06"

    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0003"
    $ current_voice = "voice/RUK04A_RUK0003.ogg"
    "琉华" "「爸爸……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0006"
    $ current_voice = "voice/RUK04A_UPP0006.ogg"
    "漆原父" "「怎么了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0004"
    $ current_voice = "voice/RUK04A_RUK0004.ogg"
    "琉华" "「爸爸，我不明白……」"
    "我怀着寻求帮助的心情，将内心浮现的疑问告诉了爸爸。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0005"
    $ current_voice = "voice/RUK04A_RUK0005.ogg"
    "琉华" "「以前，你说过的吧。人一定是会死的」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0007"
    $ current_voice = "voice/RUK04A_UPP0007.ogg"
    "漆原父" "「啊啊，确实说过呢。生命是有限的，人必定会迈向死亡。而那道路便是时间……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0006"
    $ current_voice = "voice/RUK04A_RUK0006.ogg"
    "琉华" "「那，谁什么时候会死，也是由命运决定的吗？」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0008"
    $ current_voice = "voice/RUK04A_UPP0008.ogg"
    "漆原父" "「命运吗。是呢……琉华是怎么想的呢？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0007"
    $ current_voice = "voice/RUK04A_RUK0007.ogg"
    "琉华" "「……我的话……不太明白吧……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0008"
    $ current_voice = "voice/RUK04A_RUK0008.ogg"
    "琉华" "「但是，如果是已经被决定好的话……」"
    "连弱冠之年都不到就要死去。如果这是在生下来的时候就被决定好的命运的话。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0009"
    $ current_voice = "voice/RUK04A_RUK0009.ogg"
    "琉华" "「我们到底是，为了什么而活在这个世界上的啊……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0009"
    $ current_voice = "voice/RUK04A_UPP0009.ogg"
    "漆原父" "「琉华……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0010"
    $ current_voice = "voice/RUK04A_RUK0010.ogg"
    "琉华" "「呐，我们到底是为了什么才活在这个世界上的啊！？」"
    hide screen phoneSD1
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK004A"]]["Check"]=True
    $ loadBG(0,"EV_RUK004A")

    hide screen phonebtn
    "那一天，我捂着自己的嘴看着真由理死去。"
    "想着至少要实现真由理酱的愿望，如此希望着脱离了因果。"
    "在名为时间的无法逆行的道路上，往回探索。"
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0011"
    $ current_voice = "voice/RUK04A_RUK0011.ogg"
    "琉华" "「我只是……我只是想要，实现真由理的心愿而已！」"
    "就算和爸爸说这些，他肯定也不懂吧。"
    "说的尽是些难懂的，所以我也只是把想到的东西说出来而已。"
    "但是，就算如此，我还是难以抑制把内心的思绪说出来的心情。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0012"
    $ current_voice = "voice/RUK04A_RUK0012.ogg"
    "琉华" "「我是为了而实现真由理的愿望才……！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0013"
    $ current_voice = "voice/RUK04A_RUK0013.ogg"
    "琉华" "「于是我觉得我已经实现了那个愿望。因为那个时候──」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG56A")

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "我让她看见我的Ｃｏｓｐｌａｙ装的时候。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0014"
    $ current_voice = "voice/RUK04A_RUK0014.ogg"
    "琉华" "「那个时候，真由理酱真的很开心！」"
    "她的笑容是那样的高兴。"
    "但是。"
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0015"
    $ current_voice = "voice/RUK04A_RUK0015.ogg"
    "琉华" "「但是，那真的是真由理酱的愿望吧？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0016"
    $ current_voice = "voice/RUK04A_RUK0016.ogg"
    "琉华" "「确实，真由理酱笑了……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0017"
    $ current_voice = "voice/RUK04A_RUK0017.ogg"
    "琉华" "「但是，真由理酱的真正的愿望如果还有其他的话，我……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0018"
    $ current_voice = "voice/RUK04A_RUK0018.ogg"
    "琉华" "「我……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG56A")

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "为什么，真由理酱会想让我去Ｃｏｓｐｌａｙ呢。"
    "那难道——不是为了让我笑起来吗？"
    "为了让缺少自信的我拥有一些自信，"
    "怀着这份自信，打心底笑出来。"
    "所以，才那样拼命地邀请我去参加Ｃｏｓｐｌａｙ。"
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    "不对，不止只有我。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0019"
    $ current_voice = "voice/RUK04A_RUK0019.ogg"
    "琉华" "「真由理酱她，无论何时都希望大家能够笑着啊……」"
    "是的，无论何时——"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0020"
    $ current_voice = "voice/RUK04A_RUK0020.ogg"
    "琉华" "「希望着我，希望着桥田君，希望着牧濑，希望着菲利斯，希望着楼下的店长，也希望着冈部师傅能够笑着」"
    "希望着大家都能露出笑容——"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG38N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK04A_MAY0000"
    $ current_voice = "voice/RUK04A_MAY0000.ogg"
    "真由理" "「真由喜呢，如果琉华酱呀，冈伦呀，大家都能露出笑容的话，就非常的幸福哦」"
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0021"
    $ current_voice = "voice/RUK04A_RUK0021.ogg"
    "琉华" "「大家的笑容——那才是」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0022"
    $ current_voice = "voice/RUK04A_RUK0022.ogg"
    "琉华" "「那才是，真由理酱的真正的愿望啊！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0023"
    $ current_voice = "voice/RUK04A_RUK0023.ogg"
    "琉华" "「然后，大家的里面，也当然应该包括了真由理酱自己」"
    "那是——"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0024"
    $ current_voice = "voice/RUK04A_RUK0024.ogg"
    "琉华" "「明明那才是，真由理酱的真正的心愿……」"
    "但是现在这样的话……"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0025"
    $ current_voice = "voice/RUK04A_RUK0025.ogg"
    "琉华" "「呐，爸爸，请告诉我吧」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0010"
    $ current_voice = "voice/RUK04A_UPP0010.ogg"
    "漆原父" "「…………」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0026"
    $ current_voice = "voice/RUK04A_RUK0026.ogg"
    "琉华" "「人死了之后的话会怎样呢？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0027"
    $ current_voice = "voice/RUK04A_RUK0027.ogg"
    "琉华" "「人死了之后，到底会变成怎样呢？」"

    stop bgm 
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0011"
    $ current_voice = "voice/RUK04A_UPP0011.ogg"
    "漆原父" "「……死了之后，吗」"
    "直到现在，一直听我诉说着的爸爸，用沉稳的语气开口说道。"
    play bgm "BGM14"

    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0012"
    $ current_voice = "voice/RUK04A_UPP0012.ogg"
    "漆原父" "「那种事琉华也知道的吧？人在死了以后会变成神明哦」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0013"
    $ current_voice = "voice/RUK04A_UPP0013.ogg"
    "漆原父" "「人在死了之后呢，会化为先祖之魂，守护着我们这些子孙哦」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0014"
    $ current_voice = "voice/RUK04A_UPP0014.ogg"
    "漆原父" "「对我们这些信奉神道的人来说，那就是死后的世界哦」"
    "那是，从小时候开始就一直听到的说法。"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0015"
    $ current_voice = "voice/RUK04A_UPP0015.ogg"
    "漆原父" "「……但是当然，也有其他的思考方式」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0028"
    $ current_voice = "voice/RUK04A_RUK0028.ogg"
    "琉华" "「其他的思考方式……？」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0016"
    $ current_voice = "voice/RUK04A_UPP0016.ogg"
    "漆原父" "「是的。比如说，基督教的话，就是会根据最终的审判来决定人是去天国还是地狱」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0017"
    $ current_voice = "voice/RUK04A_UPP0017.ogg"
    "漆原父" "「然后佛教里也有人死了之后就会转生——或者说，根据生前的“业”来决定是前往极乐世界还是地狱。」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0018"
    $ current_voice = "voice/RUK04A_UPP0018.ogg"
    "漆原父" "「关于人死了之后到底会怎么样这一点，世界各地有不同的看法」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0019"
    $ current_voice = "voice/RUK04A_UPP0019.ogg"
    "漆原父" "「但是呢。唯一能说的是，那些都是我们这些“活着的人类”所想到的世界。」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0029"
    $ current_voice = "voice/RUK04A_RUK0029.ogg"
    "琉华" "「…………」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0020"
    $ current_voice = "voice/RUK04A_UPP0020.ogg"
    "漆原父" "「这样说好吗，琉华。活着的人们对于死后的世界的想象，都是为了那些活着的人类哦。」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0030"
    $ current_voice = "voice/RUK04A_RUK0030.ogg"
    "琉华" "「诶？」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0021"
    $ current_voice = "voice/RUK04A_UPP0021.ogg"
    "漆原父" "「死了之后魂魄不会迷惘，会成佛什么的，去天国什么的……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0022"
    $ current_voice = "voice/RUK04A_UPP0022.ogg"
    "漆原父" "「人们这么想着，吊唁着死者」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0023"
    $ current_voice = "voice/RUK04A_UPP0023.ogg"
    "漆原父" "「但是呢，结果其实没有死去以后的世界哦」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0024"
    $ current_voice = "voice/RUK04A_UPP0024.ogg"
    "漆原父" "「不管葬礼多么豪华隆重，这一切也只是为了让活着的人们安心才那么做罢了」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0025"
    $ current_voice = "voice/RUK04A_UPP0025.ogg"
    "漆原父" "「死去的人，已经什么都不会想了」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0026"
    $ current_voice = "voice/RUK04A_UPP0026.ogg"
    "漆原父" "「也无法继续思考什么了」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0027"
    $ current_voice = "voice/RUK04A_UPP0027.ogg"
    "漆原父" "「死去的那个时候——就是那个人的世界的终点啊」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0031"
    $ current_voice = "voice/RUK04A_RUK0031.ogg"
    "琉华" "「终点……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0028"
    $ current_voice = "voice/RUK04A_UPP0028.ogg"
    "漆原父" "「是啊，但是这么想的话就好可怕哦」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0029"
    $ current_voice = "voice/RUK04A_UPP0029.ogg"
    "漆原父" "「所以，人们才会去想象死后的世界啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA02"),"True","lh/URP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0030"
    $ current_voice = "voice/RUK04A_UPP0030.ogg"
    "漆原父" "「……什么的，听身为神社主人的父亲说了这些，可不要生气哦」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0032"
    $ current_voice = "voice/RUK04A_RUK0032.ogg"
    "琉华" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0031"
    $ current_voice = "voice/RUK04A_UPP0031.ogg"
    "漆原父" "「嘛，这姑且是作为父亲能给你的意见……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0032"
    $ current_voice = "voice/RUK04A_UPP0032.ogg"
    "漆原父" "「但是呢，琉华，思考这件事可是非常重要的。」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0033"
    $ current_voice = "voice/RUK04A_RUK0033.ogg"
    "琉华" "「是……」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0033"
    $ current_voice = "voice/RUK04A_UPP0033.ogg"
    "漆原父" "「失去了朋友，现在一定很难受吧。但是，像这样自己独立思考也，也是非常重要的。爸爸是这么认为的」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0034"
    $ current_voice = "voice/RUK04A_RUK0034.ogg"
    "琉华" "「……恩」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "爸爸稍稍点了点头，又轻轻地用手拍了我几下，然后就慢慢地离开了神社。"
    "手上拿着行李的样子，好像是必须要去什么地方，然而因为我耽搁了一会。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0035"
    $ current_voice = "voice/RUK04A_RUK0035.ogg"
    "琉华" "「…………」"
    play bgm "FD2BGM04"

    "死去之人的世界终点——父亲是这样说的。"
    "但是，那样的话……"
    "那样的话，真由理酱的愿望到底会变成怎样呢。"
    "如果死了之后就是世界的终点的话，在那之后真由理酱的愿望不就消失了吗。"
    "那么我到底是为了什么——才扭曲了因果之轮，前往过去呢。"
    "已经不想再让谁受伤了——冈部师傅是这么说的。"
    "不想再牺牲谁的想法，这么说过。"
    "冈部师傅是温柔的人，所以不希望自己的自我让谁感到悲伤。"
    "那样的心情，我当然能理解。"
    "但是，这样的话真由理的“想法”会变成怎样呢？"
    "真由理的那种大家都能露出笑容比什么都重要的心情，去了哪里呢？"
    "当然，我是没有资格说这种话的。"
    "我也是因为自我意识，改变了这个世界。"
    "想要这个身体，结果导致了真由理的死亡"
    "但是，不去考虑那个也不行。"
    "关于接下来该怎么做这一点。"

    stop bgm 
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0036"
    $ current_voice = "voice/RUK04A_RUK0036.ogg"
    "琉华" "「──！」"
    window hide


    "我握起放在身边的五月雨，站了起来。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0037"
    $ current_voice = "voice/RUK04A_RUK0037.ogg"
    "琉华" "「…………」"
    "清心斩魔流。"
    "切断迷惘，斩尽妖魔。"
    "包括自己心中的魔障。"
    window hide

    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0038"
    $ current_voice = "voice/RUK04A_RUK0038.ogg"
    "琉华" "「！」"
    "按照冈部师傅教我的那样，将刀横在我眼前。"
    "然后仰起头，直直地斩落。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK002A"]]["Check"]=True
    $ loadBG(0,"EV_RUK002A")


    play se "SGSE360"







    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0039"
    $ current_voice = "voice/RUK04A_RUK0039.ogg"
    "琉华" "「一！！」"
    "为了将迷惘打散。"
    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0040"
    $ current_voice = "voice/RUK04A_RUK0040.ogg"
    "琉华" "「二！！」"
    "不可思议地，随着刀的挥舞，我心中的迷茫也越来越少。"
    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0041"
    $ current_voice = "voice/RUK04A_RUK0041.ogg"
    "琉华" "「三，四，五！」"

    "是啊。"
    "如果钻牛角尖的话，就会陷入现在冈部师傅的状态。"
    "慢慢消磨自己的精神，逐渐无法忍受。"
    "想要享乐。"
    "然后，还接受那样的冈部师傅的心意的我，还只是自我意识的凝结体而已。"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0042"
    $ current_voice = "voice/RUK04A_RUK0042.ogg"
    "琉华" "「十一，十二……！」"

    "冈部师傅犯下的罪。"
    "还有我犯下的罪。"
    "我们一起背负着那份罪的话，也只是让每个人承受的要少一些而已。"
    "那大概不是什么好事——不对。"
    "那是“不可以的事”。"
    "而且——"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0043"
    $ current_voice = "voice/RUK04A_RUK0043.ogg"
    "琉华" "「十……八！！」"

    "现在这样下去的话，冈部师傅再也不会笑了。"
    "在这之后，肯定发自内心的笑是不会有了吧。"
    "并不只有冈部师傅。"
    "我也是。"
    "牧濑也是。"
    "大家都是，再也无法露出真心的笑容了吧。"
    "真由理如果不活着的话，大家都无法发自内心地微笑了。"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0044"
    $ current_voice = "voice/RUK04A_RUK0044.ogg"
    "琉华" "「二……十！」"

    "冈部师傅的心中，现在有一个巨大的空洞。"
    "我无法将其填满。"
    "我无法取代真由理。"
    "我说过要实现真由理的愿望。"
    "为了那个回到过去。"
    "但是，这样的话，真由理的真正愿望并没有实现。"
    "因为——谁都没有在笑。"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0045"
    $ current_voice = "voice/RUK04A_RUK0045.ogg"
    "琉华" "「二十……四！」"

    "这样的世界，谁都未曾渴求过。"
    "这样的世界，我不愿看到。"
    "谁都不愿看到。"
    "桥田君曾这么说过。"
    "只有当谁观测了这个世界的时候，它才会变成真的。"
    "没有观测的时候，世界就不存在。"
    "就处于不确定的状态。"
    "那到底是什么意思呢，我并不是很理解。"
    "但是，我们现在所在的世界，一定谁都不愿意观测到吧。"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0046"
    $ current_voice = "voice/RUK04A_RUK0046.ogg"
    "琉华" "「二十……九！」"

    "这个世界，一定不是真正的世界吧"

    window hide
    play se "SGSE360"



    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0047"
    $ current_voice = "voice/RUK04A_RUK0047.ogg"
    "琉华" "「三…………十！」"

    "也就是不该存在的世界。"

    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0048"
    $ current_voice = "voice/RUK04A_RUK0048.ogg"
    "琉华" "「哈……哈……哈……」"
    window hide
    play se "SGSE359"

    stop bgm 


    $ loadBG(2,"BG15A")



    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0049"
    $ current_voice = "voice/RUK04A_RUK0049.ogg"
    "琉华" "「──！？」"
    "我又一次听到了轻轻的脚步声，抬起了头。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0000"
    $ current_voice = "voice/RUK04A_OKA0000.ogg"
    "伦太郎" "「琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0050"
    $ current_voice = "voice/RUK04A_RUK0050.ogg"
    "琉华" "「冈部师傅……」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    play bgm "FD2BGM08"

    "我们坐在走廊下，一时之间一言不发地望着天空。"
    "偷偷看了眼冈部师傅的表情，比之前我们在这里的时候，要好上很多。"

    window hide



    $ loadBG(2,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1

    $ targetmailid = gc["ScriptMacros"]["RM_RUK_RECV_UMM01_01"]

    $ LR_RM_CHANCE=2
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0001"
    $ current_voice = "voice/RUK04A_OKA0001.ogg"
    "伦太郎" "「琉华子」"
    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0051"
    $ current_voice = "voice/RUK04A_RUK0051.ogg"
    "琉华" "「是」"

    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0002"
    $ current_voice = "voice/RUK04A_OKA0002.ogg"
    "伦太郎" "「谢谢你，琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0052"
    $ current_voice = "voice/RUK04A_RUK0052.ogg"
    "琉华" "「我并没有做什么可以感谢的事情……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0003"
    $ current_voice = "voice/RUK04A_OKA0003.ogg"
    "伦太郎" "「并非如此。你之前为了真由理才去了夏Ｃｏｍｉ的Ｃｏｓｐｌａｙ吧」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0004"
    $ current_voice = "voice/RUK04A_OKA0004.ogg"
    "伦太郎" "「那天，真由理真的很开心哦。一整天……脸上都笑着。」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0005"
    $ current_voice = "voice/RUK04A_OKA0005.ogg"
    "伦太郎" "「多亏了你呢。所以，谢谢了……」"

    "被看穿了啊。"
    "冈部师傅的样子比之前看起来好一些，一定是因为我实现了真由理的梦想——或者说我觉得已经实现了她的梦想吧。"
    "一直到最后的最后真由理都笑着。"
    "因为，那是我用了那么多次时间机器回到回去才得到的啊。"
    "然后，我本来应该也对此感到高兴的。"
    "应该开心才对。"
    "但是。"

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0006"
    $ current_voice = "voice/RUK04A_OKA0006.ogg"
    "伦太郎" "「怎么了吗，琉华子？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0053"
    $ current_voice = "voice/RUK04A_RUK0053.ogg"
    "琉华" "「不，并没有什么」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0007"
    $ current_voice = "voice/RUK04A_OKA0007.ogg"
    "伦太郎" "「是吗……」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UMM01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UMM01_01"])


    "心里不停地抽痛着是为什么呢？"
    "不，这个答案事到如今连我也知道了。"
    "那是因为——我还逃避着。"
    "就算是很小的心愿，我也希望能够实现。"
    "当然，那也是我们的愿望。"
    "那也是让我们得到救赎的愿望。"
    "两个人一起背负的罪的重量。"
    "为了让它稍微减轻一些。"
    "从对于真由理见死不救这份罪的沉重中稍微解脱一些。"
    "但是，已经到了这个地步，果然还是会想。"
    "这样是不行的，啊。"
    "就算不管怎样去实现她的愿望。"
    "就算她露出怎样的笑容。"
    "就算那样，果然真由理酱还是死掉了。"
    "这一结果并未改变。"
    "然后，果然我还是不希望真由理酱死去。"
    "这也并未改变。"
    "什么都没有改变。"
    "改变的仅仅只有，我们的罪恶感而已。"
    "为了真由理酱。"
    "让真由理酱高兴。"
    "一边这么说着，我们的结局却只是让自己得到些许的救赎而已。"
    "我又想起了爸爸的话。"

    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_AMA01"),"True","lh/URP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0034"
    $ current_voice = "voice/RUK04A_UPP0034.ogg"
    "漆原父" "「这样说好吗，琉华。活着的人们对于死后的世界的想象，都是为了那些活着的人类哦。」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0035"
    $ current_voice = "voice/RUK04A_UPP0035.ogg"
    "漆原父" "「死去的人，已经什么都不会想了」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0036"
    $ current_voice = "voice/RUK04A_UPP0036.ogg"
    "漆原父" "「也无法继续思考什么了」"
    $ stopvoc("UPP")
    play UPP "RUK04A_UPP0037"
    $ current_voice = "voice/RUK04A_UPP0037.ogg"
    "漆原父" "「死去的那个时候——就是那个人的世界的终点啊」"
    window hide

    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0054"
    $ current_voice = "voice/RUK04A_RUK0054.ogg"
    "琉华" "「…………」"

    "我们所信奉的神道中，认为人死了之后就会成为先祖之魂。"
    "简单地来说，就是成为神明的伙伴。"
    "成为保护神守护着自己的子孙——这就是神道中死亡的概念。"
    "但是，这只是为了让我们这些生者感到安心的说法罢了。"
    "死了之后到底会怎样呢。"
    "如果什么都不剩的话，那就太令人悲伤了。"
    "太令人——害怕了。"
    "但是成为神明什么的，大概谁也不会高兴。"
    "首先，神就已经是神了，不再是人类。"
    "所以果然对于人类来说那个人的世界，在死亡的时候就迎来了终点。"
    "也就是说。"
    "“真由理酱的世界”，已经结束了。"

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0008"
    $ current_voice = "voice/RUK04A_OKA0008.ogg"
    "伦太郎" "「不要露出那种表情。真由理……她还活在我们的心中。只要我们不曾忘记……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0055"
    $ current_voice = "voice/RUK04A_RUK0055.ogg"
    "琉华" "「冈部师傅……」"

    "这种说法……"
    "这种说法不对。"
    "那只是还活着的我们的一厢情愿而已。"
    "死了以后，就不会或者。"
    "回忆中的真由理酱，只会存在于我们的回忆中。"
    "所以总有一天，我们也会无法想起。"
    "她的音容笑貌总会随着时间，慢慢地变得稀薄，最终消失。"
    "听起来很令人悲伤。"
    "而且，我们所拥有的罪恶感也会逐渐单薄。"
    "那样的话，真的能说真由理还活着吗。"
    "我们对于真由理酱见死不救这个事实，必须由我们两个人来背负。"
    "认为实现了真由理的愿望就能减去这份罪恶这一点。"
    "那是我们为了让自己好过一些才做出的行为，实际上是“不可以的事”。"

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0009"
    $ current_voice = "voice/RUK04A_OKA0009.ogg"
    "伦太郎" "「怎么了吗，琉华子？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0056"
    $ current_voice = "voice/RUK04A_RUK0056.ogg"
    "琉华" "「不……」"

    "但是我却没有把这些想法告诉冈部师傅。"
    "无法很好地组织语言。"
    "就这样一言不发地任凭时间流过。"
    "这样的“时间”，也正是因为我们还活着才会存在。"
    "这么想着。"

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"IBGX033")

    $ targetmailid = cml.setdefault("RM_RUK_SEND_UMM01","")

    $ LR_RM_CHANCE=0
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UMM02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UMM02_01"])




    "不知有多少云朵已经无声地消失。"
    "感觉在这秋叶原偌大的街道中，我和冈部师傅两个人就这么被孤零零地抛下了。"

    window hide


    $ loadBG(2,"BG15E")
    show screen phoneSD1



    play bgm "BGM11"

    "把手缩回袖子里的时候，感觉摸到了什么。"
    "是在夏Ｃｏｍｉ上和真由理一起的照片。"
    "大家一起拍的纪念照。"
    "那个时候真由理酱还活着。"
    "照片中的真由理酱在因为Ｃｏｓｐｌａｙ装而显得有些羞涩的我边上，露出快乐的笑容。"
    "从那时就过了短短片刻。"
    "现在时间也在流逝着。"
    "然后，一点一点，那个时刻接近着。"
    "我出发回到过去的时间。"
    "这几天都是我已经经历过一次的时间了。"
    "但是在那之后，是连我也不知道的世界。"
    "未知的未来存在于那里。"
    "冈部师傅说过，在这世界上有无数的世界线。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "现在，在我眼前的冈部师傅并不知道我曾经回到过过去。"
    "但是，以前的世界线上的冈部师傅，应该马上用时间机器要跳回到过去了。"
    "也就是说这两条世界线很快就要相交了。"
    "在那里的冈部师傅，会是哪边的冈部师傅呢，我并不是很确定。"
    "是知道我去了夏Ｃｏｍｉ的冈部师傅呢。"
    "还是不知道的冈部师傅呢。"
    "如果是不知道的冈部师傅的话，可就要给他看照片了呢。"
    "而且，在那之前会是怎样的未来，我也并不清楚。"
    "那是我还未曾经历过的时间。"
    "再过一会，那个时间就到了。"
    "我不知道的未来和现在的交叉点。"
    "再等一会儿。"

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0010"
    $ current_voice = "voice/RUK04A_OKA0010.ogg"
    "伦太郎" "「呐，琉华子」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0057"
    $ current_voice = "voice/RUK04A_RUK0057.ogg"
    "琉华" "「恩」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0011"
    $ current_voice = "voice/RUK04A_OKA0011.ogg"
    "伦太郎" "「我想把电话微波炉（暂）给扔了」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0058"
    $ current_voice = "voice/RUK04A_RUK0058.ogg"
    "琉华" "「诶？」"
    "听到意料之外的话，我停止了思考。"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0012"
    $ current_voice = "voice/RUK04A_OKA0012.ogg"
    "伦太郎" "「到头来，Ｄ－ｍａｉｌ也好，时间跳跃也好，这些道具对于我们来说太过于超前了」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0013"
    $ current_voice = "voice/RUK04A_OKA0013.ogg"
    "伦太郎" "「就算在这以后我们不再进一步研究下去，也不会有好事」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0014"
    $ current_voice = "voice/RUK04A_OKA0014.ogg"
    "伦太郎" "「对于我和我周围的人来说，那些道具没有哪怕一点点的好处」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0015"
    $ current_voice = "voice/RUK04A_OKA0015.ogg"
    "伦太郎" "「那样的东西还是……消失比较好」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0016"
    $ current_voice = "voice/RUK04A_OKA0016.ogg"
    "伦太郎" "「这也是为了让发生在真由理身上的事情……不再发生到别的人身上啊。」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0059"
    $ current_voice = "voice/RUK04A_RUK0059.ogg"
    "琉华" "「冈部……师傅……」"
    "想想看的话，冈部师傅会得出这样的结论，也是理所当然的。"
    "已经……不能再让谁的心意牺牲了。"
    "这样决定了以后，那些机器就都不需要了。"
    "那样的话，也就是说。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0060"
    $ current_voice = "voice/RUK04A_RUK0060.ogg"
    "琉华" "「认真的吗！？　真的要把它们全部破坏？」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0017"
    $ current_voice = "voice/RUK04A_OKA0017.ogg"
    "伦太郎" "「啊啊。这是我考虑了好几天的结果。」"
    "以前的冈部师傅——我曾经经历过的世界里的冈部师傅，并没有说过这样的话。"
    "现在突然这么说的话，也就是说我回到过去实现真由理的愿望之后，让冈部师傅有了什么变化吧。"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0018"
    $ current_voice = "voice/RUK04A_OKA0018.ogg"
    "伦太郎" "「我们不能一直被过去所束缚，必须要斩断与过去的联系了。」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0019"
    $ current_voice = "voice/RUK04A_OKA0019.ogg"
    "伦太郎" "「所以为了那个，我才觉得应该要把它们都破坏掉。」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0020"
    $ current_voice = "voice/RUK04A_OKA0020.ogg"
    "伦太郎" "「呐。琉华子也认为那样会比较好吧？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0061"
    $ current_voice = "voice/RUK04A_RUK0061.ogg"
    "琉华" "「我吗？　我的话……」"

    "没法一下子回答上来。"
    "因为，那就是说。"
    "放弃了再次去拯救真由理的机会。"
    "也就是说要我来决定是否那么做。"
    "啊，是这样啊。"
    "我还是太年轻了。"
    "在之前的时候，同一时间同一地点，却没有发生这样的对话。"
    "当然那个时候冈部师傅也应该做出来不再拯救真由理的决定，但是就算如此也不知在何时何地改变了心意，又回到了过去——原来的未来是这样的。"
    "但是，现在不一样。"
    "在那个未来的最后的希望，也消失了。"
    "那样的话，如果我点点头，那就会自然而然地变成那样的吧。"
    "进入再也无法遇到真由理的世界。"
    "进入真由理的存在完全消失的世界。"

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0021"
    $ current_voice = "voice/RUK04A_OKA0021.ogg"
    "伦太郎" "「怎么了，琉华子。为什么，没有点头？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0062"
    $ current_voice = "voice/RUK04A_RUK0062.ogg"
    "琉华" "「冈部师傅……」"

    "啊，是这样啊。"
    "我终于明白了那句话。"
    "冈部师傅，需要别人在背后推他一把。"
    "想要让我告诉他自己的决定没有错误。"
    "但是，反过来说这也意味着他还在犹豫。"
    "也就是说他在动摇着。"
    "一个人做出决定实在是太过于沉重。"
    "所以才希望我能肯定他。"
    "我又在我的脑海里开始了已经重复过无数次却依然无法理解的自问自答。"
    "冈部师傅说过已经不希望在牺牲谁的心意了。"
    "但是，这样的话。"
    "真由理的心情会变成怎样呢。"

    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG38N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK04A_MAY0001"
    $ current_voice = "voice/RUK04A_MAY0001.ogg"
    "真由理" "「真由喜呢，如果琉华酱呀，冈伦呀，大家都能露出笑容的话，就非常的幸福哦」"
    window hide


    $ loadBG(0,"BG15E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "那种希望大家都能露出笑容的心情。"
    "那样希望着能和大家一起度过每一天的真由理的心情。"
    "那种希望还能多活一天的真由理的心情。"
    "真由理酱的未来就——"

    hide screen phoneSD1
    window hide
    play se "SGSE087"

    stop bgm 



    $ loadBG(0,"EVX_R10A")

    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0063"
    $ current_voice = "voice/RUK04A_RUK0063.ogg"
    "琉华" "「…………」"
    window hide


    $ loadBG(0,"BG15E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "FD2BGM05"

    "那个时候——"
    "我的脑海里，浮现出了某个情景。"
    "那是，未曾看到过的未来景象。"
    "那个瞬间，我明白了。"
    "从一开始，就没有反复考虑过。"
    "和冈部师傅一起。"
    "结论大概最开始就有了。"
    "因为，那是“不可以的事”嘛"
    "确实“想法”也许是非常重要的。"
    "但是，并不是要牺牲谁来贯彻到底的“想法”。"


    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD02"),"True","lh/OKA_ALD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0022"
    $ current_voice = "voice/RUK04A_OKA0022.ogg"
    "伦太郎" "「…………」"
    "抬起头来的时候，冈部师傅露出了不可思议的表情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD01"),"True","lh/OKA_ALD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "是发现自己的惊讶被我看到了吗，把目光移开了。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0064"
    $ current_voice = "voice/RUK04A_RUK0064.ogg"
    "琉华" "「冈部……师傅？」"
    "然后，他很不可思议地看着我。"
    "看到这个我立刻明白了。"
    "啊，刚才冈部师傅的时间交叉路。"
    "那样的话，接下来就要确认一下了。"
    "现在的冈部师傅是哪个冈部师傅。"
    "是和我去了夏Ｃｏｍｉ的冈部师傅呢，还是不是呢？"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0065"
    $ current_voice = "voice/RUK04A_RUK0065.ogg"
    "琉华" "「照片……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0023"
    $ current_voice = "voice/RUK04A_OKA0023.ogg"
    "伦太郎" "「照片？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0066"
    $ current_voice = "voice/RUK04A_RUK0066.ogg"
    "琉华" "「你还记得……吗？冈部师傅」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0024"
    $ current_voice = "voice/RUK04A_OKA0024.ogg"
    "伦太郎" "「你用时间机器回到过去以后……在那之后，我就在这里了。」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0067"
    $ current_voice = "voice/RUK04A_RUK0067.ogg"
    "琉华" "「那也就是说，照片的事……」"
    "现在，我眼前的冈部师傅是。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0025"
    $ current_voice = "voice/RUK04A_OKA0025.ogg"
    "伦太郎" "「……啊，是这样啊。琉华子，你是为了实现真由理的愿望才回到过去的啊……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0026"
    $ current_voice = "voice/RUK04A_OKA0026.ogg"
    "伦太郎" "「照片……也就是说，很顺利吗？」"

    stop bgm 
    "是不知道的那个冈部吗。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0068"
    $ current_voice = "voice/RUK04A_RUK0068.ogg"
    "琉华" "「那个……」"
    "这样的话我该说的是……"
    play bgm "FD2BGM11"

    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0069"
    $ current_voice = "voice/RUK04A_RUK0069.ogg"
    "琉华" "「那个……、我好像……不行……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0027"
    $ current_voice = "voice/RUK04A_OKA0027.ogg"
    "伦太郎" "「不行……也就是说，失败了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0070"
    $ current_voice = "voice/RUK04A_RUK0070.ogg"
    "琉华" "「是的，２天之前——回到１８号还是顺利的，结果店关门了……」"
    "没想过自己会说这样的谎言。"
    "但是就算如此还是很紧张，我下意识地握紧了手里的照片，一下子就弄皱了。"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0028"
    $ current_voice = "voice/RUK04A_OKA0028.ogg"
    "伦太郎" "「这样……啊……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0071"
    $ current_voice = "voice/RUK04A_RUK0071.ogg"
    "琉华" "「是的。所以，从那个时候开始就没能回到过去……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0029"
    $ current_voice = "voice/RUK04A_OKA0029.ogg"
    "伦太郎" "「那也就是说，夏Ｃｏｍｉ……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0072"
    $ current_voice = "voice/RUK04A_RUK0072.ogg"
    "琉华" "「没能去成……」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0030"
    $ current_voice = "voice/RUK04A_OKA0030.ogg"
    "伦太郎" "「那也就是说，没能实现真由理的愿望，是吗」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0073"
    $ current_voice = "voice/RUK04A_RUK0073.ogg"
    "琉华" "「恩……」"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA07"),"True","lh/OKA_ALA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "冈部师傅露出了遗憾的表情。"
    "好像相信了我说的话一样。"
    "这也是当然的了。"
    "因为冈部师傅根本没想到我会在这种时候撒谎。"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0074"
    $ current_voice = "voice/RUK04A_RUK0074.ogg"
    "琉华" "「那个，所以说，我还想再去一次！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0075"
    $ current_voice = "voice/RUK04A_RUK0075.ogg"
    "琉华" "「这次会，好好干了！肯定会……好好地完成的！所以说！」"
    "时间的话……现在，显像管工房肯定开着。"
    "所以，尽可能地早一些。"
    "冈部师傅的内心中，刚才的话——要把装置破坏的想法已经消失了。"
    "但是，应该在什么时候又会那么想。"
    "为了不变成那样，我……"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0076"
    $ current_voice = "voice/RUK04A_RUK0076.ogg"
    "琉华" "「拜托了！为了真由理酱！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA04"),"True","lh/OKA_ALA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0031"
    $ current_voice = "voice/RUK04A_OKA0031.ogg"
    "伦太郎" "「琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0077"
    $ current_voice = "voice/RUK04A_RUK0077.ogg"
    "琉华" "「为了真由理酱，请再让我试一次！我还想再回到过去一次！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0078"
    $ current_voice = "voice/RUK04A_RUK0078.ogg"
    "琉华" "「我想……改变过去！！」"
    "慢慢地，疑惑从我心中消失了。"
    "所以在那前方……"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0032"
    $ current_voice = "voice/RUK04A_OKA0032.ogg"
    "伦太郎" "「明，明白了。那样的话，就再让你去一次吧？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0079"
    $ current_voice = "voice/RUK04A_RUK0079.ogg"
    "琉华" "「好，好的！！」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0033"
    $ current_voice = "voice/RUK04A_OKA0033.ogg"
    "伦太郎" "「注意事项就算我不说也清楚了吧？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0080"
    $ current_voice = "voice/RUK04A_RUK0080.ogg"
    "琉华" "「恩」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0034"
    $ current_voice = "voice/RUK04A_OKA0034.ogg"
    "伦太郎" "「这个时间的话，要去夏Ｃｏｍｉ就要跳跃至少４次，没问题吗。？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0081"
    $ current_voice = "voice/RUK04A_RUK0081.ogg"
    "琉华" "「恩，已经大概习惯了吧」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0035"
    $ current_voice = "voice/RUK04A_OKA0035.ogg"
    "伦太郎" "「这样啊」"
    "是这样的。"
    "最初开始就不该迷惑的。"
    window hide

    stop bgm 

    show houden 
    play se "SGSE035L" loop

    "我只是想要，我自己的未来。"
    "作为女孩子的自己的未来。"
    "能够在冈部师傅身边的我的未来。"
    "那样的生活如果不是女孩子的我的话，是不可能实现的。"
    "是不可以的事情，所以。"
    "对于现在的我内心中存在的女孩子来说，是１７年积累下来的感受。"
    "但是，那是最初开始就不该存在的东西。"
    "所以，我。"
    hide screen phonebtn
    hide screen phoneSD1
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0036"
    $ current_voice = "voice/RUK04A_OKA0036.ogg"
    "伦太郎" "「出发了！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0082"
    $ current_voice = "voice/RUK04A_RUK0082.ogg"
    "琉华" "「…………」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0037"
    $ current_voice = "voice/RUK04A_OKA0037.ogg"
    "伦太郎" "「……为什么？我脸上粘上什么了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0083"
    $ current_voice = "voice/RUK04A_RUK0083.ogg"
    "琉华" "「不，不是！」"
    $ stopvoc("OKA")
    play OKA "RUK04A_OKA0038"
    $ current_voice = "voice/RUK04A_OKA0038.ogg"
    "伦太郎" "「是吗。那么，就出发吧！」"
    $ stopvoc("RUK")
    play RUK "RUK04A_RUK0084"
    $ current_voice = "voice/RUK04A_RUK0084.ogg"
    "琉华" "「好的！」"

    hide screen phoneSD1
    window hide

    stop se
    hide screen phonebtn
    hide houden 
    scene expression Solid("000000")  with fade

    return




    play se "SGSE054"




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
