from nadia.nadia_pt_fo import check_proof

answer = """
# 32. ⊢ ( p → q ) ∨ ( q → p )

1. P | ~P LTE
2. { P                      hip
3.  { Q                     hip
4.  P                       copie 2
    }
5. Q -> P                   ->i 3-4
6. ( P -> Q ) | (Q -> P)    |i 5
}
7. { ~P                     hip
8.  { P                     hip
9.  @                       ~e 7, 8
10. Q                       @e 9
    }
11. P -> Q                  ->i 8, 9
12. ( P -> Q ) | (Q -> P)   |i 11
}
13. ( P -> Q ) | (Q -> P)   |e 1, 2-6, 7-12
"""

print(check_proof(answer))
