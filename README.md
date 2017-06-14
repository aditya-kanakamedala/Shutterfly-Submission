Purpose: Implements ingest(e, D), which ingests event data and TopXSimpleLTVCustomers(x, D), which calculates the LTV for top x customers

Pre-requisites:
  Python 2.7.x
  Unix or windows environment

Running Instructions:
  Make sure python version 2.7.x is installed, if not download the latest python 2.7 compiler.
  Run GetCustomerLifetimeValue.py from ide like PyCharm or command line
  Follow the prompts and get the output

Input Parameters:
  1> input_file: The name of the input file; The default directory is the input folder alongside the src folder, which can be changed by manually editing the input_path variable in the program
  2> output_file: The name of the output_file
  3> x: The number of top most customers with highest LTV

Output:
  Generates an output file with the name and extension supplied by the user. The default directory is the output folder alongside the src folder. You can change the folder by manually editing the output_path variable in the program.
