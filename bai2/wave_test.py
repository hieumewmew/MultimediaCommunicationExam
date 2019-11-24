import math
import wave
import struct
import os

# 44100 is the industry standard sample rate - CD quality
sample_rate = 44100.044

def make_audio(duration_milliseconds=250, volume=0.5):
    audio = []
    freq_nor = 440
    freq_rate=math.pow(2, 1/12.0)
    num_samples_per_node = duration_milliseconds * (sample_rate / 1000.0)

    for i in range(12):
        freq = freq_nor*math.pow(freq_rate,i-8)

        for x in range(int(num_samples_per_node)):
            sample = volume * math.sin(2 * math.pi * freq * ( x / sample_rate ))
            audio.append(sample)

    return audio

def save_wav(audio, file_name):

    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1
    sampwidth = 2
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the 
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return


audio = make_audio()
save_wav(audio, os.path.join('bai2',"output.wav"))