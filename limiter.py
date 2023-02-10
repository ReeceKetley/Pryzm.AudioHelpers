import sounddevice as sd
import numpy as np

def apply_limiter(input_audio, threshold=-3):
    """
    Applies limiting to an audio signal.

    :param input_audio: The input audio signal.
    :param threshold: Limiting threshold (default is -3 dB).
    :return: The limited audio signal.
    """
    limited_audio = np.clip(input_audio, -threshold, threshold)
    return limited_audio

def main():
    # Set audio device settings
    samplerate = 44100
    channels = 2
    blocksize = 1024
    device = sd.default.device
    dtype = 'float32'

    # Define audio input and output callback functions
    def audio_input_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        outdata[:] = apply_limiter(indata[:, 0])

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