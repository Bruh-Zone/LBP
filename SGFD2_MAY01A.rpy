label SGFD2_MAY01A:
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT003")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade



    $ date="8/14"
    $ day = "SAT"







    $ loadBG(0,"BG62N")

    play bgm "FD2BGM09"
    show screen phonebtn
    show screen phoneSD1

    "昨晚，难得做了一个非常幸福的梦。"
    "去给外婆扫墓的梦。"
    "法事明明在第二天，却有一种在梦中先和外婆相见的不可思议的感觉。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BLUE_WOOPA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BLUE_WOOPA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BLUE_WOOPA"])
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0000"
    $ current_voice = "voice/MAY01A_MAY0000.ogg"
    "真由理" "「今天也能做昨天那样的梦该多好啊～、是吧、{color=#f00}蓝色呜啪{/color}？」"
    window hide
    $ loadBG(0,"IBG009A",png=True)

    "一边用手拨弄着蓝色呜啪，一边试着对它说话。"
    "圆圆的耳朵，小短腿。弯曲的小尾巴。"
    "果然还是呜啪可爱啊。光是看着就会被治愈呢。"
    "毫不逊色于现在那些治愈系角色呢。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HIKONYA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HIKONYA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HIKONYA"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHIMEJI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHIMEJI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHIMEJI"])

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUMAMOMON"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUMAMOMON"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KUMAMOMON"])

    "打倒{color=#f00}彦艮猫{/color}、{color=#f00}真姬菇桑{/color}、{color=#f00}熊笨熊{/color}呦。加油、呜啪！"
    window hide
    hide background-png  with dissolve
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0001"
    $ current_voice = "voice/MAY01A_MAY0001.ogg"
    "真由理" "「但是、为什会做那样的梦呢～？」"
    "最近遇到了太多的事情了，是我觉得自己不得不向外婆报告这一切的关系吗？"
    "真由喜，过去什么话都会对外婆说呢。"
    "外婆她也总是微笑着听我说话。"
    "最后也总是会让我吃外婆她亲手做的团子呢。"
    "外婆她，对于我而言是最棒的挚友呢。"
    "即使现在外婆已化为天上的繁星了，这一点也不会改变。"
    "永远都是──"
    window hide
    $ loadBG(0,"IBG009A",png=True)
    $ loadBG(0,"IBG009A",png=True)

    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0002"
    $ current_voice = "voice/MAY01A_MAY0002.ogg"
    "真由理" "「但是呢、蓝色呜啪。听我说。昨天晚上在我的梦里呢，连冈伦都出现了」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MINCRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MINCRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MINCRO"])
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0002A"
    $ current_voice = "voice/MAY01A_MAY0002A.ogg"
    "真由理" "「昨晚的梦、真的是太神奇了～。像厨房吉罗的{color=#f00}面鸡饭{/color}那样的呢」"
    "在梦中，真由喜我，在外婆的法事结束后，和妈妈告别后，一个人去外婆的墓碑前祭拜。"
    "但是，不知为什么，冈伦也来了。"
    "虽然很诧异，但却非常开心。"
    "最近，我们说话的时间少了很多，稍微觉得有些寂寞呢。"
    "所以好想见见冈伦啊"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0003"
    $ current_voice = "voice/MAY01A_MAY0003.ogg"
    "真由理" "「啊、对了。趁还没忘记，必须得把日记写了。真由喜我、很健忘呢」"
    window hide
    hide background-png 
    $ loadBG(0,"IBG010A")








    hide screen phonebtn
    "我先把蓝色呜啪放回原处，然后打开了放在桌子上的日记本。"
    "这个日记本，不知不觉中，变成了只记录好事儿的东西了。"
    "孤独的时候，悲伤的时候，只要打开这本日记看上几眼，仅仅如此就会开心起来了。"
    "不是每天都会去写它，虽说是日记，但偶尔也会变成周记，月记。"
    "做到开心的梦时，也会把梦的内容记录下来。"
    "但是，最近，不知为何一直做着可怕的梦，所以记录梦的日记也已经很久没有写了呢。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0004"
    $ current_voice = "voice/MAY01A_MAY0004.ogg"
    "真由理" "「──在梦中、我先到外婆的墓碑前去祭拜。在那儿之后、突然、在这个绝妙的时机，冈伦出现了……」"
    "一边回忆着梦的内容，一边写着日记。"
    "我去和外婆相见的事，明明没有告诉冈伦。所以我问道「好厉害啊、为什么会知道我在这里？」──"
    "冈伦说「人质的位置我当然了然于心了」"
    "虽然有些……不。"
    "非常的开心。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0005"
    $ current_voice = "voice/MAY01A_MAY0005.ogg"
    "真由理" "「难得地和冈伦说了很多话。祭拜之后，也一起去吃了平常总是会吃的团子。过去的事无论是什么都很令人怀念呢……」"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0006"
    $ current_voice = "voice/MAY01A_MAY0006.ogg"
    "真由理" "「……团子、因为会想到外婆、虽然会有些悲伤的味道……但即便这样也会觉得值得怀念、十分美味……呢。那个梦、能应验该多好～」"
    "冈伦他，直到上高中为止，一直陪我去祭拜外婆的墓。那个时候也十分令人怀念啊。"
    "在梦中吃的团子，和过去每次祭拜完墓后和冈伦一起吃的团子是一样的味道，十分美味。"
    "想起了外婆经常做给我的团子。"
    "明天，外婆的法事结束后，也别忘了去吃。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0007"
    $ current_voice = "voice/MAY01A_MAY0007.ogg"
    "真由理" "「最近冈伦有些奇怪，从前我不开心时他总是会鼓励我，但最近，连我的梦中也会出现」"
    "最近，如果做恶梦的话，在梦中，冈伦必然会来救我呢。"
    "但是，那时的冈伦……总是那么的失落，悲伤呢。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0008"
    $ current_voice = "voice/MAY01A_MAY0008.ogg"
    "真由理" "「到现在为止，虽然冈伦一直在保护着我，但在梦里都会出现……实在是有些……」"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0009"
    $ current_voice = "voice/MAY01A_MAY0009.ogg"
    "真由理" "「是我太依赖冈伦了吗？又或者是冈伦……太温柔了吗……」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TSUNDERE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TSUNDERE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TSUNDERE"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])

    "他是非常腼腆，{color=#f00}傲娇{/color}以及无可救药的{color=#f00}厨二病的人{/color}，即使这样、冈伦却是个十分温柔的人。"
    "一直在他身边的话，马上就会明白的。"
    "外婆去世的时候，冈伦也一直保护着因为打击而变得沉默的我。"
    "在这样的冈伦身边呆着不仅心情会很好，也会让我安心下来。"
    "也会想一直这样呆在冈伦的身边。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0010"
    $ current_voice = "voice/MAY01A_MAY0010.ogg"
    "真由理" "「虽然在梦中冈伦对我说“真由里保持原样就好，什么也不用改变”」"
    "但即使不是在梦中，我想冈伦也会说那样的话呢。"
    window hide


    $ loadBG(0,"BG62N")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0011"
    $ current_voice = "voice/MAY01A_MAY0011.ogg"
    "真由理" "「但是，这样娇气果然是不行的吧？」"
    "抓着呜啪的脑袋叹着气"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0012"
    $ current_voice = "voice/MAY01A_MAY0012.ogg"
    "真由理" "「真由喜啊，不想做冈伦的包袱……」"
    "最近的冈伦，像是一个人正承受着什么巨大烦恼的样子。"
    "烦恼的原因大概是和我有什么关系吧。"
    "因为，冈伦他，会不时盯着我的脸看，露出一瞬间安心的表情后，又会变成了像是非常痛苦的表情。"
    "每次看到露出那种表情的冈伦，我都会感到痛苦得不能呼吸。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0013"
    $ current_voice = "voice/MAY01A_MAY0013.ogg"
    "真由理" "「因为冈伦太温柔了，时常会觉得非常对不起他。」"
    "明明知道自己成了冈伦的包袱，但却不知道变成这样的理由，为自己什么也帮不上忙而感到悲伤。"
    "好几次想向冈伦打听原因，但看着冈伦一副什么也不想听的样子，终归是没有说出口。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0014"
    $ current_voice = "voice/MAY01A_MAY0014.ogg"
    "真由理" "「呐，外婆」"
    hide backgroung-png 
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn

    play se "SGSE330L" loop
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWAICHUH"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWAICHUH"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KWAICHUH"])
    "闭上眼睛，将外婆留给我的怀表、{color=#f00}怀酱{/color}放到耳边、和外婆说话"
    "怀表指针跳动的声音仿佛外婆的心跳声一样。"
    "这样做的话，会非常地安心。"
    "像是外婆就在身边，立刻能倾听我说的话。"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0015"
    $ current_voice = "voice/MAY01A_MAY0015.ogg"
    "真由理" "「果然、真由喜我、像以前一样一直当冈伦的人质是不行的吧？」"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0016"
    $ current_voice = "voice/MAY01A_MAY0016.ogg"
    "真由理" "「总之──必须得独立呢」"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0017"
    $ current_voice = "voice/MAY01A_MAY0017.ogg"
    "真由理" "「……我知道。真的知道」"
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0018"
    $ current_voice = "voice/MAY01A_MAY0018.ogg"
    "真由理" "「……但是」"
    window hide

    $ loadBG(0,"IBG010A")

    stop se
    hide screen phonebtn
    show screen phoneSD1
    "在日记的最后，用小字试着写下了『不做人质』几个字。"
    "但是，看到这样的文字，不知为何会变得害怕起来了。"
    "当即用橡皮把它们擦掉了。"
    "不继续当冈伦人质的方法。"
    "倒是想到了一个方法。"
    "但是，尽量不想使用这个方法。"
    window hide


    $ loadBG(2,"BG62N")



    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY01A_MAY0019"
    $ current_voice = "voice/MAY01A_MAY0019.ogg"
    "真由理" "「必须找到其他的方法。一定会找到好方法的。」"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    "从打开的窗户仰望星空，像往常那样寻找着同一颗星星。"
    "立刻就找到了那颗星星呢。"
    "这颗星星为什么总是在同样的地方呢？"
    "在北方的天空中，闪耀着非常耀眼的光辉的北极星(Polaris)。"
    "永远在同样的地方，看着这永恒持续闪耀着的北极星，不知为何我突然安心下来了。"
    "像北极星那样，我也能永远不改变该多好啊。"

    stop bgm 

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
