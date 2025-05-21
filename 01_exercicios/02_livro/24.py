from nadia.nadia_pt_fo import check_proof

answer = """
# (P & Q) | (P & R) |- P & (Q | R)

1. (P & Q) | (P & R)    pre
2. { P & Q              hip
3. P                    &e 2
4. Q                    &e 2
5. Q | R                |i 4
6. P & (Q | R)          &i 3, 5
}
7. { P & R              hip
8. P                    &e 7
9. R                    &e 7
10. Q | R               |i 9
11. P & (Q | R)         &i 8, 10
}
12. P & (Q | R)         |e 1, 2-6, 7-11
"""

print(check_proof(answer))
