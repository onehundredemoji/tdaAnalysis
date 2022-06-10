import open3d as o3d
import numpy as np


print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("combined_multiway_registered.ply")
print(pcd)
print(np.asarray(pcd.points))

# create vector of minimum dimensions in pointcloud
data = np.asarray(pcd.points)
print("finding minimums to move cloud to origin")
# get an array of all min values in each dimension [minX, minY, minZ]
minArr = []
for dim in range(3):
    thisMin = data[0][dim]
    for point in data:
        thisMinCurr = point[dim]
        if thisMinCurr < thisMin:
            thisMin = thisMinCurr
    minArr.append(thisMin)
print(f"minimums [x, y, z]: {minArr}")

# make all values in minArr negative
negMinArr = [-1 * minArr[0], -1 * minArr[1], -1 * minArr[2]]

# translate it
pcd.translate(negMinArr)
print("shifted by subtracting the minimum vector")
print(np.asarray(pcd.points))

# visualize it
o3d.visualization.draw_geometries([pcd])