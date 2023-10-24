# YouTube Video Repurposer 1.0

![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

**YouTube Video Repurposer 1.0** is a Python application that allows you to transcribe YouTube videos and repurpose the content for social media.

## Features

- Transcribe YouTube videos to text
- Split transcribed text into chunks
- Generate social media points from text chunks
- Download transcriptions for later use

## Demo

You can see a live demo of this application [here](https://github.com/Softtech247/repurposer.git).

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python (3.6+)
- pip
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Softtech247/repurposer.git
   cd your-repo

Continuing from where we left off:

```markdown
   git clone https://github.com/Softtech247/repurposer.git
   cd repurposer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your-api-key-here
   ```

### Usage

1. Run the application:

   ```bash
   streamlit run main.py
   ```

2. Enter a YouTube URL, and the application will transcribe the video and generate social media points.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [OpenAI](https://openai.com) for the GPT-3 model
```

You can continue with this template and make any necessary adjustments to suit your project's information.