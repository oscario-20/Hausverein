import pandas as pd
import helper_functions as hf


def main():
    """
    master script to create events from excel sheets
    :return:
    """

    # Read in the mail addresses from people subscribed
    mails = hf.read_mails('Addressliste.xlsx')
    print(mails)

    # Read in the tasks
    task_name = 'Aemtli.xlsx'
    task_df = pd.read_excel(task_name, sheet_name='Aufgaben1')
    task_df = task_df.set_index('Kalenderwoche')

    # Convert all tasks into one vectorized dataframe
    tasks = pd.DataFrame(columns=['start', 'end', 'task', 'description', 'apartment', 'recipients'])
    tasks['task'] = ['test', 'test', 'test']

    # Read in Task Descriptions
    description = pd.read_excel(task_name, sheet_name='Beschreibung')
    descriptions = dict(zip(description.Aufgabe, description.Aufgabenbeschreibung))

    # Generate a list of individual tasks

    # Setup the Google Calender API

    # Create individual calender events

    # Upload this to designated calender and send notifications


if __name__ == '__main__':
    main()
