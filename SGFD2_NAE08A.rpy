label SGFD2_NAE08A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG04A4")
    $ loadBG(0,"IBG045B",png=True)



    play bgm "BGM15_2"

    $ date="7/14"
    $ day = "SAT"
    hide screen phonebtn
    show screen phoneSD1

    "一言不发，全神贯注地进行着工作。"
    "电焊铁也慢慢会用了。"
    "而且，本来这件事也没有很难。"
    "桶子叔叔，昨天和今天也都在２楼认真地干活。"
    "因为我在１楼，完全没有注意到过桶子叔叔的声音和存在。"
    "如果是几天前的我的话，肯定会因为不安而去２楼偷偷确认一下吧。"
    "但是尤其是现在，丝毫感受不到那种不安。"
    "因为我知道桶子叔叔一个人完全不能出去。也就是说，他现在自己把自己困在了这里。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0000"
    $ current_voice = "voice/NAE08A_NAE0000.ogg"
    "绹" "「…………」"
    "总感觉有些，不可思议。"
    "２年前，也是在这家店里，爸爸每天修理着电视机。"
    "我在那时，只是静静地看着。"
    "那个时候，总想着自己以后肯定不会继承爸爸的店吧。"
    "那样的我如今却在这里做着这样的事，和爸爸一样，修理着显像管电视机。"
    "虽然我现在更加觉得，这家店只靠我一个人是肯定开不起来的。"
    "就算是潜移默化吧，但是我对于自己能够好好地接手父亲留下了的东西这一点感到很高兴。"

    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0001"
    $ current_voice = "voice/NAE08A_NAE0001.ogg"
    "绹" "「完成……了……」"
    "焊好了最后一个地方。"
    "因为不能叫出来，所以只好咬紧牙关，摆出了一个胜利的姿势。"
    "这样的话，我的工作就算完成了。"
    "但是，问题是，光靠这些焊接，能够把这台４２型的显像管电视机修好吗？"
    "这只能听天由命了。"
    "但是——"
    "我当然希望它能修好。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG04A4")

    show screen phonebtn
    show screen phoneSD1
    "被拆开的４２型显像管电视机又一次恢复到了原来的样子。"
    "将电子线路板放回原来的地方。"
    "将螺丝钉一颗颗拧回去。"
    "光是这些就花了我一个小时以上。"
    window hide
    $ loadBG(0,"IBG045A",png=True)

    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0002"
    $ current_voice = "voice/NAE08A_NAE0002.ogg"
    "绹" "「呼……」"
    "大概，是恢复原状了。"
    "螺丝也没有剩下来。"
    "肯定没问题的……应该。"
    window hide
    $ loadBG(0,"BG04A3")






    hide background-png  with dissolve

    show screen phonebtn
    show screen phoneSD1
    "我朝着通向二楼的小洞喊了几声。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0003"
    $ current_voice = "voice/NAE08A_NAE0003.ogg"
    "绹" "「桶子叔叔，桶子叔叔」"
    "很快就听到了脚步声，接着就看到了桶子叔叔的脸。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0000"
    $ current_voice = "voice/NAE08A_DAR0000.ogg"
    "至" "「怎么了？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0004"
    $ current_voice = "voice/NAE08A_NAE0004.ogg"
    "绹" "「……修理、结束了」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0001"
    $ current_voice = "voice/NAE08A_DAR0001.ogg"
    "至" "「哦哦。能打开吗？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0005"
    $ current_voice = "voice/NAE08A_NAE0005.ogg"
    "绹" "「现在就来试一下」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0002"
    $ current_voice = "voice/NAE08A_DAR0002.ogg"
    "至" "「那，拜托咯」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0006"
    $ current_voice = "voice/NAE08A_NAE0006.ogg"
    "绹" "「唔……」"
    "怎，怎么办啊。紧张起来了。"
    "如果不行的话，不就意味着我到现在的努力都是徒劳无功吗。"
    "桶子叔叔也不能发送Ｄｍａｉｌ了。"
    "心，砰砰直跳。"
    "大大地深呼吸了一次。"
    "然后，用眼神和桶子叔叔做了下交流。"
    "将电源线插入插座。"
    "按下了４２型显像管电视机的电源开关——"
    window hide
    play se "SGSE339"

    play se "SGSE323"



    $ loadBG(2,"BG04A5")



    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0007"
    $ current_voice = "voice/NAE08A_NAE0007.ogg"
    "绹" "「啊……！」"
    play bgm "FD2BGM08"
    "画面亮了起来。"
    "虽然出现的只有噪点。"
    "在那个瞬间，我感觉自己几乎要跳起来了。"
    "赶紧朝桶子叔叔的方向看去。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0003"
    $ current_voice = "voice/NAE08A_DAR0003.ogg"
    "至" "「绹酱、ＧＪ。不愧是显像管小姐呢。」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0008"
    $ current_voice = "voice/NAE08A_NAE0008.ogg"
    "绹" "「恩……！」"
    "亮起来了。"
    "亮起来了哦，爸爸。"
    "太好了……"
    "于是这样，作为协力者的我的工作就告一段落。"
    "好好地完成了呢。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG03A7")


    show screen phoneSD1
    play se "SGSE342L" loop
    "在那之后的两小时里，我没有什么要做的，于是就坐在桶子叔叔的身后看他敲键盘。"
    "电脑画面上显示出的字符应该是有什么含义的吧，但是我完全搞不懂。对我来说就像是暗号或者咒语一样。"

    $ targetmailid = 478

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    "但是桶子叔叔的手从刚才开始就完全没有停下来过。"
    call CHECK_RM_RECEIVE
    "如果输入完成了，就意味着时间机器完成了，刚才他是这么和我说的。"
    call CHECK_RM_RECEIVE
    "虽然只是看着他，但是从刚才开始我就已经跃跃欲试了。"
    call CHECK_RM_RECEIVE
    "时间机器什么的，只在漫画或者电影里面见过。"
    call CHECK_RM_RECEIVE
    "但是一想到现在就要在我的眼前完成了。"
    call CHECK_RM_RECEIVE
    "但是这可是绝对不能告诉朋友们的事啊。"

    call CHECK_RM_RECEIVE


    play se "SGSE143"


    stop se
    "这么想着，桶子叔叔用力地敲了一下键盘，手停了下来。"
    "就好像钢琴家弹奏出最后一个音符一样。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB02"),"True","lh/DAR_CSB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0004"
    $ current_voice = "voice/NAE08A_DAR0004.ogg"
    "至" "「……Ｍｉｓｓｉｏｎ　Ｃｏｍｐｌｅｔｅ」"
    "朝着我露出了微笑。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0009"
    $ current_voice = "voice/NAE08A_NAE0009.ogg"
    "绹" "「那么……完成了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0005"
    $ current_voice = "voice/NAE08A_DAR0005.ogg"
    "至" "「恩。电话微波炉ｖｅｒ３．００　天王寺Ｅｄｉｔｉｏｎ完成。Ｋｉｒａ」"
    window hide


    $ loadBG(2,"BG03A7S")



    hide screen phonebtn
    play bgm "FD2BGM08"

    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0010"
    $ current_voice = "voice/NAE08A_NAE0010.ogg"
    "绹" "「这就是……时间机器……」"
    "从外观上看，只不过是把微波炉和电脑用电缆连了起来而已。"
    "我还以为会是什么更让人吃惊的造型。"
    "结果看起来很普通吗。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0006"
    $ current_voice = "voice/NAE08A_DAR0006.ogg"
    "至" "「嘛，好歹我也是打算完美地复现２年前的电话微波炉啊」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0007"
    $ current_voice = "voice/NAE08A_DAR0007.ogg"
    "至" "「但是两年前的那次，看来完全是偶然才成功的。因为不可能完美地再现了，就算能运作起来估计Ｄｍａｉｌ也有可能发不出去」"
    "是……这样啊。"
    "但是，已经努力到了这一步，还是想试试看啊。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0008"
    $ current_voice = "voice/NAE08A_DAR0008.ogg"
    "至" "「差不多了，让我们试试它到底能不能开起来吧」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0009"
    $ current_voice = "voice/NAE08A_DAR0009.ogg"
    "至" "「如果不准备直接尝试的话，失败的可能性会很大吧」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0010"
    $ current_voice = "voice/NAE08A_DAR0010.ogg"
    "至" "「成功的话，我们在观测到变化之前世界线就会发生改变吧」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0011"
    $ current_voice = "voice/NAE08A_DAR0011.ogg"
    "至" "「这可是很严重的。可能我们就白忙活了」"
    window hide



    $ loadBG(2,"BG03A7")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA03"),"True","lh/DAR_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0011"
    $ current_voice = "voice/NAE08A_NAE0011.ogg"
    "绹" "「就算如此……也是要用的吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0012"
    $ current_voice = "voice/NAE08A_DAR0012.ogg"
    "至" "「当然了啊……！我可是为了这个才忍住一周没有玩工口游戏在这里埋头苦干的啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA06"),"True","lh/DAR_CSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0013"
    $ current_voice = "voice/NAE08A_DAR0013.ogg"
    "至" "「太漫长了……长过头了……人的忍耐可是有限的啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0014"
    $ current_voice = "voice/NAE08A_DAR0014.ogg"
    "至" "「而且被可爱的女中学生摸了好几次屁股，我的理性早就不知道滚到哪里去了啊！」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0015"
    $ current_voice = "voice/NAE08A_DAR0015.ogg"
    "至" "「不准嘲笑我还是个处男！」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0012"
    $ current_voice = "voice/NAE08A_NAE0012.ogg"
    "绹" "「咿……」"
    "好，好可怕……"
    "怎么突然就生气了。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0013"
    $ current_voice = "voice/NAE08A_NAE0013.ogg"
    "绹" "「声，声音如果太大的话，就要被外面的黑衣人注意到了哦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA03"),"True","lh/DAR_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0016"
    $ current_voice = "voice/NAE08A_DAR0016.ogg"
    "至" "「抱歉鸟」"
    "说起来，“Ｃｈｕ　ｎａｎ”是什么？"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0014"
    $ current_voice = "voice/NAE08A_NAE0014.ogg"
    "绹" "「那么，什么时候用呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0017"
    $ current_voice = "voice/NAE08A_DAR0017.ogg"
    "至" "「今天」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0015"
    $ current_voice = "voice/NAE08A_NAE0015.ogg"
    "绹" "「诶……」"
    "这么急啊。"
    "完成的那天就要用啊。"
    "但是，仔细想一想的话，这是理所当然的。"
    "是为了发送Ｄｍａｉｌ，才制作出来的。"
    "桶子叔叔本身又在被坏人追赶着。"
    "到现在为止还没有被外面的黑衣人发现这一点，简直是奇迹。"
    "所以，并没有悠闲的时间。"
    "桶子叔叔，也会让我发送Ｄｍａｉｌ吧？"
    "但是就算他不让我发，也没有办法。"
    "我只是单纯的作为协力者而已。"
    "桶子叔叔也不想让我太过于深入了解他们的事情。"
    "所以——"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0018"
    $ current_voice = "voice/NAE08A_DAR0018.ogg"
    "至" "「要发送的Ｄｍａｉｌ，有我的一封和绹酱的一封，共计２封」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0016"
    $ current_voice = "voice/NAE08A_NAE0016.ogg"
    "绹" "「诶……？」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0019"
    $ current_voice = "voice/NAE08A_DAR0019.ogg"
    "至" "「发送第一封的时候，外面的家伙就应该会注意到我们的存在了。所以第二封能不能发出去，只能看运气了。」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0020"
    $ current_voice = "voice/NAE08A_DAR0020.ogg"
    "至" "「绹酱，就算如此也没问题吧？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0017"
    $ current_voice = "voice/NAE08A_NAE0017.ogg"
    "绹" "「啊，好，好的」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0021"
    $ current_voice = "voice/NAE08A_DAR0021.ogg"
    "至" "「同意的话，就告诉我你想要给谁发吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔又转过去看着ＰＣ的显示器。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0022"
    $ current_voice = "voice/NAE08A_DAR0022.ogg"
    "至" "「要先设定好才能发嘛」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0018"
    $ current_voice = "voice/NAE08A_NAE0018.ogg"
    "绹" "「让我发送……真的好吗？」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0023"
    $ current_voice = "voice/NAE08A_DAR0023.ogg"
    "至" "「但是我拒绝。虽然这么说ＯＫ的哦。绹酱可以自己选择想发给谁」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0019"
    $ current_voice = "voice/NAE08A_NAE0019.ogg"
    "绹" "「…………」"
    "我能发啊……真好。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0024"
    $ current_voice = "voice/NAE08A_DAR0024.ogg"
    "至" "「邮件本身，是从绹酱的手机通过电话微波炉来发送的」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0025"
    $ current_voice = "voice/NAE08A_DAR0025.ogg"
    "至" "「请注意一次发生的内容不能超过１８个全角文字」"
    "我到底该给谁发呢。"
    "真由理姐姐？"
    "铃羽姐姐？"
    "冈伦叔叔？"
    "……不对。"
    "虽然说，当然有想对Ｌａｂｍｅｍ的人们说的话语。"
    "但是，比起那些……"
    "最想把我现在的情况，告诉他的，果然只有。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    "爸爸、"
    window hide



    $ loadBG(0,"BG03A7")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0020"
    $ current_voice = "voice/NAE08A_NAE0020.ogg"
    "绹" "「……想好了。」"
    "我将爸爸的手机号告诉了桶子叔叔，于是桶子叔叔就将它输入了电脑。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我取出自己的手机，编写起了邮件。"
    "……想要告诉父亲的，事情。"
    "虽然，有很多很多、"
    "只靠１８个全角文字，根本无法传达。"
    "我现在最想告诉父亲的是——"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0021"
    $ current_voice = "voice/NAE08A_NAE0021.ogg"
    "绹" "「…………」"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_NAE08A_EDIT_TEN01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_NAE08A_SEND_TEN01"]
    call send_mail (id=[289,290,291])


    "１８个文字，写成这样我已经尽力了。"
    "但是……感觉这样就满足了。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0022"
    $ current_voice = "voice/NAE08A_NAE0022.ogg"
    "绹" "「桶子叔叔，写完了」"
    window hide
    call hide_phone
    hide screen phonebtn
    hide screen phoneSD1
    "我交出手机。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "桶子叔叔接过手机，确认了一遍内容。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0023"
    $ current_voice = "voice/NAE08A_NAE0023.ogg"
    "绹" "「这样就可以了吧？」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0026"
    $ current_voice = "voice/NAE08A_DAR0026.ogg"
    "至" "「恩，感觉非常的完美」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0027"
    $ current_voice = "voice/NAE08A_DAR0027.ogg"
    "至" "「那，把发件人设成电话微波炉了──」"
    play se "SGSE343"

    "这个时候，桶子叔叔的大肚子发出了巨大的轰鸣声。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB03"),"True","lh/DAR_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0028"
    $ current_voice = "voice/NAE08A_DAR0028.ogg"
    "至" "「唔哦，肚子饿了」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0024"
    $ current_voice = "voice/NAE08A_NAE0024.ogg"
    "绹" "「买了的食物，还有剩下的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0029"
    $ current_voice = "voice/NAE08A_DAR0029.ogg"
    "至" "「对于昨天晚上没能忍住全部吃完的我，诶嘿」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0025"
    $ current_voice = "voice/NAE08A_NAE0025.ogg"
    "绹" "「深夜吃东西的话，会变胖的哟……」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0030"
    $ current_voice = "voice/NAE08A_DAR0030.ogg"
    "至" "「但是那样很不错啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB08"),"True","lh/DAR_CSB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0031"
    $ current_voice = "voice/NAE08A_DAR0031.ogg"
    "至" "「啊，是哦。不好意思绹酱，能再帮我买一回吗？」"
    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0026"
    $ current_voice = "voice/NAE08A_NAE0026.ogg"
    "绹" "「诶……？」"
    "有某种预感。"
    play bgm "FD2BGM06"

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0032"
    $ current_voice = "voice/NAE08A_DAR0032.ogg"
    "至" "「嘛，感觉这就好像我在秋叶原的最后的晚餐一样啊」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0033"
    $ current_voice = "voice/NAE08A_DAR0033.ogg"
    "至" "「如果启动电话微波炉的话，大楼会晃起来了。这可比喝了可乐以后的打嗝声要被容易发现的多了」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0027"
    $ current_voice = "voice/NAE08A_NAE0027.ogg"
    "绹" "「桶子叔叔……」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0034"
    $ current_voice = "voice/NAE08A_DAR0034.ogg"
    "至" "「而且说起来，我现在从窗户里也没法逃掉啊」"
    "桶子叔叔笑着，将２张千元大钞交了给我。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA08"),"True","lh/DAR_CSA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0035"
    $ current_voice = "voice/NAE08A_DAR0035.ogg"
    "至" "「所以就这样拜托了」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0028"
    $ current_voice = "voice/NAE08A_NAE0028.ogg"
    "绹" "「桶子叔叔，我……」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0036"
    $ current_voice = "voice/NAE08A_DAR0036.ogg"
    "至" "「虽说本来也想拜托你尽可能的搞点披萨什么的，果然那样的话还是太容易暴露了啊」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0029"
    $ current_voice = "voice/NAE08A_NAE0029.ogg"
    "绹" "「不是说那个……」"
    "有那种，预感。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0030"
    $ current_voice = "voice/NAE08A_NAE0030.ogg"
    "绹" "「……时间机器，打算什么时候启动？」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0037"
    $ current_voice = "voice/NAE08A_DAR0037.ogg"
    "至" "「打算在绹酱回来以后吃了东西再启动啊，怎么了吗？」"
    "桶子叔叔用和往常一样的轻浮态度回答了我。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0031"
    $ current_voice = "voice/NAE08A_NAE0031.ogg"
    "绹" "「这样……」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0032"
    $ current_voice = "voice/NAE08A_NAE0032.ogg"
    "绹" "「…………」"
    "已经问不出什么了。"
    "但是，就算什么也不说，我也是明白的。"
    "桶子叔叔，在考虑着什么。"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0038"
    $ current_voice = "voice/NAE08A_DAR0038.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0039"
    $ current_voice = "voice/NAE08A_DAR0039.ogg"
    "至" "「怎么了吗？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0033"
    $ current_voice = "voice/NAE08A_NAE0033.ogg"
    "绹" "「没什么……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB01"),"True","lh/DAR_CMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我站了起来，向桶子叔叔伸出了手。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0034"
    $ current_voice = "voice/NAE08A_NAE0034.ogg"
    "绹" "「叔叔……能和我，握一握手吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB04"),"True","lh/DAR_CMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0040"
    $ current_voice = "voice/NAE08A_DAR0040.ogg"
    "至" "「没，没问题请！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB02"),"True","lh/DAR_CMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "桶子叔叔用自己的衬衫擦了擦手上的汗，然后握住了我的手。"
    "沾满汗水的手。"
    "比我的手大很多的手。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB07"),"True","lh/DAR_CMB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0041"
    $ current_voice = "voice/NAE08A_DAR0041.ogg"
    "至" "「哦哦，和女中学生握手什么的，我现在也加入人生赢家行列了啊……」"
    "不知为何，摆出了一副恶心的表情……"
    window hide


    $ loadBG(2,"BG01A3")



    "我放开桶子叔叔的手之后，去了厕所里。"
    "要不被外面的黑衣人发现从这里出去的话，必须从厕所里的小窗户爬到隔壁的大楼。"
    "桶子叔叔一个人没法从这个小小的窗户里出去。"
    "所以桶子叔叔只有两种方法从这里离开。"
    "打破面朝道路的玻璃跳下去。"
    "或者打开玄关的门堂堂正正地走出去。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0035"
    $ current_voice = "voice/NAE08A_NAE0035.ogg"
    "绹" "「那，我去买东西了」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0042"
    $ current_voice = "voice/NAE08A_DAR0042.ogg"
    "至" "「Ｏｋａｙ　ｄｏｋｅｙ。小心点啊」"
    window hide



    $ loadBG(2,"BG02A3")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0036"
    $ current_voice = "voice/NAE08A_NAE0036.ogg"
    "绹" "「呐，桶子叔叔……」"
    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0043"
    $ current_voice = "voice/NAE08A_DAR0043.ogg"
    "至" "「恩？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0037"
    $ current_voice = "voice/NAE08A_NAE0037.ogg"
    "绹" "「…………」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0038"
    $ current_voice = "voice/NAE08A_NAE0038.ogg"
    "绹" "「……桶子叔叔，真不擅长说谎呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE08A_DAR0044"
    $ current_voice = "voice/NAE08A_DAR0044.ogg"
    "至" "「诶？你在说啥？」"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0039"
    $ current_voice = "voice/NAE08A_NAE0039.ogg"
    "绹" "「没有，没什么」"
    "我笑着挥了挥手——"
    window hide


    $ loadBG(2,"BG_BLACK")



    stop bgm 
    play se "SGSE344"

    "关上了厕所的门。"
    "再见了，桶子叔叔。"
    window hide


    $ loadBG(0,"IBGX048")

    play bgm "FD2BGM08"
    "和平时一样，面无表情的走出大楼。"
    "然后，偷偷地去爸爸的大楼的正面看了一眼。"
    window hide


    $ loadBG(2,"BG79A5",at=[Transform(yalign=1.0)])







    "假装不经意的看了下，果然黑衣人的监视依然继续着。"
    "真的是，每天吃饱了撑着呆在这里啊。"
    "说不定早就已经注意到我和桶子叔叔在大楼里面了。"
    "这么想着就有点慌了。"
    "总之我赶紧朝着车站方向前进。"
    window hide


    $ loadBG(2,"IBGX048")



    "桶子叔叔自从呆在Ｌａｂ里开始，就一直让我买些零食呀便当呀，尽是些对身体不好的东西。"
    "偶尔也吃点别的不好嘛，我这么想道。"
    "果然，还是和平时一样吧。"
    "这么想着的时候，我才走到公园这边。"
    stop bgm 
    "从背后听到了男人们的叫声。"
    "猛地转过身去。"
    window hide


    $ loadBG(2,"BG79A5",at=[Transform(yalign=1.0)])







    play bgm "BGM08"
    "刚才的黑衣人们，跑到了道路上。看起来很慌张的样子。"
    window hide





    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0040"
    $ current_voice = "voice/NAE08A_NAE0040.ogg"
    "绹" "「……！」"
    "我也看到了。"
    "刚才我还在的Ｌａｂ，现在桶子叔叔也在那里的Ｌａｂ。"
    "朝着道路的那窗户里，发出了蓝白色的光芒。"
    "室内好像也充斥着闪光。"

    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0041"
    $ current_voice = "voice/NAE08A_NAE0041.ogg"
    "绹" "「时间机器……」"
    play bgm "FD2BGM06"
    "……预感被验证了。"
    "我果然还是协力者。"
    "我果然还是旁观者。"
    "无法成为当事者。"
    "桶子叔叔，也希望那不要发生。"
    "刚才，他对我说想要我去买东西的时候，我就已经明白这是他的温柔。"
    "我没有戳破他的谎言。"
    "时间机器到底启动了没有。"
    "Ｄｍａｉｌ到底发送到了过去没有。"
    "这些都不能让我知道。"
    window hide
    $ loadBG(0,"BG79A6",at=[Transform(yalign=0.5)])





    play se "SGSE345"








    "Ｌａｂ的窗户破了，发生了小小的爆炸。"
    "烟从室内一直飘出来。"
    "发生了什么。是因为桶子叔叔的操作呢，还是时间机器发生故障了呢，不得而知。"
    "肯定是桶子叔叔为了让我不知道发生了什么才特意搞成那样的吧，我这么想道。"
    window hide





    "黑衣人们，冲进了爸爸的大楼。"
    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0042"
    $ current_voice = "voice/NAE08A_NAE0042.ogg"
    "绹" "「呐，桶子叔叔……」"
    "我从稍远的地方看着这幅光景。"
    window hide





    $ stopvoc("NAE")
    play NAE "NAE08A_NAE0043"
    $ current_voice = "voice/NAE08A_NAE0043.ogg"
    "绹" "「如果我任性地说自己不想去买的话，叔叔会怎么办呢？」"
    "握在手里的２枚千元纸钞，变得有些皱了。"
    "仔细想了想，我手里与桶子叔叔有关的东西，好像只有这两千元。"
    "也就是说，我无法证明桶子叔叔的存在。"
    "真的是……爱丽丝的兔子那样呢。就是胖了很多。"
    "有些哭出来了。"
    "我以不被黑衣人看到的方式，离开了这里。"
    window hide


    $ loadBG(2,"BG18A2")



    "这２千元，在下次见到你的时候，一定会还给你的，叔叔。"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
