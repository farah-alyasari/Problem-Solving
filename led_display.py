'''
Scenario

You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:
  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # #
  # ### ### ### ### ###   # ### ### # #
  # #     #   #   # # #   # # #   # # #
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

'''

digits = { '0': '1111110',  	# 0
	   '1': '0110000',	# 1
	   '2': '1101101',	# 2
	   '3': '1111001',	# 3
	   '4': '0110011',	# 4
	   '5': '1011011',	# 5
	   '6': '1011111',	# 6
	   '7': '1110000',	# 7
	   '8': '1111111',	# 8
	   '9': '1111011',	# 9
	   }

def printNumber(num):
	global digits
	digs = str(num)
	lines = [ '' for l in range(5) ]
	for d in digs:
        # only display segmets for a num with more than 0 digits
		segs = [ [' ',' ',' '] for l in range(5) ]
        # the 1's in the pattern of the digit are the segments to be turned on
		ptrn = digits.get(d)
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '*'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '*'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '*'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '*'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '*'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '*'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '*'
		for l in range(5):
			#this line enables printing multiple digits next to each other
			#by joining the characters in the segment array into a string
            #The result is a horizonal line segment for multiple digit
			lines[l] += ''.join(segs[l]) + '  '
	for l in lines:
		print(l)

printNumber(int(input("Enter the number you wish to display: ")))
