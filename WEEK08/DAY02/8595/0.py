# from sys import stdin
# n =int(stdin.readline().strip()) # (1 ≤ n ≤ 5,000,000)
# inpt = list(stdin.readline().strip())
# ans = ''
# for hid_num in inpt:
#      ans=ans+hid_num  if hid_num.isnumeric()else ans+' '
# print(sum(list(map(int,ans.split()))))

# 시간초과 ㅜㅜ 
# https://buganddog.tistory.com/17 참고
n = int(input())
word = input()
number = [str(i) for i in range(10)]
def hidden_n():
    place_v = 1
    ans = 0 
    temp = 0 
    for i in range(n):
        i = -i -1 
        if word[i] in number:
            temp += int(word[i])*place_v
            place_v=place_v*10
            
        if i ==-n or word[i] not in number: 
            if place_v >= 10**7: #숫자가 6자리 이상이라면 종료, 
                place_v = 1
                temp = 0
                continue 
            ans += temp 
            place_v = 1
            temp = 0 
    return ans
    
print(hidden_n())
