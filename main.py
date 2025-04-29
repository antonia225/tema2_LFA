# Stoica Elena-Antonia
# Grupa 151

import json

# fisierele în care sunt definite funcțiile utilizate
import regex_to_postfix 
import regex_to_nfa
import nfa_to_dfa

def main():
    with open('tests.json') as f:
        tests = json.load(f)
    
    for test in tests:
        print(f"Test: {test['name']}")  # testul curent
        regex = test['regex']           # expresia regulată
        
        # se transformă regex în expresie regulară postfixată
        postfix = regex_to_postfix.regex_to_postfix(regex)
        # se transformă expresia regulată în NFA     
        nfa_start, nfa_end, nfa_transitions, alphabet = regex_to_nfa.regex_to_nfa(postfix)     
        # se transformă NFA în DFA
        dfa_initial, dfa_final, dfa_transitions = nfa_to_dfa.build_dfa(nfa_start, [nfa_end], nfa_transitions, list(set(alphabet)))
        
        for case in test['test_strings']:
            # se verifica daca stringul este acceptat de regex
            q = dfa_initial
            valid = True
            for char in case['input']:
                if q not in dfa_transitions or char not in dfa_transitions[q]:
                    valid = False
                    break
                q = dfa_transitions[q][char]
            valid = valid and (q in dfa_final)
            
            # se verifica daca raspunsul este cel așteptat
            print(f"Input: {case['input']}, Expected: {case['expected']}, Result: {valid}")
            
if __name__ == "__main__":
    main()