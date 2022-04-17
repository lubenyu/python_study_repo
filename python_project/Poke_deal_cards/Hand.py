# 定义一个类，代表一个玩家手里拿的牌
'''
    Hand有 1.增加牌 
           2.清空牌
           3.把一张牌给其他牌手 
'''
from Card import Card

class Hand(object):
    # 将玩家的所有牌都用一个列表存起来
    def __init__(self):
        self.cards = []
    
    # 显示出该牌手的所有牌
    def __str__(self):
        if self.cards:
            ret = ""
            for card in self.cards:
                ret += str(card)+"\t"
        else:
            ret = "无牌"
        return ret
            
    # 增加手牌
    def add_card(self,card:Card):
        self.cards.append(card)
    
    # 清空手牌
    def clear_card(self):
        self.cards.clear
    
    # 给手牌给别人
    def give_card(self,card,other_hand):
        # self.cards.remove(card)
        other_hand.add_card(card)
   
# hand = Hand()
# card_1 = Card("K","红桃")
# card_2 = Card("4","方块")
# hand.add_card(card_1)
# hand.add_card(card_2)
# print(hand.cards.pop())