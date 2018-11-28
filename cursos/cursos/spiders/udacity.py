import scrapy

class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div")
        for div in divs:
            link = div.xpath(".//h3/a")
            href = link.xpath("./@href").extract_first()
            
            yield scrapy.Request(
                    url= 'https://br.udacity.com%s' %href,
                    callback= self.parse_detail
                    )

    def parse_detail(self, response):
        title = response.xpath("//title/text()").extract_first()
        headline = response.xpath("//html/body/ir-root/ir-content/ir-ndop-b/section[2]/ir-nd-hero-video/div/div[2]/div/p[1]/text()").extract_first()
        headline_free_course = response.xpath("/html/body/ir-root/ir-content/ir-course-overview/section[3]/div/ir-product-summary/div/text()").extract_first()
        
        yield {
                'title': title,
                'headline': headline,
                'headline_free_course': headline_free_course}