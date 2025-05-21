from nadia.nadia_pt_fo import check_proof

answer = """
# Q -> R |- (P -> Q) -> (P -> R)

1. Q -> R                       pre
2. { P -> Q                     hip
3.      { P                     hip
4.      Q                       ->e 2, 3 
5.      R                       ->e 1, 4
        }
6.  P -> R                      ->i 3-5
}
7. (P -> Q) -> (P -> R)         ->i 2-6
"""

print(check_proof(answer))