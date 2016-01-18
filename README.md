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