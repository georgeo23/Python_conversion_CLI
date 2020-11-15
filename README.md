# Python_conversion_CLI
Welcome to my Python Unit Converter CLI

## To begin with code editor - 

Click the green 'Code' button on the repo's page and click 'Download Zip'.


Open the file when it has downloaded, click back once and you will see 'Python_conversion_CLI.zip'.


Right click on it and click 'extract all' to unzip it using your unzipping tool.


Then, once you have done that you will see a 'Python_conversion_CLI' folder, right click on it and select 'Open With' and select your preferred code editor or simply your terminal. 


Once your code editor loads up, you should see 2 '.py' files.


To begin converting, please open up a terminal in your code editor and type 'python converter.py'.


You're all set! Follow the instructions in the terminal to convert your desired units.


To enter a new conversion each time, just type 'python converter.py' or press your 'up' arrow in the terminal.





## To begin in your terminal -



Click the green 'Code' button on the repo's page and click 'Download Zip'.


Open the file when it has downloaded, click back once and you will see 'Python_conversion_CLI.zip'.


Right click on it and click 'extract all' to unzip it using your unzipping tool.


Then, once you have done that you will see a 'Python_conversion_CLI' folder.


Open up your terminal and go to the location of your folder, 'file_name/file_name/Python_conversion_CLI/' and simply type 'python converter.py'


Follow the instructions from the terminal and convert your desired units.


To make a new conversion once finished, type 'python converter.py' again or simply press the 'up' arrow on your terminal to retrieve the previous command.



## Adding a unit - 



Adding a new unit to this CLI is simple! If it's a length measurement, e.g yards, then simply google '1 yard in metres' to find the coefficient.


1 yard gives us 0.9144 m so in our to_standard dictionary, in the 'length' dictionary, we add '"yd": x*0.9144' and in from_standard's 'length' column we add '"yd": x/0.9144'.


This accounts for all measurements from m into yd and vice versa! It's really that simple. 
