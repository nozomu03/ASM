init python:
    tempact=None
    where=None
    event("redcross", "act=='보건실'")
    event("music", "act=='음악실'")
    event("money", "act=='총무부'") 
    event("shorttrip", "act=='신발장'")
    event("restPlace", "act=='쉼터'")
    event('KnightClub', "act=='검도부'")
    KnightClub = False
    eventM = False

label restPlace:
    scene bg_black with wiperight
    play sound "walk_slow.mp3"
    $eventM = True
    $renpy.pause(2.0)
    scene bg_game with wipeleft
    play sound "people.mp3"
    "많은 사람들이 모여있다."
    show mitchell_nomal at right with dissolve
    "저건... 미첼 선배인가?"
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    "미첼 선배는 핸들을 꺾었다."
    play sound "people.mp3"
    $renpy.pause(2.0)
    mitchell "......."
    "학생 1" "......."
    mitchell "음."
    "학생 1" "...졌습니다."
    "남자가 일어났다."
    play sound "hand.wav"
    "박수."
    $renpy.pause(3.0)
    "학생회장 배 게임 대회.{p=1.0} 그러고 보니 그런 것도 있었다."
    "인파 사이로 끼어들었다.{p=1.0}다른 학생이 의자에 앉는 것이 보였다."
    "학생 2" "잘 부탁드리겠습니다."
    play sound "exhaust.wav"
    "자동차의 배기음."
    $renpy.pause(5.0)
    stop sound
    $renpy.pause(3.0)
    "경기 시작부터 5분 정도 지났을까."
    "자동차가 도중에 멈추어 섰다."
    "학생 2" "제가 진 것 같네요."
    play sound "hand.wav"
    $renpy.pause(3.0)
    "도전하는 모든 플레이어들을 차례차례 꺾었다.{p=1.0}가볍게 한숨을 내쉬는 선배."
    "학생 3" "우와... 18전 18승이라고? 말도 안 돼..."
    "학생 4" "그럼 올해 전부 합쳐서 32전 전승이잖아!"
    "미첼 선배는 가볍게 한숨을 내쉬곤 내려왔다."
    mitchell "오, [name]. 안녕?"
    $where="mitchell"
    name "안녕하세요, 선배."
    show uranum_ang at left with dissolve
    "살의가 느껴졌다."
    mitchell "잠깐 시간 괜찮아?"
    name "네...{w=1.0} 상관 없어요."
    mitchell "그러면 잠깐 이야기 좀 하자."
    name "알겠습니다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_middle
    show mitchell_nomal
    with dissolve
    mitchell "요즘 별일 없었어?"
    name "네... 뭐...{w=1.0} 하루하루가 즐거웠죠."
    if p_shin >= 10:
        mitchell "뱀 한 마리가 귀찮게 굴지는 않아?"
        "뱀...?"
        show ch_snake with dissolve
        "이거요?"
        name "글쎄요..."
        mitchell "구렁이 한 마리랑 방울뱀 한 마리가 들러붙다니 참 고생이 많네."
        "나는 페르틴 선배에 대해서 말하고 있다는 것을 그재서야 깨달았다."
        name "하하..."
        "당장이라도 등 뒤에서 페르틴 선배가 무섭게 웃으며 튀어나올 것 같았다."
        mitchell "힘들면 말해. 이제 학생회장은 아니지만 도와줄게."
        name "네..."
        "선배는 내 등을 두드려 줬다."
        hide ch_snake
        menu:
            "선배님은 학생회에 들어간 것을 후회하지 않으시나요?":
                name "선배님은 학생회에 들어간 것을 후회하지 않으시나요?"
                mitchell "응? 뭐라고?"
                name "후회하지 않으시냐고요. 매일 힘들어 보이신데..."
                hide mitchell_nomal
                show mitchell_happy
                mitchell "그러니까 서 있지."
                name "네?"
                mitchell "어느쪽이 되었든 간에 학생회 같이 학생 자치에 중심이 되는 곳에 파벌이 하나만 있으면 안 돼.{p=1.0}그쪽에서 학생들 의견을 싹 무시하고 자기 멋대로 교칙을 바꾸거나 행사 계획을 수정할 지도 모르니까."
                name "......."
                mitchell "학생들 한 명 한 명이 나서서 선생님들이랑 1:1로 의견을 교환하고 그걸 반영하면 좋겠지만 그건 불가능하잖아?{p=1.0}그러니까 페르틴과 나처럼 자기가 힘들 걸 알고서 학생들의 의견이 선생님들께 잘 전달되도록 돕는 사람이 있어야 하는거지 않겠어?"
                "나는 답할 수 없었다.{p=1.0}초등학교 시절부터 배웠던 사회 교과서에는 이런 대목이 있었다."
                " '민주주의의 종류에는 직접 민주주의와 간접 민주주의가 있다. 모든 사람들이 직접 나라 혹은 자신의 속한 사회의 일을 해결하면 좋겠으나 사람의 수가 많기에 최종적으로 직접 민주주의는 국회의원과 같은 특정 사람들에게 권리를 양도하여"
                "민주주의를 집행하는 간접 민주주의의 형태를 띄게 된다.'"
                $m_ko+=5
                $m_shin+=10
            "선배님은 왜 페르틴 선배랑 사이가 안 좋으신지 물어봐도 될까요?":
                name "선배님이랑 페르틴 선배님이 사이가 안 좋은 이유를 물어봐도 될까요?"
                mitchell "사이가 안 좋은 이유? {w=1.0}음..."
                name "아, 대답하기 불편하시면 그냥 무시하셔도 괜찮아요..."
                mitchell "아니, 별로 상관 없어. 사이가 안 좋은 이유라... {w=1.0}그래, 이런 예를 한 번 들어볼까.{p=1.0}너는 아리아가 싫니?"
                name "아리아가요...{w=1.0}?"
                mitchell "응."
                "나는 곰곰히 생각해 보았다.{p=1.0}내가 아리아와 함께 다니는 이유는 책임감 뿐일까?{w=1.0} 조용히 묻고 지나갈 수도 있었을 일을 뒤엎었기에 그로인해 아리아가 피해를 입지 않도록?"
                "고개를 저었다.{p=1.0}그것은 하나의 이유일 뿐이다.{p=1.0}가장 큰 지분을 차지하고 있는 이유는 단순하다. {w=1.0}'그것이 즐거우니까'."
                name "아니요. 저는 아리아랑 같이 있으면 즐거워요."
                mitchell "그렇게 같이 붙어다니면 언제나 재미있니?"
                name "네?"
                mitchell "힘들다거나, 귀찮다거나."
                name "그런게... 없지는 않아요."
                mitchell "그런 것이랑 비슷하지 않을까 싶은데."
                name "무슨 의미인가요?"
                mitchell "나는 학생회에 소속되어서 다른 학생들의 의견을 수렴해서 학교를 바꿔 나가는게 즐거워.{p=1.0}그러니까 페르틴과 충돌하고 알력이 생기는 것 정도는 참을 수 있어야 하지 않을까?"
                name "음..."
                hide mitchell_nomal
                show mitchell_happy
                mitchell "언제나 즐거운 것만 할 수는 없는 거 아니겠어?"
                name "네..."
                $m_ko+=10
                $m_shin+=10
    return


