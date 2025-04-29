# Algoritmul lui Thompson
        
def regex_to_nfa(regex):
    state_number = 0        #numără stările create
    nfa_stack = []          #construim pas cu pas fragmente de NFA  
    alphabet = []           #lista simbolurilor din alfabetul expresiei
    
    for char in regex:
        if char == '*':
            # Se creează două stări noi: new_start și new_end
            # Se leagă new_start de începutul NFA-ului și de new_end
            # Se leagă new_end de începutul NFA-ului și de new_end
            start1, end1, transitions1 = nfa_stack.pop()
            new_start = state_number
            state_number += 1
            new_end = state_number
            state_number += 1
            transitions = {**transitions1}
            transitions.setdefault(new_start, {}).setdefault(None, []).extend([start1, new_end])
            transitions.setdefault(end1, {}).setdefault(None, []).extend([start1, new_end])
            nfa_stack.append((new_start, new_end, transitions))
            
        elif char == '+':
            # Se creează două stări noi: new_start și new_end
            # Se leagă new_start de începutul NFA-ului
            # Se leagă new_end de începutul NFA-ului și de new_end
            start1, end1, transitions1 = nfa_stack.pop()
            new_start = state_number
            state_number += 1
            new_end = state_number
            state_number += 1
            transitions = {**transitions1}
            transitions.setdefault(new_start, {}).setdefault(None, []).append(start1)
            transitions.setdefault(end1, {}).setdefault(None, []).extend([start1, new_end])
            nfa_stack.append((new_start, new_end, transitions))
            
        elif char == '?':
            # Se creează două stări noi: new_start și new_end
            # Se leagă new_start de începutul NFA-ului și de new_end
            start1, end1, transitions1 = nfa_stack.pop()
            new_start = state_number
            state_number += 1
            new_end = state_number
            state_number += 1
            transitions = {**transitions1}
            transitions.setdefault(new_start, {}).setdefault(None, []).extend([start1, new_end])
            transitions.setdefault(end1, {}).setdefault(None, []).append(new_end)
            nfa_stack.append((new_start, new_end, transitions))
            
        elif char == '.':
            # Finalul primului NFA are o lambda-tranziție către începutul celui de-al doilea NFA 
            start2, end2, transitions2 = nfa_stack.pop()
            start1, end1, transitions1 = nfa_stack.pop()
            transitions = {**transitions1}
            for state, edges in transitions2.items():
                for symbol, destinations in edges.items():
                    for dest in destinations:
                        transitions.setdefault(state, {}).setdefault(symbol, []).append(dest)
            transitions.setdefault(end1, {}).setdefault(None, []).append(start2)
            nfa_stack.append((start1, end2, transitions))
            
        elif char == '|':
            # Se creează două stări noi: new_start și new_end
            # Se leagă new_start de începuturile celor două NFA-uri existente
            # și se leagă finalurile acestora de new_end
            start2, end2, transitions2 = nfa_stack.pop()
            start1, end1, transitions1 = nfa_stack.pop()
            new_start = state_number
            state_number += 1
            new_end = state_number
            state_number += 1
            transitions = {**transitions1}
            for state, edges in transitions2.items():
                for symbol, destinations in edges.items():
                    for dest in destinations:
                        transitions.setdefault(state, {}).setdefault(symbol, []).append(dest)
            transitions.setdefault(new_start, {}).setdefault(None, []).extend([start1, start2])
            transitions.setdefault(end1, {}).setdefault(None, []).append(new_end)
            transitions.setdefault(end2, {}).setdefault(None, []).append(new_end)
            nfa_stack.append((new_start, new_end, transitions))
            
        else:
            # Se creează două stări noi: new_start și new_end
            # Se adaugă o tranziție de la start la end pe simbolul char
            start = state_number
            alphabet.append(char)
            state_number += 1
            end = state_number
            state_number += 1
            transitions = {start: {char: [end]}}
            nfa_stack.append((start, end, transitions))
            
    start, end, transitions = nfa_stack.pop()    
    return start, end, transitions, alphabet
