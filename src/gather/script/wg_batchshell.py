# -*- coding: utf-8 -*-

import sys
import getopt
from gather.script.grabber import Grabber

help_text="""Usage: python wg_batchshell.py [options]

Options:
  -j ..., --joblist=...              the joblist
  -h, --help                       show this help

Examples:
  wg_batchshell.py --joblist=1,4,6     scan the job with the id 1,4,6
"""
def print_help():
    print >>sys.stderr, help_text
    sys.exit(1)

def main(args):
   
    try:                                
        opts, args = getopt.getopt(args, "hb:", ["help", "batchid="])
    except getopt.GetoptError:
        print_help()
    joblist=None
    batchid=-1
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
        elif opt in ("-b", "--batchid"):
            try:
                batch_id=int(arg)
            except:
                print "batchid must be integer."
            if batch_id<0:
                print "batchid must be larger than zero."
    
    conn = getConnect()
    cur=conn.cursor()
    #更新抓取队列的进程id（pid）和队列状态（flag）
    cur.execute("update wg_queue set pid=%s,flag = 1 where queueid=%s",(batch_id,os.getpid()))
    conn.commit()
    #获得队列中的任务列表
    cur.execute("select job_lists from wg_queue where queueid=%s",(batch_id,))
    tmp_list = cur.fetchall()
    if len(tmp_list)>0:
        joblist = tmp_list[0][0].split(',')
    else:
        exit(1)
    conn.commit()
    conn.close()    

    for jobid in joblist:
        if len(jobid)==0:
            continue
        the_grabber = Grabber()
        the_grabber.startscan(int(jobid))
        
    conn=getConnect()
    cur=conn.cursor()
    #抓取队列抓取结束后更新队列的状态
    cur.execute("update wg_queue set flag=2 where queueid=%(batch_id)s",{'batch_id': batch_id})
    conn.commit()
    conn.close()
   

if __name__ == '__main__':
    main(sys.argv[1:])

