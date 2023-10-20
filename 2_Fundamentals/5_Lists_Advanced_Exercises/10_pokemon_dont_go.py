distances_to_pokemons = [int(distance) for distance in input().split()]
total_sum_removed_elements = 0
while len(distances_to_pokemons) > 0:
    index = int(input())
    if index < 0:
        removed_element = distances_to_pokemons.pop(0)
        distances_to_pokemons.insert(0, distances_to_pokemons[-1])
    elif index >= len(distances_to_pokemons):
        removed_element = distances_to_pokemons.pop(-1)
        distances_to_pokemons.append(distances_to_pokemons[0])
    else:
        removed_element = distances_to_pokemons.pop(index)

    total_sum_removed_elements += removed_element
    distances_to_pokemons = [distance + removed_element if distance <= removed_element else distance - removed_element \
                             for distance in distances_to_pokemons]

print(total_sum_removed_elements)
