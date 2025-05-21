from nadia.nadia_pt_fo import check_proof

answer = """
#  20. p∨q ⊢ ¬(¬p∧¬q)

1. P | Q                pre
2. { ~P & ~Q            hip
3. ~P                   &e 2
4. ~Q                   &e 2
5.      { P             hip
6.       @              ~e 3, 5
        }
7.      { Q             hip
8.      @               ~e 4, 7
        }
9. @                    |e 1, 5-6, 7-8
}
10. ~( ~P & ~Q )        ~i 2-9
"""

print(check_proof(answer))
