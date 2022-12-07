with open('file.prod') as f:
    code = f.read()


code_len = 20 # DE AICI SE SCHIMBA LUNGIMEA SIRULUI

ans = code_len-1
key = 0
for i in range(len(code)-4):
    ans += 1
    cuvant = []
    for j in range(code_len):
        cuvant.append(code[i+j])
    if cuvant[-1] == '\n':
        print("NU EXISTA!")
        break
    for k in range(len(cuvant)-1):
        #print("verific daca", cuvant[k], 'in', cuvant[k+1:len(cuvant)])
        if cuvant[k] in cuvant[k+1:len(cuvant)]:
            #print("GRESALA")
            break
    else:
        key = cuvant
        break

        
    print(cuvant)
if key != 0:
    print(ans, key)