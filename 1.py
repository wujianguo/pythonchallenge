#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
def main():
    f=string.ascii_lowercase
    t=f[2:]+f[:2]
    trans_tables=string.maketrans(f,t)
    encs="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(string.translate(encs,trans_tables))
    print(string.translate('map',trans_tables))
if __name__=='__main__':
    main()