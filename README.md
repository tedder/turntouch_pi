
Dispatch events from a [TurnTouch](), using a Raspberry Pi with [bluepy](http://ianharvey.github.io/bluepy-doc/index.html).

Designing on a Pi Zero W. Should work on Pi3 too. Python3 is a minimum requirement too- no effort will be put towards py2. Breaking changes will be allowed until we decide it's releaseable.

grep 'TODO' if you want to jump in. Currently working on monitor.py.

# dependencies to put in reqs.txt
bluepy>=0.9.11



## Notes about other libs etc
pybluez is 3 years old, there's a recent-ish update to work with BTLE but it isn't released
  https://github.com/karulis/pybluez


## turntouch scan signatures from scan.py
Device e7:5b:f9:bf:02:52 (random), RSSI=-33 dB
  Short Local Name = Turn Touch Rem
  Appearance = 8001
  Complete 16b Services = 0f180a182315
  Flags = 06
Device d2:e5:5b:7e:f6:51 (random), RSSI=-52 dB
  Short Local Name = Turn Touch Rem
  Appearance = 8001
  Complete 16b Services = 0f180a182315
  Flags = 06
Device e6:a8:90:2e:62:6d (random), RSSI=-40 dB
  Short Local Name = Turn Touch Rem
  Appearance = 8001
  Complete 16b Services = 0f180a182315
  Flags = 06


# License

MIT license. Will flesh out before first release, but every commit to this repo is under the MIT license.
