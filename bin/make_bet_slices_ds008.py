#!/usr/bin/python
import os

# since this template html file has only been saved in one specific place,
# the PATH was hard coded. If a different template is needed then this path must be changed!
template_dir = '/home/srajen/Projects/local/share/templates/html/bet_slices.html'

# reading the contents of bet_slices.html
myfile = open(template_dir, 'r')		#open file to read
data = myfile.readlines()				#print file output
myfile.close()					#close file

# use a for loop to write the file output
sub_num = 1 


output_file = '/home/srajen/Projects/output/html/sub{:03d}_bet_slices.html'

print output_file.format(sub_num)
out_file = open(output_file.format(sub_num), 'w')
#out_file.write(data.format(sub_num,sub_num))
for line in data:
	out_file.write(line.format(sub_num))
out_file.close()
