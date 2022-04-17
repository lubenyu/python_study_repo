# poke类代表一幅牌，可以看作52张牌的牌手，继承Hand类
from Hand import Hand
from Card import Card
import random
class Poke(Hand):
    
    def __init__(self):
        super().__init__() 
    
    # 生成52张牌
    def populate(self):
        for suit in Card.Suit:
            for facename in  Card.FaceNum:
                self.cards.append(Card(facename,suit))
        
    # 洗牌，打乱顺序
    def shuffle(self):
        random.shuffle(self.cards)
        
    # 发牌动作
    def deal(self,hands,per_hand=13):
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    card = self.cards.pop()
                    self.give_card(card,hand)
                else:
                    print("牌发完了！")