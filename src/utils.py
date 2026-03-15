import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def prepare_for_visual(df: pd.DataFrame, name: str, type: str) -> pd.DataFrame:
    """We will use this function to standardise our dataframes for visulisation"""
    """The type is for dataframe type wether population or fertility rate"""
    if type=='p':
        df = df[['Country Name'] + list(df.loc[:, '1960':'2024'].columns)]
        df=df[df['Country Name']==name]

        df = df.set_index('Country Name').T
        df.columns =[f'{name}\'s Population']
        df['Year']=df.index
        df=df[['Year',f'{name}\'s Population']]
        df = df.reset_index(drop=True)
        df['Year'] = df['Year'].astype(int)


    elif type=='f':
        df = df[['Country Name'] + list(df.loc[:, '1960':'2023'].columns)]
        df=df[df['Country Name']==name]

        df = df.set_index('Country Name').T
        df.columns =[f'{name}\'s fertility rate']
        df['Year']=df.index
        df=df[['Year',f'{name}\'s fertility rate']]
        df = df.reset_index(drop=True)

    else:
        print(f"expected type p for population or f for fertility rate: '{type}' not recognized")
        return
    return df


def visualize(df: pd.DataFrame, name: str, type: str, start_from_zero=False, plot_title: str=None) -> None:
    """The function is for reusable plotting"""
    """The type is for dataframe type wether population or fertility rate"""
    """ONLY USE WITH PREPARE FOR VISUAL FUNCTION"""
    if type =='p':
        if plot_title:
            title=plot_title
        else:
            title=name
        plt.figure(figsize=(16, 6))

        sns.lineplot(data=df, x='Year', y=f'{name}\'s Population', linewidth=2, color='DarkGreen',  linestyle='--')
        plt.title(f'{title}\'s Population by years (1960-2024)', fontsize=16, fontweight='bold')
        plt.xlabel('Years', fontsize=15, color='DarkRed', fontweight='bold')

        if start_from_zero:
            plt.ylim(bottom=0)

        plt.gcf().set_facecolor('Darkgray')
        sns.set_style('darkgrid') 

        plt.ylabel('Population',fontweight='bold', fontsize=15, color='DarkRed', rotation=0, loc='top')
        plt.xticks(range(1960, 2025, 5))

        plt.ticklabel_format(style='plain', axis='y')  

        plt.show()

    elif type == 'f':
        if plot_title:
            title=plot_title
        else:
            title=name
        plt.figure(figsize=(16, 6))

        sns.lineplot(data=df, x='Year', y=f'{name}\'s fertility rate', linewidth=2, color='DarkBlue',  linestyle='--')
        plt.title(f'{title}\'s fertility rate by years (1960-2024)', fontsize=16, fontweight='bold')
        plt.xlabel('Years', fontsize=15, color='DarkGreen', fontweight='bold')


        plt.gcf().set_facecolor('Darkgray')
        sns.set_style('darkgrid') 

        plt.ylabel('Population',fontweight='bold', fontsize=15, color='DarkGreen', rotation=0, loc='top')

        if start_from_zero:
            plt.ylim(bottom=0)

        plt.ticklabel_format(style='plain', axis='y')  

        plt.show()
    else:
        print(f"expected type p for population or f for fertility rate: '{type}' not recognized")