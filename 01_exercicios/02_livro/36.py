from nadia.nadia_pt_fo import check_proof

answer = """
# |- ~P -> (P -> (P -> Q))

1. {~P                      hip
2.  { P                     hip
3.      { P                 hip
4.      @                   ~e 1, 3
5.      Q                   @e 4
        }
6.  P -> Q                  ->i 3-5
    }
7.  P -> (P -> Q)           ->i 2-6
}
8. ~P -> (P -> (P -> Q))       ->i 1-7
"""

print(check_proof(answer))
