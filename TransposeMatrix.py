class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row_cnt = len(A)
        col_cnt = len(A[0])
        matrix = list()
        for col_idx in range(col_cnt):
            row_list = list()
            for row in A:
                row_list.append(row[col_idx])
            matrix.append(row_list)
        return matrix
            
        
