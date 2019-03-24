# 功能：实现类似matlab中的，动态绘图，随着迭代更新图像
# 关键：plt.clf()和plt.pause(0.01)的配合使用


for 或 while循环开始：
	...
	plt.clf() # 清除所有轴，但是窗口打开，这样它可以被重复使用
	plt.scatter(Xs, Ys, c='r')
	plot_func()
	plt.show()
	plt.pause(0.01)  #每次绘图后暂停0.01秒
	...
循环结束
