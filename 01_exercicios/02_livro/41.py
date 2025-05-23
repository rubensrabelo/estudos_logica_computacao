from nadia.nadia_pt_fo import check_proof

answer = """
# i) (C & N) -> T, H & ~S, H & ~(S | C) -> P |- (N & ~T) -> P
"""

print(check_proof(answer))
