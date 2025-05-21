from nadia.nadia_pt_fo import check_proof

answer = """
# P -> Q |- ((P & Q) -> P) & (P -> (P & Q))

1. P -> Q                                 pre
2. { P & Q                                hip
3. P                                      &e 2
}
4. (P & Q) -> P                           ->i 2-3
5. { P                                    hip
6. Q                                      ->e 1, 5
7. P & Q                                  &i 5, 6
}
8. P -> (P & Q)                           ->i 5-7
9. ((P & Q) -> P) & (P -> (P & Q))        &i 4, 8
"""

print(check_proof(answer))