from nadia.nadia_pt_fo import check_proof

answer = """
# P -> Q |- ~P | Q

1. P -> Q           pre
2. {~(~P | Q)       hip
3.  { P             hip
4.  Q               ->e 1, 3
5.  ~P | Q          |i 4
6.  @               ~e 2, 5
    }
7. ~P               ~i 3-6
8. ~P | Q           |i 7
9. @                ~e 2, 8
}
10. ~P | Q           raa 2-9
"""

print(check_proof(answer))
