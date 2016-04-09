import os, platform, sys, logging, urllib2

INSTALL_DIR = os.getcwd()
print('Installing to: %s' % INSTALL_DIR)

############################################

GITHUB_MASTER = 'https://raw.githubusercontent.com/khilnani/pythonista/master/tools/'
S3BACKUP_FILE = 's3backup.py'
S3CONF_FILE = 'sample.aws.conf'
S3CONF_DEST_FILE = 'aws.conf'

############################################

def setup_logging(log_level='INFO'):
  log_format = "%(message)s"
  logging.addLevelName(15, 'FINE')
  logging.basicConfig(format=log_format, level=log_level)


def download_file(src, dest):
  logging.info('Reading %s' % (src))
  file_content = urllib2.urlopen(src).read()
  logging.info('Writing %s' % dest)
  f = open(dest, 'w')
  f.write(file_content)
  f.close()
  logging.info('Done.')

############################################

def main():
  setup_logging()
  download_file(GITHUB_MASTER+S3BACKUP_FILE, os.path.join(INSTALL_DIR, S3BACKUP_FILE))
  download_file(GITHUB_MASTER+S3CONF_FILE, os.path.join(INSTALL_DIR, S3CONF_DEST_FILE))
  print 'Please edit %s and then run: %s' % (S3CONF_DEST_FILE, S3BACKUP_FILE)

############################################

if __name__ == '__main__':
  main()