label SGFD2_NAE09A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")

    play bgm "FD2BGM01"

    $ date="7/28"
    $ day = "SAT"
    hide screen phonebtn
    hide screen phoneSD1

    "从桶子叔叔消失到现在，已经过了两周了。"
    "在那之后——"
    "父亲的大楼因为起了点小火，连消防车都来了。"
    "桶子叔叔的身影，从大楼里完全消失了"
    "不只是桶子叔叔，花了一周以上做出来的时间机器也消失不见了。"
    "并不是被烧毁了。"
    "那种是从最开始就没有存在过的消失。"
    "大概是被黑衣人们带走了吧。"
    "就算如此——"
    "桶子叔叔说过。"
    "如果Ｄｍａｉｌ发送成功了，世界线就会发生改变，而发送过邮件这一事实也会消失。"
    "但是，我仍然记得和胖胖的兔子先生一起度过的９天。"
    "那就意味着，Ｄｍａｉｌ的发送失败了吧。"
    "就是Ｄｍａｉｌ发出去了，我和桶子叔叔在Ｌａｂ的这段日子也就会不复存在吧。"
    "几天后由不明身份的人给我寄来的手机里面，也没有Ｄｍａｉｌ的发送记录。"
    "就算现在回想起来。"
    "那９天的日子，就好像梦境一般。"
    window hide


    $ loadBG(2,"BG79A7",at=[Transform(yalign=1.0)])







    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0000"
    $ current_voice = "voice/NAE09A_NAE0000.ogg"
    "绹" "「…………」"
    "放了暑假以后，社团活动一直很忙，所以就从来没有来过这里。"
    "今天刚好是两周之后，所以就试着来看了一下。"
    window hide
    $ loadBG(2,"BG79A7",at=[Transform(yalign=0.6)])





    hide screen phonebtn
    "这么一看，还真是了不得。"
    "二楼的窗户被弄碎了。"
    "Ｌａｂ里面也一定很惨烈吧。"
    "但是现在已经没有翻新的计划了。"
    "虽然说幸高叔叔应该愿意出这笔钱，但是考虑到目前这幢大楼并没有什么用处，所以还是算了。"
    "当然，还是很想什么时候能把它修好的。"
    "让它变成就算“Ｌａｂｍｅｍ”的大家回来也没有问题的状态。"
    "但是，现在还是让它保持这样吧。"
    "如果翻修的话，感觉和桶子叔叔一起度过的日子就真的要消失了。"
    "虽然到最后还是不是能和桶子叔叔相处得很好——"
    "但是就这么消失的话，果然还是有些寂寞呢。"
    "多亏您的帮助，连社团活动都不怎么能参与进去了呢，呐，叔叔。"
    window hide





    show screen phonebtn
    "试着环顾周围。"
    "今天并没有看到“黑衣人”。"
    "虽然今天没有看到，好像从两周前桶子叔叔消失了以后，这些人就不见了呢。"
    "是因为已经捉到了桶子叔叔呢，还是因为去别的地方搜查桶子叔叔的下落了呢。"
    "不小心胡思乱想了。"
    "但是，桶子叔叔的话，一定能一边气喘吁吁一边机敏地逃掉吧。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0001"
    $ current_voice = "voice/NAE09A_NAE0001.ogg"
    "绹" "「噗……」"
    "想象了一下那画面，我忍俊不禁。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0002"
    $ current_voice = "voice/NAE09A_NAE0002.ogg"
    "绹" "「恩？」"
    "这个时候，被风吹过来的小纸片挂在了我的脚上。"
    "漫不经心地捡起来看了一眼。"
    "湿哒哒的，因为被水泡了上面手写的文字都已经快消失了。"
    "但是看出来了上面写着的是『未来道具研究所』。"
    "这个……是楼梯边上的邮筒上贴着的纸条吧。"
    "本来是用不干胶什么的固定的吧，所以现在才会脱落下来。"
    "或许，不该让它掉下来的……"
    "我写一个新的贴回去会比较好吧。"
    "这么想着，走到了邮筒面前。"
    "在那里，我注意到了。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0003"
    $ current_voice = "voice/NAE09A_NAE0003.ogg"
    "绹" "「啊……」"
    "在１楼，『显像管工房』的邮筒。"
    "在那里面，有一封信。"
    "是什么时候放进去的呢？"
    "今天？昨天？１周之前？难道说——"
    "在这２年里，我不知道来到过这里几次，但是最后一次调查邮筒的，是什么时候？"
    "记不太清楚了。"
    "从再次遇到桶子叔叔开始，就再也没有使用过这个楼梯，所以也不会有调查过这个邮筒。"
    "也许是电力公司或者水务部门的请求书也说不定。"
    "这么想着，我打开了邮筒，将信取了出来。"
    "漫不经心地看了看收件人。"
    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0004"
    $ current_voice = "voice/NAE09A_NAE0004.ogg"
    "绹" "「──」"
    "感觉呼吸仿佛要停止了一样。"
    window hide


    $ loadBG(2,"IBG046A")



    hide screen phonebtn
    "这，好像是私人信件……"
    "并没有邮局的印章。"
    "直接，投递到这里来的。"
    "翻到另一面，也没有看到寄件人。"
    "但是看到了字以后，就马上明白是谁写的了。"
    "不可能忘记的——"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0005"
    $ current_voice = "voice/NAE09A_NAE0005.ogg"
    "绹" "「这是爸爸的字啊……」"
    "握着信的手指，颤抖着。"
    "也许这封信是因为我发送的Ｄｍａｉｌ，才会被放在这里的呢？"
    "是读了我的Ｄｍａｉｌ之后，爸爸才会在这里给我答复的吗？"
    "我用颤抖的手指，撕开信封。"
    "在里面，有一封信笺。"
    "上面写着寥寥数句。"
    window hide
    play se "SGSE221"



    $ loadBG(2,"IBG047A")



    hide screen phonebtn
    play bgm "FD2BGM09"

    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0006"
    $ current_voice = "voice/NAE09A_NAE0006.ogg"
    "绹" "「啊……」"
    "眼泪夺眶而出。"
    "但是，这份眼泪并不是平时的我的懦弱的眼泪。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0007"
    $ current_voice = "voice/NAE09A_NAE0007.ogg"
    "绹" "「爸爸……」"
    "这份眼泪是，欣喜的泪水。"
    "所以，就算不去忍住，也没有关系。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0008"
    $ current_voice = "voice/NAE09A_NAE0008.ogg"
    "绹" "「谢谢你……」"

    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE005A"]]["Check"]=True


    $ loadBG(2,"EV_NAE005A")



    hide screen phonebtn
    "抬头仰望天空。"
    "在大楼与大楼之间露出的蓝天，因为自己的泪水而稍有模糊。"
    "夏天已经降临。"
    "从那时起，已经过了两年。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0009"
    $ current_voice = "voice/NAE09A_NAE0009.ogg"
    "绹" "「我，活得很好哟」"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0010"
    $ current_voice = "voice/NAE09A_NAE0010.ogg"
    "绹" "「所以，你一直在守护着我哦」"
    "对了，给留未穂姐姐打个电话吧。"
    "想告诉她，姐姐说的并不是谎话。"
    "因为会和父亲再次相见的，所以和“Ｌａｂｍｅｍ”的大家也是，总有一天也会再见的。"
    "有那样的预感。"
    $ stopvoc("NAE")
    play NAE "NAE09A_NAE0011"
    $ current_voice = "voice/NAE09A_NAE0011.ogg"
    "绹" "「那，下次再见咯」"

    stop bgm 
    "对着父亲的大楼轻声低语道。"
    "我朝着在盛夏的日光照射下的秋叶原车站方向，大步前进。"

    hide screen phoneSD1
    hide screen phonebtn
    window hide








    $ renpy.movie_cutscene("video/fd2_gend.avi")
    hide screen phonebtn
    scene expression Solid("000000")  with fade
    "月晕的彩虹桥·完成"

    return






    return
