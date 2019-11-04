screen say:

    default side_image = None
    default two_window = False

    if not two_window:

        window:

            id "window"
            background "system/bgMes~ipad.png"
            area (0,576-167,1024,167)
            anchor (0,0)
            if who:
                add "system/bgNameLeft~ipad.png" align (.3,1.0)
                add "system/bgNameRight~ipad.png" align (0.7,1.0)


                text who id "who" align (.5,1.0) bold False

            text what id "what" size 24 area (24,24,1024-48,192-24)

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    key "rollback" action ShowMenu("text_history",transition=dissolve)
    key "a" action Preference("auto-forward", "toggle")









screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:

                button:
                    action action
                    style "menu_choice_button"

                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)








screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu







screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu






transform taptobegin:
    alpha 0.0
    linear 1 alpha 1.0
    linear 1 alpha 0
    repeat
label movie_op:
    $ renpy.movie_cutscene("video/op.avi")
    return

screen fivepb:
    imagebutton idle "system/5pb_btn1~ipad.png" hover "system/5pb_btn2~ipad.png" pos (10,40) action OpenURL("http://5pb.jp/games/smapho/")
screen main_menu tag menu:
    if not renpy.android:
        on "show" action [Show("flux_anime",text=[Null(),Null(),Null(),printer_str(" TAP SCREEN  "),Null(),Null()]),SetVariable("rml",[]),SetVariable("sml",[]),SetVariable("cml",{})]
    timer 30 action Start("movie_op")
    default mainmenu = False
    default submenu = ""


    key "game_menu" action Quit()


    window:
        style "mm_root"
    add "system/bgTitle~ipad.png" at truecenter
    use fivepb

    if not mainmenu:
        imagebutton:
            idle DynamicDisplayable(printer,list("TAP SCREEN"),list("TAP SCREEN"),"s",static=True)
            hover DynamicDisplayable(printer,list("TAP SCREEN"),list("TAP SCREEN"),"s",static=True)
            selected_idle DynamicDisplayable(printer,list("TAP SCREEN"),list("TAP SCREEN"),"s",static=True)
            selected_hover DynamicDisplayable(printer,list("TAP SCREEN"),list("TAP SCREEN"),"s",static=True)
            action SetScreenVariable("mainmenu",True)
            at taptobegin
            pos (676+20,378-58*2)
        button:
            xfill True
            yfill True
            background None
            action SetScreenVariable("mainmenu",True)
    if mainmenu:
        if not renpy.android:
            timer 0.01 action Show("flux_anime",text=[printer_str("        START"),printer_str("         LOAD"),printer_str("      LIBRARY"),printer_str("        EXTRA"),printer_str("       SYSTEM"),printer_str("         HELP")],next="mainmenu_title")
        else:
            timer 0.01 action Show("mainmenu_title",transition=dissolve)

screen flux_anime(text, next=None):
    on "show" action Show("invisible")
    on "hide" action Hide("invisible")
    add "flux1" pos (676,378-58*5)
    add "flux1" pos (676,378-58*0)
    add "flux2" pos (676,378-58*1)
    add "flux2" pos (676,378-58*4)
    add "flux3" pos (676,378-58*2)
    add "flux3" pos (676,378-58*3)

    if next:
        timer 1.82 action [Hide("flux_anime"),Hide("flux_anime_text"),Show(next)]
    else:
        timer 1.82 action [Hide("flux_anime"),Hide("flux_anime_text")]
screen flux_anime_text(text):

    add text[0] pos (676,378-58*5)
    add text[1] pos (676,378-58*4)
    add text[2] pos (676,378-58*3)
    add text[3] pos (676,378-58*2)
    add text[4] pos (676,378-58*1)
    add text[5] pos (676,378-58*0)
    use fivepb
screen mainmenu_library tag menu:
    window:
        style "mm_root"
    add "system/bgTitle~ipad.png" at truecenter

    add printer_str("   LIBRARY   ") pos (676,378-58*5)
    imagebutton:
        idle printer_str("   CG LIBRARY")
        selected_idle printer_str("   CG LIBRARY")
        hover printer_str("   CG LIBRARY")
        selected_hover printer_str("   CG LIBRARY")
        pos (676,378-58*4)
        action Show("cg_library",transition=dissolve)
    imagebutton:
        idle printer_str("SOUND LIBRARY")
        selected_idle printer_str("SOUND LIBRARY")
        hover printer_str("SOUND LIBRARY")
        selected_hover printer_str("SOUND LIBRARY")
        pos (676,378-58*3)
        action Show("sound_library",transition=dissolve)
    imagebutton:
        idle printer_str("MOVIE LIBRARY")
        selected_idle printer_str("MOVIE LIBRARY")
        hover printer_str("MOVIE LIBRARY")
        selected_hover printer_str("MOVIE LIBRARY")
        pos (676,378-58*2)
        action Show("movie_library",transition=dissolve)
    imagebutton:
        idle printer_str("      <<BACK")
        selected_idle printer_str("      <<BACK")
        hover printer_str("      <<BACK")
        selected_hover printer_str("      <<BACK")
        pos (676,378-58*0)
        action Show("mainmenu_title",transition=dissolve)
    use fivepb

screen mainmenu_extra tag menu:
    window:
        style "mm_root"
    add "system/bgTitle~ipad.png" at truecenter

    add printer_str("    EXTRA    ") pos (676,378-58*5)
    imagebutton:
        idle printer_str("   CLEAR LIST")
        pos (676,378-58*4)
        action Show("clearlist",transition=dissolve)
    imagebutton:
        idle printer_str("    TIPS LIST")
        pos (676,378-58*3)
        action Show("tips",transition=dissolve)
    imagebutton:
        idle printer_str("      <<BACK")
        selected_idle printer_str("      <<BACK")
        hover printer_str("      <<BACK")
        selected_hover printer_str("      <<BACK")
        pos (676,378-58*0)
        action Show("mainmenu_title",transition=dissolve)
    use fivepb

