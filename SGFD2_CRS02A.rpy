label SGFD2_CRS02A:
    window hide


    $ loadBG(0,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ date="8/13"
    $ day ="FRI"
    hide screen phonebtn
    show screen phoneSD1

    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0000"
    $ current_voice = "voice/CRS02A_CRS0000.ogg"
    "Kurisu" "「Finished.」"
    "As I carefully connected the final two cords I proclaimed this to the LabMems. Especially Okabe."
    window hide


    $ loadBG(2,"IBG040A")



    hide screen phonebtn
    play bgm "BGM05"
    "I had just finished upgrading the improved PhoneWave. It was probably the first of its kind. It didn't just send information but human memories into the past."
    "Similar to the D-Mail function it could compress up the 36 bytes of the human consciousness and send it into the past."
    "Naturally the sender and recipient had to be the same person but this was the only limitation."
    "Evenso this machine would be the first time any human had managed to achieve this in the history of the human race."
    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0001"
    $ current_voice = "voice/CRS02A_CRS0001.ogg"
    "Kurisu" "「We may have created a monster here...」"
    "That's right. We had the technology which transcended the laws of causality. Everybody in the room understood this."
    "That was why even though we had created the greatest inventions of the century, nobody raised their voice in joy."
    "We had made something huge. I could sense that feeling in my heart."
    "I myself felt the urge to create and form the ideas so I could test my theories..."
    "While I had also been pressured by the passion of my fellow LabMems as well..."
    "Actually I was a little embarrassed now that it had been created."
    "In the first place I had also thought that this was something that shouldn't have been created."
    "The existence of a time machine, something that could rewrite the past and change the future would override the common sense that existed since the dawn of time."
    "Our world relied on a cause and effect relationship. But a time machine would break such rules."
    "With a time machine if there was some failure you could just go back into the past and undo that failure making it like it never existed in the first place."
    "If someone tried to get in your way it was the same. You could just erase the person who was getting in the way making it, as if they had never existed."
    "This could also be called the power of God. Its value politically, militarily and naturally scientifically was immeasureable."
    "However that didn't mean that a time machine shouldn't exist. Leaving the future aside for now, the human race had reached a point that surpassed time travel."
    "This was exactly the same as the development of rocket and nuclear technology in the 20th century."
    "Depending on who controlled the technology this caused a great imbalance in the world to occur."
    "Even in the 21st century, traces of this could be found in the aftermath of the development of such technologies."
    "However..."
    "However."
    "I had ended up creating a time machine."
    "For no other reason that I had just wanted to create it."
    "I had known how dangerous a thing it would be and even warned others against it. Even though I had denied it's very existance myself..."
    "My intellectual curiosity for the unkown along with my desire as a researcher had motivated me to do it."
    "Originally the reason why I came to the Future Gadget Lab was also the same impulse."
    "The experiment that Okabe and the others were doing. I had been defeated by my own curiosity after witnessing them using the PhoneWave to send messages to the past."
    "And the result of that was... this improved PhoneWave"
    window hide



    $ loadBG(2,"BG03A4")




    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "CRS02A_DAR0000"
    $ current_voice = "voice/CRS02A_DAR0000.ogg"
    "Itaru" "「…………」"
    "Hashida too..."
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0000"
    $ current_voice = "voice/CRS02A_MAY0000.ogg"
    "Mayuri" "「…………」"
    "Mayuri as well..."
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0000"
    $ current_voice = "voice/CRS02A_OKA0000.ogg"
    "Rintarou" "「…………」"
    "And even the founder of the Future Gadget Lab, the self proclaimed insane mad scientist Hououin Kyouma wasn't able to open his mouth either."
    "Everyone was visibly hesitating."
    "Even so the first to speak was as I suspected, Okabe"
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0001"
    $ current_voice = "voice/CRS02A_OKA0001.ogg"
    "Rintarou" "「First, shall we decide on the offical name?」"
    "Because he often pulled others like this made him the leader I guess."
    "However, thinking of a name was kind of a no brain reaction at a time like this..."
    window hide


    $ loadBG(2,"IBG040A")



    hide screen phonebtn
    "In the end it was decided as the Time Leap Machine (name subject to change)."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    "Along the way as usual Okabe suggested several Chunnibyou type names but Mayuri chose a simple name that I had suggested earlier."
    "And so as prompted by Okabe, I described the functions of the Time Leap machine to everyone."
    window hide


    $ loadBG(2,"IBGX058J")



    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0002"
    $ current_voice = "voice/CRS02A_CRS0002.ogg"
    "Kurisu" "「In short, this transforms memories into data and then passes it through a ring singularity into the past.」"
    "The receiving party would receive memories of the future."
    "The greatest feature of the Time Leap machine was that it provided a premonition of the future to the receiver."
    "This surpassed time using the ring singualarity. In layman terms, it passed through a black hole which would normally crush any substance or organism that would pass through it."
    "Naturally those substances or organism would not survive."
    "But as to that problem we had found a workaround bu just sending data through the ring singularity."
    window hide


    $ loadBG(2,"IBGX041")



    "And at the same time we were made aware of the presence of SERN and their LHC"
    "The LHC had the ability to generate a mini black hole which Hashida operated through cracking which was then used to compress the data."
    "Because it was such a ridiculous idea we were able to complete the TIme Leap machine."
    "I caught my breath after speaking a lot about the Time Leap machine's functions. It seemed a little difficult for Mayuri but the others seemed to understand."
    window hide



    $ loadBG(2,"BG03A4")



    "And now that I had finished speaking, the lab returned to silence."

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0002"
    $ current_voice = "voice/CRS02A_OKA0002.ogg"
    "Rintarou" "「…………」"
    $ stopvoc("DAR")
    play DAR "CRS02A_DAR0001"
    $ current_voice = "voice/CRS02A_DAR0001.ogg"
    "Itaru" "「…………」"
    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0003"
    $ current_voice = "voice/CRS02A_CRS0003.ogg"
    "Kurisu" "「…………」"
    "Okabe, Hashida and myself looked at each other."
    "Right it was obvious that we were postponing any conclusion."
    "A time machine that was like the power of God. How we should use it... still hasn't been decided."
    "After the silence that followed once again, it was Okabe who broke it and with a cough he started to speak."
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0003"
    $ current_voice = "voice/CRS02A_OKA0003.ogg"
    "Rintarou" "「What shall we do?」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "CRS02A_DAR0002"
    $ current_voice = "voice/CRS02A_DAR0002.ogg"
    "Itaru" "「What do you mean, what shall we do?」"
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0004"
    $ current_voice = "voice/CRS02A_OKA0004.ogg"
    "Rintarou" "「I'm talking about how we should use this Time Leap Machine.」"
    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0004"
    $ current_voice = "voice/CRS02A_CRS0004.ogg"
    "Kurisu" "「…………」"
    window hide




    "Okabe looked around and his line of sight finally stopped at me."
    "He was probably wanting me to say my opinion..."
    "Being quiet in a discussion was generally considered a positive trait. Matching ones opinions with the other researchers was the duty if a researcher."
    "However, there was a reason why I was hesitating to speak."
    "I had been in conflict."
    "Naturally this wasn't something we should be using freely. Monopolizing the power of God would probably just create several new problems."
    "However at the same time I wanted to experiment with it. If we used it, we could measure the results. I had wanted to see those results."
    "While this was probably just my ego, I wasn't trying to be self righteous but it was rather my desire as a researcher."
    "Because of one's own desire this has led to the development of rocket technology and miltary funding."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_V2_ROCKET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_V2_ROCKET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_V2_ROCKET"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VON_BRAUN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_VON_BRAUN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_VON_BRAUN"])

    "The{color=#f00}V2 rocket{/color}which caused a sea of flames in{color=#f00}London{/color}，was the same. "
    "My sense of justice and my desire as a reseacher were fighting a battle within me."
    "With that internal situation and then Okabe's gaze, I felt like running away."
    "Why is this guy only serious at times like these?!"
    "I involuntarily grit my teeth and muttered under my breath what I had been thinking."
    "Okabe Rintarou was surprising a serious person sometimes."
    "It was just when you were troubled, he would just say Chuunibyou type things..."
    "When I spoke about my father or when the other LabMems had something on their minds, he would support them seriously."
    "Now his look was one of his serious looks."
    "It wasn't Hououin Kyouma, but Okabe Rintarou who was staring at me now."
    window hide



    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0005"
    $ current_voice = "voice/CRS02A_CRS0005.ogg"
    "Kurisu" "「The safest thing for us to do is to collaborate with research institues and use it for national research.」"
    "I was aware this was not conclusive and reluctantly muttered so."
    "I wanted to experiment!"
    "However there were certainly many risks involved with using something like a time machine."
    $ stopvoc("DAR")
    play DAR "CRS02A_DAR0003"
    $ current_voice = "voice/CRS02A_DAR0003.ogg"
    "Itaru" "「This doesn't feel real.」"
    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0001"
    $ current_voice = "voice/CRS02A_MAY0001.ogg"
    "Mayuri" "「Mayushii doesn't get it...」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "CRS02A_DAR0004"
    $ current_voice = "voice/CRS02A_DAR0004.ogg"
    "Itaru" "「No Mayushii didn't really help out at all right?」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0002"
    $ current_voice = "voice/CRS02A_MAY0002.ogg"
    "Mayuri" "「Oh yeah, you're right. Ehehe.」"
    "The scale of what Hashida and mayuri were saying wasn't on the same level. They just seemed to be taking this lightly and not really grasping the seriousness."

    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5 
    "In that case then what was important was Okabe's opinion."
    hide bg2 
    with dissolve

    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0006"
    $ current_voice = "voice/CRS02A_CRS0006.ogg"
    "LOLsecretTextHere" "「Okabe what do you think? And by the way, not Hououin I mean Okabe right?」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "I made a point to mention that. Just because he wasn't acting Chunnibyou now, it didn't mean he woundn't respond that way."
    "Of course I thought the chance was low. Okabe was basically a serious guy."
    "Actually on the other hand, I could say such things to him because I trusted him."
    "If it were Okabe Rintarou's judgement and not Hououin Kyouma's then I would accept it. I meant it that way."
    "And if he decided to experiment then I thought I would be experimental subject."
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0005"
    $ current_voice = "voice/CRS02A_OKA0005.ogg"
    "Rintarou" "「Actually, a part of me wants to experiment.」"
    "After some time Okabe said so. I took a breath."
    "if that is your decision then..."
    "I tried to gather up my determination and speak."
    "But before I could, Okabe's words hit my ears. And this sealed what I was about to say."
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0006"
    $ current_voice = "voice/CRS02A_OKA0006.ogg"
    "Rintarou" "「However, to actually conduct Time Leaps, there are too many problems.」"
    "This is what he declared."
    "There were many problems associated with the Time Leap machine."
    "And there was also the Time Paradox."
    "We couldn't conduct animal testing with the Time Leap machine in the first place. It would have to start with human experimentation."
    "So if I were to decide to experiment, I was thinking to be the first experimental subject myself. But at the same time this didn't mean I wasn't afraid."
    "So I had tried to gather the momentum to volunteer but it was completely destroyed by Okabe's words."
    "I wondered if Okabe would ask one of the LabMems to become an experimental subject or not."
    "If it was unavoidable then I guess I would have reluctantly agrred as it was unbelievable that Hashida or Mayuri would."
    "Although Okabe probably knew this already."
    "It could be that he had known all along and had intentionally spoken at that point in order to kill my momentum."
    "Even though he didn't act like that normally. While I knew what was he always wanted everyone to know that he was the best. Or should I say I came to know."
    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0003"
    $ current_voice = "voice/CRS02A_MAY0003.ogg"
    "Mayuri" "「Hey...」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "While we were hesitating, Mayuri who was quietly watching the discussion butt in."
    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0004"
    $ current_voice = "voice/CRS02A_MAY0004.ogg"
    "Mayuri" "「You know Mayushii doesn't really get difficult things.」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0005"
    $ current_voice = "voice/CRS02A_MAY0005.ogg"
    "Mayuri" "「But what if we made the banana I bought yesterday time leap?」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "With an almost carefree opinion, Mayuri's words actually made me relax a little."
    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0007"
    $ current_voice = "voice/CRS02A_CRS0007.ogg"
    "Kurisu" "「Silly Mayuri...」"
    $ stopvoc("CRS")
    play CRS "CRS02A_CRS0008"
    $ current_voice = "voice/CRS02A_CRS0008.ogg"
    "Kurisu" "「Unlike humans, bananas don't have brains right?」"
    "That was right."
    "As previoiusly mentioned, the only candidates for the Time Leap machine were humans."
    "There were difficult points with this machine too."

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "CRS02A_MAY0006"
    $ current_voice = "voice/CRS02A_MAY0006.ogg"
    "Mayrui" "「Oh right. Well I guess that's no good then.」"
    "With that explanation, Mayuri seemed completely satisfied. But it could be that all she didn't really understand what I had said at all."
    "Or it could have been that she wasn't thinking with her brain but rather reading the tense atmosphere...?"
    "After spending around two weeks with her, I knew that she wasn't that stupid with that in mind maybe my guess wasn't so far off the mark."
    "Actually the tense air that had been floating around, the lab turned into something completly different now."
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0007"
    $ current_voice = "voice/CRS02A_OKA0007.ogg"
    "Rintarou" "「……Let's not experiment.」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "Okabe pushed for change with those words."
    $ stopvoc("OKA")
    play OKA "CRS02A_OKA0008"
    $ current_voice = "voice/CRS02A_OKA0008.ogg"
    "Rintarou" "「Let's entrust this Time Leap machine to research institutions and then publish our findings publicly.」"
    "Both Hashida and I had nothign to say in response. Naturally we would trust the decision he had made."
    scene expression Solid("000000")  with fade

    stop bgm 

    hide screen phoneSD1
    window hide





    return
