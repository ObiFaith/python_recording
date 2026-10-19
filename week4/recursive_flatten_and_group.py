def flatten(nested: list):
    flatted_list = []

    for item in nested:
        if isinstance(item, list):
            flatted_list.extend(flatten(item))
        else:
            flatted_list.append(item)

    return flatted_list

print(flatten([1, [2, [3, [4]], 5]]))

def group_by(fruits: list[str], fn):
    groups = {}

    for fruit in fruits:
        key = fn(fruit)
        if fruit[0] == key:
            if groups.get(key, None) == None:
                groups[key] = [fruit]
            else:
                groups[key].append(fruit)

    return groups

print(group_by(["apple", "avocado", "banana"], lambda w: w[0]))

def combine(nested):
    return group_by(flatten(nested), lambda w: w[0])

print(combine([["apple", "avocado"], ["banana"], [["cherrry"]]]))
