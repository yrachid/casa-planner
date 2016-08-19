from app import factory
import os

application = factory(os.environ.get('CASAPLANNER_CONFIG', 'DefaultConfig'))
