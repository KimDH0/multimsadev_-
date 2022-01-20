hong1 = {'국어':95,'영어':90,'수학':80,'과학':50}
hong2 = {'국어':100,'영어':50,'수학':90,'과학':90}
hong3 = {'국어':99,'영어':60,'수학':100,'과학':40}
hong4 = {'국어':55,'영어':80,'수학':80,'과학':60}

#리스트로 변환
h1 = list(hong1.values())
h2 = list(hong2.values())
h3 = list(hong3.values())
h4 = list(hong4.values())

i=0
h1_sum = 0
while i <= len(h1):
    h1_sum += h1[i]
    i += 1
    
    if i == len(h1):
        break

i=0
h2_sum = 0
while i <= len(h2):
    h2_sum += h2[i]
    i += 1
    
    if i == len(h2):
        break

i=0
h3_sum = 0
while i <= len(h3):
    h3_sum += h3[i]
    i += 1
    
    if i == len(h3):
        break

i=0
h4_sum = 0
while i <= len(h4):
    h4_sum += h4[i]
    i += 1
    
    if i == len(h4):
        break
    

h1_avg = h1_sum/len(h1)
h2_avg = h2_sum/len(h2)
h3_avg = h3_sum/len(h3)
h4_avg = h4_sum/len(h4)    

h_all = h1_sum + h2_sum + h3_sum + h4_sum
h_avg = h_all/len(h1)+len(h2)+len(h3)+len(h4)
    
print(h1_sum, h2_sum, h3_sum, h4_sum) #개인 합계
print(h1_avg, h2_avg, h3_avg, h4_avg) #개인 평균
print(h_all) #전체 합계
print(h_avg) #전체 평균
#while문+if문 활용
