# UWOCourseWizard
A bot to automatically enroll in full courses at UWO as soon as spots open up

## Prerequisites
Before running the bot, ensure that you have the following prerequisites installed:

- Python (version 3.7 or higher)
- Selenium library `pip install selenium`
- Chrome WebDriver (compatible with your Chrome browser version)

## Configuration
To set up the bot, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies mentioned in the "Prerequisites" section.
3. Download the Chrome WebDriver appropriate for your Chrome browser version and place it in the project directory.
4. Open the file and modify the following variables according to your needs:

`PATH = "/Users/name/chromedriver # Path to your Chrome WebDriver`

`username = "your_username"  # Your UWO student center username`

`password = "your_password"  # Your UWO student center password`

`fullCourse = "MATH 1600A"  # Full name of the course you want to enroll in`

## Authentication Using Duo Push
During the initial startup of the bot, you will need to authenticate using Duo Push. Once you execute the bot, it will open the UWO student center website and prompt you to authenticate through Duo Push. Please follow the prompts and authenticate using your preferred method (e.g., mobile app notification, SMS, etc.). This authentication is required to access the student center and proceed with the course enrollment process.

## Usage
To start the enrollment bot, execute the following command in your terminal or command prompt:

`python CourseFinder.py`

The bot will open a Chrome browser window and begin monitoring the specified course registration page. Once a spot becomes available, it will automatically fill in your login credentials, select the course, and complete the enrollment process. You will receive a notification indicating whether the enrollment was successful or not.

## Important Notes
Keep the bot running as long as you want to monitor the course availability. You can leave it running in the background or consider using a cloud service for uninterrupted monitoring.
