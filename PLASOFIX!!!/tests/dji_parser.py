#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Safari cookie parser."""

import unittest

from plaso.parsers import dji_parser

from tests.parsers import test_lib


class DJIDroneLogParserTest(test_lib.ParserTestCase):
  """Tests for the Safari cookie parser."""

  def testParseFile(self):
    """Tests the Parse function on a Safari binary cookies file."""
    parser = dji_parser.DJIDroneLogParser()
    storage_writer = self._ParseFile(['17-08-29-12-58-45_FLY005.DAT'], parser)

    # There should be:
    # * 207 events in total
    # * 182 events from the safari cookie parser
    # * 25 event from the cookie plugins

    number_of_event_data = storage_writer.GetNumberOfAttributeContainers(
        'event_data')
    self.assertEqual(number_of_event_data, 1786)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    expected_event_values = {
        'longitude': -106.2163995,
        'latitude': 39.9612155,
        'data_type': 'drone:dji:mavic',
        'timestamp': '2017-08-29T18:58:43+00:00',
        'height': 2481.301}
    
    event_data = storage_writer.GetAttributeContainerByIndex('event_data', 26)
    self.CheckEventData(event_data, expected_event_values)


if __name__ == '__main__':
  unittest.main()
