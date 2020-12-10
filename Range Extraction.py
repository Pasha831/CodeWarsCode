def solution(numbers):
    a = numbers
    temp = [] # для кратковременного внесения повторяющихся переменных
    counter = 0 # если счётчик >= 2 - то добавляем в строку, нет - не добавляем
    result = '' # our result, like '-6,-3-1,3-5,7-11,14,15,17-20'

    for i in range(len(a) - 1):
        if (a[i] != a[i + 1] - 1) and (a[i] != a[i - 1] + 1):  # -6 != -4, для чисел, которые не имеют пары совсем
            result += str(a[i]) + ','
        
        else:
            if a[i] == a[i + 1] - 1:  # -3 и -2 и -1 и 0 и 1
                #print(str(a[i]) + ' ? ' + str(a[i + 1]) + ' - 1')
                counter += 1
                temp.append(a[i])

                if i == len(a) - 2:

                    if counter >= 2:
                        temp.append(a[i] + 1)
                        string = str(min(temp)) + '-' + str(max(temp))  # '-3' + '-' + '1' 
                        result += string  # => '-3-1'
                        temp.clear()
                        counter = 0
                
                    else:
                        for j in range(len(temp)):
                            result += str(temp[j]) + ','
                        temp.clear()
                        counter = 0

            if a[i] != a[i + 1] - 1:

                if counter >= 2:
                    temp.append(a[i])
                    string = str(min(temp)) + '-' + str(max(temp)) + ','  # '-3' + '-' + '1' 
                    result += string  # => '-3-1'
                    temp.clear()
                    counter = 0
                
                else:
                    temp.append(a[i])
                    for j in range(len(temp)):
                        result += str(temp[j]) + ','
                    temp.clear()
                    counter = 0


    if result[len(result) - 1] == ',':
        result += str(a[len(a) - 1])
    return result

numbers = [1,3,4,5,7,8,9,10,14]
print(solution(numbers))