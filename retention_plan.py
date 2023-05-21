from abc import ABC, abstractmethod
from datetime import datetime, timedelta, date

class RetentionPlan(ABC):
    @abstractmethod
    def retain_snapshot(self, input_date):
        pass
    
    @abstractmethod
    def input_validation(self, input):
        pass


class StandardRetentionPlan(RetentionPlan):
    retention_days = 42
    
    def retain_snapshot(self, input_date):
        if not self.input_validation(input_date):
            raise TypeError(
                f"Expected a <class 'datetime.date'> instance but received \
                    {type(input_date)} instance.")
        
        retention_time = datetime.now().date() \
            - timedelta(days=self.retention_days)
            
        if retention_time > input_date or datetime.now().date() < input_date:
            return False
        return True
    
    def input_validation(self, input) -> bool:
        if type(input) != date:
            return False
        return True
