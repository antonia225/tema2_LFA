DESCRIERE

Acest proiect implementează procesul de conversie a unei expresii regulate într-un DFA, trecând prin următorii pași:
1. transformpă regex în postfix
2. convertește postfix în NFA
3. convertește NFA în DFA


STRUCTURĂ

1. main.py
Fișierul principal de rulare.
Coordonează toate etapele:
    - citește testele din fișierul .json
    - apelează funcțiile de conversie
    - afișează cuvântul, dacă este acceptat de DFA și răspunsul așteptat

2. regex_to_postfix.py
Conține funcția de conversie a expresiilor regulate din formă infixată în forma postfixată.

3. regex_to_nfa.py
Se ocupă cu construirea unui NFA folosind algoritmul Thompson, bazat pe expresia regulată în forma postfixată.

4. nfa_to_dfa.py
Conține algoritmul de conversie a unui NFA într-un DFA folosind metoda subsetului.


RULARE

Se rulează fișierul main.py în mod obișnuit. 
