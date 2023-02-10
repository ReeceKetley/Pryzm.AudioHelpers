# Pryzm.AudioHelpers
A collection of functions to help with realtime audio processing.

Quite basic uses sounddevice for device input and output but any other audio device lib should work just fine.

Clipper.py - Applies clipping to an audio signal with a settable threshold default is -3dB <br>
    :param input_audio: The input audio signal.
    :param threshold: Clipping threshold (default is -3 dB).
    :return: The clipped audio signal.

Limiter.py - Applies limiting to an audio signal with a settable threshold defualt is -3dB
    :param input_audio: The input audio signal.
    :param threshold: Limiting threshold (default is -3 dB).
    :return: The limited audio signal.

Compression.py - Applies compression to an audio signal.
    :param input_audio: The input audio signal.
    :param ratio: Compression ratio (default is 2).
    :param threshold: Compression threshold (default is -24 dB).
    :param attack: Attack time (default is 0.01 seconds).
    :param release: Release time (default is 0.1 seconds).
    :return: The compressed audio signal.
    
Tapedelay.py - Applies a tape delay effect with settable feedback & mix
    :param input_audio: The input audio signal.
    :param delay_samples: Number of delay samples.
    :param feedback: Feedback gain (default is 0.5).
    :param mix: Wet/dry mix (default is 0.5).
    :return: The audio signal with the tape delay effect applied.
    
Ill be adding more as i make them use them however you see fit!
