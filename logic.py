
from pytube import YouTube

# Function to extract audio from a YouTube video
def extract_audio(youtube_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)

        print("Getting Audio!")
        filename = f"{yt.title}.mp3"
        # Get the best stream with audio (usually the highest quality)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream to the specified output path
        audio_stream.download(output_path=output_path, filename= filename)
        print("Audio extraction completed successfully!")
       

    except Exception as e:
        print("An error occurred:", str(e))
        filename = None

    return filename

if __name__ == "__main__":
    # Replace 'youtube_url' with the URL of the video you want to extract audio from
    youtube_url = "https://youtu.be/OUo8QDHrCGM"

    # Replace 'output_path' with the directory where you want to save the audio file
    output_path = "resources/"

    extract_audio(youtube_url, output_path)
