# Pryzm.AudioHelpers
A collection of functions to help with realtime audio processing.

Quite basic uses sounddevice for device input and output but any other audio device lib should work just fine.

Clipper.py - Applies clipping to an audio signal with a settable threshold default is -3dB<br>
    :param input_audio: The input audio signal.<br>
    :param threshold: Clipping threshold (default is -3 dB).<br>
    :return: The clipped audio signal.<br>

Limiter.py - Applies limiting to an audio signal with a settable threshold defualt is -3dB<br>
    :param input_audio: The input audio signal.<br>
    :param threshold: Limiting threshold (default is -3 dB).<br>
    :return: The limited audio signal.<br>

Compression.py - Applies compression to an audio signal.<br>
    :param input_audio: The input audio signal.<br>
    :param ratio: Compression ratio (default is 2).<br>
    :param threshold: Compression threshold (default is -24 dB).<br>
    :param attack: Attack time (default is 0.01 seconds).<br>
    :param release: Release time (default is 0.1 seconds).<br>
    :return: The compressed audio signal.<br>
    
Tapedelay.py - Applies a tape delay effect with settable feedback & mix<br>
    :param input_audio: The input audio signal.<br>
    :param delay_samples: Number of delay samples.<br>
    :param feedback: Feedback gain (default is 0.5).<br>
    :param mix: Wet/dry mix (default is 0.5).<br>
    :return: The audio signal with the tape delay effect applied.<br>
    
Ill be adding more as i make them use them however you see fit!
