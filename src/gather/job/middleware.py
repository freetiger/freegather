# -*- coding: utf-8 -*-
'''
Created on 2014年12月31日

@author: heyuxing
'''

'''
使用方式：在settings的MIDDLEWARE_CLASSES中增加值 'gather.job.middleware.BusinessFilter',
'''
class BusinessFilter(object):
    '''
    在中间件类中， __init__() 方法用于执行系统范围的设置。
    出于性能的考虑，每个已启用的中间件在每个服务器进程中只初始化 一 次。 也就是说 __init__() 仅在服务进程启动的时候调用，而在针对单个request处理时并不执行。
    对一个middleware而言，定义 __init__() 方法的通常原因是检查自身的必要性。 如果 __init__() 抛出异常 django.core.exceptions.MiddlewareNotUsed ,
    则Django将从middleware栈中移出该middleware。 可以用这个机制来检查middleware依赖的软件是否存在、服务是否运行于调试模式、以及任何其它环境因素。
    在中间件中定义 __init__() 方法时，除了标准的 self 参数之外，不应定义任何其它参数。
    '''
    def __init__(self):
        print self.__repr__()+"  __init__()"
        
    '''
    这个方法的调用时机在Django接收到request之后，但仍未解析URL以确定应当运行的view之前。 Django向它传入相应的 HttpRequest 对象，以便在方法中修改。
    process_request() 应当返回 None 或 HttpResponse 对象.
    如果返回 None , Django将继续处理这个request,执行后续的中间件， 然后调用相应的view.
    如果返回 HttpResponse 对象, Django 将不再执行 任何 其它的中间件(而无视其种类)以及相应的view。 Django将立即返回该 HttpResponse .
    '''
    def process_request(self, request):
        try:
            real_ip = request.META['REMOTE_ADDR']
        except KeyError:
            pass
        else:
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip
        print self.__repr__()+"  process_request()"
        
    '''
    这个方法的调用时机在Django执行完request预处理函数并确定待执行的view之后，但在view函数实际执行之前。
    '''  
    def process_view(self, request, view, *args, **kwargs):
        print self.__repr__()+"  process_view()"
        pass
    
    '''
    这个方法的调用时机在Django执行view函数并生成response之后。 这里，这个处理过程会修改响应内容。
    一个明显的用例是压缩响应内容，像用gzip压缩请求返回的html代码。
    这个方法的参数相当直观: request 是request对象，而 response 则是从view中返回的response对象。
    process_response() 必须 返回 HttpResponse 对象. 这个response对象可以是传入函数的那一个原始对象(通常已被修改)，也可以是全新生成的。 
    '''
    def process_response(self, request, response):
        print self.__repr__()+"  process_response()"
        return response

    '''
    这个方法只有在request处理过程中出了问题并且view函数抛出了一个未捕获的异常时才会被调用。 
    这个钩子可以用来发送错误通知，将现场相关信息输出到日志文件, 或者甚至尝试从错误中自动恢复。
    这个函数的参数除了一贯的 request 对象之外，还包括view函数抛出的实际的异常对象 exception 。
    process_exception() 应当返回 None 或 HttpResponse 对象.
    如果返回 None , Django将用框架内置的异常处理机制继续处理相应request。
    如果返回 HttpResponse 对象, Django 将使用该response对象，并且短路框架内置的异常处理机制。（意思就是不进入系统的异常处理流程，如出错时显示的堆栈信息，都不会显示了）
    '''
    def process_exception(self, request, exception):
        print self.__repr__()+"  process_response()"      
        
    
    