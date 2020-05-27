import os
import sys
import uvicorn

from cookbook.application import APPLICATION
from cookbook.config import HOST, PORT, LOG_LEVEL

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("usage: {} <config_path>\n(example: {} dev.env)".format(cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2: usage(argv)
    uvicorn.run(app=APPLICATION,host=HOST,port=PORT,log_level=LOG_LEVEL)
