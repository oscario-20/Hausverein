import pandas as pd


def read_mails(aprt_name):
    """
    read in list of people living in the house. Select addresses subscribed to the calender and asign them the id
    of the apartment.

    :return: dictionary of apartments and multiple corresponding mail addresses
    """

    # Read in the mail addresses from people subscribed
    aprt_df = pd.read_excel(aprt_name)

    # use apartment ID as index
    aprt_df = aprt_df.set_index('#')

    #  fill in merged cells
    aprt_df.index = pd.Series(aprt_df.index).fillna(method='ffill')

    # create a dictionary of list with mail addresses for individual apartments
    mails = {}

    for index, row in aprt_df.iterrows():
        index_str = str(index)

        if pd.isna(row['e-Mail']):
            continue

        if row['Hauskalender'] != 'ja':
            continue

        if index_str in mails:
            mails[index_str].append(row['e-Mail'])
        else:
            mails[index_str] = [row['e-Mail']]

    return mails
