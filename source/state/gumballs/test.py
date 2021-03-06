import unittest

from design_patterns.source.python.state.gumballs.gumball_machine import GumballMachine


class TestNewGumballMachine(unittest.TestCase):

    def test__new_machine__with_zero_count_balls__has_zero_count(self):
        machine = GumballMachine(0)

        self.assertEqual(0, machine.count)

    def test__new_machine__with_zero_count_balls__has_state_SOLD_OUT(self):
        machine = GumballMachine(0)

        self.assertEqual(GumballMachine.SOLD_OUT, machine.state)

    def test__new_machine__with_one_ball__has_state_NO_QUARTER(self):
        machine = GumballMachine(1)

        self.assertEqual(GumballMachine.NO_QUARTER, machine.state)


class TestGumballMachineInsertQuarter(unittest.TestCase):

    def test__NO_QUARTER__to__HAS_QUARTER(self):
        machine = GumballMachine(1)

        self.assertEqual(GumballMachine.NO_QUARTER, machine.state)

        machine.insert_quarter()

        self.assertEqual(GumballMachine.HAS_QUARTER, machine.state)

    def test__HAS_QUARTER__to__HAS_QUARTER(self):
        machine = GumballMachine(1)
        machine.insert_quarter()

        self.assertEqual(GumballMachine.HAS_QUARTER, machine.state)

        machine.insert_quarter()

        self.assertEqual(GumballMachine.HAS_QUARTER, machine.state)

    def test__(self):
        pass
        # SOLD_OUT


class TestGumballMachineEjectQuarter(unittest.TestCase):

    def test__HAS_QUARTER__to__NO_QUARTER(self):
        machine = GumballMachine(1)
        machine.insert_quarter()

        machine.eject_quarter()

        self.assertEqual(GumballMachine.NO_QUARTER, machine.state)

    def test__NO_QUARTER__NO_QUARTER(self):
        machine = GumballMachine(1)

        self.assertEqual(GumballMachine.NO_QUARTER, machine.state)

    # SOLD_OUT
    # SOLD


class TestGumballMachineTurnCrank(unittest.TestCase):

    def test__take_last_one_gumball(self):
        machine = GumballMachine(1)
        machine.insert_quarter()

        machine.turn_crank()

        self.assertEqual(GumballMachine.SOLD_OUT, machine.state)
        self.assertEqual(0, machine.count)

    def test__ready_to_another_turn(self):
        machine = GumballMachine(2)
        machine.insert_quarter()

        machine.turn_crank()

        self.assertEqual(GumballMachine.NO_QUARTER, machine.state)
        self.assertEqual(1, machine.count)
