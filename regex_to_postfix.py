# Transformăm expresia regulată într-o expresie postfixată
# Algoritmul Shunting Yard

# Definim operatorii și ordinea lor de prioritate
operators = {
    '|': 1,  # SAU
    '.': 2,  # CONCATENARE
    '*': 3,  # REPETARE DE ZERO SAU MAI MULTE ORI
    '+': 3,  # REPETARE O DATĂ SAU DE MAI MULTE ORI
    '?': 3   # PREZENȚĂ OPȚIONALĂ
}

def insert_concatenation(regex):
    # Inserează operatorul de concatenare '.' în expresia regulată
    result = []
    
    for i in range(len(regex)):
        char1 = regex[i]
        result.append(char1)
        if i + 1 < len(regex):
            char2 = regex[i + 1]
            # Condiții pentru inserarea operatorului de concatenare:
            if (char1.isalnum() or char1 in ['*', '+', '?', ')']) and (char2.isalnum() or char2 == '('):
                result.append('.')
    return ''.join(result)

def regex_to_postfix(regex):
    stack, postfix = [], []     
    regex = insert_concatenation(regex)  # Inserăm operatorul de concatenare
    
    for char in regex:
        if char == '(':
            stack.append(char) 
             
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # Scoate operatorii din stivă până la (
            stack.pop()  # Scoate (
                
        elif char in operators:
            while (stack and operators.get(stack[-1], 0) >= operators.get(char, 0)):
                postfix.append(stack.pop())  # Scoate operatorii din stivă cu prioritate mai mare
            stack.append(char)  # Adaugă operatorul curent la stivă
        
        else:
            postfix.append(char)  # Adaugă caracterul la postfix

    while stack:
        postfix.append(stack.pop())  # Scoate toți operatorii rămași din stivă

    return ''.join(postfix) 