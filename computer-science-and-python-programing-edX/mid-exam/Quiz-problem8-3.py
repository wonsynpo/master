def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    # return fixedPoint(babylon, 0.0001) 	#bug
    return fixedPoint(babylon(a), 0.0001) 		#corrected