screen mainmenu_title tag menu:
    timer 30 action Start("movie_op")
    window:
        style "mm_root"
    add "system/bgTitle~ipad.png" at truecenter

    imagebutton:
        idle printer_str("        START")
        selected_idle printer_str("        START")
        hover printer_str("        START")
        selected_hover printer_str("        START")
        pos (676,378-58*5)
        if persistent.OKA1:
            action Show("route_choose",chara="oka1",transition=dissolve)
        else:
            action [Start(label="SGFD2_ROUTE_OKA")]
    imagebutton:
        idle printer_str("         LOAD")
        selected_idle printer_str("         LOAD")
        hover printer_str("         LOAD")
        selected_hover printer_str("         LOAD")
        pos (676,378-58*4)
        action Show("load",transition=dissolve)
    imagebutton:
        idle printer_str("      LIBRARY")
        selected_idle printer_str("      LIBRARY")
        hover printer_str("      LIBRARY")
        selected_hover printer_str("      LIBRARY")
        pos (676,378-58*3)
        action Show("mainmenu_library",transition=dissolve)
    imagebutton:
        idle printer_str("        EXTRA")
        selected_idle printer_str("        EXTRA")
        hover printer_str("        EXTRA")
        selected_hover printer_str("        EXTRA")
        pos (676,378-58*2)
        action Show("mainmenu_extra",transition=dissolve)
    imagebutton:
        idle printer_str("       SYSTEM")
        selected_idle printer_str("       SYSTEM")
        hover printer_str("       SYSTEM")
        selected_hover printer_str("       SYSTEM")
        pos (676,378-58*1)
        action ShowMenu("preferences")
    imagebutton:
        idle printer_str("         HELP")
        selected_idle printer_str("         HELP")
        hover printer_str("         HELP")
        selected_hover printer_str("         HELP")
        pos (676,378-58*0)
        action Show("help",transition=dissolve)
    use fivepb

screen help tag menu:
    default helpstr = u"""
    操作说明：
        PC版： 
        CTRL快进，h隐藏对话框，ESC/右键呼出菜单
        a自动模式，滚轮向上滚动可以查看历史
        手机版： 
        向右滑动呼出和隐藏菜单，向左滑动快进，向上滑动隐藏窗口，
        向下滑动查看历史，先向下滑动再向右滑动进入自动模式
    游戏说明：
        收到短信后请务必及时回复！
        可以回复且还在回复期内的短信会有蓝色的关键字提示。
        在手机开启时，请尽量不要快进游戏，否则容易出现手机屏幕无法关闭的bug。
    """

    add "system/bgHelp~ipad.png" at truecenter
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    text helpstr color "fff" pos (30,10)


