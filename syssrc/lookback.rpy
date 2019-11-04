init -3 python:

    style.readback_window.xmaximum = 760
    style.readback_window.ymaximum = 500
    style.readback_window.align = (.5, .5)

    style.readback_frame.background = None
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5

    style.readback_text.color = "#fff"

    style.create("readback_button", "readback_text")
    style.readback_button.background = None

    style.create("readback_button_text", "readback_text")
    style.readback_button_text.selected_color = "#f12"
    style.readback_button_text.hover_color = "#f12"

    style.readback_label_text.bold = True


    config.locked = False 


    config.readback_buffer_length = 100 
    config.readback_full = True 
    config.readback_disallowed_tags = ["size"] 
    config.readback_choice_prefix = ">> "   


    config.locked = True

init -2 python:

    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            current_voice = ''
            return

    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)

    config.nvl_show_display_say = say_wrapper
    adv = ReadbackADVCharacter(show_function=say_wrapper,name="",ctc="cursor")
    narrator = ReadbackADVCharacter(show_function=say_wrapper,name="",ctc="cursor",callback=stopallvoc)
    name_only = ReadbackADVCharacter(show_function=say_wrapper,name="",ctc="cursor")
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter

    def voice(file, **kwargs):
        global current_voice
        if not config.has_voice:
            return
        
        _voice.play = file
        
        current_voice = file

    def menu(items, **add_input): 
        
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
        
        rv = renpy.display_menu(newitems, **add_input)
        
        
        for label, val in items:
            if rv == val:
                current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv

    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """
        
        widget_properties = { }
        dialogue = [ ]
        
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue
            
            who, what, kwargs = entry
            
            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"
            
            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
            
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]
            
            dialogue.append((who, what, who_id, what_id, window_id))
        
        return widget_properties, dialogue


    def nvl_menu(items):
        
        renpy.mode('nvl_menu')
        
        if nvl_list is None:
            stonvl_list = [ ]
        
        screen = None
        
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
        
        if screen is not None:
            
            widget_properties, dialogue = nvl_screen_dialogue()        
            
            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
            
            for label, val in items:
                if rv == val:
                    current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
        
        ui.layer("transient")
        ui.clear()
        ui.close()
        
        ui.window(style=_m1_lookback__s(style.nvl_window))
        ui.vbox(style=_m1_lookback__s(style.nvl_vbox))
        
        for i in nvl_list:
            if not i:
                continue
            
            who, what, kw = i            
            rv = renpy.show_display_say(who, what, **kw)
        
        renpy.display_menu(items, interact=False,
                           window_style=_m1_lookback__s(style.nvl_menu_window),
                           choice_style=_m1_lookback__s(style.nvl_menu_choice),
                           choice_chosen_style=_m1_lookback__s(style.nvl_menu_choice_chosen),
                           choice_button_style=_m1_lookback__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=_m1_lookback__s(style.nvl_menu_choice_chosen_button),
                           )
        
        ui.close()
        
        roll_forward = renpy.roll_forward_info()
        
        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)
        
        for label, val in items:
            if rv == val:
                current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv


    readback_buffer = []
    current_line = None
    current_voice = None

    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
            current_voice = None

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)

    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    from re import *
    remove_tags_expr = compile(disallowed_tags_regexp) 
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    if config.readback_full:
        config.rollback_enabled = False


init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):
            
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)

    def store_yvalue(y):
        global yvalue
        yvalue = int(y)

screen text_history tag menu:

    modal True

    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []

    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]

    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):
        $ lines_to_show = readback_buffer + [current_line]

    else:
        $ lines_to_show = readback_buffer


    $ adj = NewAdj(changed = store_yvalue, step = 300)

    window:
        style_group "readback"
        frame:
            background None
            maximum (760,480)
            align (.5,.5)
            has viewport:
                align (.5,.5)
                mousewheel True
                draggable True
                yinitial 1.0
                yadjustment adj

            vbox:

                null height 10

                for line in lines_to_show:

                    if line[0] and line[0] != " ":
                        label line[0]


                    if not line[2]:
                        text line[1]


                    else:
                        textbutton line[1] action Play("voice", line[2] )

                    null height 10

        textbutton _("Return") action [Stop("voice"),Return()] align (.97, 1.0)


        key "game_menu" action [Stop("voice"),Hide("text_history",transition=dissolve)]
