from nadia.nadia_pt_fo import check_proof

answer = """
# (P -> R) & (Q -> R) |- P & Q -> R

1. (P -> R) & (Q -> R)  pre
2. (P -> R)             &e 1
3. (Q -> R)             &e 1
4. { P & Q              hip
5. P                    &e 4
6. Q                    &e 4
7. R                    ->e 3, 6
}
8. P & Q -> R           ->i 4-7
"""

print(check_proof(answer))