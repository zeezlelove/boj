re = {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5","blue":"6","violet":"7","grey":"8","white":"9"}
mul = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
li = []
for i in range(3):
    n = input()
    if i == 0:
        li.append(n)
    elif i == 1:
        li.append(n)
        result = re[li[0]]+re[li[1]]
    elif i == 2:
        print(int(result)*int(mul[int(re[n])]))
