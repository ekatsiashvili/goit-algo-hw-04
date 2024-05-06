def merge_k_lists(lists):
    merged_list = []
    
    # Поки всі списки не порожні
    while any(lists):
        min_val = float('inf')
        min_index = None
        
        # Знаходимо найменше значення серед перших елементів кожного списку
        for i, lst in enumerate(lists):
            if lst and lst[0] < min_val:
                min_val = lst[0]
                min_index = i
        
        # Додаємо мінімальне значення до об'єднаного списку
        merged_list.append(min_val)
        
        # Видаляємо мінімальне значення з відповідного списку
        lists[min_index].pop(0)
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
