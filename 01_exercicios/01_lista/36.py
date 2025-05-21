from nadia.nadia_pt_fo import check_proof

answer = """
# 36. ⊢ (p → (q → r)) → ((p → q) → (p → r))

1. { P -> (Q -> R)                                  hip
2.  { P -> Q                                        hip
3.      { P                                         hip
4.      Q                                           ->e 2, 3
5.      Q -> R                                      ->e 1, 3
6.      R                                           ->e 4, 5
        }
7.      P -> R                                      ->i 3-6
    }
8.  (P -> Q) -> (P -> R)                                ->i 2-7
}
9. (P -> (Q -> R)) -> ((P -> Q) -> (P -> R))        ->i 1-8
"""

print(check_proof(answer))
