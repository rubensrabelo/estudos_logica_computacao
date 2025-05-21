from nadia.nadia_pt_fo import check_proof

answer = """
# R, P -> (R -> Q) |- P -> (Q & R)

1. R                pre
2. P -> (R -> Q)    pre
3. { P              hip
4. R -> Q           ->e 2, 3
5. Q                ->e 1, 4
6. Q & R            &i 1, 5
}
7. P -> (Q & R)     ->i 3-6
"""

print(check_proof(answer))