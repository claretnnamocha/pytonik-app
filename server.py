from pytonik import serv
import os

port = int(os.environ.get("PORT", 5000))
serv.run(host="", path="", port=port)