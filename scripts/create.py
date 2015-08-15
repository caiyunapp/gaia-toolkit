#!/usr/bin/env python

import cli.app

@cli.app.CommandLineApp
def create(app):
	pass

create.add_param("-c", "--cwd", help="current working directory")
create.add_param("project_name", help="name of the project to create", default=1, type=str)

if __name__ == "__main__":
	create.run()