num=list()
for i in range(1,100):
    num.append(i)

muti=list()
for i in num:
    if i < 5 or i > 90:
        muti.append(i*10)
    else :
        muti.append(i*0.1)
#print(len(muti))
print(num[0])

# R
#for(i in x){if(x[i]<5 or x[i]>90){s[i]=x[i]*10}else{s[i]=x[i]*0.1}}