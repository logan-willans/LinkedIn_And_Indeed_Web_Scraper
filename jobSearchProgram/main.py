from bs4 import BeautifulSoup
import requests
from functions import *
from classes import *
import re
# import geocoder
# can possibly use geocoder to modify search string to include user's geoID. But I haven't figured it out yet

# Arrays to hold all of the job postings
linkedIn_old_job_postings = []
linkedIn_new_job_postings = []
indeed_old_job_postings = []
indeed_new_job_postings = []

# While loop variables
successfullyParsedJobPostings = False
counter = 0

# String variables to hold get requests
linkedIn_jobs = ""
indeed_jobs = ""

# Collect keyword from user
keyword = sanitizeString(input("Enter the keyword you are looking for: "))

# While loop to try multiple times to pull the job postings from both websites because sometimes one website will not return results
while not successfullyParsedJobPostings and counter < 2:
    if counter > 0:
        print('We need to try again!\n\n\n\n\n')

    # Append keyword to LinkedIn & Indeed request strings. Currently hard-coded to search for jobs in LA only.
    linkedIn_html_text = requests.get('https://www.linkedin.com/jobs/search/?geoId=90000049&keywords=' + keyword).text
    indeed_html_text = requests.get('https://www.indeed.com/jobs?q=' + keyword + '&l&vjk=39dd01f9a5283b99').text

    # Get soup variables for the linkedIn and Indeed html requests
    linkedIn_soup = BeautifulSoup(linkedIn_html_text, 'lxml')
    indeed_soup = BeautifulSoup(indeed_html_text, 'lxml')

    # Populate string variables with HTML
    linkedIn_jobs = linkedIn_soup.find_all('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card')
    indeed_jobs = indeed_soup.find_all('a', class_='tapItem')

    # Check to see if job postings were successfully pulled from both websites. If not, loop executes two more times to try again.
    if not linkedIn_jobs or not indeed_jobs:
        successfullyParsedJobPostings = False
        counter += 1
    else:
        successfullyParsedJobPostings = True

for job in linkedIn_jobs:
    # Get job title
    job_title = (job.find('h3', class_='base-search-card__title').text).strip()

    # Get company name
    company_name = (job.find('a', class_='hidden-nested-link').text).strip()

    # Get time job posted if < 24 hours ago
    time_posted = (job.find('time', class_='job-search-card__listdate--new'))
    if time_posted != None:
        time_posted = time_posted.text.strip()

    # Get description
    description = (job.find('p', 'job-search-card__snippet').text).strip()

    # Get link to job posting
    info_link = (job.find('a', class_='base-card__full-link'))['href']

    # Instantiate a new job posting object
    job_posting = JobPosting(job_title, company_name, info_link, description, time_posted)

    # If recent job posting, add to new job posting array, else add to old job posting array
    if hasattr(job_posting, 'time_posted'):
        linkedIn_new_job_postings.append(job_posting)
    else:
        linkedIn_old_job_postings.append(job_posting)


# Print the LinkedIn results
printResults('LinkedIn', linkedIn_new_job_postings, linkedIn_old_job_postings)

for job in indeed_jobs:
    # Get job title. Used a regular expression to parse the job title.
    job_title = job.find('h2', class_='jobTitle').select('span[title]')
    pattern = '''"(.*?)"'''
    job_title = re.search(pattern, str(job_title)).group(1)

    # Get company name
    company_name = (job.find('span', class_='companyName').text).strip()

    # Get time job posted
    time_posted = (job.find('span', class_='date')).text
    numDays = ''.join(filter(lambda i: i.isdigit(), time_posted))
    if numDays and int(numDays) > 1 and int(numDays) <30:
        time_posted = "Posted " + numDays + " days ago"
    elif numDays and int(numDays) >= 30:
        time_posted = "Posted " + numDays + "+ days ago"
    elif numDays and int(numDays) == 1:
        time_posted = "Posted " + numDays + " day ago"
    else:
        time_posted = None

    # Get description
    description = (job.find('div', class_='job-snippet').text).strip()

    # Get link to job posting. Had a little bit of difficulty in parsing the job's JK identifier.
    # Did some tricky stuff with regular expressions.
    info_link = job.find('a', href=True)
    pattern = 'jk=(.*?)&'
    info_link = re.search(pattern, str(info_link))
    if info_link is not None:
        jk_value = str(info_link.group(1))
        info_link = generateIndeedJobPostingLinkPageWithJKValue(jk_value)
    else:
        info_link = str(re.search(pattern, str(job)).group(1))
        jk_value = info_link[1:17]
        info_link = generateIndeedJobPostingLinkPageWithJKValue(jk_value)

    # Instantiate a new job posting object
    job_posting = JobPosting(job_title, company_name, info_link, description, time_posted)

    # Append the job posting to one of the indeed job posting arrays
    if(hasattr(job_posting, 'time_posted')):
        indeed_new_job_postings.append(job_posting)
    else:
        indeed_old_job_postings.append(job_posting)

# Bubble sort algorithm to sort the indeed_new_job_postings array
isSorted = False
while(isSorted == False):
    isSorted = True
    for i in range(len(indeed_new_job_postings)-1):
        if (int(re.search(r'\d+', indeed_new_job_postings[i].time_posted).group()) > int(re.search(r'\d+', indeed_new_job_postings[i +1].time_posted).group())):
            isSorted = False
            temp = indeed_new_job_postings[i]
            indeed_new_job_postings[i] = indeed_new_job_postings[i+1]
            indeed_new_job_postings[i + 1] = temp

# Print the Indeed results
printResults('Indeed', indeed_new_job_postings, indeed_old_job_postings)