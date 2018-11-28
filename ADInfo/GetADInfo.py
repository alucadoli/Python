#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pyad
from pyad import adquery,pyad
import sys,os,multiprocessing,time
import csv

q = adquery.ADQuery()
q.execute_query(
    attributes=["name","whenCreated","distinguishedName","userAccountControl"],
    where_clause="objectCategory = 'Computer'",
    base_dn="DC=corp,DC=fcs,DC=int")



for row in q.get_results():
   DC = pyad.adcomputer.ADComputer.from_dn(row["distinguishedName"]).get_user_account_control_settings()["SERVER_TRUST_ACCOUNT"]
   AC = pyad.adcomputer.ADComputer.from_dn(row["distinguishedName"]).get_user_account_control_settings()["ACCOUNTDISABLE"]
   LC = pyad.adcomputer.ADComputer.from_dn(row["distinguishedName"]).get_user_account_control_settings()["LOCKOUT"]
   #print(row["name"],DC,AC,LC)
   if DC :
       Type = "Domain Controller"
   else:
       Type = "Computer"

   if AC:
       Status = "Disabled"
   elif LC:
       Status = "Locked"
   else:
       Status = "Active"

   print(row["name"],DC,AC,LC,Type,Status)