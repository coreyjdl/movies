#!/usr/bin/env python3

import re, sys, requests

html = requests.get("http://manntheatres.com/theatre/?tid=86")
movies = {*re.findall(r'\<h3\>\<a href\=\".*\">(.*)(?=.<.a></h3>)', html.text)}
print(*sorted(movies), sep="\n")
