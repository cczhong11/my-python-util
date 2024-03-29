import datetime
from pytz import timezone
from typing import Tuple


def parse_time(date, pattern="%Y-%m-%d", tz="America/Los_Angeles")->datetime.datetime:
    '''
    @input: string date and its pattern
    @output: datetime obj
    '''
    tzi = timezone(tz)
    return datetime.datetime.strptime(date, pattern).replace(tzinfo=tzi)

def str_time(datetimeobj, pattern="%Y-%m-%d")->str:
    '''
	@input: datetime obj and its pattern
	@output: string for datetime
	'''
    return datetimeobj.strftime(pattern)

def get_current_date(tz="America/Los_Angeles"):
    zone = timezone(tz)
    return datetime.datetime.now(zone)

def get_week_num(cur=get_current_date()) -> int :
    '''
    return week number
    '''
    
    return int(str_time(cur, "%V"))



def date_durations(datetimeobj1, datetimeobj2)->int:
    '''
	@input: two datetime obj and second one is latter than the first one 
	@output: the duration days between two date
	'''
    return (datetimeobj2 - datetimeobj1).days

def add_time(datetimeobj, days=0, hours=0, minutes=0, seconds=0)->datetime.datetime:
    '''
	@input: add time to one datetime object
	@output: result datetime object
	'''
    return datetimeobj+datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def get_week_start_end(week_num=get_week_num()) -> Tuple[datetime.datetime, datetime.datetime]:
    CURRENTDAY = get_current_date()
    tmp_week_num = get_week_num() - week_num
    start = add_time(CURRENTDAY,days=-CURRENTDAY.weekday()-7*tmp_week_num)
    end = add_time(start, days=6)
    return start, end

def get_datetime_from_timestamp(timestamp:int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(timestamp)

def get_next_day(CURRENTDAY = get_current_date()) -> datetime.datetime:
    
    return add_time(CURRENTDAY, days=1)

def get_yesterday(CURRENTDAY = get_current_date()) -> datetime.datetime:
    return add_time(CURRENTDAY, days=-1)

def seconds_to_hour(seconds: int) -> str:  
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 