screen route_choose(chara="oka1") tag menu:

    add "system/bgStart~ipad.png" at truecenter
    if chara=="oka1":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp8~ipad.png" pos (508,164)
        add "system/jp9~ipad.png" pos (508+52,164)
        add "system/jp10~ipad.png" pos (508+52*2,164)
        add "system/jp11~ipad.png" pos (508+52*3,164)
        add "system/jp4~ipad.png" pos (508+52*4,164)
        add "system/jp12~ipad.png" pos (508+52*5,164)
        add "system/jp13~ipad.png" pos (508+52*6,164)
        add "system/jp14~ipad.png" pos (508+52*7,164)
        add "system/jp15~ipad.png" pos (508+52*8,164)
        add "system/sD.png" pos (595,224)
        add "system/sR.png" pos (595+20*1,224)
        add "system/s-0.png" pos (595+20*2,224)
        add "system/sJ.png" pos (595+20*4,224)
        add "system/sE.png" pos (595+20*5,224)
        add "system/sK.png" pos (595+20*6,224)
        add "system/sY.png" pos (595+20*7,224)
        add "system/sL.png" pos (595+20*8,224)
        add "system/sL.png" pos (595+20*9,224)
        add "system/sO.png" pos (595+20*11,224)
        add "system/sN.png" pos (595+20*12,224)
        add "system/sL.png" pos (595+20*14,224)
        add "system/sI.png" pos (595+20*15,224)
        add "system/sN.png" pos (595+20*16,224)
        add "system/sE.png" pos (595+20*17,224)
        add "system/sS.png" pos (595+20*18,224)
        add "system/OKA~ipad.png" pos (233,363)
        add "system/activeRouteFinished~ipad.png" pos (394,412)
    elif chara == "dar":
        add im.Scale("system/s3.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp16~ipad.png" pos (508,164)
        add "system/jp17~ipad.png" pos (508+52,164)
        add "system/jp18~ipad.png" pos (508+52*2,164)
        add "system/jp19~ipad.png" pos (508+52*3,164)
        add "system/jp4~ipad.png" pos (508+52*4,164)
        add "system/jp20~ipad.png" pos (508+52*5,164)
        add "system/jp21~ipad.png" pos (508+52*6,164)
        add "system/jp22~ipad.png" pos (508+52*7,164)
        add "system/jp23~ipad.png" pos (508+52*8,164)
        add "system/sB.png" pos (595-20,224)
        add "system/sI.png" pos (595,224)
        add "system/sR.png" pos (595+20*1,224)
        add "system/sD.png" pos (595+20*2,224)
        add "system/sS.png" pos (595+20*4,224)
        add "system/sI.png" pos (595+20*5,224)
        add "system/sN.png" pos (595+20*6,224)
        add "system/sG.png" pos (595+20*7,224)
        add "system/sI.png" pos (595+20*8,224)
        add "system/sN.png" pos (595+20*9,224)
        add "system/sG.png" pos (595+20*10,224)
        add "system/sI.png" pos (595+20*12,224)
        add "system/sN.png" pos (595+20*13,224)
        add "system/sC.png" pos (595+20*15,224)
        add "system/sA.png" pos (595+20*16,224)
        add "system/sG.png" pos (595+20*17,224)
        add "system/sE.png" pos (595+20*18,224)
        add "system/DAR~ipad.png" pos (233,363)
        if persistent.DAR:
            add "system/activeRouteFinished~ipad.png" pos (235+17*15,362+25)
        else:
            add "system/activeRouteNormal~ipad.png" pos (235+17*15,362+25)
    elif chara == "crs":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s2.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s8.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp1~ipad.png" pos (508+52*2,164)
        add "system/jp2~ipad.png" pos (508+52*3,164)
        add "system/jp3~ipad.png" pos (508+52*4,164)
        add "system/jp4~ipad.png" pos (508+52*5,164)
        add "system/jp5~ipad.png" pos (508+52*6,164)
        add "system/jp6~ipad.png" pos (508+52*7,164)
        add "system/jp7~ipad.png" pos (508+52*8,164)
        add "system/sV.png" pos (595+20*2,224)
        add "system/sE.png" pos (595+20*3,224)
        add "system/sR.png" pos (595+20*4,224)
        add "system/sM.png" pos (595+20*5,224)
        add "system/sI.png" pos (595+20*6,224)
        add "system/sL.png" pos (595+20*7,224)
        add "system/sI.png" pos (595+20*8,224)
        add "system/sA.png" pos (595+20*9,224)
        add "system/sN.png" pos (595+20*10,224)
        add "system/sS.png" pos (595+20*12,224)
        add "system/sO.png" pos (595+20*13,224)
        add "system/sO.png" pos (595+20*14,224)
        add "system/sT.png" pos (595+20*15,224)
        add "system/sE.png" pos (595+20*16,224)
        add "system/sE.png" pos (595+20*17,224)
        add "system/sR.png" pos (595+20*18,224)
        add "system/KRS~ipad.png" pos (233,363)
        if persistent.CRS:
            add "system/activeRouteFinished~ipad.png" pos (235+17*15,362+25*3-2)
        else:
            add "system/activeRouteNormal~ipad.png" pos (235+17*15,362+25*3-2)
    elif chara == "suz":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp24~ipad.png" pos (508+52*2,164)
        add "system/jp25~ipad.png" pos (508+52*3,164)
        add "system/jp26~ipad.png" pos (508+52*4,164)
        add "system/jp27~ipad.png" pos (508+52*5,164)
        add "system/jp4~ipad.png" pos (508+52*6,164)
        add "system/jp28~ipad.png" pos (508+52*7,164)
        add "system/jp29~ipad.png" pos (508+52*8,164)
        add "system/sG.png" pos (595+20*0,224)
        add "system/sH.png" pos (595+20*1,224)
        add "system/sO.png" pos (595+20*2,224)
        add "system/sS.png" pos (595+20*3,224)
        add "system/sT.png" pos (595+20*4,224)
        add "system/sI.png" pos (595+20*5,224)
        add "system/sN.png" pos (595+20*6,224)
        add "system/sG.png" pos (595+20*7,224)
        add "system/sR.png" pos (595+20*9,224)
        add "system/sE.png" pos (595+20*10,224)
        add "system/sN.png" pos (595+20*11,224)
        add "system/sD.png" pos (595+20*12,224)
        add "system/sE.png" pos (595+20*13,224)
        add "system/sZ.png" pos (595+20*14,224)
        add "system/sV.png" pos (595+20*15,224)
        add "system/sO.png" pos (595+20*16,224)
        add "system/sU.png" pos (595+20*17,224)
        add "system/sS.png" pos (595+20*18,224)
        add "system/SUZ~ipad.png" pos (233,363)
        if persistent.SUZ:
            add "system/activeRouteFinished~ipad.png" pos (229+17*21,363)
        else:
            add "system/activeRouteNormal~ipad.png" pos (229+17*21,363)
    elif chara == "ten":
        add im.Scale("system/s3.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s8.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp30~ipad.png" pos (508+52*2,164)
        add "system/jp31~ipad.png" pos (508+52*3,164)
        add "system/jp31~ipad.png" pos (508+52*4,164)
        add "system/jp32~ipad.png" pos (508+52*5,164)
        add "system/jp4~ipad.png" pos (508+52*6,164)
        add "system/jp33~ipad.png" pos (508+52*7,164)
        add "system/jp34~ipad.png" pos (508+52*8,164)
        add "system/sA.png" pos (595+20*-14,224)
        add "system/sS.png" pos (595+20*-12,224)
        add "system/sT.png" pos (595+20*-11,224)
        add "system/sR.png" pos (595+20*-10,224)
        add "system/sA.png" pos (595+20*-9,224)
        add "system/sN.png" pos (595+20*-8,224)
        add "system/sG.png" pos (595+20*-7,224)
        add "system/sE.png" pos (595+20*-6,224)
        add "system/sB.png" pos (595+20*-4,224)
        add "system/sU.png" pos (595+20*-3,224)
        add "system/sI.png" pos (595+20*-2,224)
        add "system/sL.png" pos (595+20*-1,224)
        add "system/sD.png" pos (595+20*0,224)
        add "system/sI.png" pos (595+20*1,224)
        add "system/sN.png" pos (595+20*2,224)
        add "system/sG.png" pos (595+20*3,224)
        add "system/sF.png" pos (595+20*5,224)
        add "system/sI.png" pos (595+20*6,224)
        add "system/sL.png" pos (595+20*7,224)
        add "system/sL.png" pos (595+20*8,224)
        add "system/sE.png" pos (595+20*9,224)
        add "system/sD.png" pos (595+20*10,224)
        add "system/sO.png" pos (595+20*12,224)
        add "system/sF.png" pos (595+20*13,224)
        add "system/sL.png" pos (595+20*15,224)
        add "system/sO.png" pos (595+20*16,224)
        add "system/sV.png" pos (595+20*17,224)
        add "system/sE.png" pos (595+20*18,224)
        add "system/MRB~ipad.png" pos (233,363)
        if persistent.TEN:
            add "system/activeRouteFinished~ipad.png" pos (229+17*21,363+24*2)
        else:
            add "system/activeRouteNormal~ipad.png" pos (229+17*21,363+24*2)
    elif chara == "fei":
        add im.Scale("system/s3.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp35~ipad.png" pos (508+52*2,164)
        add "system/jp36~ipad.png" pos (508+52*3,164)
        add "system/jp37~ipad.png" pos (508+52*4,164)
        add "system/jp38~ipad.png" pos (508+52*5,164)
        add "system/jp4~ipad.png" pos (508+52*6,164)
        add "system/jp39~ipad.png" pos (508+52*7,164)
        add "system/jp40~ipad.png" pos (508+52*8,164)
        add "system/sS.png" pos (595+20*-1,224)
        add "system/sU.png" pos (595+20*0,224)
        add "system/sP.png" pos (595+20*1,224)
        add "system/sE.png" pos (595+20*2,224)
        add "system/sR.png" pos (595+20*3,224)
        add "system/sH.png" pos (595+20*5,224)
        add "system/sE.png" pos (595+20*6,224)
        add "system/sR.png" pos (595+20*7,224)
        add "system/sO.png" pos (595+20*8,224)
        add "system/sC.png" pos (595+20*10,224)
        add "system/sH.png" pos (595+20*11,224)
        add "system/sA.png" pos (595+20*12,224)
        add "system/sT.png" pos (595+20*13,224)
        add "system/sN.png" pos (595+20*15,224)
        add "system/sO.png" pos (595+20*16,224)
        add "system/sI.png" pos (595+20*17,224)
        add "system/sR.png" pos (595+20*18,224)
        add "system/FN2~ipad.png" pos (233,363)
        if persistent.FEI:
            add "system/activeRouteFinished~ipad.png" pos (229+17*21,363+24*4)
        else:
            add "system/activeRouteNormal~ipad.png" pos (229+17*21,363+24*4)
    elif chara == "ruk":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s5.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s2.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp41~ipad.png" pos (508,164)
        add "system/jp42~ipad.png" pos (508+52,164)
        add "system/jp43~ipad.png" pos (508+52*2,164)
        add "system/jp44~ipad.png" pos (508+52*3,164)
        add "system/jp4~ipad.png" pos (508+52*4,164)
        add "system/jp45~ipad.png" pos (508+52*5,164)
        add "system/jp46~ipad.png" pos (508+52*6,164)
        add "system/jp47~ipad.png" pos (508+52*7,164)
        add "system/jp48~ipad.png" pos (508+52*8,164)
        add "system/sH.png" pos (595+20*-8,224)
        add "system/sE.png" pos (595+20*-7,224)
        add "system/sR.png" pos (595+20*-6,224)
        add "system/sM.png" pos (595+20*-5,224)
        add "system/sA.png" pos (595+20*-4,224)
        add "system/sP.png" pos (595+20*-3,224)
        add "system/sH.png" pos (595+20*-2,224)
        add "system/sR.png" pos (595+20*-1,224)
        add "system/sO.png" pos (595+20*0,224)
        add "system/sD.png" pos (595+20*1,224)
        add "system/sI.png" pos (595+20*2,224)
        add "system/sT.png" pos (595+20*3,224)
        add "system/sU.png" pos (595+20*4,224)
        add "system/sS.png" pos (595+20*5,224)
        add "system/sI.png" pos (595+20*7,224)
        add "system/sN.png" pos (595+20*8,224)
        add "system/sL.png" pos (595+20*10,224)
        add "system/sA.png" pos (595+20*11,224)
        add "system/sB.png" pos (595+20*12,224)
        add "system/sY.png" pos (595+20*13,224)
        add "system/sR.png" pos (595+20*14,224)
        add "system/sI.png" pos (595+20*15,224)
        add "system/sN.png" pos (595+20*16,224)
        add "system/sT.png" pos (595+20*17,224)
        add "system/sH.png" pos (595+20*18,224)
        add "system/LUK~ipad.png" pos (233,363)
        if persistent.RUK:
            add "system/activeRouteFinished~ipad.png" pos (223+17*27,363)
        else:
            add "system/activeRouteNormal~ipad.png" pos (223+17*27,363)
    elif chara == "may":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s5.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp49~ipad.png" pos (508+52,164)
        add "system/jp50~ipad.png" pos (508+52*2,164)
        add "system/jp51~ipad.png" pos (508+52*3,164)
        add "system/jp52~ipad.png" pos (508+52*4,164)
        add "system/jp4~ipad.png" pos (508+52*5,164)
        add "system/jp53~ipad.png" pos (508+52*6,164)
        add "system/jp54~ipad.png" pos (508+52*7,164)
        add "system/jp55~ipad.png" pos (508+52*8,164)
        add "system/sE.png" pos (595+20*4,224)
        add "system/sT.png" pos (595+20*5,224)
        add "system/sE.png" pos (595+20*6,224)
        add "system/sR.png" pos (595+20*7,224)
        add "system/sN.png" pos (595+20*8,224)
        add "system/sA.png" pos (595+20*9,224)
        add "system/sL.png" pos (595+20*10,224)
        add "system/sP.png" pos (595+20*12,224)
        add "system/sO.png" pos (595+20*13,224)
        add "system/sL.png" pos (595+20*14,224)
        add "system/sA.png" pos (595+20*15,224)
        add "system/sR.png" pos (595+20*16,224)
        add "system/sI.png" pos (595+20*17,224)
        add "system/sS.png" pos (595+20*18,224)
        add "system/MAY~ipad.png" pos (233,363)
        if persistent.MAY:
            add "system/activeRouteFinished~ipad.png" pos (223+17*27,363+24*2)
        else:
            add "system/activeRouteNormal~ipad.png" pos (223+17*27,363+24*2)
    elif chara == "moe":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s5.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s0.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s9.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp56~ipad.png" pos (508+52*2,164)
        add "system/jp57~ipad.png" pos (508+52*3,164)
        add "system/jp58~ipad.png" pos (508+52*4,164)
        add "system/jp59~ipad.png" pos (508+52*5,164)
        add "system/jp4~ipad.png" pos (508+52*6,164)
        add "system/jp60~ipad.png" pos (508+52*7,164)
        add "system/jp61~ipad.png" pos (508+52*8,164)
        add "system/sQ.png" pos (595+20*-4,224)
        add "system/sU.png" pos (595+20*-3,224)
        add "system/sA.png" pos (595+20*-2,224)
        add "system/sN.png" pos (595+20*-1,224)
        add "system/sT.png" pos (595+20*0,224)
        add "system/sU.png" pos (595+20*1,224)
        add "system/sM.png" pos (595+20*2,224)
        add "system/sE.png" pos (595+20*4,224)
        add "system/sX.png" pos (595+20*5,224)
        add "system/sC.png" pos (595+20*6,224)
        add "system/sI.png" pos (595+20*7,224)
        add "system/sT.png" pos (595+20*8,224)
        add "system/sE.png" pos (595+20*9,224)
        add "system/sD.png" pos (595+20*10,224)
        add "system/sI.png" pos (595+20*12,224)
        add "system/sN.png" pos (595+20*13,224)
        add "system/sC.png" pos (595+20*15,224)
        add "system/sO.png" pos (595+20*16,224)
        add "system/sM.png" pos (595+20*17,224)
        add "system/sA.png" pos (595+20*18,224)
        add "system/MOE~ipad.png" pos (233,363)
        if persistent.MOE:
            add "system/activeRouteFinished~ipad.png" pos (223+17*27,363+24*4)
        else:
            add "system/activeRouteNormal~ipad.png" pos (223+17*27,363+24*4)
    elif chara == "oka2":
        add im.Scale("system/s4.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s5.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s4.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp62~ipad.png" pos (508+52*2,164)
        add "system/jp63~ipad.png" pos (508+52*3,164)
        add "system/jp64~ipad.png" pos (508+52*4,164)
        add "system/jp65~ipad.png" pos (508+52*5,164)
        add "system/jp4~ipad.png" pos (508+52*6,164)
        add "system/jp66~ipad.png" pos (508+52*7,164)
        add "system/jp67~ipad.png" pos (508+52*8,164)
        add "system/sT.png" pos (595+20*-18,224)
        add "system/sH.png" pos (595+20*-17,224)
        add "system/sR.png" pos (595+20*-16,224)
        add "system/sE.png" pos (595+20*-15,224)
        add "system/sE.png" pos (595+20*-14,224)
        add "system/sC.png" pos (595+20*-12,224)
        add "system/sO.png" pos (595+20*-11,224)
        add "system/sN.png" pos (595+20*-10,224)
        add "system/sT.png" pos (595+20*-9,224)
        add "system/sR.png" pos (595+20*-8,224)
        add "system/sA.png" pos (595+20*-7,224)
        add "system/sP.png" pos (595+20*-6,224)
        add "system/sA.png" pos (595+20*-5,224)
        add "system/sS.png" pos (595+20*-4,224)
        add "system/sS.png" pos (595+20*-3,224)
        add "system/sO.png" pos (595+20*-2,224)
        add "system/sA.png" pos (595+20*0,224)
        add "system/sB.png" pos (595+20*1,224)
        add "system/sO.png" pos (595+20*2,224)
        add "system/sU.png" pos (595+20*3,224)
        add "system/sT.png" pos (595+20*4,224)
        add "system/sT.png" pos (595+20*6,224)
        add "system/sH.png" pos (595+20*7,224)
        add "system/sE.png" pos (595+20*8,224)
        add "system/sA.png" pos (595+20*10,224)
        add "system/sB.png" pos (595+20*11,224)
        add "system/sD.png" pos (595+20*12,224)
        add "system/sU.png" pos (595+20*13,224)
        add "system/sC.png" pos (595+20*14,224)
        add "system/sT.png" pos (595+20*15,224)
        add "system/sI.png" pos (595+20*16,224)
        add "system/sO.png" pos (595+20*17,224)
        add "system/sN.png" pos (595+20*18,224)
        add "system/OKA~ipad.png" pos (233,363)
        if persistent.OKA2:
            add "system/activeRouteFinished~ipad.png" pos (217+17*33,363+24*2)
        else:
            add "system/activeRouteNormal~ipad.png" pos (217+17*33,363+24*2)
    elif chara == "nae":
        add im.Scale("system/s0.png",33,68) pos (1024-345,46)
        add im.Scale("system/s-0.png",33,68) pos (1024-345+36,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36+37,46)
        add im.Scale("system/s3.png",33,68) pos (1024-345+36*2+37,46)
        add im.Scale("system/s7.png",33,68) pos (1024-345+36*2+37*2,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*3+37*2,46)
        add im.Scale("system/s6.png",33,68) pos (1024-345+36*3+37*3,46)
        add im.Scale("system/s1.png",33,68) pos (1024-345+36*4+37*3,46)
        add "system/jp68~ipad.png" pos (508+52*3,164)
        add "system/jp69~ipad.png" pos (508+52*4,164)
        add "system/jp4~ipad.png" pos (508+52*5,164)
        add "system/jp70~ipad.png" pos (508+52*6,164)
        add "system/jp71~ipad.png" pos (508+52*7,164)
        add "system/jp72~ipad.png" pos (508+52*8,164)
        add "system/sB.png" pos (595+20*3,224)
        add "system/sI.png" pos (595+20*4,224)
        add "system/sF.png" pos (595+20*5,224)
        add "system/sR.png" pos (595+20*6,224)
        add "system/sO.png" pos (595+20*7,224)
        add "system/sS.png" pos (595+20*8,224)
        add "system/sT.png" pos (595+20*9,224)
        add "system/sO.png" pos (595+20*11,224)
        add "system/sF.png" pos (595+20*12,224)
        add "system/sL.png" pos (595+20*14,224)
        add "system/sU.png" pos (595+20*15,224)
        add "system/sN.png" pos (595+20*16,224)
        add "system/sA.png" pos (595+20*17,224)
        add "system/sR.png" pos (595+20*18,224)
        add "system/NAE~ipad.png" pos (233,363)
        if persistent.NAE:
            add "system/activeRouteFinished~ipad.png" pos (211+17*38,363+24*2)
        else:
            add "system/activeRouteNormal~ipad.png" pos (211+17*38,363+24*2)
    add "system/branch1~ipad.png" pos (394+80,412-49)
    if chara!="oka1":
        imagebutton:
            if persistent.OKA1:
                idle "system/routeFinished~ipad.png"
                hover "system/routeFinished~ipad.png"
            else:
                idle "system/routenormal~ipad.png"
                hover "system/routenormal~ipad.png"
            action Show("route_choose",transition=dissolve,chara="oka1")
            pos (394,412)
    if chara !="dar":
        imagebutton:
            if persistent.DAR:
                idle "system/routeFinished~ipad.png"
                hover "system/routeFinished~ipad.png"
            else:
                idle "system/routenormal~ipad.png"
                hover "system/routenormal~ipad.png"
            action Show("route_choose",transition=dissolve,chara="dar")
            pos (235+17*15,362+25)
    if chara !="crs":
        imagebutton:
            if persistent.CRS:
                idle "system/routeFinished~ipad.png"
                hover "system/routeFinished~ipad.png"
            else:
                idle "system/routenormal~ipad.png"
                hover "system/routenormal~ipad.png"
            action Show("route_choose",transition=dissolve,chara="crs")
            pos (235+17*15,362+25*3-2)
    if persistent.DAR or persistent.CRS:
        add "system/branch2~ipad.png" pos (229+17*20,363)
        if chara !="suz":
            imagebutton:
                if persistent.SUZ:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="suz")
                pos (229+17*21,363)
        if chara != "ten":
            imagebutton:
                if persistent.TEN:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="ten")
                pos (229+17*21,363+24*2)
        if chara != "fei":
            imagebutton:
                if persistent.FEI:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="fei")
                pos (229+17*21,363+24*4)
    if persistent.TEN or persistent.FEI or persistent.SUZ:
        add "system/branch3~ipad.png" pos (224+17*26,363)
        if chara != "ruk":
            imagebutton:
                if persistent.RUK:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="ruk")
                pos (223+17*27,363)
        if chara != "may":
            imagebutton:
                if persistent.MAY:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="may")
                pos (223+17*27,363+24*2)
        if chara != "moe":
            imagebutton:
                if persistent.MOE:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="moe")
                pos (223+17*27,363+24*4)
    if persistent.RUK and persistent.MOE and persistent.MAY and persistent.TEN and persistent.FEI and persistent.SUZ and persistent.DAR and persistent.CRS:
        add "system/branch4~ipad.png" pos (219+17*32,363)
        if chara != "oka2":
            imagebutton:
                if persistent.OKA2:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="oka2")
                pos (217+17*33,363+24*2)
    if persistent.OKA2:
        if chara != "nae":
            imagebutton:
                if persistent.NAE:
                    idle "system/routeFinished~ipad.png"
                    hover "system/routeFinished~ipad.png"
                else:
                    idle "system/routenormal~ipad.png"
                    hover "system/routenormal~ipad.png"
                action Show("route_choose",transition=dissolve,chara="nae")
                pos (211+17*38,363+24*2)
    imagebutton:
        idle "system/enter~ipad.png"
        hover "system/enter~ipad.png"
        pos (211+17*39,365+24*4)
        if chara == "oka1":
            action Start(label="SGFD2_ROUTE_OKA")
        elif chara == "dar":
            action Start(label="SGFD2_ROUTE_DAR")
        elif chara == "crs":
            action Start(label="SGFD2_ROUTE_CRS")
        elif chara == "fei":
            action Start(label="SGFD2_ROUTE_FEI")
        elif chara == "may":
            action Start(label="SGFD2_ROUTE_MAY")
        elif chara == "ten":
            action Start(label="SGFD2_ROUTE_TEN")
        elif chara == "oka2":
            action Start(label="SGFD2_ROUTE_KYO")
        elif chara == "ruk":
            action Start(label="SGFD2_ROUTE_RUK")
        elif chara == "nae":
            action Start(label="SGFD2_ROUTE_NAE")
        elif chara == "moe":
            action Start(label="SGFD2_ROUTE_MOE")
        elif chara == "suz":
            action Start(label="SGFD2_ROUTE_SUZ")
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Show("mainmenu_title")] align (1.0,1.0)
    key "game_menu" action [With(dissolve),Show("mainmenu_title")]



