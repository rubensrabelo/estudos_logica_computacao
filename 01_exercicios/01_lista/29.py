from nadia.nadia_pt_fo import check_proof

answer = """
# 29. ⊢ (p → (p →q)) →(p→q)

1. { P -> ( P -> Q)                 hip
2.  { P                             hip
3.  P -> Q                          ->e 1, 2
4.  Q                               ->e 2, 3
    }
5. P -> Q                           ->i 2-4
}
6. (P -> ( P -> Q)) -> (P -> Q)     ->i 1-5
"""

print(check_proof(answer))
