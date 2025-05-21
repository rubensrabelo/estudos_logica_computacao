from nadia.nadia_pt_fo import check_proof

answer = """
# Q -> (P -> R), ~R, Q |- ~P

1. Q -> (P -> R)    pre
2. ~R               pre
3. Q                pre
4. { P              hip
5. P -> R           ->e 1, 3
6. R                ->e 4, 5
7. @                ~e 2, 6
}
8. ~P               ~i 4-7
"""

print(check_proof(answer))