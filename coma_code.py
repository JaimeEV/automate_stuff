def join_list(items_list):
    if len(items_list) == 0:
        return "There is no items in the list"
    elif len(items_list) == 1:
        return ' '.join(items_list)
    else:    
        last_item = str(items_list.pop())
        items_list_str = [str(i) for i in items_list]
        final_str = f"{', '.join(items_list_str)} and {last_item}"
        return  final_str




spam = ['apples', 'bananas', 'tofu', 'cats', True, 13]

prueba = join_list(spam)
print(prueba)