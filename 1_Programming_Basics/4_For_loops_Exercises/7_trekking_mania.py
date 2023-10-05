nr_groups = int(input())
musala, monblan, kilimandjaro, k2, everest = 0, 0, 0, 0, 0
total_trekkers = 0

for _ in range(nr_groups):
    group_size = int(input())

    if group_size <= 5:
        musala += group_size
    elif 6 <= group_size <= 12:
        monblan += group_size
    elif 13 <= group_size <= 25:
        kilimandjaro += group_size
    elif 26 <= group_size <= 40:
        k2 += group_size
    elif group_size >= 41:
        everest += group_size

    total_trekkers += group_size

percentage_musala = musala / total_trekkers * 100 #musala /= total_trekkers / 100 - taka ne vkarvame novi promenlivi;
# deleno na 100 zashtoto musala se deli na celiq izraz sled ravnoto i ako e po sto tazi stotachka ostava v delitelq
percentage_monblan = monblan / total_trekkers * 100
percentage_kilimandjaro = kilimandjaro / total_trekkers * 100
percentage_k2 = k2 / total_trekkers * 100
percentage_everest = everest / total_trekkers * 100

print(f"{percentage_musala:.2f}%")
print(f"{percentage_monblan:.2f}%")
print(f"{percentage_kilimandjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")