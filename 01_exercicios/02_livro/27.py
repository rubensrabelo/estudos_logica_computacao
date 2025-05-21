from nadia.nadia_pt_fo import check_proof

answer = """
# ~P, P | Q |- Q

1. ~P       pre
2. P | Q    pre
3. { P      hip
4.  @       ~e 1, 3
5.  Q       @e 4
}
6. { Q      hip
7.  Q       copie 6
}
8. Q        |e 2, 3-5, 6-7
"""

print(check_proof(answer))
