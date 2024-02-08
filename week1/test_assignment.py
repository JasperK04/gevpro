import os
import re
import sys
import json
import pytest

STUDENT_NUMBER_PATTERN = re.compile(r's\d{7}$')


def test_python_version():
    assert sys.version_info[0] == 3, (
        'You must use Python 3. Reinstall pytest or try: '
        'python3 -m pytest')
    assert sys.version_info[1] >= 6, (
        'You must use Python 3.6 or higher. Upgrade Python.')


class TestJSON:
    @pytest.fixture
    def data(self):
        """A special function to provide the data used in each test case with
        an argument named `data`. A new copy is created each time."""
        with open('me.json') as f:
            return json.load(f)

    def test_name(self, data):
        # each assert statement is a single test case with an optional message:
        # assert <condition>, 'message when test fails'
        assert 'Name' in data, 'Name property is missing'
        assert isinstance(data['Name'], str), 'Value for Name is not a string'
        assert data['Name'].strip(), 'Value for Name is empty'

    def test_student_number(self, data):
        assert 'Student number' in data, 'Student number property is missing'
        assert isinstance(data['Student number'], str), (
            'Value for Student number is not a string')
        match = STUDENT_NUMBER_PATTERN.match(data['Student number'])
        assert match, ('Value for Student number must be a lower-case s '
                       'followed by seven digits')

    def test_workgroup(self, data):
        assert 'Workgroup' in data, 'Workgroup property is missing'
        assert isinstance(data['Workgroup'], int), (
            'Value for Workgroup must be an integer')
        assert data['Workgroup'] in (1, 2), (
            'Value for Workgroup must be 1 or 2')


class TestImage:
    def test_image(self):
        assert (os.path.isfile('me.jpg')
                or os.path.isfile('me.png')
                or os.path.isfile('me.gif')), (
            'No image me.jpg, me.png or me.gif found')


class TestText:
    def test_text(self):
        assert os.path.isfile('me.txt'), 'No file me.txt found'
        with open('me.txt') as f:
            text = f.read()
        assert text.strip(), 'me.txt is empty'
