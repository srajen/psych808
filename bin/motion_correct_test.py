#!/usr/bin/python

html_text = [
    "<html>",
    "<head>",
    "<title>Subject {:03d}: center slices</title>",
    "</head>",
    "<body>"
]

subj_id = 1

# How do we make what we mean by the following print statement work?
# print(html_text.format(subj_id))


# We can use a for loop to print each line separately, and add the
# format() method if the list entry has a format in it.  Does this
# generalize well?

for line in html_text:
    if line.find('{:03d}'):
        print(line.format(subj_id))
    else:
        print(line)




# We can join all the lines in the list into one long string, which will
# have a format() method.

html_text = "\n".join(html_text)
print(html_text.format(subj_id))

