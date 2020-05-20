from logs import logDecorator as lD 
import jsonref, pprint

import argparse
import cv2
import dlib

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module1.module1'


@lD.log(logBase + '.blurFaces')
def blurFaces(logger):
    """Blur detected faces in an image

    This function detects frontal human faces in an input image
    using the Histogram of Oriented Gradients (HOG) feature.
    Then apply a Gaussian filter to the detected faces.

    Parameters
    ----------
    img : numpy.ndarray
        An 8-bit RGB image

    Returns
    -------
    numpy.ndarray
        An 8-bit RGB image after face blurring
    """

    img_res = img.copy()

    # Get the face detector instance
    faceDetector = dlib.get_frontal_face_detector()

    faceRects = faceDetector(img, 1)

    for bbox in faceRects:
        xmin = bbox.left()
        ymin = bbox.top()
        xmax = bbox.right()
        ymax = bbox.bottom()

        # Enlarge the face region for covering the hair
        width = xmax - xmin
        pad = width // 4
        face = img[ymin-2*pad:ymax, xmin-pad:xmax+pad]

        # Calculate the kernel size based on the size of the bounding box
        kernelSize = width // 2
        if kernelSize % 2 == 0:
            kernelSize += 1

        # Apply Gaussian filter on the faces
        face_blur = cv2.GaussianBlur(face, (kernelSize,kernelSize), 0)

        # Replace the detected faces with the blurred ones
        img_res[ymin-2*pad:ymax, xmin-pad:xmax+pad] = face_blur

    return img_res


@lD.log(logBase + '.main')
def main(logger, resultsDict, input, output):
    '''main function for module1
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    input: the path to input image
    output: the path to output image
    '''

    print('='*30)
    print('Main function of module 1')
    print('='*30)
    print('We get a copy of the result dictionary over here ...')
    pprint.pprint(resultsDict)

    configModule2 = json.load(open('../config/modules/module1.json'))
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input image')
    parser.add_argument('output', help='path to the output image')
    args = parser.parse_args()

    img = cv2.imread(args.input)
    
    # Check if the image is successfully read
    if img is None:
        print('Failed to read the image.')
        quit()
    else:
        img_blur = blurFaces(img)
        cv2.imwrite(args.output, img_blur)

    print('Getting out of Module 1')
    print('-'*30)

    return

