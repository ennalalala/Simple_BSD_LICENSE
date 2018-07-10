'''
Copyright (c) 20**-20**, The **** Project
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

   1. Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the
      distribution.
   3. Neither the name of the **** project nor the names of 
      its contributors may be used to endorse or promote products 
      derived from this software without specific prior written 
      permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''



#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os,re

rootDir = '.'
licensePath = './LICENSE'


def IterationPath(rootDir):
    with open(licensePath, "r+") as f_license:
        license_content = f_license.read()
    for root, dirs, files in os.walk(rootDir):
        for filepath in files:
            if os.path.splitext(filepath)[1] == '.h' or os.path.splitext(filepath)[1] == '.c':
                Rule = "^\/\*(\s|.)*?\*\/"
                reRule = re.compile(Rule, re.M)
                with open(os.path.join(root, filepath), "r+") as f_c:
                    old_content = f_c.read()
                    new_content = re.sub(reRule, "", old_content)
                    f_c.seek(0)
                    f_c.truncate()
                    f_c.seek(0)
                    f_c.write("/*\n")
                    f_c.write(license_content)
                    f_c.write("*/\n")
                    f_c.write(new_content)
            if os.path.splitext(filepath)[1] == '.py':
                Rule = "^\'\'\'(\s|.)*?\'\'\'"
                reRule = re.compile(Rule, re.M)
                with open(os.path.join(root, filepath), "r+") as f_c:
                    old_content = f_c.read()
                    new_content = re.sub(reRule, "", old_content)
                    f_c.seek(0)
                    f_c.truncate()
                    f_c.seek(0)
                    f_c.write("\'\'\'\n")
                    f_c.write(license_content)
                    f_c.write("\'\'\'\n")
                    f_c.write(new_content)

if __name__ == "__main__":
    IterationPath(rootDir)
