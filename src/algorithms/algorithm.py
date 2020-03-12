from defaults import *


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
        @return value:
            - the image object applied Sharpening
        """
        output = cv2.filter2D(image, ddepth=ddepth, kernel=KERNEL_SHAPEN[selected_kernel_sharpen])
        return output
    
    r"""Date: 12/3/2020
    Author: Nguyen Quoc Cuong
    """

    def Mix_channel(img,src_cs,dst_cs):
        if src_cs == dst_cs:
	        return img

        mapp = {}
        for i in range(len(dst_cs)):
	        mapp[dst_cs[i]] = i
    
        fromto = []

        for i in range(len(src_cs)):
	        fromto.append(i)
	        fromto.append(mapp[src_cs[i]])
    
        ret = np.zeros(img.shape, dtype = np.uint8 )
        cv2.mixChannels([img],[ret],fromto)

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
                    img(array of uint32) : image array 
                    src_cs(str) : original space color
                    dst(str) : target space color 
                Return image array after being converted 
                Example:
            """ 
            if src_cs == dst_cs:
    	        return img

            srcset = {x for x in src_cs}
            dstset = {x for x in dst_cs}
            if srcset == dstset:
    	        return Mix_channel(img,src_cs,dst_cs)

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

            img = Mix_channel(img,src_cs,takepresent(srcset))
            img = Change_to_RBG(img,takepresent(srcset))
            img = Change_from_RBG(img,takepresent(dstset))
            img = Mix_channel(img,takepresent(dstset),dst_cs)

            return img
