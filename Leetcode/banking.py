from banking_system import BankingSystem
import math
from collections import deque

class Refund():
    
    def __init__(self, timestamp, amount, payment_id):
        self.timestamp = timestamp
        self.amount = amount
        self.payment_id = payment_id

    def get_timestamp(self) -> str:
        return self.timestamp

    def get_amount(self) -> int:
        return self.amount

    def get_payment_id(self) -> str:
        return self.payment_id


class Account():
    
    def __init__(self, id, timestamp):
        self.id = id
        self.created_at = timestamp
        self.balance = 0
        self.total_withdrawn = 0
        self.pending_refunds = deque()
        self.payments = {}
        
    def get_balance(self) -> int:
        return self.balance
        
    def process_refunds(self, timestamp) -> None:

        while self.pending_refunds:

            next_refund = self.pending_refunds[0]

            if next_refund.get_timestamp() > timestamp:
                break

            self.pending_refunds.popleft()
            self.adjust_balance(next_refund.get_amount())
            self.payments[next_refund.get_payment_id()] = "CASHBACK_RECEIVED"
        
    def adjust_balance(self, amount) -> None:
        
        if self.balance + amount < 0:
            raise Exception("Balance cannot go below zero")
            
        if amount < 0:
            self.total_withdrawn -= amount
        
        # Execute adjustment
        self.balance += amount
    
    def pay_from(self, timestamp, amount, payment_id) -> None:
        self.adjust_balance(-amount)
        refund = Refund(timestamp + 86400000, math.floor(amount * float(.02)), payment_id)
        self.pending_refunds.append(refund)
        self.payments[payment_id] = "IN_PROGRESS"
        
    def get_payment_status(self, payment_id) -> str | None:
        if payment_id not in self.payments:
            return None
        
        return self.payments[payment_id]
        
    def get_total_withdrawn(self) -> int:
        return self.total_withdrawn
        
    def get_account_id(self) -> str:
        return self.id
        
class BankingSystemImpl(BankingSystem):

    def __init__(self):
        self.accounts = {}
        self.nextPaymentOrdinal = 1
        
    def get_and_incr_next_payment_ordinal(self) -> int:
        ret = int(self.nextPaymentOrdinal)
        self.nextPaymentOrdinal += 1
        return ret
        
    def check_account_balance(self, account_id, amount) -> bool:
        return self.accounts[account_id].get_balance() - amount >= 0
        
    def create_account(self, timestamp: int, account_id: str) -> bool:
        
        if account_id in self.accounts:
            return False
            
        account = Account(account_id, timestamp)
        self.accounts[account_id] = account
        
        return True
        
    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        
        if account_id not in self.accounts:
            return None
            
        account = self.accounts[account_id]
        account.process_refunds(timestamp)
        account.adjust_balance(amount)
        
        return account.get_balance()
        
    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        
        if source_account_id not in self.accounts:
            return None
            
        if target_account_id not in self.accounts:
            return None
            
        if target_account_id == source_account_id:
            return None
            
        source_account = self.accounts[source_account_id]
        target_account = self.accounts[target_account_id]
        
        if source_account.get_balance() - amount < 0:
            return None
            
        if target_account.get_balance() + amount < 0:
            return None
            
        source_account.adjust_balance(-amount)
        target_account.adjust_balance(amount)
        
        return source_account.get_balance()
    
    def top_spenders(self, timestamp: int, n: int) -> list[str]:
        
        accounts = sorted(self.accounts.values(), key=lambda account: (-account.get_total_withdrawn(), account.get_account_id()))
        
        return [account.get_account_id() + "(" + str(account.get_total_withdrawn()) + ")" for account in accounts[:n]]
        
    def pay(self, timestamp: int, account_id: str, amount: int) -> str | None:
                
        if account_id not in self.accounts:
            return None
            
        if not self.check_account_balance(account_id, amount):
            print("INSUFFICIENT FUNDS")
            return None
        
        account = self.accounts[account_id]
        
        account.process_refunds(timestamp)
        
        payment_id = "payment" + str(self.nextPaymentOrdinal)
        
        account.pay_from(timestamp, amount, payment_id)
        
        self.get_and_incr_next_payment_ordinal()
        
        return payment_id

    def get_payment_status(self, timestamp: int, account_id: str, payment: str) -> str | None:
        """
        Should return the status of the payment transaction for the
        given `payment`.
        Specifically:
          * Returns `None` if `account_id` doesn't exist.
          * Returns `None` if the given `payment` doesn't exist for
          the specified account.
          * Returns `None` if the payment transaction was for an
          account with a different identifier from `account_id`.
          * Returns a string representing the payment status:
          `"IN_PROGRESS"` or `"CASHBACK_RECEIVED"`.
        """
        
        if account_id not in self.accounts:
            return None
        
        account = self.accounts[account_id]
        
        account.process_refunds(timestamp)
        
        return account.get_payment_status(payment)
        
        
            
        

