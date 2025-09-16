(import json)
(import os)

(import dotenv [load-dotenv])
(import requests)


;;; api keys from dotenv
(load-dotenv)
(setv MIGADU_DOMAIN (os.getenv "MIGADU_DOMAIN"))
(setv MIGADU_USER (os.getenv "MIGADU_USER"))
(setv MIGADU_KEY (os.getenv "MIGADU_KEY"))
(setv AUTH #(MIGADU_USER MIGADU_KEY))

;;; utility functions
(defn print-as-json [jsonable]
  (print
    (json.dumps
      jsonable
      :indent 2)))

(setv r (requests.get f"https://api.migadu.com/v1/domains/{MIGADU_DOMAIN}/aliases" :auth AUTH))
(print-as-json (.json r))