label money:
    play sound "walk_slow.mp3"
    scene bg_black with wiperight
    $renpy.pause(1.0)
    scene bg_club
    show silpia_nomal at right
    with wipeleft
    silpia "어머, [name]. 무슨 일이니?"
    name "분명 바쁠테니 도울 일 없을까 해서 왔어요."
    hide silpia_nomal
    show silpia_happy at right
    silpia "고마워! 마침 일손이 부족했는데!"
    name "그럴 줄 알았어요. 뭘 하면 되나요?"
    silpia "어... 그럼 이것들 좀 교무실에 가져다 놓을래?{p=1.0}교무실 입구에 있는 책상 위에 올려놓기만 하면 돼."
    name "알겠습니다! 쌩하고 다녀올게요!"
    silpia "조심해! 양 꽤 많으니까."
    "나는 서류더미를 안아 들었다."
    play sound "walk.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    show tedian_nom with dissolve
    $renpy.pause(1.5)
    tedian "어, [name] 선배?"
    name "테디안?"
    tedian "심부름 중이신가 봐요?"
    name "응."
    tedian "요즈음에는 학생회도 총무부도 봉사회도 전부 바쁘니까요...{p=1.0}아, 그러고보니까 선배님은 축제 준비 안하시나요?"
    name "나 동아리 가입 안했어."
    tedian "예? 아무것도요?"
    name "응.{w=1.0}뭐, 그 대신 이렇게 학생회랑 총무부 일을 돕고 있지만."
    "'아리아'의 이야기는 꺼내지 않았다."
    scene bg_teachers
    show anie_nom at right
    with dissolve
    anie "괜찮겠어?"
    name "네."
    anie "음..."
    play sound "sliding.mp3"
    show aria_nomal with dissolve
    $renpy.pause(1.5)
    anie "조금은 진정됐니?"
    a "네..."
    anie "자, 마셔."
    "선생님은 아리아에게 무언가 건넸다."
    anie "카모마일. {w=1.0}마음을 진정시켜주지."
    "울먹이면서도 차를 마시는 아리아."
    name "선생님만 허락해 주시면 되요."
    anie "나야 상관없지만...{w=1.0}음...{p=1.0}알겠어. {w=1.0}후회해도 무를 수 없으니까 다시 한 번 생각해 봐."
    play sound "book.mp3"
    "선생님은 서류를 한 장 내게 내밀었다."
    $renpy.pause(2.0)
    "망설임은 없다."
    play sound "pen.mp3"
    $renpy.pause(2.0)
    scene bg_hallway with dissolve
    play sound "knock.mp3"
    name "잠깐 들어가겠습니다."
    $renpy.pause(2.0)
    play sound "sliding.mp3"
    scene bg_teacher with dissolve
    $renpy.pause(1.5)
    "아무도 안 계신다. {w=1.0}출입문 바로 앞의 책상에 서류를 올렸다."
    play sound "walk_slow.mp3"
    anie "뭐야, 내가 문을 안 닫고 갔던가?"
    $renpy.pause(1.5)
    play sound "sliding.mp3"
    show anie_nom at right with dissolve
    $renpy.pause(1.5)
    name "안녕하세요."
    anie "응. 안녕 [name]. 왠일이니?"
    name "저거 가져다 놓으러 왔어요."
    anie "벌써 시간이 그렇게 됐나..."
    name "안녕히 계세요."
    anie "잘 가."
    play sound "sliding.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(1.5)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_middle with dissolve
    "날씨가 좋다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    scene bg_stair with dissolve
    $renpy.pause(1.5)
    play sound "walk_slow.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(1.5)
    play sound "sliding.mp3"
    scene bg_club
    show silpia_nomal
    with dissolve
    $renpy.pause(1.5)
    play sound "sliding.mp3"
    name "다녀왔습니다."
    silpia "아, 어서와!{w=1.0} 별 일 없었지?"
    name "네. 아무 일 없었어요."
    "나는 주변을 둘러보았다."
    play sound "typing.mp3"
    "끊임없는 소리."
    $renpy.pause(2.0)
    stop sound
    show tedian_nom at left with dissolve
    tedian "실피아 선배? 시키신 거 다 했어요."
    silpia "음. 보여줄래?"
    play sound "book.mp3"
    $renpy.pause(2.0)
    hide silpia_nomal
    show silpia_happy
    silpia "서류 정리하는 솜씨가 처음 들어왔을 때보다 확실히 나아졌네."
    "테디안은 눈으로 '선배님이 제가 잘못할 때마다 잡아먹을 듯 으르렁거리는데 솜씨가 안 좋아지겠어요 그럼?'이라고 말했다."
    silpia "테디안?"
    tedian "네?"
    silpia "[name]이랑 같이 이걸 가지고 강당에 좀 다녀올래? 아마 밴드부 부장 선배가 거기 계실 것 같거든."
    "tedian, [name]" "알겠습니다."
    silpia "아, 거기 부장 선배님 엄청 무서우니까 조심하고."
    "우리들은 자리에서 일어났다."
    play sound "sliding.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(1.5)
    scene bg_black with wiperight
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    scene walkingPE
    show tedian_nom at left
    with dissolve
    $renpy.pause(1.5)
    "넓은 강당."
    "아무도 없는건가?"
    "{color=#8904B1}???{/color}" "아아..."
    tedian "방금 선배도 소리 들었죠?"
    name "응..."
    mumul "거기 누구 있어?"
    "힘에 부쳐 헐떡이는 목소리."
    tedian "단상 위에 누군가 있는데요?"
    scene camera_right
    show tedian_nom at left
    play sound "walk_slow.mp3"
    "우리는 단상 앞까지 이동했다.{p=1.0}스포트라이트의 바로 밑에 누워 있는 일렉 기타와 지쳐 쓰러진 사람이 보인다."
    $renpy.pause(2.0)
    show mumul_nom with dissolve
    mumul "후... 덥다, 그지?"
    "숨을 몰아쉬는 선배."
    tedian "안녕하세요."
    name "안녕하세요."
    mumul "안녕!"
    "선배님은 땀에 흠뻑 젖어있다.{p=1.0}여기서 혼자 기타 연습을 하고 있었던 걸까."
    mumul "미안한데 저기 있는 보냉병 좀 주지 않을래?"
    "건내자 선배는 뚜껑을 거의 뽑듯이 병을 열어 재끼고서 안에 든 물을 마셨다."
    mumul "캬, 시원하다.{p=1.0}아, 미안해. 너무 힘들어서 말이야. 어디보자... {w=1.0}실피아의 부탁을 받고 온 거야?"
    name "네. 어떻게 아셨어요?"
    mumul "서류를 그런 식으로 쓰는 사람은 실피아 밖에 없거든.{p=1.0}다른 총무부원도 비슷하게 하려고 하지만 약간의 차이는 남아있어."
    play sound "book.mp3"
    mumul "그런가... 진짜 코앞이네 이제."
    $renpy.pause(2.0)
    "선배가 서류를 읽고있다."
    tedian "에? 어느 틈에...?"
    "선배는 대답하지 않고서 한 손에 종이를 든 채 비뚤어진 마이크를 바로 했다."
    mumul "아. 아."
    "미성이 울린다."
    hide mumul_nom
    show mumul_sing
    mumul "{font=Mightype Script.otf}{size=30}Love Is Endless... {w=.5}Endless... {w=.5}Endless poem... {p=1.0}I believe in you forever, waiting for you...{/size}{/font}"
    mumul "{font=Mightype Script.otf}{size=30}Because I believe in love...{w=.5} I can wait...{/size}{/font}"
    "마음이 편해지는 노래다."
    hide mumul_sing
    show mumul_nom
    mumul "뭐야, 있었어?"
    tedian "멋진 노래네요. 제목이 무엇인가요?"
    mumul "...End{rt}영{/rt}l{rt}겁{/rt}ess."
    name "처음 들어보는 노래에요."
    mumul "당연하지. 이 노래는... 나만을 위한 노래니까."
    tedian "예?"
    mumul "어머니가 내게 칭얼거릴 때마다 불러주시던 노래야. 어머니 말고는 아무도 모르던 노래지."
    name "...선배님의 어머니께서 만든 노래인건가요?"
    mumul "아마도. 늘 그냥 노래만 불러줬었거든... 멜로디는 땄지만 반주는 여전히 못 만들고 있어."
    tedian "왜 반주를 만들고 계신 건가요?"
    mumul "내가 실피아랑 페르틴에게 조금 억지를 부렸거든"
    name "부르게 해달라고 한 거군요."
    mumul "응. {size=5}어머니도 올 테니까 그 앞에서 다시 한 번...{/size}"
    "선배는 무엇인가 덧붙였지만 그 말은 작아 내 귀에는 들리지 않았다."
    "우리들은 선배에게 인사를 했다."
    name "가 보겠습니다. 안녕히 계세요."
    hide mumul_nom
    show mumul_hap
    mumul "응. 잘가."
    hide mumul_hap
    play sound "walk_slow.mp3"
    "손까지 흔들며 배웅해주는 선배."
    $renpy.pause(2.0)
    scene bg_black with wiperight
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_club
    show silpia_nomal at right
    show tedian_nom at left
    with wipeleft
    silpia "잘 갔다 왔어? {w=.5}혼은 안 났니?"
    tedian "안 났어요."
    silpia "{size=5}그런가... 완전히 미움을 사 버린거려나.{/size}{p=1.0}수고했어! 덕분에 한시름 덜었어."
    $s_ko+=4
    $s_shin+=10
    if gender=="여자":
        "실피아 선배는 나를 쓰다듬어 주었다."
        "따뜻한 손길."
        "아득히 느껴지는 어렴풋한 그리움의 느낌."
        "어디서 느껴봤더라?"
    silpia "도와줘서 고마워. 이제 가도 돼."
    name "안녕하 계세요."
    play sound "sliding.mp3"
    scene bg_hallway with dissolve
    $renpy.pause(1.5)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    $eventcount=True
    $where = "silpia"
    return

