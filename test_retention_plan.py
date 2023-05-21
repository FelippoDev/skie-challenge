from datetime import date, timedelta, datetime

from pytest import mark

from retention_plan import StandardRetentionPlan, GoldRetentionPlan, \
    PlatinumRetentionPlan

@mark.standard
class StandardRetentionPlanTests:
    retention_plan = StandardRetentionPlan()
    
    def test_retain_snapshot(self):
        today = date.today()
        retention_time = today - timedelta(days=42)
        
        assert self.retention_plan.retain_snapshot(retention_time) == True
        assert self.retention_plan.retain_snapshot(today) == True
        assert (
            self.retention_plan.retain_snapshot(today + timedelta(days=1)) \
                == False
            )
        assert (
            self.retention_plan.retain_snapshot(today - timedelta(days=43)) \
                == False
            )
        
    def test_input_validation(self):
        assert self.retention_plan.input_validation("2023-05-21") == False
        assert self.retention_plan.input_validation(datetime.now()) == False
        assert self.retention_plan.input_validation(20230521) == False
        assert self.retention_plan.input_validation(date.today()) == True
        assert (
            self.retention_plan.input_validation(date.today() \
                - timedelta(days=30)) == True
            )
        assert (
            self.retention_plan.input_validation(date.today() \
                + timedelta(days=10)) == True
            )


@mark.gold
class GoldRetentionPlanTests:
    retention_plan = GoldRetentionPlan()
    
    def test_retain_snapshot(self):
        today = date.today()
        retention_time = today - timedelta(days=42)
        
        assert self.retention_plan.retain_snapshot(retention_time) == True
        assert self.retention_plan.retain_snapshot(today) == True
        assert (
            self.retention_plan.retain_snapshot(today + timedelta(days=1)) \
                == False
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                month=1, 
                day=31
                )) == True
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                month=2,
                day=28
                )) == True
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                month=4,
                day=30
                )) == True
            )
        assert (
            self.retention_plan.retain_snapshot(today + timedelta(days=370)) \
                == False
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                year=2020,
                month=1,
                day=31
                )) == False
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                year=2000,
                month=12,
                day=31
                )) == False
            )
        
    def test_retention_days_check(self):
        today = date.today()
        retention_time = today - timedelta(days=42)
        
        assert self.retention_plan.retain_snapshot(retention_time) == True
        assert self.retention_plan.retain_snapshot(today) == True
        assert (
            self.retention_plan.retain_snapshot(today + timedelta(days=1)) \
                == False
            )
    
    def test_month_retention_period_check(self):
        pass
    
    def test_input_validation(self):
        assert self.retention_plan.input_validation("2023-05-21") == False
        assert self.retention_plan.input_validation(datetime.now()) == False
        assert self.retention_plan.input_validation(20230521) == False
        assert self.retention_plan.input_validation(date.today()) == True
        assert (
            self.retention_plan.input_validation(date.today() \
                - timedelta(days=30)) == True
            )
        assert (
            self.retention_plan.input_validation(date.today() \
                + timedelta(days=10)) == True
            )

@mark.platinum
class PlatinumRetentionPlanTests:
    retention_plan = PlatinumRetentionPlan()
    
    def test_retain_snapshot(self):
        today = date.today()
        retention_time = today - timedelta(days=42)
        retention_limit_year = today - timedelta(days=365 * 7)
        
        assert self.retention_plan.retain_snapshot(retention_time) == True
        assert self.retention_plan.retain_snapshot(today) == True
        assert (
            self.retention_plan.retain_snapshot(today + timedelta(days=1)) \
                == False
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                month=1, 
                day=31
                )) == True
            )
        assert (
            self.retention_plan.retain_snapshot(today.replace(
                month=2, 
                day=28
                )) == True
            )
        assert self.retention_plan.retain_snapshot(retention_limit_year) \
            == False
        assert (
            self.retention_plan.retain_snapshot(retention_limit_year \
                - timedelta(days=1)) == False
            )
    
    def test_retention_days_check(self):
        pass
    
    def test_month_retention_period_check(self):
        pass
    
    def test_year_retention_period_check(self):
        pass
    
    def test_input_validation(self):
        pass

    