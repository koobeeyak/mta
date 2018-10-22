# 3p
from bs4 import BeautifulSoup
from selenium.webdriver import PhantomJS

# project
from common import MTA_URL, LINES, StatusTypes
from process.line import Line


class StatusFetcher(object):
    lines = []

    @staticmethod
    def get_line(soup, name):
        status = StatusTypes.NOT_DELAYED
        if soup.find(id=name).text == "Delays":
            status = StatusTypes.DELAYED
        return Line(name, status)

    def scrape_statuses(self):
        headless_browser = PhantomJS()
        headless_browser.get(MTA_URL)
        soup = BeautifulSoup(headless_browser.page_source, "html.parser")
        for line_name in LINES:
            line = self.get_line(soup, line_name)
            self.lines.append(line)

    def run(self):
        self.scrape_statuses()
        return self.lines
