transform moving:
    linear 0.5 yalign 0.7
    linear 0.5 yalign 0.5
    linear 0.5 yalign 0.7
    linear 0.5 yalign 0.5

transform moving1:

    linear 1.0 yalign 0.8
    linear 1.0 yalign 0.5

init:
    image ctc_rotate:
        xpos 1100
        ypos 620

        "ctc.png"
        linear 2000000 rotate 360000000

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

image lola_haps = LiveComposite(
    (405, 720), 
    (460, 0), "lola_hapsframe.png", 
    (460, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8), 
    (460, 0), Animation("lola_mouse0.png", .2) 
)


image lola_haps2 = LiveComposite(
    (405, 720), 
    (460, 0), "lola_hapsframe.png", 
    (460, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8), 
    (460, 0), Animation("lola_mouse0.png", .2) 
)

image nonmouth = LiveComposite(
    (405, 720), 
    (900, 0), "lola_hapsframe.png", 
    (900, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8), 
    (900, 0), Animation("lola_mouse0.png", .2) 
)


image lola_eye:
    "lola_eyeopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "lola_eyeclose.png"
    .25
    repeat

image lola_mouse:
    "lola_mouse0.png"
    .2
    "lola_mouse1.png"
    .2
    "lola_mouse2.png"
    .2
    "lola_mouse1.png"
    .2
    repeat


image side movelola happy1 = LiveComposite(
    (405, 720), 
    (900, 0), "lola_hapsframe.png", 
    (900, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8), 
    (900, 0), Animation("lola_mouse0.png", .2, "lola_mouse1.png", .2, "lola_mouse0.png", .2 ) 
)

image side movelola happy2 = LiveComposite(
    (405, 720), 
    (900, 0), "lola_hapsframe.png", 
    (900, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8), 
    (900, 0), Animation("lola_mouse0.png", .2) 
)

image side movelola nomhap1 = LiveComposite(
    (405, 720),
    (900, 0), "lola_hapframe.png",
    (900, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8),
    (900, 0), Animation("lola_mouse0.png", .4, "lola_mouse1.png", .4)
)

image side movelola nomhap2 = LiveComposite(
    (405, 720),
    (900, 0), "lola_hapframe.png",
    (900, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8)
)

image side moveanie happy1 = LiveComposite(
    (360, 720),
    (900, 0), "anie_frame.png",
    (900, 0), Animation("anie_eye1.png", .8, "anie_eye2", 3.0),
    (900, 0), Animation("anie_mouse0.png", .4, "anie_mouse", .4)
)

image anie_happy2 = LiveComposite(
    (360, 720),
    (440, 0), "anie_frame.png",
    (440, 0), Animation("anie_eye1.png", .8, "anie_eye2", 3.0),
    (440, 0), "anie_mouse0.png"
)

image side movemumul happy1 = LiveComposite(
    (386, 720),
    (900, 0), "mumul_frame.png",
    (900, 0), Animation("mumul_eye0.png" ,.8, "mumul_eye1.png", 3.0),
    (900, 0), Animation("mumul_mouse0.png", .4, "mumul_mouse1.png", .4)
)

image mumul_haps = LiveComposite(
    (386, 720),
    (450, 0), "mumul_frame.png",
    (450, 0), Animation("mumul_eye0.png" ,.8, "mumul_eye1.png", 3.0),
    (450, 0), "mumul_mouse0.png"
)
image side movelola sup = "lola_sup.png"

image shy = "lola_shy.png"


image lola_nomhap2 = LiveComposite(
    (405, 720),
    (460, 0), "lola_hapframe.png",
    (460, 0), Animation("lola_eyeopen.png", 3.0, "lola_eyeclose.png", .8)
)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
