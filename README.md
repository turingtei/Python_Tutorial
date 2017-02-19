# Python_Tutorial
An Introduction to Interactive Programming in Python (Part 1)

Changes to the .py you are trying to run:

Replace the 'import simplegui' with the following in order to run the code in codesculptor.org and on your local machine
---------
try:
    import simplegui
except:
    import simpleguitk as simplegui
---------

1. Go to :
https://pypi.python.org/pypi/SimpleGUITk

2. Fulfill requirements:

	Install pip.
	Install Pllow.
	Install Pygame.
	Install matplotlib

3. Download and unzip: SimpleGUITK-1.1.13.tar.gz
4. Open terminal or cmd.
   cd to the folder where you unzipped SimpleGUITK-1.1.13
	 Tip: 'cd Simple*' saves you some keystrokes. 
5. Type (optional), to get an understandin what's about to happen:
	
	python3 setup.py --help-commands
		
  Note: I have both python 3.X and 2.X installed. If you only have python 2.X replace 'python3' with 'python' in the following commands.

  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  check             perform some checks on the package
  upload            upload binary package to PyPI

5. Type and execute:
	
	python3 setup.py build
	
	Will build the package underneath 'build/'
6. Type and execute:
	
	python3 setup.py install_lib
	
	Install all Python modules (extensions and pure Python)
	Because we are...thorough.
7. Type and execute:

	python3 clean
	
	Clean up temporary files from 'build' command
	Because...save space.

Happy coding!



