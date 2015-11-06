#!/bin/sh

# Installation script of prolog and epilog modules for SGE
#
# Date: 29 Set. 2015
# author: mariojmavid@gmail.com
#
# pelogw/etc/ contains config files
# pelogw/src/ contains modules prolog, epilog...
# $basedir is the install dir
# cont-batch.conf is the config file

# Usage ./install.sh <INSTALL_DIR>
# Example: ./install.sh /opt/ge-tools/exec

if [ "x$1" = "x" ] 
then
    echo "Usage: ./$0 <INSTALL_DIR>"
    echo "The prolog and epilog scripts will be installed under <INSTALL_DIR>/exec"
    exit 1
fi

basedir=$1
sourcedir=`pwd`
ETC=/etc/pelogw

# Make necessary dirs if they don't exist
mkdir -p ${ETC}
mkdir -p ${basedir}/exec

if [ -e ${ETC}/cont-batch.conf ]
then
    cp ${sourcedir}/etc/cont-batch.conf ${ETC}/cont-batch.conf.new
else
    cp ${sourcedir}/etc/cont-batch.conf ${ETC}/cont-batch.conf
fi

cp ${sourcedir}/sec/*.py ${basedir}/exec/
chmod 755 ${basedir}/exec/*.py

