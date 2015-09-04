# -*- coding: utf-8  -*-
"""Tests for round-robin schedulers."""

# Copyright (C) 2015 Alexander Jones
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import random
# import unittest

from . import TestCase, PY2, PY3

from competitions.scheduler import ScheduleGenerationFailed
from competitions.scheduler.roundrobin import (
    RoundRobinScheduler,
    SingleRoundRobinScheduler,
    DoubleRoundRobinScheduler,
    TripleRoundRobinScheduler,
    QuadrupleRoundRobinScheduler
)


class TestSingleRoundRobin(TestCase):

    """Tests for single round-robin scheduling."""

    def test_match_generation(self):
        """Test single round-robin match generation."""
        # Four teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(4)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (1, 4),
                (2, 3), (4, 2), (3, 4)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1),
                (2, 3), (2, 4), (3, 4)
            ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for single '
                               'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(3)
        if PY2:
            expected_matches = [
                (2, 1), (1, 3), (3, 2),
                (1, None), (None, 2), (None, 3)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (2, 3),
                (1, None), (None, 2), (None, 3)
            ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for single '
                               'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(8)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (6, 1), (1, 7), (1, 8),
                (2, 3), (2, 4), (5, 2), (6, 2), (7, 2), (2, 8),
                (4, 3), (5, 3), (3, 6), (3, 7), (3, 8),
                (5, 4), (4, 6), (4, 7), (8, 4),
                (6, 5), (7, 5), (5, 8),
                (7, 6), (8, 6),
                (8, 7)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (1, 6), (1, 7), (8, 1),
                (3, 2), (2, 4), (5, 2), (2, 6), (7, 2), (2, 8),
                (3, 4), (5, 3), (6, 3), (3, 7), (8, 3),
                (4, 5), (4, 6), (7, 4), (8, 4),
                (5, 6), (5, 7), (8, 5),
                (6, 7), (6, 8),
                (7, 8)
            ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for single '
                               'round-robin schedule with eight teams.'))

    def test_matrix_generation(self):
        """Test single round-robin matrix generation."""
        # Four teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(4)
        if PY2:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, True],
                [False, True, False, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False],
                [False, None, True, True],
                [True, False, None, True],
                [True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for single '
                              'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(3)
        if PY2:
            expected_matrix = [
                [None, False, True, True],
                [True, None, False, False],
                [False, True, None, False],
                [False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, False],
                [False, True, True, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for single '
                              'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = SingleRoundRobinScheduler(8)
        if PY2:
            expected_matrix = [
                [None, True, False, False, True, False, True, True],
                [False, None, True, True, False, False, False, True],
                [True, False, None, False, False, True, True, True],
                [True, False, True, None, False, True, True, False],
                [False, True, True, True, None, False, False, True],
                [True, True, False, False, True, None, False, False],
                [False, True, False, False, True, True, None, False],
                [False, False, False, True, False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False, True, True, True, False],
                [False, None, False, True, False, True, False, True],
                [True, True, None, True, False, False, True, False],
                [True, False, False, None, True, True, False, False],
                [False, True, True, False, None, True, True, False],
                [False, False, True, False, False, None, True, True],
                [False, True, False, True, False, False, None, True],
                [True, False, True, True, True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for single '
                              'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test single round-robin schedule generation."""
        scheduler = SingleRoundRobinScheduler(8)
        # Failed attempt
        random.seed(17)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(4)
        if PY2:
            expected_schedule = [
                [(2, 5), (8, 6), (7, 1), (3, 4)],
                [(5, 8), (3, 7), (1, 2), (4, 6)],
                [(5, 4), (6, 3), (2, 7), (8, 1)],
                [(7, 8), (6, 5), (2, 4), (3, 1)],
                [(6, 2), (3, 8), (7, 5), (1, 4)],
                [(7, 6), (2, 3), (4, 8), (1, 5)],
                [(5, 3), (1, 6), (4, 7), (8, 2)]
            ]
        elif PY3:
            expected_schedule = [
                [(5, 7), (8, 4), (3, 6), (1, 2)],
                [(4, 2), (6, 8), (1, 5), (3, 7)],
                [(8, 1), (6, 4), (3, 5), (7, 2)],
                [(4, 1), (2, 3), (5, 8), (6, 7)],
                [(8, 3), (2, 6), (4, 5), (7, 1)],
                [(8, 2), (1, 3), (5, 6), (4, 7)],
                [(1, 6), (3, 4), (7, 8), (2, 5)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'single round-robin competition'))

    def test_bypassed_schedule_generation(self):
        """Test bypassed single round-robin schedule generation.

        This test uses RoundRobinScheduler directly, instead of
        SingleRoundRobinScheduler.
        """
        scheduler = RoundRobinScheduler(8, meetings=1)
        # Failed attempt
        random.seed(17)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(4)
        if PY2:
            expected_schedule = [
                [(2, 5), (8, 6), (7, 1), (3, 4)],
                [(5, 8), (3, 7), (1, 2), (4, 6)],
                [(5, 4), (6, 3), (2, 7), (8, 1)],
                [(7, 8), (6, 5), (2, 4), (3, 1)],
                [(6, 2), (3, 8), (7, 5), (1, 4)],
                [(7, 6), (2, 3), (4, 8), (1, 5)],
                [(5, 3), (1, 6), (4, 7), (8, 2)]
            ]
        elif PY3:
            expected_schedule = [
                [(5, 7), (8, 4), (3, 6), (1, 2)],
                [(4, 2), (6, 8), (1, 5), (3, 7)],
                [(8, 1), (6, 4), (3, 5), (7, 2)],
                [(4, 1), (2, 3), (5, 8), (6, 7)],
                [(8, 3), (2, 6), (4, 5), (7, 1)],
                [(8, 2), (1, 3), (5, 6), (4, 7)],
                [(1, 6), (3, 4), (7, 8), (2, 5)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for bypassed '
                              'single round-robin competition'))

    def test_repeated_schedule_generation(self):
        """Test repeated single round-robin schedule generation."""
        scheduler = SingleRoundRobinScheduler(8)
        random.seed(17)
        if PY2:
            expected_schedule = [
                [(7, 5), (3, 6), (2, 1), (4, 8)],
                [(7, 3), (6, 5), (1, 8), (4, 2)],
                [(5, 3), (8, 6), (1, 4), (2, 7)],
                [(1, 6), (5, 2), (7, 8), (3, 4)],
                [(8, 5), (2, 3), (6, 4), (7, 1)],
                [(4, 7), (8, 3), (6, 2), (5, 1)],
                [(6, 7), (2, 8), (3, 1), (4, 5)]
            ]
        elif PY3:
            expected_schedule = [
                [(8, 7), (1, 6), (3, 5), (4, 2)],
                [(2, 6), (4, 3), (7, 1), (5, 8)],
                [(7, 3), (4, 1), (6, 8), (2, 5)],
                [(7, 4), (3, 1), (5, 6), (8, 2)],
                [(7, 2), (3, 6), (1, 5), (8, 4)],
                [(6, 4), (8, 3), (2, 1), (5, 7)],
                [(2, 3), (6, 7), (5, 4), (1, 8)]
            ]
        schedule = scheduler.generate_schedule()
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for repeated '
                              'single round-robin competition'))


class TestDoubleRoundRobin(TestCase):

    """Tests for double round-robin scheduling."""

    def test_match_generation(self):
        """Test double round-robin match generation."""
        # Four teams
        scheduler = DoubleRoundRobinScheduler(4)
        expected_matches = [
            (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 4),
            (4, 1), (4, 2), (4, 3)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for double '
                               'round-robin schedule with four teams.'))
        # Three teams
        scheduler = DoubleRoundRobinScheduler(3)
        expected_matches = [
            (1, 2), (1, 3), (1, None),
            (2, 1), (2, 3), (2, None),
            (3, 1), (3, 2), (3, None),
            (None, 1), (None, 2), (None, 3)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for double '
                               'round-robin schedule with three teams.'))
        # Eight teams
        scheduler = DoubleRoundRobinScheduler(8)
        expected_matches = [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for double '
                               'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test double round-robin schedule generation."""
        scheduler = DoubleRoundRobinScheduler(8)
        # Failed attempt
        random.seed(5)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(2)
        if PY2:
            expected_schedule = [
                [(5, 6), (7, 4), (3, 8), (1, 2)],
                [(5, 1), (8, 4), (3, 6), (2, 7)],
                [(3, 1), (6, 5), (4, 8), (7, 2)],
                [(8, 5), (3, 2), (1, 4), (7, 6)],
                [(1, 8), (7, 3), (2, 6), (4, 5)],
                [(8, 1), (6, 3), (5, 7), (4, 2)],
                [(6, 1), (2, 5), (4, 3), (8, 7)],
                [(2, 4), (6, 8), (7, 5), (1, 3)],
                [(5, 4), (2, 1), (8, 6), (3, 7)],
                [(4, 7), (2, 8), (3, 5), (1, 6)],
                [(4, 6), (1, 7), (2, 3), (5, 8)],
                [(5, 3), (7, 8), (6, 2), (4, 1)],
                [(7, 1), (5, 2), (6, 4), (8, 3)],
                [(1, 5), (3, 4), (8, 2), (6, 7)]
            ]
        elif PY3:
            expected_schedule = [
                [(3, 2), (4, 1), (8, 5), (6, 7)],
                [(3, 8), (1, 6), (7, 5), (2, 4)],
                [(6, 8), (4, 7), (2, 3), (5, 1)],
                [(2, 1), (5, 7), (3, 6), (8, 4)],
                [(5, 4), (6, 2), (3, 7), (1, 8)],
                [(4, 3), (7, 2), (5, 6), (8, 1)],
                [(3, 1), (5, 2), (8, 6), (7, 4)],
                [(7, 1), (6, 4), (5, 3), (2, 8)],
                [(8, 7), (4, 6), (3, 5), (1, 2)],
                [(3, 4), (7, 8), (6, 1), (2, 5)],
                [(1, 4), (7, 3), (5, 8), (2, 6)],
                [(1, 3), (2, 7), (4, 8), (6, 5)],
                [(4, 5), (8, 2), (6, 3), (1, 7)],
                [(1, 5), (4, 2), (7, 6), (8, 3)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'double round-robin competition'))

    def test_bypassed_schedule_generation(self):
        """Test bypassed double round-robin schedule generation.

        This test uses RoundRobinScheduler directly, instead of
        DoubleRoundRobinScheduler.
        """
        scheduler = RoundRobinScheduler(8, meetings=2)
        # Failed attempt
        random.seed(5)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(2)
        if PY2:
            expected_schedule = [
                [(5, 6), (7, 4), (3, 8), (1, 2)],
                [(5, 1), (8, 4), (3, 6), (2, 7)],
                [(3, 1), (6, 5), (4, 8), (7, 2)],
                [(8, 5), (3, 2), (1, 4), (7, 6)],
                [(1, 8), (7, 3), (2, 6), (4, 5)],
                [(8, 1), (6, 3), (5, 7), (4, 2)],
                [(6, 1), (2, 5), (4, 3), (8, 7)],
                [(2, 4), (6, 8), (7, 5), (1, 3)],
                [(5, 4), (2, 1), (8, 6), (3, 7)],
                [(4, 7), (2, 8), (3, 5), (1, 6)],
                [(4, 6), (1, 7), (2, 3), (5, 8)],
                [(5, 3), (7, 8), (6, 2), (4, 1)],
                [(7, 1), (5, 2), (6, 4), (8, 3)],
                [(1, 5), (3, 4), (8, 2), (6, 7)]
            ]
        elif PY3:
            expected_schedule = [
                [(3, 2), (4, 1), (8, 5), (6, 7)],
                [(3, 8), (1, 6), (7, 5), (2, 4)],
                [(6, 8), (4, 7), (2, 3), (5, 1)],
                [(2, 1), (5, 7), (3, 6), (8, 4)],
                [(5, 4), (6, 2), (3, 7), (1, 8)],
                [(4, 3), (7, 2), (5, 6), (8, 1)],
                [(3, 1), (5, 2), (8, 6), (7, 4)],
                [(7, 1), (6, 4), (5, 3), (2, 8)],
                [(8, 7), (4, 6), (3, 5), (1, 2)],
                [(3, 4), (7, 8), (6, 1), (2, 5)],
                [(1, 4), (7, 3), (5, 8), (2, 6)],
                [(1, 3), (2, 7), (4, 8), (6, 5)],
                [(4, 5), (8, 2), (6, 3), (1, 7)],
                [(1, 5), (4, 2), (7, 6), (8, 3)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for bypassed '
                              'double round-robin competition'))

    def test_repeated_schedule_generation(self):
        """Test repeated double round-robin schedule generation."""
        scheduler = DoubleRoundRobinScheduler(8)
        random.seed(5)
        if PY2:
            expected_schedule = [
                [(8, 4), (3, 7), (1, 6), (2, 5)],
                [(7, 1), (6, 4), (8, 2), (5, 3)],
                [(1, 8), (2, 4), (7, 6), (3, 5)],
                [(2, 6), (5, 7), (4, 3), (8, 1)],
                [(8, 5), (1, 3), (7, 4), (6, 2)],
                [(2, 7), (4, 8), (5, 1), (3, 6)],
                [(1, 7), (6, 5), (2, 8), (3, 4)],
                [(1, 4), (8, 3), (5, 2), (6, 7)],
                [(2, 3), (4, 1), (6, 8), (7, 5)],
                [(1, 2), (5, 8), (7, 3), (4, 6)],
                [(4, 2), (6, 3), (1, 5), (7, 8)],
                [(4, 5), (8, 7), (3, 2), (6, 1)],
                [(2, 1), (4, 7), (3, 8), (5, 6)],
                [(7, 2), (8, 6), (5, 4), (3, 1)]
            ]
        elif PY3:
            expected_schedule = [
                [(4, 3), (8, 2), (6, 7), (5, 1)],
                [(5, 6), (2, 4), (3, 8), (1, 7)],
                [(6, 5), (4, 8), (1, 3), (7, 2)],
                [(8, 4), (1, 2), (5, 3), (7, 6)],
                [(8, 5), (2, 3), (7, 1), (4, 6)],
                [(4, 5), (8, 6), (2, 7), (3, 1)],
                [(2, 8), (3, 5), (1, 6), (7, 4)],
                [(6, 2), (1, 8), (3, 4), (7, 5)],
                [(5, 4), (8, 7), (2, 1), (6, 3)],
                [(8, 1), (3, 6), (4, 7), (2, 5)],
                [(4, 1), (5, 2), (7, 3), (6, 8)],
                [(6, 4), (7, 8), (1, 5), (3, 2)],
                [(8, 3), (5, 7), (2, 6), (1, 4)],
                [(5, 8), (3, 7), (6, 1), (4, 2)]
            ]
        schedule = scheduler.generate_schedule()
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for repeated '
                              'double round-robin competition'))


