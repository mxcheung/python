# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:16:21 2021

@author: cheungm
"""

   
#!/usr/bin/python3

import ftplib

with ftplib.FTP('ftp.dlptest.com') as ftp:
    
    try:
        ftp.login('dlpuser','rNrKYTX9g7z3RgJRmxWuGHbeu')

        files = []

        ftp.dir(files.append)

        print(files)
            
    except ftplib.all_errors as e:
        print('FTP error:', e)    
