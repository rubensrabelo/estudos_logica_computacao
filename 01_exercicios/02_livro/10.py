from nadia.nadia_pt_fo import check_proof

answer = """
# P -> (Q -> R), P -> Q |- P -> R

1. P -> (Q -> R)        pre
2. P -> Q               pre
3. { P                  hip
4. Q                    ->e 2, 3
5. Q -> R               ->e 1, 3
6. R                    ->e 4, 5
}
7. P -> R               ->i 3-6
"""

print(check_proof(answer))