screen navigation:


    window:
        style "gm_root"


    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:


    style gm_nav_button:
        size_group "gm_nav"



screen file_picker(quick=False):
    if quick==True:
        timer 0.0000001 action FilePage("quick")
    hbox:
        style_group "file_picker_nav"
        align (0.0,1.0)

        textbutton _("Previous"):
            text_size 28
            action FilePagePrevious()

        textbutton _("Auto"):
            text_size 28
            action FilePage("auto")

        textbutton _("Quick"):
            text_size 28
            action FilePage("quick")

        for i in range(1, 11):
            textbutton str(i):
                text_size 28
                action FilePage(i)
        textbutton _("Next"):
            text_size 28
            action FilePageNext(max=10)
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    key "game_menu" action [With(dissolve),Return()]
    grid 2 3:
        area (40,80,900,450)
        for i in range(1,7):
            button:
                action FileAction(i)
                background None
                xfill True
                add im.Scale("system/bgSaveSlot~ipad.png",400,123)


                add im.Scale(FileScreenshot(i,empty="system/iconCell~ipad.png"),160,100) pos (9,13)
                $ file_name = FileSlotName(i, 6)
                $ file_time = FileTime(i, empty="")
                $ save_name = FileSaveName(i)
                if FileNewest(file_name):
                    add "system/lastSave~ipad.png" pos (0,0)
                if file_name[0]!= 'q' and file_name[0]!= 'a':
                    text "No. %02d" % int(file_name) pos (180,13) size 25
                    text save_name pos (180,40) size 20
                    text "储存于" xanchor 0.0 pos (180,80) size 18 color "0ff"
                    text "[file_time!t]\n" xanchor 1.0 pos (380,80) size 18 color "0ff"
                else:
                    $ file_name = file_name[1:]
                    text "No. %02d" % int(file_name) pos (180,13) size 25
                    if file_time!="":
                        text save_name pos (180,40) size 20
                        text "储存于" xanchor 0.0 pos (180,80) size 18 color "0ff"
                        text "[file_time!t]\n" xanchor 1.0 pos (380,80) size 18 color "0ff"
                key "save_delete" action FileDelete(i)


