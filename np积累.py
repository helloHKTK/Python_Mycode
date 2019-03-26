# 功能：积累numpy中用到的函数

# 1. np.greater(A, B) 【返回判断 A > B 的true或false列表】

A = [1, 3, 5]
B = [2, 4, 6]
update_id = np.greater(A, B)  # 返回判断 A > B 的true或false列表
print(update_id)  # 结果为[False False False]



# 2. 使用np.argmin()或np.argmax()【查找矩阵或列表的最大值或最小值】

fitness = [8, 2, 3, 1, 6]  # 这是一个列表
max_index = np.argmax(fitness)
min_index = np.argmin(fitness)

print('最大值的下标 ' + str(max_index) + ' 最小值的下标 ' + str(min_index))
print('最大值为:' + str(fitness[max_index]) + ' 最小值为: ' + str(fitness[min_index]))


# 3. 使用np.maximum(X,Y)或np.minimum(X,Y) 将矩阵中小于0的或大于某个数的值替换掉【常常用于边界处理】
     
	 # 例1:将矩阵X中小于0的数,替换为0
	 x = np.array([1, -2, 3, 18, 6])
	 x = np.maximum(x, 0)  # np.maximum(X,Y): X与Y 逐位比较取其大者

	 # 例2:将矩阵X中大于15的数,替换为15
	 x = np.minimum(x, 15)