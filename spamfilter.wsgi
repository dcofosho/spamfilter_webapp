import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/spamfilter')
from spamfilter import app as application
application.secret_key = 'totally_secure_key' 
