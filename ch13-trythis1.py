'''Try this: Redirecting input and outputWrite some code to use the mio.py module in listing 13.1 to capture all the print output
of a script to a file named myfile.txt, reset the standard output to the screen, and print
that file to screen.'''
import mio

mio.capture_output("myfile.txt")
print("whatever you want to write.")
print(13/3)
print('these go to the file not the standard screen')
mio.restore_output()
print('this shows on the screen')
mio.print_file("myfile.txt")