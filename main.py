from bs4 import BeautifulSoup
import requests
import time

print('Put some skill with you are not Familiar with')
unfamiliar_skill = input('>')
print(f"Filtering Out {unfamiliar_skill}")


def find_jobs():
    url = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(url, 'lxml')
    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print('')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} Minutes...')
        time.sleep(time_wait * 60)
