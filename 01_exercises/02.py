from nadia.nadia_pt_fo import check_proof

answer = """
# ¬¬p ⊢ p

1. ~~P		pre
2. { ~P		hip
3. @		~e 1, 2
}
4. P		raa 2-3
"""

print(check_proof(answer))
