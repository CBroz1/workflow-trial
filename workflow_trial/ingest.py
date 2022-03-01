import csv

from workflow_trial.pipeline import subject, session, trial


def ingest_general(csvs, tables,
                   skip_duplicates=True):
    """
    Inserts data from a series of csvs into their corresponding table:
        e.g., ingest_general(['./lab_data.csv', './proj_data.csv'],
                                 [lab.Lab(),lab.Project()]
    ingest_general(csvs, tables, skip_duplicates=True)
        :param csvs: list of relative paths to CSV files
        :param tables: list of datajoint tables with ()
    """
    for insert, table in zip(csvs, tables):
        with open(insert, newline='') as f:
            data = list(csv.DictReader(f, delimiter=','))
        prev_len = len(table)
        table.insert(data, skip_duplicates=skip_duplicates,
                     ignore_extra_fields=True)
        insert_len = len(table) - prev_len     # report length change
        print(f'\n---- Inserting {insert_len} entry(s) '
              + f'into {table.table_name} ----')


def ingest_subjects(subject_csv_path='./user_data/subjects.csv',
                    skip_duplicates=True):
    """
    Inserts data from a subject csv into corresponding subject schema tables
    By default, uses data from workflow_session/user_data/
    :param subject_csv_path:     relative path of subject csv
    :param skip_duplicates=True: datajoint insert function param
    """
    csvs = [subject_csv_path]
    tables = [subject.Subject()]
    ingest_general(csvs, tables, skip_duplicates=skip_duplicates)


def ingest_sessions(session_csv_path='./user_data/sessions.csv',
                    skip_duplicates=True):
    """
    Ingests to session schema from ./user_data/sessions.csv
    """
    # ingest to session schema
    csvs = [session_csv_path, session_csv_path, session_csv_path]
    tables = [session.Session(), session.SessionDirectory(),
              session.SessionNote()]

    ingest_general(csvs, tables, skip_duplicates=skip_duplicates)


def ingest_trials(trial_csv_path='./user_data/trials.csv',
                  event_csv_path='./user_data/events.csv',
                  skip_duplicates=True):
    """
    Ingests to trial schema from ./user_data/{trials/events}.csv
    """
    csvs = [trial_csv_path, event_csv_path]
    tables = [trial.Trial(), trial.Event()]
    ingest_general(csvs, tables, skip_duplicates=skip_duplicates)


if __name__ == '__main__':
    ingest_subjects()
    ingest_sessions()
    ingest_trials()
