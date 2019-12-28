define name = Character('tempname', dynamic=True)
define mama = Character('엄마', color="#c8ffc8", ctc="ctc_rotate", ctc_position="fixed")
define a = Character('아리아', color="5ABEF5", ctc="ctc_rotate", ctc_position="fixed")
define a_a = Character('애니', color="FF6CAA", ctc="ctc_rotate", ctc_position="fixed")
define d = Character('데릭스', color="21FF00", ctc="ctc_rotate", ctc_position="fixed")
define c = Character('???', color="939393", ctc="ctc_rotate", ctc_position="fixed")
define ar = Character('에릭스', color="0004FF", ctc="ctc_rotate", ctc_position="fixed")
define reina = Character ('레이나', color="DA00FF", ctc="ctc_rotate", ctc_position="fixed")
define crey = Character('크레이', color="C46C00", ctc="ctc_rotate", ctc_position="fixed")
define lina = Character ('리나', color="8881FF", ctc="ctc_rotate", ctc_position="fixed")
define aser = Character ('아서', color="E0DEFF", ctc="ctc_rotate", ctc_position="fixed")
define silpia = Character ('실피아', color="FF22DF", ctc="ctc_rotate", ctc_position="fixed")
define mitchell = Character('미첼', color="00FF3C", ctc="ctc_rotate", ctc_position="fixed")
define laula = Character('로라', color="2FFF00", ctc="ctc_rotate", ctc_position="fixed")
define flot = Character ('플로트', color="C0C0C0", ctc="ctc_rotate", ctc_position="fixed")
define a1 = Character ('아리아 ', who_color="#FF0000", what_color="#FF0000", ctc="ctc_rotate", ctc_position="fixed")
define leah = Character('레아', color="#FF0000", ctc="ctc_rotate", ctc_position="fixed")
define mumul = Character('무물', color="#8904B1", ctc="ctc_rotate", ctc_position="fixed")
define haul = Character('하율', color="#FB1010", ctc="ctc_rotate", ctc_position="fixed")
define pertin = Character('페르틴', color="#BA0303", ctc="ctc_rotate", ctc_position="fixed")
define right = Position(xpos=900, ypos=720)
define centor = Position(xalign=0.5, ypos=720)
define left = Position(xpos=250, ypos=720)
define upcentor = Position(xalign=.4, ypos=640)
define lola = Character('로라', image="movelola", color="2FFF00", ctc="ctc_rotate", ctc_position="fixed")
define sena = Character('한세나', who_color="#ffb6c1", what_color="#9A91FF", ctc="ctc_rotate", ctc_position="fixed")
define sewol = Character('란세월', who_color="#025BD1", what_color = "#90FCBE", ctc="ctc_rotate", ctc_position="fixed")
define anie = Character('애니', image= "moveanie", color="FF6CAA", ctc="ctc_rotate", ctc_position="fixed")
define mumul1 = Character('무물', image="movemumul", color="#0004FF", ctc="ctc_rotate", ctc_position="fixed")
define sin = Character('신', who_color="#00FF80", what_color='#97F14D', ctc="ctc_rotate", ctc_position="fixed")
define tedian = Character('테디안', color="#8E6464", ctc="ctc_rotate", ctc_position="fixed")
define zeno = Character('제노', who_color="#FFEB5A", what_color="787878", ctc="ctc_rotate", what_bold=True, ctc_position="fixed")




define nvlnarr = Character(None, kind=nvl)
label temp:
    silpia "으아아아아아아아아아-!! 테디아아아아안!!!!!"
    return

init python:
    choco = Item("choco", image="gui/inv_choco.png")
    mail = Item("mail", image="gui/inv_mail.png")
    inventory = Inventory()
    gender=" "
    grade=0
    h=0
    m=0
    derix_true=0

    a_ko=20
    a_shin=30
    a_yan=10

    s_ko=10
    s_shin=30
    s_hen=5

    l_ko=10
    l_shin=30
    l_dark=20

    p_ko=0
    p_shin=0
    p_sis=0

    m_ko=0
    m_shin=10
    m_cru=0

    r_ko=10
    r_shin=10
    r_blah=0
    hehe=0

    leah_ko=10
    leah_shin=10
    leah_event=False
    leah_end=0

    anie_ko=10
    anie_shin=10
    anie_pok=0

    sena_start=False
    sena_ko=0
    sena_shin=0

    e_ikari=0

    c_reinacon=0
    c_start=False


image bg_teachers = im.Sepia("bg_teacher.jpg")


define PythonActivity = None

label abcdefg:
    call events_run_period from _call_events_run_period
    return

init python:
    eventcount=False
    mornig_move=""
    tempname=None
    school_check=True
    if renpy.android:
        import jnius
        PythonActivity = jnius.autoclass('org.renpy.android.PythonSDLActivity')

    def inputText2():
        if renpy.android:
            return PythonActivity.inputTextbox()
        
        else:
            return renpy.input("이름 입력")
    act="만남"

init python:
    temp=False

    leah_mail=False
    style.my_style=Style(style.default)
    style.say_thought.line_leading=12
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 10
    style.ruby_style.yoffset=-20
    style.default.ruby_style=style.ruby_style
    lolasleep=0

init python:
    draggeded=""
    city=""
    def dragged(drags, drop):
        if not drop:
            return
        
        store.draggeded = drags[0].drag_name
        store.city = drop.drag_name
        
        return True

screen sche:
    add "bg_map.png"
    modal True
    draggroup:
        drag:
            drag_name "me"
            child "icon_me.png"
            droppable False
            dragged dragged
            xpos 257 ypos 524

        drag:
            drag_name "보건실"
            child "icon_redcross.png"
            draggable False
            xpos 70 ypos 241

        drag:
            drag_name "음악실"
            child "icon_music.png"
            draggable False
            xpos 355 ypos 449

        drag:
            drag_name "총무부"
            child "icon_money.png"
            draggable False
            xpos 390 ypos 630

screen sche2:
    add "bg_map.png"
    modal True
    draggroup:
        drag:
            drag_name "me"
            child "icon_me.png"
            droppable False
            dragged dragged
            xpos 257 ypos 524

        drag:
            drag_name "도서관"
            child "icon_lib.png"
            droppable True
            draggable False
            xpos 386 ypos 502

        drag:
            drag_name "신발장"
            child "icon_shoes.png"
            droppable True
            draggable False
            xpos 59 ypos 200

        drag:
            drag_name "쉼터"
            child "icon_rest.png"
            droppable True
            draggable False
            xpos 70 ypos 76

screen sche3:
    add "bg_map.png"
    modal True
    draggroup:
        drag:
            drag_name "me"
            child "icon_me.png"
            droppable False
            dragged dragged
            xpos 257 ypos 524

        drag:
            drag_name "쉼터"
            droppable True
            child "icon_rest.png"
            draggable False
            xpos 70 ypos 76

        drag:
            drag_name "검도부"
            droppable True
            draggable False


image walkingPE:
    align (.5, .5)
    "bg_pe.jpg"
    linear 2.0 zoom (2.5)

image camera_right:
    align (.5, .5)
    zoom (2.5)
    "bg_pe.jpg"
    linear 2.0 align (.8, .5) zoom (4.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
