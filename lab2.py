def min_eating_gorilla(piles, H):
        if not len(piles) <= H:
        raise ValueError

    def can_eat(K):
        hours = 0
        for x in piles:
            hours += (x + K - 1) // K

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_eat(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(min_eating_gorilla([3,6,7,11], 8))
print(min_eating_gorilla([30,11,23,4,20], 5))
print(min_eating_gorilla([30,11,23,4,20], 6))
