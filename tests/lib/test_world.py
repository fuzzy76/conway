import unittest
from lib.world import World, WorldBoundariesError

class TestWorld(unittest.TestCase):
    """
    Welcome to the test class for Conway's Game Of Life.

    The test cases that are layed out here are optional, but
    might make it easier to get started. It's recommended
    to start from top to bottom as the last test cases require more
    complete implementation. Try figure out WHAT you wish to test
    before figuring out implementation.

    The basic idea here:

    1) WRITE TEST CASE.
    2) WRITE IMPLEMENTATION.
    3) RUN TEST.
    4) GOTO 1.

    The target class (test subject) where we'll implement the expected code in
    should exist in the ./lib/ folder, whereas this file expects to
    live in ./tests/lib/ folder. Run your tests from "." (root
    of project folder).

    Read more about the unittest module by visiting:
    https://docs.python.org/3.5/library/unittest.html
    """

    def setUp(self):
        """
        The "setUp" method runs before every test,
        usefull for initializing test subjects.
        """
        self.world = World()

    def test_canary_test(self):
        """
        The canary test is nice for testing if unit tests executes correctly.

        Run all tests:
        $ python -m unittest discover
        """
        self.assertTrue(True)
        self.assertIsInstance(self.world, World)

    def test_world_is_x_width(self):
        """
        Implement the constructor in World class so
        the class gets its property then remove the decorator.

        You can test this specific test alone by running:
        $ python -m unittest tests.lib.test_world.TestWorld.test_world_is_x_width
        """
        self.assertEqual(self.world.x_width, 50, "World width not 50")

    def test_world_is_y_heigth(self):
        self.assertEqual(self.world.y_height, 50, "World height not 50")

    def test_world_has_set_for_live_cells(self):
        self.assertIsInstance(self.world.live_cells, set, 'Live cells set missing')

    def test_world_supports_setting_initial_set_of_live_cells(self):
        world = World(live_cells = set([(1,2), (3,4)]))
        self.assertEqual(len(world.live_cells), 2, "Wrong number of cells")
        myset = set([(1,2), (3,4)])
        self.assertEqual(world.live_cells, myset, "Cells not equal")

    def test_autopopulate_world(self):
        self.world.autopopulate()
        self.assertEqual(len(self.world.live_cells), 25, "Not autopopulated")

    def test_world_can_be_erased(self):
        self.world.autopopulate()
        self.world.clearcells()
        self.assertEqual(len(self.world.live_cells), 0, "Not cleared")

    def test_add_single_cell_to_the_world(self):
        self.world.addcell(5,5)
        self.assertIn((5,5), self.world.live_cells)

    def test_add_single_cell_outside_world_bounderies_should_fail(self):
        with self.assertRaises(WorldBoundariesError):
            self.world.addcell(-2,-2)
        with self.assertRaises(WorldBoundariesError):
            self.world.addcell(999,999)

    def test_world_can_check_if_cell_coordinate_is_legal(self):
        self.assertTrue(self.world.checkpos(2,3))
        self.assertIsInstance(self.world.checkpos(-2,-3), str)
        self.assertIsInstance(self.world.checkpos(999,999), str)

    def test_world_can_count_neighbors_of_a_cell(self):
        self.world.clearcells()
        self.world.addcell(5,5)
        self.world.addcell(6,5)
        self.world.addcell(5,6)
        self.assertEqual(self.world.countneighbours(6,6), 3)
        self.assertEqual(self.world.countneighbours(5,5), 2)
        self.assertEqual(self.world.countneighbours(5,7), 1)
        self.assertEqual(self.world.countneighbours(7,7), 0)

    def test_world_correctly_count_neighbors_even_at_edge_of_map(self):
        self.world.clearcells()
        self.world.addcell(0,0)
        self.assertEqual(self.world.countneighbours(49,49), 1)
        self.world.clearcells()
        self.world.addcell(49,49)
        self.assertEqual(self.world.countneighbours(0,0), 1)

    def test_world_generate_new_population_glider_pattern(self):
        """
        Glider is a famous game of life pattern.

        .O
        ..O => O.O
        OOO    .OO
               .O

        http://www.conwaylife.com/wiki/Glider
        """
        glider_step_one = set([
            (5, 5),
            (6, 6),
            (4, 7),
            (5, 7),
            (6, 7)
            ])
        glider_step_two = set([
            (4, 6),
            (6, 6),
            (5, 7),
            (6, 7),
            (5, 8)
            ])
        self.world.live_cells = glider_step_one
        self.world.generate_new_generation()
        self.assertEqual(self.world.live_cells, glider_step_two, "New population didn't match expected pattern")

    def test_world_generate_new_population_claw_with_tail(self):
        """
        Claw with tail is a still life pattern that doesn't change.

        OO        OO
        .O        .O
        .O.OO  => .O.OO
        ..O..O    ..O..O
        ....OO    ....OO

        http://www.conwaylife.com/wiki/Claw_with_tail
        """
        claw_step_one = set([
            (2,2),
            (3,2),
            (3,3),
            (3,4),
            (5,4),
            (6,4),
            (4,5),
            (7,5),
            (6,6),
            (7,6)
            ])
        claw_step_two = set([
            (2,2),
            (3,2),
            (3,3),
            (3,4),
            (5,4),
            (6,4),
            (4,5),
            (7,5),
            (6,6),
            (7,6)
            ])
        self.world.live_cells = claw_step_one
        self.world.generate_new_generation()
        self.assertEqual(self.world.live_cells, claw_step_two, "New population didn't match expected pattern")
