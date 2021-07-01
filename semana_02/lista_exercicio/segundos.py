seconds = input("Por favor, entre com o número de segundos que deseja converter: ")
seconds_float = float(seconds)
a = seconds_float // 86400
hours_left = seconds_float % 86400
b = hours_left // 3600
minuts_left = hours_left % 3600
c = minuts_left // 60
d = minuts_left % 60
print(int(a), "dias,", int(b), "horas,", int(c), "minutos e", int(d), "segundos.")
