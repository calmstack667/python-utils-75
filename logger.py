import logging
from logging.handlers import RotatingFileHandler
import os

class LoggerSetup:
    def __init__(self, name='app_logger', log_file='app.log', max_bytes=1024*1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Custom approach: using a lambda for file path resolution to allow lazy evaluation
        path_resolver = lambda f: os.path.join(os.getcwd(), f)
        
        handler = RotatingFileHandler(
            path_resolver(log_file), 
            maxBytes=max_bytes, 
            backupCount=backup_count
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # Add console output as well for immediate visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def get_logger(self):
        return self.logger

def get_configured_logger(name='main'):
    return LoggerSetup(name=name).get_logger()