# Basic Ableton Remote Script

A simple Remote Script to test Ableton Live control functionality. This script provides basic transport control and track information display.

## Features

- Transport control (play/stop)
- Track information display
- Basic logging

## Installation

1. Find your Ableton Live Remote Scripts folder:
   - Windows: `C:\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts`
   - macOS: `/Applications/Ableton Live x.x Standard/Contents/App-Resources/MIDI Remote Scripts`

2. Create a new folder called `BasicRemote`

3. Copy these files into the `BasicRemote` folder:
   - `__init__.py`
   - `BasicRemote.py`

4. Restart Ableton Live

5. In Preferences > Link/MIDI, select 'BasicRemote' as a Control Surface

## Usage

Once installed and selected as a Control Surface, the script will:
- Show a message when loaded
- Display the number of tracks in your project
- Log track names and volumes
- Enable transport controls

## Development

This is a basic example that can be extended with:
- MIDI mapping
- Device control
- Mixer control
- Clip launching
- Custom UI feedback

Check Ableton's _Framework classes for more functionality.