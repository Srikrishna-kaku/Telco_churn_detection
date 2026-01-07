import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TelcoCustomerChurn:
    def __init__(self, csv_path=r'D:\data science Vtech\Internship\TASK-1\Telco-Customer-Churn.Dataset.csv'):
        self.df = pd.read_csv(csv_path)
        # ensure numeric TotalCharges and fill missing values
        self.df['TotalCharges'] = pd.to_numeric(self.df['TotalCharges'], errors='coerce')
        self.df['TotalCharges'].fillna(self.df['TotalCharges'].median(), inplace=True)
        # drop customerID if present
        if 'customerID' in self.df.columns:
            self.df.drop(['customerID'], axis=1, inplace=True)

    
     #visualization-1churn analysis in customers
    def visualize_churn_analysis(self):
    

        plt.figure(figsize=(4, 6))
        churn_counts = self.df['Churn'].value_counts()
        plt.pie(churn_counts, labels=churn_counts.index,autopct='%1.1f%%', startangle=140,  
            colors=['green','red'])
        plt.title(' Customer Churn_Distribution')
        plt.savefig('churn_distribution.png')
        plt.show()

     #visualization-2  churn customers with their tenure
    def visualize_tenure_analysis(self):
   

        plt.figure(figsize=(4, 6))
        self.df[self.df['Churn'] == 'No']['tenure'].hist(alpha=0.4, color='blue', label='Retained', bins=30)
        self.df[self.df['Churn'] == 'Yes']['tenure'].hist(alpha=0.4, color='red', label='Churned', bins=30)
        plt.xlabel('Tenure')
        plt.ylabel('Number of Customers')
        plt.title('Tenure Distribution: Retained vs Churned')
        plt.legend()
        plt.savefig('tenure_distribution.png')
        plt.show()

    #visualization-3 churn analysis with contract type
    def visualize_contract_type_analysis(self):
    

        plt.figure(figsize=(4,6))
        Contract_Churn=self.df.groupby('Contract')['Churn'].value_counts(normalize=True)
        Contract_Churn.unstack().plot(kind='bar', stacked=True,color=['green','orange'])
        plt.xlabel('Contract Type')
        plt.ylabel('Percentage of Customers (%)')
        plt.title('Churn Rate by Contract Type')
        plt.legend()
        plt.savefig('contract_type-churn.png')
        plt.show()

    #visualization-4 monthly charges comparision between churned and reteined customers
    def visualize_monthly_charges_analysis(self):
    

        plt.figure(figsize=(5, 7))
        plt.boxplot([self.df[self.df['Churn'] == 'No']['MonthlyCharges'], self.df[self.df['Churn'] == 'Yes']['MonthlyCharges']], 
                    labels=['Retained', 'Churned'], patch_artist=True,
                    boxprops=dict(facecolor='lightblue',color='blue'))
        plt.xlabel('Customer Status')
        plt.ylabel('Monthly Charges ')
        plt.title('Monthly Charges Comparison : Retained vs Churned')
        plt.savefig('monthly_charges_comparision.png')
        plt.show()


    #visualization-5 churn analysis with internet service type
    def visualize_internet_service_analysis(self):
        internet_churn = self.df.groupby(['InternetService', 'Churn']).size().unstack()
        temp = internet_churn.div(internet_churn.sum(axis=1), axis=0) * 100
        temp.plot(kind='bar', color=['green','red'])
        plt.figure(figsize=(6,8))
        plt.xlabel('Internet Service Type')
        plt.ylabel('Percentage of Customers')
        plt.title('Churn Rate by Internet Service Type')
        plt.legend()
        plt.savefig('internet_service_churn.png')
        plt.show()



    
    
    #visualization-6 churn analysis with senior citizen
    def visualize_senior_citizen_analysis(self):
        plt.figure(figsize=(6,8))
        sns.countplot(x='SeniorCitizen', hue='Churn', data=self.df)
        plt.title('Churn rate by Senior Citizen ')
        plt.xlabel('Senior Citizen')
        plt.ylabel('Number of Customers')
        plt.savefig('senior_citizen_churn.png')
        plt.legend()
        plt.show()
if __name__ == "__main__":

    obj=TelcoCustomerChurn()
    obj.visualize_churn_analysis()
    obj.visualize_tenure_analysis()
    obj.visualize_contract_type_analysis()
    obj.visualize_monthly_charges_analysis()
    obj.visualize_internet_service_analysis()
    obj.visualize_senior_citizen_analysis()






 





