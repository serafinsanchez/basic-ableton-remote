from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.MixerComponent import MixerComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.ClipCreator import ClipCreator
import Live

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1

class SmartPerformanceSuite(ControlSurface):
    def __init__(self, c_instance):
        super(SmartPerformanceSuite, self).__init__(c_instance)
        with self.component_guard():
            self._init_controls()
            self._init_transport()
            self._init_mixer()
            self._init_session()
            self._init_smart_features()
            self.show_message('Smart Performance Suite loaded')

    def _init_controls(self):
        # Map common MIDI controls (adjust these based on your MIDI controller)
        self.play_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 118)
        self.stop_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 117)
        self.tempo_encoder = EncoderElement(MIDI_CC_TYPE, 0, 14, Live.MidiMap.MapMode.relative_smooth_two_compliment)
        
    def _init_transport(self):
        self._transport = TransportComponent()
        self._transport.set_play_button(self.play_button)
        self._transport.set_stop_button(self.stop_button)
        
    def _init_mixer(self):
        self._mixer = MixerComponent(8)  # 8 tracks
        self._mixer.set_enabled(True)
        
    def _init_session(self):
        self._session = SessionComponent(8, 8)  # 8x8 clip matrix
        self._session.set_enabled(True)
        
    def _init_smart_features(self):
        self._setup_tempo_sync()
        self._setup_auto_quantize()
        self._setup_smart_monitoring()
        
    def _setup_tempo_sync(self):
        """Intelligent tempo sync that adjusts based on incoming MIDI clock"""
        def on_tempo_change(value):
            tempo = self.song().tempo
            new_tempo = tempo + (value * 0.1)  # Fine-grained tempo control
            self.song().tempo = new_tempo
            
        self.tempo_encoder.add_value_listener(on_tempo_change)
        
    def _setup_auto_quantize(self):
        """Automatically quantizes newly recorded clips"""
        def on_new_clip(clip_slot, clip):
            if clip and clip.is_midi_clip:
                clip.quantize(5)  # 1/16 note quantization
                clip.quantize_pitch(5)
                
        self.song().add_clip_creator_listener(on_new_clip)
        
    def _setup_smart_monitoring(self):
        """Intelligent auto-monitoring system"""
        def on_record_mode_changed():
            selected_track = self.song().view.selected_track
            if self.song().record_mode:
                selected_track.input_monitoring_state = 1  # In
            else:
                selected_track.input_monitoring_state = 0  # Auto
                
        self.song().add_record_mode_listener(on_record_mode_changed)
        
    def disconnect(self):
        self.show_message('Smart Performance Suite disconnected')
        super(SmartPerformanceSuite, self).disconnect()

    def refresh_state(self):
        super(SmartPerformanceSuite, self).refresh_state()
        self._update_display()

    def _update_display(self):
        """Update display with current performance metrics"""
        song = self.song()
        selected_track = song.view.selected_track
        playing_clip = None
        
        for clip_slot in selected_track.clip_slots:
            if clip_slot.is_playing:
                playing_clip = clip_slot.clip
                break
                
        status = f"BPM: {song.tempo}"
        if playing_clip:
            status += f" | Clip: {playing_clip.name}"
        
        self.show_message(status)