from nadia.nadia_pt_fo import check_proof

answer = """
# 33. ⊢ p →p

1. { P      hip
2. P        copie 1
}
3. P -> P   ->i 1-2
"""

print(check_proof(answer))
