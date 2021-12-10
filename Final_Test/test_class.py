import pandas as pd
import csv

class TestClass:

    filename = "captains.txt"
    col_name_one = "name"
    col_name_two = "tied"

    def read_col(self,file_name, col_name, col_type):
        values = list()
        with open(file_name) as FH:
            rows = csv.reader(FH)
            headers = next(rows)
            col_idx = headers.index(col_name)
            for row in rows:
                val = col_type(row[col_idx])
                values.append(val)
        return values


    def test_TC01CaptiansHavingAtleastOneTiedMatch(self):
        tied_col = self.read_col(self.filename, self.col_name_two, str)
        Tied_dataframe = pd.DataFrame(list(tied_col), columns=['Tied'])
        Atleastone_Tiedmatch = Tied_dataframe[Tied_dataframe['Tied'] > '0']
        Exp_count=3
        Act_count=int(len(Atleastone_Tiedmatch))
        assert Act_count == Exp_count

    def test_TC02HighestNoofTiedMatchCaptianName(self):
        names_col = self.read_col(self.filename, self.col_name_one, str)
        tied_col = self.read_col(self.filename, self.col_name_two, str)
        captains_dataframe = pd.DataFrame(list(zip(names_col, tied_col)), columns=['Player_Name', 'Tied'])
        captains_dataframe = captains_dataframe.sort_values(by=['Tied'], ascending=False)
        Act_captain_name = "MS Dhoni"
        Exp_captains_name = (captains_dataframe['Player_Name'].tolist())[0]
        assert Act_captain_name == Exp_captains_name

