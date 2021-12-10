number_final = 0
string_final = ""
while number_final < 100:
    number_final += 1
    last_number_final = number_final % 10
    if last_number_final == 1 and number_final != 11:
        string_final = "процент"
    elif (last_number_final >= 2 and last_number_final < 5) and (number_final < 10 or number_final > 20):
        string_final = "процента"
    else:
        string_final = "процентов"
    print(number_final,string_final)
