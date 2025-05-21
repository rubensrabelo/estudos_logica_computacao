from nadia.nadia_pt_fo import check_proof

answer = """
# (P | (Q -> P)) & Q |- P

1. (P | (Q -> P)) & Q   pre
2. P | (Q -> P)         &e 1
3. Q                    &e 1
4. { P                  hip
5. P                    copie 4
}
6. { Q -> P             hip
7. P                    ->e 3, 6
}
8. P                    |e 2, 4-5, 6-7
"""

print(check_proof(answer))