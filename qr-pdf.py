#! /usr/bin/env python

# Author: Abid H. Mujtaba (abid.naqvi83@gmail.com)
#
# This script takes a String as input (on the command line) and creates a tex file which can be compiled using pdflatex to produce the corresponding QR Code.

import qrcode
import sys


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


if __name__ == '__main__':

    main()
