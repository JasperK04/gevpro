Assignment for Week 1
=====================

In this assignment you will practice working with Git, unit tests, code style, and Markdown.

*Read the instructions VERY carefully, there are a number of details you MUST
get right in order to receive points.*

Step 1: Create your repository
------------------------------
We will use Git to get your assignment solutions from you to us. For this,
you will need your own private repository on some server.

There are a number of online services for hosting Git repositories. We will use
[Github](https://github.com/) which is the most popular.

If you do not have a Github account yet, create one.
In the top right menu, click the "+" and choose the *New repository* option;
enter "gevpro" as repository name and select *private repository*;
also enable "Add a README file".

Clone your new repository to your computer:

    $ git clone https://github.com/YOUR_USERNAME/gevpro.git

Unzip files for the assignment into the new repository:

    $ cd gevpro
    $ unzip week1.zip

Before you make any changes, commit the original version of the assignment files:

    $ git add week1
    $ git commit -m 'original assignment'


Step 2: Installing packages
---------------------------
Install the required packages for the assignments:

    $ pip3 install --user --upgrade pytest pycodestyle

If you don't have pip3, install it as follows (assuming you use Ubuntu):

	$ sudo add-apt-repository universe
	$ sudo apt update
	$ sudo apt install python3-pip

"pip3 install --user" places commands in the directory ~/.local/bin/
You need to add this directory to the search path:

    $ echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
    $ source .bashrc

On new Mac OS X versions (Catalina and later), you should use .zshrc instead of .bashrc

Step 3: Watch the tests fail
----------------------------
On the command line, change into the `week1` directory.
Run the unit tests:
    
    $ cd week1
    $ pytest

You should see the output from Python running a number of tests, and they all
fail. Your task will be to satisfy the requirements checked by the tests until
they all succeed.

Step 4: Satisfy the requirements
--------------------------------
`me.json` is a file in JSON format where you should leave some basic data about
yourself. Specifically, fill in your name and workgroup for this course. Also
add a third property `"Student number" `to the JSON file, with your student
number as value.

Put an image file called `me.jpg`, `me.png` or `me.gif` into the same
directory. This could be a photo of your face; this would help us
memorize your name (and remember, it will not be public). However, if you would
rather not submit a picture of yourself, that is also fine. In that case, use
a picture of your favorite animal.

Finally, add a text file called `me.txt` with a short introduction of yourself,
or a life motto, or a favorite quotation -- again, this is intended to help us
get to know you a bit.

Run the tests again. If some tests still fail, the messages should give you a
good idea of what is wrong. Fix that and try again until all tests succeed.

Step 5: Add test cases
----------------------
Notice that there are no unit tests for the `pets.py` program. The best
practice with unit testing is to aim for 100% test coverage; this means that
there is a test for all functions. Add tests to `test_assignment.py` to test
the behavior of the `pets` module. Ensure that these tests pass.


Step 6: Apply the style guide
-----------------------------
The directory contains a small Python program `pets.py`. It does not conform to
the [PEP 0008](https://www.python.org/dev/peps/pep-0008/) style guide. Use the
[pycodestyle](https://pypi.python.org/pypi/pycodestyle) command-line tool to
style-check the file. Modify `pets.py` so that `pycodestyle` runs without
complaints. Also ensure that `test_assignment.py` has no style issues.

Note: good coding style is more than making an automatic style checker
succeed. For example, you need to use clear variable names, write clear
comments where appropriate. Sometimes good style even involves breaking the
conventions, as explained in the beginning of PEP-0008. However, for this
course, always ensure that `pycodestyle` gives 0 warnings or errors
on your code.

Step 7: re-write README.md
--------------------------
The md in `README.md` stands for Markdown, which Github uses to display
a formatted text. The syntax of Markdown is described here:

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Open `README.md` in an editor and remove everything.
Add the following information:

1. the text from `me.txt` and the image `me.jpg` (or .png)
2. show how the run the tests and check the code style (format as code)
3. add a list with links to your three favorite Wikipedia pages

For each of the above items, add an appropriate heading

Step 8: Commit and Submit your work
-----------------------------------
You could add all changes to a single commit, but for full points, make a separate
commit for step 4, 5, 6, and 7; each with its own descriptive commit message (1 sentence is enough).

Stage your changes using the `git add` command. Don't forget to add *both*
the files you modified *and* the new files you added. Double-check with
`git status` that the right files are staged for commit; in addition, check
that no untracked files are left, and that you didn't add any files that
shouldn't be part of the repository. With `git diff --staged` you can review
the code that has been staged for commit.

Commit your changes using `git commit` and a suitable message.

Finally and crucially, *push* your commit to your private repository on
Github:

    $ git push

Go to https://github.com/USERNAME/gevpro/ (change `USERNAME` to your
Github username) to verify your commits have arrived, and that your README.md
looks good. *Double-check that all the changes and new files are there. If not,
we will not be able to see them and you will not receive points.* If something
is missing, you may have forgotten to add, commit or push. Use `git status` to
find out what is out of sync and repeat the necessary steps.

In order for your homework to be graded, you have to provide access to your
private repository. Click on *Settings* and then click on "Collaborators".
Add the usernames of the teacher and student assistant of this course:

- andreasvc (Andreas van Cranenburgh)
- topje (Jelmer Top)

Finally, *submit via Brightspace*. All you need to submit is the URL of your private
Github repository.
Important: Without this step, your work will not be graded!
Since this week's assignment is relatively easy, it will only contribute 10% of
the weighted average of the 4 homework assignments.