label redcross:
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wiperight
    scene bg_hospital
    show reina_nom at right
    with wipeleft
    reina "응?"
    name "오, 레이나!"
    reina "안녕, [name]"
    name "다쳤어?"
    reina "뭐, 조금..."
    name "어쩌다가?"
    reina "검도를 하다 보면 이 정도로 다치는 건 별거 아니야"
    "그러고 보니 레이나는 검도를 했었지..."
    name "그... 검도라는 건 정확히 어떤거야?"
    reina "궁금하면 와 볼래?"
    name "응."
    reina "그러면 나중에 점심 먹고 나서 강당으로 와. 1시 30분부터 연습하니까."
    name "응! 꼭 갈게!"
    $r_ko+=3
    $KnightClub = True
    "레이나는 손에 붕대를 감고는 묶으려 노력했다."
    reina "음..."
    "잘 되지 않는 듯 하다."
    name "이리 줘. 묶어줄게."
    "나는 레이나가 건네 준 붕대의 양끝을 잡고 단단히 묶었다."
    reina "고마워."
    "레이나의 손은 상처들로 가득하다."
    name "얼마나 오래했니?"
    reina "뭐? 검도?"
    name "응."
    reina "음... 초등학교 2학년 초부터 했으니까 8년정도 됐네."
    "그 정도 하면 이런 상처들은 평범한 걸까.{p}분명 발이라던가 다리에도 상당히 많은 상처가 있겠지."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    "레이나는 밖으로 나갔다."
    "굳이 여기에 머물러 있을 필요는 없다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_shose
    show pertin_nom at left
    with dissolve
    "페르틴 선배가 신발장 앞에 서 있다."
    pertin "[name]? 여기서 뭐해?"
    name "아무것도요. 그냥 교실에서 나와서 이리로 왔어요."
    pertin "그렇군."
    name "선배님은 어디 가시는데요?"
    pertin "옆동네에 양초랑, 향 사러 가."
    name "네에..."
    pertin "따라오고 싶으면 신발 갈아신고 신발장 앞에 서 있어.{p=1.0}난 놓고 온 게 있어서 잠깐 다시 갔다 와야 하나까."
    play sound "walk_slow.mp3"
    hide pertin_nom
    $renpy.pause(2.0)
    $eventcount=True
    $where="pertin"
    return

