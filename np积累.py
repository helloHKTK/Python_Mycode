# ���ܣ�����numpy���õ��ĺ���

# 1. np.greater(A, B) �������ж� A > B ��true��false�б�

A = [1, 3, 5]
B = [2, 4, 6]
update_id = np.greater(A, B)  # �����ж� A > B ��true��false�б�
print(update_id)  # ���Ϊ[False False False]



# 2. ʹ��np.argmin()��np.argmax()�����Ҿ�����б�����ֵ����Сֵ��

fitness = [8, 2, 3, 1, 6]  # ����һ���б�
max_index = np.argmax(fitness)
min_index = np.argmin(fitness)

print('���ֵ���±� ' + str(max_index) + ' ��Сֵ���±� ' + str(min_index))
print('���ֵΪ:' + str(fitness[max_index]) + ' ��СֵΪ: ' + str(fitness[min_index]))


# 3. ʹ��np.maximum(X,Y)��np.minimum(X,Y) ��������С��0�Ļ����ĳ������ֵ�滻�����������ڱ߽紦��
     
	 # ��1:������X��С��0����,�滻Ϊ0
	 x = np.array([1, -2, 3, 18, 6])
	 x = np.maximum(x, 0)  # np.maximum(X,Y): X��Y ��λ�Ƚ�ȡ�����

	 # ��2:������X�д���15����,�滻Ϊ15
	 x = np.minimum(x, 15)