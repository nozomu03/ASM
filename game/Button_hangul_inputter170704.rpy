init python:

    ### 한글 입력기의 스타일들
    
    style.hi_frame.align = (.5, .5)                                              # Frame 스타일
    style.hi_frame.background = '#ff000030'
    
    style.hi_label.size = 25                                                     # Label 스타일 (입력기 제일 위에 보이는 문구)
    style.hi_text.size = 50                                                      # 입력받은 텍스트를 표시하는데 사용할 스타일
    
    style.hi_alphabet_button.insensitive_background = '#00000000'       # 한글 자/모음 표시된 버튼에 사용할 스타일
    style.hi_alphabet_button.idle_background = '#ff000060'
    style.hi_alphabet_button.hover_background = '#00ffff80'
    
    style.hi_alphabet_button_text.size = 24                                        # 한글 자/모음 표시된 버튼에 있는 텍스트에 사용할 스타일
    
    style.hi_button.idle_background = '#ff000060'            # 기타 버튼에 적용할 스타일
    style.hi_button.hover_background = '#00ffff80'
    style.hi_button.insensitive_background = '#88888860'
    
    style.hi_button_text.size = 30                                 # 기타 버튼에 있는 텍스트에 적용할 스타일
    
        

##########################################
# The code which implements the hangul inputter.
# Originally scripted by JQuartz, edited by backansi from Lemma soft forum.

