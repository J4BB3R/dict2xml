#!/usr/bin/python
#
#   Author : J4BB3R<johan.maurel@protonmail.com>
#   Init-Date : 12/01/2017
#   LastDate : 12/01/2017
#   Description : These file contain funcs who give the ability to convert dict into XML
"""

    THIS DICT :

    dict : {
        "opt" : "nope"
        "data" : {
            "foo" : "none"
            DATA_SEP : "Random Data"
        }
    }

    GIVE IN XML :

    <dict opt=nope>
        <data foo=none>Random Data</data>
    </dict>

"""


__author__ = "Johan Maurel"

XML_HEAD = "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>\n"

dataSep = "><" # To store data <Foo>Bar</Foo> like XML we've define dataSep to give the fields who's store the "Bar"

def _browseIntoDictTree( d, s, v, t): # Recursive func who browse dict tree and concat string to create a xml file

    tab = t
    val = v
    paramCnt = 0
    dictCnt = 0
    orderBuff = {}
    key = None

    for k, v in d.items():

        if isinstance(v, dict):
            orderBuff[dictCnt] = k
            dictCnt += 1

        else:
            paramCnt -= 1
            orderBuff[paramCnt] = k

    for i in range(tab): val += '\t';


    val += "<"+s
    for kb in sorted(orderBuff):

        key = orderBuff.get(kb)
        value = d.get(key)

        if isinstance(value, dict):

            if kb == 0:
                val += ">"
                if dataSep in value == True:
                    val += "\n"
            if dataSep in value == False and val[-1] != '\n': # To not concat \n twice when the first element is an other markup
                val += "\n"

            tab += 1
            tab, val = _browseIntoDictTree(value, key, val, tab) # Go down into the tree

        elif key == dataSep:
            val += ">"+value+"</"+s+">\n"

        else:
            val += " "+key+"=\""+value+"\""

    if key != dataSep:
        for i in range(tab): val += '\t';
        val += "</"+s+">\n"

    tab -= 1
    return tab, val

def applyIntoDict(d, cfg): # Replace data in a dict with a filled clone of himself
                           # (it's to fill fields with some data set in a blank dict)
    for key, value in cfg.items():
        if key in d:
            if isinstance(value, dict) and isinstance(d[key], dict):
                d[key] = applyIntoDict(d[key], cfg[key])
            elif not isinstance(value, dict) and not isinstance(d[key], dict):
                d[key] = cfg[key]
            else: pass
    return d

def dict2xml(dict, key, dataSeparator): # Give a dict a name for the first markup and a separator
    dataSep = dataSeparator
    val = ""
    val += XML_HEAD
    tab, val = _browseIntoDictTree( dict, key, val, 0)
    return val
