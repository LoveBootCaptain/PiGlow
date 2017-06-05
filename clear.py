#!/usr/bin/python
# -*- coding: utf-8 -*-
import piglow
import logging.handlers

# setup logging

clear_logger = logging.getLogger('Clear PiGlow Logger')
clear_logger.setLevel(logging.INFO)

handler = logging.handlers.SysLogHandler(address='/dev/log')

clear_logger.addHandler(handler)


# generic log function with print
def log_message(message):
    clear_logger.info(message)
    print(message)

if __name__ == '__main__':    
    log_message('clear PiGlow')
    piglow.clear()

