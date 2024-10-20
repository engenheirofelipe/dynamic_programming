#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

from collections import deque

fila = deque()
fila.append(5)
fila.append(3)
fila.popleft()
fila.append(2)
fila.append(8)
fila.popleft()
fila.popleft()
print(fila)
