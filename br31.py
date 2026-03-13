# 베스킨라빈스 31 간단 버전
import random

number = 0
print("게임을 시작합니다!")

while number < 31:
    # 사용자 입력
    pick = int(input("1~3 사이의 숫자를 입력하세요: "))
    number += pick
    print(f"현재 숫자: {number}")
    
    if number >= 31:
        print("당신이 패배했습니다!")
        break
        