class TestTripleRoundRobin(TestCase):

    """Tests for triple round-robin scheduling."""

    def test_match_generation(self):
        """Test triple round-robin match generation."""
        # Four teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(4)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (1, 4),
                (2, 3), (4, 2), (3, 4)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1),
                (2, 3), (2, 4), (3, 4)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 4),
            (4, 1), (4, 2), (4, 3)
        ])
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for triple '
                               'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(3)
        if PY2:
            expected_matches = [
                (2, 1), (1, 3), (3, 2),
                (1, None), (None, 2), (None, 3)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (2, 3),
                (1, None), (None, 2), (None, 3)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, None),
            (2, 1), (2, 3), (2, None),
            (3, 1), (3, 2), (3, None),
            (None, 1), (None, 2), (None, 3)
        ])
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for triple '
                               'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(8)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (6, 1), (1, 7), (1, 8),
                (2, 3), (2, 4), (5, 2), (6, 2), (7, 2), (2, 8),
                (4, 3), (5, 3), (3, 6), (3, 7), (3, 8),
                (5, 4), (4, 6), (4, 7), (8, 4),
                (6, 5), (7, 5), (5, 8),
                (7, 6), (8, 6),
                (8, 7)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (1, 6), (1, 7), (8, 1),
                (3, 2), (2, 4), (5, 2), (2, 6), (7, 2), (2, 8),
                (3, 4), (5, 3), (6, 3), (3, 7), (8, 3),
                (4, 5), (4, 6), (7, 4), (8, 4),
                (5, 6), (5, 7), (8, 5),
                (6, 7), (6, 8),
                (7, 8)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ])
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for triple '
                               'round-robin schedule with eight teams.'))

    def test_matrix_generation(self):
        """Test triple round-robin matrix generation."""
        # Four teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(4)
        if PY2:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, True],
                [False, True, False, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False],
                [False, None, True, True],
                [True, False, None, True],
                [True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for triple '
                              'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(3)
        if PY2:
            expected_matrix = [
                [None, False, True, True],
                [True, None, False, False],
                [False, True, None, False],
                [False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, False],
                [False, True, True, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for triple '
                              'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = TripleRoundRobinScheduler(8)
        if PY2:
            expected_matrix = [
                [None, True, False, False, True, False, True, True],
                [False, None, True, True, False, False, False, True],
                [True, False, None, False, False, True, True, True],
                [True, False, True, None, False, True, True, False],
                [False, True, True, True, None, False, False, True],
                [True, True, False, False, True, None, False, False],
                [False, True, False, False, True, True, None, False],
                [False, False, False, True, False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False, True, True, True, False],
                [False, None, False, True, False, True, False, True],
                [True, True, None, True, False, False, True, False],
                [True, False, False, None, True, True, False, False],
                [False, True, True, False, None, True, True, False],
                [False, False, True, False, False, None, True, True],
                [False, True, False, True, False, False, None, True],
                [True, False, True, True, True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for triple '
                              'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test triple round-robin schedule generation."""
        scheduler = TripleRoundRobinScheduler(8)
        # Failed attempt
        random.seed(12)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(6, 5), (1, 7), (3, 4), (2, 8)],
                [(7, 5), (4, 3), (8, 6), (1, 2)],
                [(1, 8), (5, 3), (7, 2), (6, 4)],
                [(5, 8), (3, 1), (4, 6), (7, 2)],
                [(5, 4), (8, 6), (1, 2), (3, 7)],
                [(6, 7), (3, 8), (2, 5), (4, 1)],
                [(4, 3), (5, 1), (2, 7), (6, 8)],
                [(7, 4), (2, 3), (6, 5), (1, 8)],
                [(5, 8), (1, 3), (4, 7), (6, 2)],
                [(4, 5), (7, 6), (3, 8), (2, 1)],
                [(3, 5), (7, 1), (8, 2), (4, 6)],
                [(1, 4), (6, 3), (7, 5), (2, 8)],
                [(7, 8), (1, 5), (4, 2), (3, 6)],
                [(7, 3), (5, 2), (8, 4), (1, 6)],
                [(3, 7), (4, 8), (2, 6), (1, 5)],
                [(2, 4), (5, 7), (6, 1), (8, 3)],
                [(3, 2), (8, 5), (4, 1), (7, 6)],
                [(5, 4), (8, 7), (6, 1), (2, 3)],
                [(5, 3), (6, 2), (4, 7), (8, 1)],
                [(5, 6), (8, 7), (3, 1), (2, 4)],
                [(8, 4), (5, 2), (1, 7), (3, 6)]
            ]
        elif PY3:
            expected_schedule = [
                [(6, 5), (4, 3), (8, 1), (7, 2)],
                [(7, 4), (6, 2), (8, 5), (3, 1)],
                [(1, 5), (3, 2), (7, 4), (8, 6)],
                [(7, 8), (6, 4), (3, 5), (1, 2)],
                [(4, 7), (2, 8), (3, 1), (5, 6)],
                [(3, 6), (8, 7), (4, 5), (1, 2)],
                [(5, 7), (3, 4), (2, 6), (8, 1)],
                [(2, 4), (6, 3), (5, 7), (1, 8)],
                [(8, 2), (7, 1), (5, 3), (4, 6)],
                [(7, 3), (1, 5), (8, 4), (2, 6)],
                [(6, 8), (7, 2), (5, 4), (1, 3)],
                [(1, 7), (8, 5), (2, 3), (4, 6)],
                [(2, 7), (1, 6), (4, 5), (8, 3)],
                [(6, 7), (5, 2), (8, 3), (4, 1)],
                [(6, 3), (4, 8), (7, 5), (2, 1)],
                [(1, 4), (3, 7), (5, 6), (2, 8)],
                [(2, 4), (6, 1), (5, 8), (3, 7)],
                [(5, 3), (1, 6), (4, 2), (7, 8)],
                [(5, 2), (3, 4), (6, 8), (1, 7)],
                [(3, 2), (8, 4), (6, 7), (5, 1)],
                [(7, 6), (4, 1), (3, 8), (2, 5)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'triple round-robin competition'))

    def test_bypassed_schedule_generation(self):
        """Test bypassed triple round-robin schedule generation.

        This test uses RoundRobinScheduler directly, instead of
        TripleRoundRobinScheduler.
        """
        scheduler = RoundRobinScheduler(8, meetings=3)
        # Failed attempt
        random.seed(12)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(6, 5), (1, 7), (3, 4), (2, 8)],
                [(7, 5), (4, 3), (8, 6), (1, 2)],
                [(1, 8), (5, 3), (7, 2), (6, 4)],
                [(5, 8), (3, 1), (4, 6), (7, 2)],
                [(5, 4), (8, 6), (1, 2), (3, 7)],
                [(6, 7), (3, 8), (2, 5), (4, 1)],
                [(4, 3), (5, 1), (2, 7), (6, 8)],
                [(7, 4), (2, 3), (6, 5), (1, 8)],
                [(5, 8), (1, 3), (4, 7), (6, 2)],
                [(4, 5), (7, 6), (3, 8), (2, 1)],
                [(3, 5), (7, 1), (8, 2), (4, 6)],
                [(1, 4), (6, 3), (7, 5), (2, 8)],
                [(7, 8), (1, 5), (4, 2), (3, 6)],
                [(7, 3), (5, 2), (8, 4), (1, 6)],
                [(3, 7), (4, 8), (2, 6), (1, 5)],
                [(2, 4), (5, 7), (6, 1), (8, 3)],
                [(3, 2), (8, 5), (4, 1), (7, 6)],
                [(5, 4), (8, 7), (6, 1), (2, 3)],
                [(5, 3), (6, 2), (4, 7), (8, 1)],
                [(5, 6), (8, 7), (3, 1), (2, 4)],
                [(8, 4), (5, 2), (1, 7), (3, 6)]
            ]
        elif PY3:
            expected_schedule = [
                [(6, 5), (4, 3), (8, 1), (7, 2)],
                [(7, 4), (6, 2), (8, 5), (3, 1)],
                [(1, 5), (3, 2), (7, 4), (8, 6)],
                [(7, 8), (6, 4), (3, 5), (1, 2)],
                [(4, 7), (2, 8), (3, 1), (5, 6)],
                [(3, 6), (8, 7), (4, 5), (1, 2)],
                [(5, 7), (3, 4), (2, 6), (8, 1)],
                [(2, 4), (6, 3), (5, 7), (1, 8)],
                [(8, 2), (7, 1), (5, 3), (4, 6)],
                [(7, 3), (1, 5), (8, 4), (2, 6)],
                [(6, 8), (7, 2), (5, 4), (1, 3)],
                [(1, 7), (8, 5), (2, 3), (4, 6)],
                [(2, 7), (1, 6), (4, 5), (8, 3)],
                [(6, 7), (5, 2), (8, 3), (4, 1)],
                [(6, 3), (4, 8), (7, 5), (2, 1)],
                [(1, 4), (3, 7), (5, 6), (2, 8)],
                [(2, 4), (6, 1), (5, 8), (3, 7)],
                [(5, 3), (1, 6), (4, 2), (7, 8)],
                [(5, 2), (3, 4), (6, 8), (1, 7)],
                [(3, 2), (8, 4), (6, 7), (5, 1)],
                [(7, 6), (4, 1), (3, 8), (2, 5)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for bypassed '
                              'triple round-robin competition'))


class TestQuadrupleRoundRobin(TestCase):

    """Tests for quadruple round-robin scheduling."""

    def test_match_generation(self):
        """Test quadruple round-robin match generation."""
        # Four teams
        scheduler = QuadrupleRoundRobinScheduler(4)
        expected_matches = [
            (1, 2), (1, 3), (1, 4), (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 3), (2, 4), (2, 1), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 4), (3, 1), (3, 2), (3, 4),
            (4, 1), (4, 2), (4, 3), (4, 1), (4, 2), (4, 3)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quadruple '
                               'round-robin schedule with four teams.'))
        # Three teams
        scheduler = QuadrupleRoundRobinScheduler(3)
        expected_matches = [
            (1, 2), (1, 3), (1, None), (1, 2), (1, 3), (1, None),
            (2, 1), (2, 3), (2, None), (2, 1), (2, 3), (2, None),
            (3, 1), (3, 2), (3, None), (3, 1), (3, 2), (3, None),
            (None, 1), (None, 2), (None, 3), (None, 1), (None, 2), (None, 3)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quadruple '
                               'round-robin schedule with three teams.'))
        # Eight teams
        scheduler = QuadrupleRoundRobinScheduler(8)
        expected_matches = [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ]
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quadruple '
                               'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test quadruple round-robin schedule generation."""
        scheduler = QuadrupleRoundRobinScheduler(6)
        # Failed attempt
        random.seed(4)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(5, 2), (6, 1), (4, 3)],
                [(1, 2), (3, 5), (4, 6)],
                [(5, 6), (3, 1), (4, 2)],
                [(4, 6), (1, 5), (2, 3)],
                [(2, 6), (5, 3), (4, 1)],
                [(2, 5), (3, 4), (6, 1)],
                [(4, 5), (2, 1), (3, 6)],
                [(2, 4), (1, 3), (6, 5)],
                [(3, 5), (2, 4), (1, 6)],
                [(2, 5), (4, 1), (3, 6)],
                [(5, 1), (6, 4), (3, 2)],
                [(4, 2), (5, 3), (1, 6)],
                [(1, 2), (4, 5), (6, 3)],
                [(2, 6), (1, 5), (4, 3)],
                [(6, 2), (3, 4), (5, 1)],
                [(5, 6), (3, 2), (1, 4)],
                [(5, 4), (6, 3), (2, 1)],
                [(5, 4), (1, 3), (6, 2)],
                [(3, 1), (5, 2), (6, 4)],
                [(2, 3), (6, 5), (1, 4)]
            ]
        elif PY3:
            expected_schedule = [
                [(6, 2), (5, 4), (3, 1)],
                [(5, 3), (2, 4), (1, 6)],
                [(1, 4), (6, 2), (5, 3)],
                [(6, 5), (1, 3), (4, 2)],
                [(1, 6), (3, 4), (5, 2)],
                [(1, 2), (5, 4), (3, 6)],
                [(2, 1), (6, 4), (3, 5)],
                [(4, 6), (5, 1), (3, 2)],
                [(5, 2), (3, 1), (4, 6)],
                [(2, 4), (5, 6), (1, 3)],
                [(5, 1), (2, 6), (3, 4)],
                [(6, 1), (2, 3), (4, 5)],
                [(4, 3), (2, 1), (6, 5)],
                [(3, 5), (6, 1), (4, 2)],
                [(1, 5), (2, 3), (6, 4)],
                [(1, 2), (6, 3), (4, 5)],
                [(2, 5), (4, 1), (6, 3)],
                [(1, 4), (3, 6), (2, 5)],
                [(3, 2), (4, 1), (5, 6)],
                [(1, 5), (2, 6), (4, 3)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'quadruple round-robin competition'))

    def test_bypassed_schedule_generation(self):
        """Test bypassed quadruple round-robin schedule generation.

        This test uses RoundRobinScheduler directly, instead of
        QuadrupleRoundRobinScheduler.
        """
        scheduler = RoundRobinScheduler(6, meetings=4)
        # Failed attempt
        random.seed(4)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(5, 2), (6, 1), (4, 3)],
                [(1, 2), (3, 5), (4, 6)],
                [(5, 6), (3, 1), (4, 2)],
                [(4, 6), (1, 5), (2, 3)],
                [(2, 6), (5, 3), (4, 1)],
                [(2, 5), (3, 4), (6, 1)],
                [(4, 5), (2, 1), (3, 6)],
                [(2, 4), (1, 3), (6, 5)],
                [(3, 5), (2, 4), (1, 6)],
                [(2, 5), (4, 1), (3, 6)],
                [(5, 1), (6, 4), (3, 2)],
                [(4, 2), (5, 3), (1, 6)],
                [(1, 2), (4, 5), (6, 3)],
                [(2, 6), (1, 5), (4, 3)],
                [(6, 2), (3, 4), (5, 1)],
                [(5, 6), (3, 2), (1, 4)],
                [(5, 4), (6, 3), (2, 1)],
                [(5, 4), (1, 3), (6, 2)],
                [(3, 1), (5, 2), (6, 4)],
                [(2, 3), (6, 5), (1, 4)]
            ]
        elif PY3:
            expected_schedule = [
                [(6, 2), (5, 4), (3, 1)],
                [(5, 3), (2, 4), (1, 6)],
                [(1, 4), (6, 2), (5, 3)],
                [(6, 5), (1, 3), (4, 2)],
                [(1, 6), (3, 4), (5, 2)],
                [(1, 2), (5, 4), (3, 6)],
                [(2, 1), (6, 4), (3, 5)],
                [(4, 6), (5, 1), (3, 2)],
                [(5, 2), (3, 1), (4, 6)],
                [(2, 4), (5, 6), (1, 3)],
                [(5, 1), (2, 6), (3, 4)],
                [(6, 1), (2, 3), (4, 5)],
                [(4, 3), (2, 1), (6, 5)],
                [(3, 5), (6, 1), (4, 2)],
                [(1, 5), (2, 3), (6, 4)],
                [(1, 2), (6, 3), (4, 5)],
                [(2, 5), (4, 1), (6, 3)],
                [(1, 4), (3, 6), (2, 5)],
                [(3, 2), (4, 1), (5, 6)],
                [(1, 5), (2, 6), (4, 3)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for bypassed '
                              'quadruple round-robin competition'))


