from nadia.nadia_pt_fo import check_proof

answer = """
# 37. ⊢ (p → (q →p))

1. { P                  hip
2.  { Q                 hip
3.  P                   copie 1
    }
4.  Q -> P              ->i 2-3
}
5. P -> (Q -> P)        ->i 1-4
"""

print(check_proof(answer))
