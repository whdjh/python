#κΈΈμ΄κ°  π μΈ λ¦¬μ€νΈμ ν¬ν¨λ ν­λͺ©λ€μ μ΅μκ°μ κ΅¬νλ λ κ°μ ν¨μλ₯Ό κ΅¬ννλΌ.
#λ°©λ² 1: κ° ν­λͺ©μ λ€λ₯Έ λͺ¨λ  ν­λͺ©κ³Ό λΉκ΅. μΌμ  μκ°λ³΅μ‘λλ  π(π)βπ(π2) .
#λ°©λ² 2:  π(π)βπ(π) , μ¦, μ ν μκ°λ³΅μ‘λλ₯Ό κ°λλ‘ κ΅¬νν  κ².
#μ°Έκ³ : https://www.youtube.com/watch?v=p0COF_m6H1c
#λ°©λ²1
def find_min1(list_min):
    min = list_min[0]
    for i in list_min:
        flag = 1
        for j in list_min:
            if i > j:
                flag = 0
        if flag == 1:
            min = i
    return min
            

#λ°©λ²2
def find_min2(list_min):
    min = list_min[0]
    n = len(list_min)
    for i in range(1, n):
        if(min > list_min[i]):
            min = list_min[i]
    return min