screen save tag menu:


    window:
        background "system/bgSave~ipad.png"

    use file_picker

screen load(quick=False) tag menu:



    if quick == False:
        window:
            background "system/bgLoad~ipad.png"
    else:
        window:
            background "system/bgQLoad~ipad.png"

    use file_picker(quick=quick)

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


screen preferences tag menu:

    window:
        style "mm_root"

    $ config_bg = im.Scale("system/bgConfig~ipad.png",768,576)
    add config_bg xpos 512-768/2
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (630,45) action SetField(persistent,"skipmail",True)
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (715,45) action SetField(persistent,"skipmail",False)
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (630,95) action SetField(persistent,"bgmdown",True)
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (715,95) action SetField(persistent,"bgmdown",False)
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (630,145) action SetField(persistent,"tips",True)
    imagebutton idle Null(103,70) hover Null(103,70) selected_idle "system/btnCheck1~ipad.png" selected_hover "system/btnCheck1~ipad.png" pos (715,145) action SetField(persistent,"tips",False)
    bar value Preference("text speed") area (490,278,260,10)
    bar value Preference("auto-forward time") area (490,327,260,10)
    bar value Preference("voice volume") area (490,376,260,10)
    bar value Preference("music volume") area (490,425,260,10)
    bar value Preference("sound volume") area (490,474,260,10)
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    key "game_menu" action [With(dissolve),Return()]


screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

screen quick_menu:

    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

transform rmenuin:
    im.Scale("system/bgGmenu~ipad.png",342*3/4,576)
    xanchor 1.0
    xpos 0
    linear 0.5 xanchor 0.0
    Null()
transform rmenubtnin:
    xanchor 1.0
    xpos 0
    linear 0.5 xanchor 0.0
transform rmenubtnout:
    ypos 20
    LiveCrop((269,0,269,536),"system/btnGMenu~ipad.png")
    xanchor 0.0
    xpos 0
    linear 0.5 xanchor 1.0
    Null()
transform rmenuout:
    im.Scale("system/bgGmenu~ipad.png",342*3/4,576)
    xanchor 0.0
    xpos 0
    linear 0.5 xanchor 1.0
    Null()

transform rmenubg:
    im.Scale("system/bgGmenu~ipad.png",342*3/4,576)
    alpha 0.0
    0.5
    alpha 1.0
transform rmenuwait:
    alpha 0
    pause 1
    alpha 1
screen rmenu tag menu:

    on "show" action stopvoc
    add Null() at rmenuin
    key 'game_menu' action [Add(Null(),rmenuout,1),Add(Null(),rmenubtnout,2),Show("rmenuhide")]
    add rmenubg
    imagemap:
        at rmenubtnin
        ypos 20
        ground LiveCrop((269,0,269,536),"system/btnGMenu~ipad.png")
        idle LiveCrop((269,0,269,536),"system/btnGMenu~ipad.png")
        hover LiveCrop((0,0,269,536),"system/btnGMenu~ipad.png")
        selected_idle LiveCrop((269,0,269,536),"system/btnGMenu~ipad.png")
        selected_hover LiveCrop((0,0,269,536),"system/btnGMenu~ipad.png")

        hotspot (0,0,269,53) action [SetVariable("yvalue", 1.0), ShowMenu("text_history",dissolve)]
        hotspot (0,53,269,53) action [QuickSave(message='快速存档完成',newest=True),Add(Null(),rmenuout,1),Add(Null(),rmenubtnout,2),Show("rmenuhide")]
        hotspot (0,53*2,269,53) action [Show("load",dissolve,quick=True)]
        hotspot (0,53*3,269,53) action [Show("save",dissolve)]
        hotspot (0,53*4,269,53) action [Show("load",dissolve)]
        hotspot (0,53*5,269,53) action [Show("preferences",dissolve)]
        hotspot (0,53*7,269,53) action [Show("tips",dissolve)]
        hotspot (0,53*8,269,53) action [Show("help",dissolve)]
        hotspot (0,53*9,269,53) action [MainMenu(confirm=True),Show("rmenuhide",fast=True)]
    key 'K_LCTRL' action NullAction()
    key 'K_RCTRL' action NullAction()
