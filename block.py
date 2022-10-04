# coding:utf-8
import hashlib
import time
from model import Model
from rpc import BroadCast

class Block(Model):

    def __init__(self, index, timestamp, tx, previous_hash):


    def header_hash(self):


    def pow(self):


    def make(self, nouce):

    
    def ghash(self, nouce):


    def valid(self, nouce):


    def to_dict(self):



    def from_dict(cls, bdict):


    
    def spread(block):
  
