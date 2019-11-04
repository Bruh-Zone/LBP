label SGFD2_MAY05B:
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG64N")

    play bgm "FD2BGM08"

    $ date="8/16"
    $ day = "MON"
    show screen phonebtn
    show screen phoneSD1

    "夜晚的目的鸦雀无声，很能让人安心。"
    "并不觉得恐怖。"
    "因为，最喜欢的奶奶就沉睡在这个地方。"
    "如果是奶奶的幽灵的话，随时都欢迎。"
    "月光，温柔地照亮了四周。"
    window hide


    $ loadBG(2,"IBG044D")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0180"
    $ current_voice = "voice/MAY05A_MAY0180.ogg"
    "真由理" "「月亮公公，真漂亮呢～」"
    "有那么一瞬间，看着夜空中的月亮着迷了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0181"
    $ current_voice = "voice/MAY05A_MAY0181.ogg"
    "真由理" "「奶奶的法事，晴天真是太好了，真由喜是雨女的样子，担心了一下。但是妈妈她们那边也祈求了不要下雨」"
    window hide


    $ loadBG(2,"BG64N")



    show screen phonebtn
    "目光落到了奶奶的墓上，轻轻地笑了起来。"
    "在墓前，有着真由理为她供上的百合花与团子。"
    "这两个，是给奶奶扫墓不可或缺的东西。"
    "那个时候。"
    stop bgm 
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0182"
    $ current_voice = "voice/MAY05A_MAY0182.ogg"
    "真由理" "「唔！？」"
    "突然，感觉到了人的气息，我抬起了头。"
    "环视着周围。"
    "谁也没有。"
    "和刚刚一样没有任何改变的安静的光景而已。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0183"
    $ current_voice = "voice/MAY05A_MAY0183.ogg"
    "真由理" "「刚刚，感觉好像有谁在，可能是错觉吧？」"
    "再一次，环视着四周。"
    "但是，果然谁也没有。"
    "但是，刚刚，明明感觉到有谁在真由喜的旁边……"
    "感觉着不可思议，抬起头。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0184"
    $ current_voice = "voice/MAY05A_MAY0184.ogg"
    "真由理" "「我以为是有谁在玩试胆大会……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0185"
    $ current_voice = "voice/MAY05A_MAY0185.ogg"
    "真由理" "「试胆大会……」"
    "感觉就是那个某人，说过试胆大会什么的。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0186"
    $ current_voice = "voice/MAY05A_MAY0186.ogg"
    "真由理" "「明明不可能的，真奇怪……」"
    play bgm "FD2BGM06"
    "这里，明明就只有真由喜自己一个人。"
    "一瞬间。睡着了，梦到了一个很短的梦。"
    "在午休之后，上课时无意间突然睡着了的时候经常梦得到的那种很短的梦。"
    "因为今天为了奶奶的法事忙得不可开交。"
    "可能有点累了呢。"
    "法事结束之后，真由理和妈妈他们分开来到了奶奶的墓前。"
    "在奶奶的墓前蹲下后双手合十。"
    window hide


    $ loadBG(2,"IBG044D")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0187"
    $ current_voice = "voice/MAY05A_MAY0187.ogg"
    "真由理" "「奶奶，今年也是奶奶最喜欢的团子，很认真做的哟。当然，是奶奶教给我的方法。」"
    "夜空中的星星闪烁着，在附和着真由喜一样。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0188"
    $ current_voice = "voice/MAY05A_MAY0188.ogg"
    "真由理" "「在奶奶死之前，一起做团子真的太好了，在奶奶法事的时候，想着有好好地履行约定真的太好了。」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0189"
    $ current_voice = "voice/MAY05A_MAY0189.ogg"
    "真由理" "「哪怕错了一步，也可能无法履行和奶奶的约定。」"
    "奶奶死之前的那一天，真由理和奶奶约定好了要一起做团子。"
    "但是，那天，朋友邀请我去夏日祭，我想着和奶奶的约定就下一次再说吧。"
    "但是，妈妈说「再小的约定，也要遵守」，所以没去夏日祭而去找奶奶玩了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0190"
    $ current_voice = "voice/MAY05A_MAY0190.ogg"
    "真由理" "「奶奶和真由理的约定，为什么妈妈会知道，直到现在我也觉得不可思议，为什么呢？奶奶」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    "那天，和奶奶一起做团子，真好吃呢，吃完后。没多久奶奶就倒下了。"
    "慌张地和妈妈联系后，把奶奶送上急救车去医院了。"
    "但是，就那样，在半夜就去世了。"
    "如果，那天，我打破了和奶奶的约定的话，绝对会很后悔的。"
    window hide


    $ loadBG(2,"BG64N")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0191"
    $ current_voice = "voice/MAY05A_MAY0191.ogg"
    "真由理" "「其实，奶奶。时不时，我会在梦中梦到打破了和奶奶的约定。」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0192"
    $ current_voice = "voice/MAY05A_MAY0192.ogg"
    "真由理" "「……很恐怖的梦。」"
    "什么也听不到，什么也感觉不到的灰色的被世界封闭了的梦。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0193"
    $ current_voice = "voice/MAY05A_MAY0193.ogg"
    "真由理" "「但是，绝对会有来救真由喜的人。」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0194"
    $ current_voice = "voice/MAY05A_MAY0194.ogg"
    "真由理" "「那个人，每次在真由喜做噩梦的时候，就会从什么地方突然出来，救出梦中的真由喜。」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0195"
    $ current_voice = "voice/MAY05A_MAY0195.ogg"
    "真由理" "「虽然应该是不认识的人，可能是很多次在梦中出现的原因吧，感觉并不是第一次见，感觉是以前在某个地方见过的样子……」"
    "为什么呢。"
    "突然胸口开始疼了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0196"
    $ current_voice = "voice/MAY05A_MAY0196.ogg"
    "真由理" "「……嗯？」"
    "不知道的情况下，从眼睛里流出了一滴眼泪，很惊讶。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0197"
    $ current_voice = "voice/MAY05A_MAY0197.ogg"
    "真由理" "「明明没有什么伤心的事……」"
    "眼泪一次次地从脸颊流了下去。"
    "不明所以的眼泪，所以并不清楚应该怎么办"
    "好像是，失去了什么特别重要的东西的感觉。"
    "有这种感觉。"
    "但是，就是不明白那是什么。"
    "那特别的伤心悲痛。"
    "如果这个时候奶奶在的话──"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0198"
    $ current_voice = "voice/MAY05A_MAY0198.ogg"
    "真由理" "「奶奶……好想见你……」"
    "从怀中取出怀酱，放在耳边闭眼倾听。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "想起了一直在真由喜耳朵旁边说话的奶奶的笑容。"
    "这样的话，会感觉奶奶就在身边，不明的不安会稍微缓和一些。"
    "但是，心里像是被钻了个空一样的感觉，还是没有改变。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
