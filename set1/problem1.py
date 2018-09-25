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


	def problem_two(self, s1, s2, s3):
		if len(s1) != len(s2): return "Please input hex strings of same length." 
		s1 = bytearray.fromhex(s1)
		s2 = bytearray.fromhex(s2)
		xored = self.bytes_xor(s1, s2)
		if s3.strip() == bytes(xored).hex().strip(): return "You did it!"
		else: return "We are sorry! Please try again."

	def bytes_xor(self, s1, s2):
		xored = [a ^ b for a,b in zip(s1,s2)] 
		return xored

if __name__ == '__main__':
	s1= '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	s2= 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
	print(SetOne().problem_one(s1, s2))
	s1 = '1c0111001f010100061a024b53535009181c'
	s2 = '686974207468652062756c6c277320657965'
	s3 = '746865206b696420646f6e277420706c6179'
	print(SetOne().problem_two(s1, s2, s3))