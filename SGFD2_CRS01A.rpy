label SGFD2_CRS01A:
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT002")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade
    $ date="8/13"
    $ day="FRI"

    $ loadBG(0,"BG_BLACK")

    play se "SGSE300L" loop

    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0000"
    $ current_voice = "voice/CRS01A_CRS0000.ogg"
    "Kurisu" "「Pitch black darkness...?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0001"
    $ current_voice = "voice/CRS01A_CRS0001.ogg"
    "Kurisu" "「Where am I? What is this place...」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0002"
    $ current_voice = "voice/CRS01A_CRS0002.ogg"
    "Kurisu" "「Why……am i here?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0003"
    $ current_voice = "voice/CRS01A_CRS0003.ogg"
    "Kurisu" "「Huh... who am I in the first place...?」"
    "I had a light headache."
    "Looking left and right I couldn't see anything."
    "Just a space that was filled with darkness."
    "There was no wind. The only thing I could hear was the sound of a clock ticking."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLOATING_TANK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLOATING_TANK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_FLOATING_TANK"])
    "Maybe {color=#f00}sensory deprivation chamber{/color}? But I had no recollection of entering one. And there wen't supposed to be any sounds in those."
    "But the only sound here was the clock ticking endlessly."
    "I calmed myself and tried to think about the past."
    "But for some reason I couldn't think clearly. Everything was a blur……"
    "In the first place……"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0004"
    $ current_voice = "voice/CRS01A_CRS0004.ogg"
    "Kurisu" "「In the first place... who was I?」"
    "I asked myself this."
    "But the sound of the click kept interfering. I couldn't reach my memories."
    "Even though I wanted to ignore it... Every time I tried ignoring it, it would disturb my thoughts..."
    "Why the hell was that?"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0005"
    $ current_voice = "voice/CRS01A_CRS0005.ogg"
    "Kurisu" "「This isn't another one of Okabe's bad jokes is it?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0006"
    $ current_voice = "voice/CRS01A_CRS0006.ogg"
    "Kurisu" "「Actually he wouldn't do something like this I guess.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0007"
    $ current_voice = "voice/CRS01A_CRS0007.ogg"
    "Kurisu" "「Okabe?」"
    "Who is that?……"
    "Who is it?"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0008"
    $ current_voice = "voice/CRS01A_CRS0008.ogg"
    "???" "「Even when you are like this, you still remember him eh?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0009"
    $ current_voice = "voice/CRS01A_CRS0009.ogg"
    "Kurisu" "「M... Me?!」"
    window hide

    $ loadBG(0,"EV_CRS001A")

    $ loadBG(2,"EV_CRS001A")

    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0010"
    $ current_voice = "voice/CRS01A_CRS0010.ogg"
    "Kurisu" "「A woman appeared before my eyes.」"
    "For some reason I could recognize her as myself."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0011"
    $ current_voice = "voice/CRS01A_CRS0011.ogg"
    "? ?？" "「It seems you remember that much right Makise Kurisu?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0012"
    $ current_voice = "voice/CRS01A_CRS0012.ogg"
    "Kurisu" "「Makise... Makise Kurisu!"
    window hide

    $ loadBG(3,"BG_WHITE",trans=ImageDissolve(im.Scale("mask/mask09.png",1024,576),1))
    $ renpy.pause(1,hard=True)
    $ loadBG(2,"EV_CRS001A")

    "At that moment a torrent of images passed through my brain."
    "My birthday 11 years ago. When I made my papa angry."
    "Accompanying my mom to the United States."
    "Putting my utmost effort into skipping a year then graduating from university and working as a Neuroscience researcher at Victory Mitochondria University."
    "And then papa Shoichi Makise receiving a commemoration letter for completing a time machine this year."
    "Then with the pretext of doing a reverse foreign exchange at a high school returning to Japan."
    "And then..."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0013"
    $ current_voice = "voice/CRS01A_CRS0013.ogg"
    "「Kurisu」" "「And then... Huh?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0014"
    $ current_voice = "voice/CRS01A_CRS0014.ogg"
    "「???」" "「What's the matter? Don't you know what happened next?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0015"
    $ current_voice = "voice/CRS01A_CRS0015.ogg"
    "「Kurisu」" "「I came back to Japan... and was killed by papa...」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BUILDE"])
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0016"
    $ current_voice = "voice/CRS01A_CRS0016.ogg"
    "Kurisu" "「No... that's not it! At the large {color=#f00}building{/color} where the lecture was held, I met a strange guy in a labcoat...」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0017"
    $ current_voice = "voice/CRS01A_CRS0017.ogg"
    "Kurisu" "「No... I met the labcoat guy before I was killed by papa.」"
    "My memories were jumbled."
    "Several memories overlapped and conflicted within me."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0018"
    $ current_voice = "voice/CRS01A_CRS0018.ogg"
    "Kurisu" "「At the ATF lecture Okabe and I become friends...」"
    "That's right. I remembered..."
    "Okabe Rintarou."
    window hide

    $ loadBG(3,"EVX_C03A",trans=Fade(0.5,0.5,0.5,color="fff"))

    "He said that I was a ghost or something and said things like I should of died... that's what started it."
    window hide


    $ loadBG(4,"EVX_C04B",trans=Fade(0.5,0.5,0.5,color="fff"))

    "And then we talked about the possiblity of a time machine and advancement of current science and technology."
    window hide

    $ loadBG(0,"EV_CRS001A",trans=Fade(0.5,0.5,0.5,color="fff"))

    $ loadBG(2,"EV_CRS001A")

    "Because I was curious about various things I went to visit his lab..."
    "And then he and the others had actually created a time machine..."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0019"
    $ current_voice = "voice/CRS01A_CRS0019.ogg"
    "Kurisu" "「That's right... Not one that would send humans directly into the past but one that could send messages into the past.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0020"
    $ current_voice = "voice/CRS01A_CRS0020.ogg"
    "Kurisu" "「D-Mails.」"
    "Right."
    "And then we carried out various D-Mail experiments to see if we could change the past or not."
    "Then while doing experiments I started to like Okabe..."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0021"
    $ current_voice = "voice/CRS01A_CRS0021.ogg"
    "？？？" "「It seems you've remembered most of it haven't you...」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0022"
    $ current_voice = "voice/CRS01A_CRS0022.ogg"
    "？？？" "「Then can you remember what you were doing now?」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0023"
    $ current_voice = "voice/CRS01A_CRS0023.ogg"
    "Kurisu" "「Now...」"
    "Even if you said that to me..."
    "In the first place where the hell was I?"
    "And, why was I here?"
    "When you thought things out this was probably a dream and I was probably sleeping at the moment."
    "However, according to my memories I had stayed up all night trying to improve the PhoneWave..."
    "Sending things to the past. Not just D-Mails but sending a persons memories of what had occured in the future. Premonitions of what would happen."
    "However... I didn't have any recollection of going to sleep."
    "There might be the possiblity that I was daydreaming but it seemed too rare to be a possibility"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0024"
    $ current_voice = "voice/CRS01A_CRS0024.ogg"
    "？？？" "「That guess could be considered correct and incorrect also.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0025"
    $ current_voice = "voice/CRS01A_CRS0025.ogg"
    "Kurisu" "「Not correct... Wouldn't that be wrong?」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS001B"]]["Check"]=True


    $ loadBG(3,"EV_CRS001B")





    $ loadBG(4,"EV_CRS001B")





















    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0026"
    $ current_voice = "voice/CRS01A_CRS0026.ogg"
    "？？？" "「Hehe...That's just like you. You love exact definitions.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0027"
    $ current_voice = "voice/CRS01A_CRS0027.ogg"
    "Kurisu" "「If words aren't properly defined then naturally discrepancies could occur when the wrong words are used!」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0028"
    $ current_voice = "voice/CRS01A_CRS0028.ogg"
    "？？？" "「Yes that's fine. As long as you remain yourself that's fine. This is a story that you will experience.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0029"
    $ current_voice = "voice/CRS01A_CRS0029.ogg"
    "Kurisu" "「...A story?」"
    "What the hell was she talking about?"
    "Naturally this was an incoherent dream but this exchange was too strange."
    "There were also various strange parts where my brain was responding to these weird questions."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0030"
    $ current_voice = "voice/CRS01A_CRS0030.ogg"
    "？？？" "「You don't need to think so deeply about it. You just need to accept what is there and remain as yourself.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0031"
    $ current_voice = "voice/CRS01A_CRS0031.ogg"
    "？？？" "「Once the story begins you won't be able to remember any of this mirage anymore or it might appear like some kind of phantom...」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0032"
    $ current_voice = "voice/CRS01A_CRS0032.ogg"
    "？？？" "「Maybe it never existed in the first place. That is just one of many possibillities.」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS001A"]]["Check"]=True






















    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0033"
    $ current_voice = "voice/CRS01A_CRS0033.ogg"
    " ？ ？ ？" "「As long as you came here then you have the duty to witness it.」"
    "What did that mean?"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0034"
    $ current_voice = "voice/CRS01A_CRS0034.ogg"
    " ？ ？  ？" "「August 13 2010. 2:06pm. This story begins there.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0035"
    $ current_voice = "voice/CRS01A_CRS0035.ogg"
    "Huh?" "And converges at 5:34pm of the same day."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0036"
    $ current_voice = "voice/CRS01A_CRS0036.ogg"
    "Kurisu" "「Huh?」"
    "For some reason that date and time shook my consciousness."
    "Not in my memories... But in time."
    "Even so, for some reason something about it upset me deep in my subconscious."
    "My consciousness became cloudy."
    "The sound of the clock... it wouldn't part from my ears."
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0037"
    $ current_voice = "voice/CRS01A_CRS0037.ogg"
    " ？ ？  ？" "「Time moving around a clock face is an infinite spiral. An eternal trajectory that you should know.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0038"
    $ current_voice = "voice/CRS01A_CRS0038.ogg"
    " ？ ？ ？ " "「So you should confirm this and save...」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0039"
    $ current_voice = "voice/CRS01A_CRS0039.ogg"
    " ？ ？ ？ " "「Save yourself... and him.」"
    $ stopvoc("CRS")
    play CRS "CRS01A_CRS0040"
    $ current_voice = "voice/CRS01A_CRS0040.ogg"
    "Kurisu" "「Wait a minute! Don't just tell me that!」"
    "My consciousness became violently cloudy."
    "The sound of the clock became so loud it seemed like it would swallow my consciousness."
    window hide
    play se "SGSE301L" loop

    "The sound of ringing bells and my consciousness became more and more hazy..."
    "Just like when you went to sleep..."
    "No maybe it was more like when you woke up from a dream..."
    "And then... I..."

    hide screen phoneSD1
    window hide

    stop se
    scene expression Solid("000000")  with fade






    return















    return
