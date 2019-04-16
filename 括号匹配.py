def process(s):
    temp_str = []
    open_operator = ['(', '[', '{']
    combine_operator = ['()', '[]', '{}']

    for cha in s:
        if cha in open_operator:
            temp_str.append(cha)
        else:
            if not temp_str:
                return False
            temp_cha = temp_str.pop() + cha
            if temp_cha not in combine_operator:
                return False
    if not temp_str:
        return True
    else:
        return False

print(process('[[{}]]'))