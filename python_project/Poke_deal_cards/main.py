from poke import Poke
from Hand import Hand
from Card import Card


if __name__ == "__main__":
    print("这是一个面向对象的发牌程序")
    player = [Hand(),Hand(),Hand(),Hand()]
    
    # 创建扑克对象
    poke = Poke()
    
    # 生成扑克
    poke.populate()
    
    # 洗牌
    poke.shuffle()
    
    # 发牌
    poke.deal(player)
    
    for i in range(4):
        print("牌手"+str(i)+"\t"+":")
        print(player[i])
        print("\n")
    



