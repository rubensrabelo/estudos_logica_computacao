from nadia.nadia_pt_fo import check_proof

answer = """
# ¬p∧¬q ⊢¬(p∨q)

1. ~P & ~Q		pre
2. ~P			&e 1
3. ~Q			&e 1
4. { P | Q		hip
5. 	{P		    hip
6.	@		    ~e 5, 2
    }
7. 	{ Q		    hip
8.	@		    ~e 7, 3
    }
9. @			|e 4, 5-6, 7-8
    }
10. ~( P | Q )	~i 4-9
"""

print(check_proof(answer))
