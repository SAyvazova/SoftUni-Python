nr_words = int(input())
synonyms_dict = {}
for _ in range(nr_words):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = [synonym]
    else:
        synonyms_dict[word].append(synonym)

for word, synonym_list in synonyms_dict.items():
    print(f"{word} - {', '.join(synonym_list)}")

