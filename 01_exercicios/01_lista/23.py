from nadia.nadia_pt_fo import check_proof

answer = """
# 23. ¬(p ∧ ¬q) ⊢ p → q

1. ~( P & ~Q )      pre
2. { P              hip
3.      { ~Q        hip
4.      P & ~Q      &i 2, 3
5.      @           ~e 1, 4
        }
6. Q                raa 3-5
}
7. P -> Q           ->i 2-6
"""

print(check_proof(answer))
