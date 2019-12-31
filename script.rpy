init python:
    mp=MultiPersistent("renpy.second.org")

label valueswap:
    $ a_ko=mp.value_a_ko
    $ a_shin=mp.value_a_shin
    $ a_yan=mp.value_a_et

    $ s_ko=mp.value_s_ko
    $ s_shin=mp.value_s_shin
    $ s_oka=mp.value_s_oka

    $ l_ko=mp.value_l_ko
    $ l_shin=mp.value_l_shin
    $ l_dark=mp.value_l_kuro

    $ m_ko=mp.value_m_ko
    $ m_shin=mp.value_m_shin
    $ m_cru=mp.value_m_cru

    $ r_ko=mp.value_r_ko
    $ r_shin=mp.value_r_shin
    $ r_blah=mp.value_r_kill
    return

label start:

    window show
    if renpy.android:
        "가나다라마바사"
    nvlnarr " 안녕하심까.\n다들 '사카'라고 알고 있지만 사실 풀 닉네임은 '사카_지민'인 닝겐입니다."
    nvlnarr " 제가 왜 나왔을까요?\n바로 여러분들께 '어떤 정보'를 드리기 위해서입니다."
    nvlnarr " 현재 쌍둥이의 성좌를 비주얼 노벨라이징 하고 있는 '팀 더 제미니 비주얼 노블라이징 시퀸스'의 문은 언제나 열러 있습니다."
    nvlnarr " '일러스트', '음악', '프로그래밍', '시나리오', '마케터' 등"
    nvlnarr " 수많은 분야의 수많은 여러분들을 기다리고 있습니다."
    nvlnarr " 기회는 지금입니다.\n당신의 손을 잡을 수 있을 날을 기대하며 기다리고 있겠습니다."
    window hide
    nvl clear

    nvlnarr "-나는 '초콜릿'이란 이름으로 불렸던 것을 입에 집어넣었다.\n혀에 그것이 닿자 달달하면서도 쓴 맛을 가진 액체로 변했다가 덧없이 사라졌다.\n-이리야 케이지, 라스트 스토리 {font=HigashiOmeGothic.ttf}中{/font}."
    nvl clear
    window hide

    if mp.value_playername != None:
        call valueswap from _call_valueswap
        "part 1의 데이터가 발견되었습니다. {w=1.0}이름과 성별을 유지하고 플레이 하시겠습니까?{p=1.0}'아니오'를 선택하여도 호감도를 비롯한 캐릭터 관련 정보는 유지됩니다."
        menu:
            "예":
                $ tempname = mp.value_playername
                $ gender = mp.value_g
            "아니오":
                $ tempname = inputText2()
    else:

        $ tempname = inputText2()
        "가이드" "주인공의 성별은 무엇인가요?"
        menu:
            "남자":
                $ gender="남자"
            "여자":
                $ gender="여자"
        "주인공의 이름은 [tempname], 성별은 [gender].\n맞나요?"
        menu:
            "예":
                "12세 이상 이용가 모드로 진행하시겠습니까?"
                menu:
                    "네":
                        $ grade=1
                    "아니요":
                        $ grade=0
            "아니요":
                $ hehe+=1
                jump start
        "[draggeded], [city]"
    "3개월 전"
    show leah_nom at right with dissolve
    $ persistent.inven=None
    "내 이름은 레아다.\n태어났을 때부터 몸이 자주 아팠기 때문에 학교에 제대로 다녀본 기억은 없지만,\n이제 몸도 많이 괜찮아졌으니까 분명 괜찮을 것이다."
    "그래도 갑작스럽게 아버지가 날 여기로 전학시켜서 좀 많이 놀랐다.\n이번엔 학교생활 열심히 해서 친구들도 많이 사귀자."
    "시계를 보자 시간은 이미 오전 8시였다.\n 선생님이 분명 8시 30분까지 와 달라고 했지.\n 슬슬 출발하자."

    scene bg_black with dissolve
    show screen profile
    play sound "door.mp3"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_school with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_classroom with dissolve
    show leah_nom at left with dissolve
    show anie_happy2
    anie happy1 "자, 얘들아. 오늘은 전학생이 있어."
    leah "내 이름은 레아야. 앞으로 1년 동안 잘 부탁할게."
    anie happy1 "레아는 원래 다른 도시에 있다가 온 아이니까 주변이 많이 낯설거야. 그러니까 모두들 레아에게 잘 해줘야 한다?"
    "학생들" "네~"
    anie happy1 "자. 그럼 조회는 여기까지. 레아는 음... 그래, 일단은 [name] 옆에 앉으렴. [name]은 오늘 레아한테 학교를 소개시켜 주고."
    name "네."
    play sound "walk_slow.mp3"
    hide anie_happy2
    $ renpy.pause(2.3)
    name "안녕."
    leah "아... 안녕."
    play sound "bell_nomal.mp3"
    scene bg_black with dissolve
    $ renpy.pause(2.0)
    scene bg_hallway
    a "[name] 선배~"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.3)
    show aria_happy at left with dissolve
    name "왜 또."
    "한 여자아이가 [name]에게 달라 붙었다.\n나에겐 들리지 않았지만 [name]에게 무엇인가 말한 듯 했다."
    name "아, 미안. 나 아무래도 어딜 좀 갔다 와야 할 거 같아. 학교 안내는 얘가 마저 해 줄 거야."
    a "아리아에요! 잘 부탁드릴게요!"
    leah "난 레아라고 해."
    play sound "walk_slow.mp3"
    "나는 아리아와 함께 교무실로 갔다."
    play sound "door.mp3"
    scene bg_black with dissolve
    $ renpy.pause(2.0)
    scene bg_book with dissolve
    show leah_nom at right
    show aria_nomal at left
    with dissolve
    a "이 도서관엔 정말 별 책들이 다 있어요. 아마 찾으려는 책들은 거의 다 찾을 수 있을걸요?"
    "북카트에 꽂혀 있는 책 중 한 권이 눈에 띄었다."
    a "뭔가 신경 쓰이는 거라도 있어요?"
    leah "{font=HigashiOmeGothic.ttf}舞{rt}まい{/rt}る兎{rt}うさぎ{/rt}の命{rt}いのち{/rt}が終{rt}お{/rt}わった時{rt}とき{/rt}{/font}. 춤추는 토끼의 생명이 끝난 때...\n 추리 소설인가?"

    "나는 책을 집어 뒤집었다."
    a "작가는... 음..."
    leah "이리아 케이지 ."
    a "아는 작가에요?"
    leah "응."
    a "누군데요?"
    leah "일본의 라이트노벨 작가야. ROA 시리즈를 쓴 게 이 사람이지."
    "뒷편에는 '인간은 모래의 누각에서 다시금 영광을 탐한다.'\n'이리아 케이지와 대작 소설 ROA 시리즈 완결 후 4년만에 그의 손에 의해 다시 시작되는 이야기'"
    "'일러스트레이터 IHK 전격합류!'라고 적혀 있었다."
    leah "확실히 별게 다 있는 거 같긴 하네. 학교 도서관에 이런 책이 있다는 것부터 말이야."
    a "그죠? 그렇기 때문에 이 도서관이 이렇게 넓은 거랍니다!\n"
    scene bg_black with dissolve
    play sound "bell_nomal.mp3"
    $ renpy.pause(2.0)
    "밤이 깊었다. \n학생들은 다들 각자의 짐을 챙겨 기숙사로 이동했다."
    scene bg_nightschool with dissolve
    play sound "walk_slow.mp3"
    show pertin_hap at left
    show leah_nom at right
    with dissolve
    pertin "레아."
    leah "언니!"
    pertin "학교에서 보낸 하루는 어땠어? 재밌었어?"
    leah "응!"
    "언니는 내 머리를 쓰다듬었다."
    pertin "다행이다."
    leah "그럼 나 내일부터 학교 다닐 수 있는거야?"
    pertin "그럼!"
    hide leah_nom
    show leah_hap at right
    pertin "그렇게 좋아?"
    leah "응!"
    pertin "그래도 병원은 계속 다니고, 약도 제대로 먹어야한다?"
    leah "알고 있어!"
    pertin "그래."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_nightapartment with dissolve
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_room with dissolve
    show leah_hap at centor with dissolve
    leah "후아..."
    "의사 선생님과 아버지와 언니를 열심히 졸라서 겨우 다닐 수 있게 된 학교다.\n내가 기대했던 만큼 즐거운 시간이 될 것 같다."
    "나는 씻기 위해 화장실로 들어갔다."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_bathroom with dissolve
    play sound "shower.mp3"
    $ renpy.pause(8.0)
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_room with dissolve
    $ renpy.pause(1.0)
    scene bg_black with dissolve
    "불을 끄고 침대에 누웠다."
    $ renpy.pause(2.0)
    show achieve_leahstroy with dissolve
    $ achievement.grant("leahstory")
    $ renpy.pause(2.0)
    hide achieve_leahstroy
    scene bg_room2 with dissolve
    show lola_haps
    show aria_happy at left
    with dissolve
    name "재밌게 놀았어?"
    "로라, 아리아" "네!"
    hide lola_haps1
    show lola_haps2
    name "그럼 씻으러 가자."
    "로라, 아리아" "네!"
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_black
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    "우리들은 계단을 통해 지하로 내려갔다."
    name "너희들은 저쪽이지? 지금이 9시니까 1시간 정도만 씻고 와~"
    laula "넹~"
    play sound "door.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "shower.mp3"
    $ renpy.pause(2.0)
    scene bg_fitting with dissolve
    $ renpy.pause(1.0)
    scene bg_black with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(1.0)
    scene bg_room2 with dissolve
    play sound "door.mp3"
    $ renpy.pause(2.0)
    "내가 방 안에 들어가자 이미 로라와 아리아는 와 있었다."
    show aria_happy at left with dissolve
    show lola_haps with dissolve
    laula "아, 선배. 방금 전에 아주머니가 왔다 갔어요."
    hide lola_haps
    show lola_haps2
    name "어? 그래?"
    a "네. 아무래도 하루, 이틀 정도 더 걸릴거라고 하던데요."
    name "그래...? 그럼 밥도 우리끼리 먹어야겠네."
    "나는 냉장고를 열어봤다."

    "마침 냉장고엔 고기와 밀가루, 계란이 있었다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_kitchen with dissolve
    "환풍기를 튼 후 조각낸 고기에 밀가루를 묻힌 뒤\n 계란물에 한 번 담그고, 찰랑거릴 정도로 기름이\n부어져 있는 프라이팬에 집어 넣었다."
    play sound "frying.mp3"
    $ renpy.pause(4.0)
    "튀겨진 고기들을 재빨리 건져냈다."
    name "로라?"
    laula "예~!"
    name "아리아랑 와서 이거 좀 옮겨줄래?"
    laula "네~"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    show lola_haps2 with dissolve
    show aria_happy at left with dissolve
    name "자, 로라는 이걸 식탁으로 좀 옮겨줘. 아리아는 수저 좀 놔줄래?"
    a "예."
    scene bg_black with dissolve
    "우리 셋은 식탁에 앉아 튀김을 먹기 시작했다."
    play sound "eat.mp3"
    $ renpy.pause(1.0)
    play sound "eat.mp3"
    $ renpy.pause(1.0)
    play sound "eat.mp3"
    $ renpy.pause(5.0)
    "설거지를 마친 후 아리아와 로라는 양치를 하더니 자러 들어가 버렸다."
    "나는 원래라면 엄마 아빠가 써야 했을 방에 앉아 혼자 TV를 보다 슬슬 졸리길래 내 방으로 돌아와 불을 끄고 침대에 누웠다."
    name "......."
    $ renpy.pause(5.0)
    "얼마나 시간이 흘렀을까? 나는 살짝 눈을 떴다."
    "내 옆에서 바스락 거리는 소리가 들린다.\n옆을 돌아보자..."
    a "냠냠냠..."
    "침대에서 일어나 불을 키자..."
    scene bg_room2 with dissolve
    show aria_nomal at right with dissolve
    $ renpy.pause(1.0)
    hide aria_nomal
    show aria_happy at right
    a "어라라, 깼어요 선배?"
    "나는 시간을 확인했다.\n오전 3시 20분."
    name "......."
    a "...?"
    name "너, 대체 왜 여기에 있는거냐?"
    a "? 문제라도 있나요?"
    name "네 방은 어쩌고 이리로 온 건데?"
    a "잠이 안와서 아까 왔는데요?"
    name "......."
    menu:
        "쫒아낸다.":
            name "가! 가! 어서 가!"
            "나는 아리아의 등을 떠밀었다."
            a "헤에~ 선배~ 가련한 소녀를 침대에서 떨어뜨리려고 하다니~"
            "아리아는 내 팔을 붙잡고 매달렸다.\n타인의 체온이 피부를 통해 느껴졌다."
            a "계속 밀면 더한 짓도 해버릴거에요?"
            name "...에휴..."
            "나는 팔을 끌어당겼다.\n아리아가 거기에 달려 다시 침대 가운데로 돌아왔다."
            $ renpy.pause(2.0)
            "아리아는 조금 뒤척거리더니 좋은 자리를 잡았는지 움직이는 걸 멈추었다."
            a "선배."
            name "왜?"
            a "선배 덕분이에요."
            name "뭐가?"
            a "예전엔 하루하루가 고통이었고, 괴로웠는데 선배 덕분에 전부 괜찮아졌어요. 선배 같은 선배가 있어서 행복해요. 고마워요 선배."
            "싱긋 웃는 아리아."
            a "선배 덕분이에요."
            name "자라. 내일 또 졸려서 비틀거리지 말고."
            a "칫."
            scene bg_black with dissolve
            "아리아는 내 한 쪽 팔을 끌어안고 누웠다."
            name "덥다. 떨어져라. 땀 난다고!"
            a "히잉."
            "아리아는 문 쪽으로 몸을 돌렸다."
            $ a_ko+=8
            $ a_shin +=15
            $ a_yan += 3
        "내버려둔다.":
            "어차피 밀어내거나 해 봤자 더 귀찮게 굴 것이다."
            name "너무 치대지 말고 가만히 있어."
            a "예~♡"
            "아리아는 슬금슬금 몸을 돌려서 내게서 손가락 한 마디 정도 떨어진 곳에 자리를 잡았다."
            a "선배, 그럼 안녕히 주무세요~"
            "이 녀석이 옆에 있어서 제대로 못 잘 것 같지만 그 말은 하느니만 못할 것이다."
            name "잘자라."
            scene bg_black with dissolve
            "역시나 내 기대를 배신하지 않고 아리아의 손이 내 팔에 닿았지만 애써 무시했다."
            $ a_ko+=5
            $ a_shin+=15
    if grade==1 and gender== "남자":
        "........"
        "선배는 다시 잠들었다."
        a "선배?"
        name "........"
        a "선배에~?"
        name "........"
        "나는 오빠 옆에 달라붙었다.\n살짝 손을 뻗어 오빠의 가슴 위에 손을 올려봤다."
        "쿵쿵. 심장의 고동이 내 손을 타고 전해졌다."
        hide aria_happy
        show aria_yan at centor with dissolve
        a1 "오빠, 오빠가 절 지켜줘서 제가 살 수 있었으니까\n오빠는 제가 지켜드릴게요.\n많이, 엄청 많이 좋아해요. 그러니까...\n오.빠.는.제.것.이.에.요"
        $ renpy.pause(2.0)
        hide aria_yan
        show achieve_bedscene with dissolve
        $ achievement.grant("bedscene")
        $ renpy.pause(2.0)
    elif grade==1 and gender ==  "여자":
        "........"
        "선배는 다시 잠들었다."
        a "선배?"
        name "........"
        a "선배에~?"
        name "........"
        "나는 언니 옆에 달라붙었다.\n살짝 손을 뻗어 언니의 가슴 위에 손을 올려봤다."
        "쿵쿵. 심장의 고동이 내 손을 타고 전해졌다."
        hide aria_happy
        show aria_yan at centor with dissolve
        a1 "언니, 언니가 절 지켜줘서 제가 살 수 있었으니까\n언니는 제가 지켜드릴게요.\n많이, 엄청 많이 좋아해요. 그러니까...\n언.니.는.제.것.이.에.요"
        $ renpy.pause(2.0)
        hide aria_yan
        show achieve_bedscene with dissolve
        $ achievement.grant("bedscene")
        $ renpy.pause(2.0)
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    $ renpy.pause(5.0)
    "눈이 스르륵 떠졌다."
    name "으으음..."
    scene bg_room2 with dissolve
    show aria_happy at right with dissolve
    a "선배, 일어나셨어요?"
    name "...응..."
    "약간 남아있는 잠 기운을 세수로 씻어내기 위해 화장실로 향했다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_bathroom with dissolve
    play sound "door.mp3"
    $ renpy.pause(2.0)
    play sound "washing.mp3"
    $ renpy.pause(2.0)
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_living with dissolve
    show nonmouth with dissolve
    lola happy1 "아, 선배. 일어나셨어요? 간밤에 아리아가 그 쪽에 간 모양이던데, 안녕히 주무셨나요?"
    name "뭐, 그럭저럭."
    lola happy1 "그래요? 다행이네요. \n아, 선배님, 화장실 다 쓰셨나요?"
    name "어? 어."
    "나는 문 앞에서 비켰다."
    hide lola_haps2

    show aria_happy at left with dissolve
    a "이제 완전히 일어났어요?"
    name "아마도. 그보다, 아침 안 먹었지?"
    a "네."
    name "오늘은 냉장고에 아무것도 없으니까, 내려가서 사먹기로 하자."
    a "네♪"
    play sound "door.mp3"
    $ renpy.pause(2.0)
    show lola_haps2
    name "로라. 밥 먹으러 나갈거야. 챙길 거 있으면 빨리 챙겨."
    lola happy1 "없어요."
    name "그래? 그럼 나가자."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_stairroom with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    "셋이서 머리를 맞대고 의논한 결과 근처 패밀리 레스토랑에 가기로 했다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_family with dissolve
    show lola_haps2
    show aria_happy at left
    with dissolve
    "나는 파스타를, 로라는 돈까스, 아리아는 필라프를 시키고 기다렸다."
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    "점원" "주문하신 음식 나왔습니다."
    a "잘먹겠습니다."
    show lola_haps2
    lola happy1 "잘먹겠습니다."
    play sound "bite.mp3"
    play sound "eat.mp3"
    $ renpy.pause(2.0)
    "로라의 볼에 소스가 묻었다."
    menu:
        "귀엽다. 그냥 내버려 두자.":
            "나는 아무말 없이 파스타를 먹으며 흘끗흘끗 로라를 바라봤다."
            play sound "jab.mp3"
            hide aria_happy
            show aria_nomal at left
            a "선배?"
            "아리아가 웃는 얼굴로 날 쳐다봤다."
            "그 모습이 너무 무서워서 난 비명조차 삼켜버렸다."
            lola happy1 "에? 예? 무슨 일이에요? 저만 모르는거에요?"
            $ a_yan+=3
            hide aria_nomal
        "알려준다.":
            name "로라, 뺨에."
            "로라는 거울을 보더니 얼굴을 붉혔다."
            hide lola_haps2
            show lola_shy at right
            "늘 로라를 볼때 마다 '귀엽다'라고 느꼈지만 부끄러워 하는 모습은 상상을 초월할 정도로 귀여웠다."
            a "닦아."
            "로라는 아리아가 준 냅킨으로 볼을 닦았다."
            $ l_ko+=5
            hide lola_shy
        "닦아줄까?":
            "나는 냅킨을 하나 뽑았다."
            name "로라, 잠깐만."
            laula "네?"
            "나는 로라의 볼에 냅킨을 가져다 덌다."
            hide lola_haps2
            show lola_shy at right
            laula "왜... 왜요!"
            a "선.배?"
            name "아냐아냐아냐, 이상한 거 아냐."
            "나는 냅킨을 내 보였다."
            name "닦아준거야. 닦아준거라고!"
            "아리아는 날 여전히 의심의 눈초리로 쏘아봤지만 로라는 표정을 풀었다."
            hide lola_sups
            show lola_shy at right
            laula "고...고마워요... 선배..."
            "순간 나는 벙쪘다."
            play sound "jab.mp3"
            "아리아가 나의 다리를 걷어찼다."
            name "그...그래..."
            $ l_ko+=10
            $ a_yan+=4
            hide lola_shy
    show lola_haps2
    show aria_happy at left
    $ renpy.pause(2.0)
    "음식을 다 먹고 우린 밖으로 나왔다."
    play sound "walk_slow.mp3"
    scene bg_black with dissolve
    "건물의 숲 속으로 걸어 들어간 우리들은 그 안을 한참 동안 헤매고 다녔다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_living with dissolve
    show aria_happy at left
    show lola_haps2
    with dissolve
    a "어? 여기 뭔가 올려져 있는데요?"
    "쪽지 하나와 5만원짜리 지폐 두 장이 있다."
    "일이 예상외로 복잡하게 흘러가서 옆동네까지 가야 함. \n냉장고 안에 음식 재료들 넣어 놨으니 알아서 먹을 것!!!"
    name "일단 돌아다니면서 땀을 많이 흘렸으니까 씻고 와."
    laula "선배는요?"
    name "화장실에도 욕조는 있으니까 거기서 씻게."
    hide lola_haps2
    play sound "door.mp3"
    "둘은 뒤돌아 나갔다."
    $ renpy.pause(2.0)
    scene bg_bathroom with dissolve
    play sound "shower.mp3"
    $ renpy.pause(5.0)
    "깨끗하게 씻은 뒤 욕실 밖으로 나왔다."
    scene bg_living with dissolve
    "방으로 들어가 옷을 갈아입기 시작했다."
    scene bg_room2 with dissolve
    if grade==1:
        play sound "door.mp3"
        laula "선배?"
        show lola_haps at right with dissolve
        hide lola_haps
        show lola_sups at right with dissolve
        hide lola_sups
        show lola_shy at right with dissolve
        laula "어맛."
        name "...로라?"
        "나는 잠깐 멍해졌다."
        "로라도 마찬가지인지 나를 빤히 바라봤다."
        name "로라? 언제까지 보고 있을거니?"
        "로라는 바지만 걸치고 있는 내 몸에서 시선을 땠다."
        laula "시...실례했습니다..."
        $ l_ko+=4
        play sound "door.mp3"
    scene bg_living with dissolve
    show aria_happy at left with dissolve
    show lola_haps2 with dissolve
    "아리아와 로라는 거실에 축 늘어졌다."
    lola happy1 "아, 선배. 아까전에 아래쪽 목욕탕에 갔다가 이런 걸 봤어요."
    "로라는 내게 홍보지를 내밀었다."
    name "SF 전시관?"
    lola "네."
    a "되게 재미있을 거 같이 생겨서 받아왔어요~"
    name "가볼까? 보니까 학생은 무료라는데."
    lola "네~♪"
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_sfhall with dissolve
    "건물의 입구부터 영화나 애니메이션에서나 나올 법한\n 종류의 문으로 되어 있었다."
    play sound "sliding.mp3"
    scene bg_sfhallway with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_sfwappon with dissolve
    show lola_haps2 with dissolve
    show aria_happy at left with dissolve
    "다양한 영화와 애니메이션에 등장하는 무기와 탈것들의\n 모형이 전시되어 있다."
    play sound "walk_slow.mp3"
    lola "뭐가 많네요"
    play sound "walk_slow.mp3"
    "우리들은 계속 돌아다녔다."
    $ renpy.pause(2.0)
    name "오."
    "책들이 가득 꽂혀있는 책꽂이가 세워져 있었다.\n옆에 세워진 표지판에 적혀진 글자.\n책 무료로 드립니다(인당 한 권씩만 가져가세요)."
    name "음... {font=HigashiOmeGothic.ttf}入{rt}いり{/rt}矢{rt}や{/rt}ケ{rt}け{/rt}イ{rt}い{/rt}ジ{rt}じ{/rt}{/font}. 이리야 케이지.\n레아가 좋아하는 사람이네."
    a "아, 맞아요. 예전에 전학 온 첫날에도 도서관에서 이리야 케이지의 책을 한참 쳐다봤었어요."
    lola happy1 "그렇네요. 제가 도서관에서 공부하고 있었을 때에도 가끔씩 왔었는데 그때 항상 이리야 케이지의 책을 읽고 있었어요."
    "나는 책을 뽑았다. 표지에는 멋들어진 필체로 \n'R.O.A -끝에서 시작, 시작에서 끝-'이라고 적혀 있었다."
    lola happy1 "화제의 작가 이리야 케이지가 보내드리는 ROA의 마지막 작품.\n'종말의 땅에서 비로써 시작되는 첫번째 이야기.'라고 적혀 있군요..."
    "나는 책을 챙겼다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_sfcontrol with dissolve
    show lola_haps2 with dissolve
    name "어라? 아리아는?"
    lola happy1 "아리아는 화장실에 들렀다 온데요."
    "나와 로라는 조정간에 가까이 가 보았다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    lola happy1 "모의 SF 항공전 시뮬레이터\n x주의x VR멀미가 있는 분은 하실 수 없습니다."
    name "왜? 해보고 싶어?"
    lola happy1 "살짝요."
    name "2인 1조를 하는 거 같은데...\n한 번 해볼까?"
    lola "네!"
    "로라는 빈 조종간에 앉았다."
    scene bg_black with dissolve
    $ renpy.pause(5.0)
    scene bg_sfcontrol with dissolve
    show lola_haps2 with dissolve
    lola happy1 "아아~ 선배 잘하시네요~"
    name "나도 놀랐어..."
    show aria_happy at left with dissolve
    a "저 왔어요~!"
    name "꽤 걸렸네?"
    if name=="hentai" or name=="etchi" and grade==1:
        a "후훗☆ 여자아이의 매☆지☆컬 타☆임에 대해서 질문하다니\n선배는 참 무례하군요!"
        name "......."
        $ a_yan+=8
        $ a_ko+=10
    "아리아도 돌아왔기 때문에 우리는 멈췄던 관람을 마저 하기 시작했다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    "......."
    "......."
    "......."
    laula "나는 아리아가 싫었다."
    laula "내가 살아왔던 환경과는 정반대의, 양지에서 자란 사람."
    laula "관찰하고, 관찰하고, 또 관찰했다.\n기회를 잡아, 그것을 이용해 아리아를 내 앞에서 치우기 위해서."
    laula "기회는 빨리 찾아왔다. 우리가 입학하기도 전, 예비 소집일 날 부터 나는 아리아를 몰아넣는데 성공했다."
    laula "그런데... [name]선배. 그 사람이 모든 걸 바꾸었다."
    laula "나는 내 앞에서 아리아를 치워버리고 싶었다."
    laula "다시 기회를 노렸다. 최대한 아리아와 친해지고, [name]선배와\n도 친해지기 위해 노력했다."
    laula "기회를 잡았다. 찬스. 그럼에도 머뭇거렸다. 왜지? 그 사이에\n아리아를 '친구'라는 것으로 생각하게 된 건가?"
    laula "아니다. 아닐 것이다. 난 아리아를 치울 생각을 가지고 있을 뿐이니까. '친구'란 것을 알 리 없으니까."
    laula "......."
    laula "사실은 잘 모르겠다."
    laula "'따뜻함'. [name] 선배와 아리아와 가까워지고 나서 느낀 감정."
    laula "내가 알 리 없는 감정들을 느꼈다."
    laula "......."
    scene bg_room2 with dissolve
    show lola_haps2
    show aria_happy at left
    laula "나는 머리를 거칠게 문질렀다."
    lola happy1 "아~ 진짜 모르겠네-!"
    a "응? 뭐가?"
    laula "나도 모르게 혼잣말이 샌 것 같다."
    lola happy1 "아냐, 아무것도 아냐."
    laula "아리아는 다시 책을 읽기 시작했다."
    lola happy1 "아리아."
    a "왜?"
    lola happy1 "너한텐 분명 언니가 있었지?"
    a "응. 애니 선생님이 내 언니야. 왜?"
    lola happy1 "아니, 그냥."
    laula "'사이 좋아 보여서'란 뒷말을 마음 속으로 삼켰다."
    "'{rt}원{/rt}언{rt}수{/rt}니'와 나의 사이는 최악이다. 아니, 내가\n이렇게 된 이유의 1/3 정도는 언니이다."
    laula "나는 아리아와의 대화를 끝내고 밖으로 나왔다."
    play sound "door.mp3"
    scene bg_living with dissolve
    "로라가 방에서 걸어나왔다."
    show lola_haps2 with dissolve
    lola happy1 "선배, 옆에 앉아도 돼요?"
    name "응."
    "로라가 내 옆에 와 앉았다."
    lola happy1 "선배."
    name "응?"
    lola happy1 "선배는 외동이죠?"
    name "외동이지."
    lola happy1 "좋겠네요."
    name "응?"
    lola happy1 "형이나 누나, 동생을 위해서 물건을 양보할 필요도 없고 먹고 싶은 것, 하고 싶은 걸 전부 할 수 있을거 아녜요."
    name "뭐... 꼭 그렇지만은 않지만 비슷하다가 할 수도 있겠네.\n너는 오빠가 있니?"
    lola happy1 "아뇨, 언니가 한 명 있어요. 사이는 별로 안 좋지만요."
    "로라는 벽에 기댔다."
    lola happy1 "흠냐흠냐..."
    "로라는 피곤한 듯 하다."
    hide lola_haps2
    name "좀 자."
    lola "......."
    "대답이 없다."
    "어께가 무거워져 돌아보니 로라가 어께에 기대 잠들어 있었다."
    menu:
        "로라를 안아서 소파에 눕혀준다":
            "나는 로라가 깨지 않게 로라를 살짝 안아서 소파에 눕혔다."
            laula "음냐...음냐..."
            "배게를 가져와 로라의 머리 밑에 두고, 이불을 덮허주었다."
            if l_ko>10:
                laula "선배..."
                name "...?"
                laula "가지...마요..."
                "잠꼬대인가?"
                laula "아, 아, 아! 아파... 아파요... 언니... 잘못했어...\n아! 아!"
                name "......."
                laula "잘... 잘못했어요! 용서해주세요!"
                "로라가 계속 뒤척거린다."
                "나는 로라의 머리를 살짝 쓰다듬었다."
                name "괜찮아. 괜찮아..."
                "로라의 상태가 조금 안정되었다."
                $ lolasleep=1
        "가만히 둔다.":
            "얼마나 피곤하면 앉아서 졸까."
            laula "냠냠냠..."
            "로라는 머리를 계속 움찔거리더니 바닥으로 쓰러졌다."
            play sound "jab.mp3"
            show lola_sups at right with dissolve
            "로라는 번쩍 꺠어났다."
            name "들어가서 자~"
            laula "네..."
            hide lola_sups
    scene bg_kitchen with dissolve
    name "버섯, 청경채, 당근, 피망, 양념되지 않은 돼지고기... 인가. "
    "한꺼번에 넣고 볶아버리기로 했다."
    name "아리아-?"
    show aria_happy at right with dissolve
    a "네?"
    name "요리하는 거 도와줘."
    a "넹~"
    "요리를 끝내고 식탁으로 볶음밥을 식탁에 올렸다."
    name "가서 로라 깨워."
    if lolasleep == 1:
        a "어디 있는데요?"
        name "거실 소파에 누워 자고 있어."
    hide aria_happy
    $ renpy.pause(2.0)
    "졸음을 털어내며 로라가 부엌으로 걸어왔다."
    show lola_haps2 with dissolve
    show aria_happy at left
    "로라, 아리아, [name]" "잘 먹겠습니다!"
    scene bg_black with dissolve
    $ renpy.pause(5.0)
    scene bg_classroom with dissolve
    show leah_hap at right
    leah "에에, 그럼 거기서 이 책을 찾은거야?"
    name "응."
    leah "고마워! 이 책은 유난히 비싸서 못 사고 있었거든!"
    name "좋아?"
    leah "당연하지!"
    name "ROA 시리즈가 재미있어?"
    leah "응!"
    name "어떻게 처음으로 그 시리즈를 읽게 됐는데?"
    leah "너도 알겠지만 내가 몸이 좀 많이 안 좋잖아."
    name "응."
    leah "병원 안에는 TV도 병실 밖으로 나가서 봐야 하고 컴퓨터도 없었기 때문에 오빠나 언니가 책들을참 많이 넣어줬었는데 그 중에 이리야 케이지의 책이 있었어."
    name "아아..."
    leah "그 책을 오빠가 넣어줬었는데 그것 때문에 언니랑 오빠랑 싸웠었지."
    name "응? 왜?"
    leah "언니는 내가 SF나 판타지 소설 읽는 거 별로 안 좋아해."
    name "그래?"
    leah "응. 언니 성격에 나한테 언니가 싫어하는 책을 읽히는 걸 허락할 거라고\n생각한 오빠도 웃기지만 말이야. 하긴, 성격이 그러니까 학생회장을\n하고 있는거겠지만."
    name "학생회장?"
    leah "응. 내가 말 안했었나? 우리 학교 학생회장인 페르틴이 우리 언니야."
    name "에에에??"
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    show pertin_nom at left with dissolve
    pertin "잠깐 실례하겠어."
    leah "언니!"
    name "안녕하세요, 회장님."
    "학생회장 페르틴."
    "3월에 있었던 학생회장 선거에서 작년 학생 부회장이었던 미첼 선배를 꺾고 학생회장이 되었고 군소 동아리를 없에거나 비슷한 다른 동아리로 합치자는 총무부의 제안을 거절하고, 학생회 예산을 늘리는 등의 일을 해서"
    "총무회장인 실피아 선배와는 견원지간...인 것으로 알고 있다."
    pertin "네가 [name]이지?"
    name "네."
    pertin "레아, 미안한데 잠깐 나기 있어 줄래?"
    leah "응."
    hide leah_hap
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    name "레아를 만나러 온 것도 아닌 것 같은데, 왜 오신거죠?"
    pertin "너랑 하고싶은 이야기가 있어서 왔어."
    name "저랑요?"
    pertin "그래. 단도직입적으로 물을게. 혹시 학생회에 들어올 생각 없어?"
    name "네."
    pertin "왜?"
    name "제가 동아리에 들어가지 않은 이유가 동아리 때문에 시간 뺏기는 것이 싫어서 그랬는데 학생회는 다른 동아리들보다 그런게 더 심할텐데, 들어가고 싶지 않다는 것 하나와..."
    pertin "실피아와 사이가 나빠지고 싶지 않다는 건가?"
    name "......."
    menu:
        "...네":
            name "네."
            pertin "실피아와 내가 사이가 나쁜 이유를 알고 있는거야?"
            name "분명 실피아 선배가 돈을 낭비한다고 생각되는 동아리들을 정리하자고 했을 때 반대했고 예산을 추가로 타냈기 때문이라고 알고 있어요."
            pertin "틀렸다곤 못하겠네. 하지만 정답은 아니야. 실피아는 내가 회장이 될 때 무언가 수를 썼다고 생각하고 있어.\n내가 이사장의 손녀인 것도 있을 것이고, 나도 놀랐지만 미첼과 경합에서 내가 이긴 것도 있겠지."
            name "......."
            pertin "난 네가 실피아를 어떻게 생각하고 있는지 제대로 몰라. 하지만 한 가지 네가 알아 두어야 할 것이 있어.\n실피아는 절대로 좋은 사람이 아니야. 오히려 어릴적부터 주입받았을 도덕적 관점에서 보면 나쁜 사람에 해당하지."
            "실피아 선배가 지겹도록 주입받은 도덕적 관점에선 '나쁜 사람'이라고?\n무슨 소리지?"
            menu:
                "아무 말도 하지 않는다.":
                    name "......."
                    $ p_ko+=5
                "'사람은 함께있는 사람에 따라 변한다.'고 반박해본다.":
                    name "그래서 어쨌다는거죠? 회장님과 있을 때의 실피아 선배와\n저와 있을 때의 실피아 선배가 다를 수도 있는 것 아닌가요?"
                    pertin "그냥 알고 있으란거야."
                    $ p_shin+=6
            pertin "그리고 아까전에 말했던 이야기, 시간을 뺏기는 게 싫다고 했지? 그건 내가 해결해 줄 수 있어."
            name "어떻게요?"
            pertin "원래 학생회는 수업시간을 제외하곤 학생회실에 모여 있어야 하지만 넌 그럴 필요 없어. 그냥 매주 금요일 토요일 오후 9시에 잠들기 전에 하는 학생 회의에만 나오면 돼."
            name "그래도 거절하겠습니다."
            pertin "정말? 뭐, 좋아. 시간을 좀 줄테니까 천천히 생각해 보렴."
            hide pertin_nom
            play sound "sliding.mp3"
            $ renpy.pause(2.0)
        "...그건 아니에요.":
            pertin "그럼 뭔데?"
            name "...아리아 때문이에요."
            pertin "아리아?"
            name "네."
            pertin "아리아라면... 올해 초 소동의 주인공 아니야?"
            name "맞아요. 그 녀석이랑 좀 복잡한 사정으로 얽혔는데 자세한 이야기는 생략하고 결론말 말할게요.\n그 녀석은 제가 곁에 없으면 또 그럴걸요."
            pertin "...네가 그 소동을 진정시킨 사람이란 건 나도 알고 있어. 그리고 그건 분명 훌륭한 일이었지.\n하지만 말이야, 그게 네 말을 믿어야 할 이유가 되진 못해."
            name "믿지 못하겠으면 믿지 마셔요. 제가 학생회에 갈 수 없는 이유는 아리아 때문이란 것만 알아주시면 되니까요."
            pertin "일단 알았어. 생각이 바뀌면 언제든지 학생회실로 와. 기다리고 있을테니까."
            hide pertin_nom
            play sound "sliding.mp3"
            $ renpy.pause(2.0)
            "......."
            "별로 생각하고 싶지 않은 기억이 떠올라 버렸다."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    show leah_nom at right with dissolve
    leah "무슨 이야기를 그렇게 했어?"
    name "그냥... 좀..."
    "레아는 나와 페르틴 선배가 나눈 이야기가 썩 기분 좋은 건 아니란 것을 깨달은 듯 했다."
    hide leah_nom
    show leah_hap at right
    leah "...그래도 여름방학 때 재미있게 놀다 온 것 같네!"
    "레아가 억지로 대화의 주제를 바꾸었다."
    name "응, 재미는 있었어. 힘들었지만."
    "나는 레아와 주제도 뭣도 없는 두서없는 잡담을 나눴다."
    play sound "bell_nomal.mp3"
    name "아, 수업 시작이네."
    leah "이번 교시 뭐지?"
    name "수학."
    hide leah_hap
    $ renpy.pause(4.0)
    "수업이 끝났다."
    play sound "bell_nomal.mp3"
    $ renpy.pause(3.0)
    "보통이라면 다들 일어서서 동아리를 하러 가겠지만 나와 아리아는 동아리를 신청하지 않았다."
    show leah_nom at right
    leah "아아, 나도 빨리 동아리 신청해야 하는데."
    "레아는 동아리 배정이 끝난 다음에 전학 왔기 때문에 모레 동아리를 다시 뽑을 때까진 동아리가 없다."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    show aria_happy at left with dissolve
    a "선배~?"
    name "간다."
    leah "내일 보자구~"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_hallway with dissolve
    play sound "walk_slow.mp3"
    show aria_happy at left with dissolve
    a "레아 선배랑 상당히 친해졌나 봐요?"
    name "뭐, 어쩌다 보니까 말이지."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    lola nomhap1 "그럼 전 이만 가 볼게요~!"
    "로라가 뛰쳐나왔다."
    leah "[name]-! [name]-! 할 이야기가 있어-!"
    "뒤에서 레아도 뛰어왔다."
    play sound "walk.mp3"
    show lola_nomhap2
    show leah_hap at centor
    with dissolve
    "넷이서 기숙사로 향했다."
    play sound "walk_slow.mp3"
    play sound "people.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    show bg_apartment with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_room with dissolve
    name "후우..."
    "제일 먼저 화장실로 들어갔다."
    scene bg_bathroom with dissolve
    play sound "shower.mp3"
    $ renpy.pause(8.0)
    scene bg_room with dissolve
    "옷을 갈아입고 침대에 앉았다."
    play sound "phonebeep.mp3"
    $ renpy.pause(2.0)
    name "여보세요."
    mitchell "[name]?"
    name "누구신가요?"
    mitchell "[name], 나 미첼인데..."
    name "예, 미첼 선배. 무슨 일이시죠?"
    mitchell "페르틴이 너한테 찾아 갔었다면서."
    name "네."
    mitchell "뭐라고 말했는지 내게 알려줄 수 있어?"
    name "딱히 별 이야기는 없었어요. 그냥 학생회에 들어올 생각은 없는지 물어봤을 뿐이에요."
    mitchell "학생회에? 진짜?"
    name "예."
    mitchell "...응. 알았어. 고마워."
    "전화가 끊겄다.\n전화번호야 학생 등록부를 보면 나오겠지만 대체 무엇 때문에 전화를 한 거지?"
    name "이상하네..."
    leah "뭐가 그렇게 이상한데?"
    "문 밖에서 레아의 목소리가 들렸다."
    name "레아?"
    leah "잠깐 들어가도 될까?"
    name "상관없어."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    show leah_nom at right with dissolve
    name "왜 왔어?"
    leah "언니 기분이 별로 안 좋아 보여서. \n하교하기 전에 언니가 마지막으로 만났던 사람은 너였으니까 네가 뭔가 알고 있지 않을까 했거든.\n아까 전에 언니랑 대체 무슨 이야기를 했던거야?"
    name "학생부에 들어올 생각 없냐고 묻더라."
    leah "학생부에? 정말이야?"
    name "어? 응. 근데 그게 그렇게나 큰 문제야?"
    leah "당연한거 아니야? \n너 학생회에서 하는 일이 뭔지 알아?"
    name "그거야 알지...\n학교 행사를 계획하고, 불량 학생을 지도하고, 교칙을 만들거나 개정하고..."
    leah "거기거기.\n교칙을 만들거나 개정하는 건 어떻게 하지?"
    name "학생회에서 투표를 하... 아..."
    leah "그래.\n우리 언니가 해준 이야기인데, 네가 학기 초에 아리아와 관련된 일은 단번에 해결했다면서?\n그것 때문에 우리 언니는 널 정말 신뢰하고 있어."
    "그런데 학생회는 지 금 12명인데, 언니를 따르는 사람이 6명, 미첼 선배를 따르는게 6명이지."
    name "모든 개정안은 과반수 이상의 찬성이 있어야 하기 때문에 나를 포섭하려고 한다...?"
    leah "그렇지 않을까?"
    name "과대해석 아니야?"
    leah "뭐, 그거야 나도 모르지.\n추측이야 추측.\n정 궁금하면 언니한테 슬쩍 떠볼까?"
    menu:
        "부탁해 볼까?":
            name "부탁할게."
            leah "맡겨만 줘."
            $ leah_ko+=3
            $ leahQ=1
        "아무리 그래도 남 마음을 캐는 건 별로 좋지 않지.":
            $ leahQ=0
            name "괜찮아."
            leah "그래? 그래."
    name "그건 그렇고, 다른 일은 없어?"
    leah "딱히 없어."
    name "그럼 온 김에 차라도 마시고 갈래?"
    hide leah_nom
    show leah_hap at right
    leah "고마워!"
    "레아는 나와 차를 마시며 이야기하기 시작했다."
    $ renpy.pause(2.0)
    "레아가 살짝 휘청거렸다."
    hide leah_hap
    show leah_pain at right
    if leah_ko>=13:
        name "레아?"
        leah "괜찮아... 으... 미안한데 따뜻한 물 한 잔만 부탁해도 될까?"
        name "어? 잠시만..."
        $ renpy.pause(2.0)
        "부엌에서 떠온 따뜻한 물을 레아에게 건네자 레아는 곧바로 주머니에서 꺼낸 흰 알약과 함께 물을 삼켰다."
        $ leah_ko+=5
        $ leah_shin+=10
        leah "콜록콜록!"
        name "왜 그래?"
        leah "발작... 한거야...\n괜찮아... 잠깐만 쉬면..."
        "레아가 상당히 힘들어 보였기에 나는 방에서 배게와 얇은 이불을 하나 가져왔다."
        leah "미...안해..."
        name "괜찮아, 쉬어."
        hide leah_pain
        leah "하아... 하아..."
        "나는 레아의 이마에 손을 얹었다."
        name "열이 펄펄 끓잖아? 잠깐만 있어봐."
        play sound "walk.mp3"
        $ renpy.pause(3.0)
        play sound "door.mp3"
        $ renpy.pause(3.0)
        scene bg_bathroom with dissolve
        play sound "shower.mp3"
        "대야에 물을 받았다."
        $ renpy.pause(4.0)
        scene bg_room with dissolve
        play sound "walk.mp3"
        $ renpy.pause(3.0)
        "수건을 물에 적셔 레아의 이마에 대 준 후, 나는 아리아에게 전화를 걸었다."
        play sound "phonering.mp3"
        $ renpy.pause(6.0)
        a "네, 선배.\n갑자기 왜 전화를 하고 그러셔요?"
        name "아리아. 지금 빨리 뛰어가서 페르틴 선배 불러와.\n빨리!"
        a "예?\n {p}아, 예!"
        "전화를 끊고 레아의 간호를 하기 시작했다."
        leah "하아... 하아..."
        "여전히 온몸이 불타듯이 뜨거웠다."
        "나는 재빨리 옷을 갈아입고 레아를 등에 업었다.\n아리아에게 페르틴 선배를 병원으로 보내 달라고 연락한 뒤, 뛰쳐나갔다."
        scene bg_black with dissolve
        play sound "door.mp3"
        $ renpy.pause(2.0)
        play sound "walk.mp3"
        $ renpy.pause(2.0)
        play sound "car.mp3"
        leah "하아... 흐으..."
        "레아의 몸은 여전히 불덩이 같았다."
        $ renpy.pause(2.0)
        play sound "car.mp3"
        play sound "walk.mp3"
        $ renpy.pause(2.0)
        play sound "sliding.mp3"
        $ renpy.pause(5.0)
        "(1시간 후)."
        scene bg_hospital with wipedown
    else:
        name "괜찮아?"
        leah "응... 괜찮아...\n미안하지만, 가 봐야 할 것 같아..."
        name "응? 어... 응..."
        play sound "door.mp3"
        hide leah_pain
        "레아는 비틀거리면서도 문을 열고 밖으로 나갔다."
        $ renpy.pause(2.0)
        "많이 아파 보였는데... 안 쫒아가 봐도 되려나..."
        play sound "jab.mp3"
        $ renpy.pause(2.0)
        "바닥으로 무언가 떨어지는 소리가 났다."
        play sound "door.mp3"
        scene bg_black with dissolve
        "바닥에는 레아가 쓰러져 있었고, 나는 재빨리 택시를 잡아 병원으로 달려갔다."
        play sound "walk.mp3"
        $ renpy.pause(2.0)
        play sound "car.mp3"
        $ renpy.pause(2.0)
        scene bg_hospital with dissolve
    show leah_nom at right with dissolve
    leah "미안해, 걱정 끼쳐서."
    "레아가 침대에 걸터앉아 말했다."
    name "뭣 떄문에 갑자기 그런 거야?"
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    show pertin_nom at left with dissolve
    pertin "그건 내가 설명할게.\n괜찮지, 레아?"
    leah "[name]이면 상관 없어"
    pertin "레아는 태어날 때부터 머리랑 배에 지병을 가지고 태어났어.\n근데, 이 병이란 녀석이 정말 웃겨서 약으로 치료를 하거나, 수술을 해도 괜찮아졌다가 금방 다시 재발하더라고.\n계속 약을 먹어야 하는데, 깜빡했고, 발작했나 봐."
    leah "언니, 미안..."
    "페르틴 선배는 레아를 살짝살짝 쓰다듬었다."
    pertin "네가 무사하니까 괜찮아."
    "페르틴 선배는 나를 돌아보곤 말했다."
    pertin "네게 또 하나 신세를 졌네."
    hide pertin_nom
    show pertin_hap at left with dissolve
    pertin "고마워."
    "학교에서의 보여주기 위한, 만들어진 미소가 아닌 순수하게 나에게 감사하는 미소였다."
    "레아와 몇 마디를 더 주고받던 페르틴 선배는 나를 병실 밖으로 불러냈다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    scene bg_stairroom with dissolve
    show pertin_nom at right with dissolve
    name "학생회 이야기라면 제대로 거절했다고 생각하고 있었는데, 왜 그러시죠?"
    pertin "지금 부른 건 그것 떄문이 아니야."
    name "그렇다면, 뭐죠?"
    pertin "너도 방금 봤으니까 알겠지만 레아는 몸이 상당히 아파."
    name "확실히 그래 보이더군요."
    pertin "그래서 항상 챙겨 먹어야 하는 약이 여러개가 있어."
    name "네."
    pertin "염치 없다는 건 알고 있지만 레아를 조금 부탁해도 될까?"
    name "예?"
    pertin "내가 레아 옆에 계속 붙어있을 순 없어.\n다른 사람한테 부탁해도 되지만 네가 제일 믿음직스러워서 말이야...\n거절해도 상관없긴 한데..."
    menu:
        "알겠습니다.":
            name "네. 저는 따로 동아리도 없으니까 문제 없어요."
            hide pertin_nom
            show pertin_hap at right
            pertin "고마워♪"
            play sound "walk_slow.mp3"
            $ renpy.pause(2.0)
            hide pertin_hap
            "페르틴 선배는 내게 감사를 표하고 레아의 병실로 들어갔다."
            $ p_ko+=5
            $ p_shin+=10
            $ leah_event = True
            play sound "door.mp3"
            $ renpy.pause(2.0)
        "거절하겠습니다.":
            name "마음만 같아선 알겠다고 하고 싶지만 아리아 때문에..."
            pertin "응?"
            name "아직 그날 있었던 일에서 완전히 벗어나진 못한 거 같아요."
            pertin "왜 그렇게 생각하지?"
            name "학교에서 졸때나 기숙사에서 잘 때 잠꼬대를 들어보면 알 수 있죠."
            pertin "........"
            name "왜 아리아가 저한테 집착한다고 생각하세요?"
            pertin "...알았어."
            name "죄송해요."
            pertin "아니야."
            play sound "walk_slow.mp3"
            $ renpy.pause(2.0)
            "페르틴 선배는 다시 레아의 병실로 들어갔다."
            play sound "door.mp3"
            $ renpy.pause(2.0)
    "슬슬 돌아갈까."
    play sound "walk_slow.mp3"
    scene bg_black with dissolve
    $ renpy.pause(4.0)
    play sound "walk_slow.mp3"
    scene bg_apartment with dissolve
    a "서언~배!"
    "건물 위에서 아리아가 소리친다."
    name "올라가면 얘기해, 올라가면!"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    $ renpy.pause(3.0)
    "아리아가 끝없이 쏟아대는 질문에 전부 대답하고 나자 이미 해는 뉘엿뉘엿 넘어가고 있었다."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_room_night with dissolve
    name "으으..."
    "온몸에서 힘이 쫙 빠졌다.\n밥을 차려먹어야 했지만 그럴 기운+ 없이 침대 위로 쓰러졌다."
    name "음음..."
    scene bg_black with Dissolve(5.0)
    "........"
    $ renpy.pause(4.0)
    name "으으으..."
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    "무슨 소리지?"
    play sound "door.mp3"
    $ renpy.pause(2.0)
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    a "선배, 일어나세요."
    name "........"
    "방금 아리아의 목소리가 들린 것 같은데..."
    scene bg_room
    "갑자기 주변이 환해졌다."
    show aria_happy at right with dissolve
    a "선배! 일어나시라고요!"
    name "아리아...?"
    a "선배, 어서 일어나요! 학교 가야죠!"
    name "으음... 지금 몇시야?"
    a "종 칠 때까지 30분 밖에 안 남았어요! 어서요!"
    "눈이 번쩍 뜨였다.\n탁자에 놓여있던 빵을 집어들고 아리아와 함께 학교로 달렸다."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    scene bg_apartment with dissolve
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    scene bg_school with dissolve
    show anie_ang at right
    show aria_nomal at left
    with dissolve
    play sound "bell_nomal.mp3"
    $ renpy.pause(2.0)
    a_a "너희들!"
    "애니 선생님이 화난 표정으로 우리를 쳐다보고 있었다."
    a_a "너희들은 학생부로 따라와!"
    name "선생님. 아리아는 제가 안 일어나니까 깨워서 같이 오다가 늦은 거에요.\n아리아는 그냥 보내주시면 안될까요?"
    a_a "그랬어?"
    a "네..."
    hide anie_ang
    show anie_nom at right
    a_a "좋아. 아리아가 널 도와준다고 늦었단 말이지?"
    name "네."
    a_a "너희 둘 다 이번 한 번은 봐 줄 테니까, 다음부턴 절대로 늦지 마라."
    "[name], 아리아" "알겠습니다!"
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    $ renpy.pause(2.0)
    scene bg_black with dissolve
    "아리아와 함께 기숙사에서 미친듯이 달려 학교로 도착한 나는 교실로 들어섰다.\n반 친구들은 이번 시간이 체육이기에 전부 강당으로 이동한 후였다.\n교실에 혼자 앉아 책을 보던 레아에게 인사하고, 체육복을 들고 강당으로 뛰었다."
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    scene bg_pe1 with dissolve
    $ renpy.pause(5.0)
    play sound "walk.mp3"
    scene bg_pe1 at moving
    name "헥... 헥..."
    if gender == "남자":
        "1.6Km를 15분 안에 주파해야 하는 '오래달리기'. 마지막 바퀴에서 숨이 턱 밑까지 차올랐다."
        play sound "walk.mp3"
        a_a "[name], 8분 45초!"
    else:
        "1.2Km를 15분 안에 주파해야 하는 '오래달라기'. 마지막 바퀴에서 숨이 턱 밑까지 차올랐다."
        play sound "walk.mp3"
        a_a "[name], 6분 45초!"
    scene bg_pe1 at moving
    name "헤엑... 헤엑..."
    show anie_nom
    a_a "다른 애들 길 막지 말고 저기 단상 앞에 가서 쉬고 있어!"
    name "네..."
    hide anie_nom
    play sound "walk_slow.mp3"
    "지친 채로 터덜터덜 걸어 벽에 살짝 기댔다.{p}반대편에선 2학년이 축구 수행평가를 하는지 공 차는 소리가 들려왔다."
    play sound "crowd.mp3"
    $ renpy.pause(4.0)
    play sound "kick.mp3"
    "학생들" "아아~"
    name "공이 내 머리를 스치고 단상에 격돌했다."
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    show sena_nom at right with dissolve
    "???" "죄송해요. 괜찮으세요?"
    "주황색 머리를 기른 여자아이가 나에게 사과했다."
    name "응. 괜찮아.\n여기 공."
    hide sena_nom
    show sena_hap at right
    "???" "감사합니다!"
    "멀리서 2학년들이 이름을 부른다."
    "세나.{p}한세나라고."
    $ sena_start=True
    play sound "bell_nomal.mp3"
    $ renpy.pause(2.0)
    sena "갈게요."
    hide sena_hap
    "수업이 끝났다."
    play sound "people.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_school with dissolve
    play sound "walk_slow.mp3"
    scene bg_hallway
    show leah_nom at right with dissolve
    leah "왔어?"
    if leah_event == True:
        menu:
            "기다리고 있었던거야?":
                name "설마 계속 기다리고 있었던 거야?"
                hide leah_nom
                show leah_hap at right
                leah "응!"
                name "앉아서 기다리지 그랬어!{p}교실로 들어가자."
                leah "응!"
                $ leah_ko+=3
            "반 안에 있지, 여기서 뭐 해?":
                name "밖에 나와서 뭐하고 있었어?"
                leah "잠깐 바람 쐬고 있었어. 들어가자."
    else:
        menu:
            "반 안에 있지, 여기서 뭐 해?":
                name "밖에 나와서 뭐하고 있었어?"
                leah "잠깐 바람 쐬고 있었어. 들어가자."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    scene bg_classroom
    show leah_nom at right
    with dissolve
    "자리에 앉아 종이 치기를 기다렸다"
    $ renpy.pause(3.0)
    play sound "bell_nomal.mp3"
    name "다음 시간 뭐지?"
    leah "과학일걸?"
    hide leah_hap
    hide leah_nom
    "과학 교과서를 펼치고 책상에 앉아 기다린지 2분 정도 됐을까.\n복도에서 소란스러운 소리와 함께 선생님이 들어왔다."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    show sin at right with dissolve
    sin "자, 얘들아. 조용히.{p}수업 시작한다."
    "학생들" "네~"
    $ renpy.pause(5.0)
    sin "음... 시간이 좀 남긴 했지만 오늘 수업은 여기까지!{p}조용히 자습해!"
    "학생들" "우와~!!!"
    "나는 책갈피를 꽂고 덮어두었던 책을 다시 펼쳤다."
    play sound "book.mp3"
    $ renpy.pause(1.0)
    nvl clear
    nvlnarr "그녀는 말했다.{p}\"그저 원하는 대로 살아가는 삶이라니, 지루하고 재미없잖아요?\"{p}나는 대답했다."
    nvlnarr "\"그 재미없는 일상이야 말로 떫은 인생 속에서 유일하게 축복받은 일이란걸 너도 곧 깨달을 거란다.\""
    nvlnarr "잘 모르겠다고 대답하는 그녀.{p}나는 그 머리를 살짝 쓰다듬어 주고 집 밖으로 내보냈다."
    nvlnarr "그런 그녀의 뒷모습을 보며 생각했다.{p}'저런 인간이야 말로 내가 제일 싫어하는 것'이라고."
    nvlnarr "\"나에게도 그런 시절이 있었지.{p}모험 속에서 진실에 도달할 수 있다 생각했던 나날들이...\""
    nvlnarr "\"네?\""
    nvlnarr "\"아무것도 아니야.\""
    nvlnarr "\"아저씨.\""
    nvlnarr "\"응.\""
    nvlnarr "\"아저씨는 정말 좋은 사람이에요.\""
    nvlnarr "나는 속으로 비웃었다.{p}지금의 내 모습과 가장 떨어져 있는 말을 들었기 때문이었을 것이다."
    nvlnarr "\"그래, 고마워...\""
    nvlnarr "\"그럼 지금은 '안녕'인거에요!\""
    nvlnarr "\"고작 저기 앞까지 나갔다 올 뿐이잖아.{p}안녕은 무슨 안녕.\""
    nvlnarr "\"헤헤. 조금 있다가 봐요~\""
    nvl clear

    play sound "book.mp3"
    $ renpy.pause(1.0)
    "책을 덮었다.{p}역자 후기가 남아 있긴 하지만 딱히 읽고 싶은 기분은 들지 않았다."
    "레아가 이쪽을 흘끗흘끗 곁눈질한다.{p}자신이 추천한 소설을 어떻게 읽었는지 궁금한거겠지."
    "나는 책상에 엎드려 종이 치기를 기다렸다."
    $ renpy.pause(2.0)
    play sound "bell_nomal.mp3"
    "학생들" "안녕히가세요!!!"
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    hide sin
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    "나는 책을 들고 일어섰다."
    $ renpy.pause(2.0)
    show leah_nom at right with dissolve
    leah "어땠어?"
    name "음..."
    name "재밌게 잘 읽었어. 고마워, 레아."
    hide leah_nom
    show leah_hap at right
    leah "그렇지? 내가 말했잖아? 재밌다고!"
    "레아는 의기양양하게 날 쳐다봤다."
    leah "응. 고마워."
    $ leah_shin+=5
    scene bg_black with dissolve
    "레아에게 책을 돌려주고 잠깐 잡담을 하고 나니 종이 쳤다."
    play sound "bell_nomal.mp3"
    $ renpy.pause(2.0)
    "사회 수학 국어 국어 가정."
    "지겨운 수업시간이 지나고 나는 자리에서 일어났다."
    "오늘은 금요일. 수업이 일찍 끝나는 날.{p}보통은 분명 부활동을 위해 부실로 몸을 옮기거나 외출을 통해 학교를 떠날 것이다."
    "뭐, 나는 어느쪽도 아니니 도서관에 잠깐 들렀다가 기숙사로 갈 테지만."
    show bg_hallway with squares
    play sound "phonebeep.mp3"
    name "여보세요?"
    silpia "[name]?"
    name "누군가 했는데, 선배님이였군요.{p}왜 그러세요?"
    silpia "바쁘니?"
    name "딱히 바쁘진 않아요.{p}도서관 갔다가 바로 기숙사로 가려고 했으니까요."
    silpia "괜찮으면 잠깐 총무부실까지 와주겠니? 좀... 이야기 하고 싶은게 생겨서 말이야..."
    "총무부실? 총무부실... 총무부실...이면... 별관 4층... 이었던가?"
    name "금방 갈게요."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    "도서관에 가야 했지만 별로 중요한 일은 아니었기에{p}나는 바로 별관 4층으로 올라갔다."
    $ renpy.pause(2.0)
    scene bg_school with squares
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    "정말 짜증이 날 정도로 좋은 날씨다."
    scene bg_stair with squares
    play sound "walk_slow.mp3"
    "왠지 모르게 마주치는 사람 하나 없이 계단을 올라갔다."
    $ renpy.pause(2.0)
    show bg_hallway with squares
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    scene bg_club with blinds
    show silpia_angry at right with dissolve
    name "선배님?"
    silpia "빨리 빨리!{p}좀 더 빨리 못해!"
    "실피아 선배가 총무부원들을 닥달하고 있다."
    name "어... 선배?"
    hide silpia_angry
    show silpia_suprise at right
    hide silpia_suprise
    show silpia_happy at right
    silpia "어... 왔니?"
    "선배는 잠깐 놀란 표정을 짓더니 재빨리 얼굴에 웃음을 띄웠다."
    name "뭐하고 계셨어요?"
    silpia "일."
    "나는 실피아 선배가 앉아있던 자리를 살펴보았다.{p}무엇인가 적혀 있는 종이들이 한가득 올려져 있다."
    name "이게 전부 다 서류인가요?"
    silpia "응.{p}게다가 전부 오늘 안으로 처리해야 하지.{p}내가 널 부른 것도 이것 때문이야."
    name "에에... 뭔데요?"
    silpia "괜찮다면 이걸 학생회의 페르틴한테 전해줄래?"
    "선배가 가리킨 종이뭉치의 제목은 '축제 건의안과 그에 따른 예산 편성(1차)'였다."
    name "축제까지 한 달하고 조금 남았는데 벌써 준비하는 건가요?"
    silpia "응. 원래 이맘때부터 총무부랑 학생회가 갑자기 바빠지기 시작해."
    "우리 학교는 추석 당일날 저녁에 학교로 돌아와 그 다음날 축제를 시작하여 3일간 진행한다.{p}그렇기에 8월 말에서 9월 초순부터 준비를 시작할거라 생각했는데..."
    name "되게 빨리 시작하네요."
    silpia "제사라던가 준비할게 많으니까."
    name "아, 분명 축제 첫번째 날 밤에 모두 함께 제사를 지냈었죠."
    silpia "응."
    name "가져다 주기만 하면 되는거죠?"
    silpia "그것도 응."
    "나는 서류 뭉치를 들고 선배에게 인사를 했다."
    name "안녕히 계세요."
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    scene bg_hallway with squares
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_black with wipeleft
    $ renpy.pause(2.0)
    scene bg_club
    show pertin_nom
    with wiperight
    name "이걸 전해달래요."
    pertin "뭐야? 서류?"
    name "네. 총무부에서 가져온거에요."
    pertin "실피아가 날 보기 싫으니까 널 시켰군.{p}어디보자..."
    name "........"
    play sound "book.mp3"
    "페르틴 선배는 서류 뭉치를 휙휙 넘기며 대충 훑었다."
    pertin "흐으음...{p}별 문제는 없어 보이는데..."
    name "저는 이만 실례하겠습니다."
    pertin "아, 잠깐만."
    "선배는 주머니를 뒤적거리더니 무언가 던졌다."
    pertin "그거 줄게."
    if 'choco' not in str(persistent.inven):
        $ inventory.add(choco)
        $ persistent.inven=['choco']
    "낚아 채 손을 펴 보니 작은 판 초콜릿이 있었다."
    name "감사합니다."
    play sound "sliding.mp3"
    scene bg_hallway with squares
    name "흠."
    "나는 다시 교실로 향했다.\n청소는 이미 끝나 있었다."
    play sound "bell_nomal.mp3"
    $ renpy.pause(2.0)
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    play sound "sliding.mp3"
    $ renpy.pause(2.0)
    scene bg_classroom with blinds
    play sound "people.mp3"
    $ renpy.pause(2.0)
    anie happy1 "얘들아~! 자리에 앉으렴!"
    show anie_happy2
    anie happy1 "종례할테니까 앉아!"
    "아이들이 모두 앉자 선생님은 교무수첩에 적어온 것을 읽기 시작했다."
    $ renpy.pause(2.0)
    anie happy1 "...은 방과후 바로 집으로 출발하면 되고, 나머지는 즐거운 주말 보내고{p}월요일에 다시 만나자!"
    "아이들" "네~!"
    hide anie_happy2
    "나는 교실을 나섰다."
    play sound "people.mp3"
    $ renpy.pause(2.0)
    if leah_event == True:
        leah "[name]! 같이 가자!"
        name "그래."
        "나는 문 앞에서 레아를 기다렸다."
        show leah_hap at right with dissolve
        "옆에서 레아가 살짝 기대 왔다.{p}이거 아리아한테 걸리면 죽겠는걸."
        play sound "sliding.mp3"
        leah "[name]~"
        "머리를 문질문질."
        leah "[name]! 헤헤, 얼굴 빨개졌다!"
        name "그럼 안 빨게 지겠냐-!"
        "나도 모르게 소리를 빽 질렀다."
        "주변의 모두가 날 쳐다본다."
        name "우으..."
        play sound "sliding.mp3"
        scene bg_hallway with blinds
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        scene bg_school
        show leah_hap at right
        with blinds
        "나는 손목시계를 확인했다."
        name "어?"
        "레아가 약을 먹을 시간이다."
        name "레아. 약 들고있지?"
        leah "응? 응."
        "나는 가방에서 물병을 꺼냈다."
        "물을 레아에게 건네려는 순간 떠올랐다.{p}물병에 담긴 물이 내가 마시던 물이란걸."
        leah "응? 왜 그래?"
        name "이거... 내가 마시던 거라서..."
        menu:
            "이거라도 괜찮겠어?":
                name "이거라도 괜찮겠어?"
                leah "응!"
                "묘하게 레아의 눈이 반짝이는 것 같은데 기분 탓인가?"
                name "여기."
                "나는 물병을 건넸다."
                $ leah_ko+=3
                $ leah_shin+=5
            "급수대에 있는 컵에 물을 따라올게.":
                name "잠깐만 기다려. 급수대에 갔다올게."
                leah "응..."
                play sound "walk.mp3"
                scene bg_school at moving
                $ renpy.pause(2.0)
                "나는 쇠컵에 물을 가득 담았다."
                play sound "walk.mp3"
                scene bg_school at moving
                $ renpy.pause(2.0)
                show leah_hap at right with dissolve
                $ leah_shin+=3
                name "자."
                "나는 컵을 건넸다."
        leah "웩, 써..."
        scene bg_black with blinds
        "약을 먹은 레아를 기숙사까지 바래다 주고 씻은 후{p}나는 기숙사 침대에 걸터 앉았다."
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
    else:
        scene bg_black with blinds
    scene bg_room with blinds
    name "그러고보니 내일이 토요일이네..."
    "미리 뭘 할지 결정해야 하려나...?{p}뭐, 굳이 지금 할 필요는 없겠지."
    "어잿밤에 만들어 뒀던 만두를 꺼내 전자레인지에 넣고 쪘다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    "발소리가 들린다.{p}누군지 대충 짐작이 간다."
    "노크를 하기도 전에 말했다."
    name "들어와, 아리아."
    a "헤헤. 바로 알아 맞추시네요."
    name "척하면 착이지.{p}잔뜩 만들었으니까 가서 로라랑 레아도 불러와."
    a "알겠습니다!"
    play sound "walk.mp3"
    $ renpy.pause(2.0)
    "아리아가 뛰어가는 소리가 들린다.{p}음... 4명 씩이나 있으면 좁으려나...{p}옆방은 빈방이니까 쓰고 깨끗이 치워놓으면 아무도 모르겠지."
    "미리 이것저것 옮겨 놓도록 할까."
    $ renpy.pause(4.0)
    play sound "door.mp3"
    $ renpy.pause(2.0)
    show leah_hap at right
    show aria_happy at left
    show lola_haps2 at centor
    with blinds
    play sound "people.mp3"
    $ renpy.pause(2.0)
    play sound "knock.mp3"
    $ renpy.pause(2.0)
    if leah_event == True:
        pertin "잠깐 괜찮아?"
        "페르틴 선배의 목소리가 들렸다."
        name "네."
        "나는 아이들에게 먹고 있으라 말하고 밖으로 나왔다."
        play sound "door.mp3"
        $ renpy.pause(2.0)
        play sound "walk_slow.mp3"
        scene bg_apartment with blinds
        show pertin_nom at right
        name "왜 그러시죠?{p}또 학생회 제안이라면 거절하겠습니다."
        pertin "아니야. 그거 아니야.{p}"
        "페르틴 선배는 내게 무언가 내밀었다."
        name "이게 뭐죠?"
        pertin "레아의 언니로써 너와 레아에게 전하는 편지야. 나중에 둘만 있을 때 열어봐."
        name "네."
        if persistent.inven_mail is False:
            $ inventory.add(mail)
            $ persistent.inven.append("mail")
        "선배는 몸을 돌러 돌아 가려고 했다."
        name "오셔서 만두라도 몇 개 드시고 가시죠."
        pertin "괜찮아. 배불러."
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        hide pertin_nom
        "선배는 길을 가로질러 학생회실로 돌아갔다."
        "나도 돌아갈까."
        $ leah_mail=True
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        play sound "door.mp3"
        $ renpy.pause(2.0)
        scene bg_room
        show leah_hap at right
        show aria_happy at left
        show lola_haps2 at centor
        with blinds
        lola happy1 "어, 오셨어요?"
        name "응."
        a "뭣때문에 불려갔다 왔어요?{p}설마... {color=#F41D21}데이트?{/color}"
        leah "설마."
        name "아니야."
        a "에, 진짜요?"
        name "진짜로."
        a "진짜?"
        lola happy1 "진짜래잖아."
        "로라가 이 의미 없는 대화를 종결시켰다."
        name "땡큐, 로라."
        lola happy1 "히힛, 감사합니다."
        "나는 다시 자리에 앉았다."
    play sound "people.mp3"
    if p_ko < 20:
        "소란스러운 시간이다.{p}이런저런 이야기들.{p}1시간 가량 떠들고 나니 문득 실피아 선배 생각이 났다."
        name "잠깐 나갔다 올게."
        a "에에~ 또 어디 가게요?"
        name "잠깐 실피아 선배한테도 나눠 주게."
        "만두는 아직도 남아 있다."
        a "아, 그럼 저도 같이 갈래요."
        name "그럴래?"
        "나는 접시에 만두를 몇개 담고 랩으로 싸서 들었다."
        name "가자."
        play sound "door.mp3"
        $ renpy.pause(2.0)
        play sound "walk.mp3"
        scene bg_apartment
        show aria_happy
        with squares
        $ renpy.pause(2.0)
        name "아리아."
        a "네?"
        name "아니, 그냥... 요즘엔 친구들도 꽤 있는 것처럼 보여서."
        a "다 선배 덕분인걸요~"
        "아리아는 웃으며 나에게 메달렸다."
        menu:
            "무겁다. 떨어져.":
                name "무겁다. 떨어져."
                a "쳇."
            "(가만히 있기)":
                a "[name] 선배~"
                name "........"
                play sound "walk_slow.mp3"
                $ renpy.pause(2.0)
                $ a_ko+=3
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        scene bg_school with squares
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        scene bg_stair
        show aria_happy at left
        with squares
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        a "멀어요..."
        name "확실히 좀 멀기는 하네."
        play sound "walk_slow.mp3"
        "누군가 계단에서 내려오고 있다."
        $ renpy.pause(2.0)
        show tedian_nom at right
        tedian "어, 선배?"
        "총무부의 일원이자 매번 실피아 선배에게 닦이는 총알받이 테디안이 서 있다."
        name "오랜...만은 아닌가."
        "쓴웃음을 짓는 테디안"
        tedian "실피아 선배 만나러 온 거죠?"
        name "응."
        tedian "선배라면 부실에 있을거에요. 또 다른 사람들 신나게 들볶고 있겠죠."
        name "그래, 고마워."
        tedian "그럼 저는 이만~"
        hide tedian_nom
        play sound "walk_slow.mp3"
        $ renpy.pause(2.0)
        name "우리도 마저 올라가자."
        a "네~"
        play sound "walk_slow.mp3"
        scene bg_club
        show silpia_happy at right
        show aria_happy at left
        with blinds
        "우리는 부실 안에 들어가 선배에게 싸온 만두를 건넸다."
        silpia "이걸 가져다 주려고 여기까지 온거야?"
        name "네."
        silpia "고마워! 고마워!"
        name "선배... 아파요..."
        hide aria_happy
        show aria_angry at left
        a "저렇게나... 힘껏..."
        "아리아가 실피아 선배에게는 들리지 않을 정도로 살살 중얼거렸다."
        silpia "아리아. 뭐 불편한 거라도 있니?"
        hide aria_angry
        show aria_suprise at left
        $ renpy.pause(1.0)
        hide aria_suprise
        show aria_happy at left
        a "아, 아니에요."
        silpia "어디보자... 답례 할 만 한게..."
        name "에이, 필요 없어요"
        silpia "잠깐 가만히 있어봐.{p}아! 그래, 그개 있었지."
        "선배는 자신의 주머니에서 초콜릿 묻힌 사탕을 2개 꺼냈다."
        silpia "이거라도 줄게."
        "[name], 아리아" "감사합니다."
        "우리들은 선배에게 인사하고 기숙사로 되돌아왔다."
        scene bg_black with blinds
        $ renpy.pause(2.0)
        scene bg_room
        show lola_haps2 at centor
        show leah_hap at right
        show aria_happy at left
        with blinds
    $ renpy.pause(2.0)
    "어느덧 시간이 흘러 해가 넘어가려 하고 있었고, 만두 역시 동이 났다."
    a "이야이야, 오늘 정말 재밌었어요"
    lola happy1 "네, 정말 재밌었네요"
    leah "재밌었어!"
    "각자 짐을 챙겨 나갈 준비를 한다."
    play sound "door.mp3"
    $ renpy.pause(2.0)
    hide aria_happy
    hide lola_haps2

    if leah_mail==True:
        "나는 나가려고 하는 레아를 멈춰 세웠다."
        leah "응? 왜?"
        name "잠깐... 보여줄게 있어서."
        "페르틴 선배가 준 편지.{p}그것을 열었다."
        window show
        nvlnarr "레아, [name].{p}내가 편지를 써서 좀 놀랐지? 사실 별건 아니고 좀 해 놓고 싶은게 있어서 말이야.{p}레아, 너도 알고 있겠지만 너는 뭐든지 쉽게 까먹어. 그치?"
        nvlnarr "그래서 약 관리를 [name]에게 부탁한거야.{p}대충은 레아한테 설명을 들었겠지만 혹시 모르니까 다시 말할게."
        nvlnarr "아셉타토민(빨강/하양) -> 밥 먹고 30분 이내{p}로열펜탈(파랑) -> 매일 아침에 일어나서 아침을 먹자마자{p}요오드화드로벤타임(검정) -> 저녁 잠들기 전."
        nvlnarr "하루라도 거르면 저번같은 일이 생길 수 있으니까 잘 좀 챙겨주길 부탁할게.{p}-학생회장 페르틴-"
        window hide
        leah "뭐, 별건 없네."
        name "그러게. 이건 내가 들고 있을게."
        $ temp=True
    hide leah_haps
    "모두를 돌려보내고 뒷정리를 한 뒤 침대에 누웠다."
    name "거 참. 시끌벅적한 하루였네.{p}내일은... 토요일이었던가.{p}뭐 하지..."
    "내일 할 일은 내일.{p}나의 지론이다.{p}내일 고민하면 되겠지."
    scene bg_black with Dissolve(4.0)
    "눈을 깜박했을 뿐인데 발소리가 들린다."
    "보나마나 아리아려나."
    play sound "knock.mp3"
    a "선배~"
    $ renpy.pause(2.0)
    scene bg_room with Dissolve(.5)
    name "그래..."
    play sound 'walk_slow.mp3'
    $ renpy.pause(2.0)
    scene bg_bathroom with dissolve
    if l_ko>20:
        name "가만.{p}근데 아리아가 내 방문만 두드리고 갈 애가 아닌데?"
        menu:
            "쫒아가 보기":
                play sound "walk.mp3"
                scene bg_room with dissolve
                $ renpy.pause(2.0)
                play sound "door.mp3"
                scene bg_stairroom with dissolve
                show lola_shy at centor with dissolve
                $ renpy.pause(.8)
                hide lola_shy
                play sound "walk.mp3"
                name "로라?"
                "사라졌다."
                name "뭐... 상관없나."
                $ l_ko+=5
            "무시하기.":
                "신경 써 봤자 바뀔 일은 없을 것이다."
                $ l_dark+=4

    scene bg_black with wipeleft
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    scene bg_classroom with dissolve
    play sound "bell_nomal.mp3"
    name "토요일인가..."
    "TIP: 검은색 사각형을 원하는 장소의 아이콘에 끌어다 놓아 주세요."
    call screen sche 
    $ act = city
    call abcdefg from _call_abcdefg
    if eventcount:
        call screen sche2 
        $ act=city
        "[act]"
        call abcdefg from _call_abcdefg_1
    play sound "bell_nomal.mp3"
    play sound "walk_slow.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(2.0)
    stop sound
    "별로 한 것도 없었는데 점심 종이 울렸다."
    show aria_happy with dissolve
    a "밥먹으러 가요, 선배."
    name "뭐야, 너 내가 여기 있다는 거 어떻게 알았어."
    a "에... 사랑의 힘이랄까요?"
    "헛웃음이 나왔다."
    name "그래... 금강산도 식후경이라고 밥이나 먹으러 가자."
    leah "[name]-! [name]-!"
    lola happy1 "[name] 선배!"
    show leah_nom at left
    show lola_haps2
    with dissolve
    "언제나 모이던 멤버들이 모였다."
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    stop sound
    scene bg_middle with dissolve
    name "날씨 참 좋네"
    lola happy1 "그러게요"
    leah "국수 먹고 싶다..."
    name "오늘 급식 뭐지?"
    a "메밀국수 아니에요?"
    play sound "walk_slow.mp3"
    scene bg_black with dissolve
    $ renpy.pause(5.0)
    "...{w=1.0}...{w=1.0}...{w=1.0}..."
    name "잘 먹었습니다."
    "오늘은 아리아가 조용히 있어 줄 것이다.{p=1.0}애시당초 '약속'이 그랬었으니까."
    if leah_event:
        name "레아, 약 잊어버리지 말고 꼭 챙겨먹어."
        leah "응! 걱정하지 마!"
    scene bg_black with dissolve
    play sound "walk_slow.mp3"
    $ renpy.pause(2.0)
    stop sound
    "별 것 아닌 토요일의 오후."
    "시간은 느긋하게 흘러가 학교 한 가운데 설치된 종이 오후 1시를 가리켰다."
    play sound "oldClock.ogg"
    $ renpy.pause
    scene bg_middle with dissolve
    $ renpy.pause(11.0)
    stop sound
    if KnightClub == True:
        call KnightClub from _call_KnightClub    
    scene bg_black with wipeleft
    "조용한 복도. 남아있는 사람은 없는 듯 했다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    stop sound
    scene bg_room_night with dissolve
    
    play sound "knock.mp3"
    namedic["{0}".format(where)] "[name]?"
    "노크 소리와 함께 누군가 나를 불렀다."
    play sound "door.mp3"
    $renpy.pause(2.0)
    stop sound        
    if namedic["{0}".format(where)] == reina:
        show reina_nom at right with dissolve
        name "레이나? 무슨 일이야?"
        reina "고맙다는 말을 하고 싶어서."
        name "갑자기?"
        reina "U 선배가 아프다는 걸 알고 있었는데도 막지 못한 내 잘못이야."
        name "아... 그 이야기야? 난 멀쩡해. 별로 다치지도 않았고."
        reina "그럼 다행이지만..."
        name "여기까지 왔는데 뭐라도 마실래?"
        "대답을 기다리지 않고 찬장에서 커피를 꺼냈다."
        name "커피 마셔?"
        reina "아니... 그래도 한 번 마셔보고 싶었어."

    elif namedic["{0}".format(where)] == pertin:
        show pertin at right with dissolve
        name "선배? 무슨 일이세요?"
        if leah_event == True:
            pertin "아까 도와줬잖아. 그리고 내 동생 일도 있고."
        else:
            pertin "아까 도와줬잖아. 답례는 했지만 조금 부족한 거 같아서."
        pertin "잠깐 들어가도 될까?"
        name "예... 들어오세요."

    return
