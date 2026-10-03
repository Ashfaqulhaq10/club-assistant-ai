# CLUB ASSIST AI

VOYAGER.BOT is a campus club/event registration demo designed as a conversational bot experience. It presents a web-based interactive chat flow where a student can enter personal details, choose an event, and receive a generated event ticket.

This project includes:
- a browser-based interactive chatbot in `aditi.html`
- a Python terminal version in `Aditi Lohar.CHATBOT.py`
- related branding and media assets for a Kalasalingam-themed presentation

## Project Overview

The project simulates an AI-like club member named **Aditi Lohar** who greets students, asks for their details, and helps them register for a campus event. The conversation flow includes:

- Name collection
- Department selection
- Year of study
- Section information
- Event choice
- Mobile number
- Register number
- Ticket generation with an email and token

## Features

- Typed-message chat animation
- Full-screen background video layout
- Club branding and university logo display
- Event registration flow
- Ticket preview on screen
- PDF export using jsPDF
- Console-based Python version for the same experience

## Project Structure

```text
VOYAGER.BOT/
├── aditi.html                  # Main web UI and chatbot logic
├── Aditi Lohar.CHATBOT.py      # Python terminal chatbot version
├── README.md                   # Project documentation
├── Kalasalingam-Academy-of-Research.jpg
├── kalasalingam_logo-1024x179.png
├── Digital Marketing Website Background(720P_HD)_2.mp4
├── gif for website.mp4
└── ...
```

## How to Run

### Web version
1. Open the project folder.
2. Open `aditi.html` in a browser.
3. Click the button to start the chat.

### Python version
1. Open a terminal in the project folder.
2. Run:

```bash
python "Aditi Lohar.CHATBOT.py"
```

## Tech Stack

- HTML5
- CSS3
- JavaScript
- Python 3
- jsPDF library (CDN in browser version)

## Ticket Logic

The project generates:
- student name
- department
- year
- section
- selected event
- KLU email in the form: `registernumber@klu.ac.in`
- a random token for the ticket

Example:

```text
Name: John
Department: CSE
Year: Second Year
Section: A
Event: XYZ
Email: 2212345@klu.ac.in
Token: ABCD-7F4K9Q2L
```

## Notes

This is a prototype/demo project, not a real production system. It does not include:
- a real backend
- authenticated login
- database storage
- secure user data handling
- production-grade validation

## Possible Improvements

- Add a backend with database storage
- Create a real login and registration system
- Validate student input on the client and server
- Save tickets to a database or file system
- Add dynamic event management
- Replace the static event names with real event data
- Add email sending or QR-code ticket generation

## License

This project is currently a local demo and does not appear to include an explicit license file. If this project is being reused publicly, it is recommended to add a license before sharing it outside the local environment.

## Summary

VOYAGER.BOT is a student event registration chatbot demo with a modern UI and a terminal version. It is designed as a flashy campus club interaction prototype that collects student information and produces a fake event ticket for demonstration purposes.
