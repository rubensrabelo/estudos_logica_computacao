from nadia.nadia_pt_fo import check_proof

answer = """
# p∨q,p →r,q →r ⊢r

1. P | Q		pre
2. P -> R		pre
3. Q -> R		pre
4. { P			hip
5. R			->e 4, 2
}
6. { Q			hip
7. R			->e 6, 3
}
8. R			|e 1, 4-5, 6-7

"""

print(check_proof(answer))
