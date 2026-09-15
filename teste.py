num= int(input("Agora Digite um número para ter sua piramide: ")) multiplier = 1
while (num > 0):
    num2 =((num+multiplier) - num)
    num3 = (2*num2)-1
    print (" "*num,"*"*num3, " "*num)
    num = num - 1
    multiplier= multiplier +1
