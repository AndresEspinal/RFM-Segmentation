from datetime import datetime
import numpy as np
import pandas as pd


"""

Agrupar por clientes

"""

class Group_By:

    def __init__(self, m_columna, dataframe, d_columna, id_columna, qtty_columna, ff_columna, nf_columna):
        self.monto_columna=m_columna
        self.dataframe=dataframe
        self.idc_columna=id_columna
        self.date_columna=d_columna
        self.qtty_columna=qtty_columna
        self.ff_columna=ff_columna
        self.nf_columna=nf_columna


    def gbcustomer(self):
        self.dataframe=self.dataframe.groupby(self.idc_columna).agg({self.qtty_columna:'sum',self.monto_columna:'sum', self.ff_columna:lambda x: (self.dataframe[self.ff_columna].max()+pd.Timedelta(days=1)+pd.Timedelta(days=1)-x.max()).days,self.nf_columna:'count'}).reset_index()
        self.dataframe.sort_values(by=self.monto_columna,ascending=False)
        return self.monto_columna    



    def ejec_group_by(self):
        self.gbcustomer()
        return self.dataframe