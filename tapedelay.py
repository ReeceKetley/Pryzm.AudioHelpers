import sounddevice as sd
import numpy as np

def apply_tape_delay(input_audio, delay_samples, feedback=0.5, mix=0.5):
    """
    Applies a tape delay effect to an audio signal.

    :param input_audio: The input audio signal.
    :param delay_samples: Number of delay samples.
    :param feedback: Feedback gain (default is 0.5).
    :param mix: Wet/dry mix (default is 0.5).
    :return: The audio signal with the tape delay effect applied.
    """
    output_audio = np.zeros_like(input_audio)
    buffer = np.zeros(delay_samples)
    buffer_index = 0
    for i, x in enumerate(input_audio):
        output_audio[i] = mix * (x + feedback * buffer[buffer_index])
        buffer[buffer_index] = x
        buffer_index = (buffer_index + 1) % delay_samples
    return output_audio


# This bit is purely for testing you may want to swap this out to suit your own needs

def main():
    # Set audio device settings
    samplerate = 44100
    channels = 1
    blocksize = 1024
    device = sd.default.device
    dtype = 'float32'

    # Define audio input and output callback functions
    def audio_input_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        outdata[:] = apply_tape_delay(indata[:, 0], samplerate * 0.1)

    def audio_output_callback(outdata, frames, time, status):
        if status:
            print(status, file=sys.stderr)

    with sd.InputStream(samplerate=samplerate, channels=channels, blocksize=blocksize, device=device, dtype=dtype, callback=audio_input_callback):
        with sd.OutputStream(samplerate=samplerate, channels=channels, blocksize=blocksize, device=device, dtype=dtype, callback=audio_output_callback):
            print("Starting audio processing with tape delay...")
            while True:
                sd.sleep(100)

if __name__ == '__main__':
    main()