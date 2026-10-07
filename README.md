# Friday a Voice Assistant
Friday AI is a Python-based personal voice assistant built with Streamlit that uses speech recognition and text-to-speech to interact with users, answer queries, open websites, fetch Wikipedia information, tell the current time, and provide a simple interactive voice-controlled interface.
# Friday AI — Personal Voice Assistant 🎙️

A Python-based personal voice assistant designed to interact with users through voice commands. Friday AI features a modern, interactive web interface, speech recognition, text-to-speech responses, Wikipedia summaries, and browser automation.

Features
- **Voice Interaction:** Capture and process voice commands through a microphone.
- **Speech Recognition:** Convert spoken commands into text using Google Speech Recognition.
- **Text-to-Speech:** Respond verbally using the `pyttsx3` library.
- **Wikipedia Search:** Retrieve short summaries of topics using Wikipedia.
- **Browser Automation:** Open Google and YouTube through voice commands.
- **Time Assistance:** Tell the current time through voice interaction.
- **Interactive Dashboard:** Use a dark-themed Streamlit interface with an animated AI orb.
- **Assistant Status:** Visual states for Sleeping, Activated, Listening, Processing, and Speaking.
- **Thread-Based Processing:** Use background threading and a message queue to manage microphone input and interface updates.

Technologies Used
| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| SpeechRecognition | Speech-to-text conversion |
| PyAudio | Microphone access through the audio backend |
| pyttsx3 | Text-to-speech conversion |
| Wikipedia | Topic summaries |
| Webbrowser | Opening websites |
| Threading & Queue | Background listening and message handling |
| HTML & CSS | Interface styling and animations |

Prerequisites
Before running Friday AI, make sure you have:
- Python installed on your computer.
- A working microphone.
- An internet connection for Google Speech Recognition and Wikipedia requests.
- A supported system speech engine. The current implementation uses the Windows SAPI5 speech engine.

Installation and Setup
1. Clone the repository
bash
git clone <YOUR_REPOSITORY_URL>
Navigate into the project directory:
bash
cd Friday-AI

2. Create a virtual environment (recommended)
bash
python -m venv venv

Activate it on Windows:
bash
venv\Scripts\activate

3. Install dependencies
bash
pip install streamlit SpeechRecognition pyttsx3 wikipedia pyaudio
Note: PyAudio installation may require additional system support depending on your Python version and operating system.

4. Run the application
Save the Python source code as `app.py`, then execute:
bash
streamlit run app.py

Open the local URL displayed in your terminal to access the Friday AI interface.

Supported Voice Commands
| Voice command | Action |
|---|---|
| "Open YouTube" | Opens YouTube in the browser |
| "Open Google" | Opens Google in the browser |
| "Wikipedia Python" | Retrieves a short Wikipedia summary about Python |
| "What is the time?" | Announces the current time |
| "Exit" or "Sleep" | Requests the assistant to enter its sleeping state |

The assistant also supports activation, listening, and sleep controls through the web interface.

How It Works
1. Activation: Click the Activate Friday button to initialize the assistant's greeting.
2. Voice Input: Click Listen and speak a command into the microphone.
3. Speech Recognition: Convert the recorded audio into text.
4. Command Processing: Match the recognized text against supported commands.
5. Action Execution: Perform the requested operation, such as opening a website or retrieving a Wikipedia summary.
6. Voice Response: Generate a spoken response using text-to-speech.
7. Interface Update: Display the conversation and update the assistant's visual status.

Project Structure
text
Friday-AI/
├── app.py
├── README.md
└── requirements.txt

- `app.py` — Main application, interface, speech recognition, command processing, and text-to-speech.
- `README.md` — Project documentation.
- `requirements.txt` — Python dependencies.

Limitations
- Speech recognition requires internet access when using Google's recognition service.
- The current speech engine configuration is designed for Windows.
- Only the commands explicitly implemented in the code are supported.
- Microphone permissions and audio-device availability may affect operation.
- The current version is a prototype and does not provide unrestricted computer control or a general-purpose AI conversation engine.

Future Enhancements
- Add more voice commands to launch desktop applications.
- Integrate an AI language model for more natural conversations.
- Implement reminders, alarms, and task management.
- Add secure system automation and configurable shortcuts.
- Improve error handling and cross-platform compatibility.
- Introduce customizable wake-word detection and conversation history.

Learning Outcomes
This project demonstrates practical experience with Python programming, speech recognition, text-to-speech, web application development, browser automation, background threading, queue-based communication, and user interface design.

Author
Rishabh Chandra
B.Tech in Computer Science | Aspiring Technology Professional

⭐ If you find this project interesting, consider starring the repository!