label shorttrip:
    if eventcount:
        scene bg_shose
        show pertin_nom at right
        with dissolve
        if where == "pertin":
            pertin "뭐야, 진짜 왔네?"
            name "왜요? 안 올 줄 알았어요?"
            pertin "응."
            name "엑..."
        else:
            pertin "어, [name]?"
            name "안녕하세요 페르틴 선배."
            pertin "잘됐다! 조금 도와줄래?"
            name "네?"
            pertin "축제 때 쓸 제사 용품이랑 기타 이것저것 사러 가야 하는데 트럭 운전해 주기로 하셨던 선생님이 일이 생겨 버렸거든."
            name "...그런데요?"
            pertin "조금만 도와주라."
            name "뭘 하면 되죠?"
            pertin "나랑 같이 짐 좀 나르자."
            name "어떻게요? 들고?"
            pertin "그렇게까지는 할 필요 없어.{p=.5}큰 수레를 가지고 갈 테니까 그걸 둘이서 끌면 될 뿐이야."
            name "알겠어요."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_school
        show pertin_nom at right
        with dissolve
        "페르틴 선배는 아무말 없이 앞으로 걸어가고 있다."
        $renpy.transition(vpunch)
        show pertin_sup at right
        call temp from _call_temp
        name "힉..."
        hide pertin_sup
        show pertin_nom at right
        pertin "...시끄럽네."
        "테디안이 무엇인가 사고라도 친 것일까.{p=.5}실피아 선배의 노성이 교정을 가득 메웠다."
        pertin "거 참... 혼낼거면 좀 조용히 혼내라니까는..."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_mart
        show pertin_nom at right
        with dissolve
        pertin "뭐 해? 멍하니 서서는."
        name "아뇨, 이 시간대에 나오는 건 처음이라서."
        pertin "{size=5}내 말대로 학생회에 들어왔으면 이 시간에도 마음껏 나갈 수 있었을텐데.{/size}"
        name "네?"
        pertin "아니야, 아무것도."
        play sound "walk_slow.mp3"
        "천천히 걸었다."
        play sound "door.mp3"
        scene bg_black with wiperight
        $renpy.pause(2.0)
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_mart
        show pertin_nom at right
        with wipeleft
        "산 것들을 큰 수레에 실었다."
        pertin "혼자 밀 수 있겠어?"
        "페르틴 선배가 든 종이 가방 안에는 향이나 초 같은 가벼운 것들이 가득가득 쌓여 있었다.{p=1.0}아마 저것도 절대 가볍다고는 말 못하겠지."
        menu:
            "문제 없어요":
                name "괜찮아요."
                pertin "정말?"
                name "그럼요."
                play sound "wagon.wav"
                "밀었다.{p=1.0}기름칠을 하지 않은 채 오랫동안 창고에 박아 놓아서인지 바퀴의 움직임이 상당히 뻑뻑했다."
                $renpy.pause(2.0)
                stop sound
                "돌아가면 곧바로 기름칠을 할까."
                $p_ko+=3
            "헤헤... 좀 힘들긴 한데 괜찮아요!":
                play sound "wagon.wav"
                name "좀 뻑뻑하긴 한데 못 밀 정도는 아니에요."
                $renpy.pause(2.0)
                stop sound
        pertin "조금만 힘내."
        name "네."
        play sound "wagon.wav"
        $renpy.pause(2.0)
        stop sound
        "한여름이 지났을 지 몰라도 바깥은 여전히 뜨거웠다."
        pertin "덥네."
        name "그러게요."
        pertin "학교에 있을 때는 에어컨이 빵빵하게 틀어져 있으니까 몰랐지만{p=1.0}아직 여름이 완전히 지나가지는 않았다는 게 실감되네."
        name "그렇네요."
        pertin "이런 날씨에는 역시 '그거'지."
        "선배님은 짐을 수레 위에 올리더니 내 옆에 서서 수레를 힘껏 밀었다."
        play sound "wagon.wav"
        scene bg_black with wiperight
        $renpy.pause(2.0)
        stop sound
        scene bg_school
        show pertin_nom at right
        with wipeleft
        name "헥...헥..."
        pertin "괜찮아?"
        name "조금... 지치긴 했는데... 괜찮은 거... 같아요..."
        pertin "고생했어~"
        hide pertin_nom
        show pertin_hap at right
        "페르틴 선배는 내 팔을 잡아 끌었다."
        name "선배?"
        pertin "고생했으니까 내가 선물 하나 줄게."
        name "선물요?"
        pertin "응. 선물. {w=1.0}학생회실까지 따라오면 선물하나 줄게."
        "선배님의 표정을 보니 이미 나에게 도움을 청하기 전부터 준비한 듯 하다.{p=1.0}준비한 선물을 받지 않는 것도 예의에 어긋나니 지금은 따라가도록 할까."
        scene bg_black with wiperight
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        play sound "sliding.mp3"
        scene bg_club
        show mumul_nom at right
        show pertin_nom at left
        with wipeleft
        hide mumul_nom
        show mumul_hap at right
        hide pertin_nom
        show pertin_sup at left
        mumul "아, 페르틴. 마침 잘 만났다."
        pertin "에에... 무물 선배님... 여기까지 무슨 일이시죠?"
        "페르틴 선배가 쩔쩔매고 있다.{p=1.0}학생회장이자 이사장의 딸인 선배가."
        mumul "서류 처리. 내 앞에서 바로 좀 해 줄 수 있어?"
        hide pertin_sup
        show pertin_hap at left
        pertin "예, 해드릴게요.{w=1.0} [name]. 정말 미안한데, 잠깐만 밖에 있어줄래?"
        name "네."
        "무엇인가 내가 보면 안 되는 서류인 것 같다."
        play sound "sliding.mp3"
        $renpy.pause(2.0)
        scene bg_hallway with dissolve
        play sound "sliding.mp3"
        $renpy.pause(7.0)
        "얼마나 시간이 흘렀을까."
        play sound "sliding.mp3"
        show mumul_hap at right with dissolve
        mumul "흠흠흥~"
        "아까 전의 선배가 콧노래를 부르며 나왔다."
        play sound "walk_slow.mp3"
        hide mumul_hap
        $renpy.pause(2.0)
        play sound "sliding.mp3"
        scene bg_club
        show pertin_nom
        with dissolve
        $renpy.pause(2.0)
        pertin "미안, 기다리게 했지?"
        "선배는 내 쪽으로 아이스크림 하나와 스푼을 밀어줬다."
        play sound "beep.wav"
        pertin "하(삐-)다즈야. {w=1.0}...라고 말하고 싶지만 그냥 마트에서 사 온거야.{p=1.0}먹어. 녹기 전에."
        $pertin_shin+=10
        $pertin_ko+=5
        "방금 미묘한 소리를 들은 것 같지만 나는 애써 무시하고 뚜껑을 벗겼다."
        "빨간색 체리 아이스크림."
        name "잘 먹었습니다. 안녕히 계세요."
        "나는 자리에서 일어났다."
        pertin "응...? 어. 잘 가."
        play sound "sliding.mp3"
        scene bg_hallway with dissolve
        $renpy.pause(2.0)
    return

