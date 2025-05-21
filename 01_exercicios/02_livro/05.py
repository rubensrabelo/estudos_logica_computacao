from nadia.nadia_pt_fo import check_proof

answer = """
# |- (P & Q) -> P

1. { P & Q          hip
2. P                &e 1
3. Q                &e 1
4. P                copie 2
}
5. (P & Q) -> P     ->i 1-4
"""

print(check_proof(answer))