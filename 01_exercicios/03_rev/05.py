from nadia.nadia_pt_fo import check_proof

answer = """
# 5. ¬q → ¬p ⊢ p → q

1. ~Q -> ~P     pre
2. { P          hip
3.  { ~Q        hip
4.  ~P          ->e 3, 1
5.  @           ~e 2, 4
    }
6. Q            raa 3-5
}
7. P -> Q       ->i 2-6
"""

print(check_proof(answer))