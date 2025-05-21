from nadia.nadia_pt_fo import check_proof

answer = """
# (P & Q) & R |- P & (Q & R)

1. (P & Q) & R      pre
2. R                &e 1
3. P & Q            &e 1
4. P                &e 3
5. Q                &e 3
6. Q & R            &i 5, 2
7. P & (Q & R)      &i 4, 6
"""

print(check_proof(answer))