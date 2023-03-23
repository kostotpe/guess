# 產生一個隨機整數1-100 不要印出
# 讓使用者重複輸入數字去猜
# 猜對印出'恭喜你猜對了!'
# 猜錯要告訴他 比答案大/小
# 延伸 可顯示猜測次數

import random

r = random.randint(1, 100)
g = r
count = 0
while True:
    count += 1 # count = count + 1 快寫法
    g = input('請猜正確數字是多少(範圍1~100): ')
    g = int(g)
    if g == r:
        print('恭喜猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif g > r:
        print('答案小於', g)
    elif g < r:
        print('答案大於', g)
    print('這是你猜的第', count, '次')
