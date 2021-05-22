# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:37:05 2021

@author: cheungm
"""

#!/usr/bin/python3

import ftplib

with ftplib.FTP('ftp.dlptest.com') as ftp:
    print(ftp.getwelcome())
