#!/bin/bash

installdir="/opt/nginx"


yum install -y -q pcre-devel openssl-devel gcc make

cd /tmp
wget -q  http://nginx.org/download/nginx-1.4.7.tar.gz
tar zxf nginx-1.4.7.tar.gz

cd nginx-1.4.7

./configure \
--prefix=$installdir \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--with-http_gzip_static_module \
&& make -j 4 && make install
