# coding=utf-8

import unittest
import mock

from gpio_wrapper.gpio_commands import write, mode
from gpio_wrapper.errors import WrongPinNumber, WrongMode, WrongWriteValue


class GPIOCommandsWriteTestCase(unittest.TestCase):

    @mock.patch('gpio_wrapper.gpio_commands.system')
    def test_write_1_high(self, mock_system):
        write(pin=1, value=1)
        mock_system.assert_called_with('gpio -g write 1 1')

    @mock.patch('gpio_wrapper.gpio_commands.system')
    def test_write_0_low(self, mock_system):
        write(pin=0, value=0)
        mock_system.assert_called_with('gpio -g write 0 0')

    def test_write_wrong_pin(self):
        with self.assertRaises(WrongPinNumber):
            write(pin=26, value=1)

    def test_write_wrong_value(self):
        with self.assertRaises(WrongWriteValue):
            write(pin=1, value=2)


class GPIOCommandsModeTestCase(unittest.TestCase):

    @mock.patch('gpio_wrapper.gpio_commands.system')
    def test_mode_1_out(self, mock_system):
        mode(pin=1, set_mode='out')
        mock_system.assert_called_with('gpio -g mode 1 out')

    @mock.patch('gpio_wrapper.gpio_commands.system')
    def test_mode_0_in(self, mock_system):
        mode(pin=0, set_mode='in')
        mock_system.assert_called_with('gpio -g mode 0 in')

    def test_mode_wrong_pin(self):
        with self.assertRaises(WrongPinNumber):
            mode(pin=26, set_mode='out')

    def test_write_wrong_mode(self):
        with self.assertRaises(WrongMode):
            mode(pin=1, set_mode='wrong_mode')
