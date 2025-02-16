from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent

class BasicRemote(ControlSurface):
    def __init__(self, c_instance):
        super(BasicRemote, self).__init__(c_instance)
        with self.component_guard():
            self._create_transport()
            self.show_message('Basic Remote Script loaded')

    def _create_transport(self):
        self._transport = TransportComponent()
        self._transport.set_enabled(True)

    def disconnect(self):
        self.show_message('Basic Remote Script disconnected')
        super(BasicRemote, self).disconnect()

    def refresh_state(self):
        super(BasicRemote, self).refresh_state()
        self._update_display()

    def _update_display(self):
        tracks = self.song().tracks
        self.show_message(f'Number of tracks: {len(tracks)}')
        for track in tracks:
            self.log_message(f'Track: {track.name} - Volume: {track.mixer_device.volume.value}')