from nadia.nadia_pt_fo import check_proof

answer = """
# P |- (P -> Q) -> Q

1. P                pre
2. { P -> Q         hip
3.  Q               ->e 1, 2
}
4. (P -> Q) -> Q    ->i 2-3
"""

print(check_proof(answer))