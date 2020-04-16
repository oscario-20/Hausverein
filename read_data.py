import pandas as pd
import datetime



def read_data():
    """
    read data from two separate excel sheets and merge them to an iterable list
    return list with following entries:
    0 - task, 1 - name, 2 - description, 3 - start date, 4 - end date, 5 - attendees, 6 - reminders
    """


    aprt_name = 'wohnungen.xlsx'
    jobs_name = 'aemtli.xlxs'

    aprt_df = pd.read_excel(aprt_name)
    jobs_df = pd.read_excel(jobs_name)

    # Select the date row
    weeks = jobs_df.loc['Kalenderwoche', :]

    # TODO update this indices for the proper one when using the real excel sheet
    tasks = jobs_df.iloc[1:, 0]

    # TODO convert calender week to date, add different days for different task eg. Container
    # d = "2013-W26"
    # r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    # print(r)

    return [aprt_df, jobs_df]

read_data()