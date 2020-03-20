from defaults import *
import sys

class Algorithm():
    number_algorithm = 1

    def Convolution2D(image, ddepth=-1, kernel=DEFAULT_FILTER):
        """
        @params:
            - image(object): the image object that need bluring
            - ddepth(int): the depth of image output
            - kernel(np.array): the matrix apply convolutional operation on image object.
        @return value:
            - the image object applied convolutional operation.
        @reference from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/01_2d_convolution.py
        """

        output = cv2.filter2D(src=image, ddepth=ddepth, kernel=kernel)
        return output


    def Bluring(image, ddepth=-1, size=SIZE_BLURING):
        """
        @params:
            - image(object): the image object that need bluring
            - ddepth(int): the depth of image output
            - size(int): the size value in the kernel motion blur
        @return value:
            - the image object applied bluring.
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/03_sharpening.py
        """
        print(size, ddepth)
        kernel_motion_blur = np.zeros((size, size))
        kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
        kernel_motion_blur = kernel_motion_blur / size
        # applying the kernel to the input image
        output = cv2.filter2D(image, ddepth, kernel=kernel_motion_blur)
        return output


    def Sharpening(image, ddepth=-1, selected_kernel_sharpen='1'):
        """
        @params:
            - image(object): the image object that need bluring
            - ddepth(int): the depth of image output
            - selected_kernel_sharpen (enum: {1,2,3})
        @return value:
            - the image object applied sharpened
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/03_sharpening.py
        """
        output = cv2.filter2D(image, ddepth=ddepth, kernel=KERNEL_SHAPEN[selected_kernel_sharpen])
        return output

    def Mix_channel(img,src_cs,dst_cs):
        if src_cs == dst_cs:
	        return img

    def Embossing(image, ddepth=-1, selected_kernel_emboss='1'):
        """
        @params:
            - image(object): the image object that need bluring
            - ddepth(int): the depth of image output
            - selected_kernel_emboss (enum: {1,2,3})
        @return value:
            - the image object applied embossed
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/04_embossing.py
        """

        # converting the image to grayscale
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(selected_kernel_emboss)
        # applying the kernels to the grayscale image and adding the offset to produce the shadow
        output = cv2.filter2D(gray_img, -1, KERNEL_EMBOSS[selected_kernel_emboss]) + 128
        return output

    def Embossing_advance(image, selected_kernel_emboss='sobel_horizontal', ksize=5):
        """
        @params:
            - image(object): the image object that need bluring
            - selected_kernel_emboss (str) is the method will apply on image
            - ksize (int):
        @return value:
            - the image object applied embossed
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/05_embossing_advance.py
        """
        if selected_kernel_emboss == 'sobel_horizontal':
            # It is used depth of cv2.CV_64F.
            output = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=ksize)
        elif selected_kernel_emboss == 'sobel_vertical':
            # Kernel size can be: 1,3,5 or 7.
            output = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=ksize)
        elif selected_kernel_emboss == 'laplacian':
            output = cv2.Laplacian(image, cv2.CV_64F)
        elif selected_kernel_emboss == 'canny':
            output = cv2.Canny(image, 50, 240)
        else:
            print("The kernel is not valid !")
            sys.exit(2)
        return output

    def Erosion(image, ksize=5, iterations=1):
        """
        @params:
            - image(object): the image object that need bluring
            - ksize (int): the size of kernel will apply Convolution2D
            - iterations (int)
        @return value:
            - the image object applied erosion
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/06_erosion_dilation.py

        """
        kernel = np.ones((ksize, ksize), np.uint8)
        img_erosion = cv2.erode(image, kernel, iterations=1)
        return img_erosion

    def Dilation(image, ksize=5, iterations=1):
        """
        @params:
            - image(object): the image object that need bluring
            - ksize (int): the size of kernel will apply Convolution2D
            - iterations (int)
        @return value:
            - the image object applied dilation
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/06_erosion_dilation.py

        """

        kernel = np.ones((ksize, ksize), np.uint8)
        img_dilation = cv2.dilate(image, kernel, iterations=1)
        return img_dilation

    def Vignette_filter(image):
        """
        @params:
            - image(object): the image object that need bluring
            - ksize (int): the size of kernel will apply Convolution2D
            - iterations (int)
        @return value:
            - the image object applied erosion
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/06_erosion_dilation.py

        """

        rows, cols = image.shape[:2]

        # generating vignette mask using Gaussian kernels
        kernel_x = cv2.getGaussianKernel(cols,200)
        kernel_y = cv2.getGaussianKernel(rows,200)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        output = np.copy(image)

        # applying the mask to each channel in the input image
        for i in range(3):
            output[:,:,i] = output[:,:,i] * mask

        return output

    def Vifnette_gaussian(image):
        """
        @params:
            - image(object): the image object that need bluring
        @return value:
            - the image object applied Vifnette_gaussian
        @refernce from:
            - https://github.com/PacktPublishing/OpenCV-3-x-with-Python-By-Example/blob/master/Chapter02/06_erosion_dilation.py

        """
        rows, cols = img.shape[:2]

        # generating vignette mask using Gaussian kernels
        kernel_x = cv2.getGaussianKernel(int(1.5*cols),200)
        kernel_y = cv2.getGaussianKernel(int(1.5*rows),200)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        mask = mask[int(0.5*rows):, int(0.5*cols):]
        output = np.copy(img)

        # applying the mask to each channel in the input image
        for i in range(3):
            output[:,:,i] = output[:,:,i] * mask
        return output

    # def Enhancing_contrast(image, option=None):
    #
    #    if option==None:
    #        output = cv2.equalizeHist(src=image)
    #    elif option == '2':
    #        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #        # equalize the histogram of the Y channel
    #        img_grey[:,:,0] = cv2.equalizeHist(grayimg[:,:,0])
    #        # convert the YUV image back to RGB format
    #        output = cv2.cvtColor(img_grey, cv2.COLOR_GRAY2RGB)
    #
    #    return output


    def Mix_channel(image, src_cs: str, dst_cs: str):
        if src_cs == dst_cs:
            return image
        mapp = {}
        for i in range(len(dst_cs)):
	        mapp[dst_cs[i]] = i

        fromto = []

        for i in range(len(src_cs)):
	        fromto.append(i)
	        fromto.append(mapp[src_cs[i]])

        ret = np.zeros(img.shape, dtype = np.uint8 )
        cv2.mixChannels([img],[ret],fromto)

        ret = np.zeros(image.shape, dtype = np.uint8 )
        cv2.mixChannel([image],[ret],fromto)
        return ret

    def Change_to_RBG(img,src_cs):
	    if src_cs == 'RGB':
	        return img
	    mapp = {
	        'XYZ':cv2.COLOR_XYZ2RGB,
	        'HLS':cv2.COLOR_HLS2RGB,
	        'HSV':cv2.COLOR_HSV2RGB,
	        'YUV':cv2.COLOR_YUV2RGB,
	        'GRAY':cv2.COLOR_GRAY2RGB
	    }
	    return cv2.cvtColor(img,mapp[src_cs])


    def Change_from_RBG(img,dst_cs):
	    mapp = {
	        'XYZ':cv2.COLOR_RGB2XYZ,
	        'HLS':cv2.COLOR_RGB2HLS,
	        'HSV':cv2.COLOR_RGB2HSV,
	        'YUV':cv2.COLOR_RGB2YUV,
	        'GRAY':cv2.COLOR_RGB2GRAY
	    }
	    return cv2.cvtColor(img,mapp[dst_cs])

    def Color_space_convert(img,src_cs = 'RGB',dst_cs='BGR'):
        r"""
            Args:
                img(array) : image array
                src_cs(str) : original space color
                dst(str) : target space color
            Return image array after being converted
            Example:
        """
        if src_cs == dst_cs:
    	    return image
        srcset = {x for x in src_cs}
        dstset = {x for x in dst_cs}
        if srcset == dstset:
    	    return Mix_channel(image,src_cs,dst_cs)

        def takepresent(sets):
    	    if (sets =={'R','B','G'}):
    		    return 'RGB'
    	    if (sets =={'X','Y','Z'}):
    		    return 'XYZ'
    	    if (sets =={'H','L','S'}):
    		    return 'HLS'
    	    if (sets =={'H','S','V'}):
    		    return 'HSV'
    	    if (sets =={'G','R','A','Y'}):
    		    return 'GRAY'

        image = Algorithm.Mix_channel(image=image, src_cs=src_cs, dst_cs=takepresent(srcset))
        image = Algorithm.Change_to_RBG(image=image, src_cs=takepresent(srcset))
        image = Algorithm.Change_from_RBG(image=image, dst_cs=takepresent(dstset))
        image = Algorithm.Mix_channel(image=image, src_cs=takepresent(dstset), dst_cs=dst_cs)

        return img

    def Translation(img,dx,dy):
	    r"""
	        Args:
	            img(array) : image array
		    dx : translation distance along x-axis
		    dy : translation distance along y-axis
	        Return image after being translated
	        Example:
	    """
	    rows, cols = img.shape[:2]
	    translation_mat = np.float32([[1,0,dx],[0,1,dy]])
	    return cv2.warpAffine(img,translation_mat, (rows+abs(dx),cols+abs(dy)))

    def Rotation(img,angle):
        r"""
	        Args:
	            img(array) : image array
		        angle(int) : angle to rotate
	        Return image after being rotated
	        Example:
	    """
        num_rows, num_cols = img.shape[:2]
        translation_matrix = np.float32([ [1,0,int(0.5*num_cols)], [0,1,int(0.5*num_rows)] ])
        rotation_matrix = cv2.getRotationMatrix2D((num_cols, num_rows), angle, 1)

        img_translation = cv2.warpAffine(img, translation_matrix, (2*num_cols, 2*num_rows))
        return cv2.warpAffine(img_translation, rotation_matrix, (num_cols*2, num_rows*2))


    def Scaling(img,fx,fy):
	    r"""
	        Args:
	            img(array) : image array
		        fx(float) : ratio along x-axis
		        fy(float) : ratio along y-axis
	        Return image after being scaled
	        Example:
	    """
	    return cv2.resize(img,None,fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)

    def Vertical_wave(img,dx):
	    r"""
	        Args:
	            img(array) : image array
		        dx(float) : waving distance along x-axis

	        Return image after being waved
	        Example:
	    """
	    img_output = np.zeros(img.shape, dtype=img.dtype)
	    rows,cols = img.shape[:2]
	    for i in range(rows):
	        for j in range(cols):
		        offset_x = int(dx * math.sin(2 * 3.14 * i / 180))
		        offset_y = 0
		        if j+offset_x < rows:
		            img_output[i,j] = img[i,(j+offset_x)%cols]
		        else:
		            img_output[i,j] = 0
	    return img_output

    def Horizontal_wave(img,dy):
        r"""
	        Args:
	            img(array) : image array
		        dy(float) : waving distance along y-axis

	        Return image after being waved
	        Example:
	    """
        img_output = np.zeros(img.shape, dtype=img.dtype)
        rows,cols = img.shape[:2]
        for i in range(rows):
            for j in range(cols):
                offset_y = int(dy * math.sin(2 * 3.14 * j / 150))
                offset_x = 0
                if i+offset_y < rows:
                    img_output[i,j] = img[(i+offset_y)%rows,j]
                else:
                    img_output[i,j] = 0
        return img_output

    def Double_wave(img,dy):
        r"""
	        Args:
	            img(array) : image array
		        dx(float) : waving distance along x-axis
		        dy(float) : waving distance along y-axis

	        Return image after being waved
	        Example:
	    """
        img_output = np.zeros(img.shape, dtype=img.dtype)
        rows,cols = img.shape[:2]
        for i in range(rows):
            for j in range(cols):
                offset_x = int(dx * math.sin(2 * 3.14 * i / 150))
                offset_y = int(dy * math.cos(2 * 3.14 * j / 150))
                if i+offset_y < rows and j+offset_x < cols:
                    img_output[i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
                else:
                    img_output[i,j] = 0
        return img_output

    def Concave_effect(img):
        r"""
	        Args:
	            img(array) : image array


	        Return image
	        Example:
	    """
        img_output = np.zeros(img.shape, dtype=img.dtype)
        rows,cols = img.shape[:2]
        for i in range(rows):
            for j in range(cols):
                offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2*cols)))
                offset_y = 0
                if j+offset_x < cols:
                    img_output[i,j] = img[i,(j+offset_x)%cols]
                else:
                    img_output[i,j] = 0
        return img_output
