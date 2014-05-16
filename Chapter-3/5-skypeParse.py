#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import optparse
import os
import sys, codecs, locale


def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, \
      datetime(profile_timestamp,'unixepoch') FROM Accounts;")

    for row in c:
        print 'Found Account'
        print 'User           : %s ' % (row[0],)
        print 'Skype Username : %s ' % (row[1],)
        print 'Location       : %s %s' % (row[2], row[3],)
        print 'Profile Date   : %s ' % (row[4],)


def printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country,\
      phone_mobile, birthday FROM Contacts ORDER BY skypename;")

    for row in c:
        print '\n[*] -- Found Contact --'
        print (u'[+] User           : %s ' % (row[0],)).encode('utf-8')
        print '[+] Skype Username : %s ' % (row[1],)
        if (row[2]) != '' and (row[2]) != 'None':
            print '[+] Location       : %s %s ' % (row[2], row[3],)
        if (row[4]) != 'None':
            print '[+] Mobile Number  :  %s ' % (row[4],)
        if (row[5]) != 'None':
            print '[+] Birthday       : %s ' % (row[5])


def printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE \
      calls.conv_dbid = conversations.id;"
              )
    print '\n[*] -- Found Calls --'

    for row in c:
        print '[+] Time: %s ' % (row[0])+\
          ' | Partner: %s ' % (row[1])


def printMessages(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    print '\n[*] -- Found Messages --'

    for row in c:
            if 'partlist' not in (row[3]):
                if (row[1]) != (row[2]):
                    msgDirection = 'To %s :' % (row[1]) 
                else:
                    msgDirection = 'From %s :' % (row[2]) 
                print 'Time: %s %s' % (row[0], row[3]) 
      


def main():
    parser = optparse.OptionParser("usage %prog "+\
      "-p <skype profile path> ")
    parser.add_option('-p', dest='pathName', type='string',\
      help='specify skype profile path')

    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName == None:
        print parser.usage
        exit(0)
    elif os.path.isdir(pathName) == False:
        print '[!] Path Does Not Exist: ' + pathName
        exit(0)
    else:
        skypeDB = os.path.join(pathName, 'main.db')
        if os.path.isfile(skypeDB):
            printProfile(skypeDB)
            printContacts(skypeDB)
            printCallLog(skypeDB)
            printMessages(skypeDB)
        else:
            print '[!] Skype Database '+\
              'does not exist: ' + skpeDB


if __name__ == '__main__':
    main()
