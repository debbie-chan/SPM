# :printer: SPM: LMS for All-In-One 
All-In-One is a leading Printing Solution Equipment Servicing company. To address the issue of training and proficiency of the engineers, the management decided to build a software solution for a Learning System for the field engineers.

## Terminology
- **Courses** contain **Class** runs, which are composed of **Lessons**.
- There are 3 main roles in this system: **Admins**, **Trainers** and **Learners**.
  - The Human Resources (HR) team make up the **Admin** of this system. 
  - Engineers can be a **Trainer** or **Learner**, or both.

## Project Management Tools
- [Notion](https://www.notion.so/Women-in-SPM-d509d76b290144bfbeb869ff806ee5eb), our home page for the project
- [Jira](https://g7t8.atlassian.net/jira/software/projects/G7T8/boards/1), for planning and conducting sprints
- [GitHub](https://github.com/debbie-chan/spm), for version control

## Application Technologies
- **Front-End**: Vue.js, Vuetify
- **Back-End**: Python Flask
- **Database**: MongoDB Atlas
- **Testing**: Python unittest, mongomock
- **CI**: Jenkins
- **Design**: [PlantUML](https://plantuml.com/)

## Directory Layout
- `api` contains the Flask application
- `api/tests` contains backend tests
- `app` contains the Vue app 
- `design` contains PlantUML documents for all UML diagrams

```
.
├───api
│   ├───src
│   │   ├───controllers
│   ├───tests
├───app
│   ├───public
│   └───src
│       ├───assets
│       ├───components
│       ├───layouts
│       ├───plugins
│       ├───router
│       ├───store
│       ├───styles
│       ├───utils
│       └───views
└───design
```

## Installation and Running
1. Install requirements 
   ```
   pip install -r requirements.txt
   ```
2. Run Flask App 
   ```
   cd api
   python main.py
   ```
3. Run Vue App
   ```
   cd ../app
   yarn install 
   yarn serve
   ```

## Testing
To run the tests, run the following: 
```
cd api 
python -m unittest discover
```


