import sounddevice as sd
import numpy as np

def apply_compression(input_audio, ratio=2, threshold=-24, attack=0.01, release=0.1):
    """
    Applies compression to an audio signal.

    :param input_audio: The input audio signal.
    :param ratio: Compression ratio (default is 2).
    :param threshold: Compression threshold (default is -24 dB).
    :param attack: Attack time (default is 0.01 seconds).
    :param release: Release time (default is 0.1 seconds).
    :return: The compressed audio signal.
    """
    # Convert attack and release times to sample numbers
    attack_samples = int(attack * sd.default.samplerate)
    release_samples = int(release * sd.default.samplerate)

    # Initialize gain and gain_slope arrays
    gain = np.zeros(input_audio.shape)
    gain_slope = np.zeros(input_audio.shape)

    # Compute gain
    for i in range(1, input_audio.size):
        if input_audio[i] > gain[i - 1] + threshold:
            gain[i] = gain[i - 1] + threshold
        elif input_audio[i] < gain[i - 1] + threshold:
            gain[i] = gain[i - 1] + threshold + (input_audio[i] - (gain[i - 1] + threshold)) / ratio
        else:
            gain[i] = gain[i - 1]

    # Smoothen gain changes with attack and release times
    for i in range(1, input_audio.size):
        if gain[i] > gain[i - 1]:
            gain_slope[i] = np.minimum(gain_slope[i - 1] + 1 / attack_samples, 1)
        else:
            gain_slope[i] = np.maximum(gain_slope[i - 1] - 1 / release_samples, 0)
        gain[i] = gain[i - 1] + (gain[i] - Gain[i - 1]) * gain_slope[i]

    # Apply gain to audio
    compressed_audio = input_audio * gain

    return compressed_audio

# This bit is purely for testing you may want to swap this out to suit your own needs

def main():
    # Set audio device settings
    samplerate = 44100 # Set your sample rate here
    channels = 2
    blocksize = 1024
    device = sd.default.device # Set your device here
    dtype = 'float32'

    # Define audio input and output callback functions
    def audio_input_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        outdata[:] = apply_compression(indata[:, 0])

    def audio_output_callback(outdata, frames, time, status):
        if status:
            print(status, file=sys.stderr)

    with sd.InputStream(samplerate=samplerate, channels=channels, blocksize=blocksize, device=device, dtype=dtype, callback=audio_input_callback):
        with sd.OutputStream(samplerate=samplerate, channels=channels, blocksize=blocksize, device=device, dtype=dtype, callback=audio_output_callback):
            print("Starting audio limiting...")
            while True:
                sd.sleep(100)

if __name__ == '__main__':
    main()