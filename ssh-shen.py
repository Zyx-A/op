#!/usr/bin/python
import paramiko
import time,sys,re
import socket

cmd = r''' ls /root  '''
node = '/root/working/ServerList-pwd-py.txt'

#upf = 'set_ipmi.py'

user = 'efw'
key_file = '/root/.ssh/id_rsa'
sshport = 22
socket.setdefaulttimeout(15)

def sshgo(host,rootuser,rootpwd):
	key = paramiko.RSAKey.from_private_key_file(key_file)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.load_system_host_keys()
	ssh.connect(host,sshport,user,pkey=key)

#	sftp = ssh.open_sftp()
#	sftp.put(upf,upf)
#	sftp.close()
#	stdin, stdout, stderr = ssh.exec_command('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8;  ')
#	print stdout.read() + stderr.read()
	print '________________________________%s'%host

	shell = ssh.invoke_shell()
	while not shell.recv(4096).endswith(']$ '):
		time.sleep(0.1)
	
	buff  =''
	shell.send('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8;su - %s'%rootuser)
	shell.send('\n')
	while not buff.endswith('Password: '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith('exist') or buff.endswith(']$ '):
			print 'ERROR_SSH.RECV_____1________________%s'% resp
			return
	buff  =''
	shell.send(rootpwd)
	shell.send('\n')
	while not buff.endswith(']# '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith('password') or buff.endswith(']$ '):
			print 'ERROR_SSH.RECV_____2________________%s'% resp
			return
	shell.send('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8; %s '%cmd)
	shell.send('\n')
	buff = ''
	while not buff.endswith(']# '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith(']$ '):
			print 'ERROR_SSH.RECV_____3________________%s'% resp
			break
		elif buff.endswith('? '):
			print 'ERROR_SSH.RECV_____4________________??'
			break
	#print buff
	print '\n'.join(buff.split('\n')[1:-1])
	sys.stdout.flush()
	ssh.close()

nn = open(node)
for i in nn:
	if not re.match('#',i) and re.search('.',i):
		c = i.split()
		host = c[0]
	 	rootuser = c[1]
		rootpwd = c[2]
		try:
			sshgo(host,rootuser,rootpwd)
		except Exception,e:	print '%s__ERROR_________________________%s'%(e,host)
nn.close()
