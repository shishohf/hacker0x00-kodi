# -*- coding: utf-8 -*-

import base64, sys
from six import ensure_text


def chk():
    return True

tmdb_key = ensure_text(base64.b64decode(b'NDYwYTcxY2Q4ODBkMTlhZWY3ZDM1MzQzMThlY2ZhZGU=')) if chk() else ''
tvdb_key = ensure_text(base64.b64decode(b'NjZkY2JlMTYtODFkYy00ZDllLWFmYTItNGYwYTA1OWQyZWY0')) if chk() else ''
omdb_key = ensure_text(base64.b64decode(b'N2VkNjI3Yzc=')) if chk() else ''
fanarttv_key = ensure_text(base64.b64decode(b'MDhkZWU5MmFiMTgzNDFmMzY0Yjk1Zjg1M2M4ZmQzZDU=')) if chk() else ''
yt_key = ensure_text(base64.b64decode(b'Y19QN0xsOHRHeWEwZ1RLRWFrZFZ4V1dOaW9QdzZfX3dEeVNheklB')) if chk() else ''
trakt_client_id = ensure_text(base64.b64decode(b'ZjMwZjg4NTE4MTFhMGNiNjIzNjhiODNiNWE4NTRkMmE5YzM5MmNkNTg5NjA1MGExZmQ0NjYxNWY0MThkOWJlMQ==')) if chk() else ''
trakt_secret = ensure_text(base64.b64decode(b'OGQ0MGU3YjcxZjkzODk0ODI5NmU2Y2IzOWQyOTBhMzg2OTIyOGFkZTg0YjQ2YTk1ODliOTlkZWNmOTc1NDg3ZA==')) if chk() else ''
orion_key = ensure_text(base64.b64decode(b'NFZOSDZMV1NNRDlQV1hNRDRCOE0yUUVCUUZUUTlGQzM=')) if chk() else ''
