#!/usr/bin/python
#coding:utf-8
import sys
import urllib2
import urllib
import json
from commands import getstatusoutput

access_token = 'T4DDxgprfYsAAAAAAAAAASPZ234234W_Hv3hst43VZYwW32mvuTsnTdsXr23r23gE'

url_md = 'https://api.dropbox.com/1/metadata/'
url_file = 'https://api-content.dropbox.com/1/files/'


def color(str,clr=''):
	if clr == 'yellow':
		return '\033[33;1m' + str + '\033[0m'
	else:
		return '\033[36;1m' + str + '\033[0m'

def up_file(file,path):
	url = url_file + 'dropbox/' + path + '?access_token=' + access_token
	a = getstatusoutput('curl -s -F file=@%s %s'% (file,url))
	if a[0] == 0:
		print color('Upload ok ..')
	else:
		print a

def down_file(path):
	url = url_file + 'dropbox/' + path + '?access_token=' + access_token
	urllib.urlretrieve(url,path.split('/')[-1])
	print color('Download ok ..')

def get_meta(path=''):
	url = url_md + 'dropbox/' + path + '?access_token=' + access_token
	a = urllib.urlopen(url).read()
	a = json.loads(a)
	if 'error' in a.keys():
		print 'Error !  ',a['error']
		return
	if not a['is_dir']:
		print color('%s \tis a file. \t\tsize %s'%(a['path'],a['size']),clr='yellow')
		return
	if a['is_dir']:
		print color('Path: %s'%a['path'],clr='yellow')
		space = '    '
		for i in a['contents']:
			cot = i['path'].split('/')[-1]
			if i['is_dir']:
				print color(cot) + space,
			else:
				print cot + space,
		print '\n'
		return
	print '%s\nSomething ERROR'%str(a)


def main():
	opt = ['-l','-d','-u']
	if not sys.argv[1] in opt:
		print 'Error sys.argv[1] like %s'%str(opt)
		return
	if sys.argv[1] == '-l':
		if len(sys.argv) == 2:	ar2 = ''
		else:	ar2 = sys.argv[2]
		get_meta(ar2)
	if sys.argv[1] == '-d':
		down_file(sys.argv[2])
	if sys.argv[1] == '-u':
		up_file(sys.argv[2],sys.argv[3])

if __name__ == '__main__':
	main()

