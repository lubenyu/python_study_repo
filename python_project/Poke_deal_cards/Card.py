# 定义一个控制一张牌的类
class Card(object):
    
    FaceNum = {'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
    Suit = {"黑桃","方块","梅花","红心"}
    
    # 默认初始化，初始化一张牌的基本要素：1.面值facename 2.花色suit 3.显示牌面（face_ons）默认显示 
    def __init__(self,facename,suit,face_up = True):   
        self.facename = facename
        self.suit = suit
        self.is_face_up = face_up

    # __str__方法，默认在 print（对象）时默认调用该对象的__str__方法
    def __str__(self) : # 判断是不是自己，对自己显示正面，对别人显示背面
        if self.is_face_up:
            ret = self.suit + self.facename
        else:
            ret = "XX"
        return ret

    def pic_order(self):    # 牌的顺序号
        if self.facename == "A":
            order = 1
        elif self.facename == "J":
            order = 11
        elif self.facename == "Q":
            order = 12
        elif self.facename == "K":
            order = 13
        else:
            order = int(self.facename)
        if self.suit == "梅花":
            Order = 1
        elif self.suit == "方块":
            Order = 2
        elif self.suit == "梅花":
            Order = 3
        else:
            Order = 4
        return (Order - 1)*13+order  # 返回牌的编号    
    
    # 定义翻牌方法
    def flip(self):     # 就是把正的反面，反的显示出来
        self.is_face_up = not self.is_face_up
       
            
         
# card_heitao_4 = Card('4',"黑桃")
# # card_fangkuai_5 = Card('5',"方块")

# # if card_fangkuai_5.facename > card_heitao_4.facename:
# #     print("5大于4")
# print(card_heitao_4)