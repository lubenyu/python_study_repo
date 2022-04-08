from matplotlib import pyplot as plt 
import numpy as np

squares = [1,4,9,16,25]
''' 1.简单绘制
    当plot默认一个参数时,这个参数默认为Y,并且X默认为下标0~N-1。
    plt.plot(squares)相当于：
        x = [0,1,2,3,4]
        plt.plot(x,squares) 
    
    plot函数参数默认是数组或者类数组,列表会先转化为数组
'''
# plt.plot(squares)
x = [1,2,3,4,5]
plt.plot(x,squares,linewidth=5)

'''2.修改标签(xlabel,ylabel,title)和线条粗细

    plt.xlabel("Value",fontsize=14)
    第一个参数是标签字符串，后面有关键字参数**kwargs,其中匹配的关键字参数在 Text 类属性中
    def xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    
    plt.tick_params(labelsize=14)
    第一个参数是包括的轴，关键字参数列表在下面
    def tick_params(axis='both', **kwargs):
        ['size', 'width', 'color', 'tickdir', 'pad', 'labelsize', 'labelcolor', 'zorder', 'gridOn', 
        'tick1On', 'tick2On', 'label1On', 'label2On', 'length', 'direction', 'left', 'bottom', 'right', 
        'top', 'labelleft', 'labelbottom', 'labelright', 'labeltop', 'labelrotation', 'grid_agg_filter', 
        'grid_alpha', 'grid_animated', 'grid_antialiased', 'grid_clip_box', 'grid_clip_on', 'grid_clip_path',
        'grid_color', 'grid_contains', 'grid_dash_capstyle', 'grid_dash_joinstyle', 'grid_dashes', 'grid_data', 
        'grid_drawstyle', 'grid_figure', 'grid_fillstyle', 'grid_gid', 'grid_in_layout', 'grid_label', 'grid_linestyle', 
        'grid_linewidth', 'grid_marker', 'grid_markeredgecolor', 'grid_markeredgewidth', 'grid_markerfacecolor', 
        'grid_markerfacecoloralt', 'grid_markersize', 'grid_markevery', 'grid_path_effects', 'grid_picker',
        'grid_pickradius', 'grid_rasterized', 'grid_sketch_params', 'grid_snap', 'grid_solid_capstyle', 
        'grid_solid_joinstyle', 'grid_transform', 'grid_url', 'grid_visible', 'grid_xdata', 'grid_ydata', 
        'grid_zorder', 'grid_aa', 'grid_c', 'grid_ds', 'grid_ls', 'grid_lw', 'grid_mec', 'grid_mew', 'grid_mfc', 
        'grid_mfcalt', 'grid_ms']
'''
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.title("Square Numbers",fontsize=24)

plt.tick_params(labelsize=9)

plt.show()