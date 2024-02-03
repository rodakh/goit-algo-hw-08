import heapq


def minimize_costs(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


cables = [8, 4, 6, 12]
print(f"Мінімальні загальні витрати для об'єднання кабелів: {minimize_costs(cables)}")
