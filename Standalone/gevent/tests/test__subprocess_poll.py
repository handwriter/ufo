import sys
from gevent.subprocess import Popen
from gevent.testing.util import alarm

alarm(3)

popen = Popen([sys.executable, '-c', 'pass'])
while popen.poll() is None:
    pass
