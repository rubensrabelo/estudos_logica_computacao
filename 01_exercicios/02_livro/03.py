from nadia.nadia_pt_fo import check_proof

answer = """
# P -> (P -> Q), P |- Q

1. P -> (P -> Q)    pre
2. P                pre
3. P -> Q           ->e 1, 2
4. Q                ->e 2, 3
"""

print(check_proof(answer))