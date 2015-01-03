# -*- encoding=utf-8 -*-
# call4paper - a Flask powered session scheduling server
# Copyright © Jean-Baptiste Lievremont <mithfindel@gmail.com>
#
# This file is part of call4paper.
#
# call4paper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# call4paper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with call4paper.  If not, see <http://www.gnu.org/licenses/>.

import argparse
from flask import Flask
from flask.templating import render_template
import os


app = Flask(__name__)
 
@app.route("/")
def index():
  return render_template("index.html")
 
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = "Start session scheduling server")
  parser.add_argument("-D", "--debug", dest="debug", action="store_true",
                      help="Enable Web debug mode - not for production!")
  parser.add_argument("-p", "--port", dest="port", type=int,
                      help="Port to listen on")

  port_from_env = 6942
  try:
    port_from_env = int(os.environ['PORT'])
  except:
    # Swallow silently
    app.logger.debug("No port from environment, use default port")

  parser.set_defaults(debug=False, port=port_from_env or 6942)

  args = parser.parse_args()
  app.run(debug=args.debug, port=args.port, host=("127.0.0.1" if args.debug else "0.0.0.0"))
