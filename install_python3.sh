#!/bin/bash

version="3.4.2"
installdir="/opt/python34"
durl=https://www.python.org/ftp/python/$version/Python-$version.tgz

yum install -y -q readline-devel gcc make wget openssl-devel

cd /tmp
wget -q $durl
tar zxvf Python-$version.tgz
cd Python-$version
./configure --prefix=$installdir && make -j 2 && make install && ln -s $installdir/bin/python3 /usr/bin/python3


