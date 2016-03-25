__author__ = 'klaatu'
from fabric.api import *
from fabric.colors import green

env.user = 'admin'
env.host_string = '159.203.120.218'
env.password = 'ascentperu'
home_path = "/home/admin"
settings = "--settings='gym.settings.production'"
activate_env = "source {}/gymvenv/bin/activate".format(home_path)
manage = "python manage.py"


def deploy():
    print("Beginning Deploy:")
    with cd("{}/gym".format(home_path)):
        run("git pull")
        run("{} && pip install -r requirements.txt".format(activate_env))
        run("{} && {} collectstatic --noinput {}".format(activate_env, manage,
                                                         settings))
        run("{} && {} migrate {}".format(activate_env, manage, settings))
        sudo("service nginx restart", pty=False)
        sudo("service supervisor restart", pty=False)
    print(green("Deploy deployment successful"))