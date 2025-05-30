<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
      <h1>Voice-recorder</h1>
      <p>This Python script records audio from the microphone and saves it as a WAV file named Vrec.wav. It uses the sounddevice library to capture audio and scipy.io.wavfile to write the recording to disk. The default settings include a sample rate of 44,100 Hz, stereo channels, and a 10-second recording duration. It is a simple and effective way to create a basic voice recorder that stores audio locally.</p>
<hr>
<h1>To Run</h1>
<p>Install Flask:  pip install sounddevice scipy  </p>
<p>Run app:  python Vrec.py </p>
<hr>
<h1>Ourput</h1>
<audio controls>
    <source src="out.wav" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>

    
</body>
</html>
