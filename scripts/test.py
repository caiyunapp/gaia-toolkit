#!/usr/bin/env python

import cli.app

@cli.app.CommandLineApp
def test(app):
	pass

test.add_param("-c", "--cwd", help="current working directory")

if __name__ == "__main__":
	test.run()