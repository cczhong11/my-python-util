# Introduction

This package is some common functions I used in my personal project. 

## Installation

1. download the whole package
2. `pip install .`

You can also put `-e git+git@github.com:cczhong11/my-python-util.git#egg=time_util` in `requirements.txt`


## time_util

- add_time
  - input: Datetime object, days=0, hours=0, minutes=0, seconds=0
  - output: Datetime object
- date_durations
  - input:Datetime object , Datetime object
  - output: days
- get_current_date
  - input: str: timezone
  - output: Datetime object
- get_datetime_from_timestamp
  - input:int timestamp
  - output: Datetime object
- get_next_day
  - output: Datetime object
- get_week_num
  - input : Datetime object
  - output: int
- get_week_start_end
  - input: week num
  - output: Datetime object, Datetime object
- get_yesterday
  - input : Datetime object
  - output: Datetime object
- parse_time
  - input : str, str(pattern)
  - output: Datetime object
- seconds_to_hour
  - input : int(seconds)
  - output: str
- str_time
  - input : Datetime object
  - output: str



## web_util


- read_json_file
  - input : str (filename)
  - output: Dict
- dump_json_file
  - input: Dict , str (filename)
  - output: None
- parse_curl
  - input: str(curl)
  - output: str (url), Dict (headers)
- get_top
  - input: Dict, int (top)
  - output: List[str] (markdown list)
- upload_img
  - input: str (url), str (data type), str (folder), str(name)
  - output: None 


## sqlite_util

- create_datebase
  - input: filename, create_query
  - output: none
- insert_database
  - input: filename, insert_query, tuple (object)
  - output: None
- select_database
  - input: filename, select_query
  - output: List[Tuple]
- update_database
  - input: filename, update_query, tuple (object)
  - output: None