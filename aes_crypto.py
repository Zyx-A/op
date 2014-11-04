#!/usr/bin/python
from Crypto.Cipher import AES
import base64

block_size = 16
#secret = os.urandom(block_size)
secret = '\xfb8\xf6\x02\xe0\xe2P\x03\xc2\x14\xa4v\r\x10\x1dR'
padding = '{'
cipher = AES.new(secret)

def encrypt(message):
	pad = lambda s: s + (block_size - len(s) % block_size) * padding
	EncodeAES = lambda c,s: base64.b64encode(c.encrypt(pad(s)))
	return EncodeAES(cipher,message)

def decrypt(passphrase):
	DecodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(padding)
	return DecodeAES(cipher,passphrase)

