from dateutil import parser

def parse_date(date):
    return parser.parse(date.replace(":","-", 2))