label music:
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wiperight
    scene bg_music with wipeleft
    play sound "mixdown.mp3"
    "하모니카 소리."
    stop sound
    $renpy.pause(1.0)
    show crey_nom at centor with dissolve
    $renpy.pause(1.0)
    hide crey_nom
    show crey_sup at centor
    crey "...!"
    name "넌... 누구야?"
    hide crey_sup
    show crey_nom at centor
    crey "크레이."
    name "아, 크레이!{p}네가 크레이구나.{p}레이나한테 들었어."
    crey "레이나 선배를 알아요?"
    name "응. 우리 반이야."
    crey "그래요?"
    name "그럼."
    "나는 크레이의 손을 흘끗 보았다.{p=1.0}잔 상처가 많은 그 손등."
    name "너는 검도부니?"
    crey "예? 네. 어떻게 아셨어요?"
    name "그 손 때문에."
    crey "못생겼죠? 제 손."
    name "그 만큼 연습을 열심히 했다는 거겠지."
    crey "...저...선배. 이름이 무엇인가요?"
    name "[name]."
    crey "그럼 [name] 선배."
    name "왜?"
    crey "오늘 점심 먹고 나서 검도부원들이 번갈아가면서 대련할텐데 오실래요?"
    name "음..."
    "별다른 일정은 없다."
    name "그래. 가지 뭐."
    $eventcount=True
    $where="crey"
    crey "...혹시 하모니카 소리 들으셨어요?"
    name "응? 어. 왜?"
    crey "아뇨... 그냥 조금..."
    "크레이는 하모니카를 만지작거린다."
    crey "저는 먼저 가 볼게요. 안녕히 계세요."
    name "응..."
    "이유가 있어서 찾은 음악실이 아니다. 적당히 시간을 죽이다 가도록 할까."
    $KnightClub = True
    $renpy.pause(5.0)
    return

