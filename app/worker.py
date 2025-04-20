from rq import Worker, Queue, Connection
import redis

redis_conn = redis.Redis()
queue = Queue(connection=redis_conn)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker([queue])
        worker.work()