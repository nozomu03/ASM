################################################################################
## Initialization
################################################################################

init offset = -1
#custom

define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiNedJaNOXnTyQGvgm+DZgdE++BuaPbMka2TD44DgoGXFIK8MXEI0wXaEmPnZ4NUeu3+l2Y0GrOIAt/gnmmmhksVfGXSblFG/8+Ad3my18zoMaxoJ8ubKfLzFUzQiAccpfPey3DxUon01olqd5tq7pKK/d1OKSH6DjihI33w1EtgiBxnH5MJr6SoyOoE/F43L70iENrPBcNwLU2BU0NE5zYX/jb/UKIxnOrXJr1gR5bxa2+5xgbSe13dxVKj7FeRVKEdUfdmUD5sr6QNS4/bkGKKn3HWVBHG9eCjnqhkzI7Fr2BHRjMDMbnYH4RKpD5w51DiQZlxFNCcL7B07yqz40wIDAQAB"

init python:
    morning=afternoon=evening="일정"


screen planner:
    add "bg_black.png"
    vbox:
        align(.5, .5)
        grid 3 2:
            text "아침"
            text "점심"
            text "저녁"

            textbutton "[morning]" action Show("inside", period = 'morning')
            textbutton "[afternoon]" action Show("inside", period = 'afternoon')
            textbutton "[evening]" action Show("inside", period = 'evening')

    textbutton "완료" action Return() align (.6, .6)

screen inside:
    vbox:
        align (.5, .8)
        textbutton "교내 탐사" action[SetVariable(period, "교내 탐사"), Hide("inside")]
        textbutton "수영장" action[SetVariable(period, "수영장"), Hide("inside")]
        textbutton "야구장" action[SetVariable(period, "야구장"), Hide("inside")]
        textbutton "도서관" action[SetVariable(period, "도서관"), Hide("inside")]
        textbutton "강당" action[SetVariable(period, "강당"), Hide("inside")]
        textbutton "매점" action[SetVariable(period, "매점"), Hide("inside")]
        textbutton "교실에 있기" action[SetVariable(period, "교실에 있기"), Hide("inside")]

screen profile:
    #modal True
    imagebutton idle "icon_menu.png" hover "icon_menuhover.png" align(.0, .0) action[Show('memobutton'), Hide('profile')]

screen memobutton:
    add "icon_menuhover.png" align(.0, .0)
    imagebutton idle "icon_menu" hover "icon_menu" pos(350, 0) action[Show('profile'), Hide('memobutton')]
    imagebutton idle "icon_memo.png" hover "icon_memo1.png" action[Show('inprofile'), Show('profile'), Hide('memobutton')]
    textbutton "인벤토리" pos(200, 15) action Show('inventory_screen')

init python:
    def name_func(newstring):
        store.firstname = newstring

        
    def lastname_func(newstring):
        store.lastname = newstring

init:
    default firstname = " "
    default lastname = " "
    
#screen open_screen:


screen text_input_screen():
    frame:
        xsize 1280
        ysize 180
        xpos 0
        ypos 0
        vbox:
            text "{size=+5}메모"
            button:
                id "input_1"
                xysize (1280, 720)
                action NullAction()
                #hover_sound ""
                add Input(hover_color="#3399ff",size=28, color="#3399ff", default=firstname, length=60, changed=name_func, button=renpy.get_widget("text_input_screen","input_1")) yalign 0.0
        textbutton "Done" action Hide("text_input_screen") ypos 140

screen inprofile:
    add "bg_black.png"
    #modal True
    textbutton "닫기" action[Hide('inprofile'), Show('profile')] align (.95,.04)  
    vbox:
        align(.5, .5)
        textbutton "open" action Show("text_input_screen")

        grid 3 3:
            textbutton '아리아     ' action[Show("profile_a"), Hide("inprofile"), Hide("profile")]
            textbutton '실피아     ' action[Show("profile_s"), Hide("inprofile"), Hide("profile")]
            textbutton '로라       ' action[Show("profile_l"), Hide("inprofile"), Hide("profile")]
            textbutton '레이나     ' action[Show("profile_r"), Hide("inprofile"), Hide("profile")]
            textbutton '에릭스     ' action[Show("profile_e"), Hide("inprofile"), Hide("profile")]
            textbutton '레아       ' action[Show("profile_leah"), Hide("inprofile"), Hide("profile")]
            textbutton '페르틴     ' action[Show("profile_p"), Hide("inprofile"), Hide("profile")]
            textbutton '크레이     ' action[Show("profile_c"), Hide("inprofile"), Hide("profile")]
            textbutton '미첼       ' action[Show("profile_m"), Hide("inprofile"), Hide("profile")]

        #    textbutton "매ㅑㅎㅈ;ㅑㅐ거호;갿"
        #    textbutton "매ㅑㅎㅈ;ㅑㅐ거호;갿"

screen memo:
    python:
        inputoption()

