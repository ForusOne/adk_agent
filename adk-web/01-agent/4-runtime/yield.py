
import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        yield number  # 숫자를 반환하고 함수 실행을 일시 중지, 반환후 처리가 끝나고 다시 복귀할 때 실행 재개.
        print("After yield in count_up_to:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4 출력
    time.sleep(1)  # 1초 대기
    print("Yielded in loop:", num)  # Yielded: 0, Yielded: 1, ... 출력