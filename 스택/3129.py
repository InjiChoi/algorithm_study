str_list = input()

def bracket_check(test_string):
    stack = []
    for i in test_string:
        if i == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                return 'bad'
    if len(stack)==0:
        return 'good'
    else:
        return 'bad'
        
print(bracket_check(str_list))