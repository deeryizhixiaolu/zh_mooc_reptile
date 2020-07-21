"""
豆包ykt16054788784277548提供资源
https://blog.csdn.net/weixin_43978546/article/details/105117901
股票替代网站  http不是https慕课自动添加的需要注意
https://quote.eastmoney.com/stock_list.html
股票查询替代网站
https://xueqiu.com/S/SZ300783
项目Github下载地址
https://github.com/xuehang00126/MOOCdemo
项目zip压缩文件下载地址
"""

#简单优化，如果正则表达式匹配规则比较了解，可以使用正则表达式规则匹配文本，不用BeautifulSoup和scrapy.css来匹配也可以
"""
class StockSpider(scrapy.Spider):
    name = 'stock'
    #allowed_domains = ['lanrentuku.com']
    start_urls=["http://quote.eastmoney.com/stock_list.html"]
    def parse(self, response):
        for i in re.findall("http://quote.eastmoney.com/([a-z][a-z]\d+).html",response.text):
            try:
                yield scrapy.Request("https://xueqiu.com/S/{}".format(i), callback = self.parse_stock)
            except:
                continue
    def parse_stock(self,response):
        try:
            print(response.css("title"))
        except:
            print("error")
"""
