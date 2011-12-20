from twisted.internet import defer

from services import GenericService, no_response
import helpers

'''
Mapping of new Electrum protocol to old one:
    done blockchain.block.get_blocknum() -> b
    done blockchain.address.get_history(address) -> h
    done blockchain.transaction.broadcast(tx) -> tx
    
    done node.get_peers -> peers
    node.stop -> stop
    
    load
    clear_cache
    get_cache
        
    session
    new_session
    update_session
    poll
'''

class BlockchainBlockService(GenericService):
    service_type = 'blockchain.block'
    service_vendor = 'Electrum'
    is_default = True
    
    def subscribe(self):
        return True
    
    def unsubscribe(self):
        return True

    @defer.inlineCallbacks
    def get_blocknum(self):
        # FIXME: Own implementation
        print (yield helpers.ask_old_server('b'))
        defer.returnValue(True)
    
class BlockchainAddressService(GenericService):
    service_type = 'blockchain.address'
    service_vendor = 'Electrum'
    is_default = True
    
    def subscribe(self, address):
        return True
    
    def unsubscribe(self, address):
        return True

    def get_history(self, address):
        # FIXME: Own implementation
        return helpers.ask_old_server('h', address)
    
    def get_balance(self, address):
        # FIXME: Own implementation
        return helpers.ask_old_server('b', address)
    
class BlockchainTransactionsService(GenericService):
    service_type = 'blockchain.transactions'
    service_vendor = 'Electrum'
    is_default = True
    
    def subscribe(self):
        return True
    
    def unsubscribe(self):
        return True

    def guess_fee(self):
        # FIXME: Blockchain analysis
        return 0.0005
    
class BlockchainTransactionService(GenericService):
    service_type = 'blockchain.transaction'
    service_vendor = 'Electrum'
    is_default = True
    
    @defer.inlineCallbacks
    def broadcast(self, transaction):
        # FIXME: Own implementation
        if not (yield helpers.ask_old_server('tx', transaction)):
            defer.returnValue(False)
        defer.returnValue(True)
    
    def get(self, hash):
        raise NotImplemented
