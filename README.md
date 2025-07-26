# THM Room Tracker Repository

This repository contains two versions of the TryHackMe Room Tracker project, allowing users to choose between a simple localStorage-based tracker and a more advanced backend-supported tracker.

## Project Versions

### Version 1: THM-Room-Tracker-v1

- A simple tracker implemented as a single `index.html` file.
- Uses browser localStorage to save the completion state of rooms.
- No backend server required.
- Suitable for users who prefer a lightweight, client-only solution.

### Version 2: THM-Free-Rooms-Tracker (Current Project)

- A web-based tracker with backend support using Flask.
- Tracks TryHackMe rooms organized by category with progress bars and search functionality.
- Saves completion state persistently on the server using JSON.
- Responsive design with enhanced user experience.

## Repository Structure

```
repo-root/
│
├── THM-Free-Rooms-Tracker-v1/
│   └── index.html
│
└── THM-Free-Rooms-Tracker-v2/
    ├── app.py
    ├── requirements.txt
    ├── room_state.json
    └── templates/
        └── THM-Free-Rooms-Tracker.html
```

## Features of THM-Free-Rooms-Tracker

- Track completion status of TryHackMe rooms using interactive checkboxes.
- Visual progress bars for each category and overall progress tracking.
- Real-time search and filtering of rooms by name.
- Persistent state saved on the server via backend API calls.
- Responsive and modern design for usability across devices.
- Categorization of rooms into multiple cybersecurity domains such as Intro Rooms, Basic Rooms, Recon, Networking, and more.

## Getting Started with THM-Free-Rooms-Tracker

### Prerequisites

- Python 3.x
- Flask (install via `pip install -r requirements.txt`)

### Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/sundarAlok/THM-Free-Rooms-Tracker.git
   cd THM-Free-Rooms-Tracker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask backend server:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to:

   ```
   http://localhost:5000/
   ```

5. Use the tracker to mark rooms as completed, search rooms, and monitor your progress.

## Usage of THM-Room-Tracker-v1

- Open the `index.html` file located in the `THM-Room-Tracker-v1` folder directly in your browser.
- Use the checkboxes to mark rooms as completed.
- The state is saved locally in your browser's localStorage.

## Screenshots

![Tracker Screenshot 1](https://github.com/user-attachments/assets/ad7a0c7a-e920-4c41-a4be-2d69b9c4af54)
![Tracker Screenshot 2](https://github.com/user-attachments/assets/0e6887ec-93d1-416f-8767-6d7bfa1edd73)

## Technologies Used

- Python (Flask) for backend in THM-Free-Rooms-Tracker
- HTML5, CSS3, JavaScript (ES6)
- JSON for state management in THM-Free-Rooms-Tracker

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

- [sundarAlok](https://github.com/sundarAlok)

## Contributing

Contributions are welcome! Please open an issue to discuss major changes before submitting a pull request.

## Acknowledgments

- TryHackMe platform for the room content inspiration
- Flask framework for backend support
- Open source community for continuous learning and support
