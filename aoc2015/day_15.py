from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split("\n")

    ingredients = defaultdict(dict)

    for line in lines:
        name, line = line.split(": ")
        line = line.split(", ")
        for prop in line:
            prop_name, value = prop.split(" ")
            value = int(value)
            ingredients[name][prop_name] = value

    def get_cookie_score(ingredients, teaspoons):

        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0

        for ingredient, properties in ingredients.items():
            capacity += teaspoons[ingredient] * properties["capacity"]
            durability += teaspoons[ingredient] * properties["durability"]
            flavor += teaspoons[ingredient] * properties["flavor"]
            texture += teaspoons[ingredient] * properties["texture"]
            calories += teaspoons[ingredient] * properties["calories"]

        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture), calories
    
    def get_teaspoon_combos(ingredients, teaspoons):
        curr = ingredients.pop(0)
        total_teaspoons = sum(teaspoons.values())
        teaspoon_combos = tuple()

        if len(ingredients) == 0:
            teaspoons[curr] = 100 - total_teaspoons
            return (teaspoons,)
        
        for i in range(100 - total_teaspoons):
            new_teaspoons = teaspoons.copy()
            new_teaspoons[curr] = i
            teaspoon_combos += get_teaspoon_combos(ingredients.copy(), new_teaspoons)
        return teaspoon_combos
    teaspoon_combos = get_teaspoon_combos(list(ingredients.keys()), {})

    max_cookie_score1 = 0
    max_cookie_score2 = 0
    for teaspoons in teaspoon_combos:
        cookie_score, calories = get_cookie_score(ingredients, teaspoons)
        max_cookie_score1 = max(max_cookie_score1, cookie_score)
        if calories == 500:
            max_cookie_score2 = max(max_cookie_score2, cookie_score)
    part1 = max_cookie_score1
    part2 = max_cookie_score2

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")