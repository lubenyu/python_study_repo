from matplotlib import pyplot as plt 
import numpy as np

'''1.简单绘制
    def scatter(
        x, y, s=None, c=None, marker=None, cmap=None, norm=None,
        vmin=None, vmax=None, alpha=None, linewidths=None,
        verts=cbook.deprecation._deprecated_parameter,
        edgecolors=None, *, plotnonfinite=False, data=None, **kwargs):
    参数1:x表示x轴的大小,可以传入数组来表示一组点的x坐标
    参数2:y,与x同理
    参数3:控制点的大小
'''
# plt.scatter(2,4,s=300)


'''2.修改标签(xlabel,ylabel,title)和线条粗细
'''
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.title("Square Numbers",fontsize=24)

plt.tick_params(labelsize=9)

'''3.绘制一系列点
    这个时候就需要传入x和y数量对于的数组(类数组)了
'''
# x = np.arange(1,6)
# y = x*x
# plt.scatter(x,y,color="red",s=100)


'''4.自动计算数据
    可以使用列表生成器
'''
# x = list(range(1,1001))
# y = [i**2 for i in x]
# plt.scatter(x,y,s=30)
# plt.show()


'''5.平滑连着的点的轮廓
'''
x = list(range(1,1001))
y = [i**2 for i in x]
# color关键字参数自定义颜色
# edgecolors关键字参数平滑连着的点的轮廓
plt.scatter(x,y,edgecolors="none",color="red",s=30)


'''6.颜色映射
'''















# 设置每个轴的取之范围列表，【x起始值，x结束值，y起始值，y结束值】
plt.axis([0,1100,0,1100000])
plt.show()