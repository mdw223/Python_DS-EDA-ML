The input0x.txt files contain the user input for each test including the names of the input and output files. Each test will use the cardata.txt file for input and a cardata-out0x.txt for the inventory output. The output0x.txt files show all the output to the terminal based upon the input from the input0x.txt file. An additional copy of the orginial cardata.txt file is included as cardataCOPY.txt in case you accidentally override the original.

Note: My program echoes the user input to make the expected output files easier to follow. You are not required to do this as the success of each test will be determined by your cardata-out0x.txt files. For testing purposes, it may be more convenient to echo all input so that your expected output files match mine.

You can run your program with these files by redirecting the input and output:

python3 hw10LastNameFirstI.py < input01.txt > my_output01.txt

Then compare the files with the diff command:

diff output01.txt my_output01.txt

for each pair of files.

You don't need to worry about differences in whitespace.

You can also compare your output files with the ones in this folder:

diff cardata-out01.txt mycardata-out01.txt

for each pair of files.
