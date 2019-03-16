# -*- coding: utf-8 -*-
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote

driver = webdriver.Chrome()


def get_list_page(url):
    driver.get(url)
    while True:
        html = driver.page_source
        html = etree.HTML(html)
        job_list = html.xpath('//div[@class="job-list"]/ul/li')
        for job in job_list:
            detail_url = job.xpath('.//h3/a/@href')[0]
            detail_url = 'https://www.zhipin.com' + detail_url
            get_detail(detail_url)
        next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.next')))
        if not next_btn:
            break
        next_btn.click()


def get_detail(detail_url):
    driver.execute_script('window.open("{}")'.format(detail_url))
    driver.switch_to.window(driver.window_handles[1])
    detail_html = driver.page_source
    html = etree.HTML(detail_html)
    job_name = html.xpath('//div[@class="info-primary"]/div[@class="name"]/h1/text()')[0]
    job_salary = html.xpath('//div[@class="info-primary"]/div[@class="name"]/span/text()')[0].strip()
    job_location = html.xpath('//div[@class="info-primary"]/p//text()')[0]
    work_experience = html.xpath('//div[@class="info-primary"]/p//text()')[1]
    education_background = html.xpath('//div[@class="info-primary"]/p//text()')[2]
    job_detail = ''.join(html.xpath('//div[@class="detail-content"]/div[1]//text()')).strip()
    job_company = html.xpath('//div[@class="company-info"]/a/@title')[0].strip()
    # print(work_experience,education_background)
    # print(job_company)
    data = {
        'job_name': job_name,
        'job_salary': job_salary,
        'job_location': job_location,
        'work_experience': work_experience,
        'education_background': education_background,
        'job_detail': job_detail,
        'job_company': job_company
    }
    print(data)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def run(url):
    get_list_page(url)


if __name__ == '__main__':
    kw = 'python'
    url = 'https://www.zhipin.com/job_detail/?query={}&city=100010000&industry=&position='.format(quote(kw))
    run(url)
