import codecs
import base64
from operator import xor
import binascii
import itertools
import string
# from Crypto.Cipher import AES
# from Crypto.Util.strxor import strxor_c

class SetOne(object):
	"""docstring for SetOne"""
	def __init__(self, arg=None):
		# super(SetOne, self).__init__()
		self.arg = arg
		
	def problem_one(self, hex_string, check_string):
		base64_string = codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()
		# print(base64_string, check_string)
		if base64_string.strip() == check_string.strip(): return "You did it!"
		else: return "We are sorry! Please try again."


if __name__ == '__main__':
	s1= '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	s2= 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
	print(SetOne().problem_one(s1, s2))