screen rmenuhide(fast=False) tag menu:

    if not fast:
        timer 0.5 action [Return()]
    else:
        timer 0.0000001 action [Return()]


screen tips tag menu:
    $ persistent.gd['AchievementData'][27]['Check']=1
    default tip = None
    $ list = persistent.gd["TIPSData"]
    window:
        style "mm_root"

    $ cl_bg = im.Scale("system/bgTips~ipad.jpg",768,576)
    add cl_bg xpos 512-768/2
    window:
        area (512-768/2+35,94*3/4+5,200,440)
        background None
        has viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
        grid 1 len(list):
            for index,t in enumerate(list):
                $ t["index"]=index
                if t["Check"] == 0:
                    button:
                        ymargin 2
                        background None
                        text str(index+1)+". ???" color "0f0"
                        action NullAction()
                else:
                    button:
                        ymargin 2
                        background None
                        text str(index+1)+". "+t["Name"] color "0f0"
                        action SetScreenVariable("tip",t)
    if tip != None:
        text "No. "+str(tip["index"]+1) pos (210+512-768/2+35,94*3/4+5) color "fff" size 25
        text tip["Name"] xanchor 1.0 pos (850,94*3/4+5) color "fff" size 32
        text tip["Category"] pos (210+512-768/2+45,125) color "0f0" size 25
        text tip["Pronun"] xanchor 1.0 pos (855,125) color "0ff" size 25
        window:
            area (210+512-768/2+30,165,520,350)
            background None
            python:
                content = sub(r"#n",r"\n",tip["Content"])

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                text content size 25

    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
