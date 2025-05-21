from nadia.nadia_pt_fo import check_proof

answer = """
# (P -> Q) & (P -> R) |- P -> Q & R

1. (P -> Q) & (P -> R)  pre
2. P -> Q               &e 1
3. P -> R               &e 1
4. { P                  hip
5. Q                    ->e 2, 4
6. R                    ->e 3, 4
7. Q & R                &i 5, 6
}
8. P -> Q & R           ->i 4-7
"""

print(check_proof(answer))