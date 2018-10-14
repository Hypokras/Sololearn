"""
Syllable Generator
Coded by Marc Maurer (c) 2017
Generates syllables based on predefined patterns
Original code: https://code.sololearn.com/cU50eUcxRjS3/#py
"""

# -*- coding: utf-8 -*-

""" Since I love conlanging, I was looking for a generator for syllables. I found some on the web, but this was a place to start. So here is my first Python script. Not in it's first version, but still "the same" script. """



def create_syllables():
	""" create_syllables does exactly that, it creates syllables.
		Upcoming versions should be able to import rules for creating from a
		ini File """

		
	""" begin of function definition """
	def consvocs(c, v):
		""" consvocs creates syllables containing consonant / vocal """
		b = ""
		for everyC in c:
			for everyV in v:
				b += '%s%s\n' % (everyC, everyV)
		return b

	def consvocscons(c, v, e):
		""" consvocscons creates syllables containing consonant / vocal / consonant """
		b = ""
		for everyC in c:
			for everyV in v:
				for everyE in e:
					b += '%s%s%s\n' % (everyC, everyV, everyE)
		return b
	
	def vocsconsvocs(a, c, v):
		""" vocsconsvocs creates syllables containing beginning vocal / consonant / vocal """
		b = ""
		for everyA in a:
			for everyC in c:
				for everyV in v:
					b += '%s%s%s\n' % (everyA, everyC, everyV)
		return b
	
	def vocscons(v, c):
		""" vocscons creates syllables containing vocal / consonant """
		b = ""
		for everyV in v:
			for everyC in c:
				b += '%s%s\n' % (everyV, everyC)
		return b
	""" end of function definition """

	
	""" set of vars - start """	
	vokale = ["a", "e", "i", "o", "u", "y"]
	diphtonge = ["au", "ia", "ua", "ya"]
	konsonanten = ["p", "b", "t", "d", "c", "g", "f", "v", "T", "s", "z", "x", "h", "m", "n", "j", "l", "r"]
	konsonanten_zwei = ["bl", "br", "gl", "gm", "hl", "cc", "lb", "lc", "ld", "lg", "ll", "lp", "mb", "mm", "nd", "ng", "nn", "nt", "ph", "ps", "rd", "rg", "rk", "rn", "rt", "sk", "sp", "ss", "st", "th", "tt"]
	konsonanten_drei = ["nth", "pht", "thr"]

	buffer = ""
	empty = ""

	""" f=ph, T=th, x=ch, j=ng -> Just a note to myself for future changes"""
	
	""" set of vars - end """


	#Konsonant / Vokal
	
	buffer += consvocs(konsonanten, vokale)
	buffer += consvocs(konsonanten, diphtonge)
	buffer += consvocs(konsonanten_zwei, vokale)
	buffer += consvocs(konsonanten_zwei, diphtonge)
	buffer += consvocs(konsonanten_drei, vokale)
	buffer += consvocs(konsonanten_drei, diphtonge)

	
	#Konsonant / Vokal / Konsonant

	buffer += consvocscons(konsonanten, vokale, konsonanten)
	buffer += consvocscons(konsonanten, vokale, konsonanten_zwei)
	buffer += consvocscons(konsonanten, vokale, konsonanten_drei)
	buffer += consvocscons(konsonanten_zwei, vokale, konsonanten)
	buffer += consvocscons(konsonanten_zwei, vokale, konsonanten_zwei)
	buffer += consvocscons(konsonanten_zwei, vokale, konsonanten_drei)
	buffer += consvocscons(konsonanten_drei, vokale, konsonanten)
	buffer += consvocscons(konsonanten_drei, vokale, konsonanten_zwei)
	buffer += consvocscons(konsonanten_drei, vokale, konsonanten_drei)


	#Vokal / Konsonant / Vokal

	buffer += vocsconsvocs(vokale, konsonanten, vokale)
	buffer += vocsconsvocs(vokale, konsonanten, diphtonge)
	buffer += vocsconsvocs(vokale, konsonanten_zwei, vokale)
	buffer += vocsconsvocs(vokale, konsonanten_zwei, diphtonge)
	buffer += vocsconsvocs(vokale, konsonanten_drei, vokale)
	buffer += vocsconsvocs(vokale, konsonanten_drei, diphtonge)


	#Vokal / Konsonant

	buffer += vocscons(vokale, konsonanten)
	buffer += vocscons(vokale, konsonanten_zwei)
	buffer += vocscons(vokale, konsonanten_drei)

	
	return buffer

print(create_syllables())
