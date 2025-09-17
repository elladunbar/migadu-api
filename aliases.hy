(import json)
(import os)

(import dotenv [load-dotenv])
(import requests)


(setv HEADERS {"Content-Type" "application/json"})
;;; api keys from dotenv
(load-dotenv)
(setv MIGADU_DOMAIN (os.getenv "MIGADU_DOMAIN"))
(setv MIGADU_USER (os.getenv "MIGADU_USER"))
(setv MIGADU_KEY (os.getenv "MIGADU_KEY"))
;;; derived
(setv URL (+ "https://api.migadu.com/v1/domains/" MIGADU_DOMAIN "/aliases"))
(setv AUTH #(MIGADU_USER MIGADU_KEY))
(setv data {"destinations" (+ "me@" MIGADU_DOMAIN)})

;;; utility functions
(defn print-as-json [jsonable]
  (print
    (json.dumps
      jsonable
      :indent 2)))

;;; read and create aliases
(with [f (open "needed_aliases.txt" "r")]
  (setv needed-aliases (tuple (map (fn [l] (.strip l)) (.readlines f)))))
(for [needed-alias needed-aliases]
  (setv (get data "local_part") needed-alias)
  (setv response (requests.post URL :auth AUTH :json data :headers HEADERS))
  (when (!= (. response status_code) 200)
    (print (.json response))))
