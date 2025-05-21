from nadia.nadia_pt_fo import check_proof

answer = """
# 34. ⊢ (p → q) → ((r → p) → (r → p))

1. { P -> Q                                 hip
2.  { R -> P                                hip
3.      { R                                 hip
4.      P                                   ->e 2, 3
        }
5.   R -> P                                 ->i 3-4
    }
6.  (R -> P) -> (R -> P)                    ->i 2-5
}
7. (P -> Q) -> ((R -> P) -> (R -> P))       ->i 1-6
"""

print(check_proof(answer))
