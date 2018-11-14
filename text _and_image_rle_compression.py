import image_data


class RLE:


    '''
    Given any image which is represented by a list of its rows. Run Length Encodes each i of the image and returns
    the result as a list of the encoded image rows and also returns the total number of characters in both the
    original image and the encoded image and give any text is compressing using RLE
    '''




    def encode_text_image(self, srcImage):
        encodedImg = []
        numImage = 0
        encodednumImg = 0


        # loop through every image i(row)
        for i in srcImage:
            encodedRow = ''
            count = 0
            char = i[0]


            # loop through every character in the i
            # and count how many consecutive elements of
            # that character are on that image i

            for character in i:

                if char != character:

                    if count == 1:
                        encodedRow += char
                    else:
                        encodedRow += str(count) + char
                    char = character
                    count = 1

                else:
                    count += 1
            # encode the last character in the ith row
            if count == 1:
                encodedRow += char
            else:
                encodedRow += str(count) + char

            # add encoded i to list holding the image encoding
            numImage += len(i)
            encodednumImg += len(encodedRow)

            encodedImg.append(encodedRow)
        return encodedImg, numImage, encodednumImg



    def decode_text_image(self, encodedImage):
        decodeImage = []
        numEncodedImage = 0
        numDecodedImage = 0



        # loop through every image i
        for i in encodedImage:
            rowDecoded = ''
            count = 0
            # loop through every character in the i
            # and count how many consecutive elements of
            # that character are on that image i
            for character in i:
                # if character is a digit
                if character.isdigit():
                    count = count * 10 + ord(character) - ord('0')
                else:
                    if count == 0:
                        count = 1
                    rowDecoded += character * count
                    count = 0
            # add decoded i to list holding the image decoding
            decodeImage.append(rowDecoded)
            numEncodedImage += len(i)
            numDecodedImage += len(rowDecoded)

        return decodeImage, numEncodedImage, numDecodedImage


class Test:

    def __init__(self):
        self.solution = RLE()

    def test_0(self):
        encodedText = ['3bc2de4a']

        expectedDecode = 'bbbcddeaaaa'
        actualDecode, numEncoded, numDecoded = self.solution.decode_text_image(encodedText)
        return encodedText, expectedDecode, actualDecode, numEncoded, numDecoded


    '''
    This test first encodes the swan image and prints it out
    Then decodes the encoding and prints it out (the decoded image should
    match the original image)
    '''

    def img_test(self):
        swanImage = image_data.swan
        encodedImg, numImage, encodednumImg = self.solution.encode_text_image(swanImage)
        print ('Encoding of swan image')

        for i in encodedImg:
            print(i)

        print ('number of characters in original image is:' + str(numImage))
        print ('number of characters in encoded image is:' + str(encodednumImg))

        decodeImage, numEncodedImage, numDecodedImage = self.solution.decode_text_image(encodedImg)
        print ('Orginal swan image')

        for i in decodeImage:
            print (i)
        print ('number of characters in encoded image  is:' + str(numEncodedImage))
        print ('number of characters in decoded image is:' + str(numDecodedImage))





    '''
       This function test first encodes text and prints it out
       Then decodes the encoding and prints it out 
       '''




    def tests(self):
        all_tests = [self.test_0]  #all text test



        for test in all_tests:
            encodedString, expectedDecode, actualDecode, numEncoded, numDecoded = test()
            print ('encoded string  is:' + encodedString[0])
            print ('expected decode  is:' + expectedDecode)
            print ('actual decode  is:' + actualDecode[0])
            print ('number of characters in encoded string is: ' + str(numEncoded))
            print ('number of characters in decoded string  is:' + str(numDecoded))
            print( '==============================================================')


        self.img_test() #image swan test






test = Test()

test.tests()

