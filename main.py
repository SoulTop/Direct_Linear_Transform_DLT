from file2array import file2array
from dlt import DLT

_3dMat=file2array('3d.txt', sp=4)
_imgMat = file2array('image.txt', sp=3)


Matrix, err = DLT(xyz_in=_3dMat, uv_in=_imgMat)\

print('Matrix')
print(Matrix)
print('\nError')
print(err)