transform tipsin:
    xcenter .5
    yanchor 1.0

    easein 1 ypos 81
transform tipstextin:
    yanchor 1.0
    ypos -30
    xpos 70
    easein 1 ypos 51
transform tipsout:
    xcenter .5
    yanchor 0
    ypos 0
    "system/cellBuyin~ipad.png"
    easeout 1 ypos -81
transform tipstextout(i):
    yanchor 1.0
    pos (70,51)
    Text('"{color=#f00}'+gd["TIPSData"][i]['Name']+'{/color}"'+'词条已登陆。')
    easeout 1 ypos -30
screen tips_pop(i=0) tag tip:

    if not persistent.tips == True:
        timer 0.00000001 action Hide("tips_pop")
    else:
        add "system/cellBuyin~ipad.png" at tipsin
        text '"{color=#f00}'+gd["TIPSData"][i]['Name']+'{/color}"'+'词条已登陆。' at tipstextin
        timer 3 action [Show("tipshide"),Add(Null(),tipstextout(i),i=3)]
        timer 3 action Add(Null(),tipsout,i=2)

screen tipshide tag tip:

    timer 0.000001 action Hide("tip")


screen tips tag menu:
    default tip = None
    $ list = persistent.gd["TIPSData"]
    window:
        style "mm_root"

    $ cl_bg = im.Scale("system/bgTips~ipad.png",768,576)
    add cl_bg xpos 512-768/2
    window:
        area (512-768/2+35,94*3/4+5,200,420)
        background None
        has viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
        grid 1 len(list):
            for index,t in enumerate(list):
                $ t["index"]=index
                if t["Check"] == 0 and not persistent.NAE:
                    button:


                        text str(index+1)+". ???" color "0f0" size 18
                        action NullAction()
                else:
                    button:


                        text str(index+1)+". "+t["Name"] color "0f0" size 18
                        action SetScreenVariable("tip",t)
    if tip != None:
        text "No. "+str(tip["index"]+1) pos (210+512-768/2+35,94*3/4+5) color "fff" size 25
        text tip["Name"] xanchor 1.0 pos (850,94*3/4+5) color "fff" size 18
        text tip["Category"] pos (210+512-768/2+45,125) color "0f0" size 25
        text tip["Pronun"] xanchor 1.0 pos (855,125) color "0ff" size 25
        window:
            area (210+512-768/2+30,165,520,350)
            background None
            python:
                content = sub(r"#n",r"\n",tip["Content"])

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                text content size 25

    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)


screen achan(file):
    $ t = open(renpy.loader.transfn(file),"r").read().decode("UTF-8")
    $ t = sub(r"&c14;(.*?)&c0;",r"{color=#0e0}\1{/color}",t)
    $ t = sub(r"&rs(.*?)&re",r"{color=#00f}\1{/color}",t)

    add "bg/IBG053A~ipad.jpg" at truecenter
    viewport:
        mousewheel True
        draggable True
        area (188,139,634,381)
        text t color "000"
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)


screen phoneweb(file):
    add "system/phone_movie_"+current_route+"~ipad.png" at truecenter
    $ t = open(renpy.loader.transfn(file),"r").read().decode("UTF-8")
    $ t = sub(r"&c14;(.*?)&c0;",r"{color=#0e0}\1{/color}",t)
    $ t = sub(r"&rs(.*?)&re",r"{color=#00f}\1{/color}",t)
    viewport:
        mousewheel True
        draggable True
        area (291,41,436,487)
        text t color "000"
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
