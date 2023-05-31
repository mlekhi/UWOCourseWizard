# Developed by: Maya Lekhi
# Date: Jan 20, 2023
# About: A bot to automatically enroll you in full courses at UWO as soon as spots open up

# Note: you must already be logged in on student center on your browser!!

username = "username" # input your student center username here
password = "password" # input your student center password here
fullCourse = "course name" # edit your course name here; try to input the full, correct name
PATH = "/Users/name/chromedriver" # Path to your Chrome WebDriver

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(PATH)
driver.get("https://student.uwo.ca/psp/heprdweb/?cmd=login")
sleep(2)

# inputting login information
userId = driver.find_element("id","userid")
userId.send_keys(username)
pwd = driver.find_element("id","pwd")
pwd.send_keys(password)
submit = driver.find_element("name","Submit")
submit.click()

# checking if you have authenticated
while driver.current_url != "https://student.uwo.ca/psc/heprdweb/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?":
    print("Please authenticate using Duo Push!")
    sleep(8)
    
# navigating to the courses page
sleep(2)
academics = driver.find_element("id","win0groupletPTNUI_LAND_REC_GROUPLET$2")
academics.click()
sleep(2)
courseReg = driver.find_element("id","win0divPTNUI_LAND_REC_GROUPLET$1")
courseReg.click()
sleep(3)
add = driver.find_element("id","win6div$ICField$11$$4")
add.click()
sleep(2)

# choosing the semester that you are looking to enroll for
semester = driver.find_element("id","win0divDERIVED_SSR_FL_SSR_GRPBOX_TERM$16$$0") # if you are looking for the current semester,
# set the digit after the "$$" to 0. If you are looking for future semesters, set the digit to
# however many semesters away it is (e.g. next semester = 1, semester after = 2, etc.)
semester.click()
sleep(2)

# search for course
courseSearch = driver.find_element("id","PTS_KEYWORDS3")
courseSearch.send_keys(fullCourse)
submit = driver.find_element("id","PTS_SRCH_BTN")
submit.click()
sleep(2)

# select course
course = driver.find_element("id","PTS_RSLTS_LIST$0_row_0")
course.click()
sleep(5)

# searching for if there are any open courses
courses = driver.find_elements("class name","ps_grid-cell.psc_valign-top")
print(courses)
for course in courses:
    if "Open" in course.text:
        print("Found 'Open' Course")
        found = driver.find_element("id","SSR_CLS_DTLS_VW$0_row_0")
        found.click()
        availability = True
        break
else:
    # reloading the page
    sleep(10)
    driver.refresh()
    availability = False

# loop to check if courses open up
while availability == False:

    # renavigating to the course
    recentCourse = driver.find_element("id","RECENTLY_VIEWED$0_row_0")
    recentCourse.click()

    # searching for if there are any open courses
    courses = driver.find_elements("class name","ps_grid-cell.psc_valign-top")
    print(courses)
    for course in courses:
        if "Open" in course.text:
            print("Found 'Open' Course")
            found = driver.find_element("id","SSR_CLS_DTLS_VW$0_row_0")
            found.click()
            availability = True
    else:
        # reloading the page
        sleep(60)
        driver.refresh()

# finalizing the course selection
openCourse = driver.find_element("id","PTGP_GPLT_WRK_PTGP_NEXT_PB")
openCourse.click()
sleep(3)
openCourse2 = driver.find_element("id","SSR_ENRL_FL_WRK_SUBMIT_PB")
openCourse2.click()
sleep(3)
print("You have been enrolled in the course. Happy learning!")
    
driver.close()
