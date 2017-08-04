import random
class CardGame(object):
    def __init__(self,Hero,Monster,Boss):
        super(CardGame,self).__init__()
        self.hero = Hero
        self.monster = Monster
        self.boss = Boss
        self.monsterType = self.monster 
        self.cardHero = [0,0,0]
        self.state = 1
        self.turn = 0
        self.statusHero = ""
        self.statusMons = ""
        self.bossburn = 0
    
    def randomCard(self,x):
        x.selectCard = random.randint(0,3)
        self.monsterName = 'Mons'
        if self.state == 2 :
            self.monsterName = 'Boss'

    def randomCardHero(self):
        for x in range(3):
            self.cardHero[x] = random.randint(0,3)
        print 'Draw Card : ' + str(self.cardHero)
        
    def chooseCard(self):
        print 'You Have Card ' + str(self.cardHero)
        if self.hero.selectCard == 0 :
            pass #atk
        elif self.hero.selectCard == 1 :
            pass #def
        elif self.hero.selectCard == 2 :
            pass #brk
        else :
            pass #heal
                       
                   
    def imageHero(self):
        self.count = 0      
        for x in self.cardHero :
            if x == 0 :
                pass
            elif x == 1 :
                pass
            elif x == 2 :
                pass
            else :
                pass
            self.count+=1 

    def action(self):
        self.fineMonster = 1
        
             
        if self.state != 3 :            
            if self.hero.hp >0 and self.monsterType.hp >0 :
                
                print '--------- Turn ' + str(self.turn) +' -------------'
                
                self.imageHero()
                
                print 'Hero SelectCard == ' + str(self.hero.selectCard) + '\nMonster SelectCard == ' + str(self.monsterType.selectCard)
                if self.hero.selectCard == 0 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' +str(self.hero.atk) +'\n'+ self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                    self.statusHero = 'HP : - ' +str(self.monsterType.atk)
                    self.statusMons = 'HP : - ' +str(self.hero.atk)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= (self.hero.atk - self.monsterType.deff)
                    print 'Hero Attack : ' +str(self.hero.atk)+'\n'+self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)
                    self.statusHero = ''
                    self.statusMons = 'HP : - ' +str(self.hero.atk - self.monsterType.deff)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 2 :
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' + str(self.hero.atk) +'\n'+self.monsterType.name + ' Break  : Break Fail '
                    self.statusHero = ''
                    self.statusMons = 'HP : - ' +str(self.hero.atk)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.atk-self.monsterType.hel)
                    print 'Hero Attack : ' +str(self.hero.atk) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                    self.statusHero = '' 
                    self.statusMons = 'HP : - ' +str(self.hero.atk-self.monsterType.hel)
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= ( self.monsterType.atk - self.hero.deff )
                    print 'Hero Deffend : ' +str(self.hero.deff)+'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                    self.statusHero = 'HP : - ' +str( self.monsterType.atk - self.hero.deff )  
                    self.statusMons = ''       
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 1 :
                    print 'Hero Deffend : ' +str(self.hero.deff)+'\n'+self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff) +'\n'+  'Nothing' 
                    self.statusHero = ''
                    self.statusMons = ''   
                    print 'Nothing'
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    print 'Hero Deffend : Deffend Fail'+'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk)   
                    self.statusHero = 'HP : - ' +str(self.monsterType.brk)  
                    self.statusMons = '' 
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    print 'Hero Deffend : ' +str(self.hero.deff) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)  
                    self.statusHero = ''   
                    self.statusMons = 'HP : + '  +str(self.monsterType.hel)
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    print 'Hero Break : Break Fail' +'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                    self.statusHero = 'HP : - '  +str(self.monsterType.atk)  
                    self.statusMons = ''
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Deffend : Deffend Fail'
                    self.statusHero = '' 
                    self.statusMons = 'HP : - ' +str(self.hero.brk)  
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                    self.statusHero = 'HP : - ' +str(self.monsterType.brk) 
                    self.statusMons = 'HP : - ' +str(self.hero.brk) 
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.brk-self.monsterType.hel)
                    print'Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                    self.statusHero = '' 
                    self.statusMons = 'HP : - ' +str(self.hero.brk-self.monsterType.hel)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= (self.monsterType.atk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                    self.statusHero = 'HP : - ' +str(self.monsterType.atk-self.hero.hel)
                    self.statusMons = ''
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 1 :
                    self.hero.hp += self.hero.hel
                    print ' Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Deffend '
                    self.statusHero = 'HP : + ' +str(self.hero.hel)
                    self.statusMons = ''
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= (self.monsterType.brk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                    self.statusHero = 'HP : - ' +str(self.monsterType.brk-self.hero.hel)
                    self.statusMons = ''
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    self.hero.hp += self.hero.hel
                    print 'Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                    self.statusHero = 'HP : + ' +str(self.hero.hel)
                    self.statusMons = 'HP : + ' +str(self.monsterType.hel)

                if self.hero.hp > 300 :
                    self.hero.hp = 300
                if self.monster.hp > 150 :
                    self.monsterType.hp = 150
                if self.boss.hp > 300 :
                    self.boss.hp = 300

                print self.hero.name + ' HP : ' + str(self.hero.hp)
                print self.monsterType.name + '  HP : ' + str(self.monsterType.hp)


                if self.state == 1:
                    print "Monster HP %s/150"%(self.monsterType.hp)
  
                elif self.state == 2 :
                    print "Boss HP %s/300"%(self.monsterType.hp) 


                print  "Hero HP %s/300"%(self.hero.hp)
                
                #self.checkHPbar()
                self.turn+=1
                
        if self.state == 1 :
            if self.hero.hp <= 0 :
                print 'Monster Win \n----------- End Game ------------ ' 
                print '-------- Monster Win -----------'
                self.end()
            elif self.monster.hp <= 0 :
                self.state+=1
                self.bossburn = 1
                print ' Hero Win  \n----------- Next State (Boss)  ------------ ' 
                print '-------- Hero Win --------------'
                print '-------- Next State (Boss) ----------'
                self.monsterType = self.boss  
 
        elif self.state == 2 :
            if self.hero.hp <= 0 :
                #cmds.text("event",e=True, label = ' Boss Win \n----------- End Game ------------ ' )
                print '-------- Boss Win -----------'
                print '--------- End Game ----------'
                self.end()
            elif self.monsterType.hp <= 0 :
                print ' Hero Win  \n----------- End Game  ------------ ' 
                print '-------- Hero Win --------------'
            
                print '--------- End Game ----------'
                self.end()

    def end (self):
        print "END END END"
    def start(self):
        self.randomCardHero()
        self.imageHero()
        self.action()
'''
    def checkHPbar(self):

        if self.hero.hp <= 0 :
            self.hero.hp = 0
        if self.monster.hp <= 0 :
           self.monster.hp = 0
        if self.boss.hp <= 0 :
          self.boss.hp = 0

        self.rHero = 0.00
        self.gHero = 0.00
        self.rMonster = 0.00
        self.gMonster = 0.00
        self.rBoss = 0.00
        self.gBoss = 0.00
        self.Hpercent = self.hero.hp*100 /300.00
        self.Mpercent = (self.monster.hp/150.00) * 100.00
        self.Bpercent = (self.boss.hp/300.00) * 100.00

        self.gHero = self.Hpercent*1.00 /100.00
        self.rHero = 1.00 - self.gHero 
        self.gMonster = (self.Mpercent/100.00) * 1.00
        self.rMonster = 1.00 - self.gMonster 
        self.gBoss = (self.Bpercent/100.00) * 1.00
        self.rBoss = 1.00 - self.gBoss 
        print self.gMonster
        print self.rMonster
        print self.Mpercent

        if self.state == 1 :
            if self.monster.hp == 0 :
                pass
            elif self.monster.hp > 0 :
                pass
        elif self.state == 2 :
            if self.boss.hp == 0 :
                pass
            else :
                pass

        if self.hero.hp == 0 :
            pass
        else :
            pass


    def rematch(self):
        self.state = 1
        self.hero.hp = 300
        self.boss.hp = 300
        self.monster.hp = 150
        self.start()
        


    def buttonCard0(self,*agrs):
        if self.cardHero[0] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[0] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[0] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[0]=random.randint(0,3)
        self.action()
        
    def buttonCard1(self,*agrs):
        if self.cardHero[1] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[1] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[1] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[1]=random.randint(0,3)
        self.action()
        
    def buttonCard2(self,*agrs):
        if self.cardHero[2] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[2] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[2] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[2]=random.randint(0,3)
        self.action()

'''
