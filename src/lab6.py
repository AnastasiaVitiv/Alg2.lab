def is_boy(person):
    return person % 2 == 1


def dfs(person, graph, visited, tribe):
    visited.add(person)
    tribe.append(person)
    for neighbor in graph.get(person, []):
        if neighbor not in visited:
            dfs(neighbor, graph, visited, tribe)


def count_pairs(n, pairs):
    graph = {}
    all_people = set()

    for a, b in pairs:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
        all_people.add(a)
        all_people.add(b)

    visited = set()
    tribes = []

    for person in all_people:
        if person not in visited:
            tribe = []
            dfs(person, graph, visited, tribe)
            tribes.append(tribe)

    tribe_boys = []
    tribe_girls = []
    total_boys = []
    total_girls = []

    for tribe in tribes:
        boys = [p for p in tribe if is_boy(p)]
        girls = [p for p in tribe if not is_boy(p)]
        tribe_boys.append(boys)
        tribe_girls.append(girls)
        total_boys.extend(boys)
        total_girls.extend(girls)

    result = 0
    combinations = []

    for i in range(len(tribes)):
        boys = tribe_boys[i]
        girls = tribe_girls[i]

        other_girls = [g for g in total_girls if g not in girls]
        other_boys = [b for b in total_boys if b not in boys]

        for b in boys:
            for g in other_girls:
                combinations.append((b, g))
                result += 1


    return result, combinations


with open('../input.txt', 'r', encoding='utf-8') as f:
    lines = f.read().strip().split('\n')
    n = int(lines[0])
    pairs = [tuple(map(int, line.strip().split())) for line in lines[1:n+1]]

result, combinations = count_pairs(n, pairs)

with open('../output.txt', 'w', encoding='utf-8') as f:
    f.write(
        f"Кількість можливих комбінацій: {result}\n"
    )
    if combinations:
        formatted = ', '.join(f'{b}/{g}' for b, g in combinations)
        f.write(f"(Можливі пари - {formatted})\n")
