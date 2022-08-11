import requests
from selenium import webdriver


def get_agify_age(agify_link):
    agify_result = requests.get(agify_link)
    print(agify_result.json()["age"])
    return


def check_title(actual, expected):
    if expected == actual:
        print("title as expected")
    else:
        print("not matching title")
    return


result = []
names = ["saby", "jack", "inbar"]
repos = requests.get("https://api.github.com/users/avielb/repos")
universities = requests.get("http://universities.hipolabs.com/search?country=Israel")


# API Testing
if len(repos.json()) >= 5:
    print("Yes, we have more then 5")
else:
    print("No, we have less then 5")

for name in names:
    print(name, end='-')
    get_agify_age("https://api.agify.io/?name=" + name)

if len(universities.json()) >= 5:
    print("Yes, we have more then 5 universities")
else:
    print("No, we have less then 5 universities")

# UI Testing
ycombinator_driver = webdriver.Chrome(executable_path='/Users/sabybehar/Downloads/chromedriver')
docker_driver = webdriver.Chrome(executable_path="/Users/sabybehar/Downloads/chromedriver")
ycombinator_driver.get("https://www.ycombinator.com/")
docker_driver.get("https://hub.docker.com/")
expected_ycombinator_title = "Y Combinator"
expected_docker_title = 'Docker Hub Container Image Library | App Containerization'
check_title(ycombinator_driver.title, expected_ycombinator_title)
check_title(docker_driver.title, expected_docker_title)


