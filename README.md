Purpose: Implements ingest(e, D), which ingests event data and TopXSimpleLTVCustomers(x, D), which calculates the LTV for top x customers

Pre-requisites:
  1. Python 2.7.x
  2. Unix or windows environment

Running Instructions:
  1. Make sure python version 2.7.x is installed, if not download the latest python 2.7 compiler.
  2. Run GetCustomerLifetimeValue.py from ide like PyCharm or command line
  3. Follow the prompts to get the output

Input Parameters:
  1. input_file: The name of the input file; The default directory is the input folder alongside the src folder, which can be changed by manually editing the input_path variable in the program
  2. output_file: The name of the output_file
  3. x: The number of top most customers with highest LTV

Input file requirements:
  1. The input file is expected to be in JSON format and currently does not support any other format
  2. The extension of the file wouldn't matter as long as the data is stored as a JSON object
  3. Please keep these in mind when formatting the input to the program
  
Output:
  Generates an output file with the name and extension supplied by the user.
  The default directory is the output folder alongside the src folder.
  You can change the folder by manually editing the output_path variable in the program.
