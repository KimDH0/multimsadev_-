hong1 = {'국어':95,'영어':90,'수학':80,'과학':50}
hong2 = {'국어':100,'영어':50,'수학':90,'과학':90}
hong3 = {'국어':99,'영어':60,'수학':100,'과학':40}
hong4 = {'국어':55,'영어':80,'수학':80,'과학':60}

hong1_sum = sum(hong1.values())
hong1_avg = sum(hong1.values())/len(hong1)

hong2_sum = sum(hong2.values())
hong2_avg = sum(hong2.values())/len(hong2)

hong3_sum = sum(hong3.values())
hong3_avg = sum(hong3.values())/len(hong3)

hong4_sum = sum(hong4.values())
hong4_avg = sum(hong4.values())/len(hong4)

all_sum = hong1_sum + hong2_sum + hong3_sum + hong4_sum
all_avg = all_sum/len(hong1)+len(hong2)+len(hong3)+len(hong4)

print(hong1_sum, hong2_sum, hong3_sum, hong4_sum) #개인 합계
print(hong1_avg, hong2_avg, hong3_avg, hong4_avg) #개인 평균
print(all_sum) #전체 합계
print(all_avg) #전체 평균
#무지성 방법