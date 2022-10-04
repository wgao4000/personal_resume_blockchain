# coding:utf-8
import time
import json
import hashlib
from model import Model
from database import TransactionDB, UnTransactionDB
from rpc import BroadCast

class Vin(Model):
    def __init__(self, utxo_hash, amount):


class Vout(Model):
    def __init__(self, receiver, amount):

    
    def get_unspent(cls, addr):


class Transaction():
    def __init__(self, vin, vout,):


    def gen_hash(self):


    
    def transfer(cls, from_addr, to_addr, amount):


    
    def unblock_spread(untx):


    
    def blocked_spread(txs):
  

    def to_dict(self):


def select_outputs_greedy(unspent, min_value): 
