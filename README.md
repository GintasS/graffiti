# Project Name: **GraffLib**

## Overview
**GraffLib** is a comprehensive application designed to catalog and explore graffiti art across urban environments. It serves as a temporal gallery and a tool for searching similar graffiti. With a combination of graffiti and library functionalities, GraffLib aims to capture the beauty and dynamics of graffiti in cities.

## Features
- **Graffiti Cataloging:** Easily create, organize, and search graffiti artworks.
- **Temporal Gallery:** Visualize the changes in graffiti spots over time.
- **Users system** The project contains a basic user system: registering and changing of the password.
- **Rest API:** An extensive API designed to easily integrate with different platforms and apps (Web, Apps, Desktop).
- **Front-end support:** Available on the Android OS.
- **3rd party APIs** The project uses 3rd party APIs (Nominatim, IsItWater, VirusTotal).
- **Database**: a lot of user data, markers, metadata are saved in the PostgreSQL DB.
- **Hosting**: the application is currently hosted on the Google Cloud. Previously, I have tried running it on the AWS.

## Demo
Back-end: [live demo](https://grafflibapi-7qcob53xgq-ew.a.run.app/)<br>
Front-end: [Android APK](https://play.google.com/store/apps/details?id=com.company.grafflib)<br>
Presentation: [PDF](https://gsvedas.me/Grafflib_presentation.pdf)

## Prerequisites
- Python 3.9
- requirements.txt
- Android (for running front-end)
- Web brwoser/Postman for calling API endpoints;

## Media
<img src="docs/images/1.jpg" alt="alt text" width="200"/>
<img src="docs/images/2.jpg" alt="alt text" width="200"/>
<img src="docs/images/3.jpg" alt="alt text" width="200"/>
<img src="docs/images/4.jpg" alt="alt text" width="200"/>

## Installation
To get started with GraffLib, follow these simple steps:

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/gintass/grafflib.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd \ROOT PROJECT PATH\src\GraffLibAPI\GraffLibAPI
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Edit these configuration files:**<br>
    appsettings.ini<br>
    dbsettings.ini<br>
    environment.ini<br>

    Search for every **ENTER_YOUR** prefix in these three .ini files, to replace strings with your data.
  
6. **Start the development server:**
    ```bash
   python runserver.py
    ```
## Usage
After running the **runserver.py** script, the application can be reached at `http://localhost:8080`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or suggestions, feel free to reach out to us at [svedgintas@gmail.com](mailto:svedgintas@gmail.com).
