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
    

class GoldRetentionPlan(RetentionPlan):
    retention_days = 42
    month_retention_period = 12
    
    def retain_snapshot(self, input_date: date) -> bool:
        if not self.input_validation(input_date):
            raise TypeError(
                f"Expected a <class 'datetime.date'> instance but received \
                    {type(input_date)} instance.")
            
        if self.retention_days_check(input_date):
            return True
        elif self.month_retention_period_check(input_date):
            return True
        return False
    
    def retention_days_check(self, input_date: date) -> bool:
        retention_time = datetime.now().date() \
            - timedelta(days=self.retention_days)
            
        if retention_time > input_date or datetime.now().date() < input_date:
            return False
        return True
    
    def month_retention_period_check(self, input_date: date) -> bool:
        current_year = (
            True if input_date.year == datetime.now().year else False
            )
        if current_year:
            last_day_month = (
                True if (input_date + timedelta(days=1)).month \
                    != input_date.month else False
                )
            if last_day_month:
                return True
        return False
    
    def input_validation(self, input) -> bool:
        if type(input) != date:
            return False
        return True
        

class PlatinumRetentionPlan(RetentionPlan):
    retention_days = 42
    month_retention_period = 12
    year_retention_period = 7
    
    def retain_snapshot(self, input_date: date) -> bool:
        if not self.input_validation(input_date):
            raise TypeError(
                f"Expected a <class 'datetime.date'> instance but received \
                    {type(input_date)} instance.")
            
        if self.retention_days_check(input_date):
            return True
        elif self.month_retention_period_check(input_date):
            return True
        else:
            if self.year_retention_period_check(input_date):
                return True
        return False
    
    def retention_days_check(self, input_date: date) -> bool:
        retention_time = datetime.now().date() \
            - timedelta(days=self.retention_days)
            
        if retention_time > input_date or datetime.now().date() < input_date:
            return False
        return True
    
    def month_retention_period_check(self, input_date: date) -> bool:
        current_year = True if input_date.year == datetime.now().year else False
        if current_year:
            last_day_month = (
                True if (input_date + timedelta(days=1)).month != input_date.month \
                    else False
                )
            if last_day_month:
                return True
        return False
    
    def year_retention_period_check(self, input_date: date) -> bool:
        retention_limit_year = datetime.now().date() - timedelta(days=365 * 7)
        if retention_limit_year <= input_date:
            if input_date.day == 31:
                return True
        return False
    
    def input_validation(self, input) -> bool:
        if type(input) != date:
            return False
        return True
