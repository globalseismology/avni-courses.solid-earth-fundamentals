# GEO 203: Fundamentals of Solid Earth Science

## Guidelines and expectations from Instructional Staff

GEO203 is meant to be an introductory course in **solid** Earth geosciences. The sections below document the various procedures and workflows expected from 
the staff involved in delivering this course. If you have any questions or concerns, please do not assume anything, and simply e-mail the instructor of the course.

----

Table of Contents
-----------------

  1. [Pedagogy](#pedagogy)
    * [Layout of responsibilities](#layout-of-responsibilities)
    * [Grading and Honor Code](#grading-and-honor-code)
    * [Folders](#folders)
    * [Workflow](#workflow)
    * [Editing on Github](#editing-on-github)
    
  2. [Document your work](#document-your-work)
    * [Coding style](#coding-style)
  	* [Python](#python-formatting)

Pedagogy
--------

There are 4 teaching and evaluation components in this course - lectures, precepts, field trips, and problem sets. The instructor
is in charge of coordinating with others to make sure the content is as cohesive as feasible. This course is a smorgasbord of topics so this a challenging 
task. All staff are expected to coordinate with each other and discuss details with the instructor so that all components work together and topics are
tackled in a logical fashion.

Layout of responsibilities
--------------------------

All staff will coordinate with the instructor before posting content on Canvas. The TA's are responsible for running the precepts, preparing the related problem sheet in Jupyter 
Notebook in consultation with the instructor using the resources available from the Geosciences lab manager (e.g. samples, microscope) and other divisions at Princeton. The TA's are expected to assimilate information from various sources when preparing the final Jupyter Notebook. This includes but is not limited to revising questions based on the feedback and training provided to them. No major content development is expected from the TA's but working professionally to deliver a final product under the supervision of the instructor is. Professional and respectful conduct also includes being pro-active about grading on time and helping the lab manager setup the precept room whenever applicable.
TA's are expected to answer questions
from students through e-mail, during office hours or at other times by appointment, if available.

Grading and Honor Code
-------

The TA's are responsible for preparing a key for their problem set (i.e. suffix *-Key.ipynb*), and creating a grading rubric that informs the marking scheme on Gradescope. The grading should be done in a fair and consistent fashion. **Please feel free to grade but do NOT publish scores on Canvas without coordinating with the lab manager *and* the instructor**. With students, only discuss the broad themes of what was expected discussing their scores on graded content, and refrain from making comments about the fairness of the evaluation. If they have additional issues and want their answer re-evaluated for (partial or full) credit, they should request this in writing (i.e. by e-mailing the instructor).

If similar mistakes or responses are found between/across various submissions, the grader must make a list of the students involved and **inform the instructor immediately**. Students at Princeton must follow the *honor code* specified in the links below and exam times are not proctored, but with great power, comes great responsibility. **Please do not confront the student(s) about suspected violations**. Better that students learn the lessons of integrity when the stakes are smaller; no infraction is therefore too small to be reported to the instructor! 

More guidance on the *honor code* can be found in the University’s [Rights, Rules, and Responsibilities](https://rrr.princeton.edu/) as well as in the University’s booklet [Academic Integrity at Princeton](https://odoc.princeton.edu/sites/odoc/files/950045_AcademicIntegrity2018-19_FINAL_PDF.pdf). We will refer any suspected infractions of the honor code to the Faculty-Student Committee on Discipline or the Honor Committee, in accordance with the University policy.

Folders
-------

There are three locations where files are kept:

 1. [Course Dropbox Directory](https://www.dropbox.com/sh/qxoqmnwdo66uhph/AADnfvFriiPj2DslMsbuDgBLa?dl=0): This folder contains copies of presentations 
 and other ancillary material for the course. Please do not use this for storing material relevant to the problem sets.
 
 2. [Our working Github repository](https://github.com/pmoulik/GEO203_Fall2022_PSETS/tree/devel): We will be working on the devel branch of this repository. Github is good for browsing files and even 
  uploading/editing simple files directly from the browser without opening an Adroit session (. There is a branch called *main* that is synched with
  the Princeton repository. You have **read access to main branch** and **read/write access to devel branch**. 

 3. [Princeton Github repository](https://github.com/PrincetonUniversity/GEO203_Fall2022_PSETS): This is the downstream production version of all problem sets and exercises. 
     You and the students **only have read** access to this repository. This is also what the students have access to through Adroit.

Workflow
--------

As part of this course, you will have to work with a team. This means that version control of various (sets of) documents becomes critical so that we do not
work across purposes and can revert back to a stable version of a (set of) files whenever needed. Please clone the folders 2 and 3 onto Adroit through the commands line
and add suffixes *_pmoulik* and *_Princeton* to the folders. During Precepts, only work with the *_Princeton* folder to be in sync with the students.

The pipeline for precepts and field guides wil include the following general steps:

1. Convert all doc files, if any, to Markdown in a Jupyter notebook. 

2. Add images and data and display any within the notebook (refer the [Markdown cheatsheet](../PS_0_Setup/00_Markdown/Markdown_Cheat_Sheet.png))

3. After finalizing the precept in folder 2, we push the changes downstream to folder 3 before the precept starts on Thursdays.

The typical Github workflow follows only a few commands. Whenever you start working on a problem set on a given workday, first check that you are in the right branch (`devel`) of the repository by typing:

`git branch`

If this highlights any branch other than `devel` as your current working branch (i.e. displays a star (`*`) or text in green), change your working
branch by typing:

`git checkout devel`

Next pull the changes that others might have pushed to Github while you were away:

`git pull origin`

Next, look at the status of your files relative to those online, and add files if you have created/modified files for your precept:

```
git status
git add -f filename.png
```

Please note that the [.gitignore](../../.gitignore) file specifies a *very long* list of files/extensions that are meant to be ignored while checking for local changes
to the repository. This is done to make sure whatever changes students make on their end do not cause conflicts with our *persistent* files in the folder 3 [above](#folders).
However, this also means that you have to add the `-f` flag when adding files that you want to force push to the remote Github online repository. The best way to check if you have gotten
the desired result is by checking the list of files under your precept folder (e.g. `PS_1_*`) on [our working Github repository](https://github.com/pmoulik/GEO203_Fall2022_PSETS/tree/devel).

Keep checking `git status` until you get the desired list of files to be pushed online. Then, commit this change, add a comment and push to the Github repository:

```
git commit -am "I have added cool things"
git push origin
```

Check the messages from these commands and the files on the Github repository online. There should be a key for the problem set (i.e. suffix *-Key.ipynb*) online.
**Please leave a message for the instructor on Slack latest by 9 PM before the day of the first precept**, so that they can review and push it downstream to
the Princeton repository for the students. You are then good to go!

During the Precept
------------------

Please ask students to start an Adroit session an pull the latest changes using the following the [Resource Pipeline](../Resource_Pipeline.png). They should
duplicate the notebook and put the suffix *-PUID.ipynb* where *PUID* is their Princeton user name.

Ask students to answer questions (To Do's) by filling cells within Jupyter notebooks with (Markdown) text or (Python) code answers. 
Make them run the whole notebook on Adroit and upload the output as pdf on Gradescope (See [Start End Session](Start_End_Session.png)).

Please note that this procedure will require that we move all course content on our end to Jupyter Notebooks and Markdown text. 
No Microsoft doc files will be created unless it is absolutely required to fulfill a very specific purpose.

Editing on Github
-----------------

Some tasks only require editing text and no execution of code. These include posting keys to reading quizzes. These can be easily done directoy on Github without
opening a terminal or Jupyter notebook.

Regarding quizzes, we upload the answers in Markdown onto Github through the [following page](https://github.com/pmoulik/GEO203_Fall2022_PSETS/tree/devel/Reading_Quizzes).
Click the `Add file->Create new file` button on the top right, and name your file with an extension *.md* so that Github knows that it is a Markdown file.

You can then write to Github in Markdown and preview how it will look like. For reference, the first quiz gets rendered 
[like this in Markdown](https://github.com/pmoulik/GEO203_Fall2022_PSETS/blob/devel/Reading_Quizzes/Quiz_Stellar_Formation_and_Comparative_Planetology.md).

Note that the answer is given in green colors. The text between `<font color='green'>` and `</font> `gets rendered in green. e.g.

`<font color='green'>Oxygen-rich atmosphere</font>`

At the bottom, add a comment about what you did, choose `Commit directly to the devel branch.` and press the `Commit new file` button.

Document your work
------------------

Please use as many Markdown cells as you can and be as descriptive as possible. The usage of images (png/jpeg files) or videos (gif works best) works well with
Jupyter Notebooks and their use in instruction is strongly encouraged. 

Any new code block should be fully Doxygen commented in [Python](#python-formatting). If you have some free time, feel free to comment any code you modify.

Coding style
------------

When modifying an existing file, try to maintain consistency with its original style.  If the code you add looks drastically different from the original code, it may be difficult for readers to follow. Try to avoid this. As a general guideline, we recommend the following code formatting style:

Python formatting
------------------

**give space for breathing, use 4 spaces instead of tabs:**

good
~~~python
    dx = 0.5 * fac * (a - b)
~~~

bad
~~~python
	dx=1/2*fac*(a-b)
~~~

**comment, comment, comment your functions using Doxygen convention:**

good
~~~python
"""@package docstring
Documentation for this module.
More details.
"""
def func():
    """Documentation for a function.
    More details.
    """
    pass
class PyClass:
    """Documentation for a class.
    More details.
    """

    def __init__(self):
        """The constructor."""
        self._memVar = 0;
        pass
~~~


