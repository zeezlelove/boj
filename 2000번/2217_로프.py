"""
문제
N(1≤N≤100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다. 단, 각각의 로프는 한 개씩만 존재한다.

입력
첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1
2
10
15
예제 출력 1
20
"""
n = int(input())
a = [int(input()) for i in range(n)]
def main(n):
    a.sort(reverse=True)
    if n == 1:
        return a[0]
    if n == 2:
        return min(a)*len(a)
    else:
        compare = []
        c = 0
        for i in range(n):
            if i == 0:
                compare.append(a[i])
                c = a[i]
            else:
                compare.append(a[i])
                tmp = a[i]*len(compare)
                if c < tmp:
                    c = tmp
        return c
print(main(n))
'''
한개일경우:
로프가 한개면 있는중량하나를 출력
두개일경우:
로프가 두개면 제일작은 로프의힘*2
왜그럴까??
문제에 다음 조건이 존재하기 때문이다.
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
중량이 20 일때 로프 두개를 사용하면 한 로프당 걸리는 중량은 10 이다.
최대중량이 10, 12 의 로프 두개가 있을때 최대 중량이 12인 로프가 아무리 10보다 더 들 수 있어도 그 이상의 무게를 들게 되면 최대 중량이 10인 로프는 끊어지게 된다.
w = min( 병렬 연결된 로프의 중량 ) * 병렬 연결된 로프의 수
위의 식을 이용해서 예시로 주어진 10과 15의 로프 두개가 들 수 있는 최대 중량은 10 * 2 가 되므로 20이 된다.
여러개일경우:
testcase:
N:5/35 33 30 20 12
1)  중량 35 로프가 꺼내지고 최대 중량은 35
2) 중량 33 로프랑 병렬로 연결 되면서 최대 중량은 66
3) 중량 30 로프가 꺼내지고 먼저 꺼내진 35, 33 로프랑 병렬 연결 되면서 30 * 3 해서 최대 중량은 90
4) 중량 20 로프가 꺼내지고 먼저 꺼내진 35, 33, 30 로프랑 병렬 연결 되면서 20 * 4 해서 최대 중량은 80
5) 중량 12 로프가 꺼내지고 먼저 꺼내진 35, 33, 30, 20 로프랑 병렬 연결 되면서 12 * 5 해서 최대 중량은 60
'''