label KnightClub:
    play sound "walk_slow.mp3"
    $renpy.pause(3.0)
    stop sound
    "???" "수 레이나, 공 크레이! 그럼 양측. 정정당당히, 승부!"
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    stop sound
    scene bg_knight
    show U_nom at centor
    show reina_nom at left
    show tedian_nom at right
    with dissolve
    play sound "sword.ogg"   
    $renpy.pause(3.0)
    stop sound
    reina "많이 날카로워졌는걸."
    tedian "헥... 헥...{w=.5}고맙습니다..."
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound 
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound 
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound 
    "레이나의 목검이 테디안의 어깨뼈를 스쳤다."
    "???" "그만!"
    tedian "아아... 아까워라."
    reina "공격하고 싶으면 공격에만 집중해. 방어하고 싶으면 방어에만 집중해.{p=1.0}어중간한 공격, 어중간한 방어는 상대에게 흐름을 넘겨주는 것 밖에 안 돼."
    tedian "그게 말처럼 쉽지가 않네요..."
    reina "다시 한 번 해보자."
    "자세를 가다듬었다."
    "???" "제2전! 양측 모두 정정당당히, 승부!"
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound 
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound       
    tedian "하아앗!"
    play sound "sword.ogg"
    $renpy.pause(3.0)
    stop sound       
    play sound "hit.ogg"
    $renpy.pause(2.0)
    stop sound       
    reina "큿!"
    "레이나의 종아리에 목도가 격돌했다."
    tedian "선배!"
    reina "으... 따가워... {w=1.0}괜찮아. {p=1.0}이 정도는 뭐..."
    "피가 흐르고 있다."
    tedian "피가 나잖아요..."
    reina "괜찮아...{w=1.0} [name]. 저기 있는 구급상자 좀 가져다 줄래?"
    "건넸다."
    reina "앗따따따따... {w=.5}으... 소독은 이걸로 됐고 밴드 좀 붙여줘."
    play sound "bandding.mp3"
    $renpy.pause(2.0)
    stop sound
    name "괜찮은거 맞아?"
    reina "멀쩡해, 멀쩡해."
    tedian "으아아... 죄송해요..."
    reina "선배."
    "???" "......."
    reina "선...배?"
    "???" "{color=#FFF000}쿠쿠쿠쿠...{/color}"
    tedian "아... 설마..."
    "???" "{color=#FFF000}하하하하하하하하하!!!{/color}"
    show U_ang
    name "...?"
    "???" "힘이 넘쳐 흐르는구나!! 하하하하!!"
    reina "[name], 피해!"
    "???" "{color=#FF0000}{b}늦{w=.5}.{w=.5}었{w=.5}.{w=.5}어{w=.5}."
    play sound "hit.ogg"
    "레이나가 던진 목도에 궤도가 흐트러졌다."
    "???" "방해하겠다는 거야... 레이나?"
    hide reina_nom
    show reina_ang at left
    reina "테디안. 가서 고문 선생님 불러와. 저걸 막을 수 있는 사람은 그 분 외엔 없어."
    play sound "walk.mp3"
    hide tedian_nom
    $renpy.pause(2.0)
    stop sound
    name "대체 무슨 일이 벌어지고 있는 거야?"
    reina "U... 저 3학년 선배는 검도부 '최약'이자 '최강'인 선배야..."
    name "...?"
    "U" "하아아앗!{w=.5} 문답무용!"
    "레이나는 멀리 떨어져 있다.{p=.5}맞으면... 상당히 아프겠지."
    play sound "hit.ogg"
    "목도가 내 옆구리를 아슬아슬하게 비껴나가 바닥에 충돌했다."
    "U" "너는 도망칠 수 없어...!"
    play sound "hit.ogg"
    show zeno_ang at right with dissolve
    "???" "후배 앞에서 안 쪽팔리냐?"
    "U" "히... 히익!"
    tedian "선생님 모셔왔어요!"
    hide reina_ang
    show reina_nom at left
    reina "잘했어!"
    hide U_ang
    show U_sad
    "U" "히잉..."
    zeno "이 녀석을 대신해서 사과할게."
    name "아니... 저는 다치지 않아서 괜찮은데요...{p=1.0}아까 전부에 레이나도 그렇고 테디안도 그렇고 선생님까지...{p=.5}제가 처한 상황을 저조차 이해를 못하겠는데요..."
    zeno "으음... 뭐라고 설명하면 제일 좋으려나..."
    "선생님은 고민하시는 것 같다."
    "U" "히잉..."
    zeno "저 녀석... U는 병이 좀 있어."
    "목소리를 낮춰 물었다."
    name "병이요?"
    "내 귀에 속삭였다."
    zeno "본인 앞에서 할 만한 이야기는 아니니까, 나가서 하자."
    play sound "walk_slow.mp3"
    scene bg_black with dissolve
    $renpy.pause(2.0)
    stop sound 
    play sound "walk_slow.mp3"
    $renpy.pause(5.0)
    stop sound  
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    stop sound
    scene bg_teacher with dissolve
    zeno "여기 앉아 볼래?"
    name "네."
    zeno "U는 정체감 장애가 있어."
    name "...? {w=.5}뭐죠, 그게?"
    zeno "'해리성 정체감 장애.'{w=.5} 흔히들 다중 인격이라고 많이 하지."
    name "다중 인격이라면..."
    zeno "영화. 드라마에 뻔질나게 나오는 것과는 다르게 희귀병이라는데 U는 앓고 있어."
    name "왜 치료를 안 하는거죠?"
    zeno "해리성 정체감 장애는 희귀병 중에서도 상위권에 위치할 정도로 드물어.{p=.5}미국 같은 나라에도 치료 사례는 고사하고 발병 사례도 몇 년에 한 번 나올까 말까 한 정도인데 그걸 뚝딱 고칠 수는 없을거 아니야."
    zeno "그리고 저 녀석은 주도권을 '원래의 U' 쪽이 잡고 있으니까 그렇게 심각하지도 않아. 심각하지 않아야 하는데..."
    name "...피가 도화선이라는 건가요?"
    zeno "응. 저것도 꽤 호전된 거야. 옛날에는 사람 피는 물론 동물의 피나 피 상상도 엄금이었어."
    name "......."
    zeno "저렇게 호전된 건 미첼의 공이 크긴 한데... {w=.5}이 이상 궁금한 일 있으면 본인들한테 들으시고, 많이 놀랐지?"
    name "아뇨, 별로 안 놀랐어요."
    "놀람의 정도로만 따지면 평소의 아리아쪽이 더 심하다."
    zeno "그럼 다행이고.{w=.5} 자, 이거라도 하나 먹어."
    "검정색 홍삼 캔디.{p=.5}비닐을 벗겨 입에 집어 넣었다."
    name "안녕히 계세요."
    zeno "별로 안 바쁘다면 검도부실로 돌아가 봐. 아마 레이나가 '뭔가' 준비해 놓았을 거야."
    name "알겠습니다."
    play sound "sliding.mp3"
    scene bg_black with dissolve
    $renpy.pause(2.0)
    stop sound
    "아리아 덕분에 예민해진 나의 촉이 선생님이 말씀하신 '뭔가'에 대해 경고했으나 성의를 무시할 수는 없을 것 같아 검도부실로 향했다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    stop sound
    scene bg_knight
    show reina_nom at left
    show tedian_hap at right
    show U_sad at upcentor
    with dissolve
    "구석에 작은 솥이 끓고 있다."
    reina "어, 딱 맞춰서 왔네."
    name "이게... 뭐야?"
    reina "뭐긴, 차 끓일때 쓰는 솥이지. 테디안, 불 꺼도 될 거 같아."
    "찻잔을 하나 받았다."
    tedian "뜨거우니까 조심하세요."
    "잔 가득이 따라지는 녹색 액체."
    name "이게 뭐야?"
    tedian "가루녹차요."
    name "비싼거 아니야?"
    tedian "잘 모르겠어요. 부비로 산게 아니라 레이나 선배가 선물 받은 거라서요."
    reina "내가 뭘 가지고 있는 것도 아니니까.{p=.5}사과의 뜻으로는 딱이지."
    play sound "walk.mp3"
    "울려퍼지는 발소리."
    $renpy.pause(2.0)
    stop sound
    play sound "sliding.mp3"
    if where == "크레이":
        crey "들어갈게요!"
    else:
        "???" "들어갈게요!"
    $renpy.pause(2.0)
    stop sound
    "찻잔에 담긴 차가 튀어오를 정도로 기운차게 문이 열렸다."
    show crey_nom at centor with dissolve
    if where == "크레이":
        crey "어라, 티타임을 방해해버린 건가요?"
        reina "아니, 상관없어. 너도 줄까?"
        crey "헤헤, 부탁할게요. {w=.5}그런데 U 선배는 저 구석에서 뭐하시는 거에요?"
    else:
        "???" "어라, 티타임을 방해해버린 건가요?"
        reina "아니, 상관없어. 너도 줄까?"
        crey "헤헤, 부탁할게요. {w=.5}그나저나 못보던 분이 있네요?"
        reina "반 친구야"
        crey "안녕하세요. 전 [crey]라고 해요."
        name "난 [name]이야."
    "U" "히잉..."
    reina "그만 하시고 사과하는게 어때요?"
    "U" "미안해... 내...내가 그만..."
    name "괜찮아요. 선배님이야 말로 괜찮으세요?"
    "U" "나...나는... 괜찮아..."
    crey "무슨 일 있었어요?"
    reina "U 선배잖아. 왜인지는 뻔하지 않아?"
    crey "...못 볼 것을 보였나 보네요."
    "U" "너까지 놀리면... 난 누구를 믿어야 하냐..."
    crey "미첼 선배한테 가 보면 되는 것 아녜요?"
    "U" "야... 그 분을 그렇게 쉽게 만날 수 있을 것 같아?"
    if eventM:
        "아까 만나고 왔는데..."
    "담소."
    "검도부원들은 서로에 대해서 상당히 잘 알고 있는 듯 했다."
    play sound "drink.ogg"
    $renpy.pause(1.6)
    stop sound
    hide reina_nom
    show reina_hap at left
    hide U_sad
    show U_sad at upcentor
    hide crey_nom
    show crey_hap
    reina "그랬었단 말이지..."
    crey "예. 정말... 좋았어요."
    



    
