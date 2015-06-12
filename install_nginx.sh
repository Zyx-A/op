#!/bin/bash

installdir="/opt/nginx"
version=1.6.3

yum install -y -q pcre-devel openssl-devel gcc make

cd /tmp
wget -q  http://nginx.org/download/nginx-$version.tar.gz
tar zxf nginx-$version.tar.gz

cd nginx-$version

./configure \
--prefix=$installdir \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--with-http_gzip_static_module \
&& make -j 4 && make install