class TestQuintupleRoundRobin(TestCase):

    """Tests for quintuple round-robin scheduling."""

    def test_match_generation(self):
        """Test quintuple round-robin match generation."""
        # Four teams
        random.seed(1)
        scheduler = RoundRobinScheduler(4, meetings=5)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (1, 4),
                (2, 3), (4, 2), (3, 4)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1),
                (2, 3), (2, 4), (3, 4)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 4),
            (4, 1), (4, 2), (4, 3)
        ] * 2)
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quintuple '
                               'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = RoundRobinScheduler(3, meetings=5)
        if PY2:
            expected_matches = [
                (2, 1), (1, 3), (3, 2),
                (1, None), (None, 2), (None, 3)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (2, 3),
                (1, None), (None, 2), (None, 3)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, None),
            (2, 1), (2, 3), (2, None),
            (3, 1), (3, 2), (3, None),
            (None, 1), (None, 2), (None, 3)
        ] * 2)
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quintuple '
                               'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = RoundRobinScheduler(8, meetings=5)
        if PY2:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (6, 1), (1, 7), (1, 8),
                (2, 3), (2, 4), (5, 2), (6, 2), (7, 2), (2, 8),
                (4, 3), (5, 3), (3, 6), (3, 7), (3, 8),
                (5, 4), (4, 6), (4, 7), (8, 4),
                (6, 5), (7, 5), (5, 8),
                (7, 6), (8, 6),
                (8, 7)
            ]
        elif PY3:
            expected_matches = [
                (1, 2), (3, 1), (4, 1), (1, 5), (1, 6), (1, 7), (8, 1),
                (3, 2), (2, 4), (5, 2), (2, 6), (7, 2), (2, 8),
                (3, 4), (5, 3), (6, 3), (3, 7), (8, 3),
                (4, 5), (4, 6), (7, 4), (8, 4),
                (5, 6), (5, 7), (8, 5),
                (6, 7), (6, 8),
                (7, 8)
            ]
        expected_matches.extend([
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ] * 2)
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for quintuple '
                               'round-robin schedule with eight teams.'))

    def test_matrix_generation(self):
        """Test quintuple round-robin matrix generation."""
        # Four teams
        random.seed(1)
        scheduler = RoundRobinScheduler(4, meetings=5)
        if PY2:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, True],
                [False, True, False, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False],
                [False, None, True, True],
                [True, False, None, True],
                [True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for quintuple '
                              'round-robin schedule with four teams.'))
        # Three teams
        random.seed(1)
        scheduler = RoundRobinScheduler(3, meetings=5)
        if PY2:
            expected_matrix = [
                [None, False, True, True],
                [True, None, False, False],
                [False, True, None, False],
                [False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, True],
                [False, None, True, False],
                [True, False, None, False],
                [False, True, True, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for quintuple '
                              'round-robin schedule with three teams.'))
        # Eight teams
        random.seed(1)
        scheduler = RoundRobinScheduler(8, meetings=5)
        if PY2:
            expected_matrix = [
                [None, True, False, False, True, False, True, True],
                [False, None, True, True, False, False, False, True],
                [True, False, None, False, False, True, True, True],
                [True, False, True, None, False, True, True, False],
                [False, True, True, True, None, False, False, True],
                [True, True, False, False, True, None, False, False],
                [False, True, False, False, True, True, None, False],
                [False, False, False, True, False, True, True, None]
            ]
        elif PY3:
            expected_matrix = [
                [None, True, False, False, True, True, True, False],
                [False, None, False, True, False, True, False, True],
                [True, True, None, True, False, False, True, False],
                [True, False, False, None, True, True, False, False],
                [False, True, True, False, None, True, True, False],
                [False, False, True, False, False, None, True, True],
                [False, True, False, True, False, False, None, True],
                [True, False, True, True, True, False, False, None]
            ]
        matrix = scheduler.generate_matrix()
        self.assertListEqual(expected_matrix, matrix,
                             ('Incorrect matrix generated for quintuple '
                              'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test quintuple round-robin schedule generation."""
        scheduler = RoundRobinScheduler(6, meetings=5)
        # Failed attempt
        random.seed(8)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(5, 2), (4, 1), (3, 6)],
                [(2, 1), (4, 3), (5, 6)],
                [(2, 5), (6, 3), (1, 4)],
                [(3, 5), (6, 4), (2, 1)],
                [(3, 6), (4, 1), (2, 5)],
                [(4, 2), (3, 1), (6, 5)],
                [(3, 4), (5, 6), (2, 1)],
                [(3, 5), (2, 6), (4, 1)],
                [(6, 3), (2, 4), (5, 1)],
                [(3, 2), (5, 1), (6, 4)],
                [(1, 6), (5, 4), (2, 3)],
                [(5, 3), (2, 6), (1, 4)],
                [(4, 3), (1, 2), (5, 6)],
                [(6, 1), (2, 3), (4, 5)],
                [(3, 6), (4, 2), (1, 5)],
                [(5, 2), (1, 6), (3, 4)],
                [(4, 6), (3, 1), (2, 5)],
                [(6, 2), (5, 4), (1, 3)],
                [(6, 2), (1, 3), (4, 5)],
                [(1, 5), (4, 3), (6, 2)],
                [(5, 3), (6, 1), (2, 4)],
                [(3, 2), (1, 6), (5, 4)],
                [(1, 5), (3, 2), (6, 4)],
                [(5, 3), (1, 2), (4, 6)],
                [(1, 3), (4, 2), (6, 5)]
            ]
        elif PY3:
            expected_schedule = [
                [(4, 6), (2, 5), (3, 1)],
                [(3, 4), (2, 5), (6, 1)],
                [(5, 1), (4, 3), (2, 6)],
                [(3, 6), (4, 5), (2, 1)],
                [(6, 4), (5, 3), (2, 1)],
                [(2, 4), (1, 3), (5, 6)],
                [(2, 3), (4, 1), (6, 5)],
                [(2, 5), (1, 4), (6, 3)],
                [(6, 4), (2, 3), (5, 1)],
                [(3, 1), (4, 2), (6, 5)],
                [(6, 1), (4, 5), (3, 2)],
                [(3, 2), (1, 5), (4, 6)],
                [(6, 2), (1, 4), (5, 3)],
                [(6, 1), (4, 3), (5, 2)],
                [(5, 4), (1, 2), (6, 3)],
                [(4, 6), (3, 2), (5, 1)],
                [(5, 6), (3, 4), (1, 2)],
                [(2, 4), (6, 3), (1, 5)],
                [(1, 6), (3, 4), (5, 2)],
                [(6, 2), (1, 4), (3, 5)],
                [(2, 4), (1, 6), (5, 3)],
                [(5, 4), (1, 3), (2, 6)],
                [(1, 2), (3, 6), (4, 5)],
                [(3, 5), (2, 6), (4, 1)],
                [(4, 2), (1, 3), (5, 6)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'quintuple round-robin competition'))


