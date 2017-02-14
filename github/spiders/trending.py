# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem


class TrendingSpider(scrapy.Spider):
    name = "trending"
    allowed_domains = ["github.com"]
    start_urls = ['https://github.com/trending']

    def parse(self, response):
        # This selector will find all the `li` elements inside an `ol` with the
        # CSS class `repo-list` and store them in the repos variable.
        repos = response.selector.css('ol.repo-list li')

        # If you're wondering what the above code would look like if you used
        # XPath instead of CSS, here it is:
        # repos = response.selector.xpath('//ol[contains(@class, "repo-list")]/li')
        # Try commenting the CSS version and trying the above version, you
        # should get the same results.

        for repo in repos:
            # Here we are using `extract_first` which extracts the text and
            # returns the first result. This is needed quite often and some
            # selectors are intended to return only a single item.
            # You can also use `.extract()[0]` which will return the first item
            # in the returned array, however that will cause and error if the
            # result is empty and `extract_first` will just return an empty
            # None response.
            name = repo.xpath('.//h3/a/@href').extract_first()

            # Here we are looking for a span that has a particular attribute
            # set to a particular value. Simply using span[itemprop] would
            # return all spans that have the `itemprop` attribute, no matter
            # what it's value.
            lang = repo.css(
                'span[itemprop="programmingLanguage"]::text'
            ).extract()

            # Like above we are now searching for an `a` tag using the
            # `aria-label` attribute set on it.
            stars = repo.css('a[aria-label="Stargazers"]::text').extract()

            # To contrast with the CSS version above, here is the XPath way of
            # searching for a tag that has a particular attribute.
            forks = repo.xpath('.//a[@aria-label="Forks"]/text()').extract()

            # Finally we put all the data we have collected into a `GithubItem`
            # and yield it to Scrapy so it can store it the way the user wants.
            yield GithubItem(
                repo=name,
                language=lang,
                stars=stars,
                forks=forks,
            )
