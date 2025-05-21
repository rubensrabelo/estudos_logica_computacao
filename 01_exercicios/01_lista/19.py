from nadia.nadia_pt_fo import check_proof

answer = """
# 19. ¬(p → ¬q) ⊢ p ∧ q

1. ~(P -> ~Q)       pre
2. { ~( P & Q )     hip
3.      { P         hip
4.          { Q     hip
5.          P & Q   &i 3, 4
6.          @       ~e 2, 5
            }
7.      ~Q          ~i 4-6
        }
8. P -> ~Q          ->i 3-7
9. @                ~e 1, 8
}
10. P & Q           raa 2-9
"""

print(check_proof(answer))
