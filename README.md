# Urlshrink
Webapp that shrinks url's just like bit.ly
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
Approach Used:-
First the user enters long url in the textfild. This address is stored in the Database with integer ID which is unique
for every record. The id is randomly generated 6-9 digit integer.
Then this id is taken and is coverted to 64 base character string(a-z,A-Z,0-9). This conversion creates the short url
which user can use to navigate to the original url.
When the user enters the short url in the text field then this short url is converted back to the integer id.
This integer id is queried in the database to find out the Original Url and then user is redirected to the original url.

Why this approach is best:-
This approach is best because it uses bijective function for conversion betweeen id and string. This easily creates a short url
from given id. Bijective function is reliable as it can not give wrong coversions. The url created are short no matter how much the
length of original url is. It is fast approach as databse used is nosql that stores key value pair and queries fast and conversion
also takes very less time.

