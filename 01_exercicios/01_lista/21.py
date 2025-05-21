from nadia.nadia_pt_fo import check_proof

answer = """
# 21. ¬( ¬p ∧ ¬q ) ⊢ p ∨ q

1. ~( ~P & ~Q )         pre
2. { ~( P | Q )         hip
3.      { P             hip
4.      P | Q           |i 3
5.      @               ~e 2, 4
        }
6. ~P                   ~i 3-5
7.      { Q             hip
8.      P | Q           |i 7
9.      @              ~e 2, 8
        }
10. ~Q                  ~i 7-9
11. ~P & ~Q             &i 6, 10
12. @                   ~e 1, 11
}
13. P | Q               raa 2-12
"""

print(check_proof(answer))
