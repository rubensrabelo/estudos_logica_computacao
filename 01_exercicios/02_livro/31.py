from nadia.nadia_pt_fo import check_proof

answer = """
# P & ~P |- ~(R -> Q) & (R -> Q)

1. P & ~P                   pre
2. P                        &e 1
3. ~P                       &e 1
4. @                        ~e 2, 3
5. { R -> Q                 hip
6. @                        copie 4
}
7. ~(R -> Q)                ~i 5-6
8. { R                      hip
9. @                        copie 4
10. Q                       @e 9
}
11. R -> Q                  ->i 8-10
12. ~(R -> Q) & (R -> Q)    &i 7, 11
"""

print(check_proof(answer))
