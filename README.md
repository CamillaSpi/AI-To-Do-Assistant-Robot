# Project RoboTo-Do Assistant

## Overview

RoboTo-Do Assistant is a robotic platform developed to assist users in managing their personal to-do lists using natural language interactions. The project utilizes ROS (Robot Operating System) and RASA for building a dialogue system that allows seamless communication with the robot.

## Features

- **Spoken Natural Language Interaction:**
  - The robot communicates with users using spoken natural language.
  - A microphone on the robot captures the audio stream through PyAudio.

- **Personalized To-Do Lists:**
  - The robot manages a different to-do list for each person it interacts with.
  - New users are identified through face or voice recognition.
  - If a new person is met, the robot asks for their name and creates a new to-do list.

- **To-Do List Requirements:**
  - Develop a ROS dialogue system for inserting, removing, and managing activities in the to-do lists.
  - Each to-do list item is identified by a tag, a deadline, and a category (e.g., CR course, sport, personal, etc.).
  - The dialogue system (with RASA) allows users to:
    - View activities in the to-do list.
    - Insert a new activity into the to-do list.
    - Remove an activity from the to-do list.
    - Activate a reminder when the deadline is approaching.

- **Optional Features:**
  - Manage multiple users.
  - Manage multiple categories of to-do lists.
  - Update an activity in the to-do list.

## Environmental Constraints

- The distance between the user and the robot must be less than 2 meters.
- No ambient noises during the conversation.
- Only one person at a time can interact with the robot.
- Conversations can occur in both English and Italian.

## More Information
for more info click [here](https://github.com/CamillaSpi/DefinitivoCog/blob/main/ReportCRFinaleCognitive.pdf)
Feel free to customize this template according to your project's specific needs.
