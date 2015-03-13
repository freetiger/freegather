# -*- coding: utf-8 -*-

from Queue import Queue
import datetime
import re
import threading
import utils

from gather.job.models import Job, Scan
from gather.script.models import PageInfo, BlockMatch, RegularMatch, LoopInfo

'''
抓取的主程序：在数据库中设置抓取前的任务状态，启动抓取线程，启动输出抓取结果的线程，在数据库中设置抓取任务的状态
'''
class Grabber(object):

    def __init__(self):
        #抓取规则
        self.page_info_list = []      
        self.grbQueue = Queue()  #抓取队列      
        self.output_queue = Queue()    #结果输出队列
        self.cgqueue = Queue()
        
        self.job_id = None
        self.scan_id = 0
    
    def startscan(self, job_id, job_name="", get_rules="",placeholders={}, thread_num=0):
        #
        self.job_id = job_id
        #
        self.cleanParams(job_name, get_rules, placeholders, thread_num)
        #扫描开始，设置数据库状态
        scan = Scan(job_id=job_id, job_name=job_name, get_rules=get_rules, placeholders=placeholders, scan_start=datetime.datetime.now(), scan_end=datetime.datetime.now(), thread_num=thread_num)
        scan.save()
        self.scan_id = scan.id
        #
        self.page_info_list = self.convertRulesToPageInfos(get_rules, placeholders)
        
        #启动抓取线程，线程处于ready状态
        for i in range(thread_num):
            t = GatherWorker("GatherWorker_"+str(i), self.page_info_list,self.grbQueue, self.output_queue)
            t.setDaemon(True)
            t.start()
        #创建输出最终结果的txt，启动输出结果的线程，线程处于ready状态
        #清空输出结果文件
        outputfile = open(OutputFileScanResult.outputfilename,"w")
        outputfile.close()
        #将结果输出到文件
        for i in range(0,1):
            t = OutputFileScanResult(threadname="OutputFileScanResult_"+str(i), scan_id=self.scan_id, output_queue=self.output_queue)
            t.setDaemon(True)
            t.start()            
        
        #设置抓取第一步，用第一个正则语句块进行抓取。（广度优先）
        runtime_status = {}
        self.grbQueue.put((0,runtime_status))
        #等待grbQueue线程队列结束
        self.grbQueue.join()
        #等待output_queue队列结束
        self.output_queue.join()   
        
        #将结果文件内容输出到数据库
        outputfile = open(OutputFileScanResult.outputfilename,"r")
        line = outputfile.readline()    # 调用文件的 readline()方法
        while line:
            from gather.job.models import ScanResult
            scanResult = ScanResult(scan_id=self.scan_id, scan_result=line.strip('\n'))
            scanResult.save()
            print line.strip('\n')
            line = outputfile.readline()
        outputfile.close()
        
        #完成扫描，设置数据库状态
        scan = Scan.objects.get(pk=self.scan_id)
        scan.scan_end=datetime.datetime.now()
        scan.is_finish = '1'
        scan.save()
        print "finish"
        
        return
        
    def cleanParams(self, job_name="", get_rules="",placeholders={}, thread_num=0):
        job = Job.objects.get(pk=self.job_id)
        print job
        if job_name=="":
            job_name = job.job_name
        if get_rules=="":
            get_rules = job.get_rules
        #传入的参数覆盖数据库中的数值
        if len(job.placeholders)>0:
            temp_placeholders = eval(job.placeholders)
            for placeholder_key in placeholders:
                temp_placeholders[placeholder_key] = placeholders[placeholder_key]
        else:
            temp_placeholders = placeholders
        #
        placeholders = temp_placeholders
        #
        if thread_num<=0:
            thread_num = job.thread_num
            
    def convertRulesToPageInfos(self, get_rules="",placeholders={}):
        page_infos = []
        page_info_list = []
        #替换规则中的占位符
        if len(get_rules)>0:
            for placeholder_key in placeholders:
                get_rules = get_rules.replace("{{"+placeholder_key+"}}", placeholders[placeholder_key])
            exec(get_rules)
            page_info_list = eval("page_info_list")
        #将抓取规则转换为对象
        for path in page_info_list:
            #页面信息
            page_info = PageInfo()
            page_info.urls = path.get("urls", [])
            page_info.encoding = path.get("encoding", "")
            page_info.description = path.get("description", "")
            page_info.is_end = path.get("is_end", "")
            page_info.output_keys = path.get("output_keys", "")
            page_info.post_datas = path.get("post_datas", {})
            #正则匹配
            regular_matchs = []
            temp_regular_matchs = path.get("regular_matchs", [])
            if temp_regular_matchs:
                for temp_regular_match in temp_regular_matchs:
                    regular_match = RegularMatch()
                    regular_match.result = temp_regular_match.get("result", "")
                    regular_match.is_unique = temp_regular_match.get("is_unique", "")
                    regular_match.is_scroll = temp_regular_match.get("is_scroll", "")
                    regular_match.omit_tags = temp_regular_match.get("omit_tags", "")
                    regular_match.regulars = temp_regular_match.get("regulars", [])
                    regular_matchs.append(regular_match)
            page_info.regular_matchs = regular_matchs
            #块匹配
            block_match = None
            temp_block_match = path.get("block_match", None)
            if temp_block_match is not None:
                block_match = BlockMatch()
                block_match.result = temp_block_match.get("result", "")
                block_match.start_str = temp_block_match.get("start_str", "")
                block_match.end_str = temp_block_match.get("end_str", "")
            page_info.block_match = block_match
            #
            loop_info = None
            temp_loop_info = path.get("loop_info", None)
            if temp_loop_info is not None:
                loop_info = LoopInfo()
                loop_info.offset = temp_loop_info.get("offset", "1")
                loop_info.limit = temp_loop_info.get("limit", "0")
                loop_info.step = temp_loop_info.get("step", "1")
                loop_info.is_need_loop = temp_loop_info.get("is_need_loop", "1")
                loop_info.loop_urls = temp_loop_info.get("loop_urls", [])
            page_info.loop_info = loop_info
            #
            page_infos.append(page_info)
        return page_infos
    
  