class TestSextupleRoundRobin(TestCase):

    """Tests for sextuple round-robin scheduling."""

    def test_match_generation(self):
        """Test sextuple round-robin match generation."""
        # Four teams
        scheduler = RoundRobinScheduler(4, meetings=6)
        expected_matches = [
            (1, 2), (1, 3), (1, 4),
            (2, 1), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 4),
            (4, 1), (4, 2), (4, 3),
        ] * 3
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for sextuple '
                               'round-robin schedule with four teams.'))
        # Three teams
        scheduler = RoundRobinScheduler(3, meetings=6)
        expected_matches = [
            (1, 2), (1, 3), (1, None),
            (2, 1), (2, 3), (2, None),
            (3, 1), (3, 2), (3, None),
            (None, 1), (None, 2), (None, 3),
        ] * 3
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for sextuple '
                               'round-robin schedule with three teams.'))
        # Eight teams
        scheduler = RoundRobinScheduler(8, meetings=6)
        expected_matches = [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ] * 3
        matches = scheduler.generate_matches()
        self.assertCountEqual(expected_matches, matches,
                              ('Incorrect matches generated for sextuple '
                               'round-robin schedule with eight teams.'))

    def test_schedule_generation(self):
        """Test sextuple round-robin schedule generation."""
        scheduler = RoundRobinScheduler(6, meetings=6)
        # Failed attempt
        random.seed(35)
        self.assertRaises(ScheduleGenerationFailed,
                          scheduler.generate_schedule, try_once=True)
        # Successful attempt
        random.seed(1)
        if PY2:
            expected_schedule = [
                [(6, 4), (3, 1), (2, 5)],
                [(3, 1), (6, 5), (4, 2)],
                [(6, 1), (2, 3), (5, 4)],
                [(5, 1), (2, 6), (3, 4)],
                [(1, 6), (2, 5), (3, 4)],
                [(5, 6), (4, 3), (2, 1)],
                [(2, 6), (3, 5), (4, 1)],
                [(3, 1), (2, 5), (4, 6)],
                [(1, 4), (3, 5), (6, 2)],
                [(1, 2), (5, 4), (6, 3)],
                [(5, 2), (6, 4), (1, 3)],
                [(1, 3), (4, 2), (6, 5)],
                [(5, 3), (2, 6), (4, 1)],
                [(5, 1), (4, 6), (3, 2)],
                [(3, 2), (1, 6), (4, 5)],
                [(1, 3), (4, 6), (5, 2)],
                [(3, 6), (4, 5), (2, 1)],
                [(2, 3), (4, 5), (1, 6)],
                [(1, 2), (5, 3), (6, 4)],
                [(4, 1), (3, 2), (6, 5)],
                [(1, 4), (6, 3), (5, 2)],
                [(1, 5), (3, 6), (4, 2)],
                [(5, 1), (2, 4), (6, 3)],
                [(1, 2), (3, 6), (5, 4)],
                [(5, 6), (1, 4), (2, 3)],
                [(5, 3), (6, 1), (2, 4)],
                [(4, 3), (1, 5), (6, 2)],
                [(2, 1), (3, 4), (5, 6)],
                [(6, 1), (2, 4), (3, 5)],
                [(1, 5), (6, 2), (4, 3)]
            ]
        elif PY3:
            expected_schedule = [
                [(6, 4), (2, 3), (5, 1)],
                [(4, 5), (1, 2), (3, 6)],
                [(3, 4), (1, 2), (6, 5)],
                [(2, 6), (5, 3), (4, 1)],
                [(6, 3), (1, 5), (2, 4)],
                [(5, 6), (3, 2), (1, 4)],
                [(6, 1), (4, 2), (5, 3)],
                [(1, 3), (6, 4), (5, 2)],
                [(5, 1), (3, 4), (6, 2)],
                [(4, 1), (5, 6), (3, 2)],
                [(4, 5), (6, 1), (2, 3)],
                [(2, 1), (5, 4), (3, 6)],
                [(6, 2), (4, 5), (3, 1)],
                [(1, 5), (2, 4), (3, 6)],
                [(2, 6), (1, 5), (4, 3)],
                [(4, 6), (2, 1), (5, 3)],
                [(3, 1), (2, 5), (6, 4)],
                [(1, 6), (4, 2), (3, 5)],
                [(6, 1), (2, 3), (5, 4)],
                [(1, 4), (6, 2), (3, 5)],
                [(5, 2), (1, 4), (6, 3)],
                [(5, 6), (2, 4), (3, 1)],
                [(3, 4), (6, 5), (1, 2)],
                [(2, 5), (4, 1), (6, 3)],
                [(4, 3), (5, 1), (2, 6)],
                [(2, 5), (4, 6), (1, 3)],
                [(1, 3), (5, 2), (4, 6)],
                [(1, 6), (5, 4), (3, 2)],
                [(2, 1), (4, 3), (6, 5)],
                [(3, 5), (1, 6), (4, 2)]
            ]
        schedule = scheduler.generate_schedule(try_once=True)
        self.assertListEqual(expected_schedule, schedule,
                             ('Wrong schedule created for '
                              'sextuple round-robin competition'))
