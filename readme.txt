Setup:
1. Install Java
   java -version
     java version "1.8.0_102"
   javac -version
     javac 1.8.0_102
2. Install python
   python
     Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32  
3. Download project from github
   cd C:\work
   git clone git@github.com:mkautomation/Fibonacci-webservice.git
4. Build and install the service
   cd C:\work\Fibonacci-webservice
   python setup.py develop

C:\work\Fibonacci-webservice>python setup.py develop
running develop
running egg_info
creating Fibonacci_webservice.egg-info
writing requirements to Fibonacci_webservice.egg-info\requires.txt
writing Fibonacci_webservice.egg-info\PKG-INFO
writing top-level names to Fibonacci_webservice.egg-info\top_level.txt
writing dependency_links to Fibonacci_webservice.egg-info\dependency_links.txt
writing manifest file 'Fibonacci_webservice.egg-info\SOURCES.txt'
file fibonacci.py (for module fibonacci) not found
file endpoints.py (for module endpoints) not found
file tests.py (for module tests) not found
package init file 'fibonacci\__init__.py' not found (or not a regular file)
package init file 'endpoints\__init__.py' not found (or not a regular file)
reading manifest file 'Fibonacci_webservice.egg-info\SOURCES.txt'
writing manifest file 'Fibonacci_webservice.egg-info\SOURCES.txt'
running build_ext
Creating c:\python27\lib\site-packages\Fibonacci-webservice.egg-link (link to .)
Fibonacci-webservice 1.0 is already the active version in easy-install.pth

Installed c:\work\fibonacci-webservice
Processing dependencies for Fibonacci-webservice==1.0
Searching for flask==0.11.1
Best match: flask 0.11.1
Processing flask-0.11.1-py2.7.egg
flask 0.11.1 is already the active version in easy-install.pth
Installing flask-script.py script to C:\Python27\Scripts
Installing flask.exe script to C:\Python27\Scripts

Using c:\python27\lib\site-packages\flask-0.11.1-py2.7.egg
Searching for click==6.6
Best match: click 6.6
Processing click-6.6-py2.7.egg
click 6.6 is already the active version in easy-install.pth

Using c:\python27\lib\site-packages\click-6.6-py2.7.egg
Searching for itsdangerous==0.24
Best match: itsdangerous 0.24
Processing itsdangerous-0.24-py2.7.egg
itsdangerous 0.24 is already the active version in easy-install.pth

Using c:\python27\lib\site-packages\itsdangerous-0.24-py2.7.egg
Searching for jinja2==2.8
Best match: jinja2 2.8
Processing jinja2-2.8-py2.7.egg
jinja2 2.8 is already the active version in easy-install.pth

Using c:\python27\lib\site-packages\jinja2-2.8-py2.7.egg
Searching for werkzeug==0.11.10
Best match: werkzeug 0.11.10
Processing werkzeug-0.11.10-py2.7.egg
werkzeug 0.11.10 is already the active version in easy-install.pth

Using c:\python27\lib\site-packages\werkzeug-0.11.10-py2.7.egg
Searching for markupsafe==0.23
Best match: markupsafe 0.23
Processing markupsafe-0.23-py2.7.egg
markupsafe 0.23 is already the active version in easy-install.pth

Using c:\python27\lib\site-packages\markupsafe-0.23-py2.7.egg
Finished processing dependencies for Fibonacci-webservice==1.0

5. Start the service
   cd C:\work\Fibonacci-webservice
   python endpoints/fibonacci_service.py		normal mode
   python endpoints/fibonacci_service.py -d		debug mode

C:\work\Fibonacci-webservice>python endpoints/fibonacci_service.py -d
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 302-049-159
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

6. Run the functional and unit test
   cd C:\work\Fibonacci-webservice
   python -m unittest tests

C:\work\Fibonacci-webservice>python -m unittest tests
0 : 1 : {u'fibonacci': [0]}
Test test_start_0_length_1 passed.
.
0 : 2 : {u'fibonacci': [0, 1]}
Test test_start_0_length_2 passed.
.
0 : 3 : {u'fibonacci': [0, 1, 1]}
Test test_start_0_length_3 passed.
.
0 : 4 : {u'fibonacci': [0, 1, 1, 2]}
Test test_start_0_length_4 passed.
.
0 : 5 : {u'fibonacci': [0, 1, 1, 2, 3]}
Test test_start_0_length_5 passed.
.
1 : 0 : {u'error': u'The "length" parameter can not be less than 1 (length >= 1)'}
Test test_start_1_length_0 passed.
.
1 : 10 : {u'fibonacci': [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]}
Test test_start_1_length_10 passed.
.
-1 : 0 : {u'error': u'The "start" parameter can not be a negative number (start >= 0)'}
Test test_start_negative_1_length_0 passed.
.
-1 : 1 : {u'error': u'The "start" parameter can not be a negative number (start >= 0)'}
Test test_start_negative_1_length_1 passed.
.
----------------------------------------------------------------------
Ran 9 tests in 9.318s

OK


C:\work\Fibonacci-webservice>python endpoints/fibonacci_service.py -d
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 302-049-159
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [26/Jul/2016 17:42:07] "GET /fibonacci?start=0&length=1 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:08] "GET /fibonacci?start=0&length=2 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:09] "GET /fibonacci?start=0&length=3 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:11] "GET /fibonacci?start=0&length=4 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:12] "GET /fibonacci?start=0&length=5 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:13] "GET /fibonacci?start=1&length=0 HTTP/1.0" 400 -
127.0.0.1 - - [26/Jul/2016 17:42:14] "GET /fibonacci?start=1&length=10 HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2016 17:42:15] "GET /fibonacci?start=-1&length=0 HTTP/1.0" 400 -
127.0.0.1 - - [26/Jul/2016 17:42:16] "GET /fibonacci?start=-1&length=1 HTTP/1.0" 400 -
