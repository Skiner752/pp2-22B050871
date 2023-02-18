from datetime import datetime
# 1 
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=5)
# print(tday - tdelta)


# 2
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=1)
# yday = tday - tdelta
# tomday = tday + tdelta
# print(yday)
# print(tday)
# print(tomday)     


# 3 
# time = datetime(2023 , 2 , 15 , 4 , 5 , 6 , 23533)
# time_no_micro = time.replace(microsecond = 0)
# print(time_no_micro)
 


# 4 
# tday = datetime(2023, 2, 15, 4, 6, 5, 123456)
# tday_only_micro = tday.replace(year = 1 , month = 1 , day = 1 , hour = 0 , minute = 0 , second = 0)
# yday = datetime(2023, 2, 15, 4, 6, 5, 56)
# yday_only_micro = yday.replace(year = 1 , month = 1 , day = 1 , hour = 0 , minute = 0 , second = 0)
# print(tday_only_micro - yday_only_micro)

