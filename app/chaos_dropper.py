from rq import Queue
from redis import Redis
from app.harvest import extract_insight
import os

def chaos_from_file(path):
    q = Queue(connection=Redis())
    with open(path, 'r') as f:
        data = f.read()
    q.enqueue(extract_insight, data, path)