'''
抓取页面线程，通过设置的规则，抓取到页面，并解析页面，解析结果存入中间数据队列
'''  
class GatherWorker(threading.Thread):
    
    def __init__(self, threadname="未设置线程名", page_info_list=[], queue=None,output_queue=None):
        
        threading.Thread.__init__(self, name = threadname)
        #执行抓取的线程队列
        self.sharedata = queue
        #抓取规则
        self.page_info_list = page_info_list #PageInfo的list集合
        #输出队列
        self.output_queue = output_queue


    def run(self):

        print self.getName(),'Started'
        
        while True:            
            items = self.sharedata.get()
            self.parsePage(items[0],items[1])
            self.sharedata.task_done()           
        
        print self.getName(),'Finished'

    '''
            根据输出列表output_keys的规则将抓取结果runtime_status（一条结果，即一行结果）整理后存入output_queue
    '''
    def outputvalues(self,output_keys,runtime_status):
    
        output_v = []
        for kys in output_keys:
            if kys in runtime_status:
                output_v.append(self.removeMask(runtime_status[kys]))
                #print removeMask(runtime_status[kys])
            elif kys.endswith("*"):
                prex_key = kys[:-1]
                n = 1
                while prex_key+str(n) in runtime_status:
                    output_v.append(self.removeMask(runtime_status[prex_key+str(n)]))                   
                    n = n+1
            elif kys.startswith("$"):
                output_v.append(kys[1:])
            else:
                output_v.append("n\\a")

        self.output_queue.put(output_v)   
        
    #中间变量换为实际值：source中包含占位符${}，runtime_status中存储了占位符的实际值
    def setVariables(self, source,runtime_status):
        param_retrieve_str = re.compile(r'\$\{([^}]*)\}')
        params = param_retrieve_str.findall(source)
        for items in params:
            if items not in runtime_status:
                print "can't find "+items+" in runtime status when setVariables"
                return ""
            else:
                source = source.replace('${'+items+'}',str(runtime_status[items]))
        #eval执行
        param_retrieve_str = re.compile(r'\$eval\{([^}]*)\}')
        params = param_retrieve_str.findall(source)
        for items in params:
            source = source.replace('$eval{'+items+'}',str(eval(items)))
        return source     
    

    
    '''
            移除字符串中的html标签
    '''
    def removeMask(self, instr):
    
        instr = instr.replace(chr(13),"")
        instr = instr.replace(chr(10),"")
        instr = instr.replace(chr(9),"")
        instr = instr.replace("&nbsp;","")
    
        #去掉标签
        normalTagreg =re.compile("(<\s*(?:span|a|font|p|h|h1|h2|h3|)?[^>]*>)")
        tags = normalTagreg.findall(instr)
        for tagstr in tags:
            instr = instr.replace(tagstr,"")
            
        return instr
    
    '''
            移除html标签，特别的：br标签替换成一个空格
    '''
    def remove_tag(self, page_src,omit_tag):
        
        chunk_list = []
        tag_head = "<"+omit_tag
        b_pos = page_src.find(tag_head)
        e_pos = 0
        while b_pos>=0 and e_pos>=0:
            if omit_tag.startswith("br"):
                chunk_list.append(page_src[e_pos:b_pos]+" ")
            else:
                chunk_list.append(page_src[e_pos:b_pos])
            e_pos = page_src.find(">",b_pos)+1
            b_pos = page_src.find(tag_head,e_pos)
        if b_pos == -1 and e_pos >=0:
            chunk_list.append(page_src[e_pos:])
        return ''.join(chunk_list)
    
    '''
            批量移除html标签，特别的：br标签替换成一个空格
    page_src= '<div>he<a href="www.baidu.com">yu</a>'xing</div>
    omit_tags=['a','/a','br/','p','/p','div','/div','span','/span']
    return 'heyuxing'
    '''
    def remove_tags(self, page_src, omit_tags=[]):
        if omit_tags is not None:
            for omit_tag in omit_tags:
                page_src = self.remove_tag(page_src,omit_tag)
        return page_src
                
    '''
            依据块的定位符，从应答页面中分理出需要详细解析的结果块，可以有多块结果。
    result：value
            块名字：块数据
    http://www.baidu.com/s?wd=github
    return [{"title_result":"<a>oschina (开源中国) · </a>"}, {"title_result":"<a>首页、文档和下载 - 代码托管服务 - 开源中国社区</a>"}, ]
    '''
    def parse_block_match(self, page_src, block_match):
        block_data_map_list = []
        if block_match is not None:
            start_str = block_match.start_str
            end_str = block_match.end_str
            result = block_match.result
            if start_str.strip()=="" or end_str.strip()=="":
                block_data_map_list.append({result:page_src})
                block_num=1
            else:
                tmp_src = page_src.replace("\n","").replace("\r","")
                b_pos = tmp_src.find(start_str)
                block_num = 0
                while b_pos >= 0:
                    block_num += 1
                    e_pos = tmp_src.find(end_str,b_pos+len(start_str))
                    block_data_map_list.append({result:tmp_src[b_pos:e_pos]})
                    if e_pos>=0:
                        b_pos = tmp_src.find(start_str,e_pos)
                    else: #未找到结束块e_pos为负值，跳出while循环
                        b_pos = e_pos
            print  result,block_num
        if len(block_data_map_list) == 0:
            block_data_map_list =[{}]   #默认一块
        return block_data_map_list
                
    '''
            解析raw_url请求（数据块、页面链接）
    raw_url:获取页面的链接（或数据）
    page_info:解析页面的规则
    runtime_status：运行时的一些状态，中间值、解析结果等
    '''
    def parse_page_data(self, raw_url,page_info,runtime_status,post_datas={}):
        #获取raw_url的应答页面，并处理好编码问题
        page_encoding = "UTF-8"
        if page_info.encoding.strip():
            page_encoding = page_info.encoding
        #
        raw_url = raw_url.decode("UTF-8","ignore").encode(page_encoding,"ignore")
        page_src = utils.getUrlContent(raw_url,post_datas)
        #
        if page_encoding == "unicode":
            page_src = eval("u'"+page_src+"'").encode('utf-8',"ignore")
        else:
            page_src = page_src.decode(page_encoding,"ignore").encode('utf-8',"ignore")
        
        #开始解析获得页面page_src      
    
        #依据块的定位符，从应答页面中分理出需要详细解析的结果块，可以有多块结果
        block_data_map_list = self.parse_block_match(page_src, page_info.block_match)
                
        #整个页面用正则表示式匹配，匹配结果都要补入块匹配的结果block_data_map_list中每一天记录中   
        for regular_match in page_info.regular_matchs:
            datalist = []   #正则表达式中捕获到的数据
            #使用exp中的正则表达式匹配出相关结果
            for regular in regular_match.regulars:
                tmp_src = page_src  #page_src循环匹配中会多次使用
                tmp_src = self.remove_tags(tmp_src, regular_match.omit_tags)
                pagedata_ret = re.compile(regular)
                tmp_datalist = pagedata_ret.findall(tmp_src)
                datalist.extend(tmp_datalist)
                
            #正则表达式未匹配到值时，前面的解析结果中有相关值则赋值到datalist中   
            if len(datalist)==0:
                tmp_list = []
                tmp_n = 0
                while (regular_match.result+str(tmp_n)) in runtime_status:
                    tmp_list.append("n/a")
                    tmp_n = tmp_n + 1
                datalist.extend(tmp_list)
                
            #   
            tmp_addon_list = [] #新增加的行结果记录
            scroll_str = "" #正则匹配结果折叠                
            for data_i in range(0,len(datalist)):
                #如果is_unique等于一，则只取匹配结果中的第一个值。等于0时取所有的结果
                if regular_match.is_unique == "1" and data_i>0:
                    continue          
                data = datalist[data_i]
                grub_status = {}
                
                #正则表达式中没有括号或者只有一个捕获型括号，返回的字符串list ['qqq', 'hyx',]
                #正则表达式中有多个捕获型括号，返回的字符串list [('qqq', 'hyx'),('12','hellooo'),]
                if type(data) == type("a"):
                    grub_status[regular_match.result+"1"]=data
                    scroll_str = scroll_str + data + "||"
                else:
                    for i in range(0,len(data)):                    
                        grub_status[regular_match.result+str(i+1)]=data[i]
                        scroll_str = scroll_str + data[i] + "||"            
    
                if regular_match.is_scroll!="1":
                    #block_data_map_list记录数不变，每一条数据扩展上grub_status，成为tmp_addon_list
                    for items in block_data_map_list:
                        tmp_map = {}
                        tmp_map.update(grub_status)
                        tmp_map.update(items)
                        tmp_addon_list.append(tmp_map)   
                else:
                    pass
            #将新增加的行记录tmp_addon_list加入到block_data_map_list结果中，记录数增加
            if regular_match.is_scroll!="1":
                if len(tmp_addon_list) == 0:
                    tmp_addon_list = [{}]
                else:
                    block_data_map_list = []
                    for items in tmp_addon_list:
                        if len(items)>0:
                            block_data_map_list.append(items)
            else:
                tmp_addon_list = []
                for items in block_data_map_list:
                    if len(items)>0:
                        tmp_addon_list.append(items)
                    
                block_data_map_list = []
                if len(tmp_addon_list)==0:
                    tmp_addon_list = [{}]
                for items in tmp_addon_list:
                    items[regular_match.result] = scroll_str
                    block_data_map_list.append(items) 
                
    
        return block_data_map_list
    
    '''
            执行第parse_step步抓取，runtime_status是中间状态值
    '''
    def parsePage(self,parse_step,runtime_status):
    
        print "parsePage call" + str(parse_step)
        next_status = {}
        if parse_step>= len(self.page_info_list):
            return
        #所有的抓取规则都执行了，或者遇到终止标识，提前终止抓取。根据规则将结果存入output_queue.
        if parse_step >= len(self.page_info_list)-1 or self.page_info_list[parse_step].is_end == "1":
            self.outputvalues(self.page_info_list[len(self.page_info_list)-1].output_keys,runtime_status)
            return
            
        page_info = self.page_info_list[parse_step]
        status_list = []
        #所有的抓取规则都执行了，到了输出列表处（字典page_info不包含url这个key），结束抓取
        if not page_info.urls:
            return
        #执行parse_step该步的抓取：parse_step在这个循环处没有自增，遍历的是url的集合
        for url in page_info.urls:
            next_url = self.setVariables(url,runtime_status)
            status_list = self.parse_page_data(next_url,page_info,runtime_status,page_info.post_datas)
            
            #解析结果status_list和解析时的中间结果runtime_status合并，并将合并的结果用于下一步的解析
            for tmp_status in status_list:
                if type(tmp_status) == type({}):
                    next_status = {}
                    next_status.update(runtime_status)
                    next_status.update(tmp_status)    
                    self.sharedata.put((parse_step+1 ,next_status))  
                else:
                    print "parse_page_data result error: "+str(tmp_status)   

        #is_need_loop等于一时处理循环抓取的情况，可以按照loop_url抓取下一页，还可以设置分页步进长度，分页数目
        loop_info = page_info.loop_info
        if loop_info and loop_info.is_need_loop == "1":
            hasNext = True
            lastUrl = ""
            for loop_url in loop_info.loop_urls:
                hasNext = True
                lastUrl = ""
                while hasNext:            
                    status_list = [{}]
                    offset_str = "offset"
                    limit = int(loop_info.limit)
                    step = int(loop_info.step)
                    print loop_info,limit
                    if offset_str not in next_status:
                        next_status[offset_str] = "1"
                    next_status[offset_str] = str(step + int(next_status[offset_str]))
                    offset = next_status[offset_str]
                    next_status[offset_str] = offset
                    print int(next_status[offset_str]), limit
                    if limit<=0:
                        pass
                    elif int(next_status[offset_str]) > limit:
                        print int(next_status[offset_str]), limit
                        print int(next_status[offset_str]) > limit
                        hasNext = False
                        break
                    next_url = self.setVariables(loop_url,next_status)                
                    if len(next_url) == 0 or next_url == lastUrl:   #当设置limit<=0时，抓取所有页，以此判断循环抓取结束        
                        hasNext = False
                    else:
                        lastUrl = next_url
                        status_list = self.parse_page_data(next_url,page_info,runtime_status)                
                        #解析结果status_list和解析时的中间结果runtime_status合并，并将合并的结果用于下一步的解析
                        for tmp_status in status_list:
                            if type(tmp_status) == type({}):
                                next_status.update(tmp_status)     
                                self.sharedata.put((step ,next_status))
                            else:
                                print "parse_page_data result error: "+str(tmp_status)   
        return

'''
将结果output_queue输出的最终的txt文件中
'''
class OutputFileScanResult(threading.Thread):
    from freegather.settings import BASE_DIR
    outputfilename = BASE_DIR+"/gather/script/OutputFileScanResult.txt"
    
    def __init__(self, threadname, scan_id, output_queue):
        
        threading.Thread.__init__(self, name = threadname)
        self.scan_id = scan_id
        self.sharedata = output_queue

    def run(self):

        print self.name,'Started'    
        while True:
            items = self.sharedata.get()
            self.outputfile = open(self.outputfilename,"a")
            for item in items:
                self.outputfile.write(item)
                self.outputfile.write("\t")
            self.outputfile.write("\n")
            self.outputfile.close()
            self.sharedata.task_done()

if __name__ == "__main__":   
    pass
    

    
    


