import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv.power_status() == False, "TV initial status should be set to FALSE"
    assert tv.current_channel() == Television.MIN_CHANNEL, "Initial channel should be equal to the MIN_CHANNEL"
    assert tv.current_volume() == Television.MIN_VOLUME, "Initial channel should be equal to the MIN_VOLUME"

def test_power():
    tv = Television()
    tv.power()
    assert tv.power_status() == True, "TV power status should be ON/TRUE after powered"
    tv.power()
    assert tv.power_status() == False, "TV power status should be OFF/FALSE after powered"

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv.is_muted() == True, "TV should be muted"
    tv.mute()
    assert tv.is_muted() == False, "TV should NOT be muted"

def test_channel_up():
    tv = Television()
    tv.power()
    initial_channel = tv.current_channel()
    tv.channel_up()
    assert tv.current_channel() == initial_channel + 1, "Channel value should be increased by 1"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_up()
    initial_channel = tv.current_channel()
    tv.channel_down()
    assert tv.current_channel() == initial_channel - 1, "Channel value should be decreased by 1"

def test_volume_up():
    tv = Television()
    tv.power()
    initial_volume = tv.current_volume()
    tv.volume_up()
    assert tv.current_volume() == initial_volume + 1, "Volume should be increased by 1 (INITIAL VOLUME = 0)"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    initial_volume = tv.current_volume()
    tv.volume_down()
    assert tv.current_volume() == initial_volume - 1, "Volume should be decreased by 1 (INITIAL VOLUME = 0)"