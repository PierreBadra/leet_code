from colorama import Fore


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        numCols = len(s)
        Matrix = [[" " for _ in range(numCols)] for _ in range(numRows)]

        currRow = 0
        currCol = 0
        i = 0
        while i < len(s) and currCol < numCols:
            if currCol != 0 and currRow == 0:
                currRow += 1

            if currRow < numRows:
                Matrix[currRow][currCol] = s[i]
                currRow += 1
                i += 1
            else:
                currRow -= 1
                while currRow != 0 and i < len(s):
                    currRow -= 1
                    currCol += 1
                    if currCol >= numCols:
                        break
                    Matrix[currRow][currCol] = s[i]
                    i += 1

        converted_string = ""

        for row in Matrix:
            converted_string += str.strip("".join(row)).replace(" ", "")

        return converted_string


def main():
    solution = Solution()
    test_cases = [
        [["PAYPALISHIRING", 3], "PAHNAPLSIIGYIR"],
        [["PAYPALISHIRING", 4], "PINALSIGYAHRPI"],
        [["A", 1], "A"],
        [["ABCD", 3], "ABDC"],
        [
            [
                "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.",
                3,
            ],
            "Aiosrhem,tseoihartaaeeriwgrlasasnoctaoieplnrmiaodprs,ubroohreunefnttacneedhsmwynihrieto,iheeaalwnefrdutettpntainnwrdvdr.adew,anereqcustbaeeitdcntnlocojmsuuoddis",
        ],
        [
            [
                "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.",
                5,
            ],
            "Aore,sohraerwraancaiprmods,roreeftaeesmniie,ieawnrdetntnndv.adew,anereqcustbaeeitdcntnlocojmsuuoddislniaprubohunntcndhwyhrtohealefuttpaiwrdrishmteiataeiglssotoe",
        ],
    ]

    for test_case in test_cases:
        answer = solution.convert(test_case[0][0], test_case[0][1])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected \n"{test_case[1]}"; got \n"{answer}"')


if __name__ == "__main__":
    main()