screen profile_a_a:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_a_a'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "anie_nom" 
    text "{color=#FF6CAA}{size=+20}애니{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value anie_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value anie_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value anie_pok
                xmaximum 500
                range 100
    text "{color=#FF6CAA}{size=+20}중학교 3학년 1반 담임.\n아리아의 언니로 감정 표현이 조금 솔직하지\n못한 선생님이다.{/size}{/color}" pos(400, 400)    

screen profile_m:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_m'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "mitchell_nomal" 
    text "{color=#00FF3C}{size=+20}미첼{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value m_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value m_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value m_cru
                xmaximum 500
                range 100
    text "{color=#00FF3C}{size=+20}고등학교 1학년 1반.\n작년 학생회장이였다.\n남녀 상관없이 인기가 많으며\n친위대도 있다.{/size}{/color}" pos(400, 400)

screen profile_a:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_a'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "aria_nomal" 
    text "{color=#5ABEF5}{size=+20}아리아{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value a_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value a_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value a_yan
                xmaximum 500
                range 100
    text "{color=#5ABEF5}{size=+20}중학교 2학년 2반.\n연초에 반 친구들한테 괴롭힘 받는 것을 \n내가 구해준 뒤로 계속 날 쫒아 다닌다.{/size}{/color}" pos(400, 400)

screen profile_s:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_s'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "silpia_nomal" 
    text "{color=#FF22DF}{size=+20}실피아{/size}{/color}" pos(400, 0)
    
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value s_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value s_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value s_hen
                xmaximum 500
                range 100
    
    text "{color=#FF22DF}{size=+20}고등학교 2학년 3반.\n수영을 아주 잘하는 예쁜 선배님이다.\n총무부의 부장이며 학생회 사람들과 사이가\n좋지 않다.{/size}{/color}" pos(400, 400)

screen profile_l:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_l'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "lola_nom" 
    text "{color=#2FFF00}{size=+20}로라{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value s_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value s_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value l_dark
                xmaximum 500
                range 100
    
    text "{color=2FFF00}{size=+20}중학교 2학년 2반.\n나와 도서관에서 처음 만났으며, 그 이후로\n가끔씩 도서관에서 만나며 친해졌다.\n공부를 아주 잘하며, 귀엽다.{/size}{/color}" pos(400, 400)

