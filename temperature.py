#攝氏('C)轉換為華氏('F)的程式
#請使用者輸入 攝氏溫度
#然後印出華氏溫度

Celsius = input('請問現在是攝氏幾度C :')
Celsius = int(Celsius)
Fahrenheit = Celsius * 9 / 5 + 32
Fahrenheit = str(Fahrenheit)
print('現在是華氏', Fahrenheit, '度')