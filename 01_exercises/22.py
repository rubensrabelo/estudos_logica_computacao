from nadia.nadia_pt_fo import check_proof

answer = """
# 22. p → q ⊢ ¬( p ∧ ¬q )

1. P -> Q       pre
2. { P & ~Q     hip
3. P            &e 2
4. ~Q           &e 2
5. Q            ->e 1, 3
6. @            ~e 4, 5
}
7. ~( P & ~Q )  ~i 2-6
"""

print(check_proof(answer))
