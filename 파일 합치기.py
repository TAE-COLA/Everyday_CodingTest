# 파일을 합치는 데 소요되는 시간은 두 파일의 크기의 합과 같다.
# 파일의 크기들이 나열될 떄, 파일을 전부 합칠 수 있는 최소 비용을 구하시오.
def pick_smallest(files, merged):
    if len(files) == 0:
        return merged.pop()
    elif len(merged) == 0:
        return files.pop()

    f = files.pop()
    m = merged.pop()
    if f < m:
        merged.append(m)
        return f
    else:
        files.append(f)
        return m


def solution(n, files):
    answer = 0

    files.sort(reverse=True)
    merged = []

    while len(files) + len(merged) > 1:
        cost = pick_smallest(files, merged) + pick_smallest(files, merged)
        answer += cost
        inserted = False
        for i in range(len(merged)):
            if cost >= merged[i]:
                merged.insert(cost, i)
                break
        if not inserted:
            merged.append(cost)
        print(merged)

    return answer


t = int(input())
for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    print(solution(n, files))


# 2
# 4
# 40 30 30 50
# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
