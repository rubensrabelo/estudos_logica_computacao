from nadia.nadia_pt_fo import check_proof

answer = """
# 38. ⊢ ((p → q) → p) → p

1. { (P -> Q) -> P              hip
2.  { ~P                        hip
3.      { P                     hip
4.      @                       ~e 2, 3
5.      Q                       @e 4
        }
6. P-> Q                        ->i 3-5
7. P                            ->e 1, 6
8. @                            ~e 2, 7
    }
9.  P                           raa 2-8
}
10. ((P -> Q) -> P) -> P        ->i 1-9
"""

print(check_proof(answer))
