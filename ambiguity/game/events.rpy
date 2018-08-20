# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.


# Some characters that are used in events in the game.
    
# First up, we define some simple events for the various actions, that
# are run only if no higher-priority event is about to occur.

init python:        
    tempact=None
    where=None
    event("redcross", "act == '보건실'")
    event("music", "act=='음악실'")
    event("money", "act=='총무부'") 
    event("shorttrip", "act=='신발장'")
    
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
    name '테디안?'
    tedian "심부름 중이신가 봐요?"
    name "응."
    tedian "요즈음에는 학생회도 총무부도 봉사회도 전부 바쁘니까요...{p=1.0}아, 그러고보니까 선배님은 축제 준비 안하시나요?"
    name "나 동아리 가입 안했어."
    tedian "예? 아무것도요?"
    name "응.{w=1.0}뭐, 그 대신 이렇게 학생회랑 총무부 일을 돕고 있지만."
    "\'아리아\'의 이야기는 꺼내지 않았다."
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
    "테디안은 눈으로 \'선배님이 제가 잘못할 때마다 잡아먹을 듯 으르렁거리는데 솜씨가 안 좋아지겠어요 그럼?\'이라고 말했다."
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
        if where != None:
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
        call temp
        name "힉..."
        hide pertin_sup
        show pertin_nom at right
        pertin "...시끄럽네."
        "테디안이 무엇인가 사고라도 친 것일까.{p=.5}실피아 선배의 노성이 교정을 가득 메웠다."
        pertin "거 참... 혼낼거면 좀 조용히 혼내라니까는..."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_mart 
        with dissolve
        pertin "뭐 해? 멍하니 서서는."
        name "아뇨, 이 시간대에 나오는 건 처음이라서."    
        peritn "{size=5}내 말대로 학생회에 들어왔으면 이 시간에도 마음껏 나갈 수 있었을텐데.{/size}"
        name "네?"
        pertin "아니야, 아무것도."
        play sound "walk_slow.mp3"
        "천천히 걸었다."
        play sound "door.mp3"
        scene bg_black with wiperight
        $renpy.pause(2.0)
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_mart with wipeleft
        "산 것들을 큰 수레에 실었다."
        pertin "혼자 밀 수 있겠어?"
        menu:
            "문제 없어요":
                name "괜찮아요."
                pertin "정말?"
                name "그럼요."
                play sound "wagon.wav"
                "밀었다.{p=1.0}기름칠을 하지 않은 채 오랫동안 창고에 박아 놓아서인지 바퀴의 움직임이 상당히 뻑뻑했다."
                $renpy.pause(2.0)                
                stop sound

            "헤헤... 좀 힘들긴 한데 괜찮아요!":

    return

label music:
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wiperight
    scene bg_music with wipeleft
    play sound "mixdown.mp3"
    "하모니카 소리." 
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