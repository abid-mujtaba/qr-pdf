#! /usr/bin/env python

# Author: Abid H. Mujtaba (abid.naqvi83@gmail.com)
#
# This script takes a String as input (on the command line) and creates a tex file which can be compiled using pdflatex to produce the corresponding QR Code.

import jinja2
import qrcode
import sys

BASE_FILE = "qr-pdf"
TEMPLATE_FILE = BASE_FILE + ".template"
TEX_FILE = BASE_FILE + ".tex"


def main():

    if (len(sys.argv) < 2):
        print("Error: String input for conversion to QR Code is missing")
        sys.exit(1)

    data = sys.argv[1]      # The String that will be converted to the qr code

    qr = qrcode.QRCode()    # Object for generating the QR Code

    qr.add_data(data)
    qr.make(fit=True)       # Generate the QR Code

    matrix = qr.get_matrix()

    length = len(matrix)        # The side length of the QR Code

    print("Length: " + str(length))

    # Load the template
    loader = jinja2.FileSystemLoader(searchpath=".")        # Search for templates in current folder
    env = jinja2.Environment(loader=loader)
    template = env.get_template(TEMPLATE_FILE)

    # Write rendered template to tex file
    fout = open(TEX_FILE, "w")
    fout.write(template.render())
    fout.close()



if __name__ == '__main__':

    main()
