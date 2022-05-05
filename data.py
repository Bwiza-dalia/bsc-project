import pandas as pd
import numpy as np


class dataset:
    def __init__(self) -> None:
        self.sales = pd.read_excel("sales_bcs.xlsx")
        self.customers=pd.read_excel('sales_bcs.xlsx', 'Customers Sheet')
        self.sites = pd.read_excel('sales_bcs.xlsx', 'Site Location sheet')
        self.products=pd.read_excel('sales_bcs.xlsx', 'Products_Sheet')
        self.sales_team= pd.read_excel('sales_bcs.xlsx','Sales Team Sheet')

        #Add a total amount to every transaction
        self.add_sales()
        #Add a month column
        self.add_month()
        #add profit
        self.add_profit()
        self.add_month_year()
        #self.add_bandwidth()
        self.demand_pro()


    def demand_pro(self):
        prod_demand = {}
        for product in list(self.sales['_ProductID'].unique()):
         month_demand = []
        for mo in list(self.sales['Month-Year'].unique()):
          b = self.sales.loc[(self.sales['Month-Year'] == mo) & (self.sales['_ProductID'] == product)].OrderNumber.count() 
          month_demand.append(b)

        prod_demand[product] = month_demand
        prod_demand['Month-Year'] = self.sales['Month-Year'].unique()
        bv= pd.DataFrame(prod_demand)
        chart_data = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['Month-Year', '1'])



    def add_month(self):
        self.sales['Month'] = pd.DatetimeIndex(self.sales['OrderDate']).month

    def add_sales(self):
        self.sales['Total'] = (self.sales['Order Quantity'] * self.sales['Unit Price']) - self.sales['Discount Applied']

    def add_profit(self):
        self.sales['Profit'] = (self.sales['Unit Price']- self.sales['Unit Cost'])-self.sales['Discount Applied']
    # def add_bandwidth(self):
    #     self.sales['bandwidth'] = self.sales(pd.concat(self.products[('Bandwidth','_ProductID')], keys=['Bandwidth','_ProductID'], axis=1))
    def add_month_year(self):
        self.sales['Month-Year']= self.sales['OrderDate'].dt.strftime('%Y/%m')
    @property
    def best_months_df(self):
        best_month = self.sales.groupby('Month').sum()
        return best_month['Total']

    @property
    def best_district_df(self):
        best_district = self.sales.groupby('_SiteID').sum()
        return best_district['Total']
    
    @property
    def best_district_products(self):
        all_transactions = self.sales[(self.sales['_SiteID']) == 284]
        product = all_transactions.groupby('_ProductID', as_index=False).sum()
        return product[['_ProductID', 'Total']]

    @property
    def total_orders(self):
        total_orders = self.sales.groupby('OrderNumber').sum()
        return total_orders
