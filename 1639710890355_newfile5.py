a=int(input())
hour=(int(a/3600))
min=int((a-hour*3600)/60)
sec=int(a-hour*3600-min*60)
print(hour,"часы", min,"минуты", sec,"секунды")