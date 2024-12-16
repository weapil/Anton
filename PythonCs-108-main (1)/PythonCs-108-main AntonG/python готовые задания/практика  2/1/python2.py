import statistics

def analyze_list(lst):
    analysis = {
        'max': max(lst),
        'min': min(lst),
        'avg': sum(lst) / len(lst),
        'med': statistics.median(lst)
    }
    return analysis
test_list = [59, 56, 56, 66, 15, 9, 84, 99, 67, 76]
analysis_result = analyze_list(test_list)
print("Список:", test_list)
print("Анализ списка:", analysis_result)
