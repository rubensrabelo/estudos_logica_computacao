from nadia.nadia_pt_fo import check_proof

answer = """
# 18. p ∧ q ⊢ ¬( p → ¬q )

1. P & Q        pre
2. P            &e 1
3. Q            &e 1
4. { P -> ~Q    hip
5. ~Q           ->e 2, 4
6. @            ~e 3, 5
}
7. ~( P -> ~Q ) ~i 4-6
"""

print(check_proof(answer))
