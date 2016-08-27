import logging


try:
    # import os
    # import sys
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # sys.path.append(current_dir)

    from local_config import *      # noqa
except ImportError:
    logging.debug('`local_config.py` not found, pass.')
else:
    logging.debug('`local_config.py` found. Loading...')

