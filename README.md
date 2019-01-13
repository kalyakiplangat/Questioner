# Questioner
This application enables meetup organizer to prioritize questions for meetup

Badges
----------------
[![Build Status](https://travis-ci.com/kalyakiplangat/Questioner.svg?branch=develop)](https://travis-ci.com/kalyakiplangat/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/kalyakiplangat/Questioner/badge.svg)](https://coveralls.io/github/kalyakiplangat/Questioner)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/b7e6dd16f0c9616587df/maintainability)](https://codeclimate.com/github/gitlabhq/gitlab-ci/maintainability)

Summary
--------
Questioner allows the meetup organizer to prioritize questions to be answered. Users vote on asked questions, and they bubble to the top or the bottom of the log.

Find the UI [here](https://kalyakiplangat.github.io/Questioner/UI)

This project is managed using a pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235263)

Pre-requisites
----------------------
1. Python3
2. Flask
3. Flask restplus
4. Postman

Getting started
--------------------
1. Clone this repository
```
    https://github.com/kalyakiplangat/Questioner.git
```

2. Navigate to the cloned repository
```
    cd Questioner
```

Installation
---------------------------------
1. Create a virtual env
```
    python3 -m venv venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install git-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```
Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following API endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup-id&gt; | Fetch a specific meetup record
GET /meetups/upcoming/ | Fetch all upcoming meetup records
POST /questions | Create a question for a specific meetup
PATCH /questions/&lt;question-id&gt;/upvote | Upvote (increase votes by 1) a specific question
PATCH /questions/&lt;question-id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup-id&gt;/rsvps | Respond to meetup RSV

Authors
-----------------------------
**Cheruiyot Enock** - _Initial work_-[kalyakiplangat](https://github.com/kalyakiplangat)

Acknowledgements
--------------------------------
1. Andela Workshops
2. Team members
