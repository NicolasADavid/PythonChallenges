class Logger(object):

    def __init__(self):
        self.last_log_time = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.last_log_time:
            last_time_logged = self.last_log_time[message]
            if timestamp - last_time_logged < 10:
                return False
        
        self.last_log_time[message] = timestamp
        return True
            
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)