<details open="open">
<summary>Table of Contents</summary>

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Project scope](#project-scope)
- [Overall description](#overall-description)
  - [Product perspective](#product-perspective)
- [MVP Architecture](#mvp-architecture)
	- [Scenarios](#scenarios)
- [Requirements](#requirements)
	- [Functional Requirements](#functional-requirements)
	- [Non-Functional Requirements](#non-functional-requirements)	
		- [Performance and scalability](#performance-and-scalability)	
		- [Portability and compatibility](#portability-and-compatibility)	
		- [Reliability, Availability, Maintainability](#reliability-availability-maintainability)	
		- [Security](#security)
		- [Localization](#localization)
		- [Usability](#usability)
		- [Other](#other)	
- [Technologies](#technologies)
- [Additional Information](#additional information)


</details>

---

## Introduction

This is the specification of requirements for GraffLib project. This is a software for sharing graffiti and it's information with people.

### Purpose

This is the document describing requirements for our GraffLib project. The purpose of this software is to allow sharing, analyzing, comparing of various graffities around a specific
geographical location.

### Project scope

Our goal is to connect people who are interested in graffiti and enable them to share, analyze and compare pictures of graffiti online. 
Our application would save the meta-data of the picture(location, date and others). 
The meta-data would allow us to track the locations of the graffities, how do they change over time and would ultimately allow us to compare them. 
We are thinking of hosting our back-end system on Vilnius University's infrastructure.

## Overall description

## Product perspective

We will store the following information:

- User
	- Username
	- Password
	- Email Address
	- First Name
	- Last Name
	- Privileges status (admin, normal user)
- Image
	- source (image's bytes)
- Image meta-data
	- Latitude (GIS)
	- Longitude (GIS)
	- Photography Time (when was the picture taken?)
	- Upload Time (when was the picture uploaded?)
- Image Description
	- Image's text description (e.g it's a car, elephant).
	- Direction of the photo (front-facing, on the angle).
- City
	- Name
- Marker
	- Latitude (GIS)
	- Longitude (GIS)
	- Images
	- Statistics
	- Various other information.

***- The following information is subject to change.***<br>
***- In the list above, we are not taking into consideration various relationships between the objects.***<br>
***- City object will hold all the cities where images are available.***

## MVP Architecture

[<img src="images/project-architecture.jpg" width="1000" height="475"/>](image.png)

### Scenarios

Scenario 1:
- We would have ***two parts: front-end and back-end.***<br>
Back-end would save, analyze and compare data sent to it via an API.<br>
Front-end would be ***a Android app***, where user could add images, view them, compare them, basically, a GUI.

Scenario 2:
- We would have ***two parts: front-end and back-end.***<br>
Back-end would save, analyze and compare data sent to it via an API.<br>
Front-end would be ***a website/desktop application***, where user could add images, view them, compare them, basically, a GUI.

Scenario 3:
- We would have ***only one part: back-end.*** <br>
Back-end would save, analyze and compare data sent to it via an API.<br>

Other scenarios are also possible.

## Requirements


### Functional requirements

- As a user, I want to add new graffities to our system or have existing graffities.
- As a user, I want to compare graffities.
- As a user, I want to see information about graffities.
- As a user, I want to compare graffities over time.
- As a user, I want to see graffiti information for one specific geographical location.
- As an administrator, I want to be able to manage users and their information.

### Non-Functional requirements

#### Performance and scalability

- Response time for our back-end system (API and other parts) should be no less than 2 seconds.
- Our back-end system should be able to handle 10 users.

#### Portability and compatibility

- N/A

#### Reliability, Availability, Maintainability

- N/A

#### Security

- User information in database should be kept in a secure manner.
- User passwords should be hashed using a modern and secure hashing algorithm.
- Our back-end system should validate user information as not to allow malicious code.
- Normal users should not have administrative privileges in our system.

#### Localization

- No localization is provided for this project, English will be used as a main language.

#### Usability

- If a GUI exists, user should be able to upload a photo in a less than 15 clicks.

#### Other

- System programming shall not use deprecated code.

## Technologies

- Software:
	- Front-end:
		- TBD, if any.
	- Back-end:
		- Python
		- Flask
		- Packages:
			- Click
			- itsdangerous
			- Jinja2
			- MarkupSafe
			- pip
			- setuptools
			- Werkzeug
	- Databases:
		- Any RDBMS (TBD)
	- AI/ML:
		- TBD, if any.
- Hardware:
	- OS with network adapter enabled.
	- OS that supports Python and it's packages.

## Additional Information

- GraffLib Project Vision can be found here: [link](https://miro.com/app/board/o9J_lyyCsbc=/).
- GraffLib MVP can be found here: [link](https://miro.com/app/board/o9J_lws9LDk=/).
- GraffLib Project Architecture can be found here: [link](https://miro.com/app/board/o9J_lvYW3C4=/).