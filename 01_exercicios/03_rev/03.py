from nadia.nadia_pt_fo import check_proof

answer = """
# 3. p ∨ q, p → r, q → r ⊢r

1. P | Q    pre
2. P -> Q   pre
3. Q -> R   pre
4. { P      hip
5. Q        ->e 2, 4
6. R        ->e 3, 5
}
7. { Q      hip
8. R        ->e 3, 7
}
9. R        |e 1, 4-6, 7-8
"""

print(check_proof(answer))