from app import factory
import os
import sys

app_root = os.environ.get('APP_ROOT')
sys.path.insert(0, app_root)

sys.stdout = sys.stderr

application = factory(os.environ.get('CASAPLANNER_CONFIG', 'DefaultConfig'))
