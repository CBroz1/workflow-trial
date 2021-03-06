import datajoint as dj

from element_lab import lab
from element_animal import subject
from element_session import session
from element_trial import trial, event

from element_animal.subject import Subject
from element_lab.lab import Source, Lab, Protocol, User, Project
from element_session.session import Session

if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')

__all__ = ['Subject', 'Source', 'Lab', 'Protocol', 'User', 'Project', 'Session',
           'trial', 'event']


# Activate "lab", "subject", "session" schema -------------

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + 'session', linking_module=__name__)

# Activate "trial" and "event" schemas --------------------------------

trial.activate(db_prefix + 'trial', linking_module=__name__)
event.activate(db_prefix + 'event', linking_module=__name__)
