#科学松鼠会-原创标题链接	{"offset":"1", "limit":"1", "step":"1", }	1	2015-01-01 00:31:05
#start

page_info_list = []

page_info_list.append({
        "urls":['http://songshuhui.net/archives/tag/%E5%8E%9F%E5%88%9B',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['<a class="nextpostslink" href="([^"]*)"[^>]*>[^<]*</a>',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<html>',
	       "end_str":'</html>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"科学松鼠会-原创列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<h3 class="storytitle"><a class="black" href="([^"]*)"[^>]*>([^<]*)</a></h3>',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"科学松鼠会-原创标题链接"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end


#豆瓣：音乐标签：摇滚	{"offset":"1", "limit":"1", "step":"1", }	1	2015-01-02 23:59:31
#start

page_info_list = []

page_info_list.append({
        "urls":['http://music.douban.com/tag/%E6%91%87%E6%BB%9A',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
			"regulars":['<span class="next"><a href="([^"]*)">',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
	       "start_str":'<body>',
	       "end_str":'</body>',
	       "result":"comblock"},

       "encoding":"UTF-8",
       "loop_info":{
	       "is_need_loop":"1",
	       "loop_urls":["${nextPageUrl1}",],
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
       "job_description":"豆瓣：音乐标签：摇滚"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<td valign="top">\s*<div class="pl2">\s*<a\s*href="([^"]*)"\s*title="([^"]*)"\s*>',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
	"encoding":"UTF-8",
   "job_description":"豆瓣：音乐标签：摇滚",
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end


#科学松鼠会-原创标题链接	{"offset":"1", "limit":"1", "step":"1"}	1	2014-11-10 11:25:48
#start

page_info_list = []

page_info_list.append({
        "urls":['http://songshuhui.net/archives/tag/%E5%8E%9F%E5%88%9B',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['<a class="nextpostslink" href="([^"]*)"[^>]*>[^<]*</a>',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<html>',
	       "end_str":'</html>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"科学松鼠会-原创列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<h3 class="storytitle"><a class="black" href="([^"]*)"[^>]*>([^<]*)</a></h3>',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"科学松鼠会-原创标题链接"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<html>',
	       "end_str":'</html>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<html>',
	       "end_str":'</html>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'sogou.weixin.gzhcb\(\{',
	       "end_str":'/DOCUMENT\>"\]\}\)',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///<block>weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;</block>',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<block>',
	       "end_str":'</block>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []



page_info_list.append({
    "urls":['weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///<block>weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;</block>',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'<block>',
	       "end_str":'</block>',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9&t=1421026952995;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10&t=1421026952995;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"}	1	2015-01-12 10:40:24
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<[^/]*/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表2		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)','<url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表2	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 13:37:22
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)','<url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表2	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 13:37:22
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表3		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=${offset}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表3	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 14:08:15
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=${offset}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表3	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 14:08:15
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=${offset}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表4		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['"totalPages":(\d*),"page":(\d*)', '<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${title2})+1}",], 
	       "offset":"${title2}", 
	       "limit":"${title1}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title3","title4",]})

#end

#近铁城市广场-文章列表4	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 16:12:59
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['"totalPages":(\d*),"page":(\d*)', '<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${title2})+1}",], 
	       "offset":"${title2}", 
	       "limit":"${title1}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title3","title4",]})

#end

#近铁城市广场-文章列表4	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 16:12:59
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"title",
	        "regulars":['"totalPages":(\d*),"page":(\d*)', '<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${title2})+1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({"is_end":"1","output_keys":["title3","title4",]})

#end

#科学松鼠会-原创标题链接5		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['"totalPages":(\d*),"page":(\d*)',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${nextPageUrl2})+1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"科学松鼠会-原创列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"科学松鼠会-原创标题链接"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表 5		1	2015-01-12 16:31:26
#start

page_info_list = []

page_info_list.append({
        "urls":['http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['"totalPages":(\d*),"page":(\d*)',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${nextPageUrl2})+1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"科学松鼠会-原创列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"科学松鼠会-原创标题链接"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表 5	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 16:31:26
#start

page_info_list = []

page_info_list.append({
        "urls":['http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['"totalPages":(\d*),"page":(\d*)',],
	        "is_unique":"1",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"1", 
	       "loop_urls":["http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=$eval{int(${nextPageUrl2})+1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"科学松鼠会-原创列表"
    })

page_info_list.append({
    "urls":['inline:///${comblock}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['\<title1\>\<\!\[CDATA\[([^]]*)\]\]\>\<\\/title1>\<imglink\>\<\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"科学松鼠会-原创标题链接"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 13:37:22
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表--bak		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['inline:///http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=1;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=2;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=3;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=4;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=5;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=6;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=7;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=8;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=9;http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt-Atb62Noyz4nKX1nvrmFHQ&page=10;',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#近铁城市广场-文章列表	{"offset":"1", "limit":"1", "step":"1"} 	1	2015-01-12 13:37:22
#start

page_info_list = []

page_info_list.append({
        "urls":['{{list_page}}',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

#微信文章列表		1	None
#start
page_info_list = []

page_info_list.append({
        "urls":['{{list_page}}',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"微信文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"微信文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})
#end

#微信文章列表	{"offset":"1", "limit":"1", "step":"1", }	1	2015-01-12 22:52:08
#start
page_info_list = []

page_info_list.append({
        "urls":['{{list_page}}',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"微信文章列表"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"微信文章列表"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})
#end

#近铁城市广场-文章内容		1	None
#start

page_info_list = []

page_info_list.append({
        "urls":['{{list_page}}',],
        "regular_matchs":[{        
	        "result":"nextPageUrl",
	        "regulars":['([^;]*);',],
	        "is_unique":"0",
	        }, ],
       "block_match":{
       	   "start_str":'',
	       "end_str":'',
	       "result":"comblock"},
       "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":["${nextPageUrl1}",], 
	       "offset":"{{offset}}", 
	       "limit":"{{limit}}", 
	       "step":"{{step}}", },
	   "encoding":"UTF-8",
       "job_description":"近铁城市广场-文章内容"
    })

page_info_list.append({
    "urls":['${nextPageUrl1}',],
    "regular_matchs":[{        
        "result":"title",
        "regulars":['<title><\!\[CDATA\[([^]]*)\]\]><[^/]*/title><url><\!\[CDATA\[([^]]*)',],
        "is_unique":"0",
        },],
   "loop_info":{
       	   "is_need_loop":"0", 
	       "loop_urls":[], },
   "encoding":"UTF-8",
   "job_description":"近铁城市广场-文章内容"
})

page_info_list.append({"is_end":"1","output_keys":["title1","title2",]})

#end

