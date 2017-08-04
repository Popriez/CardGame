from PySide import QtGui,QtCore
import sys
import random
import getpass
user = getpass.getuser()

from PySide.QtCore import QObject, Signal, Slot
if not "C:/Users/"+user+"/Documents/CardGame" in sys.path:
    sys.path.append("C:/Users/"+user+"/Documents/CardGame")

import pipelineGameCard.CG_masterCompiled as GameFuc
reload(GameFuc)


class CardGame(QtGui.QDialog):
    
    def __init__(self):
        super(CardGame, self).__init__()

        self.cardGame = GameFuc.c
        self.check = 0
        self.setFixedSize(QtCore.QSize(600,510))
        self.w = 600
        self.h = 510
        self.widget()
        self.layout()
        self.connect()
        self.timer()
        self.virable()


        #self.setAcceptDrops(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.c1_count = 0
        self.c2_count = 0
        self.c3_count = 0
        self.heroCard_count = 0

        self.c1_switch = 0
        self.c2_switch = 0
        self.c3_switch = 0
        self.heroCard_switch = 0



    def widget(self):
        self.back_path = "backCard.png"
        self.ss_path = "space.png"
        self.atk_path = "aHero.png"
        self.dif_path = "dHero.png"
        self.brk_path = "bHero.png"
        self.hel_path = "heal.png"

        self.blank = QtGui.QPixmap(self.back_path)
        self.space = QtGui.QPixmap(self.ss_path)
        self.hero_pic = QtGui.QPixmap("charHero.png")
        self.monster_pic = QtGui.QPixmap("charMons.png")
        self.atk = QtGui.QPixmap(self.atk_path)
        self.dif = QtGui.QPixmap(self.dif_path)
        self.brk = QtGui.QPixmap(self.brk_path)
        self.hel = QtGui.QPixmap(self.hel_path)
        self.resize = QtGui.QPixmap("resize.png")


        self.title = QtGui.QLabel("CARD GAME |")
        self.title.setAlignment(QtCore.Qt.AlignLeft)
        self.title.setStyleSheet("QLabel{ color:white }")
        self.title.setFixedSize(QtCore.QSize(65,15))
        #self.label.setFixedSize(QtCore.QSize(1000,500))
        #self.label.setStyleSheet("""QLabel{ background:rgba(255, 255, 255); color : grey; border-radius:15px;}""")
        self.restart_button = QtGui.QPushButton("RESTART")
        self.restart_button.setFixedSize(QtCore.QSize(50,20))
        self.restart_button.setStyleSheet("""QPushButton{ background:white;border-radius:10px;}
            QPushButton:hover:!pressed{background:#CD853F}""")
        #self.s.setStyleSheet("QPushButton{background:red;color:yellow;}")
        self.minimize_button = QtGui.QPushButton("_")
        self.minimize_button.setFixedSize(QtCore.QSize(30,20))
        self.close_button = QtGui.QPushButton("x")
        self.close_button.setFixedSize(QtCore.QSize(30,20))


        self.heroHp_label = QtGui.QLabel("HP")
        self.heroHp_label.setStyleSheet("""QLabel{ color:white ;}""")
        self.monsterHp_label = QtGui.QLabel("HP")
        self.monsterHp_label.setStyleSheet("""QLabel{ color:white ;}""")
        self.turn_label = QtGui.QLabel("00")
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_label.setFixedSize(QtCore.QSize(30,30))
        self.turn_label.setStyleSheet("""QLabel{ ;background:white; border-radius:15px; }""")
        self.heroHp_bar = QtGui.QProgressBar()
        self.heroHp_bar.setAlignment(QtCore.Qt.AlignCenter)
        #self.heroHp_bar.setTextVisible (False)
        self.heroHp_bar.setMaximum(300)
        self.heroHp_bar.setMinimum(0)
        self.heroHp_bar.setValue(self.cardGame.hero.hp)

        self.monsterHp_bar = QtGui.QProgressBar()
        self.monsterHp_bar.setMaximum(150)
        self.monsterHp_bar.setMinimum(0)
        self.monsterHp_bar.setValue(self.cardGame.monsterType.hp)

        self.monsterHp_bar.setAlignment(QtCore.Qt.AlignCenter)
        #self.monsterHp_bar.setTextVisible (False)
        self.monsterHp_bar.setInvertedAppearance (True)


        self.hero_event = QtGui.QLabel("Hero Event")
        self.hero_event.setAlignment(QtCore.Qt.AlignCenter)
        self.hero_event.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")
        self.hero_event.setFixedSize(QtCore.QSize(200,30))
        self.monster_event = QtGui.QLabel("Monster Event")
        self.monster_event.setAlignment(QtCore.Qt.AlignCenter)
        self.monster_event.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")
        self.monster_event.setFixedSize(QtCore.QSize(200,30))
        
        shadow = QtGui.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0))

        shadow2 = QtGui.QGraphicsDropShadowEffect(self)
        shadow2.setBlurRadius(20)
        shadow2.setOffset(5)
        shadow2.setColor(QtGui.QColor(0, 0, 0))

        shadow3 = QtGui.QGraphicsDropShadowEffect(self)
        shadow3.setBlurRadius(20)
        shadow3.setOffset(5)
        shadow3.setColor(QtGui.QColor(0, 0, 0))

        shadow4 = QtGui.QGraphicsDropShadowEffect(self)
        shadow4.setBlurRadius(20)
        shadow4.setOffset(5)
        shadow4.setColor(QtGui.QColor(0, 0, 0))

        shadow5 = QtGui.QGraphicsDropShadowEffect(self)
        shadow5.setBlurRadius(20)
        shadow5.setOffset(5)
        shadow5.setColor(QtGui.QColor(0, 0, 0))

        shadow6 = QtGui.QGraphicsDropShadowEffect(self)
        shadow6.setBlurRadius(20)
        shadow6.setOffset(5)
        shadow6.setColor(QtGui.QColor(0, 0, 0))

        shadow7 = QtGui.QGraphicsDropShadowEffect(self)
        shadow7.setBlurRadius(20)
        shadow7.setOffset(5)
        shadow7.setColor(QtGui.QColor(0, 0, 0))

        shadow8 = QtGui.QGraphicsDropShadowEffect(self)
        shadow8.setBlurRadius(20)
        shadow8.setOffset(5)
        shadow8.setColor(QtGui.QColor(0, 0, 0))


        
        self.hero_dis = QtGui.QLabel()
        self.hero_dis.setGraphicsEffect(shadow)
        self.hero_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.hero_dis.setStyleSheet("""QLabel{  border-radius:10px; }""")
        self.hero_dis.setPixmap (self.hero_pic)
        self.monster_dis = QtGui.QLabel()
        self.monster_dis.setGraphicsEffect(shadow2)
        self.monster_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.monster_dis.setStyleSheet("""QLabel{  border-radius:10px; }""")
        self.monster_dis.setPixmap (self.monster_pic)

        self.hero_card = QtGui.QLabel()
        self.hero_card.setGraphicsEffect(shadow3)
        self.hero_card.setAlignment(QtCore.Qt.AlignCenter)
        self.hero_card.setStyleSheet("""QLabel{  border-radius:10px; }""")
        self.hero_card.setPixmap (self.space)
        self.hero_card.setAcceptDrops(True)
        self.hero_card.mouseMoveEvent = self.dragMoveEvent_heroCard
        self.hero_card.dragEnterEvent = self.dragEvent_heroCard
        self.hero_card.dropEvent = self.dropEvent_heroCard

        self.monster_card = QtGui.QLabel()
        self.monster_card.setGraphicsEffect(shadow4)
        self.monster_card.setAlignment(QtCore.Qt.AlignCenter)
        self.monster_card.setStyleSheet("""QLabel{  border-radius:10px; }""")
        self.monster_card.setPixmap (self.space) 
        self.monster_card.setAcceptDrops(True)

        self.vs = QtGui.QLabel("VS")
        self.vs.setAlignment(QtCore.Qt.AlignCenter)
        self.vs.setFixedSize(QtCore.QSize(50,150))
        self.vs.setStyleSheet("""QLabel{ color:white; }""")



        self.hero = QtGui.QLabel("HERO")
        self.hero.setAlignment(QtCore.Qt.AlignCenter)
        self.hero.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")
        self.hero.setFixedSize(QtCore.QSize(100,30))
        self.monster = QtGui.QLabel("MONSTER")
        self.monster.setAlignment(QtCore.Qt.AlignCenter)
        self.monster.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")
        self.monster.setFixedSize(QtCore.QSize(100,30))
        self.battle_button = QtGui.QPushButton("BATTLE")
        self.battle_button.setFixedSize(QtCore.QSize(70,20))
        self.battle_button.setStyleSheet("""QPushButton{ background:#CD853F;border-radius:10px;}
            QPushButton:hover:!pressed{background:#DAA520}""")


        self.c1 = QtGui.QLabel()
        self.c1.setGraphicsEffect(shadow5)
        self.c1.setAlignment(QtCore.Qt.AlignCenter)
        self.c1.setPixmap(self.space)
        self.c1.setAcceptDrops(True)
        self.c1.mouseMoveEvent = self.dragMoveEvent_c1
        self.c1.dragEnterEvent = self.dragEvent_c1
        self.c1.dropEvent = self.dropEvent_c1
        #self.c1.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")

        self.c2 = QtGui.QLabel()
        self.c2.setGraphicsEffect(shadow6)
        self.c2.setAlignment(QtCore.Qt.AlignCenter)
        self.c2.setPixmap(self.space)
        self.c2.setAcceptDrops(True)
        self.c2.mouseMoveEvent = self.dragMoveEvent_c2
        self.c2.dragEnterEvent = self.dragEvent_c2
        self.c2.dropEvent = self.dropEvent_c2
        #self.c2.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")

        self.c3 = QtGui.QLabel()
        self.c3.setGraphicsEffect(shadow7)
        self.c3.setAlignment(QtCore.Qt.AlignCenter)
        self.c3.setPixmap(self.space)
        self.c3.setAcceptDrops(True)
        self.c3.mouseMoveEvent = self.dragMoveEvent_c3
        self.c3.dragEnterEvent = self.dragEvent_c3
        self.c3.dropEvent = self.dropEvent_c3
        #self.c3.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")

        self.deck = QtGui.QLabel()
        self.deck.setGraphicsEffect(shadow8)
        self.deck.setAlignment(QtCore.Qt.AlignCenter)
        self.deck.setPixmap(self.blank)
        #self.deck.setStyleSheet("""QLabel{ background:white; border-radius:15px; }""")
        self.deck.mouseMoveEvent = self.dragMoveEvent_deck


        self.scale = QtGui.QLabel()
        self.scale.setPixmap(self.resize)
        self.scale.setAlignment(QtCore.Qt.AlignRight)
        self.scale.enterEvent = self.mouseEnterEvent
        self.scale.leaveEvent = self.mouseLeaveEvent



        #self.deck.dragMoveEvent = self.mouseEnterEvent

        
    def connect(self):
        self.restart_button.clicked.connect(self.restart)
        self.close_button.clicked.connect(self.end)
        self.minimize_button.clicked.connect(self.minimize)
        self.battle_button.clicked.connect(self.battleCard)
        self.scale.mouseMoveEvent = self.scaleF




    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        headlayout = QtGui.QHBoxLayout()
        closelayout = QtGui.QHBoxLayout()
        hplayout = QtGui.QHBoxLayout()
        eventlayout = QtGui.QHBoxLayout()
        h_eventlayout = QtGui.QHBoxLayout()
        m_eventlayout = QtGui.QHBoxLayout()
        showlayout = QtGui.QHBoxLayout()
        namelayout = QtGui.QHBoxLayout()
        cardlayout = QtGui.QHBoxLayout()
        footlayout = QtGui.QHBoxLayout()

        dialog = QtGui.QDialog()
        dialog.setLayout(mainlayout)
        dialog.setStyleSheet("""QDialog{ background:rgba(255,192,203, 200);  border-radius:15px;}""")

        panel = QtGui.QVBoxLayout()
        panel.addWidget(dialog)



        headlayout.addWidget(self.title)
        headlayout.addWidget(self.restart_button)
        headlayout.setAlignment(QtCore.Qt.AlignTop)
        headlayout.setAlignment(self.restart_button,QtCore.Qt.AlignLeft)

        closelayout.addWidget(self.minimize_button)
        closelayout.addWidget(self.close_button)
        closelayout.setAlignment(QtCore.Qt.AlignRight)


        hplayout.addWidget(self.heroHp_label)
        hplayout.addWidget(self.heroHp_bar)
        hplayout.addWidget(self.turn_label)
        hplayout.addWidget(self.monsterHp_bar)
        hplayout.addWidget(self.monsterHp_label)
        hplayout.setAlignment(QtCore.Qt.AlignTop)


        eventlayout.addLayout(h_eventlayout)
        eventlayout.addLayout(m_eventlayout)
        h_eventlayout.addWidget(self.hero_event)
        m_eventlayout.addWidget(self.monster_event)
        #eventlayout.setAlignment(QtCore.Qt.AlignCenter)
        h_eventlayout.setAlignment(QtCore.Qt.AlignLeft)
        m_eventlayout.setAlignment(QtCore.Qt.AlignRight)


        showlayout.addWidget(self.hero_dis)
        showlayout.addWidget(self.hero_card)
        showlayout.addWidget(self.vs)
        showlayout.addWidget(self.monster_card)
        showlayout.addWidget(self.monster_dis)
        showlayout.setAlignment(QtCore.Qt.AlignCenter)


        namelayout.addWidget(self.hero)
        namelayout.addWidget(self.battle_button)
        namelayout.addWidget(self.monster)


        cardlayout.addWidget(self.c1)
        cardlayout.addWidget(self.c2)
        cardlayout.addWidget(self.c3)
        cardlayout.addWidget(self.deck)


        footlayout.addWidget(self.scale)
        footlayout.setAlignment(QtCore.Qt.AlignRight)


        headlayout.addLayout(closelayout)
        mainlayout.addLayout(headlayout)
        mainlayout.addLayout(hplayout)
        mainlayout.addLayout(eventlayout)
        mainlayout.addLayout(showlayout)
        mainlayout.addLayout(namelayout)
        mainlayout.addLayout(cardlayout)
        mainlayout.addLayout(footlayout)
        mainlayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(panel)
        self.setWindowTitle("CardGame")

        dialog.keyPressEvent = self.keyPressEvent




    def keyPressEvent(self,event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()

    def end(self):
        self.close()

    def minimize(self):
        self.showMinimized()

    def scaleF(self,event):

        x = event.x()
        y = event.y()
        self.w += x
        self.h += y

        if self.w < 600 :
            self.w = 600
        if self.h < 510 :
            self.h = 510
        else:
            self.setFixedSize(QtCore.QSize(self.w,self.h))
        #self.title.setFixedSize(QtCore.QSize(self.w/10,self.h/10))
        #self.restart_button.setFixedSize(QtCore.QSize(self.w/10,self.h/10))
        #self.minimize_button.setFixedSize(QtCore.QSize(self.w/10,self.h/10))
        #self.close_button.setFixedSize(QtCore.QSize(self.w/4,self.h/4))
        #self.heroHp_bar.setFixedSize(QtCore.QSize(self.w/10,self.h/10))
        #self.turn_label.setFixedSize(QtCore.QSize(self.w/10,self.h/10))
        #self.monsterHp_bar.setFixedSize(QtCore.QSize(self.w/10,self.h/10))

        #self.blank = self.blank.scaled(100+x,150+y,aspectMode=QtCore.Qt.IgnoreAspectRatio,mode=QtCore.Qt.SmoothTransformation)
        #self.deck.setPixmap(self.blank)
        #self.space = self.space.scaled(100+x,150+y,aspectMode=QtCore.Qt.IgnoreAspectRatio,mode=QtCore.Qt.SmoothTransformation)
        #self.c1.setPixmap(self.space)
        #self.c2.setPixmap(self.space)
        #self.c3.setPixmap(self.space)
        

    def restart(self):
        reload(GameFuc)
        self.close()
        c = CardGame()
        c.show()

    def mousePressEvent(self,event):
        self.moving = True
        self.mouseClick = event.pos()

    def mouseMoveEvent(self,event):
        if self.moving:
            self.move(event.globalPos()-self.mouseClick)

    def mouseEnterEvent(self,event):
        self.setCursor(QtCore.Qt.SizeFDiagCursor)
    def mouseLeaveEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)




    def dragMoveEvent_deck(self,event):
        #self.setCursor(QtCore.Qt.DragCopyCursor)
        #self.setCursor(self.blank)
        #event.setDragCursor(self.blank)
        mimeData = QtCore.QMimeData()
        mimeData.setText(self.back_path)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

        pixmap = QtGui.QPixmap(self.back_path)
        #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

        drag.setPixmap(pixmap)
        drag.start(QtCore.Qt.MoveAction)

    def dragMoveEvent_c1(self,event):
        
        if self.c1_count != 0 :
            self.c1_switch=1
            self.c2_switch=0
            self.c3_switch=0
            self.heroCard_switch=0
            if self.c1_count == 1:
                self.pic = self.atk_path
            elif self.c1_count == 2:
                self.pic = self.dif_path
            elif self.c1_count == 3:
                self.pic = self.brk_path
            elif self.c1_count == 4:
                self.pic = self.hel_path

            #self.setCursor(QtCore.Qt.DragCopyCursor)
            #self.setCursor(self.blank)
            #event.setDragCursor(self.blank)
            mimeData = QtCore.QMimeData()
            mimeData.setText(self.pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(self.pic)
            #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)
            
        else :
            event.ignore()

    def dragMoveEvent_c2(self,event):
        
        if self.c2_count != 0 :
            self.c1_switch=0
            self.c2_switch=1
            self.c3_switch=0
            self.heroCard_switch=0
            if self.c2_count == 1:
                self.pic = self.atk_path
            elif self.c2_count == 2:
                self.pic = self.dif_path
            elif self.c2_count == 3:
                self.pic = self.brk_path
            elif self.c2_count == 4:
                self.pic = self.hel_path

            #self.setCursor(QtCore.Qt.DragCopyCursor)
            #self.setCursor(self.blank)
            #event.setDragCursor(self.blank)
            mimeData = QtCore.QMimeData()
            mimeData.setText(self.pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(self.pic)
            #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)
            

        else :
            event.ignore()

    def dragMoveEvent_c3(self,event):

        if self.c3_count != 0 :
            self.c1_switch=0
            self.c2_switch=0
            self.c3_switch=1
            self.heroCard_switch=0
            if self.c3_count == 1:
                self.pic = self.atk_path
            elif self.c3_count == 2:
                self.pic = self.dif_path
            elif self.c3_count == 3:
                self.pic = self.brk_path
            elif self.c3_count == 4:
                self.pic = self.hel_path

            #self.setCursor(QtCore.Qt.DragCopyCursor)
            #self.setCursor(self.blank)
            #event.setDragCursor(self.blank)
            mimeData = QtCore.QMimeData()
            mimeData.setText(self.pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(self.pic)
            #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)

        else :
            event.ignore()

    def dragMoveEvent_heroCard(self,event):
        
        if self.heroCard_count != 0 :
            self.c1_switch=0
            self.c2_switch=0
            self.c3_switch=0
            self.heroCard_switch=1
            if self.heroCard_count == 1:
                self.pic = self.atk_path
            elif self.heroCard_count == 2:
                self.pic = self.dif_path
            elif self.heroCard_count == 3:
                self.pic = self.brk_path
            elif self.heroCard_count == 4:
                self.pic = self.hel_path

            #self.setCursor(QtCore.Qt.DragCopyCursor)
            #self.setCursor(self.blank)
            #event.setDragCursor(self.blank)
            mimeData = QtCore.QMimeData()
            mimeData.setText(self.pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(self.pic)
            #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)

        else :
            event.ignore()





    def dragEvent_c1(self,event):
        if self.c1_count == 0:
            event.accept()

    def dragEvent_c2(self,event):
        if self.c2_count == 0:
            event.accept()

    def dragEvent_c3(self,event):
        if self.c3_count == 0:
            event.accept()

    def dragEvent_heroCard(self,event):
        if self.heroCard_count == 0:
            event.accept()




    def dropEvent_c1(self,event):
        text = event.mimeData().text()
        if text == "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                if ran == 1 :
                    text = self.atk_path
                elif ran == 2 :
                    text = self.dif_path
                elif ran == 3 :
                    text = self.brk_path
                elif ran == 4 :
                    text = self.hel_path
  
                self.c1.setPixmap(text)
                self.c1_count = ran

            else:
                event.ignore()

        elif text != "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.c1.setPixmap(text)
                if text == self.atk_path:
                    self.c1_count = 1
                elif text == self.dif_path:
                    self.c1_count = 2
                elif text == self.brk_path:
                    self.c1_count = 3
                elif text == self.hel_path:
                    self.c1_count = 4

                if self.c2_switch == 1 :
                    self.c2.setPixmap(self.space)
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c3_switch == 1 :
                    self.c3.setPixmap(self.space)
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.heroCard_switch == 1 :
                    self.hero_card.setPixmap(self.space)
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()

    def dropEvent_c2(self,event):
        text = event.mimeData().text()
        if text == "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                #text = event.mimeData().text()
                if ran == 1 :
                    text = self.atk_path
                elif ran == 2 :
                    text = self.dif_path
                elif ran == 3 :
                    text = self.brk_path
                elif ran == 4 :
                    text = self.hel_path

                self.c2.setPixmap(text)
                self.c2_count = ran

            else:
                event.ignore()

        elif text != "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.c2.setPixmap(text)
                if text == self.atk_path:
                    self.c2_count = 1
                elif text == self.dif_path:
                    self.c2_count = 2
                elif text == self.brk_path:
                    self.c2_count = 3
                elif text == self.hel_path:
                    self.c2_count = 4

                if self.c1_switch == 1 :
                    self.c1.setPixmap(self.space)
                    self.c1_switch = 0
                    self.c1_count = 0
                elif self.c3_switch == 1 :
                    self.c3.setPixmap(self.space)
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.heroCard_switch == 1 :
                    self.hero_card.setPixmap(self.space)
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()

    def dropEvent_c3(self,event):
        text = event.mimeData().text()
        if text == "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                #text = event.mimeData().text()
                if ran == 1 :
                    text = self.atk_path
                elif ran == 2 :
                    text = self.dif_path
                elif ran == 3 :
                    text = self.brk_path
                elif ran == 4 :
                    text = self.hel_path

                self.c3.setPixmap(text)
                self.c3_count = ran

            else:
                event.ignore()

        elif text != "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.c3.setPixmap(text)
                if text == self.atk_path:
                    self.c3_count = 1
                elif text == self.dif_path:
                    self.c3_count = 2
                elif text == self.brk_path:
                    self.c3_count = 3
                elif text == self.hel_path:
                    self.c3_count = 4

                if self.c2_switch == 1 :
                    self.c2.setPixmap(self.space)
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c1_switch == 1 :
                    self.c1.setPixmap(self.space)
                    self.c1_switch = 0
                    self.c1_count = 0
                elif self.heroCard_switch == 1 :
                    self.hero_card.setPixmap(self.space)
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()

    def dropEvent_heroCard(self,event):
        text = event.mimeData().text()
        print text
        if text != "backCard.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.hero_card.setPixmap(text)
                if text == self.atk_path:
                    self.heroCard_count = 1
                elif text == self.dif_path:
                    self.heroCard_count = 2
                elif text == self.brk_path:
                    self.heroCard_count = 3
                elif text == self.hel_path:
                    self.heroCard_count = 4

                if self.c2_switch == 1 :
                    self.c2.setPixmap(self.space)
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c3_switch == 1 :
                    self.c3.setPixmap(self.space)
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.c1_switch == 1 :
                    self.c1.setPixmap(self.space)
                    self.c1_switch = 0
                    self.c1_count = 0

            else:
                event.ignore()






    def barhp(self):
        if self.valueH != self.cardGame.hero.hp :
            self.heroHp_bar.setValue(self.valueH)
            if self.valueH <= self.cardGame.hero.hp:
                self.valueH+=1
            else:
                self.valueH-=1

        if self.cardGame.bossburn == 0 :
            if self.valueM != self.cardGame.monsterType.hp :
                self.monsterHp_bar.setValue(self.valueM)
                if self.valueM <= self.cardGame.monsterType.hp:
                    self.valueM+=1
                else:
                    self.valueM-=1
        else :
            if self.check == 0 :
                self.monster_dis.setPixmap(QtGui.QPixmap(self.cha[2]))
                self.monsterHp_bar.setMaximum(300)
                self.monsterHp_bar.setValue(self.valueB)
                self.hero_event.setText("HERO WIN !! BUT!")
                self.monster_event.setText("BOSS APPEAR !!!!") 
                self.monster_card.setPixmap(self.space)
                self.check = 1
            if self.valueB != self.cardGame.monsterType.hp :
                self.monsterHp_bar.setValue(self.valueB)
                if self.valueB <= self.cardGame.monsterType.hp:
                    self.valueB+=1
                else:
                    self.valueB-=1

        if self.valueH == self.cardGame.hero.hp and self.valueM == self.cardGame.monsterType.hp :
            self.timer.stop()


    def battleCard(self):
        if self.heroCard_count != 0:
            self.cardGame.hero.selectCard = self.heroCard_count-1
            self.cardGame.randomCard(self.cardGame.monsterType)
            self.monster_card.setPixmap(QtGui.QPixmap(self.monsCard[self.cardGame.monsterType.selectCard]))
            self.cardGame.start()
            self.hero_event.setText(self.cardGame.statusHero)
            self.monster_event.setText(self.cardGame.statusMons) 
            self.timer.start()
            self.heroCard_count = 0
            self.hero_card.setPixmap(self.space)
            print self.cardGame.monsterType.hp 
            print self.cardGame.hero.hp
            self.turn_label.setText("%02d"%(self.cardGame.turn))
            if self.cardGame.monsterType.hp <= 0:
                win = Victory(self)
                win.exec_()
            elif self.cardGame.hero.hp <= 0:
                lose = Defeted(self)
                lose.exec_()


    def timer(self):
        self.valueH = 300
        self.valueM = 150
        self.valueB = 300
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.barhp)

    def virable(self):
        self.cha = ["charHero.png","charMons.png","charBoss.png"]
        self.heroCard = ["aHero.png","dHero.png","bHero.png","heal.png"]
        self.monsCard = ["aMons.png","dMons.png","bMons.png","heal.png"]
        self.bossCard = ["aBoss.png","dMons.png","bMons.png","heal.png"]







class Victory(QtGui.QDialog):
    def __init__(self,parent):
        super(Victory,self).__init__(parent)
        self.setFixedSize(QtCore.QSize(300,200))
        self.widget()
        self.layout()
        self.connect()
        
    def widget(self):

        self.mainlabel = QtGui.QLabel("YOU WIN")

        self.hero_pic = QtGui.QPixmap("charHero.png")
        self.hero_dis = QtGui.QLabel()
        self.hero_dis.setPixmap (self.hero_pic)

        self.OK_btn = QtGui.QPushButton("OK")
        
    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        suplayout = QtGui.QHBoxLayout()

        suplayout.addWidget(self.hero_dis)
        suplayout.addWidget(self.mainlabel)
        mainlayout.addLayout(suplayout)

        mainlayout.addWidget(self.OK_btn)

        self.setLayout(mainlayout)
        self.setWindowTitle("WIN")
        
    def connect(self):
        self.OK_btn.clicked.connect(self.exit)

    def exit(self):
        window.close()

class Defeted(QtGui.QDialog):
    def __init__(self,parent):
        super(Defeted,self).__init__(parent)
        self.setFixedSize(QtCore.QSize(300,200))
        self.widget()
        self.layout()
        self.connect()
        
    def widget(self):

        self.mainlabel = QtGui.QLabel("YOU LOSE")

        self.monster_pic = QtGui.QPixmap("charBoss.png")
        self.monster_dis = QtGui.QLabel()
        self.monster_dis.setPixmap (self.monster_pic)

        self.OK_btn = QtGui.QPushButton("OK")
        
    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        suplayout = QtGui.QHBoxLayout()

        suplayout.addWidget(self.monster_dis)
        suplayout.addWidget(self.mainlabel)
        mainlayout.addLayout(suplayout)

        mainlayout.addWidget(self.OK_btn)

        self.setLayout(mainlayout)
        self.setWindowTitle("LOSE")
        
    def connect(self):
        self.OK_btn.clicked.connect(self.exit)

    def exit(self):
        window.close()





app = QtGui.QApplication(sys.argv)
window = CardGame()
window.show()
app.exec_()
