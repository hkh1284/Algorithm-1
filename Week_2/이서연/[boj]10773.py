'''
제로

- 문제 요약
수를 모두 받아 적은 후 그 수의 합을 출력하는 프로그램.
잘못된 수를 부르면 0을 외쳐서 가장 최근에 적은 수를 지운다.

- 입력 조건
첫째 줄에 정수 K가 주어짐.(1 <= K <= 100,000)
이후 K개의 줄에 정수가 1개씩 주어짐.
정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0"일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장.

- 출력 조건
최종적으로 적어낸 수의 합을 출력.
(2**31 -1보다 작거나 같은 정수)
'''
k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
