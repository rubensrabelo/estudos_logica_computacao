from nadia.nadia_pt_fo import check_proof

answer = """
# ¬(p∧q) ⊢ ¬p∨¬q

1. ~( P & Q)		pre
2. { ~(~P | ~Q)		hip
3.	{ ~P		    hip
4.	~P | ~Q	        |i 3
5.	@		        ~e 4, 2
    }
6. P			    raa 3-5
7.	{ ~Q		    hip
8.	~P | ~Q	        |i 7
9.	@		        ~e 8, 2
    }
10. Q			    raa 7-9
11. P & Q		    &i 6, 10
12. @			    ~e 11, 1
}
13. ~P | ~Q		    raa 2-12
"""

print(check_proof(answer))
