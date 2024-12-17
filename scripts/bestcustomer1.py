from datetime import datetime
import numpy as np
import pandas as pd


"""



"""

class BestCustomers:

    def __init__(self, m_columna, dataframe, dataframe2, d_columna, nfact_columna, monetary_columna, Recency_columna, Frecuency_columna, RFM_SCORE_columna, seg_columna, id_columna):
        self.monto_columna=m_columna
        self.dataframe=dataframe
        self.dataframe2=dataframe2
        self.date_columna=d_columna
        self.nfact_columna=nfact_columna
        self.monetary_columna=monetary_columna
        self.Recency_columna=Recency_columna
        self.Frecuency_columna=Frecuency_columna
        self.RFM_SCORE_columna=RFM_SCORE_columna
        self.seg_columna=seg_columna
        self.id_columna=id_columna



    def category(self):
        self.dataframe[self.monetary_columna]=pd.qcut(self.dataframe[self.monto_columna],q=5, labels=[1,2,3,4,5])
        self.dataframe[self.Recency_columna]=pd.qcut(self.dataframe[self.date_columna],q=5, labels=[5,4,3,2,1])
        self.dataframe[self.Frecuency_columna]=pd.qcut(self.dataframe[self.nfact_columna].rank(method='first'),q=5, labels=[1,2,3,4,5])
        return self.dataframe   

    def RFM_Score(self):
        self.dataframe[self.RFM_SCORE_columna] = (self.dataframe[self.Recency_columna].astype(str) + self.dataframe[self.Frecuency_columna].astype(str))
        return self.dataframe
    
    def mapp(self):
        seg_map = {r'[1-2][1-2]': 'hibernating',r'[1-2][3-4]': 'at_Risk',r'[1-2]5': 'cant_loose',r'3[1-2]': 'about_to_sleep',r'33': 'need_attention',r'[3-4][4-5]': 'loyal_customers',r'41': 'promising',r'51': 'new_customers',r'[4-5][2-3]': 'potential_loyalists',r'5[4-5]': 'champions'}
        self.dataframe[self.seg_columna]=self.dataframe[self.RFM_SCORE_columna].replace(seg_map, regex=True)
        return self.dataframe

    def int(self):
        self.dataframe[self.Recency_columna]=self.dataframe[self.Recency_columna].astype(int)
        self.dataframe[self.monetary_columna]=self.dataframe[self.monetary_columna].astype(int)
        self.dataframe[self.Frecuency_columna]=self.dataframe[self.Frecuency_columna].astype(int)
        return self.dataframe

    def eliminar_esp(self):
        self.dataframe2.columns = self.dataframe2.columns.str.strip()
        return self.dataframe2
    
    #def final(self):
    #    pd.merge(self.dataframe, self.dataframe2[[self.seg_columna, self.id_columna]], on=self.id_columna)
    #    return self.dataframe

    def ejec_bestcustomer(self):
        self.category()
        self.RFM_Score()
        self.mapp()
        self.int()
        self.eliminar_esp()
        #self.final()
        return self.dataframe