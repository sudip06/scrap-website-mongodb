#### Project Highlight
This project uses scrapy to scrap guardian.com/au From the front page.It gets all links from the front page for the stories and then traverses to get the story, author, Title and url thereafter. Then it inserts all the data in mongodb.
The mongodb is installed in atlas mongodb.net. The collection name is "data".

There is a webserver implemented using Flask framework(webserver.py) which will search the substring(case insensitively) in "GET" requests(either as part of Url, Author, Body or Title) and will send the response accordingly.

### Features ###
(1) The get request can combine queries, one can filter both on Author and Title simulatenously
(2) Search request can also be done with special characters such as quote(such as " and '. Ex: http://127.0.0.1:5000/request?Title="after student uses Snapchat's 'gender") gives valid results
(3) While scrapping, we could clean up the content and advertisements by regular expressions rather than using readability.

### Limitations ###
(1) The webserver could be put on AWS(ec2-3-95-152-148.compute-1.amazonaws.com), but unfortunately, there seems some issue in accessing atlas mongodb from aws.
(2) The index has been done on Url field, but we could certainly do multiple field indexing. Its not been done as of now.

### Source code ###
The complete source code along with test test file can be downloaded by the command:
"git clone https://github.com/sudip06/scrap-website-mongodb.git"

### Way to run: ###
The scrapy can be run from the root directory by "scrapy crawl getdata". This inserts the collected data in mongodb "data" collection. The webserver can be run as
"python3 webserver.py" This launches a web server, and the following searches can be conducted:
(a) One can search the documents based on either of part of title, Author, Body or Url in the following way(The entry point is "request")
                Example:"
               (a)request?Title='Uber'"
               (b)request?Title='carbon levels'"
               (c)request?Title='carbon levels'&Body='we would arrive at the 
               same level of national wealth'
#### Query parameters for webserver: ####
3 parameters are accepted namely "Url","Title", "Body" and "Url".
The query handles invalid key values as well as example values of entries such as invalid key as "Urlxyz"

#### Testing ####
Tests have been performed through browser
##### Browser test #####
Paste onto browser the following address: http://127.0.0.1:5000/request?Url='smoking'
### Results on the browser:
Author	"Ian Sample"
Title	"Earliest known signs of cannabis smoking unearthed in China"
Url	"https://www.theguardian.com/science/2019/jun/12/earliest-known-signs-of-cannabis-smoking-unearthed-in-china"

#### Test 2
http://127.0.0.1:5000/request?Title="against 'book-up' credit"
### Result on browser:
Author	"Christopher Knaus"
Title	"Asic loses court fight against 'book-up' credit scheme in Indigenous community"
Url	"https://www.theguardian.com/australia-news/2019/jun/12/asic-loses-high-court-fight-against-book-up-credit-scheme-in-indigenous-community"

### Test 3:
http://127.0.0.1:5000/request?Title="could be wiped out by fungal infection"&Author="Charles Anderson"
### Result
Author	"Charles Anderson"
Title	"World’s fattest parrot, the endangered kākāpō, could be wiped out by fungal infection"
Url	"https://www.theguardian.com/world/2019/jun/13/worlds-fattest-parrot-endangered-kakapo-fungal-infection-new-zealand"

### Test 4
http://127.0.0.1:5000/request?
### Result
No filtering parameters passed

Usage: One can search by 4 fields, namely Title, Author, Body and Url
Example:(a)request?Title="against 'book-up' credit"
(b)request?Title="could be wiped out by fungal infection"&Author="Charles Anderson"
(c)request?Url='smoking'"

### Negative Tests
### Test 1
request?Titxyzle="could be wiped out by fungal infection"&Author="Charles Anderson"
### Result
Not a valid key to filter on

Usage: One can search by 4 fields, namely Title, Author, Body and Url
Example:(a)request?Title="against 'book-up' credit
(b)request?Title="could be wiped out by fungal infection"&Author="Charles Anderson
(c)request?Url='smoking'


#### Authors #####

    Sudip Midya - Initial Work

