DESCRIERE

Acest proiect implementează procesul de conversie a unei expresii regulate într-un DFA, parcurgând următorii pași:
1. Transformarea expresiei regulate în formă postfixată folosind algoritmul Shunting Yard
2. Conversia expresiei postfixate într-un NFA utilizând algoritmul lui Thompson
3. Transformarea NFA în DFA prin algoritmul de subset construction


STRUCTURĂ

1. main.py:
    - Fișierul principal de rulare.
    - Coordonează toate etapele:
        • citește testele din fișierul tests.json
        • apelează funcțiile de conversie (regex_to_postfix, regex_to_nfa, build_dfa)
        • afișează cuvântul, dacă este acceptat de DFA și răspunsul așteptat

2. regex_to_postfix.py:
    - Conține funcția de conversie a expresiilor regulate din formă infixată în forma postfixată.
    - Funcția principală: regex_to_postfix(regex).

3. regex_to_nfa.py:
    - Se ocupă cu construirea unui NFA folosind algoritmul Thompson, bazat pe expresia regulată în forma postfixată.
    - Funcția principală: regex_to_nfa(regex).

4. nfa_to_dfa.py:
    - Conține algoritmul de conversie a unui NFA într-un DFA folosind metoda subsetului.
    - Funcția principală: build_dfa(nfa_start, nfa_final_states, nfa_transitions, alphabet)


IMPLEMENTARE

• Expresia regulată postfixată este stocată în memorie sub forma unei liste, fiind mai eficientă la inserare decât un string.
• Tranzițiile NFA sunt reprezentate ca dicționare de dicționare (ex: {stare: {simbol: [stări_destinație]}}).
• DFA-ul este reprezentat prin stări etichetate (ex: q0, q1), cu tranziții reprezentate similar cu cele al NFA-ului.
• Testele sunt validate prin simularea directă a DFA-ului pe șirurile de intrare.


ALGORITMI

1. Algoritmul Shunting Yard 
- Transformă o expresie regulată din formă infixată (a|b*c) în formă postfixată (ab*c|).
- Pași:
    • Operatorii, împreună cu prioritatea lor, sunt reținuți într-un dicționar: {operator: priority}.
    • Inserarea operatorului de concatenare ('.')
        - între două caractere alfanumerice (ex. ab -> a.b)
        - După operatorii '*', '?', '+' sau după ')' urmate de un caracter sau de '(' (ex. a*b -> a*.b)
    • Transformarea expresiei regulate în forma postfixată:
        - se rețin într-o stivă operatorii și parantezele pentru a putea asigura ordinea corectă în expresia postfixată
        - se parcurge expresia caracter cu caracter:
            • operand: se adaugă direct la rezultat
            • operator: sunt scoși din stivă toți operatorii cu prioritatea mai mare sau egală și se adaugă în stivă operatorul 
                        curent
            • '(': se adaugă în stivă 
            • ')': scoate operatorii din stivă până la '(' și îi adaugă la rezultat
        - la final se scot toți operatorii rămași pe stivă și se adaugă la rezultat 

2. Algoritmul lui Thompson
- Construiește un NFA din expresia postfixată, folosind epsilon-tranziții (reprezentate prin None) pentru a lega stări.
- NFA-ul are structura (start_state, end_state, transitions).
- Pași: 
    • Fiecare caracter alfanumeric este convertit într-un NFA elementar cu două stări și o tranziție pe simbolul respectiv (char).
    • Fragmentele de NFA generate se rețin temporar într-o stivă.
    • Operatorii manipulează stiva astfel:
        - '.': leagă finalul primului NFA cu începutul celui de-al doilea printr-o epsilon-tranziție
        - '|': creează două stări noi care se ramifică în cele două NFA-uri și se reunesc la final
        - '?': creează două stări noi; se leagă new_start de începutul NFA-ului și de new_end
        - '*': creează două stări noi; se leagă new_start de începutul NFA-ului și de new_end; se leagă finalul NFA-ului de 
               începutul NFA-ului și de new_end
        - '+': creează două stări noi; se leagă new_start de începutul NFA-ului; se leagă finalul NFA-ului de începutul NFA-ului 
               și de new_end

3. Algoritmul de Construcție a Subsetului
- Convertește NFA-ul într-un DFA prin simularea tuturor căilor posibile în NFA, prin gruparea stărilor NFA în subseturi.
- Funcții ajutătoare:
    • epsilon_closure(state) -> toate stările NFA accesibile dintr-o stare (sau un set de stări) prin epsilon-tranziții
                             -> mulțimea devine o stare DFA
    • move(state, letter, transitions) -> mulțimea stărilor NFA accesibile prin citirea simbolului
- Pași:
    • Starea inițială a DFA-ului este epsilon-closure(nfa_start)
    • Pentru fiecare stare din DFA și simbol din alfabet:
        - se calculează move(current, letter, nfa_transitions) pentru a găsi mulțimea stărilor NFA accesibile dintr-un set de stări 
          prin citirea unui simbol
        - aplică epsilon_closure pe rezultat pentru a obține noua stare DFA (closure) -> extinde rezultatul cu lambda-tranziții
        - dacă noua stare nu există deja în DFA, o adaugă la DFA ca unmarked
        - definește tranziția: current --letter--> closure
    • O stare DFA este finală dacă ea conține cel puține o stare finală NFA.
- DFA-ul are structura (start_state, end_states, transitions).


RULARE PROIECT

- Cerințe:
    • python 3 instalat
    • fișierul tests.json în același director cu celelalte fișiere

- Instrucțiuni:
    • rulează fișierul main.py în terminal: python main.py  
    • rezultatele vor fi afișate în consolă


DATE DE IEȘIRE

- Pentru fiecare test din tests.json, programul afișează:
    • numele testului
    • fiecare șir de intrare (input), rezultatul așteptat (expected) și rezultatul obținut (result)
