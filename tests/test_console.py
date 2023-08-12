#!/usr/bin/python3
"""This module defines unit tests for the HBNBCommand class."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test_HBNBCommand(unittest.TestCase):
    """Test class for the command line interface"""

    def test_prompt(self):
        """Test if prompt is set to '(hbnb) '."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
        # to do a test that the prompt is "hbnb " when called from main

    def test_create(self):
        """Test create method."""
        input = "create"
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output, output)

        input = "create invalidClass"
        expected_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output, output)

        input = "create BaseModel"
        expected_regex = "........-....-....-....-............"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input)
            output = fakeOutput.getvalue().strip()
            self.assertRegex(output, expected_regex)

        # TO DO: check that instance is saved in the dict

    def test_exit(self):
        """Test exit functionality of cli."""
        input = "quit"
        expected_output = True
        result = HBNBCommand().onecmd(input)
        self.assertEqual(result, expected_output)

        with patch("builtins.input", side_effect=["quit"]):
            self.assertTrue(HBNBCommand().onecmd("quit"))

        input = "EOF"
        expected_output = True
        result = HBNBCommand().onecmd(input)
        self.assertEqual(result, expected_output)

        with patch("builtins.print") as mock_print:
            with patch("builtins.input", side_effect=["EOF"]):
                self.assertTrue(HBNBCommand().onecmd("EOF"))
            mock_print.assert_called_with()

        # To do: test that the cli exits

    def test_empty_line(self):
        """Test empty lines are ignored by parser and not printed on stdout."""
        input = "   \n\t  \r\n     \n\t  \
        \r\n"
        expected_output = ""
        with patch("sys.stdout", new=StringIO()) as fakeOut:
            HBNBCommand().onecmd(input)
            output = fakeOut.getvalue().strip("\n")
            self.assertEqual(expected_output, output)

        with patch("builtins.print") as mock_print:
            cmd = HBNBCommand()
            cmd.emptyline()
            mock_print.assert_not_called()

    def test_show(self):
        """Test show command."""

        input1 = "show"
        expected_output1 = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input1)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input2 = "show InvalidClass"
        expected_output1 = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input2)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input3 = "show BaseModel"
        expected_output1 = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input3)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input4 = "show BaseModel InvalidId"
        expected_output1 = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input4)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        """ input5 = "show Basemodel "
        expected_output1 = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)"""
        # to implement show with a real instance above

    def test_destroy(self):
        """Test destroy command."""

        input1 = "destroy"
        expected_output1 = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input1)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input2 = "destroy InvalidClass"
        expected_output1 = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input2)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input3 = "destroy BaseModel"
        expected_output1 = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input3)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input4 = "destroy BaseModel InvalidId"
        expected_output1 = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input4)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)
        # to do destroy the actual instance

    def test_all(self):
        """Test all command."""
        input2 = "all InvalidClass"
        expected_output1 = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input2)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        # to do for actual all

    def test_count(self):
        """Test count command."""
        input1 = "count"
        expected_output1 = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input1)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input2 = "count InvalidClass"
        expected_output1 = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input2)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

    def test_update(self):
        """Test update command."""
        input1 = "update"
        expected_output1 = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input1)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input2 = "update InvalidClass"
        expected_output1 = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input2)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input3 = "update BaseModel"
        expected_output1 = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input3)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input4 = "update BaseModel InvalidId"
        expected_output1 = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input4)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        """input5 = "update BaseModel"
        expected_output1 = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input3)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)

        input6 = "update BaseModel"
        expected_output1 = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            HBNBCommand().onecmd(input3)
            output = fakeOutput.getvalue().strip()
            self.assertEqual(expected_output1, output)"""

    def test_default(self):
        """Test default command."""
        input1 = "InvalidInput"
        expected_output1 = "** Unknown syntax: {}".format(input1)
        with patch("sys.stdout", new=StringIO()) as fakeError:
            HBNBCommand().onecmd(input1)
            error = fakeError.getvalue().strip()
            self.assertEqual(error, expected_output1)
