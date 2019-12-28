define config.name = _("ambiguity")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _("")
define build.name = "ambiguity"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.after_load_transition = None
define config.end_game_transition = None

define config.developer = True
define config.window = "hide"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 30
default preferences.afm_time = 15



define config.save_directory = "ambiguity-1507129421"
define config.window_icon = "gui/window_icon.png"
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.png', 'archive')
    build.classify('**jpg', 'archive')
    build.classify('**mp3', 'archive')
    build.classify('**ttf', 'archive')
    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
