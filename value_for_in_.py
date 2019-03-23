# 1. 求列表的最小值min()就可以搞定
# 2. for...in... 真是个好东西

# 下面的例子是自己在写轮盘赌选择方法时候遇到的

# 低效率方法
	# min_fit_value = fit_value[0]
    # for k in range(pop_size):
    #     if fit_value[k] < min_fit_value:
    #         min_fit_value = fit_value[k]  # 先找到当前种群最小fit_value

    # if min_fit_value < 0:
    #     for k in range(pop_size):
    #         fit_value[k] = fit_value[k] + (-1)*min_fit_value
    # #
	
# (高效方法只需要两行) 先找到当前种群最小fit_value
    min_fit_value = min(fit_value)
    fit_value = [(i - min_fit_value) for i in fit_value]