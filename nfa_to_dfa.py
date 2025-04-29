# Se transofrmă NFA-ul în DFA utilizând algoritmul subset construction

def epsilon_closure(states, nfa_transitions):
    # Găsește toate stările la care se poate ajunge prin lambda-tranziții
    closure = set(states)
    stack = list(states)
    
    while stack:
        state = stack.pop()
        if state in nfa_transitions and None in nfa_transitions[state]:
            for next_state in nfa_transitions[state][None]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    return frozenset(closure)

def move(states, symbol, nfa_transitions):
    # Găsește toate stările la care putem ajunge citind simbolul respectiv din oricare stare
    next_states = set()
    for state in states:
        if state in nfa_transitions and symbol in nfa_transitions[state]:
            next_states.update(nfa_transitions[state][symbol])
    return frozenset(next_states)

def build_dfa(nfa_start, nfa_final_states, nfa_transitions, alphabet):
    # Construiește un DFA pornind de la un NFA
    alphabet = [s for s in alphabet if s is not None]
    initial_closure = epsilon_closure({nfa_start}, nfa_transitions)
    dfa_states = [initial_closure]          # lista de stări DFA
    unmarked = [initial_closure]            # stările neprocesate
    dfa_transitions = {}                    # tranzițiile DFA
    
    while unmarked:
        current = unmarked.pop()
        dfa_transitions[current] = {}
        
        for letter in alphabet:
            moved = move(current, letter, nfa_transitions)
            if not moved:
                continue
            closure = epsilon_closure(moved, nfa_transitions)
            
            # verificăm dacă closure este deja în lista de stări DFA
            # dacă nu, adăugăm closure în lista de stări DFA și în lista de stări neprocesate
            if closure not in dfa_states:
                dfa_states.append(closure)
                unmarked.append(closure)
            
            # adăugăm tranziția în DFA
            dfa_transitions[current][letter] = closure
    
    state_labels = {s: f"q{i}" for i, s in enumerate(dfa_states)}
    dfa_final = [s for s in dfa_states if any(st in nfa_final_states for st in s)]
    final_labels = [state_labels[s] for s in dfa_final]
    
    transitions = {
        state_labels[start]: {letter: state_labels[end] for letter, end in symbols.items()}
        for start, symbols in dfa_transitions.items()
    }
    
    return state_labels[initial_closure], final_labels, transitions