from app import factory
import os
import sys

app_root = os.environ.get('APP_ROOT')
sys.path.append(app_root)

application = factory(os.environ.get('CASAPLANNER_CONFIG', 'DefaultConfig'))
