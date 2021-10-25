h = int(input("평균값을 구할 때의 입력받고 싶은 무게 값 수 : "))

s = int(input("기준이 되는 편심의 무게값(g) : "))

weights = []
for _ in range(h):
    n = (map(int, input().split("\n")))
    weights.append(*list(n))

total = sum(weights)

ave_weight = (total // h)

to_one_gram = ave_weight // s

# print(total)
# print(ave_weight)
print("hx.set_reference_unit()에 넣어줄 값:", to_one_gram)

