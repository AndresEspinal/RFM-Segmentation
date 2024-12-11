from datetime import datetime
import numpy as np
import pandas as pd


"""

Cambiar a formato de puntuación y fecha, duplicados, nulos y registros sin sentido

"""

class DateFormat:

    def __init__(self, m_columna, dataframe, d_columna):#, profit, bet, co, result, dropid, dropgameid):
        self.monto_columna=m_columna
        self.dataframe=dataframe
        self.date_columna=d_columna
        #self.prof_columna=profit
        #self.bet_columna=bet
        #self.co_columna=co
        #self.result_columna=result
        #self.drop_id=dropid
        #self.drop_gameid=dropgameid

    def format(self):
        self.dataframe[self.monto_columna]=self.dataframe[self.monto_columna].str.replace(',', '.').astype(float)
        return self.monto_columna    

    def fecha(self):
        self.dataframe[self.date_columna]=pd.to_datetime(self.dataframe[self.date_columna], format='%m/%d/%Y %H:%M:%S', dayfirst=True)
        return self.date_columna
    
    def duplicados(self):
        self.dataframe.drop_duplicates(inplace=True)
        return self.dataframe

    def nulos(self):
        self.dataframe=self.dataframe.dropna()
        return self.dataframe

    def eliminar_reg(self):
        self.dataframe=self.dataframe[self.dataframe[self.monto_columna]!=0]
        self.dataframe=self.dataframe[self.dataframe[self.monto_columna]>0]
        return self.dataframe
    
    def ejec_dateformat(self):
        self.format()
        self.fecha()
        self.duplicados()
        self.nulos()
        self.eliminar_reg()
        return self.dataframe