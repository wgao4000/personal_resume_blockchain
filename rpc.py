# coding:utf-8
from xmlrpc.server import SimpleXMLRPCServer  
from xmlrpc.client import ServerProxy
from node import get_nodes, add_node
from database import BlockChainDB, UnTransactionDB, TransactionDB
from lib.common import cprint
server = None

PORT = 8301

class RpcServer():

    def __init__(self,server):


    def ping(self):
   
    
    def get_blockchain(self):


    def new_block(self,block):


    def get_transactions(self):


    def new_untransaction(self,untx):


    def blocked_transactions(self,txs):
 

    def add_node(self, address):


class RpcClient():



    def __init__(self, node):

    
    def __getattr__(self, name):
        def noname(*args, **kw):

        return noname

class BroadCast():

    def __getattr__(self, name):
        def noname(*args, **kw):


def start_server(ip, port=8301):


def get_clients():
