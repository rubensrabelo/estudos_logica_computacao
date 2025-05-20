from nadia.nadia_pt_fo import check_proof

answer = """
# 28. ⊢ (p → (q →r)) →(q →(p→r))

1. { P -> ( Q -> R )                            hip
2.      { Q                                     hip
3.              { P                             hip
4.              Q -> R                          ->e 1, 3
5.              R                               ->e 2, 4
                }
6.      P -> R                                  ->i 3-5
        }
7. Q -> ( P -> R )                              ->i 2-6
}
8. (P -> ( Q -> R )) -> (Q -> ( P -> R ))       ->i 1-7
"""

print(check_proof(answer))
