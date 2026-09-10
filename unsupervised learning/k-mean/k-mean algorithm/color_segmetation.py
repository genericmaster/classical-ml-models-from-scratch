import PIL.Image
import numpy as np
from sklearn.cluster import KMeans
"ckustering algorithms like kmeans can be usedasfilter type algorthms over images that give the mean colours within a specific k you use for clustering "
image = np.asarray(PIL.Image.open(r"add  any  image you want "))



X=image.reshape(-1,4)


kmean = KMeans(n_clusters=32,init="k-means++",random_state=42).fit(X)
print(kmean.labels_)
segmented_img =kmean.cluster_centers_[kmean.labels_]
print(segmented_img)
segmented_img =segmented_img.reshape(image.shape)
print(segmented_img)

segmented_img_uint8 = segmented_img.astype(np.uint8)
final_image = PIL.Image.fromarray(segmented_img_uint8)
final_image.show()