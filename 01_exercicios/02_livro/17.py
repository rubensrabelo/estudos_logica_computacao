from nadia.nadia_pt_fo import check_proof

answer = """
# P -> Q & R |- (P -> Q) & (P -> R)

1. P -> Q & R               pre
2. { P                      hip
3. Q & R                    ->e 1, 2
4. Q                        &e 3
}
5. P -> Q                   ->i 2-4
6. { P                      hip
7. Q & R                    ->e 1, 6
8. R                        &e 7
}
9. P -> R                   ->i 6-8
10. (P -> Q) & (P -> R)     &i 5, 9
"""

print(check_proof(answer))