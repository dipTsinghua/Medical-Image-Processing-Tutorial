import SimpleITK as sitk
import matplotlib.pyplot as plt


def display_single_image(image_x, image_y, image_z, image_npa):
    plt.subplots(1,3,figsize=(10,8))

    # Draw the fixed image in the first subplot.
    plt.subplot(1,3,1)
    plt.imshow(image_npa[image_z,:,:],cmap=plt.cm.Greys_r)
    plt.title('image')
    plt.axis('off')
    
    # Draw the fixed image in the second subplot.
    plt.subplot(1,3,2)
    plt.imshow(image_npa[:,image_y,:],cmap=plt.cm.Greys_r)
    plt.title('image')
    plt.axis('off')

    # Draw the fixed image in the third subplot.
    plt.subplot(1,3,3)
    plt.imshow(image_npa[:,:,image_x],cmap=plt.cm.Greys_r)
    plt.title('image')
    plt.axis('off')

    plt.show()


# Callback invoked by the interact IPython method for scrolling through the image stacks of
# the two images (moving and fixed).
def display_images(fixed_image_z, moving_image_z, fixed_npa, moving_npa):
    # Create a figure with two subplots and the specified size.
    plt.subplots(1,2,figsize=(10,8))
    
    # Draw the fixed image in the first subplot.
    plt.subplot(1,2,1)
    plt.imshow(fixed_npa[fixed_image_z,:,:],cmap=plt.cm.Greys_r);
    plt.title('fixed image')
    plt.axis('off')
    
    # Draw the moving image in the second subplot.
    plt.subplot(1,2,2)
    plt.imshow(moving_npa[moving_image_z,:,:],cmap=plt.cm.Greys_r);
    plt.title('moving image')
    plt.axis('off')
    
    plt.show()


# Callback invoked by the IPython interact method for scrolling and modifying the alpha blending
# of an image stack of two images that occupy the same physical space. 
def display_images_with_alpha(image_z, alpha, fixed, moving):
    img = (1.0 - alpha)*fixed[:,:,image_z] + alpha*moving[:,:,image_z] 
    plt.imshow(sitk.GetArrayViewFromImage(img),cmap=plt.cm.Greys_r);
    plt.axis('off')
    plt.show()
    

# Callback invoked when the StartEvent happens, sets up our new data.
def start_plot():
    global metric_values, multires_iterations
    
    metric_values = []
    multires_iterations = []


# Callback invoked when the EndEvent happens, do cleanup of data and figure.
def end_plot():
    global metric_values, multires_iterations
    
    del metric_values
    del multires_iterations
    # Close figure, we don't want to get a duplicate of the plot latter on.
    plt.close()