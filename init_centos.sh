#!/bin/bash

yum update -y
yum install -y tree vim lrzsz gcc make bind-utils zip unzip wget curl openssl-devel git python-devel

cd /tmp
rm -f vimrc
wget https://raw.githubusercontent.com/WillGhost/op/master/vimrc
mv -f vimrc /etc/vimrc

pip install -U pip

