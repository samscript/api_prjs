This my solutions for:  

Timestamp Microservice.
------------------------
I elected to use python 2.7 with 2 available 3rd party libraries:
    -dateparser
        it deals with natural language date entries
    -bottle
        it deals with web API service
        
        
Examples: 
https://api-prjs-samscript.c9users.io/datetime/86400
Response:  {"unix": "86400", "natural": "January 2, 1970"}


Request Header Parser Microservice
-----------------------------------

Examples: 
https://api-prjs-samscript.c9users.io/whoami
{"ipaddress": "10.240.0.157", "language": "en-US,en", "software": "X11; Ubuntu; Linux i686; rv:43.0"}


Url Shortener Microservice
---------------------------

Examples:

https://api-prjs-samscript.c9users.io/shorten_url/bbc.com 
or
https://api-prjs-samscript.c9users.io/shorten_url/http://bbc.com

result:
{"entered_url": "bbc.com", "short_url": "https://api-prjs-samscript.c9users.io/url_short/0"}
or
{"entered_url": "http://bbc.com", "short_url": "https://api-prjs-samscript.c9users.io/url_short/0"}

then 

you can type:

https://api-prjs-samscript.c9users.io/url_short/0 as a shortcut for bbc.com
