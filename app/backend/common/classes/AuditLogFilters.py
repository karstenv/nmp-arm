import logging

class AuditLogFilterTrue( logging.Filter ):
    def filter(self, record):
        if record.getMessage().rfind( 'Audit') :
            return False
        else:
            return True
        
        
class AuditLogFilterFalse( logging.Filter ):
    def filter(self, record):
        if record.getMessage().rfind( 'Audit') :
            return True
        else:
            return False
