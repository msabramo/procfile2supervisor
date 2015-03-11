#!/usr/bin/env python

import pkg_resources
import subprocess

import click


@click.command()
@click.version_option()
@click.option('-a', '--app',
              default=None,
              help='app name')
def main(app):
    """Convert Procfile to supervisor config file"""
    click.echo('app = %r' % app)
    # honcho export --template-dir=. --user=profilesvcuser --app=profilesvc supervisord --log=/var/log/sm . && cat profilesvc.conf
    template_dir = pkg_resources.resource_filename('procfile2supervisor', None)
    click.echo('template_dir = %r' % template_dir)
    # cmd = 'honcho export --template-dir=. --user=profilesvcuser --app=profilesvc supervisord --log=/var/log/sm .'
    cmd = ['honcho', 'export']
    # return pkg_resources.resource_filename('smstack', None)
    cmd.append('--template-dir=%s' % template_dir)
    cmd.append('--user=profilesvcuser')
    cmd.append('--app=profilesvc')
    cmd.append('supervisord')
    cmd.append('--log=/var/log/sm')
    cmd.append('.')
    status = subprocess.call(cmd)


if __name__ == '__main__':
    main()
