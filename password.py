password = 'a123456'
i = 3 #剩餘機會
while True:
	code = input('請輸入密碼: ')
	if code == password:
		print('登入成功')
		break #逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤!剩', i, '次機會') #i=創造變數
		if i == 0:
			print('沒機會了')
			break















