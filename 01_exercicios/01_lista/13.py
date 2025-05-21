from nadia.nadia_pt_fo import check_proof

answer = """
#  p∧(q ∨r) ⊢ (p∧q)∨(p∧r)

1. P & ( Q | R )			pre
2. P				        &e 1
3. ( Q | R )			    &e 1
4. { Q				        hip
5. P & Q			        &i 2, 4
6. ( P & Q ) | ( P & R )	|i 5
}
7. { R				        hip
8. P & R			        &i 2, 7
9. ( P & Q ) | ( P & R )	|i 8
}
10. ( P & Q ) | ( P & R )	|e 3, 4-6, 7-9
"""

print(check_proof(answer))
