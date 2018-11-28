#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import hashlib
import base64

str = '<request><addressList><str>北京市通州区中关村科技园通州园光机电一体化产业基地嘉创路3号</str></addressList></request>'
sign = "jfiaodkfIUHFHIE/.83("

inputstr = list(str+sign)
lists = []

m1 = hashlib.md5()
m1.update((str+sign).encode('utf-8'))
print(base64.b64encode(m1.digest()))

# for index,x in enumerate(inputstr):
#     if ord(x)<999:
#         lists.append(ord(x))
#     else:
#         lists.append(ord(x) >> 12 | 224)
#         lists.append(ord(x) >> 6 & 63 | 128)
#         lists.append(63 & ord(x)  | 128)
#
# print(lists)
#
# def r(e):
#     if e.length % i != 0:
#         r = e.length + (i - e.length % i)
#         e = t.concat([e, n], r)
#     for (a = new Array(e.length >>> 2), f = 0, o = 0; f < e.length; f += i,
#             o++)
#         a[o] = e.readInt32LE(f);
#     return a
#
#
# md5 = hashlib.md5()
# md5.update(repr(lists).encode('utf-8'))
#
# a = '�`�����ɉ��/�p'
#
#
# print(md5.digest())
# print(md5.hexdigest())
# print(base64.b64encode(md5.digest()))
# print(base64.b64encode(bytes(md5.hexdigest(),'ascii')))



#'data_digest':'z2DaAhnC7v3SyYmAxi/kcA=='