screen profile_p:
    modal True
    textbutton  "{size=+20}닫기{/size}" action[Hide('profile_p'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "pertin_nom" 
    text "{color=#BA0303}{size=+20}페르틴{/size}{/color}" pos(400, 0)
    
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value p_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value p_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value p_sis
                xmaximum 500
                range 100
    text "{color=#BA0303}{size=+20}고등학교 3학년.\n학교 이사장의 딸이며 학생회장이다.\n총무부, 특히 실피아와는 견원지간이며\n전 학생회장인 미첼과도 사이가 좋지 않다.{/size}{/color}" pos(400, 400)

screen profile_r:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_r'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    text "{color=#DA00FF}{size=+20}레이나{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value r_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value r_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value r_blah
                xmaximum 500
                range 100
    text "{color=#DA00FF}{size=+20}중학교 3학년 1반.\n거의 알려진게 없는 미스테리한 소녀.\n책을 상당히 좋아하는 듯 하며\n수준급의 검도 실력을 가지고 있다.{/size}{/color}" pos(400, 400)

screen profile_e:
    modal True
    #add "leah_nom.png" 
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_e'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    text "{color=#0004FF}{size=+20}에릭스{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value e_ikari
                xmaximum 500
                range 100
    text "{color=#0004FF}{size=+20}중학교 3학년 1반.\n남을 잘 품어주는 따뜻한 성격으로 인기가 많다.\n페르틴과의 사이가 좋지 않다는 소문이 있다.{/size}{/color}" pos(400, 400) 
    
screen profile_leah:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_leah'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    add "leah_nom"
    text "{color=#FF0000}{size=+20}레아{/size}{/color}" pos(400, 0)
    vbox:
        hbox:
            text("호감도") pos(680, 0)
            bar:
                pos(710, 0)
                value leah_ko 
                xmaximum 500
                range 100 
    vbox:
        hbox:
            text "신뢰도" pos(680, 100)
            bar:
                pos(710, 100)
                value leah_shin
                xmaximum 500
                range 100
    vbox:
        hbox:
            text "  ???  " pos(680, 200)          
            bar:
                pos(710, 200)
                value leah_end
                xmaximum 500
                range 100
        if leah_event==True:                                                        
            text "{color=#FF0000}{size=+20}중학교 3학년 1반.\n학기 도중에 전학해 온 전학생이다. 학생회장 페르틴의 여동생이라고 한다.\n지병이 있어 약을 먹고 있다.{/size}{/color}" pos(400, 400)
        else:
            text "{color=#FF0000}{size=+20}중학교 3학년 1반.\n학기 도중에 전학해 온 전학생이다.{/size}{/color}" pos(400, 400)        

screen profile_c:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_c'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    text "{color=#C46C00}{size=+20}크레이{/size}{/color}" pos(400, 0)
    if c_start==True:
        vbox:
            hbox:
                text "  ???  " pos(680, 200)          
                bar:
                    pos(710, 200)
                    value 
                    xmaximum 500
                    range 100
        text "{color=#C46C00}{size=+20}중학교 2학년 2반.\n무슨 일이 있어도 쾌활한 검도부의 무드 메이커\n소문에 따르면 레이나를 좋아한다고 한다.{/size}{/color}" pos(400, 400) 
    else:
        text "{color=#C46C00}{size=+20}데이터 없음{/size}{/color}" pos(400, 400) 
screen profile_sena:
    modal True
    textbutton "{size=+20}닫기{/size}" action[Hide('profile_sena'), Show('inprofile')] pos(400, 0)
    add "bg_black"
    text "{color=#ffb6c1}{size=+20}한세나{/size}{/color}" pos(400, 0)
    text "{color=#ffb6c1}{size=+20}데이터 없음.{/size}{/color}" pos(400, 400) 
###############################################################################
#screen check:
#    modal True
#    add "bg_black.png"
#    
#    vbox:
#        align(.5, .5)
#        grid 4 2:
#            text "아리아: [a_ko] "
#            text "로라: [l_ko] "
#            text "실피아: [s_ko] "
#            text "페르틴: [p_ko] "
#           text "무물: [m_ko] "
#            text "레이나: [r_ko] "
#            text "레아 [leah_ko] "
#            text "애니 [anie_ko] "

################################################################################
#549, 45 left top
#771 45
#987 45
#220
#45 259 472
init -1 python:
    import renpy.store as store
    import renpy.exports as renpy 
    from operator import attrgetter 
    _menu=0
    inv_page = 0 
    item = None
    class Item(store.object):
        def __init__(self, name, hidden="", image=""):
            self.name = name
            self.hidden=hidden
            self.image=image 

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item):
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"


    showitems = True
screen inventory_button:
    textbutton "인벤토리" action [Show("inventory_screen"), Hide("inventory_button")] pos(1170, 0)
screen inventory_screen:    
    add "inven_back.png" 
    modal True    
    textbutton "X 닫기" action [ Hide("inventory_screen"), Show("inventory_button"), Hide("gui_tooltip")] align (.95,.04)
    $x = 549 
    $y = -169
    $i = 0
    $sorted_items = sorted(inventory.items, key=attrgetter('hidden'), reverse=True) 
    for item in sorted_items:
        $ x += 220
        if i%3==0:
            $ y += 214
            $ x = 549
        $ pic = item.image
        $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") 
        imagebutton idle pic hover pic xpos x ypos y action [Show("gui_tooltip", my_picture=my_tooltip, my_tt_xpos=x, my_tt_ypos=y)] 
        $i+=1
screen gui_tooltip (my_picture=my_tooltip, my_tt_xpos=0, my_tt_ypos=0):
    add my_picture xpos 0 ypos 0


init -1:
    image tooltip_inventory_choco=LiveComposite((665, 73), (0,10), ImageReference("text_frame"), (50, 150), Text("                {size=+20}{color=#FFFFFF}판 초콜릿{/color}{/size}"))
    
    image tooltip_inventory_mail=LiveComposite((665, 73), (0,10), ImageReference("text_frame"), (50, 150), Text("                {size=+20}{color=#FFFFFF}편지{/color}{/size}"))



################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

#init:
    #$narrator = Character(None, window_background="bg_room1.jpg")


screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() 


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("뒤로") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("스킵") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동저장") action Preference("auto-forward", "toggle")
            textbutton _("저장하기") action ShowMenu('save')
            textbutton _("퀵세이브") action QuickSave()
            textbutton _("퀵로드") action QuickLoad()
            textbutton _("설정") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("저장하기") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("환경 설정") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("메인 메뉴") action MainMenu()

        textbutton _("렌파이란") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("도움말") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("끝내기") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20
    
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("돌아가기"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "mouse" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("렌파이란"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("저장하기"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}AUTO") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}QUICK") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    use game_menu(_("환경 설정"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 모드") action Preference("display", "window")
                        textbutton _("전체 화면 모드") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("스킵")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("선택지 이후 스킵") action Preference("after choices", "toggle")
                    textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    label _("클릭 비활성화")
                    textbutton "활성화" action Preference("auto-forward after click", "toggle")
                    textbutton "비활성화" action Preference("auto-forward after click", "disable")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("배경음 크기")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("효과음 크기")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("음성 크기")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("도움말"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("네") action yes_action
                textbutton _("아니오") action no_action

    ## Right-click and escape answer "no".
    key "mouse" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 1.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("뒤로") action Rollback()
        textbutton _("스킵") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("자동저장") action [Preference("auto-forward", "toggle")]
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600