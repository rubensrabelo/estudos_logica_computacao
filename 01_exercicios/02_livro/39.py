from nadia.nadia_pt_fo import check_proof

answer = """
# g) |- ~P | Q -> (P -> Q)

1. { ~P | Q                 hip
2.  { P                     hip
3.      { ~P                hip
4.      @                   ~e 2, 3
5.      Q                   @e 4
        }
6.      {Q                  hip
        }
7.  Q                       |e 1, 3-5, 6-6
    }
8.  P -> Q                  ->i 2-7
}
9.  (~P | Q) -> (P -> Q)    ->i 1-8
"""

print(check_proof(answer))
