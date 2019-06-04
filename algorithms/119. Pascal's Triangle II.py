class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            newRow = [1]

            for j in range(1, len(row)):
                newRow.append(row[j] + row[j - 1])

            newRow.append(1)
            row = newRow

        return row
