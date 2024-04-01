def join_list(items_list):
    if len(items_list) == 0:
        return "There is no items in the list"
    elif len(items_list) == 1:
        return ' '.join(items_list)
    else:    
        last_item = items_list.pop()
        final_str = f"{', '.join(items_list)} and {last_item}"
        return  final_str




spam = ['apples', 'bananas', 'tofu', 'cats']

prueba = join_list(spam)
print(prueba)