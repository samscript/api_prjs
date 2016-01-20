# API PROJETCS

from bottle import route, run, template, request, redirect, tob
import dateparser
import json
import datetime
import re
import urllib
import validators
import webbrowser

# Free Code Camp TimeStamp Microservice
# Using:
#   .https://dateparser.readthedocs.org/en/latest/index.html
#   .http://bottlepy.org/docs/dev/index.html

def parsed_entry(entry):
    return dateparser.parse(entry)

def is_unix_stamp(entry):

    parsed = parsed_entry(entry)

    str1 = str(parsed)

    # 1st check if its an integer which should be a unix timestamp
    if entry.isdigit():
            return True

    # 2nd we are going to check if the string is not a natural date
    elif parsed == None:
        return None

    # if the string is a natural language we return False
    else:
        return False

def unix_stamp(parsed):
    unix_start_time = dateparser.parse(' 1970 1 1')
    return (parsed - unix_start_time).total_seconds()

def returned_date(parsed):
    month   = parsed.strftime("%B")
    day     = parsed.day
    year    = parsed.year

    return month + " " + str(day) + ", " + str(year)

def return_json(unix, date):
    return json.dumps({"unix":unix,"natural":date})

def processing_input_output(entry):

    if is_unix_stamp(entry) == True:
        # unix timestamp
        # return "unix timestamp"
        unix_to_date =  dateparser.parse(' 1970 1 1') + datetime.timedelta(0,int(entry))

        return return_json( str(entry), returned_date(unix_to_date) )

    elif  is_unix_stamp(entry) == False:
        # natural language date
        return return_json(unix_stamp(parsed_entry(entry)), returned_date(parsed_entry(entry)))
    else:
        # neither unix timestamp nor natural language date
        return return_json(None, None)

@route('/')
@route('/datetime/<entry>')
def date_time(entry):
    return processing_input_output(entry)

# ###################################################################################################

# Free Code Camp Request Header Parser Microservice
# Using:

def return_json1(ip1, lg, os):
    return json.dumps({"ipaddress":ip1,"language":lg, "software":os})

def return_regex_str(regex, string1 ):
    return re.findall(regex ,string1)
    
def get_my_ip():
    # due to problem in c9.io can't get my ip with REMOTE_ADDR
    # this function is a solution for this prob
    link = "http://curlmyip.com/"
    f = urllib.urlopen(link)
    return f.readline().strip()

@route('/whoami')
def show_info():
    # PHP header request
    if request.environ.get('HTTP_X_FORWARDED_FOR') != None:
        # we are behind a proxy
        ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.environ.get('REMOTE_ADDR')
    # ip                      = get_my_ip()
    language                = request.environ.get('HTTP_ACCEPT_LANGUAGE')
    software                = request.environ.get('HTTP_USER_AGENT')
    # using regex to get the part I need
    software_string_regexed = return_regex_str("\(.*?\)", software )[0]
    language_string = (language ).split(",")[0]

    return return_json1(ip, language_string, software_string_regexed[1:len(software_string_regexed)-1])

# ###########################################################################################################

# FreeCodeCamp Url Shortener Microservice
# Using:
#       https://github.com/kvesteri/validators

url_dict = dict()

def return_json5(original_url, shortened_url):
    return json.dumps({"short_url":shortened_url, "entered_url":original_url})


def adjusted_entry(entry):
    #if url have 'http://' in it
    if entry.split('://')[0] == 'http' or entry.split('://')[0] == 'https':
        return entry
    #if url have not 'http://' in it
    else:
        return 'http://' + entry

def valid_url(entry):
        return validators.url(adjusted_entry(entry))

def shorten_url(entry):
    url1 = adjusted_entry(entry)
    length = len(url_dict)
    url_dict[str(length)] = url1
    return return_json5(entry, "api-prjs-samscript.c9users.io/url_short/" + str(length))

@route('/shorten_url/<entry:path>')
def shortened_url(entry):
    if valid_url(entry):
        return shorten_url(entry)
    else:
        return return_json5(entry, "error - entered invalid url")

@route('/url_short/<entry>')
def call_short_url(entry):
    # webbrowser.open_new(url_dict[entry])
    # webbrowser.open(url_dict[entry], new=0, autoraise=True)
    redirect(tob(url_dict[entry]))
    
# ###########################################################################################################

run(host='0.0.0.0', port=8080, debug=True)