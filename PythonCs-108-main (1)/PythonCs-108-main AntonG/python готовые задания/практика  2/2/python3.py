def reverse_words(lst):
    return lst[::-1]
def sort_words_by_length(lst):
    return sorted(lst, key=len)
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
reversed_words = reverse_words(words_list)
sorted_words = sort_words_by_length(words_list)
print("Исходный список слов:", words_list)
print("Список в обратном порядке:", reversed_words)
print("Список, отсортированный по длине:", sorted_words)
