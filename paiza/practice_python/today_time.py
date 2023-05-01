# 日本時間取得、特定時間指定方法

from datetime import datetime, timedelta, timezone

today = datetime.now()

# 日本時間を表示するにはtimedeltaとtimezoneが必要
jst = timezone(timedelta(hours=9))

japan_today = datetime.now(jst)
print(japan_today)

print(japan_today.year)
print(japan_today.month)
print(japan_today.day)

# 日時を指定したい時はstrptimeを使う。
day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)
# ％Y：年
# ％m：月
# ％d：日
# ％H：時
# ％M：分
# ％S：秒