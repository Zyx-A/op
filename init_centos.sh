#!/bin/bash

yum update -y
yum install -y tree vim lrzsz gcc make bind-utils zip unzip wget curl openssl-devel git python-devel

\cp vimrc /etc/vimrc

pip install -U pip

