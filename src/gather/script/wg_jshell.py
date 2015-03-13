# -*- coding: utf-8 -*-
import getopt
import sys

import django

from gather.script.grabber import Grabber


help_text="""Usage: python wg_jshell.py [options]

Options:
  -j ..., --jobid=...              the jobid
  -h, --help                       show this help

Examples:
  wg_jshell.py --jobid=1     scan the job with the id 1
"""
def print_help():
    print >>sys.stderr, help_text
    sys.exit(1)

#启动抓取任务的操作菜单
def main(args):
    
    try:                                
        opts, args = getopt.getopt(args, "hj:n:", ["help", "jobid=", "placeholders="])
    except getopt.GetoptError:
        print_help()
        
    job_id = 421
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
        elif opt in ("-j", "--jobid"):
            try:
                job_id=int(arg)
            except:
                print "jobid must be interger"
    the_grabber = Grabber()
    placeholders={}
    thread_num=1
    the_grabber.startscan(job_id,placeholders, thread_num)
    
   

if __name__ == '__main__':    
    django.setup()
    main(sys.argv[1:])