init -1 python:
    
    def hangulInput(prompt='', default = '', limit=99):
        if type(default) == int:
            limit = default
            default = ''
            
        hangul = HI(default, limit)
        
        while True:
            ui.frame(style = 'hi_frame')
            ui.vbox()
            if prompt:
                ui.text(prompt)
            name, final = hangul.db()
            
            if name:
                return name, final
            

    ##############################
    # Create styles.
    
    style.hi_frame=Style(style.frame)
    style.hi_label = Style(style.label)
    style.hi_text=Style(style.text)
    style.hi_alphabet_button=Style(style.button)
    style.hi_alphabet_button_text=Style(style.button_text)
    style.hi_button=Style(style.button)
    style.hi_button_text=Style(style.button_text)

    class HI:
        global final, input
        placeHolder = tempWord = ''
        cho = jung = jong = 0
        state = 'start'
        alphabets=[
                    ("ㄱ", 1, 1, 0),("ㄴ", 3, 4, 0),("ㄷ", 4, 7, 0),("ㄹ", 6, 8, 0),("ㅁ", 7, 16, 0),
                    ("ㅂ", 8, 17, 0),("ㅅ", 10, 19, 0),("ㅇ", 12, 21, 0),("ㅈ", 13, 22, 0),("ㅊ", 15, 23, 0),
                    ("ㅋ", 16, 24, 0),("ㅌ", 17, 25, 0),("ㅍ", 18, 26, 0),("ㅎ", 19, 27, 0),(" ", 0, 0, 4),

                    ("ㄲ", 2, 2, 0),("ㄸ", 5, 29, 0),("ㅃ", 9, 30, 0),("ㅆ", 11, 20, 0),("ㅉ", 14, 31, 0),
                    (" ", 0, 0, 4),

                    ("ㄳ", 0, 3, 2),("ㄵ", 0, 5, 2),("ㄶ", 0, 6, 2),("ㄺ", 0, 9, 2),("ㄻ", 0, 10, 2),
                    ("ㄼ", 0, 11, 2),    ("ㄽ", 0, 12, 2),("ㄾ", 0, 13, 2),("ㄿ", 0, 14, 2),("ㅀ", 0, 15, 2),
                    ("ㅄ", 0, 18, 2),(" ", 0, 0, 4),

                    ("ㅏ", 101, 0, 1),("ㅑ", 103, 0, 1),("ㅓ", 105, 0, 1),("ㅕ", 107, 0, 1),
                    ("ㅗ", 109, 0, 1),("ㅛ", 113, 0, 1),("ㅜ", 114, 0, 1),("ㅠ", 118, 0, 1),
                    ("ㅡ", 119, 0, 1),("ㅣ", 121, 0, 1),(" ", 0, 0, 4),

                    ("ㅐ", 102, 0, 1),("ㅒ", 104, 0, 1),("ㅔ", 106, 0, 1),("ㅖ", 108, 0, 1),(" ", 0, 0, 4),

                    ("ㅘ", 110, 0, 1),("ㅙ", 111, 0, 1),("ㅚ", 112, 0, 1),("ㅝ", 115, 0, 1),("ㅞ", 116, 0, 1),
                    ("ㅟ", 117, 0, 1),("ㅢ", 120, 0, 1),(" ", 0, 0, 4),
                    ("지우기", 'delete', 0, 3), ("완료", 'done', 0, 3)]
        
        def __init__(self, default = None, limit = 0):
            self.word = default
            self.limit = limit
            
        def db(self):
                ################################################
    # to place the inputted words

            ui.text('%s%s|' %(self.word, self.placeHolder), style = 'hi_text')
            ui.null(height = 5)

    ###############################################
    # For putting buttons

            ui.hbox()
            for text, value, value2, type in self.alphabets:
                if len(self.word) <= self.limit-1:
                    if type==0 :
                        
                        if self.state=='jungsung':
                            ui.textbutton(text, ui.returns(value2), 
                                            style = "hi_alphabet_button", 
                                            text_style = "hi_alphabet_button_text")

                        elif self.state == 'chosung':
                            ui.textbutton(text, style = "hi_alphabet_button", text_style = "hi_alphabet_button_text")
                            
                        else:
                            ui.textbutton(text, ui.returns(value), style = "hi_alphabet_button", text_style = "hi_alphabet_button_text")

                    if type==1:                        
                       
                        if self.state == 'chosung' or self.state=='wait':
                            ui.textbutton(text, ui.returns(value), 
                                            style = "hi_alphabet_button", 
                                            text_style = "hi_alphabet_button_text")
                        
                        else:
                            ui.textbutton(text, 
                                            style = "hi_alphabet_button", 
                                            text_style = "hi_alphabet_button_text")

                    if type==2:
                        
                        if self.state=='jungsung':
                            ui.textbutton(text, ui.returns(value2), 
                                            style = "hi_alphabet_button", 
                                            text_style = "hi_alphabet_button_text")
                            
                        else:
                            ui.textbutton(text, style = "hi_alphabet_button", text_style = "hi_alphabet_button_text")
                    
                    if type ==3:
                        if self.state =='start' and not self.word:
                            ui.textbutton(text, style = "hi_button", text_style = "hi_button_text")
                    
                        else:
                            ui.textbutton(text, ui.returns(value), style = "hi_button", text_style = "hi_button_text")
                        
                if type==4:
                    ui.close()
                    ui.hbox()
                    
                elif len(self.word) == self.limit:
                    if type == 3:   
                        ui.textbutton(text, ui.returns(value), 
                                           style = "hi_button", 
                                           text_style = "hi_button_text")
                    else:                   
                        ui.textbutton(text, 
                                           style = "hi_alphabet_button", 
                                           text_style = "hi_alphabet_button_text")
                
            ui.close()

            ui.close()      # vbox
            
            select = ui.interact()

        #########################################
        # convert value to unicode
            if select == 'delete':
                self.cho = self.jong = self.jung = 0
                if self.placeHolder:
                    self.placeHolder = ''
                else:
                    self.word = self.word [:-1]
                self.state = 'start'
                
                return 0, 0
                
            elif select == 'done':
                self.word = self.word + self.placeHolder
                self.placeHolder = ''
                self.cho = self.jung = self.jong = 0
                self.state = 'start'

                J_ki_last_alphabet=repr(self.word[-1])
                J_ki_dec = "%d" % int(str(J_ki_last_alphabet[4:-1]), 16)
                J_ki_dec=(int(J_ki_dec)-44032) % 588 % 28
                
                if J_ki_dec == 0: 
                    final = 0 
                else: 
                    final = 1
                    
                return self.word, final
                
            if self.state=='start':

                self.cho = select
                
                for text, value, value2, type in self.alphabets:
                    if self.cho == value and type==0:
                        self.placeHolder = text
        
                self.state='chosung'
                
                return 0, 0

            if self.state=='chosung':
                
                self.jung = select - 100
                self.placeHolder = (self.cho-1)*588 + (self.jung-1)*28 + 44032
                self.placeHolder = unichr (self.placeHolder)
                self.tempWord = self.placeHolder
                self.state='jungsung'

                return 0, 0

            if self.state=='jungsung':
                
                if len(self.word)<self.limit-1:
                    self.jong = select
                    self.tempWord = self.placeHolder
                    
                    if select in (29, 30, 31):
                        
                        self.word = self.word + self.tempWord
                        self.state = 'chosung'
                        
                        for text, value, value2, type in self.alphabets:
                            if self.jong==value2 and type ==0:
                                self.cho = value
                                self.placeHolder = text
                                
                        return 0, 0
                                
                    self.placeHolder = (self.cho-1)*588 + (self.jung-1)*28 + self.jong +44032
                    self.placeHolder = unichr (self.placeHolder)

                    for text, value, value2, type in self.alphabets:            
                        if self.jong == value2 and type==2:                      
                            self.word = self.word+ self.placeHolder
                            self.placeHolder = ''
                            self.state = 'start'                                         

                        elif self.jong == value2 and type == 0:
                            self.state='wait'
                        
                elif len(self.word)==self.limit-1:
                    
                    self.jong = select
                    self.placeHolder = (self.cho-1)*588 + (self.jung-1)*28 + self.jong +44032
                    self.placeHolder = unichr (self.placeHolder)
                    self.word = self.word + self.placeHolder
                    self.placeHolder=''
                    self.state = 'start'

                return 0, 0

            if self.state=='wait':
                
                if select >100:
                    
                    self.jung = select - 100
                    self.word = self.word + self.tempWord
                    
                    for text, value, value2, type in self.alphabets:
                        if self.jong == value2 and type==0:
                            self.cho = value

                    self.placeHolder = (self.cho-1)*588 + (self.jung-1)*28 + 44032
                    self.placeHolder = unichr (self.placeHolder)
                    self.state='jungsung'

                else:
                    
                    self.word = self.word + self.placeHolder
                    self.cho = select
                    
                    for text, value, value2, type in self.alphabets:
                        if self.cho == value and type==0:
                            self.placeHolder = text
                            
                    self.state = 'chosung'

                return 0, 0