import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(filename='Vrec.wav', duration=10, fs=44100):
    """
    Records audio from the microphone and saves it to a .wav file.

    Parameters:
    - filename: Name of the output file
    - duration: Duration in seconds to record
    - fs: Sampling rate (Hz)
    """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)  # Save as WAV file
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    record_voice()
