# Basic Ableton Remote Script

A simple Remote Script to test Ableton Live control functionality. This script provides basic transport control, track information display, and smart performance features.

## Features

* Transport control (play/stop)
* Track information display
* Basic logging
* Smart Performance Suite:
  * Intelligent tempo sync
  * Auto-quantization for MIDI clips
  * Smart monitoring system
  * Performance metrics display

## Installation

1. Find your Ableton Live Remote Scripts folder:  
   * Windows: `C:\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts`  
   * macOS: `/Applications/Ableton Live x.x Standard/Contents/App-Resources/MIDI Remote Scripts`
2. Create a new folder called `BasicRemote`
3. Copy these files into the `BasicRemote` folder:  
   * `__init__.py`  
   * `SmartPerformanceSuite.py`
4. Restart Ableton Live
5. In Preferences > Link/MIDI, select 'BasicRemote' as a Control Surface

## Usage

Once installed and selected as a Control Surface, the script will:

* Show a message when loaded
* Display the number of tracks in your project
* Log track names and volumes
* Enable transport controls
* Provide smart performance features:
  * Automatic tempo sync based on MIDI clock
  * Auto-quantization for newly recorded MIDI clips
  * Intelligent monitoring state management
  * Real-time performance metrics display

## Development

This script demonstrates advanced features that can be extended with:

* MIDI mapping
* Device control
* Mixer control
* Clip launching
* Custom UI feedback

Check Ableton's _Framework classes for more functionality.

## MIDI Control Mappings

* Play: Note 118
* Stop: Note 117
* Tempo Control: CC 14

Adjust these mappings in `SmartPerformanceSuite.py` to match your MIDI controller.