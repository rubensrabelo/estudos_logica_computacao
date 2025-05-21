from nadia.nadia_pt_fo import check_proof

answer = """
# P |- Q -> (P & Q)

1. P                pre
2. { Q              hip
3. P & Q            &i 1, 2
}
4. Q -> (P & Q)     ->i 2-3
"""

print(check_proof(answer))