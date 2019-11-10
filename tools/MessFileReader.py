# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:16:59 2019

@author: Bartek
"""

import json
import datetime
import pandas as pd

from bisect import bisect_left
from colorama import Fore
from itertools import cycle, islice

import pprint
pp = pprint.PrettyPrinter(depth=6)
  
def _parse_obj(dct):
    for key in dct:
        if type(dct[key]) == str:
            dct[key] = dct[key].encode('latin_1').decode('utf-8')
        if type(dct[key]) == int:
            dct[key]  = datetime.datetime.fromtimestamp(dct[key]/1000.0)  
    return dct
    
def readFile(path):
    with open(path + '/' + "message_1.json") as f: # Use file to refer to the file object
        conv = json.load(f, object_hook=_parse_obj)  
    return conv

def getConvInfo(conv):
    dic = {}
    dic['title'] = conv['title']
    dic['participants'] = conv['participants']
    dic['thread_path'] = conv['thread_path']
    dic['last message'] = conv["messages"][0]['timestamp_ms']
    l = len(conv["messages"])
    dic['first message'] = conv["messages"][l-1]['timestamp_ms']
    return dic

def getMessages(conv, ignore_quiters = False):
    messages = conv["messages"]
    messages.reverse() #reverse to get chronological order
    
    if ignore_quiters: #Delete people who quite conv 
        participants = [node['name'] for node in conv['participants']]
        messages = [mess for mess in messages if mess['sender_name'] in participants]
    return messages

def findByDate(messages, day, month, year):
    timestamps = [mess['timestamp_ms'] for mess in messages]
    t = datetime.datetime(year, month, day)
    i = bisect_left(timestamps, t)
    return i

def preetyPrintMess(messages, conv_params, start, stop):
    l = messages[start:stop]
    part = [i['name'] for i in conv_params['participants'] ]
    cols = [ Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    cols_match = list(islice(cycle(cols), len(part)))
    rule = dict(zip(part, cols_match))
    for mess in l:
        try:
            dt = mess['timestamp_ms']
            print(rule[mess['sender_name']]) # Set color
            print(mess['sender_name'], dt.date(), str(dt.time())[:-7])#Sill timestamp
            print(mess['content'])
            print(Fore.RESET) #Reset color
        except KeyError: #In case of strange errors
            print(mess)
 
def mineConv(messages, conv_params, sender):

    #Leave only messages with propere sender and if they contain content
    send_mess = [mess for mess in messages if mess['sender_name'] == sender and 'content' in mess.keys()]
    
    df_orgin = []
    for mess in send_mess:
        df_orgin.append((mess['content'], conv_params['title'], mess['timestamp_ms']))
        
    df = pd.DataFrame(df_orgin, columns = ['text','conv','timestamp']) 
    return df   





