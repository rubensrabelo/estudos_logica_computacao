from nadia.nadia_pt_fo import check_proof

answer = """
#  11. p ∨ (q ∧ r) ⊢ (p ∨ q)∧(p ∨ r)

1. P | (Q & R)          pre
2. { P                  hip
3. P | Q                |i 2
4. P | R                |i 2
5. (P | Q) & (P | R)    &i 3, 4
}
6. { Q & R              hip
7. Q                    &e 6
8. R                    &e 6
9. P | Q                |i 7
10. P | R               |i 8
11. (P | Q) & (P | R)   &i 9, 10
}
12. (P | Q) & (P | R)   |e 1, 2-5, 6-11
"""

print(check_proof(answer))