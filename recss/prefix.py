#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2017/12/23 18:00
# @Author : aimkiray
# @Email  : root@meowwoo.com

raw_str = 'C:\\Users\\nekuata\\Desktop\\github.css'
out_str = 'C:\\Users\\nekuata\\Desktop\\out_github.css'
temp_str = ""


def operator_css(the_str, the_line):
    global temp_str
    if line[0] in ['\n', '\r', ' ', '}']:
        temp_str = the_str + the_line
    else:
        temp_str = the_str + ".github_css " + the_line


with open(raw_str, "r") as raw:
    for count, line in enumerate(raw):
        operator_css(temp_str, line)
    with open(out_str, "w") as out:
        out.write(temp_str)
