from nadia.nadia_pt_fo import check_proof

answer = """
#  31. ⊢ p∨¬p

1. { ~(P | ~P)      hip
2.  { P             hip
3.  P | ~P          |i 2
4.  @               ~e 1, 3
    }
5.  ~P              ~i 2-4
6. P | ~P           |i 5
7. @                ~e 1, 6
}
8. P | ~P           raa 1-7
"""

print(check_proof(answer))
