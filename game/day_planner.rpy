




init -100 python:


    style.dp_frame = Style(style.frame)
    style.dp_vbox = Style(style.vbox)
    style.dp_hbox = Style(style.hbox)


    style.dp_choices = Style(style.default)
    style.dp_choices_vbox = Style(style.vbox) 
    style.dp_choices.xalign = 0.5


    style.dp_choice_button = Style(style.button)
    style.dp_choice_button_text = Style(style.button_text)

    style.dp_done_button = Style(style.button)
    style.dp_done_button_text = Style(style.button_text)


    style.dp_label = Style(style.label)
    style.dp_label_text = Style(style.label_text)


    dp_done_title = "Done Planning"



    _m1_day_planner__periods = { }


    _m1_day_planner__period = None

    class _m1_day_planner__Period(object):
        
        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        _m1_day_planner__periods[name] = store._m1_day_planner__period = _m1_day_planner__Period(name, var)

    _m1_day_planner__None = object()

    def dp_choice(name, value=_m1_day_planner__None, enable="True", show="True"):
        
        if not _m1_day_planner__period:
            raise Exception("Choices must be part of a defined period.")
        
        if value is _m1_day_planner__None:
            value = name
        
        _m1_day_planner__period.acts.append((name, value, enable, show))

    def _m1_day_planner__set_noncurried(var, value):
        setattr(store, var, value)
        return True

    _m1_day_planner__set = renpy.curry(_m1_day_planner__set_noncurried)


label day_planner(periods):

    python hide:
        renpy.choice_for_skipping()

label day_planner_repeat:

    if renpy.has_label("dp_callback"):
        call dp_callback from _call_dp_callback

    python hide:

        ui.window(style=style.dp_frame)
        ui.vbox(style=style.dp_vbox)
        ui.hbox(style=style.dp_hbox)

        can_continue = True

        for p in periods:
            
            if p not in _m1_day_planner__periods:
                raise Exception("Period %r was never defined." % p)
            
            ui.window(style=style.dp_choices)
            ui.vbox(style=style.dp_choices_vbox)
            
            p = _m1_day_planner__periods[p]
            v = getattr(store, p.var)
            
            layout.label(p.name, "dp")
            
            valid_choice = False
            
            for name, value, enable, show in p.acts:
                show = eval(show)
                enable = eval(enable)
                
                selected = (v == value)
                
                if show:
                    layout.button(
                        name, 
                        "dp_choice",
                        clicked=_m1_day_planner__set(p.var, value),
                        selected=selected,
                        enabled=enable,
                        )
                
                if show and enable and selected:
                    valid_choice = True
            
            if not valid_choice:
                can_continue = False
            
            ui.close()

        ui.close() 

        layout.button(
            dp_done_title,
            "dp_done",
            clicked=ui.returns(False),
            enabled=can_continue)

        ui.close() 

    if ui.interact():
        jump day_planner_repeat
    else:
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
