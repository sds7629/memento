# 1번 문제 x만큼 간격이 있는 n개의 숫자
from typing import Sequence


def solution1(x, n) -> Sequence[int]:
    return [x * (i + 1) for i in range(n)]


print(solution1(2, 5))
print(solution1(4, 3))
print(solution1(-4, 2))


# 핸드폰 번호 가리기
def solution2(phone_number) -> str:
    back_number = phone_number[-4:]
    return ("*" * (len(phone_number) - 4)) + back_number


print(solution2("01033334444"))
print(solution2("027778888"))


## test commit
## test commit 2
## feature test commit - 1
## dev commit - 1
## feature test commit - 2
