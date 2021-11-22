import numpy as np

class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        
        with open(filename, 'w') as f:
            f.writelines(self._matrix)
    
    def transpose(self):
        """
        Transpose the matrix.
        TODO: implement
        """      

        tran = Matrix(self._columns, self._rows)
        tran._rows =  [list(item) for item in zip(*self._rows)]
        
        return tran
          
    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if (self._rows != len(other)) or (self._columns != len(other[0])):
            raise Exception("Matrices cannot be added!")
            
        summ = Matrix(self._rows, self._columns)
        
        for i in range(self._rows):
            row = [sum(item) for item in zip(self._rows[i], other[i])]
            summ[i] = row

        return summ
      

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.

        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if (self._rows != len(other)) or (self._columns != len(other[0])):
            raise Exception("Matrices cannot be multiplied!")
        
        ret = Matrix(self._rows, self._columns)
        
        for i in range(self._rows):
            for j in range(self._columns):
                ret[i][j] = self._matrix[i][j]*other[i][j]
        
        if type(other) == int or type(other) == float:
            ret = self._matrix*other    

        return ret
        

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """
        
        if self._columns != other._rows:
            raise Exception("Matrices cannot be multiplied!")
        
        return np.matrix(self._matrix) @ np.matrix(other)

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        if self._rows != self._columns:
          raise Exception("Trace of the matrix does not exist!")
        
        trace = sum(self._matrix[i][i] for i in range(self._rows))
        
        return trace

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        if self._columns != self._rows:
            raise ValueError("Determinant does not exist!")
            
        return np.linalg.det(self._matrix)
    
        


